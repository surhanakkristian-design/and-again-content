// Phase 1b – pattern compiler + matcher for "translate the sentence".
// Spec: translation-offline/phase1b/FORMAT_SPEC.md §1 (synonym table), §3 (annotation).
// Pure functions, no I/O. The device holds one annotation per sentence, the
// forms of the synonym groups it references and the library items of its topic;
// compile() turns them into slot graphs, matchGraph() decides "matches",
// alignGraph() finds the closest path (weighted edit distance) for the tip.
//
// Graph: one node pair (in_k, out_k) per word boundary k of a sentence.
//   in_k → out_k   ε, or an optional word (+w, +w@anchor, a determiner inserted before a noun)
//   out_k → in_j   the words k..j-1: literal readings, or the alternatives of a slot
//                  (contextual synonym, safe synonym, pronoun, determiner), or ε (-anchor)
// An optional word carries a bit; a path may use each bit once (+w "at most once").
// Every text (pattern side and answer side) goes through the Phase 1 normalisation
// (lib/typedAnswer + Phase 1 §3.2: contractions, numbers, noun + 's readings).

import { normalizeBasic } from '../typedAnswer.ts';
import { preNormalize, readings, type Level, type WordLookup } from '../offlineCheck.ts';

// ---------------------------------------------------------------------------
// Data shapes
// ---------------------------------------------------------------------------

export interface GroupForms {
  kind: 'safe' | 'contextual';
  pos: string;
  /** member lemmas */
  m: string[];
  /** form tag → surface strings of every member in that form */
  forms: Record<string, string[]>;
}
export interface SynForms {
  groups: Record<string, GroupForms>;
}

export interface LibraryItem {
  id: string;
  kind?: string;
  verdict: 'wrong' | 'correct_with_tip';
  pattern?: string;
  slots?: string[];
  sk: string;
  cz: string;
  en: string;
}
/** library item id → item (all topics merged; ids are unique by their type prefix) */
export type Library = Record<string, LibraryItem>;

/** [libId, wrongText] | [libId, wrongText, anchor] | [libId, wrongText, anchor|null, {slot: value}] */
export type MistakeRef = [string, string, (string | null)?, Record<string, string>?];

export interface Annotation {
  id: number;
  t: number;
  lv: Level;
  v: string[];
  lk?: string[];
  s?: Record<string, string>;
  g?: string[][];
  o?: Record<string, string>;
  d?: Record<string, string>;
  p?: string[];
  m?: MistakeRef[];
  ng?: Record<string, unknown>;
}

export interface Edge {
  to: number;
  /** normalised token, null = ε */
  tok: string | null;
  /** optional-word bit (0 = none); set on the first edge of the word's chain */
  bit: number;
}
export interface Graph {
  edges: Edge[][];
  order: number[];
  start: number;
  end: number;
  tokens: Set<string>;
}

export interface CompiledVariant {
  index: number;
  text: string;
  lockText: string;
  graphs: Graph[];
}
export interface CompiledMistake {
  libId: string;
  item: LibraryItem | null;
  verdict: 'wrong' | 'correct_with_tip';
  /** the wrong sentence (display words) */
  text: string;
  right: string;
  wrong: string;
  slots: Record<string, string>;
  variant: number;
  graphs: Graph[];
}
export interface Compiled {
  id: number;
  level: Level;
  topic: number;
  variants: CompiledVariant[];
  mistakes: CompiledMistake[];
  /** synonym groups the sentence uses (s references + safe groups found) */
  groups: Set<string>;
  /** problems found while compiling (anchor not found, anchor in lock, unknown group …) */
  notes: string[];
  /** typo neighbour list (real words one edit from a pattern token + the pattern tokens) */
  neighbours?: Set<string>;
}

// ---------------------------------------------------------------------------
// Words, anchors, locks
// ---------------------------------------------------------------------------

export interface WordSeq {
  raw: string[];
  display: string[];
}

const EDGE_PUNCT = /^[^\p{L}\p{N}']+|[^\p{L}\p{N}']+$/gu;

/** Words of a text: `raw` = normalizeBasic per word (lower case, no punctuation), `display` = as written. */
export const splitWords = (text: string): WordSeq => {
  const raw: string[] = [];
  const display: string[] = [];
  for (const piece of preNormalize(text).split(/\s+/)) {
    const norm = normalizeBasic(piece);
    if (!norm) continue;
    const parts = norm.split(' ');
    if (parts.length === 1) {
      raw.push(parts[0]);
      display.push(piece.replace(/[’‘‛ʼ`´]/g, "'").replace(EDGE_PUNCT, '') || parts[0]);
    } else for (const part of parts) { raw.push(part); display.push(part); }
  }
  return { raw, display };
};

export const normPhrase = (text: string): string => splitWords(text).raw.join(' ');

const readingCache = new Map<string, string[][]>();
/** Phase 1 readings of a phrase ("don't" → do not, "twenty-one" → 21, "car's" → car's / car is / car has). */
export const phraseReadings = (text: string): string[][] => {
  let r = readingCache.get(text);
  if (!r) {
    r = text.trim() ? readings(text) : [[]];
    if (r.length === 0) r = [[]];
    if (readingCache.size > 50000) readingCache.clear();
    readingCache.set(text, r);
  }
  return r;
};

export const parseAnchor = (anchor: string): { text: string; nth: number } => {
  const m = anchor.match(/^(.*?)#(\d+)$/);
  return m ? { text: m[1], nth: Math.max(1, Number(m[2])) } : { text: anchor, nth: 1 };
};

export const findSeq = (raw: string[], seq: string[], from = 0): number => {
  outer: for (let i = from; i + seq.length <= raw.length; i++) {
    for (let k = 0; k < seq.length; k++) if (raw[i + k] !== seq[k]) continue outer;
    return i;
  }
  return -1;
};

/** [start, end) of the nth occurrence of the anchor (case-insensitive, whole words). */
export const locateAnchor = (raw: string[], anchor: string): [number, number] | null => {
  const { text, nth } = parseAnchor(anchor);
  const seq = splitWords(text).raw;
  if (seq.length === 0) return null;
  let pos = -1;
  let from = 0;
  for (let c = 0; c < nth; c++) {
    pos = findSeq(raw, seq, from);
    if (pos < 0) return null;
    from = pos + 1;
  }
  return [pos, pos + seq.length];
};

export const lockPieces = (lock: string): string[] => lock.split(/\s+\.\.\s+/).map((p) => p.trim()).filter(Boolean);

/** Ranges of the lock pieces in order, null when a piece is missing. */
export const locateLock = (raw: string[], lock: string | undefined): [number, number][] | null => {
  if (!lock || !lock.trim()) return [];
  const out: [number, number][] = [];
  let from = 0;
  for (const piece of lockPieces(lock)) {
    const seq = splitWords(piece).raw;
    if (seq.length === 0) continue;
    const pos = findSeq(raw, seq, from);
    if (pos < 0) return null;
    out.push([pos, pos + seq.length]);
    from = pos + seq.length;
  }
  return out;
};

// ---------------------------------------------------------------------------
// Slot alternatives
// ---------------------------------------------------------------------------

export const DETERMINERS = new Set(['the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'some', 'any', 'no']);
export const DET_CODES: Record<string, string[]> = {
  A: ['the', 'a', 'an', 'this', 'that'],
  P: ['the', 'these', 'those', '∅'],
  Z: ['the', '∅'],
};

/** Determiner alternatives ('' = ∅), null when the value is invalid. a ≡ an. */
export const detAlternatives = (value: string): string[] | null => {
  const list = DET_CODES[value] ?? value.split('|').map((s) => s.trim()).filter(Boolean);
  if (list.length === 0) return null;
  const out = new Set<string>();
  for (const item of list) {
    if (item === '∅' || item === '0') out.add('');
    else if (/^[a-z' ]+$/i.test(item)) out.add(item.toLowerCase());
    else return null;
  }
  if (out.has('a') || out.has('an')) { out.add('a'); out.add('an'); }
  return [...out];
};

export const PERSONAL_PRONOUNS = new Set(['he', 'she', 'him', 'her', 'his', 'hers', 'himself', 'herself']);
/** Words after which "her" is an object (→ him), not a possessive (→ his). */
const NOT_A_NOUN = new Set([
  'to', 'at', 'in', 'on', 'with', 'for', 'from', 'by', 'of', 'about', 'into', 'onto', 'over', 'under', 'through', 'across',
  'and', 'but', 'or', 'so', 'because', 'when', 'while', 'if', 'that', 'than', 'as', 'before', 'after', 'until',
  'up', 'down', 'out', 'off', 'away', 'back', 'again', 'too', 'very', 'now', 'then', 'today', 'yesterday', 'tomorrow',
  'a', 'an', 'the', 'this', 'these', 'those', 'some', 'any', 'no', 'every', 'all', 'it', 'there', 'here', 'home',
  'alone', 'already', 'still', 'yet', 'soon', 'later', 'once', 'twice', 'is', 'was', 'will', 'would', 'can', 'could',
]);

/** The other gender of a pronoun, given the next word (her → his before a noun, him otherwise). */
export const flipPronoun = (word: string, next: string | undefined): string[] | null => {
  const nounFollows = next !== undefined && !NOT_A_NOUN.has(next);
  switch (word) {
    case 'he': return ['she'];
    case 'she': return ['he'];
    case 'him': return ['her'];
    case 'himself': return ['herself'];
    case 'herself': return ['himself'];
    case 'hers': return ['his'];
    case 'his': return nounFollows ? ['her'] : ['hers'];
    case 'her': return nounFollows ? ['his', 'him'] : ['him'];
    default: return null;
  }
};

/** Surfaces of a group in the anchor's form(s); null when the anchor is not a form of a member. */
export const groupAlternatives = (syn: SynForms, gid: string, anchorText: string): string[] | null => {
  const group = syn.groups[gid];
  if (!group) return null;
  const key = normPhrase(anchorText);
  const out = new Set<string>();
  for (const list of Object.values(group.forms)) {
    if (list.some((s) => normPhrase(s) === key)) for (const s of list) out.add(s);
  }
  return out.size ? [...out] : null;
};

interface SafeEntry { seq: string[]; alts: string[]; gid: string }
const safeCache = new WeakMap<SynForms, SafeEntry[]>();
const safeIndex = (syn: SynForms): SafeEntry[] => {
  let idx = safeCache.get(syn);
  if (idx) return idx;
  const bySurface = new Map<string, SafeEntry>();
  for (const [gid, group] of Object.entries(syn.groups)) {
    if (group.kind !== 'safe') continue;
    for (const list of Object.values(group.forms)) {
      for (const surface of list) {
        const key = `${gid}|${normPhrase(surface)}`;
        const entry = bySurface.get(key) ?? { seq: splitWords(surface).raw, alts: [], gid };
        for (const s of list) if (!entry.alts.includes(s)) entry.alts.push(s);
        bySurface.set(key, entry);
      }
    }
  }
  idx = [...bySurface.values()].filter((e) => e.seq.length > 0).sort((a, b) => b.seq.length - a.seq.length);
  safeCache.set(syn, idx);
  return idx;
};

// ---------------------------------------------------------------------------
// Graph building
// ---------------------------------------------------------------------------

class Builder {
  edges: Edge[][] = [];
  tokens = new Set<string>();
  private seen = new Set<string>();
  node(): number {
    this.edges.push([]);
    return this.edges.length - 1;
  }
  seq(from: number, to: number, toks: string[], bit = 0): void {
    const key = `${from}|${to}|${bit}|${toks.join(' ')}`;
    if (this.seen.has(key)) return;
    this.seen.add(key);
    if (toks.length === 0) {
      this.edges[from].push({ to, tok: null, bit });
      return;
    }
    let cur = from;
    toks.forEach((tok, i) => {
      const next = i === toks.length - 1 ? to : this.node();
      this.edges[cur].push({ to: next, tok, bit: i === 0 ? bit : 0 });
      this.tokens.add(tok);
      cur = next;
    });
  }
  build(start: number, end: number): Graph {
    const n = this.edges.length;
    const indeg = new Int32Array(n);
    for (const list of this.edges) for (const e of list) indeg[e.to]++;
    const order: number[] = [];
    const queue: number[] = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) queue.push(i);
    while (queue.length) {
      const u = queue.pop()!;
      order.push(u);
      for (const e of this.edges[u]) if (--indeg[e.to] === 0) queue.push(e.to);
    }
    return { edges: this.edges, order, start, end, tokens: this.tokens };
  }
}

export const MAX_GENDER_CHAINS = 3;
const MAX_BITS = 30;

interface Sentence {
  ws: WordSeq;
  lock: [number, number][];
}

interface Notes {
  list: string[];
  groups: Set<string>;
}

const note = (notes: Notes, text: string) => {
  if (!notes.list.includes(text)) notes.list.push(text);
};

/** One graph: the sentence with every freedom of the annotation, gender chains flipped per `flips` bit. */
export const sentenceGraph = (sent: Sentence, ann: Annotation, syn: SynForms, flips: number, notes: Notes): Graph => {
  const { raw } = sent.ws;
  const n = raw.length;
  const rangeOf = new Int32Array(n).fill(-1);
  sent.lock.forEach(([s, e], ri) => { for (let k = s; k < e; k++) rangeOf[k] = ri; });
  const spanned = new Array<boolean>(n).fill(false);
  const isFree = (s: number, e: number) => {
    for (let k = s; k < e; k++) if (spanned[k] || rangeOf[k] >= 0) return false;
    return true;
  };
  const spans: { s: number; e: number; alts: string[] }[] = [];
  const claim = (r: [number, number], alts: string[]): boolean => {
    if (!isFree(r[0], r[1])) return false;
    for (let k = r[0]; k < r[1]; k++) spanned[k] = true;
    spans.push({ s: r[0], e: r[1], alts });
    return true;
  };
  const anchorAt = (anchor: string, kind: string): [number, number] | null => {
    const r = locateAnchor(raw, anchor);
    if (!r) return null;
    for (let k = r[0]; k < r[1]; k++) if (rangeOf[k] >= 0) { note(notes, `${kind}_anchor_in_lock:${anchor}`); return null; }
    return r;
  };
  const textOf = (r: [number, number]) => raw.slice(r[0], r[1]).join(' ');
  const inserts: { at: number[] | null; alts: string[]; bit: number }[] = [];
  let nextBit = 0;
  const bit = () => (nextBit < MAX_BITS ? 1 << nextBit++ : 0);

  // s – contextual synonyms (same form)
  for (const [anchor, gid] of Object.entries(ann.s ?? {})) {
    const r = anchorAt(anchor, 's');
    if (!r) continue;
    notes.groups.add(gid);
    const alts = groupAlternatives(syn, gid, textOf(r));
    if (!alts) note(notes, syn.groups[gid] ? `s_anchor_not_a_form:${anchor}->${gid}` : `s_unknown_group:${gid}`);
    if (!claim(r, [textOf(r), ...(alts ?? [])])) note(notes, `s_overlap:${anchor}`);
  }
  // g – gender chains (a flipped chain replaces every one of its anchors)
  (ann.g ?? []).slice(0, MAX_GENDER_CHAINS).forEach((chain, ci) => {
    if (!(flips & (1 << ci))) return;
    for (const anchor of chain) {
      const r = anchorAt(anchor, 'g');
      if (!r) continue;
      const alts = r[1] - r[0] === 1 ? flipPronoun(raw[r[0]], raw[r[0] + 1]) : null;
      if (!alts) { note(notes, `g_not_a_pronoun:${anchor}`); continue; }
      if (!claim(r, alts)) note(notes, `g_overlap:${anchor}`);
    }
  });
  // o – single pronoun alternatives
  for (const [anchor, value] of Object.entries(ann.o ?? {})) {
    const r = anchorAt(anchor, 'o');
    if (!r) continue;
    if (!claim(r, [textOf(r), ...value.split('|').map((x) => x.trim()).filter(Boolean)])) note(notes, `o_overlap:${anchor}`);
  }
  // d – determiner freedom
  for (const [anchor, value] of Object.entries(ann.d ?? {})) {
    const r = anchorAt(anchor, 'd');
    if (!r) continue;
    const alts = detAlternatives(value);
    if (!alts) { note(notes, `d_invalid:${anchor}=${value}`); continue; }
    if (r[1] - r[0] === 1 && DETERMINERS.has(raw[r[0]])) {
      if (!claim(r, [textOf(r), ...alts])) note(notes, `d_overlap:${anchor}`);
    } else {
      // the anchor has no determiner: one may be inserted right before it
      inserts.push({ at: [r[0]], alts: alts.filter(Boolean), bit: bit() });
    }
  }
  // p – optional words
  const skips: [number, number][] = [];
  for (const entry of ann.p ?? []) {
    if (entry.startsWith('-')) {
      const r = anchorAt(entry.slice(1), 'p');
      if (r) skips.push(r);
    } else if (entry.startsWith('+')) {
      const body = entry.slice(1);
      const at = body.lastIndexOf('@');
      if (at > 0) {
        const r = anchorAt(body.slice(at + 1), 'p');
        if (r) inserts.push({ at: [r[1]], alts: [body.slice(0, at)], bit: bit() });
      } else inserts.push({ at: null, alts: [body], bit: bit() });
    } else note(notes, `p_invalid:${entry}`);
  }
  // safe groups – everywhere outside the lock and the annotated slots
  for (const entry of safeIndex(syn)) {
    let from = 0;
    for (;;) {
      const pos = findSeq(raw, entry.seq, from);
      if (pos < 0) break;
      if (claim([pos, pos + entry.seq.length], entry.alts)) notes.groups.add(entry.gid);
      from = pos + 1;
    }
  }

  // build
  const b = new Builder();
  const inN: number[] = [];
  const outN: number[] = [];
  for (let k = 0; k <= n; k++) {
    inN.push(b.node());
    outN.push(b.node());
    b.seq(inN[k], outN[k], []);
  }
  for (let k = 0; k < n; k++) {
    if (spanned[k]) continue;
    for (const r of phraseReadings(raw[k])) b.seq(outN[k], inN[k + 1], r);
    // number phrases spread over several words ("twenty one" = 21)
    for (let len = 2; len <= 4 && k + len <= n; len++) {
      let ok = true;
      for (let j = k; j < k + len; j++) if (spanned[j]) ok = false;
      if (!ok) break;
      for (const r of phraseReadings(raw.slice(k, k + len).join(' '))) {
        if (r.length < len && r.some((t) => /^\d+$/.test(t))) b.seq(outN[k], inN[k + len], r);
      }
    }
  }
  for (const span of spans) for (const alt of span.alts) for (const r of phraseReadings(alt)) b.seq(outN[span.s], inN[span.e], r);
  for (const [s, e] of skips) b.seq(outN[s], inN[e], []);
  const lockInterior = (k: number) => k > 0 && k < n && rangeOf[k - 1] >= 0 && rangeOf[k - 1] === rangeOf[k];
  for (const ins of inserts) {
    const at = ins.at ?? Array.from({ length: n + 1 }, (_, k) => k).filter((k) => !lockInterior(k));
    for (const k of at) for (const alt of ins.alts) for (const r of phraseReadings(alt)) if (r.length) b.seq(inN[k], outN[k], r, ins.bit);
  }
  return b.build(inN[0], outN[n]);
};

// ---------------------------------------------------------------------------
// Compile
// ---------------------------------------------------------------------------

const replaceRange = (ws: WordSeq, s: number, e: number, text: string): { ws: WordSeq; len: number } => {
  const rep = splitWords(text);
  return {
    ws: { raw: [...ws.raw.slice(0, s), ...rep.raw, ...ws.raw.slice(e)], display: [...ws.display.slice(0, s), ...rep.display, ...ws.display.slice(e)] },
    len: rep.raw.length,
  };
};
const shift = (ranges: [number, number][], after: number, delta: number): [number, number][] =>
  ranges.map(([s, e]) => (s >= after ? [s + delta, e + delta] : [s, e]) as [number, number]);

export interface CompileOptions {
  /** full word list: builds the typo neighbour list into compiled.neighbours */
  words?: WordLookup;
  /** compile only these variant indexes (lint: "is v_i a mere freedom swap of v_j") */
  only?: number[];
  /** skip the mistake patterns */
  noMistakes?: boolean;
}

export const compile = (ann: Annotation, syn: SynForms, library: Library, options: CompileOptions = {}): Compiled => {
  const notes: Notes = { list: [], groups: new Set() };
  const chains = Math.min((ann.g ?? []).length, MAX_GENDER_CHAINS);
  const graphsOf = (sent: Sentence): Graph[] =>
    Array.from({ length: 1 << chains }, (_, flips) => sentenceGraph(sent, ann, syn, flips, notes));

  const sentences: { index: number; sent: Sentence; lockText: string }[] = [];
  ann.v.forEach((text, index) => {
    const ws = splitWords(text);
    const lockText = ann.lk?.[index] ?? '';
    const lock = locateLock(ws.raw, lockText);
    if (!lock) note(notes, `lock_not_found:v${index}:${lockText}`);
    sentences.push({ index, sent: { ws, lock: lock ?? [] }, lockText });
  });

  const variants: CompiledVariant[] = sentences
    .filter((s) => !options.only || options.only.includes(s.index))
    .map(({ index, sent, lockText }) => ({ index, text: ann.v[index], lockText, graphs: graphsOf(sent) }));

  const mistakes: CompiledMistake[] = [];
  if (!options.noMistakes) {
    const seen = new Set<string>();
    for (const ref of ann.m ?? []) {
      const [libId, wrongText, anchor, extra] = ref;
      const item = library[libId] ?? null;
      if (!item) note(notes, `m_unknown_item:${libId}`);
      const verdict = item?.verdict ?? 'wrong';
      const push = (variant: number, sent: Sentence, right: string, wrong: string) => {
        const key = `${libId}|${sent.ws.raw.join(' ')}`;
        if (seen.has(key)) return;
        seen.add(key);
        mistakes.push({ libId, item, verdict, text: sent.ws.display.join(' '), right, wrong, slots: extra ?? {}, variant, graphs: graphsOf(sent) });
      };
      if (typeof wrongText !== 'string') { note(notes, `m_invalid:${libId}`); continue; }
      if (wrongText.startsWith('=')) {
        const ws = splitWords(wrongText.slice(1));
        push(0, { ws, lock: locateLock(ws.raw, ann.lk?.[0]) ?? [] }, (ann.lk?.[0] ?? '').replace(/ \.\. /g, ' … '), wrongText.slice(1));
        continue;
      }
      let used = false;
      for (const { index, sent } of sentences) {
        if (anchor) {
          const r = locateAnchor(sent.ws.raw, anchor);
          if (!r) continue;
          const right = sent.ws.display.slice(r[0], r[1]).join(' ');
          const { ws, len } = replaceRange(sent.ws, r[0], r[1], wrongText);
          const lock = shift(sent.lock, r[1], len - (r[1] - r[0]));
          if (len) lock.push([r[0], r[0] + len]);
          push(index, { ws, lock }, right, wrongText);
          used = true;
        } else {
          if (sent.lock.length === 0) continue;
          const right = sent.lock.map(([s, e]) => sent.ws.display.slice(s, e).join(' ')).join(' … ');
          const pieces = lockPieces(wrongText);
          let ws = sent.ws;
          let lock: [number, number][] = [];
          if (pieces.length === sent.lock.length && pieces.length > 1) {
            for (let p = sent.lock.length - 1; p >= 0; p--) {
              const [s, e] = sent.lock[p];
              const res = replaceRange(ws, s, e, pieces[p]);
              ws = res.ws;
              lock = shift(lock, e, res.len - (e - s));
              if (res.len) lock.unshift([s, s + res.len]);
            }
          } else {
            const s = sent.lock[0][0];
            const e = sent.lock[sent.lock.length - 1][1];
            const res = replaceRange(ws, s, e, wrongText);
            ws = res.ws;
            if (res.len) lock = [[s, s + res.len]];
          }
          push(index, { ws, lock }, right, wrongText.replace(/ \.\. /g, ' … '));
          used = true;
        }
      }
      if (!used) note(notes, `m_not_applicable:${libId}:${wrongText}${anchor ? '@' + anchor : ''}`);
    }
  }

  const compiled: Compiled = { id: ann.id, level: ann.lv, topic: ann.t, variants, mistakes, groups: notes.groups, notes: notes.list };
  if (options.words) compiled.neighbours = typoNeighbours(compiled, options.words);
  return compiled;
};

// ---------------------------------------------------------------------------
// Typo neighbour list
// ---------------------------------------------------------------------------

const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
export const edits1 = (word: string): Set<string> => {
  const out = new Set<string>();
  for (let i = 0; i <= word.length; i++) {
    const a = word.slice(0, i);
    const b = word.slice(i);
    if (b) out.add(a + b.slice(1));
    if (b.length > 1) out.add(a + b[1] + b[0] + b.slice(2));
    for (const c of ALPHABET) {
      if (b) out.add(a + c + b.slice(1));
      out.add(a + c + b);
    }
  }
  out.delete(word);
  return out;
};

/** Every real word one edit away from a token of an accepted path, plus the real-word tokens themselves:
 *  all the device needs for the "typed word is a real word" exclusion and the BrE/AmE rules. */
export const typoNeighbours = (compiled: Compiled, words: WordLookup): Set<string> => {
  const out = new Set<string>();
  const tokens = new Set<string>();
  for (const v of compiled.variants) for (const g of v.graphs) for (const t of g.tokens) tokens.add(t);
  for (const t of tokens) {
    if (!/^[a-z]+$/.test(t)) continue;
    if (words.has(t)) out.add(t);
    if (t.length < 3) continue;
    for (const c of edits1(t)) if (words.has(c)) out.add(c);
  }
  return out;
};

// ---------------------------------------------------------------------------
// Matching
// ---------------------------------------------------------------------------

/** Exact match of one answer reading against a graph (each optional-word bit used at most once). */
export const matchGraph = (g: Graph, toks: string[], eq?: (a: string, t: string) => boolean): boolean => {
  const L = toks.length;
  const N = g.edges.length;
  const seen = new Set<number>();
  const stack: number[] = [g.start, 0, 0];
  while (stack.length) {
    const mask = stack.pop()!;
    const p = stack.pop()!;
    const u = stack.pop()!;
    if (u === g.end && p === L) return true;
    const key = (mask * N + u) * (L + 1) + p;
    if (seen.has(key)) continue;
    seen.add(key);
    for (const e of g.edges[u]) {
      if (e.bit && mask & e.bit) continue;
      const nm = mask | e.bit;
      if (e.tok === null) stack.push(e.to, p, nm);
      else if (p < L && (toks[p] === e.tok || (eq !== undefined && eq(toks[p], e.tok)))) stack.push(e.to, p + 1, nm);
    }
  }
  return false;
};

export interface Alignment {
  cost: number;
  /** the pattern tokens of the closest path */
  path: string[];
}

/** Weighted edit distance of an answer reading to the closest path of the graph
 *  (insert / delete cost 1, substitute = subCost). Optional-word bits are not
 *  enforced here (only the tip uses this). */
export const alignGraph = (g: Graph, toks: string[], subCost: (a: string, t: string) => number): Alignment => {
  const L = toks.length;
  const W = L + 1;
  const N = g.edges.length;
  const D = new Float64Array(N * W).fill(Infinity);
  const prev = new Int32Array(N * W).fill(-1);
  const via: (string | null)[] = new Array(N * W).fill(null);
  D[g.start * W] = 0;
  const relax = (cell: number, cost: number, from: number, tok: string | null) => {
    if (cost < D[cell]) { D[cell] = cost; prev[cell] = from; via[cell] = tok; }
  };
  for (const u of g.order) {
    const base = u * W;
    for (let j = 0; j < L; j++) if (D[base + j] + 1 < D[base + j + 1]) relax(base + j + 1, D[base + j] + 1, base + j, null);
    for (const e of g.edges[u]) {
      const vb = e.to * W;
      for (let j = 0; j <= L; j++) {
        const c = D[base + j];
        if (c === Infinity) continue;
        if (e.tok === null) { relax(vb + j, c, base + j, null); continue; }
        relax(vb + j, c + 1, base + j, e.tok);
        if (j < L) relax(vb + j + 1, c + (toks[j] === e.tok ? 0 : subCost(toks[j], e.tok)), base + j, e.tok);
      }
    }
  }
  const endCell = g.end * W + L;
  const path: string[] = [];
  let cell = endCell;
  let guard = N * W + 1;
  while (cell !== g.start * W && cell >= 0 && guard-- > 0) {
    if (via[cell] !== null) path.push(via[cell]!);
    cell = prev[cell];
  }
  return { cost: D[endCell], path: path.reverse() };
};

/** Graph size (nodes + edges) – "the most complex compiled sentence". */
export const graphSize = (c: Compiled): number => {
  let size = 0;
  for (const v of [...c.variants, ...c.mistakes]) for (const g of v.graphs) size += g.edges.length + g.edges.reduce((a, l) => a + l.length, 0);
  return size;
};

/** Library index from the mistakes/<type_id>.json files. */
export const libraryIndex = (files: { type_id?: number; items?: LibraryItem[] }[]): Library => {
  const out: Library = {};
  for (const f of files) for (const item of f.items ?? []) out[item.id] = item;
  return out;
};
