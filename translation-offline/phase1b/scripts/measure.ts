// Phase 1b measurements. Works on whatever annotations exist (missing ones are counted, not fatal).
//   node phase1b/scripts/measure.ts coverage <translations.json> <out.json>
//   node phase1b/scripts/measure.ts fa <fa_translations.json> <out.json>
//   node phase1b/scripts/measure.ts regression <out.json>
//   node phase1b/scripts/measure.ts timing <out.json>
//   node phase1b/scripts/measure.ts sizes <out.json>
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { gzipSync } from 'node:zlib';
import { performance } from 'node:perf_hooks';
import { expandSlots } from '../../checker/slots.ts';
import { graphSize, type Compiled, type Graph } from '../../checker/v2/match.ts';
import { check } from '../../checker/v2/check.ts';
import { P1B, ROOT, annotationIds, compiler, libraryFiles, loadAnnotation, phase1Generated, readJson, selection } from './data.ts';

const [cmd, ...args] = process.argv.slice(2);
const sel = selection();
const c = compiler();
const write = (path: string, data: unknown) => writeFileSync(path, JSON.stringify(data, null, 1));
const bytes = (text: string) => ({ raw: Buffer.byteLength(text), gzip: gzipSync(text).length });
const stats = (xs: number[]) => {
  const s = [...xs].sort((a, b) => a - b);
  const q = (p: number) => (s.length ? s[Math.min(s.length - 1, Math.floor(p * s.length))] : 0);
  return { n: s.length, mean: s.length ? +(s.reduce((a, b) => a + b, 0) / s.length).toFixed(1) : 0, p50: q(0.5), p99: q(0.99), max: s.at(-1) ?? 0 };
};

/** [{exercise_id, translations:[string|{text}]}] or {items:[…]} → flat rows */
const readTranslations = (path: string): { exercise_id: number; text: string; extra: any }[] => {
  const data = readJson<any>(path);
  const list: any[] = Array.isArray(data) ? data : data.items ?? data.translations ?? [];
  const out: { exercise_id: number; text: string; extra: any }[] = [];
  for (const item of list) {
    const id = Number(item.exercise_id ?? item.id);
    const ts = item.translations ?? item.items ?? (item.text ? [item] : []);
    for (const t of ts) {
      const text = typeof t === 'string' ? t : t.text ?? t.answer;
      if (typeof text === 'string') out.push({ exercise_id: id, text, extra: typeof t === 'string' ? {} : t });
    }
  }
  return out;
};

const runRows = (path: string) =>
  readTranslations(path).map(({ exercise_id, text, extra }) => {
    const s = sel.get(exercise_id);
    const compiled = c.get(exercise_id);
    const base = { exercise_id, level: s?.level ?? null, new_long: s?.new_long ?? null, topic: s?.topic ?? null, reference: s?.en ?? null, sk: s?.sk ?? null, answer: text, ...(extra.kind ? { kind: extra.kind } : {}) };
    if (!compiled) return { ...base, verdict: 'no_annotation', step: null, feedback: null, closest: null };
    const r = check(text, compiled, { native: 'sk' });
    return { ...base, verdict: r.verdict, step: r.step, feedback: r.feedback, closest: r.closest, mistake: r.mistake ?? null };
  });

const totals = (rows: any[]) => {
  const out: Record<string, Record<string, number>> = {};
  const add = (key: string, v: string) => { (out[key] ??= {})[v] = (out[key][v] ?? 0) + 1; out[key].total = (out[key].total ?? 0) + 1; };
  for (const r of rows) {
    add('all', r.verdict);
    add(`level_${r.level}`, r.verdict);
    add(`new_long_${r.new_long}`, r.verdict);
    if (r.step) add('steps', r.step);
  }
  return out;
};

if (cmd === 'coverage' || cmd === 'fa') {
  const [input, output] = args;
  if (!input || !output) throw new Error(`usage: measure.ts ${cmd} <in.json> <out.json>`);
  const rows = runRows(input);
  const t = totals(rows);
  if (cmd === 'coverage') {
    write(output, { totals: t, rows });
    console.log(`coverage ${rows.length}: ${JSON.stringify(t.all)}`);
  } else {
    const accepted = rows.filter((r) => r.verdict === 'correct' || r.verdict === 'correct_with_tip');
    write(output, { totals: t, accepted_count: accepted.length, accepted, rows });
    console.log(`fa ${rows.length}: accepted ${accepted.length} ${JSON.stringify(t.all)}`);
  }
} else if (cmd === 'regression') {
  const [output] = args;
  const bench = readJson<any[]>(join(ROOT, 'measurements', 'bench_comparison.json'), []);
  const benchRows = bench.map((b) => {
    const compiled = c.get(b.exercise_id);
    if (!compiled) return { id: b.id, exercise_id: b.exercise_id, answer: b.answer, phase1: b.offline, v2: 'no_annotation' };
    const r = check(b.answer, compiled, { native: 'sk' });
    return { id: b.id, exercise_id: b.exercise_id, category: b.category, answer: b.answer, phase1: b.offline, phase1_step: b.step, gemini_37: b.gemini_37,
      v2: r.verdict, v2_step: r.step, feedback_sk: r.feedback, changed: r.verdict !== b.offline, agrees_gemini: r.verdict === b.gemini_37 };
  });
  const p1Rows: any[] = [];
  for (const id of annotationIds()) {
    const compiled = c.get(id);
    const p1 = phase1Generated(id);
    if (!compiled || !p1) continue;
    for (const m of p1.mistakes ?? []) {
      let texts: string[] = [];
      try { texts = expandSlots(m.text); } catch { continue; }
      for (const text of texts) {
        const r = check(text, compiled, { native: 'sk' });
        p1Rows.push({ exercise_id: id, kind: m.kind, text, phase1: m.verdict, v2: r.verdict, v2_step: r.step, changed: r.verdict !== m.verdict });
      }
    }
  }
  const benchAnnotated = benchRows.filter((r) => r.v2 !== 'no_annotation');
  const summary = {
    bench: { total: benchRows.length, annotated: benchAnnotated.length, changed: benchAnnotated.filter((r: any) => r.changed).length,
      agree_gemini_v2: benchAnnotated.filter((r: any) => r.agrees_gemini).length, agree_gemini_phase1: bench.filter((b) => b.agree).length },
    phase1_mistakes: { total: p1Rows.length, changed: p1Rows.filter((r) => r.changed).length },
  };
  write(output, { summary, bench_changes: benchRows.filter((r: any) => r.changed || r.v2 === 'no_annotation'), phase1_mistake_changes: p1Rows.filter((r) => r.changed), bench: benchRows });
  console.log(`regression ${JSON.stringify(summary)}`);
} else if (cmd === 'timing') {
  const [output] = args;
  let target: Compiled | null = null;
  for (const id of annotationIds()) {
    const compiled = c.get(id);
    if (compiled && (!target || graphSize(compiled) > graphSize(target))) target = compiled;
  }
  if (!target) { write(output, { error: 'no annotations' }); console.log('timing: no annotations'); process.exit(0); }
  let seed = 12345;
  const rnd = () => ((seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648);
  const pickOf = <T>(xs: T[]) => xs[Math.floor(rnd() * xs.length)];
  const walk = (g: Graph): string[] => {
    const out: string[] = [];
    let u = g.start;
    let guard = 1000;
    while (u !== g.end && guard-- > 0) {
      const e = pickOf(g.edges[u]);
      if (!e) break;
      if (e.tok) out.push(e.tok);
      u = e.to;
    }
    return out;
  };
  const vocab = [...new Set(target.variants.flatMap((v) => v.graphs.flatMap((g) => [...g.tokens])))];
  const answers: { kind: string; text: string }[] = [];
  for (let i = 0; i < 2000; i++) {
    const v = pickOf([...target.variants, ...target.mistakes]);
    const toks = walk(pickOf(v.graphs));
    const kind = ['path', 'near_miss', 'near_miss2', 'shuffle', 'long', 'long_repeat'][i % 6];
    if (kind === 'near_miss' || kind === 'near_miss2') {
      for (let k = 0; k < (kind === 'near_miss' ? 1 : 3); k++) {
        const at = Math.floor(rnd() * (toks.length + 1));
        const op = Math.floor(rnd() * 4);
        if (op === 0) toks.splice(at, 1);
        else if (op === 1) toks.splice(at, 0, pickOf(vocab));
        else if (op === 2 && toks[at]) toks[at] = toks[at].slice(0, -1) + 'x';
        else if (toks[at + 1]) [toks[at], toks[at + 1]] = [toks[at + 1], toks[at]];
      }
    } else if (kind === 'shuffle') toks.sort(() => rnd() - 0.5);
    else if (kind === 'long') while (toks.length < 80) toks.push(pickOf(vocab));
    else if (kind === 'long_repeat') { const base = [...toks]; while (toks.length < 120) toks.push(...base); }
    answers.push({ kind, text: toks.join(' ') });
  }
  const times: number[] = [];
  const byKind: Record<string, number[]> = {};
  for (const a of answers) {
    const t0 = performance.now();
    check(a.text, target, { native: 'sk' });
    const ms = performance.now() - t0;
    times.push(ms);
    (byKind[a.kind] ??= []).push(ms);
  }
  const round = (o: any) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, typeof v === 'number' ? +v.toFixed(3) : v]));
  const result = { exercise_id: target.id, graph_size: graphSize(target), variants: target.variants.length, mistakes: target.mistakes.length,
    answers: answers.length, ms: round(stats(times)), by_kind: Object.fromEntries(Object.entries(byKind).map(([k, v]) => [k, round(stats(v))])) };
  write(output, result);
  console.log(`timing ${JSON.stringify({ exercise_id: result.exercise_id, max: result.ms.max, p99: result.ms.p99 })}`);
} else if (cmd === 'sizes') {
  const [output] = args;
  const file = (rel: string) => (existsSync(join(P1B, rel)) ? readFileSync(join(P1B, rel), 'utf8') : '');
  const lib = libraryFiles();
  const perTopic: Record<string, { raw: number; gzip: number }> = {};
  for (const f of lib) perTopic[f.type_id] = bytes(JSON.stringify(f.items));
  const forms = c.forms;
  const perSentence: number[] = [];
  const perExercise: { id: number; raw: number; gzip: number; parts: Record<string, number> }[] = [];
  for (const id of annotationIds()) {
    const ann = loadAnnotation(id);
    const compiled = c.get(id);
    if (!ann || !compiled) continue;
    const annText = JSON.stringify(ann);
    perSentence.push(Buffer.byteLength(annText));
    const libIds = new Set((ann.m ?? []).map((m) => m[0]));
    const items = [...libIds].map((x) => c.library[x]).filter(Boolean).map((i) => ({ id: i.id, verdict: i.verdict, sk: i.sk, slots: i.slots }));
    const groups = Object.fromEntries([...compiled.groups].filter((g) => forms.groups[g]).map((g) => [g, forms.groups[g].forms]));
    const neighbours = [...(compiled.neighbours ?? [])];
    const parts = { annotation: annText, library_sk: JSON.stringify(items), forms: JSON.stringify(groups), neighbours: JSON.stringify(neighbours) };
    const all = JSON.stringify(parts);
    perExercise.push({ id, ...bytes(all), parts: Object.fromEntries(Object.entries(parts).map(([k, v]) => [k, Buffer.byteLength(v)])) });
  }
  const result = {
    table: bytes(file('synonyms/table.json')),
    forms: bytes(file('synonyms/forms.json')),
    library_all: bytes(JSON.stringify(lib.map((f) => f.items))),
    library_per_topic: perTopic,
    annotation_per_sentence: stats(perSentence),
    per_exercise_download: { raw: stats(perExercise.map((e) => e.raw)), gzip: stats(perExercise.map((e) => e.gzip)),
      parts_mean: Object.fromEntries(['annotation', 'library_sk', 'forms', 'neighbours'].map((k) => [k, stats(perExercise.map((e) => e.parts[k])).mean])) },
    exercises: perExercise,
  };
  write(output, result);
  console.log(`sizes ${JSON.stringify({ table: result.table, forms: result.forms, library_all: result.library_all, annotation: result.annotation_per_sentence, per_exercise_gzip: result.per_exercise_download.gzip })}`);
} else {
  console.error('usage: measure.ts coverage|fa <in.json> <out.json> | regression|timing|sizes <out.json>');
  process.exit(1);
}
