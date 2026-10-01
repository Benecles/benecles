// chair: aids for the CEO of the Ordenações Filipinas project.
//  1. Context weather above the prompt; at 75% it says to hand over the chair (CEO.md gotcha:
//     long sessions balloon).
//  2. Merge guard: `gh pr merge N` needs a passed figure gate for PR N at its current head
//     (stamp written by work/checks/gate_prs.sh). Merging several PRs in a loop is refused too,
//     so each merge is checked by number.

const reading = { plugin: "chair", key: "reading" };
const BANDS = [
  { upTo: 40, icon: "☀", word: "Clear", color: "green" },
  { upTo: 60, icon: "☁", word: "Cloudy", color: "cyan" },
  { upTo: 75, icon: "☂", word: "Showers", color: "yellow" },
  { upTo: Infinity, icon: "☇", word: "Hand over the chair", color: "red" },
];

async function take($) {
  const { context } = await $.session.usage();
  if (!context?.window) return;
  const tokens = context.tokens ?? 0;
  const percent = context.percent ?? Math.round((tokens / context.window) * 100);
  await $.state.set(reading, { percent, tokens, window: context.window });
}

const k = (n) => (n >= 1e6 ? `${(n / 1e6).toFixed(2)}M` : `${Math.round(n / 1e3)}k`);

export function register(on) {
  on("session.start", async ($, e, next) => { const r = await next(e); await take($); return r; });
  on("turn.complete", async ($, e, next) => { const r = await next(e); if (!e.agentId) await take($); return r; });

  on("ui.render", { component: "AbovePrompt" }, async ($, e, next) => {
    const { value } = await $.state.get(reading);
    if (!value || e.props.hasSurvey) return next(e);
    const b = BANDS.find((x) => value.percent < x.upTo);
    const { Box, Text } = $.ui.resolve(e);
    return Box({ flexDirection: "row", paddingX: 1, children: [
      Text({ color: b.color, bold: true, children: `${b.icon}  ${b.word}` }),
      Text({ dimColor: true, children: `  ${value.percent}% of context · ${k(value.tokens)} / ${k(value.window)}` }),
    ] });
  });

  on("tool.call", { tool: "Bash" }, async ($, e, next) => {
    const cmd = e.command ?? "";
    if (!/\bgh\s+pr\s+merge\b/.test(cmd) || /ordenacoes-filipinas-workshop/.test(cmd)) return next(e);
    const nums = [...cmd.matchAll(/\bgh\s+pr\s+merge\s+(\d+)/g)].map((m) => m[1]);
    if (nums.length === 0 || /\bfor\b|\bxargs\b|\$\w+/.test(cmd)) {
      return { deny: "chair: merge site PRs one at a time with a literal number (gh pr merge 41), so the gate stamp can be checked for each." };
    }
    const home = await $.env.get("HOME");
    for (const n of nums) {
      const stamp = await $.fs.read(`${home}/.cache/ordenacoes-gate/pr-${n}`).catch(() => null);
      if (!stamp) {
        return { deny: `chair: PR ${n} has no passed gate. Run ~/Developer/ordenacoes-filipinas-workshop/work/checks/gate_prs.sh ${n} first.` };
      }
    }
    return next(e);
  });
}
