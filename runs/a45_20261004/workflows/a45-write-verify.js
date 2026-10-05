export const meta = {
  name: 'a45-write-verify',
  description: 'A45: write and independently verify exercise content per group of 4 videos',
  phases: [{ title: 'Write' }, { title: 'Verify' }],
}
const RUN = '~/Projects/and-again-content/runs/a45_20261004'
const groups = args.groups || args.g.map(ids => ({ ids, write: true }))
const results = await pipeline(
  groups,
  g => g.write
    ? agent(`Read ${RUN}/WRITER_BRIEF.md and follow it exactly. Your videos (media ids): ${g.ids.join(', ')}. Write content/<id>.json for each, run draw.py for each and look at the drawn pictures as the brief says. Reply only with the lines the brief asks for.`, { label: `write ${g.ids[0]}`, phase: 'Write' })
    : 'already written',
  (w, g) => agent(`Read ${RUN}/VERIFIER_BRIEF.md and follow it exactly. Your videos (media ids): ${g.ids.join(', ')}. Reply only with the lines the brief asks for.`, { label: `verify ${g.ids[0]}`, phase: 'Verify' })
)
return results.map((r, i) => ({ ids: groups[i].ids, verify: r }))