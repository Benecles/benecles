#!/usr/bin/env python3
"""Prepare staged ship requests and ship only Claude-approved work."""
from __future__ import annotations

import fcntl
import base64
import errno
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path, PurePosixPath

ROOT = Path("/Users/benecles/Documents/Codex/2026-09-23/you-h/work")
PROGRAM = ROOT / "program"
R = ROOT / "relay-design-2026-09-29"
SHIPS = PROGRAM / "ships"
PUBLISH = Path("/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish")
NODE = Path("/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node")
COPY_RETRIES = 3


def run(args: list[str], *, cwd: Path, env: dict[str, str] | None = None, log=None):
    result = subprocess.run(args, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log:
        log.write(result.stdout)
        log.flush()
    if result.returncode:
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(map(str, args))}\n{result.stdout[-3000:]}")
    return result.stdout


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def safe_rel(raw: str) -> str:
    p = PurePosixPath(raw)
    if not raw or p.is_absolute() or any(x in ("", ".", "..") for x in p.parts):
        raise ValueError(f"unsafe relative path: {raw!r}")
    return str(p)


def is_site_content_rel(rel: str) -> bool:
    """Allow only paths the live site serves; reject staging and curation data."""
    parts = PurePosixPath(rel).parts
    if not parts or parts[0] in {"curation", "program", "tools", ".git"}:
        return False
    return len(parts) == 1 or parts[0] in {"courses", "assets"}


def validate_copyset_paths(src: Path, dst: Path, files: list[str], *, staged_ok: bool = False):
    if not (inside(src, R / "site") or (staged_ok and inside(src, SHIPS / "staged"))):
        raise ValueError(f"SHIPCOPY source must be site content or its frozen ship snapshot: {src}")
    if not inside(dst, PUBLISH):
        raise ValueError(f"SHIPCOPY destination must be in publish checkout: {dst}")
    for rel in files:
        full = (dst / rel).relative_to(PUBLISH).as_posix()  # judge the path from the site root, not the copyset root (30/09)
        if not is_site_content_rel(full):
            raise ValueError(f"SHIPCOPY path is not site content: {full}")


def copy2_with_icloud_retry(src: Path, dst: Path, *, retry_limit: int = COPY_RETRIES, run_command=run):
    """Retry transient iCloud EAGAIN reads, asking File Provider to download this exact file."""
    for attempt in range(retry_limit):
        try:
            return shutil.copy2(src, dst)
        except OSError as exc:
            if exc.errno != errno.EAGAIN or attempt + 1 >= retry_limit:
                raise
            run_command(["brctl", "download", str(src)], cwd=src.parent)


def queue_rows():
    rows = []
    for line in (PROGRAM / "queue.tsv").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) >= 5:
            rows.append(cols[:5])
    return rows


def set_index(order: str, status: str, detail: str = ""):
    index = SHIPS / "INDEX.md"
    lines = index.read_text().splitlines() if index.exists() else ["# Ship requests"]
    entry = f"- {order} — {status}" + (f" — {detail}" if detail else "")
    prefix = f"- {order} —"
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(entry)
    index.write_text("\n".join(kept).rstrip() + "\n")


def resolve_gate(order: str) -> Path:
    order_file = PROGRAM / "orders" / f"{order}.md"
    if order_file.exists():
        for line in order_file.read_text(errors="replace").splitlines():
            if line.startswith("SHIP_GATE="):
                return Path(line.split("=", 1)[1].strip())
    return R / "program" / f"{order}-GATE.md"


def staging_only_gate(gate: Path) -> bool:
    """True when every declared ship-copy line explicitly says there are no site files."""
    copy_lines = [line.split(":", 1)[1].strip() for line in gate.read_text(errors="replace").splitlines()
                  if line.startswith("SHIPCOPY:")]
    return bool(copy_lines) and all(re.match(r"^N/A(?:\s|$)", value) for value in copy_lines)


def parse_shipcopies(gate: Path):
    changes = ""
    check = ""
    crops: list[str] = []
    copysets: list[tuple[str, str, str, list[str]]] = []
    for line in gate.read_text(errors="replace").splitlines():
        if line.startswith("SHIPCHANGE:"):
            changes = line.split(":", 1)[1].strip()
        elif line.startswith("SHIPCHECK:"):
            check = line.split(":", 1)[1].strip()
        elif line.startswith("SHIPCROP:"):
            crops.extend(x.strip() for x in line.split(":", 1)[1].split(",") if x.strip())
        elif line.startswith("SHIPCOPY:"):
            fields = [x.strip() for x in line.split(":", 1)[1].split("|")]
            if len(fields) != 4:
                raise ValueError(f"bad SHIPCOPY line in {gate}: {line}")
            files = [safe_rel(x.strip()) for x in fields[3].split(",") if x.strip()]
            if not files:
                raise ValueError(f"empty SHIPCOPY file list in {gate}")
            copysets.append((fields[0], fields[1], fields[2], files))
    if not changes or not check or not copysets:
        raise ValueError(f"{gate} needs SHIPCHANGE, SHIPCHECK, and one or more SHIPCOPY lines")
    return changes, check, crops[:3], copysets


def prepare(order: str, force: bool = False, quiet: bool = False):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", order):
        raise ValueError(f"invalid order id: {order}")
    status = (PROGRAM / "state" / f"{order}.status").read_text().strip() if (PROGRAM / "state" / f"{order}.status").exists() else ""
    if status != "done" and not force:
        raise ValueError(f"{order} has not passed its queue check (state: {status or 'missing'})")
    pending = SHIPS / "pending" / f"{order}.md"
    if pending.exists():
        print(f"already pending: {pending}")
        return
    no_ship = SHIPS / "done" / f"{order}.not-a-ship"
    if no_ship.exists():
        return
    gate = resolve_gate(order)
    if not gate.is_file() or not any(x.startswith("SHIPCOPY:") for x in gate.read_text(errors="replace").splitlines()):
        if not quiet:
            print(f"no staged live-file ship map for {order}; skipped")
        return
    if staging_only_gate(gate):
        no_ship.parent.mkdir(parents=True, exist_ok=True)
        no_ship.write_text(f"Staging-only order; no site files to ship. Gate: {gate}\n")
        set_index(order, "STAGING ONLY", str(gate))
        if not quiet:
            print(f"staging-only order; no ship request created: {order}")
        return
    changes, check, crops, copysets = parse_shipcopies(gate)
    file_list = []
    baseline_list = []
    rows = []
    frozen_root = SHIPS / "staged" / order
    for index, (src, dst, base, files) in enumerate(copysets, 1):
        srcp, dstp, basep = Path(src), Path(dst), Path(base)
        validate_copyset_paths(srcp, dstp, files)
        if (not inside(basep, R) and not inside(basep, SHIPS / "baselines")):
            raise ValueError(f"ship roots must stay in staging/publish checkouts: {src} | {dst} | {base}")
        frozen_set = frozen_root / f"set-{index:02d}"
        for rel in files:
            staged_file = srcp / rel
            frozen_file = frozen_set / rel
            if not staged_file.is_file():
                raise ValueError(f"missing staged file: {staged_file}")
            frozen_file.parent.mkdir(parents=True, exist_ok=True)
            if frozen_file.exists():
                if not __import__("filecmp").cmp(staged_file, frozen_file, shallow=False):
                    raise ValueError(f"immutable ship snapshot differs; refusing to replace: {frozen_file}")
            else:
                shutil.copy2(staged_file, frozen_file)
            file_list.append(f"{dstp / rel}")
            baseline_list.append(f"{basep / rel}")
        rows.append(f"COPYSET\t{frozen_set}\t{dstp}\t{basep}\t{','.join(files)}")
    check_text = check if check.startswith("PASS") else f"PASS — {check}"
    lines = [
        f"# Ship request — {order}",
        f"Changes: {changes}",
        f"Check: {check_text}; runner output: {PROGRAM / 'logs' / f'{order}.check.txt'}",
        f"Files: {', '.join(file_list)}",
        f"Crops: {', '.join(crops) if crops else '(none supplied)'}",
        f"Pre-edit baselines: {', '.join(baseline_list)}",
        f"Gate: {gate}",
        *rows,
    ]
    if len(lines) > 25:
        raise ValueError(f"ship request would exceed 25 lines ({len(lines)})")
    pending.parent.mkdir(parents=True, exist_ok=True)
    pending.write_text("\n".join(lines) + "\n")
    set_index(order, "PENDING", str(gate))
    print(f"prepared {pending}")


def prepare_done_orders():
    for row in queue_rows():
        order = row[0]
        state = PROGRAM / "state" / f"{order}.status"
        if not state.exists() or state.read_text().strip() != "done":
            continue
        if (SHIPS / "done" / f"{order}.not-a-ship").exists():
            continue
        if any((SHIPS / "done").glob(f"{order}.superseded*")):
            continue
        if (SHIPS / "pending" / f"{order}.md").exists() or (SHIPS / "done" / f"{order}.md").exists():
            continue
        if (SHIPS / "done" / f"{order}.rejected-request.md").exists() or (SHIPS / "rejected" / ".handled" / order).exists():
            continue
        if (SHIPS / "conflicts" / f"{order}.md").exists() or (SHIPS / "errors" / f"{order}.md").exists():
            continue
        try:
            prepare(order, quiet=True)
        except Exception as exc:
            with (SHIPS / "watcher.log").open("a") as f:
                f.write(f"{datetime.now().astimezone().isoformat()} prepare {order}: {exc}\n")


def parse_request(path: Path):
    copysets = []
    for line in path.read_text().splitlines():
        if line.startswith("COPYSET\t"):
            fields = line.split("\t")
            if len(fields) != 5:
                raise ValueError(f"bad COPYSET in {path}: {line}")
            src, dst, base = map(Path, fields[1:4])
            files = [safe_rel(x) for x in fields[4].split(",") if x]
            validate_copyset_paths(src, dst, files, staged_ok=True)
            if (not inside(base, R) and not inside(base, SHIPS / "baselines")):
                raise ValueError(f"unsafe ship roots in {path}")
            copysets.append((src, dst, base, files))
    if not copysets:
        raise ValueError(f"no COPYSET lines in {path}")
    return copysets


def git_status() -> str:
    return subprocess.run(["git", "status", "--porcelain"], cwd=PUBLISH, text=True, stdout=subprocess.PIPE, check=True).stdout


def git_changed_paths() -> list[str]:
    """Return every tracked or untracked path changed in the publish checkout."""
    raw = subprocess.run(
        ["git", "ls-files", "--modified", "--others", "--exclude-standard", "-z"],
        cwd=PUBLISH, stdout=subprocess.PIPE, check=True,
    ).stdout
    return [path.decode("utf-8", errors="surrogateescape") for path in raw.split(b"\0") if path]


def write_inbox_line(prefix: str, line: str):
    inbox = PROGRAM / "claude-inbox.md"
    existing = inbox.read_text().splitlines() if inbox.exists() else ["# Claude inbox"]
    if any(x.startswith(prefix) for x in existing):
        return
    if len(existing) >= 39:
        return
    existing.append(line)
    inbox.write_text("\n".join(existing).rstrip() + "\n")


def conflict(order: str, request: Path, conflicts: list[str]):
    folder = SHIPS / "conflicts"
    folder.mkdir(parents=True, exist_ok=True)
    report = folder / f"{order}.md"
    report.write_text(
        f"# Re-stage required — {order}\n\n"
        "The approved staging no longer matches its pre-edit baseline. Nothing was copied live. "
        "Re-stage this order on top of the current publish files, preserve unrelated live edits, rerun its gate and mechanical check, then request approval for the new baseline.\n\n"
        f"Request: {request}\n\n" + "\n".join(f"- {x}" for x in conflicts) + "\n"
    )
    approval = SHIPS / "approved" / order
    if approval.exists():
        target = folder / f"{order}.approval"
        if target.exists():
            target = folder / f"{order}.{int(time.time())}.approval"
        shutil.move(str(approval), str(target))
    set_index(order, "RE-STAGE", str(report))
    write_inbox_line(f"- {order} —", f"- {order} — baseline conflict; re-stage on top of live before approval: {report}")
    requests = PROGRAM / "claude-requests.md"
    line = (f"- Ship baseline conflict for {order}: read {report}; re-stage the approved changes on the current live baseline, "
            "preserve unrelated live edits, rerun the gate and original mechanical check, and request fresh approval (maximum two redo generations).")
    old = requests.read_text() if requests.exists() else ""
    if line not in old:
        with requests.open("a") as f:
            f.write(("\n" if old and not old.endswith("\n") else "") + line + "\n")


def write_error(order: str, request: Path, error: str):
    if "Errno 11" in error or "Resource deadlock avoided" in error:
        # iCloud file-provider contention (Documents syncs to iCloud): transient, so retry on a later loop instead of failing the ship (30/09)
        (SHIPS / "journal" / f"{order}.json").unlink(missing_ok=True)
        print(f"{order}: transient iCloud read error, will retry", file=sys.stderr)
        time.sleep(60)
        return
    folder = SHIPS / "errors"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{order}.md").write_text(f"# Ship failed — {order}\n\nRequest: {request}\n\n{error}\n")
    set_index(order, "ERROR", str(folder / f"{order}.md"))
    write_inbox_line(f"- {order} —", f"- {order} — ship pipeline error; inspect {folder / f'{order}.md'}")


def baton_log(order: str, summary: str, paths: list[str], commit: str):
    entry = (f"{datetime.now().astimezone().strftime('%Y-%m-%d')} — {order.upper()} SHIPPED — "
             f"commit {commit[:10]}. {summary} Files: {', '.join(paths)}. "
             "Checks passed: offline build, polish capture where applicable, and polish check.")
    temp = SHIPS / "logs" / f"{order}-baton.txt"
    temp.parent.mkdir(parents=True, exist_ok=True)
    temp.write_text(entry + "\n")
    run(["python3", str(R / "milestone.py"), str(temp)], cwd=ROOT)


def finish_ship(order: str, pending: Path, approval: Path, commit: str, summary: str, paths: list[str]):
    baton_log(order, summary, paths, commit)
    done = SHIPS / "done"
    done.mkdir(parents=True, exist_ok=True)
    shutil.move(str(pending), str(done / f"{order}.md"))
    (PROGRAM / "state" / f"ship:{order}.status").write_text("done\n")
    if approval.exists():
        shutil.move(str(approval), str(done / f"{order}.approved"))
    set_index(order, "SHIPPED", commit[:10])
    journal = SHIPS / "journal" / f"{order}.json"
    data = json.loads(journal.read_text())
    data.update(phase="done", commit=commit)
    journal.write_text(json.dumps(data, indent=2) + "\n")


def ship(order: str, approval: Path):
    pending = SHIPS / "pending" / f"{order}.md"
    if not pending.exists():
        return
    journal_dir = SHIPS / "journal"
    journal_dir.mkdir(parents=True, exist_ok=True)
    journal_path = journal_dir / f"{order}.json"
    journal = json.loads(journal_path.read_text()) if journal_path.exists() else None
    if journal and journal.get("phase") == "done":
        return
    if (SHIPS / "errors" / f"{order}.md").exists() or (SHIPS / "conflicts" / f"{order}.md").exists():
        return
    try:
        copysets = parse_request(pending)
        all_paths = [f"{dst / rel}" for _, dst, _, files in copysets for rel in files]
        html_paths = [str(Path(p).relative_to(PUBLISH)) for p in all_paths if p.lower().endswith((".html", ".htm"))]
        summary = next((x.split(":", 1)[1].strip() for x in pending.read_text().splitlines() if x.startswith("Changes:")), order)
        if not journal:
            status = (PROGRAM / "state" / f"{order}.status").read_text().strip() if (PROGRAM / "state" / f"{order}.status").exists() else ""
            if status != "done":
                raise ValueError(f"order state is not done: {status or 'missing'}")
            dirty = git_status()
            if dirty:
                raise ValueError(f"publish checkout is not clean before shipping:\n{dirty[:3000]}")
            issues = []
            for src, dst, base, files in copysets:
                for rel in files:
                    staged, live, baseline = src / rel, dst / rel, base / rel
                    if not staged.is_file():
                        issues.append(f"missing staged file: {staged}")
                    elif baseline.exists():
                        if not live.is_file() or staged.is_symlink() or baseline.is_symlink():
                            issues.append(f"baseline/live is not a regular file: {live} (baseline {baseline})")
                        elif not __import__("filecmp").cmp(live, baseline, shallow=False):
                            issues.append(f"live differs from baseline: {live} (baseline {baseline})")
                    elif live.exists():
                        issues.append(f"expected new destination to be absent: {live}")
            if issues:
                conflict(order, pending, issues)
                return
            preimages = {}
            for _, dst, _, files in copysets:
                for rel in files:
                    live = dst / rel
                    preimages[str(live)] = ("file:" + base64.b64encode(live.read_bytes()).decode("ascii")) if live.is_file() else "absent"
            journal = {"phase": "copying", "order": order, "paths": all_paths, "html_paths": html_paths,
                       "summary": summary, "preimages": preimages}
            journal_path.write_text(json.dumps(journal, indent=2) + "\n")
        if journal.get("phase") == "copying":
            issues = []
            for src, dst, base, files in copysets:
                for rel in files:
                    staged, live, baseline = src / rel, dst / rel, base / rel
                    if live.exists() and __import__("filecmp").cmp(staged, live, shallow=False):
                        continue
                    if baseline.exists():
                        if not live.is_file() or not __import__("filecmp").cmp(live, baseline, shallow=False):
                            issues.append(f"live changed during copy: {live}")
                    elif live.exists():
                        issues.append(f"new destination appeared during copy: {live}")
            if issues:
                conflict(order, pending, issues)
                return
            for src, dst, base, files in copysets:
                for rel in files:
                    live = dst / rel
                    if (src / rel).is_file() and live.exists() and __import__("filecmp").cmp(src / rel, live, shallow=False):
                        continue
                    live.parent.mkdir(parents=True, exist_ok=True)
                    copy2_with_icloud_retry(src / rel, live)
            journal["phase"] = "copied"
            journal_path.write_text(json.dumps(journal, indent=2) + "\n")
        if journal.get("phase") == "copied":
            (SHIPS / "logs").mkdir(parents=True, exist_ok=True)
            with (SHIPS / "logs" / f"{order}.log").open("a") as log:
                run(["python3", "tools/offline_build.py"], cwd=PUBLISH, log=log)
                if html_paths:
                    env = os.environ.copy()
                    env["POLISH_BASE"] = "HEAD"
                    run(["python3", "tools/polish.py", "capture", *html_paths], cwd=PUBLISH, env=env, log=log)
                run(["python3", "tools/polish.py", "check"], cwd=PUBLISH, log=log)
                # The checkout was required to be clean before this ship. Capture the
                # complete post-build delta so generated assetver restamps, the offline
                # manifest, and polish snapshots travel with the copied site files.
                # This list comes from this isolated ship's build/capture result.
                changed_paths = git_changed_paths()
                if not changed_paths:
                    raise RuntimeError("ship produced no publish-checkout changes")
                stage_paths = sorted(set(changed_paths) | {str(Path(p).relative_to(PUBLISH)) for p in all_paths})
                run(["git", "add", "--", *stage_paths], cwd=PUBLISH, log=log)
                msg = f"Ship {order}: {summary[:140]}"
                run(["git", "commit", "-m", msg, "-m", "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], cwd=PUBLISH, log=log)
                journal["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PUBLISH, text=True, stdout=subprocess.PIPE, check=True).stdout.strip()
                remaining = git_status()
                if remaining:
                    raise RuntimeError(
                        "publish checkout is not clean after ship commit; request left unarchived:\n"
                        f"{remaining[:3000]}"
                    )
            journal["phase"] = "committed"
            journal["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=PUBLISH, text=True, stdout=subprocess.PIPE, check=True).stdout.strip()
            journal_path.write_text(json.dumps(journal, indent=2) + "\n")
        if journal.get("phase") == "committed":
            with (SHIPS / "logs" / f"{order}.log").open("a") as log:
                run(["git", "push", "origin", "HEAD:main"], cwd=PUBLISH, log=log)
            journal["phase"] = "pushed"
            journal_path.write_text(json.dumps(journal, indent=2) + "\n")
        if journal.get("phase") == "pushed":
            finish_ship(order, pending, approval, journal["commit"], journal["summary"], journal["paths"])
            print(f"SHIPPED {order} {journal['commit'][:10]}")
    except Exception as exc:
        if journal and not journal.get("commit") and journal.get("preimages") and journal.get("phase") in {"copying", "copied", "error"}:
            for raw_path, snapshot in journal["preimages"].items():
                live = Path(raw_path)
                if not inside(live, PUBLISH):
                    continue
                if snapshot == "absent":
                    live.unlink(missing_ok=True)
                elif snapshot.startswith("file:"):
                    live.parent.mkdir(parents=True, exist_ok=True)
                    live.write_bytes(base64.b64decode(snapshot[5:]))
        write_error(order, pending, str(exc))
        journal = journal or {"order": order}
        journal["phase"] = "error"
        journal["error"] = str(exc)
        journal_path.write_text(json.dumps(journal, indent=2) + "\n")


def enqueue_curations():
    curation = R / "curation"
    if not curation.is_dir():
        return
    known = {row[0] for row in queue_rows()}
    for approval in sorted(curation.glob("APPROVED-*")):
        course = approval.name.removeprefix("APPROVED-")
        if not re.fullmatch(r"[a-z0-9-]+", course):
            continue
        order = f"curation-build-{course}"
        state = PROGRAM / "state" / f"{order}.status"
        if order in known or (state.exists() and state.read_text().strip() in ("done", "running", "blocked", "failed 2")):
            continue
        plans = [p for p in curation.iterdir() if p.is_file() and p.suffix.lower() in (".csv", ".md", ".json") and course in p.name and not p.name.startswith("APPROVED-")]
        if not plans:
            continue
        plan_lines = "\n".join(f"- {p}" for p in plans)
        gate = R / "program" / f"{order}-GATE.md"
        node = str(NODE)
        jank = f"{node} {R}/gates/jank.mjs --site {R}/site --course {course} --out {R}/program/{order}-jank.csv"
        check = f"python3 {R}/curation/check_build_{course}.py {course} && {jank} && test -s {gate}"
        brief = f"""ORDER {order} (token budget 900000)

Approval marker: {approval}
Approved plan inputs:
{plan_lines}

Implement the approved curation plan exactly. Work only in {R}/site and private staging evidence. Before editing, preserve every affected staged page in {R}/program-old/{order}/ using a never-overwrite copy. The plan alone controls which figure counts may change. Text outside figures must remain byte-for-byte unchanged except the plan's specified figure insertions/removals. Do not add content or unrelated polish.

Done-condition: implement every approved plan item; create `python3 {R}/curation/check_build_{course}.py {course}` so it checks the plan's exact figure-count allowances and verifies text outside figures against the preserved baselines; run it and the jank scanner (`{jank}`) with exit 0; write `{gate}` with changed paths, staging URLs, and machine-readable SHIPCHANGE, SHIPCHECK, SHIPCROP (1–3 crop paths), and SHIPCOPY lines. Keep the ship map limited to the exact changed live files and their pre-edit baselines.

Queue mechanical check command: {check}
"""
        (PROGRAM / "orders" / f"{order}.md").write_text(brief)
        # Serialize queue append with runner.sh's picker.
        start = time.monotonic()
        while True:
            try:
                (PROGRAM / ".pick").mkdir()
                break
            except FileExistsError:
                if time.monotonic() - start > 30:
                    raise TimeoutError(f"timed out waiting for {PROGRAM / '.pick'}")
                time.sleep(0.2)
        try:
            with (PROGRAM / "queue.tsv").open("a") as q:
                q.write(f"{order}\t-\t-\t{check}\tcuration-{course}\n")
        finally:
            (PROGRAM / ".pick").rmdir()
        known.add(order)
        print(f"queued approved curation: {course}")


def process_rejections():
    rejected = SHIPS / "rejected"
    handled = rejected / ".handled"
    handled.mkdir(parents=True, exist_ok=True)
    for reason in sorted(rejected.glob("*.md")):
        order = reason.stem
        match = re.fullmatch(r"(.+)-r([12])", order)
        base_order = match.group(1) if match else order
        marker = handled / order
        request = SHIPS / "pending" / f"{order}.md"
        if marker.exists() or not request.exists():
            continue
        redos = sorted((PROGRAM / "orders").glob(f"{base_order}-r*.md"))
        if len(redos) >= 2:
            write_inbox_line(f"- {base_order} — BLOCKED", f"- {base_order} — BLOCKED after two redo generations; ship rejection: {reason}")
            set_index(base_order, "BLOCKED", str(reason))
        else:
            claude_requests = PROGRAM / "claude-requests.md"
            generation = len(redos) + 1
            next_order = f"{base_order}-r{generation}"
            line = (f"- Ship rejection for {base_order}, redo generation {generation} (order {order}): read {reason}; "
                    f"create {next_order}, re-stage on the current live baseline, preserve unrelated live edits, address every reason, rerun the original check, and request fresh approval.")
            old = claude_requests.read_text() if claude_requests.exists() else ""
            if line not in old:
                with claude_requests.open("a") as f:
                    f.write(("\n" if old and not old.endswith("\n") else "") + line + "\n")
            set_index(order, "REJECTED", str(reason))
        if request.exists():
            archive = SHIPS / "done" / f"{order}.rejected-request.md"
            archive.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(request), str(archive))
        marker.write_text(str(reason) + "\n")


def watch():
    lock_path = SHIPS / ".watcher.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("ship watcher already running")
            return
        try:
            (SHIPS / "watcher.pid").write_text(f"{os.getpid()}\n")
        except OSError:
            pass  # pid file is informational only; a stale lock on it must not kill the watcher (EDEADLK seen 30/09)
        while True:
            try:
                for step in (enqueue_curations, prepare_done_orders, process_rejections):
                    try:
                        step()  # each step fails on its own; a prepare error must never block approvals (30/09)
                    except Exception as exc:
                        print(f"{step.__name__} error: {exc}", file=sys.stderr)
                for approval in sorted((SHIPS / "approved").iterdir()):
                    if approval.name.startswith("."):
                        continue
                    ship(approval.name, approval)
            except Exception as exc:
                with (SHIPS / "watcher.log").open("a") as f:
                    f.write(f"{datetime.now().astimezone().isoformat()} watcher error: {exc}\n")
            time.sleep(5)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "watch":
        watch()
    elif len(sys.argv) >= 3 and sys.argv[1] == "prepare":
        prepare(sys.argv[2], force="--force" in sys.argv[3:])
    else:
        print("usage: shipper.py watch | prepare <order> [--force]", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
