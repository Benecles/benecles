#!/usr/bin/env python3
"""restage.py <order>... — 3-way merge an approved-but-conflicted order onto current live:
for each COPYSET file where live != baseline: merge (baseline→staged) into live with git merge-file.
Clean merges rewrite the staged file and refresh the baseline to current live; conflicts are listed and left alone."""
import subprocess, sys, shutil, filecmp, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import shipper
S = shipper.SHIPS
for order in sys.argv[1:]:
    req = S / 'pending' / f'{order}.md'
    bad = 0
    for src, dst, base, files in shipper.parse_request(req):
        for rel in files:
            st, lv, bs = src / rel, dst / rel, base / rel
            if not bs.exists() or not lv.exists() or filecmp.cmp(lv, bs, shallow=False): continue
            with tempfile.NamedTemporaryFile(delete=False) as t: shutil.copy(lv, t.name)
            r = subprocess.run(['git', 'merge-file', '-p', str(st), str(bs), t.name], capture_output=True)
            if r.returncode == 0:
                st.write_bytes(r.stdout); shutil.copy(lv, bs); print(f'{order}: merged {rel}')
            else: print(f'{order}: CONFLICT {rel} ({r.returncode} hunks)'); bad += 1
    if not bad:
        for ext in ('md', 'approval'):
            c = S / 'conflicts' / f'{order}.{ext}'
            if ext == 'approval' and c.exists(): shutil.move(str(c), str(S / 'approved' / order))
            elif c.exists(): c.unlink()
        (S / 'journal' / f'{order}.json').unlink(missing_ok=True)
        print(f'{order}: re-staged cleanly')
