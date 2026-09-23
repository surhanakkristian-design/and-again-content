// Diagnostic (NOT a measurement): runs the DEPLOYED wave-1 ua stack (and-again supabase/functions/check-translation/
// sourceOnly/wave1.ts, unchanged) offline on items from an input jsonl {id, src, answer}.
// Gemini key read from ~/Projects/and-again/.env.local, never printed. Hard cap on calls via CALL_CAP (env).
// Every model call (request user text, reply text) is appended verbatim to calls.jsonl.
import { readFileSync, appendFileSync, existsSync } from 'node:fs';
import { homedir } from 'node:os';
import { runWave1Stack } from '../../../and-again/supabase/functions/check-translation/sourceOnly/wave1.ts';
import { geminiTransport } from '../../../and-again/supabase/functions/check-translation/sourceOnly/transport.ts';
import type { ModelRequest } from '../../../and-again/supabase/functions/check-translation/sourceOnly/replies.ts';

const [inFile, outFile] = process.argv.slice(2);
const cap = Number(process.env.CALL_CAP ?? '0');
const env = readFileSync(homedir() + '/Projects/and-again/.env.local', 'utf8');
const key = (env.split('\n').find((l) => l.startsWith('GEMINI_API_KEY=')) ?? '').split('=').slice(1).join('=').trim().replace(/^["']|["']$/g, '');
if (!key) throw new Error('no GEMINI_API_KEY');
const ledger = new URL('./calls.jsonl', import.meta.url).pathname;
const used = existsSync(ledger) ? readFileSync(ledger, 'utf8').split('\n').filter(Boolean).length : 0;
let made = used;
const real = geminiTransport({ apiKey: key, timeoutMs: 30000 });
const callModel = async (req: ModelRequest) => {
  if (made + 1 > cap) throw new Error(`CALL_CAP ${cap} reached (made ${made})`);
  made++;
  const r = await real(req);
  appendFileSync(ledger, JSON.stringify({ ts: new Date().toISOString(), system_head: req.system.slice(0, 60), user: req.user,
    ok: r.ok, text: r.ok ? r.text : null, kind: r.ok ? null : r.kind, tin: r.ok ? r.tokensIn : 0, tout: r.ok ? r.tokensOut : 0 }) + '\n');
  return r;
};
const done = new Set(existsSync(outFile) ? readFileSync(outFile, 'utf8').split('\n').filter(Boolean).map((l) => JSON.parse(l).id) : []);
for (const line of readFileSync(inFile, 'utf8').split('\n').filter(Boolean)) {
  const it = JSON.parse(line);
  if (done.has(it.id)) continue;
  const r = await runWave1Stack({ lang: 'ua', sentence: it.src, answer: it.answer }, callModel);
  const row = { id: it.id, src: it.src, answer: it.answer, accept: r.accept, layer: r.layer,
    l3_raw: r.calls[0]?.ok ? (r.calls[0] as any).text : null, l3: r.l3?.verdict ?? null,
    cc_raw: r.calls[1]?.ok ? (r.calls[1] as any).text : null, cc: r.cc?.verdict ?? null, calls: r.calls.length };
  appendFileSync(outFile, JSON.stringify(row) + '\n');
  console.log(it.id, r.accept ? 'ACCEPT' : 'REJECT', r.layer);
}
console.log('calls ledger total', made);
