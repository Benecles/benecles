#!/usr/bin/env python3
"""Isolated shipper safety checks; all checkout paths are temporary fixtures."""
from __future__ import annotations

import errno
import importlib.util
import tempfile
from pathlib import Path

SHIPPER_PATH = Path(__file__).resolve().parents[1] / "ships" / "shipper.py"
spec = importlib.util.spec_from_file_location("shipper_under_test", SHIPPER_PATH)
shipper = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(shipper)


def check_path_policy(tmp: Path):
    relay = tmp / "relay"
    publish = tmp / "publish"
    staged = tmp / "ships" / "staged" / "example"
    (relay / "site" / "courses").mkdir(parents=True)
    (relay / "curation").mkdir()
    publish.mkdir()
    staged.mkdir(parents=True)
    shipper.R, shipper.PUBLISH, shipper.SHIPS = relay, publish, tmp / "ships"

    try:
        shipper.validate_copyset_paths(relay / "site", publish, ["curation/plan.csv"])
    except ValueError:
        pass
    else:
        raise AssertionError("curation path was accepted as site content")
    try:
        shipper.validate_copyset_paths(relay, publish, ["courses/aula.html"])
    except ValueError:
        pass
    else:
        raise AssertionError("non-site source root was accepted")
    shipper.validate_copyset_paths(relay / "site", publish / "courses", ["aula.html"])
    shipper.validate_copyset_paths(staged, publish / "courses", ["aula.html"], staged_ok=True)


def check_bounded_download_retry(tmp: Path):
    tmp.mkdir(parents=True, exist_ok=True)
    source, target = tmp / "icloud-file", tmp / "copied-file"
    source.write_bytes(b"contents")
    original = shipper.shutil.copy2
    calls, downloads = [], []

    def flaky(src, dst):
        calls.append((Path(src), Path(dst)))
        if len(calls) < 3:
            raise OSError(errno.EAGAIN, "Resource temporarily unavailable")
        Path(dst).write_bytes(Path(src).read_bytes())
        return dst

    shipper.shutil.copy2 = flaky
    try:
        shipper.copy2_with_icloud_retry(source, target, retry_limit=3,
                                        run_command=lambda args, **kwargs: downloads.append(args))
    finally:
        shipper.shutil.copy2 = original
    assert len(calls) == 3, calls
    assert downloads == [["brctl", "download", str(source)]] * 2, downloads
    assert target.read_bytes() == b"contents"

    calls.clear()
    def always_fails(src, dst):
        calls.append(1)
        raise OSError(errno.EAGAIN, "Resource temporarily unavailable")
    shipper.shutil.copy2 = always_fails
    try:
        try:
            shipper.copy2_with_icloud_retry(source, target, retry_limit=3,
                                            run_command=lambda args, **kwargs: downloads.append(args))
        except OSError as exc:
            assert exc.errno == errno.EAGAIN
        else:
            raise AssertionError("retry limit did not fail")
    finally:
        shipper.shutil.copy2 = original
    assert len(calls) == 3, calls


def check_failure_rollback(tmp: Path):
    relay, publish, ships = tmp / "relay", tmp / "publish", tmp / "ships"
    site, live = relay / "site", publish / "courses"
    staged = ships / "staged" / "order" / "set-01"
    for path in (site / "courses", live, staged, ships / "pending", ships / "journal", ships / "approved"):
        path.mkdir(parents=True, exist_ok=True)
    (site / "courses" / "changed.html").write_bytes(b"new bytes")
    (site / "courses" / "fresh.html").write_bytes(b"new file")
    (staged / "changed.html").write_bytes(b"new bytes")
    (staged / "fresh.html").write_bytes(b"new file")
    original_owned = live / "changed.html"
    original_owned.write_bytes(b"exact old bytes\x00\xff")
    unrelated = publish / "unrelated.txt"
    unrelated.write_bytes(b"leave me")
    baseline = relay / "baseline"
    baseline.mkdir()
    (baseline / "changed.html").write_bytes(original_owned.read_bytes())
    # A missing baseline represents the expected-new destination.
    request = ships / "pending" / "order.md"
    request.write_text("Changes: simulated\nCOPYSET\t" + str(staged) + "\t" + str(live) + "\t" +
                       str(baseline) + "\tchanged.html,fresh.html\n")
    (tmp / "state").mkdir()
    (tmp / "state" / "order.status").write_text("done\n")

    shipper.R, shipper.PUBLISH, shipper.SHIPS = relay, publish, ships
    shipper.PROGRAM = tmp
    shipper.git_status = lambda: ""
    original_run = shipper.run
    def fail_build(args, **kwargs):
        if any("offline_build.py" in str(arg) for arg in args):
            # Simulate unrelated concurrent work during the attempted ship.
            unrelated.write_bytes(b"concurrent edit")
            raise RuntimeError("simulated offline build failure")
        return original_run(args, **kwargs)
    shipper.run = fail_build
    try:
        shipper.ship("order", ships / "approved" / "order")
    finally:
        shipper.run = original_run
    assert original_owned.read_bytes() == b"exact old bytes\x00\xff"
    assert not (live / "fresh.html").exists()
    assert unrelated.read_bytes() == b"concurrent edit"


def main():
    with tempfile.TemporaryDirectory(prefix="ship-pipeline-check-") as raw:
        tmp = Path(raw)
        check_path_policy(tmp / "paths")
        check_bounded_download_retry(tmp / "retry")
        check_failure_rollback(tmp / "rollback")
    print("ship pipeline checks passed")


if __name__ == "__main__":
    main()
