export const meta = {
  name: 'a57-batch',
  description: 'A57: one batch of 100 videos per language (de/es/fr): write, verify, fix, help translations, audio, validation, guarded write',
  phases: [{ title: 'Write' }, { title: 'Verify' }, { title: 'Rewrite' }, { title: 'Translate' }, { title: 'Finish' }],
}
const RUN = '~/Projects/and-again-content/runs/a57_20261006'
const LANGS = args.langs || ['de', 'es', 'fr']
const NAMES = { de: 'German (Germany)', es: 'Spanish (Spain)', fr: 'French (France)' }
const NATS = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
const NATNAME = { sk: 'Slovak', cz: 'Czech', en: 'English', de: 'German', es: 'Spanish (Spain)', fr: 'French (France)', hu: 'Hungarian', tr: 'Turkish', ua: 'Ukrainian' }
const G = args.group || 5
const VSCHEMA = { type: 'object', properties: { results: { type: 'array', items: { type: 'object', properties: {
  id: { type: 'integer' }, verdict: { type: 'string', enum: ['PASS', 'FIXED', 'FAIL'] }, changed: { type: 'integer' }, keyword: { type: 'string' } },
  required: ['id', 'verdict'] } } }, required: ['results'] }
const MECH = { type: 'object', properties: { ok: { type: 'boolean' }, summary: { type: 'string' } }, required: ['ok', 'summary'] }
const mech = (cmd, label, phase) => agent(`Mechanical step, no content decisions. In ${RUN}: ${cmd} Use a Bash timeout of at most 10 minutes per call; for anything longer start it in the background with nohup, redirect output to ${RUN}/logs/, and poll every few minutes until it ends. Return ok=true only if it finished without error, and summary = the last output line(s) (short).`, { label, phase, model: 'sonnet', schema: MECH })

async function oneLang(batch, lang, ids) {
  const groups = []
  for (let i = 0; i < ids.length; i += G) groups.push(ids.slice(i, i + G))
  const verdicts = await pipeline(groups,
    g => args.skipWrite ? 'skip' : agent(`Read ${RUN}/WRITER_BRIEF.md and follow it exactly. Language: ${lang} (${NAMES[lang]}). Your videos (media ids): ${g.join(', ')}. Skip any video whose content/${lang}/<id>.json exists already AND has a verdict file verify/${lang}/<id>.md. Reply only with the lines the brief asks for.`, { label: `write ${batch} ${lang} ${g[0]}`, phase: 'Write' }),
    (w, g) => agent(`Read ${RUN}/VERIFIER_BRIEF.md and follow it exactly. Language: ${lang} (${NAMES[lang]}). Your videos (media ids): ${g.join(', ')}. A video that already has verify/${lang}/<id>.md with PASS or FIXED and whose content file is not newer than it: keep that verdict, do not redo it. Return one result per video.`, { label: `verify ${batch} ${lang} ${g[0]}`, phase: 'Verify', schema: VSCHEMA }),
    async (v, g) => {
      const res = (v && v.results) || []
      const fails = g.filter(id => !res.find(r => r.id === id && r.verdict !== 'FAIL'))
      if (!fails.length) return { res, skipped: [] }
      await agent(`Read ${RUN}/WRITER_BRIEF.md. Language: ${lang} (${NAMES[lang]}). These videos FAILED independent verification: ${fails.join(', ')}. For each, read the verifier's notes in ${RUN}/verify/${lang}/<id>.md, then REWRITE content/${lang}/<id>.json from scratch following the brief, fixing every point raised (look at the drawn pictures again). Then rename verify/${lang}/<id>.md to verify/${lang}/<id>.first.md. Reply one line per video.`, { label: `rewrite ${batch} ${lang} ${fails[0]}`, phase: 'Rewrite' })
      const v2 = await agent(`Read ${RUN}/VERIFIER_BRIEF.md and follow it exactly (second verification after a rewrite; the first verifier's notes are in verify/${lang}/<id>.first.md). Language: ${lang} (${NAMES[lang]}). Your videos: ${fails.join(', ')}. Return one result per video.`, { label: `verify2 ${batch} ${lang} ${fails[0]}`, phase: 'Rewrite', schema: VSCHEMA })
      const r2 = (v2 && v2.results) || []
      const skipped = fails.filter(id => !r2.find(r => r.id === id && r.verdict !== 'FAIL'))
      return { res: res.filter(r => !fails.includes(r.id)).concat(r2), skipped }
    })
  const all = verdicts.filter(Boolean)
  const results = all.flatMap(x => x.res)
  const skipped = all.flatMap(x => x.skipped).concat(groups.filter((g, i) => !verdicts[i]).flat())
  if (skipped.length) await mech(`run: python3 -c "import json,os; p='data/skipped.json'; s=set(json.load(open(p))) if os.path.exists(p) else set(); s|={${skipped.map(i => `'${lang}:${i}'`).join(',')}}; json.dump(sorted(s),open(p,'w'))"`, `skip ${batch} ${lang}`, 'Rewrite')
  const src = await mech(`run: python3 trsource57.py ${batch} ${lang}`, `trsource ${batch} ${lang}`, 'Translate')
  const tr = await pipeline(NATS.filter(n => n !== lang),
    n => agent(`Read ${RUN}/TR_BRIEF.md and follow it exactly. Batch: ${batch}. Learning language: ${lang}. Your native language: ${n} (${NATNAME[n]}). Write tr/${batch}/${lang}/${n}.json (skip if it exists and tr_check57.py passes). Reply with one line.`, { label: `tr ${batch} ${lang}>${n}`, phase: 'Translate' }),
    (t, n) => agent(`Read ${RUN}/TR_VERIFY_BRIEF.md and follow it exactly. Batch: ${batch}. Learning language: ${lang}. Your native language: ${n} (${NATNAME[n]}). Reply with one line.`, { label: `trv ${batch} ${lang}>${n}`, phase: 'Translate' }))
  const fin = await mech(`run: python3 finish57.py ${batch} ${lang}  (records audio with macOS say; can take 10-20 minutes: run it in the background and poll; if it ends with videos failing only on "audio", run it once more).`, `finish ${batch} ${lang}`, 'Finish')
  const app = args.apply === false ? null : await mech(`run: bash apply_a57.sh ${batch}_${lang}  (uploads audio one file at a time and writes rows; can take several minutes: background + poll). Then run: python3 progress57.py "${batch} ${lang} done".`, `apply ${batch} ${lang}`, 'Finish')
  const cnt = v => results.filter(r => r.verdict === v).length
  return `${batch} ${lang}: PASS ${cnt('PASS')} FIXED ${cnt('FIXED')} FAIL ${cnt('FAIL')} skipped [${skipped.join(',')}] tr ${tr.filter(Boolean).length}/8 | ${(fin && fin.summary || 'no finish').slice(0, 160)} | ${(app && app.summary || 'no apply').slice(0, 160)}`
}
const out = []
for (const b of args.batches) {
  out.push(...(await parallel(LANGS.map(l => () => oneLang(b.batch, l, b.ids)))))
}
return out