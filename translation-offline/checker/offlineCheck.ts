// "Translate the sentence" – offline answer check (Phase 1 pilot, content repo).
// Pure functions, no React, no Supabase: `node --test checker/*.test.ts`.
// Spec: docs/features/reports/TRANSLATION_OFFLINE_PHASE1_REPORT.md §3 (app repo).
//
// Order of the steps:
//   1. the answer matches the reference or an acceptable translation → correct
//      (1b: the only differences are British/American spellings → correct)
//   2. it matches a stored typical mistake → that mistake's verdict + feedback
//   3. exactly one word is one edit away from the same word of an accepted
//      sentence, that word has ≥ 4 letters, and the typed word is neither a
//      real English word nor another form of the same word → correct_with_tip
//   4. anything else → wrong, with a tip built from a word-by-word alignment
//      against the closest accepted sentence
// "Matches" always means the typed-answer normalisation of lib/typedAnswer.ts
// (case, whitespace, punctuation, apostrophes, diacritics, English
// contractions, number words): the level-B form sets of the two sides share a
// member.

import { normalizeBasic, variantForms } from './typedAnswer.ts';

export type Verdict = 'correct' | 'correct_with_tip' | 'wrong';
export type Level = 'A1' | 'A2' | 'B1' | 'B2';
export type FeedbackLanguage = 'sk' | 'cz' | 'en';
export type CheckStep = 'reference' | 'acceptable' | 'spelling_variant' | 'mistake' | 'typo' | 'auto';

export interface MistakeEntry {
  text: string;
  verdict: 'wrong' | 'correct_with_tip';
  feedback_sk: string;
  feedback_cz: string;
  feedback_en: string | null;
}

/** What the device holds for one exercise (expanded sentences, no slots). */
export interface ExerciseCheckData {
  level: Level;
  reference: string;
  acceptable: string[];
  mistakes: MistakeEntry[];
}

export interface CheckResult {
  verdict: Verdict;
  /** Text for the feedback panel, null = show only the correct sentence. */
  feedback: string | null;
  step: CheckStep;
  /** The accepted sentence the answer was matched or aligned against. */
  closest: string;
  /** True for steps 3 and 4: the answer is in no stored list → log it anonymously. */
  unmatched: boolean;
}

/** A lower-case English word list (see wordlist/). */
export interface WordLookup {
  has(word: string): boolean;
}

export const MAX_FEEDBACK_CHARS = 150;

// ---------------------------------------------------------------------------
// Feedback language (decision 4)
// ---------------------------------------------------------------------------

/** sk → Slovak, cz → Czech (all levels); any other native language → English
 *  at B1/B2, no feedback text at A1/A2. */
export const feedbackLanguage = (nativeLanguage: string, level: Level): FeedbackLanguage | null => {
  const native = nativeLanguage.toLowerCase();
  if (native === 'sk') return 'sk';
  if (native === 'cz' || native === 'cs') return 'cz';
  return level === 'B1' || level === 'B2' ? 'en' : null;
};

const pickFeedback = (mistake: MistakeEntry, language: FeedbackLanguage | null): string | null => {
  if (!language) return null;
  const text = language === 'sk' ? mistake.feedback_sk : language === 'cz' ? mistake.feedback_cz : mistake.feedback_en;
  return text && text.trim() ? text.trim() : null;
};

// ---------------------------------------------------------------------------
// Forms
// ---------------------------------------------------------------------------

/** Characters lib/typedAnswer.ts does not treat as punctuation yet (typographic
 *  double quotes, dashes, brackets). Mapped before its normalisation; to be
 *  folded into the shared normaliser in Phase 2. */
const EXTRA_PUNCTUATION = /[“”„‟″«»()\[\]–—]/g;
export const preNormalize = (text: string): string => text.replace(EXTRA_PUNCTUATION, ' ');

/** Pronoun heads whose 's lib/typedAnswer.ts already expands. */
const S_HEADS = new Set(['he', 'she', 'it', 'that', 'there', 'here', 'what', 'who', 'where', 'how']);
const MAX_FORMS = 64;

/** Level-B forms (lib/typedAnswer.ts) plus one extension: "globe's got" may
 *  be "globe has got" and "the car's broken" "the car is broken" – a noun + 's
 *  also reads as noun + is / has (the possessive reading stays too). */
export const formsOf = (text: string): Set<string> => {
  const forms = new Set<string>();
  for (const form of variantForms(normalizeBasic(preNormalize(text)), 'en')) {
    let readings: string[][] = [[]];
    for (const token of form.split(' ').filter(Boolean)) {
      const stem = token.endsWith("'s") && token.length > 2 ? token.slice(0, -2) : null;
      const options = stem && !S_HEADS.has(stem) ? [[token], [stem, 'is'], [stem, 'has']] : [[token]];
      const next: string[][] = [];
      for (const reading of readings) for (const option of options) if (next.length < MAX_FORMS) next.push([...reading, ...option]);
      readings = next;
    }
    for (const reading of readings) if (forms.size < MAX_FORMS) forms.add(reading.join(' '));
  }
  return forms;
};

/** All readings of a sentence as token arrays. */
export const readings = (text: string): string[][] =>
  Array.from(formsOf(text)).map((form) => form.split(' ').filter(Boolean));

const sameReading = (answerForms: Set<string>, text: string): boolean => {
  for (const form of formsOf(text)) if (answerForms.has(form)) return true;
  return false;
};

// ---------------------------------------------------------------------------
// Step 1b – British / American spelling pairs
// ---------------------------------------------------------------------------

const SPELLING_PAIRS = new Map<string, string>([
  ['grey', 'gray'], ['greys', 'grays'], ['programme', 'program'], ['programmes', 'programs'],
  ['catalogue', 'catalog'], ['dialogue', 'dialog'], ['tyre', 'tire'], ['tyres', 'tires'],
  ['pyjamas', 'pajamas'], ['aluminium', 'aluminum'], ['jewellery', 'jewelry'], ['cheque', 'check'],
  ['mum', 'mom'], ['mums', 'moms'], ['plough', 'plow'], ['moustache', 'mustache'], ['cosy', 'cozy'],
  ['doughnut', 'donut'], ['doughnuts', 'donuts'], ['kerb', 'curb'], ['storey', 'story'],
  ['travelled', 'traveled'], ['travelling', 'traveling'], ['traveller', 'traveler'], ['travellers', 'travelers'],
  ['cancelled', 'canceled'], ['cancelling', 'canceling'], ['labelled', 'labeled'], ['modelling', 'modeling'],
  ['fuelled', 'fueled'], ['levelled', 'leveled'], ['signalled', 'signaled'], ['jewelled', 'jeweled'],
  ['practise', 'practice'], ['practised', 'practiced'], ['practising', 'practicing'], ['licence', 'license'],
  ['defence', 'defense'], ['offence', 'offense'], ['sceptical', 'skeptical'], ['skilful', 'skillful'],
  ['enrol', 'enroll'], ['fulfil', 'fulfill'], ['ageing', 'aging'], ['judgement', 'judgment'],
]);

/** Rule-based British → American spelling, only accepted when the result is
 *  a word of the list (so "four" never becomes "for": "for" is not reached by
 *  the -our rule, which needs two letters before it and a known result). */
const americanSpellings = (word: string, words: WordLookup): string[] => {
  const out: string[] = [];
  const pair = SPELLING_PAIRS.get(word);
  if (pair) out.push(pair);
  const rules: [RegExp, string][] = [
    [/^([a-z]{2,})our(s|ed|ing|ite|ites|ful|less|able|er|ers)?$/, '$1or$2'],
    [/^([a-z]{3,})is(e|es|ed|ing|ation|ations|er|ers)$/, '$1iz$2'],
    [/^([a-z]{2,})ys(e|es|ed|ing)$/, '$1yz$2'],
    [/^([a-z]*[^aeiou])tre(s)?$/, '$1ter$2'],
    [/^([a-z]{3,})ogue(s)?$/, '$1og$2'],
  ];
  for (const [rule, replacement] of rules) {
    if (rule.test(word)) {
      const american = word.replace(rule, replacement);
      if (american !== word && words.has(american)) out.push(american);
    }
  }
  return out;
};

export const isSpellingVariant = (a: string, b: string, words: WordLookup): boolean =>
  a !== b && (americanSpellings(a, words).includes(b) || americanSpellings(b, words).includes(a));

// ---------------------------------------------------------------------------
// Step 3 – one typo
// ---------------------------------------------------------------------------

/** Optimal string alignment distance (insert, delete, substitute, swap of two
 *  neighbours), generic over strings and token arrays. */
export const osaDistance = <T>(a: ArrayLike<T>, b: ArrayLike<T>): number => {
  const rows = a.length + 1;
  const cols = b.length + 1;
  const d: number[][] = Array.from({ length: rows }, (_, i) => {
    const row = new Array<number>(cols).fill(0);
    row[0] = i;
    return row;
  });
  for (let j = 0; j < cols; j++) d[0][j] = j;
  for (let i = 1; i < rows; i++) {
    for (let j = 1; j < cols; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost);
      if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
        d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
      }
    }
  }
  return d[a.length][b.length];
};

/** Endings whose addition or removal is ONE edit and makes another form of
 *  the same word (childs, mouses, sleded is 2 edits and never reaches here). */
const FORM_ENDINGS = ['s', 'd', 'r', 'n', 'y'];

export const isOtherFormOfSameWord = (typed: string, target: string): boolean =>
  FORM_ENDINGS.some((ending) => typed === target + ending || target === typed + ending);

export const MIN_TYPO_WORD_LENGTH = 4;

export const isTypo = (typed: string, target: string, words: WordLookup): boolean =>
  target.length >= MIN_TYPO_WORD_LENGTH &&
  /^[a-z]+$/.test(typed) &&
  /^[a-z]+$/.test(target) &&
  osaDistance(typed, target) === 1 &&
  !words.has(typed) &&
  !isOtherFormOfSameWord(typed, target);

// ---------------------------------------------------------------------------
// Step 4 – alignment tip
// ---------------------------------------------------------------------------

type Op =
  | { kind: 'same'; a: string; t: string }
  | { kind: 'sub'; a: string; t: string }
  | { kind: 'ins'; t: string } // missing in the answer
  | { kind: 'del'; a: string } // extra in the answer
  | { kind: 'swap'; a: [string, string]; t: [string, string] };

const alignTokens = (answer: string[], target: string[]): Op[] => {
  const n = answer.length;
  const m = target.length;
  const d: number[][] = Array.from({ length: n + 1 }, () => new Array<number>(m + 1).fill(0));
  for (let i = 0; i <= n; i++) d[i][0] = i;
  for (let j = 0; j <= m; j++) d[0][j] = j;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      const cost = answer[i - 1] === target[j - 1] ? 0 : 1;
      d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost);
      if (i > 1 && j > 1 && answer[i - 1] === target[j - 2] && answer[i - 2] === target[j - 1]) {
        d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
      }
    }
  }
  const ops: Op[] = [];
  let i = n;
  let j = m;
  while (i > 0 || j > 0) {
    if (i > 0 && j > 0 && answer[i - 1] === target[j - 1] && d[i][j] === d[i - 1][j - 1]) {
      ops.push({ kind: 'same', a: answer[i - 1], t: target[j - 1] });
      i--; j--;
    } else if (i > 1 && j > 1 && answer[i - 1] === target[j - 2] && answer[i - 2] === target[j - 1] && d[i][j] === d[i - 2][j - 2] + 1) {
      ops.push({ kind: 'swap', a: [answer[i - 2], answer[i - 1]], t: [target[j - 2], target[j - 1]] });
      i -= 2; j -= 2;
    } else if (i > 0 && j > 0 && d[i][j] === d[i - 1][j - 1] + 1) {
      ops.push({ kind: 'sub', a: answer[i - 1], t: target[j - 1] });
      i--; j--;
    } else if (j > 0 && d[i][j] === d[i][j - 1] + 1) {
      ops.push({ kind: 'ins', t: target[j - 1] });
      j--;
    } else {
      ops.push({ kind: 'del', a: answer[i - 1] });
      i--;
    }
  }
  return ops.reverse();
};

interface Region {
  answer: string[];
  target: string[];
  order: boolean;
}

const regionsOf = (ops: Op[]): Region[] => {
  const regions: Region[] = [];
  let current: Region | null = null;
  for (const op of ops) {
    if (op.kind === 'same') {
      current = null;
      continue;
    }
    if (!current) {
      current = { answer: [], target: [], order: false };
      regions.push(current);
    }
    if (op.kind === 'sub') { current.answer.push(op.a); current.target.push(op.t); }
    if (op.kind === 'ins') current.target.push(op.t);
    if (op.kind === 'del') current.answer.push(op.a);
    if (op.kind === 'swap') { current.answer.push(...op.a); current.target.push(...op.t); current.order = true; }
  }
  return regions;
};

const sortedKey = (tokens: string[]): string => [...tokens].sort().join(' ');

type Templates = {
  replace: (a: string, t: string) => string;
  missing: (t: string) => string;
  extra: (a: string) => string;
  order: (t: string) => string;
  orderGeneric: string;
  generic: string;
  typo: (t: string) => string;
};

const q = (language: FeedbackLanguage, text: string): string => (language === 'en' ? `“${text}”` : `„${text}“`);

export const TEMPLATES: Record<FeedbackLanguage, Templates> = {
  sk: {
    replace: (a, t) => `Namiesto ${q('sk', a)} patrí ${q('sk', t)}.`,
    missing: (t) => `Chýba ${q('sk', t)}.`,
    extra: (a) => `${q('sk', a)} tu nepatrí.`,
    order: (t) => `Pozor na poradie slov: ${q('sk', t)}.`,
    orderGeneric: 'Pozor na poradie slov.',
    generic: 'Porovnaj svoju vetu so správnym prekladom.',
    typo: (t) => `Preklep: správne je ${q('sk', t)}.`,
  },
  cz: {
    replace: (a, t) => `Místo ${q('cz', a)} patří ${q('cz', t)}.`,
    missing: (t) => `Chybí ${q('cz', t)}.`,
    extra: (a) => `${q('cz', a)} sem nepatří.`,
    order: (t) => `Pozor na pořadí slov: ${q('cz', t)}.`,
    orderGeneric: 'Pozor na pořadí slov.',
    generic: 'Porovnej svou větu se správným překladem.',
    typo: (t) => `Překlep: správně je ${q('cz', t)}.`,
  },
  en: {
    replace: (a, t) => `Write ${q('en', t)} instead of ${q('en', a)}.`,
    missing: (t) => `${q('en', t)} is missing.`,
    extra: (a) => `Leave out ${q('en', a)}.`,
    order: (t) => `Check the word order: ${q('en', t)}.`,
    orderGeneric: 'Check the word order.',
    generic: 'Compare your sentence with the correct translation.',
    typo: (t) => `Check the spelling: ${q('en', t)}.`,
  },
};

/** At most this many differing places are described one by one. */
export const MAX_TIP_REGIONS = 2;
/** A quoted span longer than this is not quoted (it would repeat half the sentence). */
export const MAX_QUOTED_TOKENS = 5;

/** Lower-case token → how the accepted sentence writes it mid-sentence
 *  ("I", names); the capital of the first word is not kept. */
const displayCase = (source: string): ((token: string) => string) => {
  const cased = new Map<string, string>();
  source.split(/\s+/).forEach((word, index) => {
    const bare = word.replace(/^[^\p{L}\p{N}']+|[^\p{L}\p{N}']+$/gu, '');
    const lower = bare.toLowerCase();
    if (index > 0 && bare !== lower && !cased.has(lower)) cased.set(lower, bare);
  });
  return (token) => cased.get(token) ?? (token === 'i' ? 'I' : token);
};

/** Digits produced by the number rule → the word the accepted sentence uses
 *  ("the same one" is not shown as "the same 1"). */
const numberWordsOf = (source: string): Map<string, string> => {
  const map = new Map<string, string>();
  for (const token of normalizeBasic(preNormalize(source)).split(' ')) {
    const form = Array.from(variantForms(token, 'en'))[0];
    if (form && form !== token && /^\d+$/.test(form) && !map.has(form)) map.set(form, token);
  }
  return map;
};

export const buildTip = (
  answerTokens: string[],
  targetTokens: string[],
  targetText: string,
  language: FeedbackLanguage | null
): string | null => {
  if (!language) return null;
  const t = TEMPLATES[language];
  const cased = displayCase(targetText);
  const numberWords = numberWordsOf(targetText);
  const show = (token: string) => numberWords.get(token) ?? cased(token);
  const join = (tokens: string[]) => tokens.map(show).join(' ');
  if (answerTokens.length === targetTokens.length && sortedKey(answerTokens) === sortedKey(targetTokens)) {
    let first = 0;
    while (answerTokens[first] === targetTokens[first]) first++;
    let last = targetTokens.length - 1;
    while (answerTokens[last] === targetTokens[last]) last--;
    const span = targetTokens.slice(first, last + 1);
    return span.length <= MAX_QUOTED_TOKENS + 1 && span.length < targetTokens.length ? t.order(join(span)) : t.orderGeneric;
  }
  const regions = regionsOf(alignTokens(answerTokens, targetTokens));
  if (regions.length === 0 || regions.length > MAX_TIP_REGIONS + 1) return t.generic;
  const parts: string[] = [];
  for (const region of regions.slice(0, MAX_TIP_REGIONS)) {
    if (region.answer.length > MAX_QUOTED_TOKENS || region.target.length > MAX_QUOTED_TOKENS) return t.generic;
    if (region.order && sortedKey(region.answer) === sortedKey(region.target)) parts.push(t.order(join(region.target)));
    else if (region.answer.length === 0) parts.push(t.missing(join(region.target)));
    else if (region.target.length === 0) parts.push(t.extra(join(region.answer)));
    else parts.push(t.replace(join(region.answer), join(region.target)));
  }
  let text = Array.from(new Set(parts)).join(' ');
  if (text.length > MAX_FEEDBACK_CHARS) text = parts[0];
  return text.length > MAX_FEEDBACK_CHARS ? t.generic : text;
};

// ---------------------------------------------------------------------------
// The check
// ---------------------------------------------------------------------------

export const checkTranslation = (
  answer: string,
  data: ExerciseCheckData,
  nativeLanguage: string,
  words: WordLookup
): CheckResult => {
  const language = feedbackLanguage(nativeLanguage, data.level);
  const accepted = [data.reference, ...data.acceptable.filter((text) => text !== data.reference)];
  const answerForms = formsOf(answer);
  if (normalizeBasic(preNormalize(answer)).length === 0) {
    return { verdict: 'wrong', feedback: null, step: 'auto', closest: data.reference, unmatched: false };
  }

  // 1. reference / acceptable
  for (const [index, text] of accepted.entries()) {
    if (sameReading(answerForms, text)) {
      return { verdict: 'correct', feedback: null, step: index === 0 ? 'reference' : 'acceptable', closest: text, unmatched: false };
    }
  }
  const answerReadings = Array.from(answerForms).map((form) => form.split(' ').filter(Boolean));
  const acceptedReadings = accepted.map((text) => ({ text, readings: readings(text) }));

  // 1b. British / American spelling only
  for (const { text, readings: candidateReadings } of acceptedReadings) {
    for (const a of answerReadings) {
      for (const c of candidateReadings) {
        if (a.length !== c.length) continue;
        const diffs = a.map((token, k) => [token, c[k]]).filter(([x, y]) => x !== y);
        if (diffs.length > 0 && diffs.every(([x, y]) => isSpellingVariant(x, y, words))) {
          return { verdict: 'correct', feedback: null, step: 'spelling_variant', closest: text, unmatched: false };
        }
      }
    }
  }

  // 2. typical mistakes
  for (const mistake of data.mistakes) {
    if (sameReading(answerForms, mistake.text)) {
      return { verdict: mistake.verdict, feedback: pickFeedback(mistake, language), step: 'mistake', closest: data.reference, unmatched: false };
    }
  }

  // 3. one typo in one word
  for (const { text, readings: candidateReadings } of acceptedReadings) {
    for (const a of answerReadings) {
      for (const c of candidateReadings) {
        if (a.length !== c.length) continue;
        let diff = -1;
        let count = 0;
        for (let k = 0; k < a.length && count < 2; k++) {
          if (a[k] !== c[k]) { diff = k; count++; }
        }
        if (count === 1 && isTypo(a[diff], c[diff], words)) {
          const shown = displayCase(text)(c[diff]);
          return {
            verdict: 'correct_with_tip',
            feedback: language ? TEMPLATES[language].typo(shown) : null,
            step: 'typo',
            closest: text,
            unmatched: true,
          };
        }
      }
    }
  }

  // 4. wrong + alignment tip against the closest accepted sentence; an accepted
  //    sentence with exactly the answer's words (only the order differs) wins,
  //    so a word-order error is not described as replaced words.
  let best = { distance: Infinity, answer: answerReadings[0], target: acceptedReadings[0].readings[0], text: data.reference };
  permutation: for (const { text, readings: candidateReadings } of acceptedReadings) {
    for (const a of answerReadings) {
      for (const c of candidateReadings) {
        if (a.length === c.length && sortedKey(a) === sortedKey(c)) {
          best = { distance: 0, answer: a, target: c, text };
          break permutation;
        }
      }
    }
  }
  for (const { text, readings: candidateReadings } of best.distance === 0 ? [] : acceptedReadings) {
    for (const a of answerReadings) {
      for (const c of candidateReadings) {
        if (Math.abs(a.length - c.length) >= best.distance) continue;
        const distance = osaDistance(a, c);
        if (distance < best.distance) best = { distance, answer: a, target: c, text };
      }
    }
  }
  return {
    verdict: 'wrong',
    feedback: buildTip(best.answer, best.target, best.text, language),
    step: 'auto',
    closest: best.text,
    unmatched: true,
  };
};
