export const meta = {
  name: 'a45-translate',
  description: 'A45: native translations (8 languages) of the exercise texts of a batch, each with a grammar verifier',
  phases: [{ title: 'Translate' }, { title: 'Verify' }],
}
const RUN = '~/Projects/and-again-content/runs/a45_20261004'
const PAIRS = [['de', 'fr'], ['es', 'hu'], ['sk', 'cz'], ['ua', 'tr']]
const NAMES = { de: 'German', fr: 'French', es: 'Spanish', hu: 'Hungarian', sk: 'Slovak', cz: 'Czech', ua: 'Ukrainian', tr: 'Turkish' }
const items = args.batches.flatMap(b => PAIRS.map(p => ({ b, p })))
const res = await pipeline(
  items,
  it => agent(`Read ${RUN}/TR_BRIEF.md and follow it exactly. Batch: ${it.b}. Your languages: ${it.p.map(c => c + ' (' + NAMES[c] + ')').join(' and ')}. Write ${RUN}/tr/${it.b}/<code>.json for each, one language after the other, and run tr_check.py for each. Any helper file you create must have the batch and language code in its name. Reply only with the lines the brief asks for.`, { label: `tr ${it.b} ${it.p.join('+')}`, phase: 'Translate' }),
  (r, it) => parallel(it.p.map(c => () => agent(`Read ${RUN}/TR_VERIFY_BRIEF.md and follow it exactly. Batch: ${it.b}. Your language: ${c} (${NAMES[c]}). Any helper file you create must have the batch and language code in its name. Reply only with the line the brief asks for.`, { label: `verify ${it.b} ${c}`, phase: 'Verify' })))
)
return res.map((r, i) => ({ batch: items[i].b, langs: items[i].p, verify: r }))