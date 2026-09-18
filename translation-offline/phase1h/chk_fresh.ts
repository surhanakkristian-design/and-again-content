// Phase 1h - produce the app checker's own verdict (the `chk` block FRESH_SCHEMA.md requires) for the
// blind fresh answers. This is NOT a Phase 1h rule: it runs the EXISTING app checker (checker/v2/check.ts)
// over the fresh answers, exactly as Phase 1c produced measure_after.json for the 80.
//   ANN_DIR=... SYN_DIR=... LIB_OVERLAY=... node phase1h/chk_fresh.ts <out.jsonl>
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';

const [out] = process.argv.slice(2);
const { check } = await import('../checker/v2/check.ts');
const { compiler } = await import('../phase1b/scripts/data.ts');
const c: any = (compiler as any)();
const dir = new URL('./fresh/', import.meta.url);
const files = readdirSync(dir).filter((f) => /^(correct|wrong)_part\d+\.jsonl$/.test(f)).sort();
const lines: string[] = [];
let ok = 0, miss = 0;
const missing = new Set<number>();
for (const f of files) {
  for (const ln of readFileSync(new URL(f, dir), 'utf8').split('\n')) {
    if (!ln.trim()) continue;
    const r = JSON.parse(ln);
    let target: any = null;
    try { target = c.get(Number(r.sid)); } catch { target = null; }
    if (!target) { miss++; missing.add(Number(r.sid)); continue; }
    const res: any = check(r.en, target, { native: 'sk' });
    ok++;
    lines.push(JSON.stringify({ sid: r.sid, n: r.n, en: r.en,
      chk: { verdict: res.verdict, step: res.step, feedback: res.feedback ?? '' } }));
  }
}
writeFileSync(out, lines.length ? lines.join('\n') + '\n' : '');
console.error(JSON.stringify({ out, ann_dir: process.env.ANN_DIR ?? null, checked: ok, no_target: miss,
  missing_sids: [...missing].slice(0, 5), sample: lines[0]?.slice(0, 240) ?? null }));
