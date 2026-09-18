// Lint gate for the Phase 1b data (no model tokens). Works on whatever files exist.
// Run: node phase1b/scripts/lint.ts   → review/lint.json + one summary line per error class.
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { expandSlots } from '../../checker/slots.ts';
import { MAX_FEEDBACK_CHARS } from '../../checker/offlineCheck.ts';
import {
  compile, detAlternatives, groupAlternatives, locateAnchor, locateLock, parseAnchor, splitWords, PERSONAL_PRONOUNS,
  type Annotation, type LibraryItem,
} from '../../checker/v2/match.ts';
import { check, fillFeedback } from '../../checker/v2/check.ts';
import { P1B, annotationIds, libraryFiles, loadAnnotation, loadForms, loadWords, phase1Generated, selection, synonymFiles } from './data.ts';

// Phase 1 lint lists (scripts/build_pilot.ts)
const GENDERED = /\b\p{L}+l[ao]?\s+(si|jsi)\b/iu;
const TRANSLATED_TENSE = /(\p{L}*(prítomn|přítomn|minul|budúc|budouc|predprítomn|předpřítomn|predminul|předminul)\p{L}*\s+(čas|času|časom|časem)|\b(trpn|činn)\p{L}*\s+rod|\bpriebehov|\bprůběhov|podmieňovac\p{L}*\s+spôsob|podmiňovac\p{L}*\s+způsob|\bneurčit(ok|ek|ku|kem|kom)\b|\bpríčasti|\bpříčest|\bgerundi(um|a|e))/iu;
const PRAISE = /(veta je správn|věta je správn|je to správn|\bdobre\b|\bvýborne\b|\bskvel|\bskvěl|\bsuper\b|\bwell done\b|\bgreat\b|\bgood job\b|\bnice\b|\bcorrect,? but\b|\bis correct\b|správne,? ale|správně,? ale)/iu;
const LONG_FILL = 'would have been waiting for them'; // 32 chars: a long plausible {right}/{wrong}

type Issue = { id: number | string; cls: string; detail: string };
const issues: Issue[] = [];
const flag = (id: number | string, cls: string, detail: string) => issues.push({ id, cls, detail });

const words = loadWords();
const forms = loadForms();
const sel = selection();
const libFiles = libraryFiles();
const library: Record<string, LibraryItem> = {};
const topicItems = new Map<number, Set<string>>();

// ---- library files
for (const f of libFiles) {
  if (String(f.type_id) !== f.file.replace('.json', '')) flag(f.file, 'lib_type_id_mismatch', String(f.type_id));
  const ids = new Set<string>();
  for (const item of f.items ?? []) {
    const where = `${f.file}#${item.id}`;
    if (!item.id) { flag(f.file, 'lib_required_key', 'id'); continue; }
    if (ids.has(item.id)) flag(where, 'lib_duplicate_id', item.id);
    ids.add(item.id);
    library[item.id] = item;
    if (!['wrong', 'correct_with_tip'].includes(item.verdict)) flag(where, 'lib_verdict', String(item.verdict));
    for (const lang of ['sk', 'cz', 'en'] as const) {
      const text = item[lang];
      if (typeof text !== 'string' || !text.trim()) { flag(where, 'lib_feedback_missing', lang); continue; }
      const extra = (item.slots ?? []).filter((s) => s !== 'right' && s !== 'wrong');
      const used = [...text.matchAll(/\{(\w+)\}/g)].map((m) => m[1]);
      for (const slot of used) if (!(item.slots ?? []).includes(slot)) flag(where, 'lib_slot_not_declared', `${lang}: {${slot}}`);
      const filled = text.replace(/\{(\w+)\}/g, (_, k) => (extra.includes(k) ? 'had been waiting' : LONG_FILL));
      if (filled.length > MAX_FEEDBACK_CHARS) flag(where, 'lib_too_long_filled', `${lang} ${filled.length}: ${text}`);
      if (PRAISE.test(text)) flag(where, 'lib_praise', `${lang}: ${text}`);
      if (lang !== 'en' && GENDERED.test(text)) flag(where, 'lib_maybe_gendered', `${lang}: ${text}`);
      if (lang !== 'en' && TRANSLATED_TENSE.test(text)) flag(where, 'lib_translated_grammar_name', `${lang}: ${text}`);
    }
  }
  topicItems.set(Number(f.type_id), ids);
}

// ---- synonym table
const synGroups = new Map<string, any>();
for (const file of synonymFiles()) {
  for (const g of file.groups) {
    if (synGroups.has(g.id)) flag(`synonyms/${file.file}`, 'syn_duplicate_id', g.id);
    synGroups.set(g.id, g);
    if (!['safe', 'contextual'].includes(g.kind)) flag(g.id, 'syn_kind', String(g.kind));
    if (g.kind === 'contextual' && (!g.ok || !g.bad)) flag(g.id, 'syn_missing_ok_bad', '');
    if (!Array.isArray(g.m) || g.m.length < 2) flag(g.id, 'syn_members', JSON.stringify(g.m));
    if (!forms.groups[g.id]) flag(g.id, 'syn_not_in_forms_json', 'run build_forms.ts');
  }
}

// ---- annotations
const REQUIRED = ['id', 't', 'lv', 'v', 'lk'];
let annotations = 0;
for (const id of annotationIds()) {
  const ann = loadAnnotation(id) as Annotation | null;
  if (!ann) { flag(id, 'ann_unparsable', ''); continue; }
  annotations++;
  for (const key of REQUIRED) if ((ann as any)[key] === undefined) flag(id, 'ann_required_key', key);
  if (!Array.isArray(ann.v) || ann.v.length === 0) continue;
  const s = sel.get(id);
  if (!s) flag(id, 'ann_not_in_selection', '');
  else {
    if (ann.v[0] !== s.en) flag(id, 'ann_v0_not_reference', `${ann.v[0]} ≠ ${s.en}`);
    if (ann.t !== s.type_id) flag(id, 'ann_type_mismatch', `${ann.t} ≠ ${s.type_id}`);
    if (ann.lv !== s.level) flag(id, 'ann_level_mismatch', `${ann.lv} ≠ ${s.level}`);
  }
  if (ann.v.length > 4) flag(id, 'ann_too_many_variants', String(ann.v.length));
  if (!Array.isArray(ann.lk) || ann.lk.length !== ann.v.length) flag(id, 'ann_lock_count', `${ann.lk?.length} locks for ${ann.v.length} variants`);
  const words_ = ann.v.map((v) => splitWords(v).raw);
  const locks = ann.v.map((_, i) => locateLock(words_[i], ann.lk?.[i]));
  locks.forEach((l, i) => { if (!l || l.length === 0) flag(id, 'ann_lock_not_found', `v${i}: ${ann.lk?.[i]}`); });

  // anchors: found in ≥1 variant, never inside a lock
  const anchors: [string, string][] = [];
  for (const a of Object.keys(ann.s ?? {})) anchors.push(['s', a]);
  for (const chain of ann.g ?? []) for (const a of chain) anchors.push(['g', a]);
  for (const a of Object.keys(ann.o ?? {})) anchors.push(['o', a]);
  for (const a of Object.keys(ann.d ?? {})) anchors.push(['d', a]);
  for (const p of ann.p ?? []) {
    if (p.startsWith('-')) anchors.push(['p', p.slice(1)]);
    else if (p.startsWith('+')) { const at = p.lastIndexOf('@'); if (at > 1) anchors.push(['p', p.slice(at + 1)]); }
    else flag(id, 'ann_p_invalid', p);
  }
  for (const m of ann.m ?? []) if (m[2]) anchors.push(['m', m[2]]);
  for (const [kind, anchor] of anchors) {
    let found = 0;
    words_.forEach((raw, i) => {
      const r = locateAnchor(raw, anchor);
      if (!r) return;
      found++;
      for (const [ls, le] of locks[i] ?? []) if (r[0] < le && ls < r[1]) flag(id, 'ann_anchor_in_lock', `${kind} "${anchor}" in v${i}`);
    });
    if (!found) flag(id, 'ann_anchor_not_found', `${kind} "${anchor}"`);
  }
  // s groups
  for (const [anchor, gid] of Object.entries(ann.s ?? {})) {
    if (!synGroups.has(gid) && !forms.groups[gid]) { flag(id, 'ann_unknown_group', `${anchor} → ${gid}`); continue; }
    if (forms.groups[gid] && !groupAlternatives(forms, gid, parseAnchor(anchor).text)) flag(id, 'ann_anchor_not_a_member_form', `${anchor} → ${gid}`);
    if (synGroups.get(gid)?.kind === 'safe') flag(id, 'ann_s_uses_safe_group', `${anchor} → ${gid}`);
  }
  for (const chain of ann.g ?? []) for (const a of chain) if (!PERSONAL_PRONOUNS.has(parseAnchor(a).text.toLowerCase())) flag(id, 'ann_g_not_pronoun', a);
  const DET_OK = new Set(['the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'some', 'any', 'no',
    'one', 'each', 'every', 'another', 'both', 'all', '∅']);
  for (const [a, value] of Object.entries(ann.d ?? {})) {
    if (!detAlternatives(value)) flag(id, 'ann_d_invalid', `${a}: ${value}`);
    else if (!['A', 'P', 'Z'].includes(value) && value.split('|').some((x) => !DET_OK.has(x.trim().toLowerCase()))) flag(id, 'ann_d_invalid', `${a}: ${value}`);
  }
  for (const [a, value] of Object.entries(ann.o ?? {})) {
    if (!/^[a-z]+( [a-z]+)*(\|[a-z]+( [a-z]+)*)+$/i.test(value) && !/^[a-z]+$/i.test(value)) flag(id, 'ann_o_invalid', `${a}: ${value}`);
  }
  // library references
  const topic = topicItems.get(ann.t);
  for (const m of ann.m ?? []) {
    const [libId, wrong, , extra] = m;
    if (!topic) { flag(id, 'ann_topic_library_missing', `t=${ann.t}`); break; }
    if (!topic.has(libId)) { flag(id, 'ann_library_id_unknown', `${libId} (topic ${ann.t})`); continue; }
    if (typeof wrong !== 'string') flag(id, 'ann_m_invalid', JSON.stringify(m));
    const need = (library[libId].slots ?? []).filter((x) => x !== 'right' && x !== 'wrong');
    for (const slot of need) if (!extra || !extra[slot]) flag(id, 'ann_slot_missing', `${libId} {${slot}}`);
  }

  // matcher checks
  const compiled = compile(ann, forms, library, { words });
  for (const n of compiled.notes) if (!/^(s|g|o|d|p)_anchor_in_lock|^lock_not_found/.test(n)) flag(id, 'compile_note', n);
  for (const m of compiled.mistakes) {
    for (const lang of ['sk', 'cz', 'en'] as const) {
      const text = fillFeedback(m, lang);
      if (m.item && text === null) flag(id, 'feedback_unfilled_slot', `${m.libId} ${lang}`);
      if (text && text.length > MAX_FEEDBACK_CHARS) flag(id, 'feedback_too_long', `${m.libId} ${lang} ${text.length}: ${text}`);
    }
    const r = check(m.text, { ...compiled, mistakes: [] }, { native: 'sk' });
    if (r.step === 'match' || r.step === 'spelling_variant') flag(id, 'mistake_accepted_as_correct', `${m.libId}: ${m.text}`);
  }
  if (ann.v.length > 1) {
    ann.v.forEach((text, i) => {
      ann.v.forEach((_, j) => {
        if (i === j) return;
        const other = compile(ann, forms, library, { only: [j], noMistakes: true, words });
        const r = check(text, other, { native: 'sk' });
        if (r.verdict === 'correct') flag(id, 'variant_is_freedom_swap', `v${i} is accepted by v${j}: ${text}`);
      });
    });
  }
  // Phase 1 stored mistakes keep their Phase 1 verdict
  const p1 = phase1Generated(id);
  for (const m of p1?.mistakes ?? []) {
    let texts: string[] = [];
    try { texts = expandSlots(m.text); } catch { continue; }
    for (const text of texts) {
      const r = check(text, compiled, { native: 'sk' });
      if (r.verdict !== m.verdict) flag(id, 'p1_mistake_verdict_changed', `${m.verdict} → ${r.verdict} (${r.step}): ${text}`);
    }
  }
}

const LINT_DIR = process.env.LINT_DIR ?? join(P1B, 'review');
mkdirSync(LINT_DIR, { recursive: true });
const summary: Record<string, number> = {};
for (const i of issues) summary[i.cls] = (summary[i.cls] ?? 0) + 1;
writeFileSync(join(LINT_DIR, 'lint.json'), JSON.stringify({ annotations, library_topics: libFiles.length, synonym_groups: synGroups.size, summary, issues }, null, 1));
console.log(`lint: ${annotations} annotations, ${libFiles.length} library topics, ${synGroups.size} synonym groups, ${issues.length} issues`);
for (const [cls, n] of Object.entries(summary).sort((a, b) => b[1] - a[1])) console.log(`${cls}: ${n}`);
