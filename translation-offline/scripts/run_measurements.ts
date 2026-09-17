// Part E1 (coverage) and E2 (bench answers vs gemini-3.7-flash) on the expanded pilot data.
// Run: node scripts/run_measurements.ts
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { checkTranslation, type ExerciseCheckData } from '../checker/offlineCheck.ts';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const WORDS = new Set(readFileSync(join(ROOT, 'wordlist', 'en_words.txt'), 'utf8').split('\n').filter(Boolean));
const load = (id: number): ExerciseCheckData & { raw: any } => {
  const raw = JSON.parse(readFileSync(join(process.env.EXPANDED ?? join(ROOT, 'pilot', 'expanded'), `${id}.json`), 'utf8'));
  return { raw, level: raw.level, reference: raw.reference, acceptable: raw.acceptable.map((a: any) => a.text), mistakes: raw.mistakes };
};

// E2 – bench
const GEMINI_37: Record<number, string> = { 1: 'correct', 2: 'wrong', 3: 'correct_with_tip', 4: 'wrong', 5: 'wrong', 6: 'wrong', 7: 'wrong',
  8: 'correct_with_tip', 9: 'correct_with_tip', 10: 'wrong', 11: 'correct', 12: 'wrong', 13: 'wrong', 14: 'wrong', 15: 'correct_with_tip',
  16: 'wrong', 17: 'wrong', 18: 'wrong', 19: 'wrong', 20: 'correct' };
const bench = JSON.parse(readFileSync(join(process.env.HOME!, 'Projects/and-again/scripts/translation-bench/cases.json'), 'utf8'));
const benchOut = bench.map((c: any) => {
  const data = load(c.exercise_id);
  const r = checkTranslation(c.answer, data, 'sk', WORDS);
  return { id: c.id, exercise_id: c.exercise_id, level: c.level, topic: c.topic, category: c.category, answer: c.answer,
    offline: r.verdict, step: r.step, feedback_sk: r.feedback, gemini_37: GEMINI_37[c.id], agree: r.verdict === GEMINI_37[c.id],
    feedback_cz: checkTranslation(c.answer, data, 'cz', WORDS).feedback, feedback_other: checkTranslation(c.answer, data, 'de', WORDS).feedback };
});
writeFileSync(join(ROOT, 'measurements', (process.env.TAG ?? '') + 'bench_comparison.json'), JSON.stringify(benchOut, null, 1));
console.log('bench agree', benchOut.filter((b: any) => b.agree).length, '/', benchOut.length);

// E1 – coverage
const covPath = join(ROOT, 'measurements', 'coverage_translations.json');
if (existsSync(covPath)) {
  const cov = JSON.parse(readFileSync(covPath, 'utf8'));
  const rows: any[] = [];
  for (const item of cov) {
    const data = load(item.exercise_id);
    for (const t of item.translations) {
      const r = checkTranslation(t, data, 'sk', WORDS);
      rows.push({ exercise_id: item.exercise_id, level: data.level, topic: data.raw.topic, reference: data.reference, sk: data.raw.sk,
        translation: t, verdict: r.verdict, step: r.step, feedback_sk: r.feedback, closest: r.closest });
    }
  }
  writeFileSync(join(ROOT, 'measurements', (process.env.TAG ?? '') + 'coverage_results.json'), JSON.stringify(rows, null, 1));
  const count = (v: string) => rows.filter((r) => r.verdict === v).length;
  console.log('coverage', rows.length, 'correct', count('correct'), 'with_tip', count('correct_with_tip'), 'wrong', count('wrong'),
    'steps', JSON.stringify(rows.reduce((a: any, r) => ((a[r.step] = (a[r.step] ?? 0) + 1), a), {})));
}
