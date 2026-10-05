// check-listen-speak: the handler with mocked loaders and a mocked model (no
// network), and the lenient speaking rule. Run: npm test.
import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import {
  MAX_AUDIO_BASE64_CHARS,
  handleCheck,
  parseListeningReply,
  parseRequest,
  type HandlerDeps,
  type ListeningQuestion,
  type ModelReply,
  type ModelRequest,
} from './logic.ts';
import { geminiRequestBody, parseGeminiUsage } from './gemini.ts';
import {
  letterSimilarity,
  listeningMatchesLocally,
  matchSpokenLine,
  spokenLineMatches,
} from '../_shared/listenSpeakRules.ts';

// A video as it is in the DB: the transcript exists, but the check must never use it
const MEDIA = {
  id: 1,
  transcript: 'I take a short break. But I must study now.',
  media_url: 'https://example.test/a_break_1.mp4',
  speech_sentences: ['I take a short break But I must study now', "It's not enough.", 'Awesome!'],
};
const QUESTION: ListeningQuestion = {
  id: 7,
  question: 'What kind of break does he take?',
  correctAnswer: 'short',
  acceptedAnswers: ['a short break', 'a short one'],
};
const AUDIO = 'UklGRiQAAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YQAAAAA=';

const harness = (reply: string | Error = 'SAME') => {
  const requests: ModelRequest[] = [];
  const logs: Record<string, unknown>[] = [];
  const deps: HandlerDeps = {
    loadQuestion: async (id) => (id === QUESTION.id ? QUESTION : null),
    loadSentences: async (mediaId) => (mediaId === MEDIA.id ? MEDIA.speech_sentences : null),
    callModel: async (request): Promise<ModelReply> => {
      requests.push(request);
      if (reply instanceof Error) throw reply;
      return { text: reply, usage: { inputTokens: 100, outputTokens: 1, audioTokens: 30 }, model: 'gemini-3.1-flash-lite' };
    },
    log: (event) => logs.push(event),
  };
  return { deps, requests, logs };
};

describe('listening: free check first, the model only after it fails', () => {
  test('exact answer: 0 model calls', async () => {
    const h = harness();
    const r = await handleCheck({ kind: 'listening', question_id: 7, answer: 'Short.' }, h.deps);
    assert.deepEqual(r.body, { kind: 'listening', correct_answer: 'short', verdict: 'correct', path: 'exact' });
    assert.equal(h.requests.length, 0);
  });

  test('near-exact (accepted variant, articles, case, punctuation): 0 model calls', async () => {
    for (const answer of ['a short one', 'A SHORT BREAK!', 'short break', 'the short one']) {
      const h = harness();
      const r = await handleCheck({ kind: 'listening', question_id: 7, answer }, h.deps);
      assert.equal((r.body as { verdict: string }).verdict, 'correct', answer);
      assert.equal(h.requests.length, 0, answer);
    }
  });

  test('one letter off in a long word: correct with 0 model calls; a different word still goes to the model', async () => {
    const typo = harness('DIFF');
    const r = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a shortt break' }, typo.deps);
    assert.equal((r.body as { verdict: string; path: string }).verdict, 'correct');
    assert.equal((r.body as { path: string }).path, 'exact');
    assert.equal(typo.requests.length, 0);
    const other = harness('DIFF');
    const r2 = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a small break' }, other.deps);
    assert.equal((r2.body as { verdict: string }).verdict, 'wrong');
    assert.equal(other.requests.length, 1);
  });

  test('not matched locally: exactly ONE model call, SAME -> correct, DIFF -> wrong', async () => {
    const same = harness('SAME');
    const r1 = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a quick little break' }, same.deps);
    assert.equal((r1.body as { verdict: string; path: string }).verdict, 'correct');
    assert.equal((r1.body as { path: string }).path, 'model');
    assert.equal(same.requests.length, 1);
    const diff = harness('DIFF');
    const r2 = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a long break' }, diff.deps);
    assert.equal((r2.body as { verdict: string }).verdict, 'wrong');
    assert.equal(diff.requests.length, 1);
  });

  test('the model sees question, correct answer, variants and the answer – never the transcript or the video', async () => {
    const h = harness('SAME');
    await handleCheck({ kind: 'listening', question_id: 7, answer: 'a quick little break' }, h.deps);
    const sent = JSON.stringify(h.requests[0]);
    for (const part of [QUESTION.question, QUESTION.correctAnswer, ...QUESTION.acceptedAnswers, 'a quick little break']) {
      assert.ok(sent.includes(part), part);
    }
    assert.ok(!sent.includes('I must study now'), 'transcript text');
    assert.ok(!sent.toLowerCase().includes('transcript'), 'transcript field');
    assert.ok(!sent.includes('.mp4'), 'video');
    assert.ok(h.requests[0].parts.every((p) => 'text' in p), 'text only, no media');
    assert.equal(h.requests[0].temperature, 0);
  });

  test('the loaders never read media.transcript (source check of the function and the app loader)', () => {
    const index = readFileSync(new URL('./index.ts', import.meta.url), 'utf8');
    const appLoader = readFileSync(new URL('../../../lib/listenSpeakData.ts', import.meta.url), 'utf8');
    const selects = [...index.matchAll(/\.select\('([^']*)'\)/g), ...appLoader.matchAll(/\.select\('([^']*)'\)/g)].map((m) => m[1]);
    assert.ok(selects.length >= 4);
    for (const columns of selects) assert.ok(!columns.includes('transcript'), columns);
  });

  test('model failure or nonsense -> not_verified (nothing is scored)', async () => {
    const broken = harness(new Error('Gemini HTTP 503'));
    const r = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a quick little break' }, broken.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'not_verified');
    assert.equal(parseListeningReply('Maybe'), null);
    assert.equal(parseListeningReply(' same.\n'), 'correct');
    assert.equal(parseListeningReply('DIFF'), 'wrong');
  });

  test('a model call that hangs is cut off', async () => {
    const h = harness();
    h.deps.callModel = () => new Promise(() => undefined);
    h.deps.timeoutMs = { listening: 20 };
    const r = await handleCheck({ kind: 'listening', question_id: 7, answer: 'a quick little break' }, h.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'not_verified');
  });

  test('unknown question -> 404, bad input -> 400', async () => {
    const h = harness();
    assert.equal((await handleCheck({ kind: 'listening', question_id: 999, answer: 'x' }, h.deps)).status, 404);
    assert.equal((await handleCheck({ kind: 'listening', question_id: 7, answer: '  ' }, h.deps)).status, 400);
    assert.equal((await handleCheck({ kind: 'listening', question_id: 7, answer: 'x'.repeat(201) }, h.deps)).status, 400);
    assert.equal((await handleCheck({ kind: 'nope' }, h.deps)).status, 400);
  });
});

describe('speaking: transcription + the lenient rule; the audio is never kept', () => {
  test('a matching line -> match; the audio goes to the model once, as inline data', async () => {
    const h = harness('Um, it is not enough.');
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.deepEqual(r.body, {
      kind: 'speaking',
      verdict: 'match',
      heard: 'Um, it is not enough.',
      matched: "It's not enough.",
      closest: "It's not enough.",
      calls: 1,
    });
    assert.equal(h.requests.length, 1);
    const audioParts = h.requests[0].parts.filter((p) => 'audio' in p);
    assert.equal(audioParts.length, 1);
    assert.equal(h.requests[0].temperature, 0);
    // The first transcription is not told which sentences are expected
    assert.ok(!JSON.stringify(h.requests[0]).includes('enough'));
  });

  test('a different sentence -> no_match with the nearest sentence', async () => {
    const h = harness('That car are amazing');
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'no_match');
  });

  test('the audio never reaches a log line or a metrics row', async () => {
    const h = harness('Awesome!');
    await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    const broken = harness(new Error('Gemini HTTP 500'));
    await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, broken.deps);
    const logged = JSON.stringify([...h.logs, ...broken.logs]);
    assert.ok(h.logs.length === 1 && broken.logs.length === 1);
    assert.ok(!logged.includes(AUDIO.slice(0, 24)), 'no audio bytes in logs');
    // the function has no storage write at all (source check)
    const index = readFileSync(new URL('./index.ts', import.meta.url), 'utf8');
    assert.ok(!/storage\s*\.\s*from|\.upload\(|\.insert\(/.test(index), 'no storage / table write in the function');
  });

  test('silence (empty transcript) -> no_match with nothing heard', async () => {
    const h = harness('\n');
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.deepEqual(r.body, { kind: 'speaking', verdict: 'no_match', heard: '', matched: null, closest: null, calls: 1 });
    assert.equal(h.requests.length, 1, 'nothing heard: no second listen (it could only invent a sentence)');
  });

  // Call 1 answers from the first list entry, call 2 from the second
  const twoListens = (first: string, second: string) => {
    const h = harness();
    const replies = [first, second];
    h.deps.callModel = async (request) => {
      h.requests.push(request);
      return { text: replies[h.requests.length - 1] ?? '', usage: { inputTokens: 100, outputTokens: 5, audioTokens: 30 }, model: 'm' };
    };
    return h;
  };

  test('accent: call 1 misses, call 2 (with the sentences) decodes it, call 1 sounds alike -> match', async () => {
    const h = twoListens('It is not enuf', "It's not enough.");
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'match');
    assert.equal((r.body as { matched: string }).matched, "It's not enough.");
    assert.equal((r.body as { heard: string }).heard, 'It is not enuf', 'what call 1 heard is shown');
    assert.equal(h.requests.length, 2);
    assert.ok(!JSON.stringify(h.requests[0]).includes('enough'), 'call 1 does not know the sentences');
    assert.ok(JSON.stringify(h.requests[1]).includes('enough'), 'call 2 gets them as context');
  });
  test('a different sentence stays a miss even when call 2 "hears" a listed one', async () => {
    const h = twoListens('Listen, the fizz.', 'Awesome!');
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'no_match');
    assert.equal(h.requests.length, 2);
  });

  test('call 2 failing keeps the miss (not "could not check")', async () => {
    const h = harness();
    h.deps.callModel = async (request) => {
      h.requests.push(request);
      if (h.requests.length === 2) throw new Error('Gemini HTTP 503');
      return { text: 'That car are amazing', usage: { inputTokens: 1, outputTokens: 1 }, model: 'm' };
    };
    const r = await handleCheck({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps);
    assert.equal((r.body as { verdict: string }).verdict, 'no_match');
  });

  test('request validation: unknown video 404, too long or foreign audio 400', async () => {
    const h = harness();
    assert.equal((await handleCheck({ kind: 'speaking', media_id: 2, audio_base64: AUDIO, mime_type: 'audio/wav' }, h.deps)).status, 404);
    assert.equal(
      parseRequest({ kind: 'speaking', media_id: 1, audio_base64: 'A'.repeat(MAX_AUDIO_BASE64_CHARS + 4), mime_type: 'audio/wav' }).ok,
      false
    );
    assert.equal(parseRequest({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'video/mp4' }).ok, false);
    assert.equal(parseRequest({ kind: 'speaking', media_id: 1, audio_base64: AUDIO, mime_type: 'audio/webm;codecs=opus' }).ok, true);
  });
});

describe('the lenient speaking rule', () => {
  const accepts: [string, string][] = [
    ['That car is amazing!', 'that car is amazing'],
    ['I am at home.', "I'm at home"],
    ["It's not enough.", 'it is not enough'],
    ['I look away for one second.', 'I look away for 1 second.'],
    ['I take a course online.', 'I take course online'],
    ['I take a course online.', 'I take the course online'],
    ['My class is crazy!', 'Uh, my class is, um, crazy.'],
    ['Look at all my certificates!', 'look at all my certificate'],
    ['I study very hard.', 'I studdy very hard'],
    ['Awesome!', 'awesome'],
    ['Ah, yes.', 'yes'],
  ];
  const rejects: [string, string][] = [
    ['That car is amazing!', 'That car are amazing!'],
    ['I study very hard.', 'I study hard.'],
    ['I study very hard.', 'I study very very hard.'],
    ['I study very hard.', 'My class is crazy!'],
    ['Look at all my certificates!', 'look at all my certificate i studdy'],
    ['I look away for one second.', 'I look away for 2 second.'],
    ['I am at home.', 'I am not at home.'],
    ['Look at all my certificates!', 'look at all her certificates'],
    ['Awesome!', ''],
  ];
  for (const [sentence, heard] of accepts) {
    test(`accepts "${heard}" for "${sentence}"`, () => assert.equal(spokenLineMatches(heard, sentence), true));
  }
  for (const [sentence, heard] of rejects) {
    test(`rejects "${heard}" for "${sentence}"`, () => assert.equal(spokenLineMatches(heard, sentence), false));
  }
  test('letter similarity guards the second listen', () => {
    assert.ok(letterSimilarity('work every bit', 'Worth every bit.') >= 0.8);
    assert.ok(letterSimilarity('Listen, the fizz.', 'In they go.') < 0.3);
    assert.equal(letterSimilarity('', 'Awesome!'), 0);
  });
  test('any sentence of the video counts; the nearest one is shown after a miss', () => {
    const list = ['I study very hard.', 'Look at all my certificates!'];
    assert.equal(matchSpokenLine('look at all my certificates', list).matched, 'Look at all my certificates!');
    const miss = matchSpokenLine('I study very hardly', list);
    assert.equal(miss.matched, null);
    assert.equal(miss.closest, 'I study very hard.');
  });
  test('listening free check: typed-answer rules + articles', () => {
    assert.equal(listeningMatchesLocally('1 second', 'one second', []), true);
    assert.equal(listeningMatchesLocally("it isn't enough", 'not enough', ["it's not enough", 'it is not enough']), true);
    assert.equal(listeningMatchesLocally('20 euros', '250 Euros', []), false);
  });
  test('listening free check: ONE letter off in ONE word of 5+ letters is forgiven (decision 71)', () => {
    // changed, dropped, added letter – against correct_answer and against an accepted variant
    assert.equal(listeningMatchesLocally('a beautifull dress', 'A beautiful dress', []), true);
    assert.equal(listeningMatchesLocally('the tower bridje', 'Tower Bridge', []), true);
    assert.equal(listeningMatchesLocally('chocolat', 'cake', ['chocolate']), true);
    assert.equal(listeningMatchesLocally('the Eifel tower', 'the Eiffel Tower', []), true);
    // a different word is still wrong
    assert.equal(listeningMatchesLocally('a lovely dress', 'A beautiful dress', []), false);
    assert.equal(listeningMatchesLocally('bridge', 'Tower', []), false);
    // short words must be exact (cat / car), both words need 5+ letters
    assert.equal(listeningMatchesLocally('a car', 'a cat', []), false);
    assert.equal(listeningMatchesLocally('tent', 'tents', []), false);
    // one word only, one letter only (a transposition is two)
    assert.equal(listeningMatchesLocally('beautifull dresss', 'beautiful dress', []), false);
    assert.equal(listeningMatchesLocally('beautifull shoess', 'beautiful shoes', []), false);
    assert.equal(listeningMatchesLocally('recieve', 'receive', []), false);
    // no digit in either word
    assert.equal(listeningMatchesLocally('12345', '12346', []), false);
    assert.equal(listeningMatchesLocally('room 12a45', 'room 12345', []), false);
  });
});

describe('Gemini request shape', () => {
  test('temperature 0, the audio as inline_data, minimal thinking for Flash-Lite', () => {
    const body = geminiRequestBody(
      { purpose: 'speaking', system: 'S', parts: [{ audio: { mimeType: 'audio/wav', base64: AUDIO } }, { text: 'T' }], temperature: 0, maxOutputTokens: 120 },
      'gemini-3.1-flash-lite'
    ) as { contents: { parts: Record<string, unknown>[] }[]; generationConfig: Record<string, unknown> };
    assert.deepEqual(body.contents[0].parts[0], { inline_data: { mime_type: 'audio/wav', data: AUDIO } });
    assert.equal(body.generationConfig.temperature, 0);
    assert.deepEqual(body.generationConfig.thinkingConfig, { thinkingLevel: 'minimal' });
  });
  test('usage: audio tokens and thinking tokens are counted', () => {
    assert.deepEqual(
      parseGeminiUsage({
        usageMetadata: {
          promptTokenCount: 49,
          candidatesTokenCount: 5,
          thoughtsTokenCount: 2,
          promptTokensDetails: [{ modality: 'AUDIO', tokenCount: 30 }, { modality: 'TEXT', tokenCount: 19 }],
        },
      }),
      { inputTokens: 49, outputTokens: 7, audioTokens: 30 }
    );
  });
});
