// annotated/batch_*.json (JSON arrays) → annotated/<id>.json, one per sentence.
// `ng` proposals move to synonyms/annotator.json as ng_<exercise>_<k>; the `s` references are rewritten.
// Idempotent: re-running rewrites the same files; annotator.json groups are replaced by id.
// Run: node phase1b/scripts/merge_batches.ts
import { existsSync, readdirSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { P1B, readJson } from './data.ts';

const dir = join(P1B, 'annotated');
mkdirSync(dir, { recursive: true });
mkdirSync(join(P1B, 'synonyms'), { recursive: true });

/** A batch is a JSON array; tolerate one object per line with stray commas/brackets. */
const parseBatch = (text: string, file: string): any[] => {
  try { const d = JSON.parse(text); return Array.isArray(d) ? d : [d]; } catch { /* fall through */ }
  const out: any[] = [];
  for (const line of text.split('\n')) {
    const t = line.trim().replace(/^\[/, '').replace(/,?\]?$/, '').replace(/,$/, '');
    if (!t.startsWith('{')) continue;
    try { out.push(JSON.parse(t)); } catch { console.error(`${file}: unparsable line: ${t.slice(0, 80)}`); }
  }
  return out;
};

const annotatorPath = join(P1B, 'synonyms', 'annotator.json');
const annotator: { groups: any[] } = readJson(annotatorPath, { groups: [] });
const groups = new Map<string, any>(annotator.groups.map((g) => [g.id, g]));
const KEY_ORDER = ['id', 't', 'lv', 'v', 'lk', 's', 'g', 'o', 'd', 'p', 'm'];
let sentences = 0;
let proposals = 0;
const batches = readdirSync(dir).filter((f) => /^batch_.*\.json$/.test(f)).sort();
for (const file of batches) {
  for (const ann of parseBatch(readFileSync(join(dir, file), 'utf8'), file)) {
    if (!ann || typeof ann.id !== 'number') { console.error(`${file}: entry without numeric id`); continue; }
    const rename = new Map<string, string>();
    for (const [key, group] of Object.entries<any>(ann.ng ?? {})) {
      const k = key.replace(/^ng_?/, '') || String(rename.size);
      const id = `ng_${ann.id}_${k}`;
      rename.set(key, id);
      groups.set(id, { id, kind: 'contextual', pos: group.pos ?? 'x', m: group.m ?? [], ...(group.irr ? { irr: group.irr } : {}),
        ...(group.head !== undefined ? { head: group.head } : {}), ok: group.ok ?? '', bad: group.bad ?? '', source: ann.id });
      proposals++;
    }
    if (ann.s) for (const [anchor, gid] of Object.entries<string>(ann.s)) if (rename.has(gid)) ann.s[anchor] = rename.get(gid)!;
    delete ann.ng;
    const out: any = {};
    for (const key of KEY_ORDER) {
      const value = ann[key];
      if (value === undefined || value === null) continue;
      if (typeof value === 'object' && Object.keys(value).length === 0) continue;
      out[key] = value;
    }
    for (const key of Object.keys(ann)) if (!(key in out) && !KEY_ORDER.includes(key)) out[key] = ann[key];
    writeFileSync(join(dir, `${ann.id}.json`), JSON.stringify(out) + '\n');
    sentences++;
  }
}
writeFileSync(annotatorPath, JSON.stringify({ groups: [...groups.values()].sort((a, b) => a.id.localeCompare(b.id)) }, null, 0).replace(/\},\{/g, '},\n{') + '\n');
console.log(JSON.stringify({ batches: batches.length, sentences, ng_groups: proposals, annotator_groups: groups.size, existed: existsSync(annotatorPath) }));
