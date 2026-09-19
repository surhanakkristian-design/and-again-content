# Task C+E (Phase 1O) - rebuild per-item layer records for 1N and 1M with ZERO model calls.
# Sandbox: every write outside phase1o is redirected into phase1o/diag/_redirected, sockets and subprocess are disabled.
import sys, os, json, builtins, socket, time, collections, inspect, traceback, subprocess
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
O = os.path.join(TOFF, 'phase1o'); D = os.path.join(O, 'diag'); RED = os.path.join(D, '_redirected')
os.makedirs(RED, exist_ok=True)
_open = builtins.open
def safe_open(file, mode='r', *a, **k):
    if isinstance(file, (str, bytes, os.PathLike)) and any(c in mode for c in 'wax+'):
        p = os.path.abspath(os.fspath(file))
        if not p.startswith(O + os.sep):
            file = os.path.join(O, 'access_log.jsonl') if p.endswith('access_log.jsonl') else os.path.join(RED, os.path.basename(p))
    return _open(file, mode, *a, **k)
builtins.open = safe_open
import io; io.open = safe_open
def _nonet(*a, **k): raise RuntimeError('network disabled in Task CE')
import ssl, urllib.request, http.client
socket.socket.connect = _nonet; socket.create_connection = _nonet; urllib.request.urlopen = _nonet
def _nosub(*a, **k): raise FileNotFoundError('subprocess disabled in Task CE')
subprocess.run = subprocess.check_output = subprocess.Popen = subprocess.call = _nosub
def mylog(what, n, purpose):
    _open(os.path.join(O, 'access_log.jsonl'), 'a').write(json.dumps({'ts': time.strftime('%Y-%m-%dT%H:%M:%S'), 'side': 'taskCE', 'what': what, 'caller': 'phase1o/diag/ce_build.py', 'n': n, 'purpose': purpose}) + '\n')
def snap():
    s = {}
    for ph in ('phase1n', 'phase1m'):
        for r, d, f in os.walk(os.path.join(TOFF, ph)):
            if '__pycache__' in r: continue
            for x in f:
                p = os.path.join(r, x); s[p] = (os.path.getsize(p), os.path.getmtime(p))
    return s
before = snap()
sys.path.insert(0, os.path.join(TOFF, 'phase1n'))
sys.argv = ['ce_build']
sys.dont_write_bytecode = True
import runner_1n as RN
RL, R1K, LM = RN.RL, RN.R1K, RN.LM
RN.say = lambda *a, **k: None
try: RL.say = lambda *a, **k: None
except Exception: pass
PURPOSE = 'Phase 1O Task C+E diagnosis: per-item layer reconstruction, 0 model calls'

def vm_from(path, variant):
    vm, rows = {}, {}
    for l in _open(path):
        d = json.loads(l)
        if d.get('variant') == variant and d.get('verdict'):
            vm[d['item_id']] = d['verdict']; rows[d['item_id']] = d
    return vm, rows

def do_side(tag):
    if tag == '1n':
        st, recs, ann, by, info = RN.build_side_1n(PURPOSE)
        labels, controls, lmeta = LM.load_labels(PURPOSE, caller='phase1o/diag/ce_build.py')
        vm, rows = vm_from(os.path.join(TOFF, 'phase1n/calls.jsonl'), 'L-1N:main')
        RL.TYPES = RN.TYPES
    else:
        st, recs, ann, by, info = RN.fresh1m_side(PURPOSE)
        labels, controls, lmeta = RN.fresh1m_labels(PURPOSE)
        vm, rows = vm_from(os.path.join(TOFF, 'phase1m/calls.jsonl'), 'L-1M:main')
        RL.TYPES = RN.TYPES_1M
    for r in recs:
        if r['item_id'] in labels: r['judged'], r['wrong_type'] = labels[r['item_id']]
    if tag == '1n':
        RN.select_f8('f8'); g = R1K.guard_readouts(recs, ann, False)
        guards = {i: {'f8': None, 'f9': g[i]['f9']} for i in g}
        res = R1K.configure_row(st, recs, vm, True, guards, False, False, True)
    else:
        RN.select_f8('f8v2'); g = R1K.guard_readouts(recs, ann, False)
        guards = {i: {'f8': g[i]['f8'], 'f9': g[i]['f9']} for i in g}
        res = R1K.configure_row(st, recs, vm, True, guards, True, False, True)
    RL.RES_VM[0] = vm
    m = RL.col_metrics(recs, res, labels)
    print('[%s] coverage %s  fr_by_layer %s  n_fr %d' % (tag, json.dumps(m['coverage']), json.dumps({k: v['k'] for k, v in m['fr_by_layer'].items()}), len(m['fr_ids'])))
    print('[%s] chk dist %s ; sample res: %s' % (tag, info.get('chk_distribution'), repr(res[recs[0]['item_id']])[:300]))
    jpass = (lmeta or {}).get('passive_by_item') or {}
    out = []
    for r in recs:
        i = r['item_id']
        if r['judged'] != 'correct': continue
        mi = RL.col_metrics([r], res, labels)
        acc = mi['coverage']['k'] == 1
        lay = [L for L, v in mi['fr_by_layer'].items() if v['k'] == 1]
        a = ann.get(str(r['sid'])) or {}
        hy = a.get('hygienised', a)
        out.append({'id': i, 'set': tag, 'sid': r['sid'], 'sk': r['sk'], 'level': r['level'], 'topic': r['topic'], 'refs': r['refs'], 'alt': hy.get('alt'), 'locks': r['locks'],
                    'answer': r['answer'], 'kind': r['kind'], 'intent': r['intent'], 'passive_w': r.get('passive'), 'passive_j': jpass.get(i), 'chk_step': r['chk']['step'],
                    'chk_verdict': r['chk']['verdict'], 'lock_ok': r.get('lock_ok'), 'accepted': acc, 'layer': (lay[0] if lay else None), 'verdict': vm.get(i), 'reply': (rows.get(i) or {}).get('reply'),
                    'tense_open': a.get('tense_open'), 'voice_sk': a.get('voice_sk'), 'tf_gold': a.get('tf_gold'), 'tags': r.get('tags'), 'res_raw': repr(res[i])[:400]})
    fr = sorted(x['id'] for x in out if not x['accepted'])
    print('[%s] judged-correct %d accepted %d ; fr ids identical to results file: %s' % (tag, len(out), sum(x['accepted'] for x in out), fr == sorted(m['fr_ids'])))
    wc = [r for r in recs if r['intent'] == 'C']
    print('[%s] writer-C items %d, of them chk match %d ; kind C %d ; judged-correct with chk match %d' % (tag, len(wc), sum(r['chk']['step'] == 'match' for r in wc), sum(r['kind'] == 'C' for r in recs), sum(x['chk_step'] == 'match' for x in out)))
    print('[%s] intents %s' % (tag, dict(collections.Counter(r['intent'] for r in recs))))
    mylog('phase1%s data+annotations+judge labels+calls.jsonl(main)' % tag[1], len(recs), PURPOSE)
    return out, m

allrows = []
for tag in ('1n', '1m'):
    try:
        o, m = do_side(tag); allrows += o
        ref = json.load(_open(os.path.join(TOFF, 'phase1%s/results_1%s.json' % (tag[1], tag[1]))))['metrics']
        print('[%s] stored fr_ids == rebuilt: %s' % (tag, sorted(ref['fr_ids']) == sorted(m['fr_ids'])))
    except Exception:
        traceback.print_exc()
json.dump(allrows, _open(os.path.join(D, 'ce_dump.json'), 'w'), ensure_ascii=False, indent=0)
with _open(os.path.join(D, 'ce_fr_listing.txt'), 'w') as fh:
    for x in allrows:
        if x['accepted']: continue
        refs = ' // '.join(x['refs'][:3])
        fh.write('%s|%s|%s|p=%s/%s|%s|tf=%s,open=%s\nSK: %s\nREF: %s\nANS: %s\nALT: %s LK: %s\n' % (x['id'], x['layer'], x['verdict'], x['passive_w'], x['passive_j'], x['intent'], x['tf_gold'], x['tense_open'], x['sk'], refs, x['answer'], json.dumps(x['alt'], ensure_ascii=False), json.dumps(x['locks'], ensure_ascii=False)))
# ---- F5: locate in code
tot = 0
for name, mod in list(sys.modules.items()):
    f = getattr(mod, '__file__', None) or ''
    if not f.startswith(TOFF): continue
    try: src = inspect.getsource(mod)
    except Exception: continue
    if 'F5' not in src: continue
    print('== module %s (%s) mentions F5 %d times' % (name, os.path.relpath(f, TOFF), src.count('F5')))
    for fn, fo in inspect.getmembers(mod, inspect.isfunction):
        if getattr(fo, '__module__', None) != mod.__name__: continue
        try: s = inspect.getsource(fo)
        except Exception: continue
        if ('F5' in s or 'f5' in fn.lower()) and tot < 7000:
            cut = s if len(s) < 2600 else '\n'.join(l for l in s.split('\n') if 'F5' in l or 'f5' in l or l.startswith('def '))[:1500]
            print('-- %s.%s (%d chars)\n%s' % (name, fn, len(s), cut)); tot += len(cut)
after = snap()
chg = [p for p in set(before) | set(after) if before.get(p) != after.get(p)]
print('files changed under phase1n/phase1m:', chg)
print('redirected writes:', os.listdir(RED))
