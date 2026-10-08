# Workshop

The pipeline behind the courses: the rules, the checks, the briefs agents work from, and the records each run leaves. Source texts are not here; `work/pipeline/*/shelf.csv` and `triage.csv` record what each source was and which lesson used it.

| Folder | What it holds |
|---|---|
| `protocols/` | Writing Standard, Design Direction, Visual Genres, Source Pipeline, House Manual; `protocols/tools/` has the prose and marks linters with tests |
| `work/pipeline/` | Per course: shelf, triage, course map, and per lesson a blueprint and its panel review; `work/pipeline/tools/` builds and checks them |
| `work/briefs/` | Briefs written for the agents (what to build, how it should look, what it must never do) |
| `work/house-style/` | House-style and quotation checks, and the ship script |
| `work/slop-bench/` | The prose-linter backtest against human legal doctrine |
| `work/*-build/`, `work/figure-sheet/`, `work/latam-maps/` | Figure and page generators |
| `work/program/` | Orders, checks and ship journals from the parallel agent runs |
| `CEO.md`, `FLIGHT-LOG.md`, `BUGS.md`, `RUN-*.md`, `Relay Baton.md` | Handoffs, numbered gate lessons, the bug catalogue and run ledgers |

Paths inside these files sometimes point to the private checkout (`~/Developer/ordenacoes-filipinas-workshop`); here that is this folder.
