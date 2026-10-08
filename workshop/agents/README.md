# Shared agent-status registry

Live coordination between Claude Code and Codex (Sol/Luna) on this Mac.

- **One file per orchestrating instance**, named for the runtime (`Claude1.md`, `Sol1.md`, `Luna1.md`). Create it from `STATUS_TEMPLATE.md` at the start of substantive work; update it at handoffs and scope changes; record the outcome and **delete it** when the run ends.
- **Subagents never create files here.** The orchestrator lists them in its own file.
- **Listed paths are claimed.** Don't write to another active instance's owned paths without coordinating (the Relay Baton at `~/Desktop/Relay Baton.md` is the place to hand work over).
- Keep files short. No credentials, tokens or personal data.
- Long-running project state, orders and history live in the Relay Baton, not here.
