// Listening and Speaking exercises – server-side check (English learners only).
// docs/features/reports/LISTENING_SPEAKING_REPORT.md. The flow lives in logic.ts
// (pure, tested); this file only wires the real loaders, the Gemini call and the
// metrics row.
//
// NOT DEPLOYED (brief of 23 Sept 2026: no deploy). Deploy like check-translation:
// verify_jwt OFF (guests carry the publishable key, which is not a JWT), then the
// auth check below. Secrets: GEMINI_API_KEY; optional MODEL_CHECK_LISTENING /
// MODEL_TRANSCRIBE_SPEECH (default gemini-3.1-flash-lite).
//
// Privacy: the recording is only in this request's body. It is passed to one
// Gemini call and dropped with the request – never stored, never logged (the log
// line and the metrics row carry counts and the verdict only).

import { createClient, type SupabaseClient } from 'npm:@supabase/supabase-js@2';
import { corsHeaders, jsonResponse } from '../_shared/cors.ts';
import { recordStep } from '../_shared/aiMetrics.ts';
import { captureEdgeException } from '../_shared/sentry.ts';
import { DEFAULT_MODEL, handleCheck, toListeningQuestion, type ModelRequest } from './logic.ts';
import { geminiModelCaller } from './gemini.ts';

const FUNCTION_NAME = 'check-listen-speak';
const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY') ?? '';

const modelFor = (purpose: ModelRequest['purpose']): string => {
  const name = purpose === 'listening' ? 'MODEL_CHECK_LISTENING' : 'MODEL_TRANSCRIBE_SPEECH';
  return (Deno.env.get(name) ?? '').trim() || DEFAULT_MODEL;
};

declare const EdgeRuntime: { waitUntil(promise: Promise<unknown>): void } | undefined;
const runAfterResponse = (task: Promise<unknown>) => {
  const guarded = task.catch(() => undefined);
  if (typeof EdgeRuntime !== 'undefined' && EdgeRuntime?.waitUntil) EdgeRuntime.waitUntil(guarded);
};

// --- Auth (same rule as check-translation): a user JWT, or a public key as a guest ---
function knownPublicKeys(): Set<string> {
  const keys = new Set<string>();
  const legacy = (Deno.env.get('SUPABASE_ANON_KEY') ?? '').trim();
  if (legacy) keys.add(legacy);
  const raw = Deno.env.get('SUPABASE_PUBLISHABLE_KEYS') ?? '';
  if (raw) {
    try {
      for (const value of Object.values(JSON.parse(raw) as Record<string, unknown>)) {
        if (typeof value === 'string' && value) keys.add(value);
      }
    } catch {
      console.error(JSON.stringify({ event: 'publishable_keys_unparseable', function: FUNCTION_NAME }));
    }
  }
  return keys;
}
const isAcceptedGuestKey = (apiKey: string): boolean => {
  if (!apiKey) return false;
  const known = knownPublicKeys();
  return known.size > 0 ? known.has(apiKey) : apiKey.startsWith('sb_publishable_');
};
const looksLikeJwt = (token: string): boolean => token.split('.').length === 3;

// deno-lint-ignore no-explicit-any
type ServiceClient = SupabaseClient<any, any, any>;

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: corsHeaders });
  if (req.method !== 'POST') return jsonResponse({ error: 'Method not allowed' }, 405);
  try {
    if (!GEMINI_API_KEY) return jsonResponse({ error: 'GEMINI_API_KEY is not configured' }, 500);
    const service: ServiceClient = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
    );
    const bearer = (req.headers.get('Authorization') ?? '').replace(/^Bearer\s+/i, '').trim();
    const apiKey = (req.headers.get('apikey') ?? '').trim();
    if (bearer && looksLikeJwt(bearer)) {
      const {
        data: { user },
      } = await service.auth.getUser(bearer);
      if (!user) return jsonResponse({ error: 'Unauthorized' }, 401);
    } else if (!isAcceptedGuestKey(apiKey || bearer)) {
      return jsonResponse({ error: 'Unauthorized' }, 401);
    }

    const body = await req.json().catch(() => null);
    const result = await handleCheck(body, {
      // The transcript column is never selected: the model must not see it
      loadQuestion: async (id) => {
        const { data, error } = await service
          .from('listening_questions')
          .select('id, question, correct_answer, accepted_answers')
          .eq('id', id)
          .maybeSingle();
        if (error) throw new Error(`question load failed: ${error.message}`);
        return data ? toListeningQuestion(data) : null;
      },
      loadSentences: async (mediaId) => {
        const { data, error } = await service
          .from('media')
          .select('speech_sentences, speaking_eligible')
          .eq('id', mediaId)
          .maybeSingle();
        if (error) throw new Error(`media load failed: ${error.message}`);
        if (!data || data.speaking_eligible !== true) return null;
        return Array.isArray(data.speech_sentences) ? (data.speech_sentences as string[]) : null;
      },
      callModel: geminiModelCaller({ apiKey: GEMINI_API_KEY, model: modelFor }),
      log: (event) => {
        console.log(JSON.stringify(event));
        if (typeof event.tokens_in !== 'number') return;
        runAfterResponse(
          recordStep(service, {
            step: event.event === 'listening_check' ? 'check_listening' : 'check_speaking',
            model: String(event.model ?? ''),
            latencyMs: Number(event.model_ms ?? 0),
            ttftMs: null,
            tokensIn: Number(event.tokens_in ?? 0),
            tokensOut: Number(event.tokens_out ?? 0),
            cachedTokens: 0,
            cacheHit: false,
            extra: { verdict: event.verdict, audio_tokens: event.tokens_audio ?? null },
          })
        );
      },
    });
    return jsonResponse(result.body, result.status);
  } catch (error) {
    captureEdgeException(error, { function: FUNCTION_NAME });
    return jsonResponse({ error: 'Internal error' }, 500);
  }
});
