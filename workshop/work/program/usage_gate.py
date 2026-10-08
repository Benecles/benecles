#!/usr/bin/env python3
"""Prints 'ok', 'sleep <seconds>' (5h window nearly full) or 'stop' (weekly nearly exhausted) from the newest Codex rate_limits."""
import glob, json, os, time, shutil
if shutil.disk_usage('/').free < 2 * 1024**3:  # disk guard (30/09): below 2 GB free, sleep instead of filling the disk
    print('sleep 1800'); raise SystemExit
fs = sorted(glob.glob(os.path.expanduser('~/.codex/sessions/2026/*/*/*.jsonl')), key=os.path.getmtime)[-20:]
rl = None
for f in fs:
    for l in open(f, errors='ignore'):
        if '"rate_limits"' in l:
            try: r = json.loads(l)['payload'].get('rate_limits')
            except Exception: continue
            if r and r.get('secondary'): rl = r
if not rl: print('ok'); raise SystemExit
if rl['secondary']['used_percent'] >= 97: print('stop'); raise SystemExit
if rl['primary']['used_percent'] >= 90: print('sleep', max(60, int(rl['primary']['resets_at'] - time.time()) + 90)); raise SystemExit
print('ok')
