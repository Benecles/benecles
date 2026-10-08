# Ship failed — main-pages-r1

Request: /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/pending/main-pages-r1.md

command failed (1): python3 tools/offline_build.py
Traceback (most recent call last):
  File "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/tools/offline_build.py", line 13, in <module>
    sanitize.run()   # no visible sourcing, whatever generated the page
  File "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/tools/sanitize.py", line 20, in run
    p = os.path.join(d, f); s = open(p).read(); s2 = sanitize(s)
OSError: [Errno 11] Resource deadlock avoided

