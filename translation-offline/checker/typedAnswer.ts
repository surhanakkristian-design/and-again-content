// "Type the answer" exercise format – answer checking. Pure functions, no
// React, no Supabase, so they run under `node --test lib/typedAnswer.test.ts`.
// Spec: docs/features/TYPED_ANSWER_EXERCISE.md §3.
//
// The learner types only the missing part of the sentence
// (exercise_localizations.correct_answer). Both the learner's text and the
// stored answer go through the SAME pipeline and are compared:
//   - level A (rules 1–3: case, whitespace, punctuation, apostrophes, the
//     "..." separator of two-blank answers) → 'exact'
//   - level B (rules 4–6: diacritics, English contractions, digits vs number
//     words) → 'variant' (counts as correct)
//   - otherwise 'wrong'
// Level B is a SET of candidate strings per side (a contraction like "I'd"
// expands to two readings, German "ü" to "ue" and "u"); the answer is a
// variant when the two sets share a member.

export type TypedAnswerVerdict = 'exact' | 'variant' | 'wrong';

/** Learning languages the checker knows number words and contractions for. */
export type TypedAnswerLanguage = 'en' | 'de' | 'es' | 'fr';

// Rule 3: every apostrophe-like character is the straight apostrophe.
// iOS types ’ (U+2019); ‘ ʼ ` ´ appear in copied text.
const APOSTROPHES = /[’‘‛ʼ`´]/g;
// Rule 2: punctuation that never decides correctness (the brief's list).
const PUNCTUATION = /[.,!?;:"«»¿¡…]/g;
// The two-blank separator of German answers ("ist ... gedruckt") – rule 2.
const BLANK_SEPARATOR = /\.\.\./g;

const collapseWhitespace = (text: string): string => text.trim().split(/\s+/).filter(Boolean).join(' ');

/**
 * Level A (rules 1–3): lower-case, trimmed, single spaces, punctuation and
 * the "..." separator removed, apostrophes unified. Two strings equal here
 * are an 'exact' match.
 */
export const normalizeBasic = (text: string): string =>
  collapseWhitespace(
    text
      .replace(BLANK_SEPARATOR, ' ')
      .replace(APOSTROPHES, "'")
      .replace(PUNCTUATION, ' ')
      .toLowerCase()
  );

// ---------------------------------------------------------------------------
// Rule 4 – diacritics
// ---------------------------------------------------------------------------

/** ß → ss, œ → oe, æ → ae, then every combining mark dropped (é → e, ñ → n,
 *  ç → c, ä → a). Applied to both sides, so a learner may type either. */
export const stripDiacritics = (text: string): string =>
  text
    .replace(/ß/g, 'ss')
    .replace(/œ/g, 'oe')
    .replace(/æ/g, 'ae')
    .normalize('NFD')
    .replace(/\p{M}/gu, '');

/** German only: ä/ö/ü may also be written ae/oe/ue. */
const expandUmlauts = (text: string): string =>
  text.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue');

const diacriticForms = (text: string, language: string): string[] => {
  const forms = [stripDiacritics(text)];
  if (language === 'de') forms.push(stripDiacritics(expandUmlauts(text)));
  return Array.from(new Set(forms));
};

// ---------------------------------------------------------------------------
// Rule 5 – English contractions (both directions, because both sides expand)
// ---------------------------------------------------------------------------

/** Words after which 's is a contraction (is/has), never a possessive. */
const CONTRACTIBLE_S_HEADS = new Set([
  'he',
  'she',
  'it',
  'that',
  'there',
  'here',
  'what',
  'who',
  'where',
  'how',
]);

/** n't stems whose full form is not simply stem + "not". */
const IRREGULAR_NOT = new Map<string, string>([
  ['ca', 'can'], // can't
  ['wo', 'will'], // won't
  ['sha', 'shall'], // shan't
]);

/** All full-form readings of one token (a token without a contraction maps
 *  to itself). "cannot" and "can't" both become "can not". */
const expandContraction = (token: string): string[][] => {
  if (token === 'cannot') return [['can', 'not']];
  if (token === "let's") return [['let', 'us']];
  if (token.endsWith("n't") && token.length > 3) {
    const stem = token.slice(0, -3);
    if (stem === 'ai') return [[token]]; // ain't has no single full form
    return [[IRREGULAR_NOT.get(stem) ?? stem, 'not']];
  }
  const suffixes: [string, string[]][] = [
    ["'re", ['are']],
    ["'ve", ['have']],
    ["'ll", ['will']],
    ["'m", ['am']],
    ["'d", ['would', 'had']],
  ];
  for (const [suffix, fullForms] of suffixes) {
    if (token.endsWith(suffix) && token.length > suffix.length) {
      const stem = token.slice(0, -suffix.length);
      return fullForms.map((full) => [stem, full]);
    }
  }
  if (token.endsWith("'s") && token.length > 2) {
    const stem = token.slice(0, -2);
    // Possessives ("Peter's", "the dog's") stay as they are
    if (CONTRACTIBLE_S_HEADS.has(stem)) return [[stem, 'is'], [stem, 'has']];
  }
  return [[token]];
};

/** Cartesian product of the per-token readings, capped so a pathological
 *  input cannot explode (six 'd/'s tokens = 64 readings, more is cut). */
const MAX_READINGS = 64;
const expandContractions = (tokens: string[]): string[][] => {
  let readings: string[][] = [[]];
  for (const token of tokens) {
    const options = expandContraction(token);
    const next: string[][] = [];
    for (const reading of readings) {
      for (const option of options) {
        if (next.length >= MAX_READINGS) break;
        next.push([...reading, ...option]);
      }
    }
    readings = next;
  }
  return readings;
};

// ---------------------------------------------------------------------------
// Rule 6 – numbers 0–100 as digits or words, per language
// ---------------------------------------------------------------------------

type NumberTable = Map<string, number>;

/** Keys are stored diacritic-free and hyphen-free (the same form the
 *  candidate strings have when the table is consulted). */
const numberTable = (entries: [string, number][]): NumberTable => {
  const table: NumberTable = new Map();
  for (const [phrase, value] of entries) {
    table.set(collapseWhitespace(stripDiacritics(phrase.toLowerCase()).replace(/-/g, ' ')), value);
  }
  return table;
};

const englishNumbers = (): NumberTable => {
  const ones = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ');
  const tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
  const entries: [string, number][] = ones.map((word, i) => [word, i]);
  tens.forEach((ten, t) => {
    entries.push([ten, 20 + t * 10]);
    for (let unit = 1; unit <= 9; unit++) entries.push([`${ten} ${ones[unit]}`, 20 + t * 10 + unit]);
  });
  entries.push(['hundred', 100], ['one hundred', 100], ['a hundred', 100]);
  return numberTable(entries);
};

const germanNumbers = (): NumberTable => {
  // "ein"/"eine" are also the indefinite article – only "eins" means 1 on
  // its own (an article ending must never be forgiven by the number rule).
  const ones = 'null eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn'.split(' ');
  const units = 'ein zwei drei vier fünf sechs sieben acht neun'.split(' ');
  const tens = ['zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig'];
  const entries: [string, number][] = ones.map((word, i) => [word, i]);
  tens.forEach((ten, t) => {
    entries.push([ten, 20 + t * 10]);
    units.forEach((unit, u) => entries.push([`${unit}und${ten}`, 20 + t * 10 + u + 1]));
  });
  entries.push(['hundert', 100], ['einhundert', 100]);
  return numberTable(entries);
};

const spanishNumbers = (): NumberTable => {
  // "un"/"una" are articles as well – only "uno" is the bare numeral.
  const ones = 'cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciséis diecisiete dieciocho diecinueve veinte veintiuno veintidós veintitrés veinticuatro veinticinco veintiséis veintisiete veintiocho veintinueve'.split(' ');
  const units = 'uno dos tres cuatro cinco seis siete ocho nueve'.split(' ');
  const tens = ['treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'];
  const entries: [string, number][] = ones.map((word, i) => [word, i]);
  tens.forEach((ten, t) => {
    entries.push([ten, 30 + t * 10]);
    units.forEach((unit, u) => entries.push([`${ten} y ${unit}`, 30 + t * 10 + u + 1]));
  });
  entries.push(['cien', 100], ['ciento', 100]);
  return numberTable(entries);
};

const frenchNumbers = (): NumberTable => {
  // "un"/"une" are articles as well – 1 on its own is not mapped, but
  // "vingt et un" etc. are (matched as a whole phrase).
  const ones = 'zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize dix-sept dix-huit dix-neuf'.split(' ');
  const entries: [string, number][] = ones
    .map((word, i): [string, number] => [word, i])
    .filter(([, n]) => n !== 1);
  const tens: [string, number][] = [
    ['vingt', 20],
    ['trente', 30],
    ['quarante', 40],
    ['cinquante', 50],
    ['soixante', 60],
    ['septante', 70],
    ['huitante', 80],
    ['octante', 80],
    ['nonante', 90],
  ];
  for (const [ten, value] of tens) {
    entries.push([ten, value]);
    entries.push([`${ten} et un`, value + 1]);
    for (let unit = 2; unit <= 9; unit++) entries.push([`${ten} ${ones[unit]}`, value + unit]);
  }
  // 70–79 and 90–99 in France: soixante-dix, soixante et onze, …
  entries.push(['soixante dix', 70], ['soixante et onze', 71]);
  for (let n = 12; n <= 19; n++) entries.push([`soixante ${ones[n]}`, 60 + n]);
  entries.push(['quatre vingts', 80], ['quatre vingt', 80], ['quatre vingt un', 81]);
  for (let unit = 2; unit <= 9; unit++) entries.push([`quatre vingt ${ones[unit]}`, 80 + unit]);
  for (let n = 10; n <= 19; n++) entries.push([`quatre vingt ${ones[n]}`, 80 + n]);
  entries.push(['cent', 100]);
  return numberTable(entries);
};

const NUMBER_TABLES: Record<TypedAnswerLanguage, NumberTable> = {
  en: englishNumbers(),
  de: germanNumbers(),
  es: spanishNumbers(),
  fr: frenchNumbers(),
};

/** Longest phrase in the table is four tokens ("quatre vingt dix neuf"). */
const MAX_NUMBER_PHRASE_TOKENS = 4;

/** Replaces number words (single words or phrases) with their digits. */
const digitizeNumbers = (tokens: string[], table: NumberTable | undefined): string[] => {
  if (!table) return tokens;
  const result: string[] = [];
  let i = 0;
  while (i < tokens.length) {
    let matched = false;
    for (let span = Math.min(MAX_NUMBER_PHRASE_TOKENS, tokens.length - i); span >= 1; span--) {
      const value = table.get(tokens.slice(i, i + span).join(' '));
      if (value !== undefined) {
        result.push(String(value));
        i += span;
        matched = true;
        break;
      }
    }
    if (!matched) {
      result.push(tokens[i]);
      i += 1;
    }
  }
  return result;
};

// ---------------------------------------------------------------------------
// Level B candidates + the verdict
// ---------------------------------------------------------------------------

const isKnownLanguage = (language: string): language is TypedAnswerLanguage =>
  language === 'en' || language === 'de' || language === 'es' || language === 'fr';

/**
 * Every level-B reading of an already level-A-normalised string: hyphens
 * become spaces (number phrases), diacritics are stripped (rule 4, with the
 * German ae/oe/ue twin), English contractions expand (rule 5) and number
 * words become digits (rule 6).
 */
export const variantForms = (basic: string, language: string): Set<string> => {
  const lang = language.toLowerCase();
  const table = isKnownLanguage(lang) ? NUMBER_TABLES[lang] : undefined;
  const forms = new Set<string>();
  for (const form of diacriticForms(basic.replace(/-/g, ' '), lang)) {
    const tokens = collapseWhitespace(form).split(' ').filter(Boolean);
    const readings = lang === 'en' ? expandContractions(tokens) : [tokens];
    for (const reading of readings) forms.add(digitizeNumbers(reading, table).join(' '));
  }
  return forms;
};

/**
 * The verdict for what the learner typed against the stored correct answer
 * of the learning-language row. `language` = that row's language_code.
 */
export const checkTypedAnswer = (
  typed: string,
  correctAnswer: string,
  language: string
): TypedAnswerVerdict => {
  const learner = normalizeBasic(typed);
  const answer = normalizeBasic(correctAnswer);
  if (learner.length === 0 || answer.length === 0) return 'wrong';
  if (learner === answer) return 'exact';
  const answerForms = variantForms(answer, language);
  for (const form of variantForms(learner, language)) {
    if (answerForms.has(form)) return 'variant';
  }
  return 'wrong';
};

/** True when the verdict counts as a correct answer (streak, repetition step). */
export const isTypedAnswerCorrect = (verdict: TypedAnswerVerdict): boolean => verdict !== 'wrong';
