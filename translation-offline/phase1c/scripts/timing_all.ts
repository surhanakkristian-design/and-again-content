// Phase 1c §6.4: worst-case matching time over ALL annotated exercises (ANN_DIR), many runs.
//   ANN_DIR=… SYN_DIR=… LIB_OVERLAY=… node phase1c/scripts/timing_all.ts <out.json> [answersPerExercise=600] [runs=5]
// Per exercise: real answers from phase1c/inputs (cov_heldout, supp_all, fa) + synthetic answers (same generator as measure.ts timing:
// path / near_miss / near_miss2 / shuffle / long(80 tok) / long_repeat(120 tok)). Each answer is checked `runs` times; first run = cold (compile cached).
import { writeFileSync, readFileSync } from 'node:fs';
import { performance } from 'node:perf_hooks';
import { graphSize, type Graph } from '../../checker/v2/match.ts';
import { check } from '../../checker/v2/check.ts';
import { annotationIds, compiler } from '../../phase1b/scripts/data.ts';

const [out, perEx = '600', runsArg = '5'] = process.argv.slice(2);
const N = +perEx, RUNS = +runsArg;
const c = compiler();
const real: Record<number, string[]> = {};
for (const f of ['cov_heldout', 'supp_all', 'fa']) {
  const d = JSON.parse(readFileSync(new URL(`../inputs/${f}.json`, import.meta.url), 'utf8'));
  for (const it of Array.isArray(d) ? d : d.items ?? d.translations ?? []) {
    const id = Number(it.exercise_id ?? it.id);
    for (const t of it.translations ?? it.items ?? []) (real[id] ??= []).push(typeof t === 'string' ? t : t.text ?? t.answer);
  }
}
const stats = (xs: number[]) => { const s = [...xs].sort((a, b) => a - b); const q = (p: number) => s[Math.min(s.length - 1, Math.floor(p * s.length))];
  return { n: s.length, mean: +(s.reduce((a, b) => a + b, 0) / s.length).toFixed(3), p50: +q(0.5).toFixed(3), p99: +q(0.99).toFixed(3), max: +s.at(-1)!.toFixed(3) }; };
let seed = 12345;
const rnd = () => ((seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648);
const pickOf = <T>(xs: T[]) => xs[Math.floor(rnd() * xs.length)];
const walk = (g: Graph) => { const o: string[] = []; let u = g.start, guard = 1000;
  while (u !== g.end && guard-- > 0) { const e = pickOf(g.edges[u]); if (!e) break; if (e.tok) o.push(e.tok); u = e.to; } return o; };
const all: number[] = [], warm: number[] = [], compileMs: number[] = [];
const per: any[] = [];
let worst = { ms: 0, id: 0, kind: '', text: '' };
for (const id of annotationIds()) {
  const t0 = performance.now(); const target = c.get(id); compileMs.push(performance.now() - t0);
  if (!target) continue;
  const vocab = [...new Set(target.variants.flatMap((v) => v.graphs.flatMap((g) => [...g.tokens])))];
  const answers = (real[id] ?? []).map((text) => ({ kind: 'real', text }));
  for (let i = 0; i < N; i++) {
    const v = pickOf([...target.variants, ...target.mistakes]); const toks = walk(pickOf(v.graphs));
    const kind = ['path', 'near_miss', 'near_miss2', 'shuffle', 'long', 'long_repeat'][i % 6];
    if (kind.startsWith('near_miss')) for (let k = 0; k < (kind === 'near_miss' ? 1 : 3); k++) {
      const at = Math.floor(rnd() * (toks.length + 1)); const op = Math.floor(rnd() * 4);
      if (op === 0) toks.splice(at, 1); else if (op === 1) toks.splice(at, 0, pickOf(vocab));
      else if (op === 2 && toks[at]) toks[at] = toks[at].slice(0, -1) + 'x'; else if (toks[at + 1]) [toks[at], toks[at + 1]] = [toks[at + 1], toks[at]];
    } else if (kind === 'shuffle') toks.sort(() => rnd() - 0.5);
    else if (kind === 'long') while (toks.length < 80) toks.push(pickOf(vocab));
    else if (kind === 'long_repeat') { const base = [...toks]; while (base.length && toks.length < 120) toks.push(...base); }
    answers.push({ kind, text: toks.join(' ') });
  }
  const mine: number[] = [];
  for (let r = 0; r < RUNS; r++) for (const a of answers) {
    const t = performance.now(); check(a.text, target, { native: 'sk' }); const ms = performance.now() - t;
    all.push(ms); mine.push(ms); if (r > 0) warm.push(ms);
    if (ms > worst.ms) worst = { ms: +ms.toFixed(3), id, kind: a.kind, text: a.text.slice(0, 160) };
  }
  per.push({ id, graph_size: graphSize(target), answers: answers.length, ...stats(mine) });
}
per.sort((a, b) => b.max - a.max);
const res = { exercises: per.length, answers_per_exercise: N, runs: RUNS, checks: all.length, ms_all: stats(all), ms_warm_runs: stats(warm),
  compile_ms: stats(compileMs), worst, top10_by_max: per.slice(0, 10), largest_graph: [...per].sort((a, b) => b.graph_size - a.graph_size)[0] };
writeFileSync(out, JSON.stringify(res, null, 1));
console.log(JSON.stringify({ checks: res.checks, all: res.ms_all, warm: res.ms_warm_runs, worst }));
