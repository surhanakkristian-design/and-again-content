// Phase 1b checker – unit tests with synthetic fixtures.
// Run: node --test checker/v2/v2.test.ts
import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { compile, libraryIndex, type Annotation, type Library } from './match.ts';
import { check } from './check.ts';
import { buildForms } from './forms.ts';

const HERE = dirname(fileURLToPath(import.meta.url));
const WORDS = new Set(readFileSync(join(HERE, '..', '..', 'wordlist', 'en_words.txt'), 'utf8').split('\n').filter(Boolean));

const SYN = buildForms([{ groups: [
  { id: 'someone', kind: 'safe', pos: 'x', m: ['someone', 'somebody'] },
  { id: 'have_to', kind: 'safe', pos: 'v', m: ['have to', 'have got to'], irr: { have: ['has', 'had', 'had', 'having'] } },
  { id: 'lift_raise', kind: 'contextual', pos: 'v', m: ['lift', 'raise'], ok: 'She lifted her eyes.', bad: 'They raised money.' },
  { id: 'go_leave', kind: 'contextual', pos: 'v', m: ['go', 'leave'], ok: 'She went early.', bad: 'She left the book.' },
  { id: 'barely_hardly', kind: 'contextual', pos: 'x', m: ['barely', 'hardly'], ok: '…', bad: '…' },
  { id: 'big_large', kind: 'contextual', pos: 'a', m: ['big', 'large'], ok: '…', bad: '…' },
] }], WORDS);
const FORMS = SYN.forms;

const LIB: Library = libraryIndex([{ items: [
  { id: '44.01', verdict: 'wrong', slots: ['right', 'wrong'], sk: 'Patrí „{right}“, nie „{wrong}“.', cz: 'Patří „{right}“, ne „{wrong}“.', en: 'Use “{right}”, not “{wrong}”.' },
  { id: '44.02', verdict: 'wrong', slots: ['right', 'wrong', 'base'], sk: 'Základ je „{base}“: „{right}“.', cz: 'Základ je „{base}“: „{right}“.', en: 'The base is “{base}”: “{right}”.' },
  { id: '44.03', verdict: 'correct_with_tip', slots: ['right', 'wrong'], sk: 'X'.repeat(140) + ' „{right}“ „{wrong}“', cz: 'Y', en: 'Z' },
] }]);

const ann = (a: Partial<Annotation> & { v: string[] }): Annotation => ({ id: 1, t: 44, lv: 'B1', ...a });
const C = (a: Annotation) => compile(a, FORMS, LIB, { words: WORDS });
const verdict = (c: ReturnType<typeof C>, text: string, native = 'sk') => check(text, c, { native }).verdict;

const OFFICER = C(ann({
  v: ['The officer who stamped his passport barely raised her eyes.'],
  lk: ['who stamped'],
  s: { raised: 'lift_raise', barely: 'barely_hardly' },
  m: [['44.01', 'which stamped'], ['44.02', 'who stamp', null, { base: 'stamp' }], ['44.03', 'that stamped']],
}));

describe('forms', () => {
  test('regular forms by rule, kept only when in the word list; irregular from the table', () => {
    const lift = FORMS.groups.lift_raise.forms;
    assert.deepEqual(lift.past, ['lifted', 'raised']);
    assert.ok(lift.ing.includes('raising') && !lift.ing.includes('raiseing'));
    assert.deepEqual(FORMS.groups.go_leave.forms.past, ['went', 'left']);
    assert.ok(FORMS.groups.go_leave.forms['3sg'].includes('goes'));
    assert.ok(FORMS.groups.have_to.forms['3sg'].includes('has got to'));
    assert.ok(SYN.dropped.some((d) => d.includes('raiseing')));
  });
});

describe('s – contextual synonyms keep the form', () => {
  test('lifted for raised, hardly for barely', () => {
    assert.equal(verdict(OFFICER, 'The officer who stamped his passport barely lifted her eyes.'), 'correct');
    assert.equal(verdict(OFFICER, 'The officer who stamped his passport hardly lifted her eyes'), 'correct');
  });
  test('base form "lift"/"raise" for the past tense is rejected', () => {
    assert.equal(verdict(OFFICER, 'The officer who stamped his passport barely lift her eyes.'), 'wrong');
    assert.equal(verdict(OFFICER, 'The officer who stamped his passport barely raise her eyes.'), 'wrong');
  });
  test('irregular forms: went → left, never leaved', () => {
    const c = C(ann({ v: ['She went home early.'], lk: ['early'], s: { went: 'go_leave' } }));
    assert.equal(verdict(c, 'She left home early.'), 'correct');
    assert.equal(verdict(c, 'She leaved home early.'), 'wrong');
    assert.equal(verdict(c, 'She leave home early.'), 'wrong');
  });
});

describe('lock', () => {
  const c = C(ann({ v: ['Somebody has to lift the box.'], lk: ['has to lift'], s: { lift: 'lift_raise' } }));
  test('no contextual synonym inside the lock (anchor ignored + noted)', () => {
    assert.equal(verdict(c, 'Somebody has to raise the box.'), 'wrong');
    assert.ok(c.notes.some((n) => n.startsWith('s_anchor_in_lock')));
  });
  test('no safe synonym inside the lock, safe synonyms outside it', () => {
    assert.equal(verdict(c, 'Somebody has got to lift the box.'), 'wrong');
    assert.equal(verdict(c, 'Someone has to lift the box.'), 'correct');
  });
  test('safe multi-word group applies everywhere outside the lock', () => {
    const d = C(ann({ v: ['We have to leave before someone sees us.'], lk: ['sees'] }));
    assert.equal(verdict(d, 'We have got to leave before somebody sees us.'), 'correct');
  });
  test('contractions are normalisation, not a freedom', () => {
    const d = C(ann({ v: ['She does not like it.'], lk: ['does not like'] }));
    assert.equal(verdict(d, "She doesn't like it"), 'correct');
  });
});

describe('g – gender chains flip together', () => {
  const c = C(ann({ v: ['He pushed his bike up the hill.'], lk: ['pushed'], g: [['He', 'his']] }));
  test('consistent flip', () => {
    assert.equal(verdict(c, 'She pushed her bike up the hill.'), 'correct');
    assert.equal(verdict(c, 'He pushed his bike up the hill.'), 'correct');
  });
  test('half flip rejected', () => {
    assert.equal(verdict(c, 'She pushed his bike up the hill.'), 'wrong');
    assert.equal(verdict(c, 'He pushed her bike up the hill.'), 'wrong');
  });
});

describe('o – pronoun alternatives', () => {
  test('her | it', () => {
    const c = C(ann({ v: ['I saw her in the garden.'], lk: ['saw'], o: { her: 'her|it' } }));
    assert.equal(verdict(c, 'I saw it in the garden.'), 'correct');
    assert.equal(verdict(c, 'I saw him in the garden.'), 'wrong');
  });
});

describe('d – determiners', () => {
  test('code A on the determiner', () => {
    const c = C(ann({ v: ['The dog is barking.'], lk: ['is barking'], d: { The: 'A' } }));
    assert.equal(verdict(c, 'A dog is barking.'), 'correct');
    assert.equal(verdict(c, 'That dog is barking.'), 'correct');
    assert.equal(verdict(c, 'Dog is barking.'), 'wrong');
  });
  test('code P allows ∅', () => {
    const c = C(ann({ v: ['The apples are red.'], lk: ['are'], d: { The: 'P' } }));
    assert.equal(verdict(c, 'Apples are red.'), 'correct');
    assert.equal(verdict(c, 'Those apples are red.'), 'correct');
    assert.equal(verdict(c, 'An apples are red.'), 'wrong');
  });
  test('code Z on a bare noun inserts the article', () => {
    const c = C(ann({ v: ['Water is cold.'], lk: ['is'], d: { Water: 'Z' } }));
    assert.equal(verdict(c, 'The water is cold.'), 'correct');
    assert.equal(verdict(c, 'A water is cold.'), 'wrong');
  });
  test('explicit list, a ≡ an', () => {
    const c = C(ann({ v: ['She ate the orange.'], lk: ['ate'], d: { the: 'the|a' } }));
    assert.equal(verdict(c, 'She ate an orange.'), 'correct');
    const k = C(ann({ v: ['She lost the key.'], lk: ['lost'], d: { the: 'the|her|his' } }));
    assert.equal(verdict(k, 'She lost her key.'), 'correct');
    assert.equal(verdict(k, 'She lost my key.'), 'wrong');
  });
});

describe('p – optional words', () => {
  test('+w anywhere outside the lock, at most once', () => {
    const c = C(ann({ v: ['They have finished the work.'], lk: ['have finished'], p: ['+already'] }));
    assert.equal(verdict(c, 'They have finished the work already.'), 'correct');
    assert.equal(verdict(c, 'Already they have finished the work.'), 'correct');
    assert.equal(verdict(c, 'They have already finished the work.'), 'wrong');
    assert.equal(verdict(c, 'Already they have finished the work already.'), 'wrong');
  });
  test('+w@anchor only right after the anchor', () => {
    const c = C(ann({ v: ['We cleaned the kitchen yesterday.'], lk: ['yesterday'], p: ['+up@cleaned'] }));
    assert.equal(verdict(c, 'We cleaned up the kitchen yesterday.'), 'correct');
    assert.equal(verdict(c, 'We cleaned the kitchen up yesterday.'), 'wrong');
  });
  test('-anchor may be dropped (numbers normalised)', () => {
    const c = C(ann({ v: ['I waited for two hours.'], lk: ['waited'], p: ['-for'] }));
    assert.equal(verdict(c, 'I waited two hours.'), 'correct');
    assert.equal(verdict(c, 'I waited 2 hours'), 'correct');
  });
  test('discontinuous lock: words may go between the pieces', () => {
    const c = C(ann({ v: ['She would never have been late.'], lk: ['would .. have been'], p: ['+really'] }));
    assert.equal(verdict(c, 'She would never really have been late.'), 'correct');
    assert.equal(verdict(c, 'She would never have really been late.'), 'wrong');
  });
});

describe('typo (step 3)', () => {
  const c = C(ann({ lv: 'A1', v: ['The children played in the garden.'], lk: ['played'] }));
  test('one typo → correct_with_tip', () => {
    const r = check('The children played in the gardn.', c, { native: 'sk' });
    assert.equal(r.verdict, 'correct_with_tip');
    assert.equal(r.step, 'typo');
    assert.equal(r.feedback, 'Preklep: správne je „garden“.');
  });
  test('real-word exclusion', () => {
    assert.equal(check('The children plated in the garden.', c, { native: 'sk' }).verdict, 'wrong');
  });
  test('word-form exclusion', () => {
    assert.equal(check('The children played in the gardenn.', c, { native: 'sk' }).verdict, 'wrong');
  });
  test('typo against an allowed alternative names that alternative', () => {
    const b = C(ann({ v: ['The big dog sleeps.'], lk: ['sleeps'], s: { big: 'big_large' } }));
    const r = check('The lagre dog sleeps.', b, { native: 'sk' });
    assert.equal(r.step, 'typo');
    assert.ok(r.feedback?.includes('large'));
  });
});

describe('library mistakes (step 2)', () => {
  test('pattern with freedoms, {right}/{wrong} filled, per language', () => {
    const answer = 'The officer which stamped his passport hardly lifted her eyes.';
    const sk = check(answer, OFFICER, { native: 'sk' });
    assert.equal(sk.step, 'mistake');
    assert.equal(sk.feedback, 'Patrí „who stamped“, nie „which stamped“.');
    assert.equal(check(answer, OFFICER, { native: 'cs' }).feedback, 'Patří „who stamped“, ne „which stamped“.');
    assert.equal(check(answer, OFFICER, { native: 'de' }).feedback, 'Use “who stamped”, not “which stamped”.');
    assert.equal(check(answer, OFFICER, { native: 'de', level: 'A2' }).feedback, null);
    assert.equal(check(answer, OFFICER, { native: 'de', level: 'A2' }).verdict, 'wrong');
  });
  test('extra per-sentence slot', () => {
    const r = check('The officer who stamp his passport barely raised her eyes.', OFFICER, { native: 'sk' });
    assert.equal(r.feedback, 'Základ je „stamp“: „who stamped“.');
  });
  test('150-character cap → automatic tip instead', () => {
    const r = check('The officer that stamped his passport barely raised her eyes.', OFFICER, { native: 'sk' });
    assert.equal(r.verdict, 'correct_with_tip');
    assert.ok(r.feedback && r.feedback.length <= 150 && !r.feedback.startsWith('XXX'));
  });
  test('a mistake beats step 4', () => {
    const answer = 'The officer which stamped his passport barely raised her eyes.';
    assert.equal(check(answer, { ...OFFICER, mistakes: [] }, { native: 'sk' }).step, 'auto');
    assert.equal(check(answer, OFFICER, { native: 'sk' }).step, 'mistake');
  });
});

describe('automatic tip (step 4)', () => {
  test('never names an allowed alternative', () => {
    const r = check('The officer who stamped his passport lifted her eyes.', OFFICER, { native: 'sk' });
    assert.equal(r.verdict, 'wrong');
    assert.ok(r.feedback && !r.feedback.includes('raised') && !r.feedback.includes('lifted'), r.feedback ?? '');
    assert.match(r.feedback!, /Chýba „(barely|hardly)“\./);
  });
  test('closest path is shown with the learner\'s allowed choice', () => {
    const r = check('The officer who stamped his passport hardly lifted her eye.', OFFICER, { native: 'en' });
    assert.equal(r.feedback, 'Write “eyes” instead of “eye”.');
    assert.equal(r.closest, 'The officer who stamped his passport hardly lifted her eyes.');
  });
});

describe('BrE / AmE (step 1b)', () => {
  test('pair list and -our rule', () => {
    const g = C(ann({ v: ['The walls are grey.'], lk: ['are'] }));
    assert.equal(check('The walls are gray.', g, { native: 'sk' }).step, 'spelling_variant');
    const c = C(ann({ v: ['What colour is it?'], lk: ['is'] }));
    const r = check('What color is it?', c, { native: 'sk' });
    assert.equal(r.verdict, 'correct');
    assert.equal(r.step, 'spelling_variant');
  });
});
