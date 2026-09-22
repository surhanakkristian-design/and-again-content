#!/usr/bin/env python3
"""Record a finished subagent's reported usage for a pending session (decision 26 transport).
    python3 -B rec_tokens.py <lang> <writers|judge> <sid> <subagent_tokens> <tool_uses> <duration_ms>"""
import json, os, sys, time
W1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lang, kind, sid, tok, tu, ms = sys.argv[1:7]
d = os.path.join(W1, lang, 'partD', kind, 'sessions', sid)
assert os.path.exists(os.path.join(d, 'prompt.txt')), d
assert os.path.exists(os.path.join(d, 'reply.txt')), 'no reply.txt in %s' % d
json.dump({'total_tokens': int(tok), 'tool_uses': int(tu), 'secs': round(int(ms) / 1000.0, 1), 'agent': 'opus subagent (tx-opus)',
           'ts': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, open(os.path.join(d, 'tokens.json'), 'w'), indent=1)
print('recorded', lang, kind, sid, tok)
