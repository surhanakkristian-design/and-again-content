// Phase 1b – the offline check (FORMAT_SPEC.md §4). Pure functions.
//   normalise (lib/typedAnswer + Phase 1 §3.2) →
//   1  any variant with all freedoms                              → correct
//   1b the same, British/American spelling pairs counted as equal → correct
//   2  any library mistake pattern (same freedoms)                → item verdict + filled feedback
//   3  exactly one typo on the closest path (Phase 1 exclusions)  → correct_with_tip
//   4  wrong + automatic tip from the closest path including every freedom
// Feedback language (Phase 1): sk → sk, cz/cs → cz, others → en at B1/B2, none at A1/A2; ≤150 characters.

import { normalizeBasic, variantForms } from '../typedAnswer.ts';
import {
  buildTip,
  feedbackLanguage,
  isSpellingVariant,
  isTypo,
  preNormalize,
  readings,
  MAX_FEEDBACK_CHARS,
  TEMPLATES,
  type FeedbackLanguage,
  type Level,
  type Verdict,
  type WordLookup,
} from '../offlineCheck.ts';
import { alignGraph, matchGraph, type Compiled, type CompiledMistake } from './match.ts';

export type StepV2 = 'match' | 'spelling_variant' | 'mistake' | 'typo' | 'auto';

export interface CheckOptions {
  /** learner's native language (sk, cz/cs, de, …) */
  native: string;
  /** defaults to the annotation's level */
  level?: Level;
  /** word lookup for the typo exclusions; defaults to compiled.neighbours */
  words?: WordLookup;
}

export interface CheckResultV2 {
  verdict: Verdict;
  step: StepV2;
  feedback: string | null;
  /** steps 3 and 4: log the answer anonymously */
  unmatched: boolean;
  /** the accepted sentence the answer matched, or the closest accepted path */
  closest: string;
  variant?: number;
  mistake?: string;
}

const EMPTY: WordLookup = { has: () => false };
/** Answer readings used for the (costlier) closest-path search. */
const MAX_ALIGN_READINGS = 8;
const TYPO_COST = 0.5;

/** Lower-case token → how the sentence writes it mid-sentence (names, "I"); digits → the number word used. */
const displayMapper = (source: string): ((token: string) => string) => {
  const cased = new Map<string, string>();
  source.split(/\s+/).forEach((word, index) => {
    const bare = word.replace(/^[^\p{L}\p{N}']+|[^\p{L}\p{N}']+$/gu, '');
    const lower = bare.toLowerCase();
    if (index > 0 && bare !== lower && !cased.has(lower)) cased.set(lower, bare);
    const form = Array.from(variantForms(normalizeBasic(bare), 'en'))[0];
    if (form && /^\d+$/.test(form) && form !== lower && !cased.has(form)) cased.set(form, lower);
  });
  return (token) => cased.get(token) ?? (token === 'i' ? 'I' : token);
};

const sentenceOf = (tokens: string[], source: string): string => {
  const show = displayMapper(source);
  const text = tokens.map(show).join(' ');
  const end = source.trim().match(/[.!?]$/)?.[0] ?? '';
  return text ? text[0].toUpperCase() + text.slice(1) + end : source;
};

const pick = (m: CompiledMistake, language: FeedbackLanguage): string | null => {
  const item = m.item;
  if (!item) return null;
  const template = language === 'sk' ? item.sk : language === 'cz' ? item.cz : item.en;
  return template && template.trim() ? template.trim() : null;
};

/** Library feedback with {right}/{wrong} from the match and the per-sentence slots; null if a slot stays empty. */
export const fillFeedback = (m: CompiledMistake, language: FeedbackLanguage | null): string | null => {
  if (!language) return null;
  const template = pick(m, language);
  if (!template) return null;
  const values: Record<string, string> = { right: m.right, wrong: m.wrong, ...m.slots };
  let missing = false;
  const text = template.replace(/\{(\w+)\}/g, (_, key: string) => {
    const value = values[key];
    if (value === undefined || value === '') { missing = true; return ''; }
    return value;
  });
  return missing ? null : text;
};

export const check = (answer: string, compiled: Compiled, options: CheckOptions): CheckResultV2 => {
  const level = options.level ?? compiled.level;
  const language = feedbackLanguage(options.native, level);
  const words = options.words ?? compiled.neighbours ?? EMPTY;
  const reference = compiled.variants[0]?.text ?? '';
  if (normalizeBasic(preNormalize(answer)).length === 0) {
    return { verdict: 'wrong', step: 'auto', feedback: null, unmatched: false, closest: reference };
  }
  const answerReadings = readings(answer);

  // 1. any variant with all freedoms
  for (const v of compiled.variants) {
    for (const g of v.graphs) for (const r of answerReadings) {
      if (matchGraph(g, r)) return { verdict: 'correct', step: 'match', feedback: null, unmatched: false, closest: v.text, variant: v.index };
    }
  }
  // 1b. British / American spelling
  const spelling = (a: string, t: string) => isSpellingVariant(a, t, words);
  for (const v of compiled.variants) {
    for (const g of v.graphs) for (const r of answerReadings) {
      if (matchGraph(g, r, spelling)) return { verdict: 'correct', step: 'spelling_variant', feedback: null, unmatched: false, closest: v.text, variant: v.index };
    }
  }

  // closest path (steps 3 and 4, and the fallback tip of an over-long library text)
  const typoCache = new Map<string, boolean>();
  const typo = (a: string, t: string): boolean => {
    const key = `${a}${t}`;
    let r = typoCache.get(key);
    if (r === undefined) {
      r = Math.abs(a.length - t.length) <= 1 && isTypo(a, t, words);
      typoCache.set(key, r);
    }
    return r;
  };
  const subCost = (a: string, t: string) => (typo(a, t) ? TYPO_COST : 1);
  let best: { cost: number; answer: string[]; path: string[]; text: string; variant: number } | null = null;
  const closest = () => {
    if (best) return best;
    for (const v of compiled.variants) {
      for (const g of v.graphs) for (const r of answerReadings.slice(0, MAX_ALIGN_READINGS)) {
        const a = alignGraph(g, r, subCost);
        if (!best || a.cost < best.cost) best = { cost: a.cost, answer: r, path: a.path, text: v.text, variant: v.index };
      }
    }
    return best!;
  };
  const autoTip = () => {
    const b = closest();
    if (!language) return null;
    // cost 0 = only an optional word used twice (the edit search does not count bits);
    // Phase 1 buildTip needs a difference, so describe it generically
    if (b.answer.join(' ') === b.path.join(' ')) return TEMPLATES[language].generic;
    return buildTip(b.answer, b.path, b.text, language);
  };

  // 2. library mistakes
  for (const m of compiled.mistakes) {
    for (const g of m.graphs) for (const r of answerReadings) {
      if (!matchGraph(g, r)) continue;
      let feedback = fillFeedback(m, language);
      if (language && (!feedback || feedback.length > MAX_FEEDBACK_CHARS)) feedback = autoTip();
      return { verdict: m.verdict, step: 'mistake', feedback, unmatched: false, closest: compiled.variants.find((v) => v.index === m.variant)?.text ?? reference, variant: m.variant, mistake: m.libId };
    }
  }

  const b = closest();
  // 3. one typo on the closest path
  if (b.cost === TYPO_COST && b.answer.length === b.path.length) {
    const diffs: number[] = [];
    b.answer.forEach((token, k) => { if (token !== b.path[k]) diffs.push(k); });
    if (diffs.length === 1 && isTypo(b.answer[diffs[0]], b.path[diffs[0]], words)) {
      const shown = displayMapper(b.text)(b.path[diffs[0]]);
      return {
        verdict: 'correct_with_tip', step: 'typo', feedback: language ? TEMPLATES[language].typo(shown) : null,
        unmatched: true, closest: sentenceOf(b.path, b.text), variant: b.variant,
      };
    }
  }
  // 4. wrong + tip from the closest path
  return { verdict: 'wrong', step: 'auto', feedback: autoTip(), unmatched: true, closest: sentenceOf(b.path, b.text), variant: b.variant };
};
