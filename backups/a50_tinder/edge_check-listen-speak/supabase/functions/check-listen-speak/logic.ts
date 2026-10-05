// check-listen-speak – the pure handler (no Deno, no Supabase client, no fetch):
// the data loaders and the model call are injected, so the whole flow runs under
// node --test with mocks (logic.test.ts) and under the local dev server
// (scripts/listen-speak-dev-server.mjs) with real ones.
//
// LISTENING  in: { kind: 'listening', question_id, answer }
//   1. the question row is loaded HERE (question, correct_answer, accepted_answers);
//      the app never sends the texts it is judged against;
//   2. the free check (lib rules: exact / typed-answer variant / articles / one-letter typo) → correct, no model;
//   3. otherwise ONE model call that sees the question, the correct answer, the
//      accepted variants and the learner's answer – never the transcript, never
//      the video – and replies SAME or DIFF.
// SPEAKING   in: { kind: 'speaking', media_id, audio_base64, mime_type }
//   1. media.speech_sentences are loaded HERE;
//   2. call 1 transcribes the recording WITHOUT knowing the sentences; the
//      deterministic rule (matchSpokenLine) decides → match;
//   3. only when that misses (and something was heard): call 2 listens again WITH
//      the video's sentences as context (a strong accent is decoded, measured
//      9 of 30 accented misses → 30 of 30); its line counts only when it matches a
//      sentence by the same rule AND call 1's words sound like that sentence
//      (letter similarity ≥ SECOND_LISTEN_MIN_SIMILARITY) – the context call
//      alone once turned a different spoken sentence into a listed one.
//   The audio lives only in this request: never stored, never logged, never
//   written anywhere.
// Out: see ListeningResponse / SpeakingResponse. `not_verified` = the model could
// not be reached or answered nonsense; the app then says so and lets the learner
// go on (nothing is scored).

import {
  cleanAccepted,
  cleanSentences,
  letterSimilarity,
  listeningMatchesLocally,
  matchSpokenLine,
} from '../_shared/listenSpeakRules.ts';

// ---------------------------------------------------------------------------
// Named constants
// ---------------------------------------------------------------------------

/** Longest typed listening answer accepted. */
export const MAX_ANSWER_CHARS = 200;
/** Largest recording accepted, as base64 characters (16 kHz mono WAV ≈ 15 s). */
export const MAX_AUDIO_BASE64_CHARS = 700_000;
/** Recordings the model is given. */
export const AUDIO_MIME_TYPES = ['audio/wav', 'audio/webm', 'audio/ogg', 'audio/mp4', 'audio/aac', 'audio/mpeg'] as const;
/** Hard stop for one model call; over it the answer is `not_verified`. */
export const LISTENING_TIMEOUT_MS = 6000;
export const SPEAKING_TIMEOUT_MS = 10000;
/** Output token caps: SAME/DIFF is one token, but Flash-Lite needs head room (a cap of 4 returned an empty MAX_TOKENS reply); a transcript is one or two sentences. */
export const LISTENING_MAX_OUTPUT_TOKENS = 16;
export const SPEAKING_MAX_OUTPUT_TOKENS = 120;
export const DEFAULT_MODEL = 'gemini-3.1-flash-lite';
/** Call 2 may only confirm a sentence that call 1's transcript already resembles (0..1). */
export const SECOND_LISTEN_MIN_SIMILARITY = 0.3;

// ---------------------------------------------------------------------------
// Request
// ---------------------------------------------------------------------------

export type CheckRequest =
  | { kind: 'listening'; questionId: number; answer: string }
  | { kind: 'speaking'; mediaId: number; audioBase64: string; mimeType: string };

export type ParseResult = { ok: true; request: CheckRequest } | { ok: false; error: string };

const positiveInt = (value: unknown): number | null =>
  typeof value === 'number' && Number.isInteger(value) && value > 0 ? value : null;

export const parseRequest = (body: unknown): ParseResult => {
  if (!body || typeof body !== 'object') return { ok: false, error: 'Body must be a JSON object' };
  const b = body as Record<string, unknown>;
  if (b.kind === 'listening') {
    const questionId = positiveInt(b.question_id);
    if (questionId === null) return { ok: false, error: 'question_id must be a positive integer' };
    const answer = typeof b.answer === 'string' ? b.answer.trim() : '';
    if (!answer) return { ok: false, error: 'answer is empty' };
    if (answer.length > MAX_ANSWER_CHARS) return { ok: false, error: 'answer is too long' };
    return { ok: true, request: { kind: 'listening', questionId, answer } };
  }
  if (b.kind === 'speaking') {
    const mediaId = positiveInt(b.media_id);
    if (mediaId === null) return { ok: false, error: 'media_id must be a positive integer' };
    const audioBase64 = typeof b.audio_base64 === 'string' ? b.audio_base64 : '';
    if (!audioBase64 || !/^[A-Za-z0-9+/]+=*$/.test(audioBase64)) return { ok: false, error: 'audio_base64 is missing' };
    if (audioBase64.length > MAX_AUDIO_BASE64_CHARS) return { ok: false, error: 'recording is too long' };
    const mimeType = typeof b.mime_type === 'string' ? b.mime_type.split(';')[0].trim().toLowerCase() : '';
    if (!(AUDIO_MIME_TYPES as readonly string[]).includes(mimeType)) return { ok: false, error: 'unsupported mime_type' };
    return { ok: true, request: { kind: 'speaking', mediaId, audioBase64, mimeType } };
  }
  return { ok: false, error: "kind must be 'listening' or 'speaking'" };
};

// ---------------------------------------------------------------------------
// Model requests (plain data; the caller maps them to the Gemini API)
// ---------------------------------------------------------------------------

export type ModelPart = { text: string } | { audio: { mimeType: string; base64: string } };

export interface ModelRequest {
  purpose: 'listening' | 'speaking';
  system: string;
  parts: ModelPart[];
  temperature: 0;
  maxOutputTokens: number;
}

export interface ModelUsage {
  inputTokens: number;
  outputTokens: number;
  audioTokens?: number;
}

export interface ModelReply {
  text: string;
  usage: ModelUsage;
  model: string;
}

export const LISTENING_SYSTEM =
  'You grade a short answer to a listening-comprehension question for learners of English. ' +
  'Reply with exactly one word: SAME if the learner\'s answer gives the same information as the correct answer ' +
  '(spelling mistakes, word order, missing or extra small words, numbers as digits or words, synonyms are fine), ' +
  'DIFF if it gives different or missing information.';

export interface ListeningQuestion {
  id: number;
  question: string;
  correctAnswer: string;
  acceptedAnswers: string[];
}

export const listeningModelRequest = (q: ListeningQuestion, answer: string): ModelRequest => ({
  purpose: 'listening',
  system: LISTENING_SYSTEM,
  parts: [
    {
      text:
        `Question: ${q.question}\n` +
        `Correct answer: ${q.correctAnswer}\n` +
        `Also accepted: ${q.acceptedAnswers.length > 0 ? q.acceptedAnswers.join(' | ') : '(none)'}\n` +
        `Learner's answer: ${answer}`,
    },
  ],
  temperature: 0,
  maxOutputTokens: LISTENING_MAX_OUTPUT_TOKENS,
});

export const SPEAKING_SYSTEM =
  'You transcribe a short recording of a learner of English saying one sentence. ' +
  'Write exactly the English words that were said, in standard spelling, even with a strong accent. ' +
  'Do not correct grammar, do not complete or improve the sentence, do not add words that were not said. ' +
  'If no English words can be heard, reply with an empty line.';

export const speakingContextSystem = (sentences: readonly string[]): string =>
  'You transcribe a short recording of a learner of English with a strong accent. ' +
  'For context only, the video they watched contains these sentences:\n' +
  sentences.map((s) => `- ${s}`).join('\n') +
  '\nThe learner may say one of them, or something else entirely. Write exactly the words that were actually said, in standard spelling, ' +
  'using the context only to decode sounds that the accent makes unclear. If the learner said different words or a different sentence, write those words. ' +
  'Do not correct grammar and never output a sentence from the list unless those words were said. If no English words can be heard, reply with an empty line.';

/** Call 2 (only after call 1 missed): the same recording, with the sentences as context. */
export const speakingContextRequest = (audioBase64: string, mimeType: string, sentences: readonly string[]): ModelRequest => ({
  purpose: 'speaking',
  system: speakingContextSystem(sentences),
  parts: [{ audio: { mimeType, base64: audioBase64 } }, { text: 'Transcribe the recording.' }],
  temperature: 0,
  maxOutputTokens: SPEAKING_MAX_OUTPUT_TOKENS,
});

export const speakingModelRequest = (audioBase64: string, mimeType: string): ModelRequest => ({
  purpose: 'speaking',
  system: SPEAKING_SYSTEM,
  parts: [{ audio: { mimeType, base64: audioBase64 } }, { text: 'Transcribe the recording.' }],
  temperature: 0,
  maxOutputTokens: SPEAKING_MAX_OUTPUT_TOKENS,
});

/** SAME / DIFF → verdict; anything else → null (not verified). */
export const parseListeningReply = (text: string): 'correct' | 'wrong' | null => {
  const word = text.trim().replace(/[^A-Za-z]/g, '').toUpperCase();
  if (word === 'SAME') return 'correct';
  if (word === 'DIFF' || word === 'DIFFERENT') return 'wrong';
  return null;
};

/** The transcript as one plain line (quotes and "Transcript:" labels dropped). */
export const cleanTranscript = (text: string): string =>
  text
    .replace(/^\s*(transcript(ion)?\s*:)/i, '')
    .replace(/[“”"]/g, '')
    .replace(/\s+/g, ' ')
    .trim();

// ---------------------------------------------------------------------------
// Handler
// ---------------------------------------------------------------------------

export interface ListeningResponse {
  kind: 'listening';
  verdict: 'correct' | 'wrong' | 'not_verified';
  /** 'exact' = the free check decided (0 model calls), 'model' = one model call */
  path: 'exact' | 'model';
  correct_answer: string;
}

export interface SpeakingResponse {
  kind: 'speaking';
  verdict: 'match' | 'no_match' | 'not_verified';
  /** what the model heard ('' = nothing intelligible) */
  heard: string;
  /** model calls used: 1, or 2 when the second listen ran */
  calls?: number;
  matched: string | null;
  closest: string | null;
}

export interface HandlerDeps {
  loadQuestion: (id: number) => Promise<ListeningQuestion | null>;
  loadSentences: (mediaId: number) => Promise<string[] | null>;
  callModel: (request: ModelRequest) => Promise<ModelReply>;
  /** metrics/log sink – receives counts and verdicts only, never the audio or the texts */
  log?: (event: Record<string, unknown>) => void;
  timeoutMs?: { listening?: number; speaking?: number };
}

export interface HandlerResult {
  status: number;
  body: ListeningResponse | SpeakingResponse | { error: string };
}

const withTimeout = <T>(promise: Promise<T>, ms: number): Promise<T> => {
  let timer: ReturnType<typeof setTimeout> | undefined;
  const timeout = new Promise<never>((_, reject) => {
    timer = setTimeout(() => reject(new Error('model timeout')), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer)) as Promise<T>;
};

/** Rows of listening_questions → the handler's question (accepted answers cleaned). */
export const toListeningQuestion = (row: {
  id: number;
  question: string | null;
  correct_answer: string | null;
  accepted_answers: unknown;
}): ListeningQuestion | null => {
  const question = row.question?.trim() ?? '';
  const correctAnswer = row.correct_answer?.trim() ?? '';
  if (!question || !correctAnswer) return null;
  return { id: row.id, question, correctAnswer, acceptedAnswers: cleanAccepted(row.accepted_answers) };
};

export async function handleCheck(body: unknown, deps: HandlerDeps): Promise<HandlerResult> {
  const parsed = parseRequest(body);
  if (!parsed.ok) return { status: 400, body: { error: parsed.error } };
  const request = parsed.request;
  const log = deps.log ?? (() => undefined);

  if (request.kind === 'listening') {
    const question = await deps.loadQuestion(request.questionId);
    if (!question) return { status: 404, body: { error: 'Question not found' } };
    const base = { kind: 'listening' as const, correct_answer: question.correctAnswer };
    if (listeningMatchesLocally(request.answer, question.correctAnswer, question.acceptedAnswers)) {
      log({ event: 'listening_check', path: 'exact', verdict: 'correct', question_id: question.id });
      return { status: 200, body: { ...base, verdict: 'correct', path: 'exact' } };
    }
    const startedAt = Date.now();
    try {
      const reply = await withTimeout(
        deps.callModel(listeningModelRequest(question, request.answer)),
        deps.timeoutMs?.listening ?? LISTENING_TIMEOUT_MS
      );
      const verdict = parseListeningReply(reply.text) ?? 'not_verified';
      log({
        event: 'listening_check',
        path: 'model',
        verdict,
        question_id: question.id,
        model: reply.model,
        tokens_in: reply.usage.inputTokens,
        tokens_out: reply.usage.outputTokens,
        model_ms: Date.now() - startedAt,
      });
      return { status: 200, body: { ...base, verdict, path: 'model' } };
    } catch (error) {
      log({
        event: 'listening_check',
        path: 'model',
        verdict: 'not_verified',
        question_id: question.id,
        error: error instanceof Error ? error.message : 'model error',
      });
      return { status: 200, body: { ...base, verdict: 'not_verified', path: 'model' } };
    }
  }

  const sentences = cleanSentences(await deps.loadSentences(request.mediaId));
  if (sentences.length === 0) return { status: 404, body: { error: 'Video has no spoken sentences' } };
  const startedAt = Date.now();
  const timeout = deps.timeoutMs?.speaking ?? SPEAKING_TIMEOUT_MS;
  const usage = { tokens_in: 0, tokens_audio: 0, tokens_out: 0 };
  const count = (reply: ModelReply) => {
    usage.tokens_in += reply.usage.inputTokens;
    usage.tokens_audio += reply.usage.audioTokens ?? 0;
    usage.tokens_out += reply.usage.outputTokens;
  };
  const fail = (error: unknown, calls: number): HandlerResult => {
    log({
      event: 'speaking_check',
      verdict: 'not_verified',
      media_id: request.mediaId,
      audio_chars: request.audioBase64.length,
      calls,
      ...(calls > 1 ? usage : {}),
      error: error instanceof Error ? error.message : 'model error',
    });
    return { status: 200, body: { kind: 'speaking', verdict: 'not_verified', heard: '', matched: null, closest: null } };
  };

  // Call 1: plain transcription, the sentences unknown to the model
  let first: ModelReply;
  try {
    first = await withTimeout(deps.callModel(speakingModelRequest(request.audioBase64, request.mimeType)), timeout);
  } catch (error) {
    return fail(error, 1);
  }
  count(first);
  const heard = cleanTranscript(first.text);
  let { matched, closest } = heard ? matchSpokenLine(heard, sentences) : { matched: null as string | null, closest: null as string | null };
  let calls = 1;

  // Call 2: only after a miss with something heard; guarded by call 1's words
  if (!matched && heard) {
    calls = 2;
    let second: ModelReply | null = null;
    try {
      second = await withTimeout(
        deps.callModel(speakingContextRequest(request.audioBase64, request.mimeType, sentences)),
        timeout
      );
    } catch {
      second = null; // call 1 still decides: a miss stays a miss
    }
    if (second) {
      count(second);
      const again = cleanTranscript(second.text);
      const candidate = again ? matchSpokenLine(again, sentences).matched : null;
      if (candidate && letterSimilarity(heard, candidate) >= SECOND_LISTEN_MIN_SIMILARITY) {
        matched = candidate;
        closest = candidate;
      }
    }
  }
  const verdict = matched ? 'match' : 'no_match';
  log({
    event: 'speaking_check',
    verdict,
    media_id: request.mediaId,
    audio_chars: request.audioBase64.length,
    model: first.model,
    calls,
    ...usage,
    model_ms: Date.now() - startedAt,
  });
  return { status: 200, body: { kind: 'speaking', verdict, heard, matched, closest, calls } };
}
