// Run: node --test checker/*.test.ts   (Node ≥ 22.18 strips the types natively)
import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import {
  buildTip,
  checkTranslation,
  feedbackLanguage,
  isOtherFormOfSameWord,
  isSpellingVariant,
  isTypo,
  osaDistance,
  readings,
  MAX_FEEDBACK_CHARS,
  type ExerciseCheckData,
} from './offlineCheck.ts';
import { expandSlots } from './slots.ts';

const HERE = dirname(fileURLToPath(import.meta.url));
const WORDS = new Set(readFileSync(join(HERE, '..', 'wordlist', 'en_words.txt'), 'utf8').split('\n').filter(Boolean));

const SLED: ExerciseCheckData = {
  level: 'A1',
  reference: 'He sleds down this slope every winter.',
  acceptable: ['Every winter he sleds down this slope.', 'He sleds down this hill every winter.'],
  mistakes: [
    {
      text: 'He sled down this slope every winter.',
      verdict: 'wrong',
      feedback_sk: 'Po „he“ patrí v Present Simple „sleds“.',
      feedback_cz: 'Po „he“ patří v Present Simple „sleds“.',
      feedback_en: null,
    },
  ],
};

const FUTURE_PERFECT: ExerciseCheckData = {
  level: 'B2',
  reference: 'By the end of the lesson every student will have given a presentation.',
  acceptable: ['By the end of the lesson each student will have given a presentation.'],
  mistakes: [
    {
      text: 'By the end of the lesson every student will give a presentation.',
      verdict: 'wrong',
      feedback_sk: 'Po „By the end of…“ patrí Future Perfect: „will have given“.',
      feedback_cz: 'Po „By the end of…“ patří Future Perfect: „will have given“.',
      feedback_en: 'After “By the end of…” use the Future Perfect: “will have given”.',
    },
  ],
};

const BOIL: ExerciseCheckData = {
  level: 'A2',
  reference: 'Wait a minute and the water will boil!',
  acceptable: ['Wait a moment and the water will boil!'],
  mistakes: [],
};

describe('word list', () => {
  test('has inflected forms and no abbreviations that mask typos', () => {
    assert.ok(WORDS.size > 90_000);
    for (const w of ['sled', 'sleds', 'give', 'gave', 'their', 'there', 'then', 'than', 'boil', 'held']) assert.ok(WORDS.has(w), w);
    for (const w of ['biol', 'govt', 'childs']) assert.ok(!WORDS.has(w), w);
  });
});

describe('feedback language (decision 4)', () => {
  test('sk and cz at every level', () => {
    for (const level of ['A1', 'A2', 'B1', 'B2'] as const) {
      assert.equal(feedbackLanguage('sk', level), 'sk');
      assert.equal(feedbackLanguage('cz', level), 'cz');
    }
  });
  test('other native languages: English at B1/B2, nothing at A1/A2', () => {
    assert.equal(feedbackLanguage('de', 'B1'), 'en');
    assert.equal(feedbackLanguage('hu', 'B2'), 'en');
    assert.equal(feedbackLanguage('ua', 'A1'), null);
    assert.equal(feedbackLanguage('tr', 'A2'), null);
  });
});

describe('slot expansion (build time)', () => {
  test('every combination, empty option, whitespace collapsed', () => {
    assert.deepEqual(expandSlots('The {big|large} plate is {very |}clean.'), [
      'The big plate is very clean.',
      'The big plate is clean.',
      'The large plate is very clean.',
      'The large plate is clean.',
    ]);
  });
  test('space before punctuation removed, duplicates removed', () => {
    assert.deepEqual(expandSlots('He left {now|} .'), ['He left now.', 'He left.']);
    assert.deepEqual(expandSlots('{a|a} b'), ['a b']);
  });
  test('nested braces throw', () => {
    assert.throws(() => expandSlots('a {b {c|d}|e}'));
    assert.throws(() => expandSlots('a {b|c'));
  });
});

describe('step 1 – reference and acceptable translations', () => {
  test('reference with case, punctuation and whitespace differences', () => {
    const r = checkTranslation('  he sleds down this slope every winter ', SLED, 'sk', WORDS);
    assert.equal(r.verdict, 'correct');
    assert.equal(r.step, 'reference');
    assert.equal(r.feedback, null);
    assert.equal(r.unmatched, false);
  });
  test('acceptable translation', () => {
    const r = checkTranslation('Every winter he sleds down this slope!', SLED, 'cz', WORDS);
    assert.deepEqual([r.verdict, r.step], ['correct', 'acceptable']);
  });
  test('contractions and number words both ways', () => {
    const data: ExerciseCheckData = { level: 'A1', reference: "She isn't at home, she has two cats.", acceptable: [], mistakes: [] };
    assert.equal(checkTranslation("She is not at home, she's 2 cats.", data, 'sk', WORDS).verdict, 'correct');
  });
  test('curly apostrophe and diacritics', () => {
    const data: ExerciseCheckData = { level: 'A2', reference: "We don't go to the café.", acceptable: [], mistakes: [] };
    assert.equal(checkTranslation('We don’t go to the cafe', data, 'sk', WORDS).verdict, 'correct');
  });
  test('1b British / American spelling counts as correct', () => {
    const data: ExerciseCheckData = { level: 'A1', reference: 'Her favorite color is gray.', acceptable: [], mistakes: [] };
    const r = checkTranslation('Her favourite colour is grey.', data, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.step], ['correct', 'spelling_variant']);
  });
  test('spelling rules never pair unrelated words', () => {
    assert.equal(isSpellingVariant('four', 'for', WORDS), false);
    assert.equal(isSpellingVariant('your', 'yor', WORDS), false);
    assert.equal(isSpellingVariant('centre', 'center', WORDS), true);
    assert.equal(isSpellingVariant('realised', 'realized', WORDS), true);
  });
  test('empty answer is wrong without feedback', () => {
    const r = checkTranslation('  ?! ', SLED, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.feedback, r.unmatched], ['wrong', null, false]);
  });
});

describe('step 2 – typical mistakes', () => {
  test('stored mistake → its verdict and the Slovak feedback', () => {
    const r = checkTranslation('he sled down this slope every winter', SLED, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.step, r.unmatched], ['wrong', 'mistake', false]);
    assert.equal(r.feedback, 'Po „he“ patrí v Present Simple „sleds“.');
  });
  test('Czech feedback for cz', () => {
    assert.equal(checkTranslation('He sled down this slope every winter.', SLED, 'cz', WORDS).feedback, 'Po „he“ patří v Present Simple „sleds“.');
  });
  test('other native language at A1: verdict without feedback text', () => {
    const r = checkTranslation('He sled down this slope every winter.', SLED, 'de', WORDS);
    assert.deepEqual([r.verdict, r.feedback], ['wrong', null]);
  });
  test('other native language at B2: English feedback', () => {
    const r = checkTranslation('By the end of the lesson every student will give a presentation.', FUTURE_PERFECT, 'hu', WORDS);
    assert.equal(r.feedback, 'After “By the end of…” use the Future Perfect: “will have given”.');
  });
  test('a mistake is only checked after the acceptable list', () => {
    const data: ExerciseCheckData = { ...SLED, acceptable: [...SLED.acceptable, SLED.mistakes[0].text] };
    assert.equal(checkTranslation(SLED.mistakes[0].text, data, 'sk', WORDS).verdict, 'correct');
  });
});

describe('step 3 – one typo', () => {
  test('swapped letters in one word ≥ 4 letters → correct_with_tip with the spelling', () => {
    const r = checkTranslation('Wait a minute and the water will biol!', BOIL, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.step, r.unmatched], ['correct_with_tip', 'typo', true]);
    assert.equal(r.feedback, 'Preklep: správne je „boil“.');
  });
  test('insert, delete and substitute are typos too', () => {
    assert.equal(isTypo('miniute', 'minute', WORDS), true);
    assert.equal(isTypo('minte', 'minute', WORDS), true);
    assert.equal(isTypo('minuke', 'minute', WORDS), true);
  });
  test('typo against an acceptable translation, feedback language rules', () => {
    const r = checkTranslation('Wait a momnet and the water will boil', BOIL, 'cz', WORDS);
    assert.deepEqual([r.verdict, r.feedback], ['correct_with_tip', 'Překlep: správně je „moment“.']);
    assert.equal(checkTranslation('Wait a momnet and the water will boil', BOIL, 'de', WORDS).feedback, null);
  });
  test('NOT a typo: another real English word (sled/sleds, give/gave, their/there, then/than)', () => {
    assert.equal(isTypo('sled', 'sleds', WORDS), false);
    assert.equal(isTypo('sleds', 'sled', WORDS), false);
    assert.equal(isTypo('gave', 'give', WORDS), false);
    assert.equal(isTypo('there', 'their', WORDS), false);
    assert.equal(isTypo('than', 'then', WORDS), false);
    assert.equal(isTypo('then', 'than', WORDS), false);
  });
  test('NOT a typo: another form of the same word even when it is no real word', () => {
    assert.equal(isOtherFormOfSameWord('childs', 'child'), true);
    assert.equal(isTypo('childs', 'child', WORDS), false);
    assert.equal(isTypo('womans', 'woman', WORDS), false);
    assert.equal(isTypo('hitted', 'hitte', WORDS), false);
  });
  test('the sled answer is wrong, not a typo (without a stored mistake)', () => {
    const data = { ...SLED, mistakes: [] };
    const r = checkTranslation('He sled down this slope every winter.', data, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.step], ['wrong', 'auto']);
    assert.equal(r.feedback, 'Namiesto „sled“ patrí „sleds“.');
  });
  test('NOT a typo: word shorter than 4 letters', () => {
    assert.equal(isTypo('teh', 'the', WORDS), false);
    const data: ExerciseCheckData = { level: 'A1', reference: 'The cat is on the bed.', acceptable: [], mistakes: [] };
    assert.equal(checkTranslation('The cat is on teh bed.', data, 'sk', WORDS).verdict, 'wrong');
  });
  test('NOT a typo: two edits in one word, or typos in two words', () => {
    assert.equal(isTypo('bojl', 'boil', WORDS), true);
    assert.equal(isTypo('bjol', 'boil', WORDS), false);
    assert.equal(checkTranslation('Wait a minuet and the watr will boil!', BOIL, 'sk', WORDS).verdict, 'wrong');
  });
  test('osa distance', () => {
    assert.equal(osaDistance('boil', 'biol'), 1);
    assert.equal(osaDistance('kitten', 'sitting'), 3);
    assert.equal(osaDistance(['a', 'b', 'c'], ['a', 'c', 'b']), 1);
  });
});

describe('step 4 – wrong with an alignment tip', () => {
  const PORCH: ExerciseCheckData = { level: 'A1', reference: 'They watch the storm from the porch.', acceptable: [], mistakes: [] };
  test('missing words', () => {
    const r = checkTranslation('They watch storm from porch.', PORCH, 'sk', WORDS);
    assert.deepEqual([r.verdict, r.step, r.unmatched], ['wrong', 'auto', true]);
    assert.equal(r.feedback, 'Chýba „the“.');
  });
  test('extra word (Czech)', () => {
    assert.equal(checkTranslation('They watch the storm from the big porch.', PORCH, 'cz', WORDS).feedback, '„big“ sem nepatří.');
  });
  test('wrong word (English at B1)', () => {
    const data = { ...PORCH, level: 'B1' as const };
    assert.equal(checkTranslation('They watch the storm from the garden.', data, 'de', WORDS).feedback, 'Write “porch” instead of “garden”.');
  });
  test('neighbouring edits are one place: "will give" → "have given"', () => {
    const data = { ...FUTURE_PERFECT, mistakes: [] };
    const r = checkTranslation('By the end of the lesson every student will gives a presentation.', data, 'sk', WORDS);
    assert.equal(r.feedback, 'Namiesto „gives“ patrí „have given“.');
  });
  test('word order', () => {
    const data: ExerciseCheckData = { level: 'B1', reference: 'If he held the screwdriver, that shelf would be on the floor by now.', acceptable: [], mistakes: [] };
    const r = checkTranslation('If he held the screwdriver, that shelf would by now on the floor be.', data, 'sk', WORDS);
    assert.equal(r.verdict, 'wrong');
    assert.equal(r.feedback, 'Pozor na poradie slov: „be on the floor by now“.');
  });
  test('word order wins over a closer sentence with other words', () => {
    const data: ExerciseCheckData = {
      level: 'B1',
      reference: 'If he held the screwdriver, that shelf would be on the floor by now.',
      acceptable: ['If he held the screwdriver, that shelf would already be on the floor.'],
      mistakes: [],
    };
    const r = checkTranslation('If he held the screwdriver, that shelf would by now on the floor be.', data, 'sk', WORDS);
    assert.equal(r.feedback, 'Pozor na poradie slov: „be on the floor by now“.');
  });
  test('adjacent swap', () => {
    assert.equal(checkTranslation('They watch the storm the from porch.', PORCH, 'sk', WORDS).feedback, 'Pozor na poradie slov: „from the“.');
  });
  test('"I" and names keep their capital in the tip', () => {
    const data: ExerciseCheckData = { level: 'A1', reference: 'Tomorrow I visit Anna in London.', acceptable: [], mistakes: [] };
    assert.equal(checkTranslation('Tomorrow visit Anna in London.', data, 'sk', WORDS).feedback, 'Chýba „I“.');
    assert.equal(checkTranslation('Tomorrow I visit in London.', data, 'sk', WORDS).feedback, 'Chýba „Anna“.');
  });
  test('closest accepted sentence is used for the tip', () => {
    const r = checkTranslation('He sleds down this hill each winter.', SLED, 'sk', WORDS);
    assert.equal(r.closest, 'He sleds down this hill every winter.');
    assert.equal(r.feedback, 'Namiesto „each“ patrí „every“.');
  });
  test('too many differences → a generic line, never the whole reference', () => {
    const r = checkTranslation('Yesterday we ate pizza in a small restaurant.', PORCH, 'sk', WORDS);
    assert.equal(r.feedback, 'Porovnaj svoju vetu so správnym prekladom.');
    assert.ok(!r.feedback?.includes('They watch the storm from the porch'));
  });
  test('no feedback text for other native languages at A1/A2', () => {
    assert.equal(checkTranslation('They watch storm from porch.', PORCH, 'ua', WORDS).feedback, null);
  });
  test('tips stay within 150 characters', () => {
    const tip = buildTip(
      ['a', 'b', 'extraordinarily', 'd', 'e', 'f'],
      ['a', 'b', 'incomprehensibilities', 'd', 'e', 'unquestionably'],
      'a b incomprehensibilities d e unquestionably',
      'en'
    );
    assert.ok(tip !== null && tip.length <= MAX_FEEDBACK_CHARS, tip ?? '');
  });
});

describe('normalisation gaps closed in the offline checker', () => {
  test('typographic double quotes, dashes and brackets are punctuation', () => {
    const data: ExerciseCheckData = { level: 'B1', reference: 'The director shouted “action” – twice.', acceptable: [], mistakes: [] };
    assert.equal(checkTranslation('The director shouted "action" twice', data, 'sk', WORDS).verdict, 'correct');
    assert.equal(checkTranslation('The director shouted (action) twice', data, 'sk', WORDS).verdict, 'correct');
  });
  test("noun + 's reads as is / has as well as the possessive", () => {
    const data: ExerciseCheckData = { level: 'A1', reference: 'Their old globe has got a wooden stand.', acceptable: [], mistakes: [] };
    assert.equal(checkTranslation("Their old globe's got a wooden stand.", data, 'sk', WORDS).verdict, 'correct');
    const possessive: ExerciseCheckData = { level: 'A1', reference: "The dog's bowl is empty.", acceptable: [], mistakes: [] };
    assert.equal(checkTranslation("The dog's bowl is empty", possessive, 'sk', WORDS).verdict, 'correct');
  });
  test('number words are shown as words in a tip', () => {
    const data: ExerciseCheckData = { level: 'B1', reference: 'She wanted exactly the same one.', acceptable: [], mistakes: [] };
    assert.equal(checkTranslation('She wanted exactly the same kind.', data, 'sk', WORDS).feedback, 'Namiesto „kind“ patrí „one“.');
  });
});

describe('readings', () => {
  test("'d has two readings", () => {
    assert.equal(readings("I'd go.").length, 2);
  });
});

describe('typedAnswer.ts is the app file, byte for byte', () => {
  const app = join(process.env.HOME ?? '', 'Projects', 'and-again', 'lib', 'typedAnswer.ts');
  test('copy is identical', { skip: !existsSync(app) }, () => {
    assert.equal(readFileSync(join(HERE, 'typedAnswer.ts'), 'utf8'), readFileSync(app, 'utf8'));
  });
});
