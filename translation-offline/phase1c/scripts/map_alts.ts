// Phase 1c – deterministic mapping of the annotator's free-text alternatives (`alt`) to synonym groups. Zero model tokens.
//   node phase1c/scripts/map_alts.ts <batch.json> [--out-dir DIR] [--ng-file FILE] [--report FILE]
// Defaults: --out-dir phase1c/annotated  --ng-file phase1b/synonyms/ng_phase1c.json  --report phase1c/annotated/map_<batch>.json
// Per anchor: every contextual group that has the anchor as a member form is a candidate; an alternative is COVERED by a group
// when it is a form of a member in the anchor's form tag(s) (or the member lemma itself). The group covering most alternatives
// wins (tie: fewer members, then id). All covered → s[anchor] = group. Otherwise → a proposed new group (`ng`) with the anchor
// and every alternative as lemmas (pos from the best group / lemmatiser; pos "x" with surfaces when lemmatising fails), deduped
// across sentences by (pos, members); s[anchor] = that ng id. Output annotations are in the checker's format (alt kept for audit).
// After a run: node phase1b/scripts/build_forms.ts (merges ng_phase1c.json into forms.json).
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildForms, type SynGroup } from '../../checker/v2/forms.ts';
import { locateAnchor, locateLock, parseAnchor, splitWords } from '../../checker/v2/match.ts';
import { loadForms, loadWords, P1B, readJson, synonymFiles } from '../../phase1b/scripts/data.ts';

const P1C = join(dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
const opt = (name: string, dflt: string) => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : dflt; };
const batchFile = argv.find((a, i) => !a.startsWith('--') && (i === 0 || !argv[i - 1].startsWith('--')));
if (!batchFile) { console.error('usage: map_alts.ts <batch.json> [--out-dir DIR] [--ng-file FILE] [--report FILE]'); process.exit(1); }
const batchName = basename(batchFile).replace(/\.json$/, '');
const outDir = opt('--out-dir', join(P1C, 'annotated'));
const ngFile = opt('--ng-file', join(P1B, 'synonyms', 'ng_phase1c.json'));
const reportFile = opt('--report', join(outDir, `map_${batchName}.json`));

const norm = (s: string) => s.toLowerCase().replace(/[’]/g, "'").replace(/[^a-z' -]/g, ' ').replace(/\s+/g, ' ').trim();
const words = loadWords();
const forms = loadForms();

// surface → [{gid, tag}] over contextual groups
const bySurface = new Map<string, { gid: string; tag: string }[]>();
for (const [gid, g] of Object.entries(forms.groups)) {
  if (g.kind !== 'contextual' || gid.startsWith('ng1c_')) continue;
  for (const [tag, list] of Object.entries(g.forms)) for (const s of list) {
    const k = norm(s); const arr = bySurface.get(k) ?? []; arr.push({ gid, tag }); bySurface.set(k, arr);
  }
}

// lemmatiser: surface → {lemma, pos, tag} via the table's member lemmas, then suffix-stripping candidates checked by buildForms
const lemmaIndex = new Map<string, { lemma: string; pos: string; tag: string }[]>();
{
  const seen = new Set<string>();
  const singles: SynGroup[] = [];
  for (const f of synonymFiles()) for (const g of f.groups) {
    if (g.kind !== 'contextual' || !['v', 'n', 'a'].includes(g.pos ?? 'x')) continue;
    for (const m of g.m) {
      const id = `${g.pos}|${m}`;
      if (seen.has(id) || m.includes(' ')) continue;
      seen.add(id);
      singles.push({ id, kind: 'contextual', pos: g.pos, m: [m], ...(g.irr?.[m] ? { irr: { [m]: g.irr[m] } } : {}) });
    }
  }
  const built = buildForms([{ groups: singles }], words).forms;
  for (const [id, g] of Object.entries(built.groups)) {
    const [pos, lemma] = id.split('|');
    for (const [tag, list] of Object.entries(g.forms)) for (const s of list) {
      const arr = lemmaIndex.get(s) ?? []; arr.push({ lemma, pos, tag }); lemmaIndex.set(s, arr);
    }
  }
}
const candidates = (w: string): string[] => {
  const c = new Set([w]);
  const rules: [RegExp, string][] = [[/ies$/, 'y'], [/es$/, ''], [/s$/, ''], [/ied$/, 'y'], [/ed$/, ''], [/ed$/, 'e'], [/d$/, ''],
    [/([bcdfgklmnprtvz])\1ed$/, '$1'], [/ing$/, ''], [/ing$/, 'e'], [/([bcdfgklmnprtvz])\1ing$/, '$1'], [/ier$/, 'y'], [/iest$/, 'y'],
    [/er$/, ''], [/er$/, 'e'], [/est$/, ''], [/est$/, 'e'], [/([bdgmnpt])\1er$/, '$1'], [/([bdgmnpt])\1est$/, '$1']];
  for (const [re, rep] of rules) if (re.test(w)) c.add(w.replace(re, rep));
  return [...c].filter((x) => x.length > 1);
};
const lemmaCache = new Map<string, { lemma: string; pos: string; tag: string }[]>();
const lemmatiseWord = (w: string): { lemma: string; pos: string; tag: string }[] => {
  if (lemmaCache.has(w)) return lemmaCache.get(w)!;
  const out = [...(lemmaIndex.get(w) ?? [])];
  const groups: SynGroup[] = [];
  for (const cand of candidates(w)) if (words.has(cand)) for (const pos of ['v', 'n', 'a']) groups.push({ id: `${pos}|${cand}`, kind: 'contextual', pos, m: [cand] });
  const built = buildForms([{ groups }], words).forms;
  for (const [id, g] of Object.entries(built.groups)) {
    const [pos, lemma] = id.split('|');
    for (const [tag, list] of Object.entries(g.forms)) {
      if (list.includes(w) && !out.some((o) => o.lemma === lemma && o.pos === pos && o.tag === tag)) out.push({ lemma, pos, tag });
    }
  }
  lemmaCache.set(w, out);
  return out;
};
/** Lemma of a (multi-word) surface for a given pos and tag; verbs inflect word 0, nouns the last word. */
const lemmatise = (surface: string, pos: string, tag: string): string | null => {
  const ws = surface.split(' ');
  const head = pos === 'n' ? ws.length - 1 : 0;
  if (pos === 'x') return surface;
  const hit = lemmatiseWord(ws[head]).find((r) => r.pos === pos && r.tag === tag);
  if (!hit) return null;
  ws[head] = hit.lemma;
  return ws.join(' ');
};

// ng store (deduped by pos + members across runs)
const ngStore: { groups: any[] } = readJson(ngFile, { groups: [] });
const ngByKey = new Map<string, any>(ngStore.groups.map((g) => [`${g.pos}|${[...g.m].sort().join('|')}`, g]));
let ngNext = ngStore.groups.reduce((mx, g) => Math.max(mx, Number(String(g.id).replace('ng1c_', '')) || 0), 0) + 1;

const batch: any[] = (() => {
  const text = readFileSync(batchFile, 'utf8');
  try { const d = JSON.parse(text); return Array.isArray(d) ? d : [d]; } catch { /* one object per line */ }
  return text.split('\n').map((l) => l.trim().replace(/^\[/, '').replace(/,?\]?$/, '').replace(/,$/, '')).filter((l) => l.startsWith('{')).map((l) => JSON.parse(l));
})();

const stats = { batch: batchName, sentences: 0, anchors: 0, alternatives: 0, alt_mapped_existing: 0, alt_new: 0,
  anchors_to_existing_group: 0, anchors_to_ng: 0, ng_new_groups: 0, ng_reused_groups: 0, ng_lemmatised: 0, ng_surface_x: 0,
  skipped: [] as string[] };
const perSentence: any[] = [];
const KEY_ORDER = ['id', 't', 'lv', 'v', 'lk', 's', 'g', 'o', 'd', 'p', 'm'];
mkdirSync(outDir, { recursive: true });

for (const ann of batch) {
  stats.sentences++;
  const s: Record<string, string> = { ...(ann.s ?? {}) };
  const detail: any[] = [];
  const variants: string[] = ann.v ?? [];
  for (const [anchor, rawAlts] of Object.entries<any>(ann.alt ?? {})) {
    const anchorText = norm(parseAnchor(anchor).text);
    const alts = [...new Set((Array.isArray(rawAlts) ? rawAlts : [rawAlts]).map((x: string) => norm(String(x))).filter((x) => x && x !== anchorText))];
    if (!alts.length) continue;
    // the anchor must occur outside the lock in at least one variant
    let ok = false;
    let prevWord = '';
    variants.forEach((v, i) => {
      const raw = splitWords(v).raw;
      const r = locateAnchor(raw, anchor);
      if (!r) return;
      const lock = locateLock(raw, ann.lk?.[i]) ?? [];
      if (!lock.some(([a, b]) => r[0] < b && a < r[1])) { if (!ok) prevWord = raw[r[0] - 1] ?? ''; ok = true; }
    });
    if (!ok) { stats.skipped.push(`${ann.id}:${anchor} (not found outside the lock)`); continue; }
    stats.anchors++; stats.alternatives += alts.length;
    // candidate groups
    const cands = new Map<string, Set<string>>();
    for (const { gid, tag } of bySurface.get(anchorText) ?? []) { const t = cands.get(gid) ?? new Set(); t.add(tag); cands.set(gid, t); }
    let best: { gid: string; covered: string[]; size: number } | null = null;
    for (const [gid, tags] of cands) {
      const g = forms.groups[gid];
      const surf = new Set<string>();
      for (const t of tags) for (const x of g.forms[t] ?? []) surf.add(norm(x));
      const covered = alts.filter((x) => surf.has(x) || g.m.map(norm).includes(x));
      const cand = { gid, covered, size: g.m.length };
      if (!best || covered.length > best.covered.length || (covered.length === best.covered.length && (cand.size < best.size || (cand.size === best.size && gid < best.gid)))) best = cand;
    }
    const coveredN = best ? best.covered.length : 0;
    stats.alt_mapped_existing += coveredN;
    stats.alt_new += alts.length - coveredN;
    if (best && coveredN === alts.length) {
      s[anchor] = best.gid; stats.anchors_to_existing_group++;
      detail.push({ anchor, alts, group: best.gid });
      continue;
    }
    // proposed new group
    // readings of the anchor: the best group's (pos, tag) when it covered something, then every lemmatiser reading;
    // the reading under which anchor + all alternatives lemmatise wins (tie: more inflected members, i.e. lemma ≠ surface)
    const readingsOf: { pos: string; tag: string }[] = [];
    if (best && coveredN > 0) for (const t of cands.get(best.gid)!) readingsOf.push({ pos: forms.groups[best.gid].pos, tag: t });
    const multi = [anchorText, ...alts].some((x) => x.includes(' '));
    // multi-word items: only the covering group's reading, else pos "x" (surfaces) – no parser to find the head
    if (!multi) for (const h of lemmatiseWord(anchorText)) readingsOf.push({ pos: h.pos, tag: h.tag });
    // context hint from the word before the anchor: determiner/preposition → noun, pronoun/auxiliary/to → verb
    const hint = /^(the|a|an|this|that|these|those|my|your|his|her|its|our|their|some|any|no|every|of|in|on|at|with|for|from|by|into|onto)$/.test(prevWord) ? 'n'
      : /^(i|you|he|she|it|we|they|to|will|would|can|could|should|must|might|may|do|does|did|has|have|had|was|were|is|are|am|be|been)$/.test(prevWord) ? 'v' : '';
    let pos = 'x';
    let members: string[] | null = null;
    let bestScore = -1;
    readingsOf.forEach((r, k) => {
      if (!['v', 'n', 'a'].includes(r.pos)) return;
      const items = [anchorText, ...alts];
      const lem = items.map((x) => lemmatise(x, r.pos, r.tag));
      if (!lem.every((x) => x)) return;
      const score = (k < (best && coveredN > 0 ? cands.get(best.gid)!.size : 0) ? 1000 : 0) + (r.pos === hint ? 100 : 0)
        + lem.filter((x, j) => x !== items[j]).length * 10 + (r.pos === 'n' ? 2 : r.pos === 'v' ? 1 : 0);
      if (score > bestScore) { bestScore = score; pos = r.pos; members = [...new Set(lem as string[])]; }
    });
    const lemmatised = members !== null;
    if (!members) { pos = 'x'; members = [anchorText, ...alts]; }
    const key = `${pos}|${[...members].sort().join('|')}`;
    let g = ngByKey.get(key);
    if (g) { stats.ng_reused_groups++; if (!g.sources.includes(ann.id)) g.sources.push(ann.id); }
    else {
      g = { id: `ng1c_${ngNext++}`, kind: 'contextual', pos, m: members, ok: '', bad: '', basis: best?.gid ?? null,
        sources: [ann.id], anchor: anchorText, batch: batchName, lemmatised };
      ngByKey.set(key, g); stats.ng_new_groups++;
      if (lemmatised) stats.ng_lemmatised++; else stats.ng_surface_x++;
    }
    s[anchor] = g.id; stats.anchors_to_ng++;
    detail.push({ anchor, alts, ng: g.id, basis: best?.gid ?? null, covered_by_basis: best?.covered ?? [] });
  }
  const out: any = {};
  const merged = { ...ann, s };
  for (const k of KEY_ORDER) {
    const v = merged[k];
    if (v === undefined || v === null || (typeof v === 'object' && Object.keys(v).length === 0)) continue;
    out[k] = v;
  }
  if (ann.alt) out.alt = ann.alt;
  writeFileSync(join(outDir, `${ann.id}.json`), JSON.stringify(out) + '\n');
  perSentence.push({ id: ann.id, anchors: detail });
}
mkdirSync(dirname(ngFile), { recursive: true });
writeFileSync(ngFile, JSON.stringify({ groups: [...ngByKey.values()] }).replace(/\},\{/g, '},\n{') + '\n');
writeFileSync(reportFile, JSON.stringify({ stats, sentences: perSentence }, null, 1));
const { skipped, ...head } = stats;
console.log(JSON.stringify({ ...head, skipped: skipped.length, ng_file: ngFile, report: reportFile }));
