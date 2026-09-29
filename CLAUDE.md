# Notes for coding agents

Before changing anything in this repository, read the Relay Baton (the shared handoff between Claude Code, Codex and cloud sessions) and the agent registry it points to. They say who owns what, what is in progress and what must not be redone.

- Work that happens in Claude Code **cloud** sessions is mirrored in the private repository `benecles/study-lab-private` (same home-relative paths as the owner's Mac, text only). Its copy of the baton has the cloud session's entries at the top of the live log; bring them into the Mac baton before starting new work.
- Fixes may arrive on `claude/*` branches before they reach `main`. Check open branches before publishing.
- After adding or changing any page, run `python3 tools/offline_build.py`; after hand-editing generated pages, run `python3 tools/polish.py capture` and then `python3 tools/polish.py check`.
