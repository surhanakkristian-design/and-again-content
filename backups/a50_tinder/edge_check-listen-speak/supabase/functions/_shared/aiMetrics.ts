/** Per-call Add-flow metrics. Always printed as JSON; also stored when the table exists. */

import type { SupabaseClient } from 'npm:@supabase/supabase-js@2';

export type AiStep =
  | 'analyze'
  | 'keywords'
  | 'generate'
  | 'translate'
  | 'spell'
  // Brief 15: notebook scan (handwriting read) and the catalogue match
  | 'scan'
  | 'scan_match'
  // Brief 19: sentence chunking for the build-the-sentence exercise
  | 'chunk'
  // "Translate the sentence" format: one row per real model call (check-translation)
  | 'check_translation'
  // Listening / Speaking exercises (check-listen-speak): SAME/DIFF call, transcription call
  | 'check_listening'
  | 'check_speaking';

export interface StepMetrics {
  step: AiStep;
  model: string;
  latencyMs: number;
  ttftMs: number | null;
  tokensIn: number;
  tokensOut: number;
  cachedTokens: number;
  cacheHit: boolean;
  validatorFirst?: string | null;
  exerciseType?: string | null;
  level?: string | null;
  extra?: Record<string, unknown>;
}

export function logStep(metrics: StepMetrics): void {
  console.log(
    JSON.stringify({
      event: 'ai_step',
      step: metrics.step,
      model: metrics.model,
      latency_ms: metrics.latencyMs,
      ttft_ms: metrics.ttftMs,
      tokens_in: metrics.tokensIn,
      tokens_out: metrics.tokensOut,
      cached_tokens: metrics.cachedTokens,
      cache_hit: metrics.cacheHit,
      cache_hit_share:
        metrics.tokensIn > 0
          ? Number((metrics.cachedTokens / metrics.tokensIn).toFixed(3))
          : 0,
      validator_first: metrics.validatorFirst ?? null,
      type: metrics.exerciseType ?? null,
      level: metrics.level ?? null,
      extra: metrics.extra ?? undefined,
    })
  );
}

export async function recordStep(
  service: SupabaseClient | null,
  metrics: StepMetrics
): Promise<void> {
  logStep(metrics);
  if (!service) return;
  const { error } = await service.from('ai_call_metrics').insert({
    step: metrics.step,
    model: metrics.model,
    latency_ms: Math.round(metrics.latencyMs),
    ttft_ms: metrics.ttftMs == null ? null : Math.round(metrics.ttftMs),
    tokens_in: metrics.tokensIn,
    tokens_out: metrics.tokensOut,
    cached_tokens: metrics.cachedTokens,
    cache_hit: metrics.cacheHit,
    validator_first: metrics.validatorFirst ?? null,
    exercise_type: metrics.exerciseType ?? null,
    level: metrics.level ?? null,
    extra: metrics.extra ?? {},
  });
  if (error) {
    console.error('ai_call_metrics insert failed', error.message);
  }
}

export interface TokenUsage {
  inputTokens: number;
  outputTokens: number;
  cachedTokens: number;
  /** usageMetadata.thoughtsTokenCount when the response reports it (additive, optional). */
  thinkingTokens?: number;
}

export function emptyUsage(): TokenUsage {
  return { inputTokens: 0, outputTokens: 0, cachedTokens: 0 };
}
