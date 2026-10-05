// check-listen-speak – the Gemini REST call for one ModelRequest. Plain fetch,
// no Deno APIs, so the edge function and the local dev server share it.
// The key travels in the x-goog-api-key header (never in the URL, which ends up
// in logs). The audio is only part of the request body of this one call.

import type { ModelReply, ModelRequest, ModelUsage } from './logic.ts';

type FetchLike = (url: string, init: { method: string; headers: Record<string, string>; body: string }) => Promise<{
  ok: boolean;
  status: number;
  json: () => Promise<unknown>;
  text: () => Promise<string>;
}>;

export interface GeminiCallerOptions {
  apiKey: string;
  /** model per purpose; both default to the caller's choice */
  model: (purpose: ModelRequest['purpose']) => string;
  fetchImpl?: FetchLike;
  /** retries on 429/503 (short backoff) */
  retries?: number;
}

/** Gemini "minimal" thinking for Flash-Lite, "low" otherwise (same rule as _shared/models.ts). */
const thinkingLevel = (model: string): string => (model.includes('flash-lite') ? 'minimal' : 'low');

export const geminiRequestBody = (request: ModelRequest, model: string): Record<string, unknown> => ({
  systemInstruction: { parts: [{ text: request.system }] },
  contents: [
    {
      role: 'user',
      parts: request.parts.map((part) =>
        'text' in part ? { text: part.text } : { inline_data: { mime_type: part.audio.mimeType, data: part.audio.base64 } }
      ),
    },
  ],
  generationConfig: {
    temperature: request.temperature,
    maxOutputTokens: request.maxOutputTokens,
    thinkingConfig: { thinkingLevel: thinkingLevel(model) },
  },
});

export const parseGeminiUsage = (data: Record<string, unknown>): ModelUsage => {
  const meta = (data.usageMetadata ?? {}) as Record<string, unknown>;
  const details = Array.isArray(meta.promptTokensDetails) ? (meta.promptTokensDetails as Record<string, unknown>[]) : [];
  const audio = details.find((d) => d.modality === 'AUDIO');
  const thoughts = typeof meta.thoughtsTokenCount === 'number' ? meta.thoughtsTokenCount : 0;
  return {
    inputTokens: typeof meta.promptTokenCount === 'number' ? meta.promptTokenCount : 0,
    // thinking tokens are billed as output
    outputTokens: (typeof meta.candidatesTokenCount === 'number' ? meta.candidatesTokenCount : 0) + thoughts,
    audioTokens: typeof audio?.tokenCount === 'number' ? (audio.tokenCount as number) : 0,
  };
};

const replyText = (data: Record<string, unknown>): string => {
  const candidates = Array.isArray(data.candidates) ? data.candidates : [];
  const first = candidates[0] as { content?: { parts?: { text?: string; thought?: boolean }[] } } | undefined;
  return (first?.content?.parts ?? [])
    .filter((part) => typeof part.text === 'string' && !part.thought)
    .map((part) => part.text)
    .join('');
};

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

export const geminiModelCaller =
  (options: GeminiCallerOptions) =>
  async (request: ModelRequest): Promise<ModelReply> => {
    const model = options.model(request.purpose);
    const doFetch = options.fetchImpl ?? (fetch as unknown as FetchLike);
    const body = JSON.stringify(geminiRequestBody(request, model));
    const retries = options.retries ?? 2;
    for (let attempt = 0; ; attempt++) {
      const res = await doFetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-goog-api-key': options.apiKey },
        body,
      });
      if (res.ok) {
        const data = (await res.json()) as Record<string, unknown>;
        return { text: replyText(data), usage: parseGeminiUsage(data), model };
      }
      // The error body may echo the request; it is read and dropped, never logged
      await res.text().catch(() => '');
      if ((res.status === 429 || res.status === 503) && attempt < retries) {
        await sleep(400 * 2 ** attempt);
        continue;
      }
      throw new Error(`Gemini HTTP ${res.status}`);
    }
  };
