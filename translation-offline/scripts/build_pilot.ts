// Expands and lints the generated pilot files.
// Run: node scripts/build_pilot.ts [generated-dir] [out-dir]
// In:  pilot/generated/<exercise_id>.json (GENERATION_SPEC.md, with slots)
// Out: <out-dir>/<exercise_id>.json – the database shape (expanded sentences +
//      normalised form), and <out-dir>/_lint.json – every rule violation found.
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { expandSlots } from '../checker/slots.ts';
import { normalizeBasic } from '../checker/typedAnswer.ts';
import { checkTranslation, formsOf, MAX_FEEDBACK_CHARS, type ExerciseCheckData, type Level } from '../checker/offlineCheck.ts';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const inDir = process.argv[2] ?? join(ROOT, 'pilot', 'generated');
const outDir = process.argv[3] ?? join(ROOT, 'pilot', 'expanded');
mkdirSync(outDir, { recursive: true });
const WORDS = new Set(readFileSync(join(ROOT, 'wordlist', 'en_words.txt'), 'utf8').split('\n').filter(Boolean));
const selection: any[] = JSON.parse(readFileSync(join(ROOT, 'pilot', 'selection.json'), 'utf8'));
const byId = new Map(selection.map((s) => [s.exercise_id, s]));

const MAX_COMBINATIONS = 96;
const GENDERED = /\b\p{L}+l[ao]?\s+(si|jsi)\b/iu;
const TRANSLATED_TENSE = /(\p{L}*(prítomn|přítomn|minul|budúc|budouc|predprítomn|předpřítomn|predminul|předminul)\p{L}*\s+(čas|času|časom|časem)|\b(trpn|činn)\p{L}*\s+rod|\bpriebehov|\bprůběhov|podmieňovac\p{L}*\s+spôsob|podmiňovac\p{L}*\s+způsob|\bneurčit(ok|ek|ku|kem|kom)\b|\bpríčasti|\bpříčest|\bgerundi(um|a|e))/iu;
const PRAISE = /(veta je správn|věta je správn|je to správn|\bdobre\b|\bvýborne\b|\bskvel|\bskvěl|\bsuper\b|\bwell done\b|\bgreat\b|\bgood job\b|\bnice\b|\bcorrect,? but\b|\bis correct\b|správne,? ale|správně,? ale)/iu;

type Issue = { exercise_id: number; rule: string; detail: string };
const issues: Issue[] = [];
const flag = (exercise_id: number, rule: string, detail: string) => issues.push({ exercise_id, rule, detail });

const forms = formsOf;
const stats: any[] = [];

for (const file of readdirSync(inDir).filter((f) => /^\d+\.json$/.test(f)).sort()) {
  const g = JSON.parse(readFileSync(join(inDir, file), 'utf8'));
  const id = g.exercise_id;
  const sel = byId.get(id);
  if (!sel) { flag(id, 'not_in_selection', file); continue; }
  for (const key of ['type_id', 'topic', 'level', 'sk', 'cz'] as const) if (g[key] !== sel[key]) flag(id, 'copied_field_changed', key);
  if (g.reference !== sel.en) flag(id, 'copied_field_changed', 'reference');
  const level: Level = sel.level;
  const isB = level === 'B1' || level === 'B2';

  const acceptable: string[] = [];
  for (const pattern of g.acceptable ?? []) {
    let expanded: string[] = [];
    try { expanded = expandSlots(pattern); } catch (e) { flag(id, 'slot_syntax', pattern); continue; }
    if (expanded.length > MAX_COMBINATIONS) flag(id, 'too_many_combinations', `${expanded.length}: ${pattern}`);
    for (const text of expanded) if (!acceptable.includes(text) && normalizeBasic(text) !== normalizeBasic(sel.en)) acceptable.push(text);
  }
  const acceptedForms = new Set<string>();
  for (const text of [sel.en, ...acceptable]) for (const f of forms(text)) acceptedForms.add(f);

  const mistakes: any[] = [];
  const mistakeForms = new Map<string, number>();
  if (!Array.isArray(g.mistakes) || g.mistakes.length < 3 || g.mistakes.length > 6) flag(id, 'mistake_count', String(g.mistakes?.length));
  (g.mistakes ?? []).forEach((m: any, index: number) => {
    let expanded: string[] = [];
    try { expanded = expandSlots(m.text); } catch { flag(id, 'slot_syntax', m.text); return; }
    if (expanded.length > MAX_COMBINATIONS) flag(id, 'too_many_combinations', `${expanded.length}: ${m.text}`);
    if (!['wrong', 'correct_with_tip'].includes(m.verdict)) flag(id, 'verdict_value', String(m.verdict));
    for (const lang of ['sk', 'cz', 'en'] as const) {
      const fb = m[`feedback_${lang}`];
      if (lang === 'en' && !isB) { if (fb !== null && fb !== undefined && fb !== '') flag(id, 'feedback_en_on_A_level', fb); continue; }
      if (typeof fb !== 'string' || !fb.trim()) { flag(id, 'feedback_missing', `${lang} #${index}`); continue; }
      if (fb.length > MAX_FEEDBACK_CHARS) flag(id, 'feedback_too_long', `${lang} ${fb.length}: ${fb}`);
      if (lang !== 'en' && GENDERED.test(fb)) flag(id, 'feedback_maybe_gendered', `${lang}: ${fb}`);
      if (lang !== 'en' && TRANSLATED_TENSE.test(fb)) flag(id, 'feedback_translated_grammar_name', `${lang}: ${fb}`);
      if (PRAISE.test(fb)) flag(id, 'feedback_praise', `${lang}: ${fb}`);
      if (normalizeBasic(fb).includes(normalizeBasic(sel.en))) flag(id, 'feedback_repeats_reference', `${lang}: ${fb}`);
    }
    for (const text of expanded) {
      for (const f of forms(text)) {
        if (acceptedForms.has(f)) flag(id, 'mistake_equals_acceptable', text);
        if (mistakeForms.has(f) && mistakeForms.get(f) !== index) flag(id, 'mistake_duplicate', text);
        mistakeForms.set(f, index);
      }
      mistakes.push({ text, normalized: normalizeBasic(text), kind: m.kind, verdict: m.verdict,
        feedback_sk: m.feedback_sk, feedback_cz: m.feedback_cz, feedback_en: isB ? m.feedback_en : null });
    }
  });

  // the checker must land every stored sentence in the intended step
  const data: ExerciseCheckData = { level, reference: sel.en, acceptable, mistakes };
  for (const text of acceptable) if (checkTranslation(text, data, 'sk', WORDS).verdict !== 'correct') flag(id, 'checker_rejects_acceptable', text);
  for (const m of mistakes) {
    const r = checkTranslation(m.text, data, 'sk', WORDS);
    if (r.step !== 'mistake' && !(r.verdict === 'correct')) flag(id, 'checker_misses_mistake', m.text);
  }

  const out = {
    exercise_id: id, type_id: sel.type_id, topic: sel.topic, level, reference: sel.en, sk: sel.sk, cz: sel.cz,
    acceptable: acceptable.map((text) => ({ text, normalized: normalizeBasic(text) })),
    mistakes,
    source_issues: g.source_issues ?? [],
  };
  const json = JSON.stringify(out);
  writeFileSync(join(outDir, file), JSON.stringify(out, null, 1));
  stats.push({ exercise_id: id, level, bench: sel.bench, acceptable_patterns: (g.acceptable ?? []).length, acceptable: acceptable.length,
    mistake_patterns: (g.mistakes ?? []).length, mistakes: mistakes.length, bytes: Buffer.byteLength(json),
    source_issues: (g.source_issues ?? []).length });
}

writeFileSync(join(outDir, '_lint.json'), JSON.stringify(issues, null, 1));
writeFileSync(join(outDir, '_stats.json'), JSON.stringify(stats, null, 1));
const byRule: Record<string, number> = {};
for (const i of issues) byRule[i.rule] = (byRule[i.rule] ?? 0) + 1;
console.log(JSON.stringify({ files: stats.length, issues: issues.length, byRule }));
