// LISTENING and SPEAKING exercises (docs/features/reports/LISTENING_SPEAKING_REPORT.md):
// the free, deterministic checks. Pure functions without Deno or RN APIs, so the
// same file runs in the app (lib/listenSpeak*), in the edge function
// check-listen-speak and under node --test.
//
// LISTENING (typed answer to a question about the video): an answer is right
// without any model call when it matches correct_answer or one of
// accepted_answers under the typed-answer rules (case, spacing, punctuation,
// apostrophes, English contractions, numbers as digits or words), when the two
// differ only by the articles a / an / the, or when ONE word of 5+ letters (no
// digit) is one letter off – the speaking rule 6 below (decision 71). Anything
// else goes to ONE model call.
//
// SPEAKING (the learner says one sentence of the video): the transcript must be
// one of media.speech_sentences word for word, after both sides are normalised:
//   1. lower case; punctuation, quotes and hyphens dropped; apostrophes unified;
//   2. English contractions expanded (I'm = I am, don't = do not, it's = it is / it has, ...);
//   3. numbers 0-100 as digits or words are the same ("1 second" = "one second");
//   4. the articles a / an / the are ignored;
//   5. filler sounds are ignored (um, uh, erm, er, hmm, mm, ah, oh, eh, ...);
//   6. at most ONE word may differ by one letter (added, dropped or changed), and
//      only when both words have 5 or more letters: a transcription spelling of an
//      accented word ("certificate" / "certificates"). Short words must be exact,
//      so "That car are amazing" is not "That car is amazing".
// Pronunciation and accent never reach this rule: the model writes what was
// said in standard spelling, and the rule compares words. A strong accent is
// handled by a second listen in check-listen-speak (the sentences as context),
// which may only confirm a sentence that the first, context-free transcript
// already sounds like (letterSimilarity).

import { normalizeBasic, variantForms } from './typedAnswerNormalizer.ts';

const LANGUAGE = 'en';

/** Articles a learner may add or drop. */
export const ARTICLES: ReadonlySet<string> = new Set(['a', 'an', 'the']);

/** Filler sounds that never decide a spoken line. */
export const FILLERS: ReadonlySet<string> = new Set([
  'um',
  'umm',
  'uh',
  'uhh',
  'uhm',
  'erm',
  'er',
  'hmm',
  'hm',
  'mm',
  'mmm',
  'mhm',
  'ah',
  'ahh',
  'oh',
  'ooh',
  'eh',
]);

/** Minimum letters of both words for the one-letter tolerance (rule 6). */
export const TYPO_MIN_LENGTH = 5;

/** Every rule-1-to-3 reading of a text, as token lists. */
const readings = (text: string): string[][] => {
  const basic = normalizeBasic(text.replace(/[-–—/()[\]{}]/g, ' '));
  if (!basic) return [];
  return Array.from(variantForms(basic, LANGUAGE), (form) => form.split(' ').filter(Boolean));
};

const withoutArticles = (tokens: string[]): string[] => tokens.filter((t) => !ARTICLES.has(t));
const withoutFillers = (tokens: string[]): string[] => tokens.filter((t) => !FILLERS.has(t));

/** Levenshtein distance, stopping early above `limit`. */
const editDistance = (a: string, b: string, limit: number): number => {
  if (Math.abs(a.length - b.length) > limit) return limit + 1;
  let previous = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) {
    const current = [i];
    let best = i;
    for (let j = 1; j <= b.length; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      current[j] = Math.min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + cost);
      best = Math.min(best, current[j]);
    }
    if (best > limit) return limit + 1;
    previous = current;
  }
  return previous[b.length];
};

/** Rule 6 (speaking and listening): same words, at most one pair of long words one letter apart. */
const sameWords = (heard: string[], sentence: string[]): boolean => {
  if (heard.length !== sentence.length) return false;
  let tolerated = 0;
  for (let i = 0; i < heard.length; i++) {
    if (heard[i] === sentence[i]) continue;
    const long = heard[i].length >= TYPO_MIN_LENGTH && sentence[i].length >= TYPO_MIN_LENGTH;
    if (!long || /\d/.test(heard[i] + sentence[i]) || editDistance(heard[i], sentence[i], 1) > 1) return false;
    tolerated += 1;
    if (tolerated > 1) return false;
  }
  return true;
};

// ---------------------------------------------------------------------------
// Listening
// ---------------------------------------------------------------------------

/**
 * One answer against one stored answer: exact, typed-answer variant, the same
 * apart from articles, and in each case one long word may be one letter off
 * ("beautifull" = "beautiful"; "cat" / "car", "recieve" / "receive"
 * (two letters) and different words stay wrong).
 */
export const listeningAnswerMatches = (answer: string, target: string): boolean => {
  const learner = readings(answer);
  const stored = readings(target);
  if (learner.length === 0 || stored.length === 0) return false;
  return learner.some((tokens) =>
    stored.some(
      (candidate) =>
        sameWords(tokens, candidate) || sameWords(withoutArticles(tokens), withoutArticles(candidate))
    )
  );
};

/** The free path of the listening check: true = right without a model call. */
export const listeningMatchesLocally = (
  answer: string,
  correctAnswer: string,
  acceptedAnswers: readonly string[]
): boolean => [correctAnswer, ...acceptedAnswers].some((target) => target && listeningAnswerMatches(answer, target));

/** Accepted answers from the jsonb column: strings only, trimmed, no empties. */
export const cleanAccepted = (value: unknown): string[] =>
  Array.isArray(value)
    ? value.filter((v): v is string => typeof v === 'string').map((v) => v.trim()).filter(Boolean)
    : [];

// ---------------------------------------------------------------------------
// Speaking
// ---------------------------------------------------------------------------

/** Every normalised word list of a spoken line or a stored sentence (rules 1-5). */
export const spokenForms = (text: string): string[][] => {
  const seen = new Set<string>();
  const out: string[][] = [];
  for (const tokens of readings(text)) {
    const kept = withoutFillers(withoutArticles(tokens));
    const key = kept.join(' ');
    if (!key || seen.has(key)) continue;
    seen.add(key);
    out.push(kept);
  }
  return out;
};

/** True when the spoken line counts as the stored sentence. */
export const spokenLineMatches = (heard: string, sentence: string): boolean => {
  const heardForms = spokenForms(heard);
  if (heardForms.length === 0) return false;
  const sentenceForms = spokenForms(sentence);
  return heardForms.some((h) => sentenceForms.some((s) => sameWords(h, s)));
};

/** Word overlap (0..1) of two lines, for showing the nearest sentence after a miss. */
const overlap = (a: string, b: string): number => {
  const x = spokenForms(a)[0] ?? [];
  const y = spokenForms(b)[0] ?? [];
  if (x.length === 0 || y.length === 0) return 0;
  const pool = [...y];
  let common = 0;
  for (const token of x) {
    const at = pool.indexOf(token);
    if (at !== -1) {
      common += 1;
      pool.splice(at, 1);
    }
  }
  return (2 * common) / (x.length + y.length);
};

export interface SpokenMatch {
  /** the stored sentence the line counts as, or null */
  matched: string | null;
  /** the stored sentence closest to the line (shown in green after a miss), or null */
  closest: string | null;
}

/** The speaking verdict over all acceptable sentences of the video. */
export const matchSpokenLine = (heard: string, sentences: readonly string[]): SpokenMatch => {
  const list = sentences.map((s) => s.trim()).filter(Boolean);
  const matched = list.find((sentence) => spokenLineMatches(heard, sentence)) ?? null;
  if (matched) return { matched, closest: matched };
  let closest: string | null = null;
  let best = 0;
  for (const sentence of list) {
    const score = overlap(heard, sentence);
    if (score > best) {
      best = score;
      closest = sentence;
    }
  }
  return { matched: null, closest };
};

/**
 * How much two lines SOUND alike: 1 − (letter edit distance / longer length) over
 * the normalised words joined without spaces ("work every bit" / "Worth every bit."
 * = 0.85, "Listen, the fizz" / "In they go" = 0.20). Guards the second listen.
 */
export const letterSimilarity = (a: string, b: string): number => {
  const x = (spokenForms(a)[0] ?? []).join('');
  const y = (spokenForms(b)[0] ?? []).join('');
  if (!x || !y) return 0;
  return 1 - editDistance(x, y, Math.max(x.length, y.length)) / Math.max(x.length, y.length);
};

/** speech_sentences from the jsonb column: strings only, trimmed, no empties. */
export const cleanSentences = (value: unknown): string[] => cleanAccepted(value);
