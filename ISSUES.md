# Issues shipped

One line per merged issue: number · date · what changed · the check that proves it.

- **#0** · 30/09 · Front generator + gates moved into `tools/`; fronts regenerate byte-identical to live (drawings kept verbatim, unapproved Processo railway dropped, stale front.css cache stamp fixed) · `tools/check_all.sh` PASS, FAILs on a changed data file.
- **REG-6** · 30/09 · Contratos class-register data: a `does` line per lesson (what it lets you do) + exam coverage · `check_register_data.py` PASS, `check_all` PASS (no live change).
