// check-lab-answer (A65, /lab only) – the lab's written / spoken answers of exercises 3-5. The flow lives in logic.ts
// (pure, tested); this file wires the auth, the daily counter, the Gemini call (the check-comment caller, the same key)
// and the log table `lab_answer_checks` (migration 20261008100000; service role only, every call with its tokens).
//
// Deploy (verify_jwt OFF: lab guests carry the publishable key, then the auth check below):
//   supabase functions deploy check-lab-answer --project-ref abyrutykpvmzkfbesire --no-verify-jwt --use-api
// Secrets: GEMINI_API_KEY (shared); optional MODEL_CHECK_LAB (default gemini-3.1-flash-lite), LAB_CHECK_DAILY_LIMIT
// (default 200).

import { createClient, type SupabaseClient } from 'npm:@supabase/supabase-js@2';
import { corsHeaders, jsonResponse } from '../_shared/cors.ts';
import { captureEdgeException } from '../_shared/sentry.ts';
import { geminiModelCaller } from '../check-comment/gemini.ts';
import { DEFAULT_DAILY_LIMIT, DEFAULT_MODEL, handleFillAll, handleLabCheck } from './logic.ts';

const FUNCTION_NAME = 'check-lab-answer';
const GEMINI_API_KEY = Deno.env.get('GEMINI_API_KEY') ?? '';
const MODEL = (Deno.env.get('MODEL_CHECK_LAB') ?? '').trim() || DEFAULT_MODEL;
const DAILY_LIMIT = Number(Deno.env.get('LAB_CHECK_DAILY_LIMIT') ?? '') || DEFAULT_DAILY_LIMIT;

function knownPublicKeys(): Set<string> {
  const keys = new Set<string>();
  const legacy = (Deno.env.get('SUPABASE_ANON_KEY') ?? '').trim();
  if (legacy) keys.add(legacy);
  const raw = Deno.env.get('SUPABASE_PUBLISHABLE_KEYS') ?? '';
  if (raw) {
    try {
      for (const value of Object.values(JSON.parse(raw) as Record<string, unknown>)) if (typeof value === 'string' && value) keys.add(value);
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

const sha = async (value: string): Promise<string> => {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value));
  return Array.from(new Uint8Array(digest).slice(0, 12), (b) => b.toString(16).padStart(2, '0')).join('');
};

// deno-lint-ignore no-explicit-any
type ServiceClient = SupabaseClient<any, any, any>;

const gemini = geminiModelCaller({ apiKey: GEMINI_API_KEY, model: () => MODEL, retries: 1 });

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: corsHeaders });
  if (req.method !== 'POST') return jsonResponse({ error: 'Method not allowed' }, 405);
  try {
    if (!GEMINI_API_KEY) return jsonResponse({ error: 'GEMINI_API_KEY is not configured' }, 500);
    const service: ServiceClient = createClient(Deno.env.get('SUPABASE_URL') ?? '', Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '');
    const bearer = (req.headers.get('Authorization') ?? '').replace(/^Bearer\s+/i, '').trim();
    const apiKey = (req.headers.get('apikey') ?? '').trim();
    let userId: string | null = null;
    if (bearer && looksLikeJwt(bearer)) {
      const {
        data: { user },
      } = await service.auth.getUser(bearer);
      if (user) userId = user.id;
      else if (!isAcceptedGuestKey(apiKey)) return jsonResponse({ error: 'Unauthorized' }, 401);
    } else if (!isAcceptedGuestKey(apiKey || bearer)) {
      return jsonResponse({ error: 'Unauthorized' }, 401);
    }
    const body = await req.json().catch(() => null);
    const deviceId = body && typeof body.device_id === 'string' && /^[A-Za-z0-9-]{8,64}$/.test(body.device_id) ? body.device_id : null;
    const ip = (req.headers.get('x-forwarded-for') ?? '').split(',')[0].trim();
    const who = userId ? `user:${userId}` : deviceId ? `device:${deviceId}` : `ip:${await sha(ip || 'unknown')}`;
    // A67: exercise 4 checks all its boxes in one request
    const handle = body && body.exercise === 'fill_all' ? handleFillAll : handleLabCheck;
    const result = await handle(body, {
      who,
      dailyLimit: DAILY_LIMIT,
      countToday: async (key) => {
        const since = new Date();
        since.setUTCHours(0, 0, 0, 0);
        const { count, error } = await service
          .from('lab_answer_checks')
          .select('id', { count: 'exact', head: true })
          .eq('who', key)
          .eq('source', 'gemini')
          .gte('created_at', since.toISOString());
        if (error) throw new Error(`count failed: ${error.message}`);
        return count ?? 0;
      },
      callModel: gemini,
      log: async (row) => {
        console.log(JSON.stringify({ event: 'lab_check', exercise: row.exercise, media_id: row.media_id, verdict: row.verdict, source: row.source, fallback: row.fallback, model: row.model, tokens_in: row.tokens_in, tokens_out: row.tokens_out, latency_ms: row.latency_ms }));
        const { error } = await service.from('lab_answer_checks').insert(row);
        if (error) console.error(JSON.stringify({ event: 'lab_check_store_failed', message: error.message }));
      },
    });
    return jsonResponse(result.body, result.status);
  } catch (error) {
    captureEdgeException(error, { function: FUNCTION_NAME });
    return jsonResponse({ error: 'Internal error' }, 500);
  }
});
