#!/usr/bin/env python3
"""Phase 2I stage-2 suite: the real run_2i / stack code path with ONLY the Gemini HTTP layer mocked. 0 model calls.
(a) '429' in reply text / jid is not a rate limit   (b) genuine HTTP 429 envelope retried, counted:false
(c) daily-quota / usage-limit envelopes stop cleanly (d) resume after a completed run = 0 calls
(e) TRANSLATION-ONLY reads lk nowhere (poisoned items + static grep + import graph)
(f) TONLY prompt has no 'ALREADY VERIFIED' / 'Practised grammar'; = FROZEN prompt minus exactly that line
(g) FROZEN reproduces the stored 1W verdicts from phase1w/a4/run (all 900, stored L3 replies)
(h) empty 200 -> FAILED, not retried              (i) hard cap and spend cap stop before any call
(k) the 2F adapter is verbatim and reproduces phase2f/p3/probe/data  (w) write guard redirects
(z) no earlier-phase file changed: git status, and sha256 of every file under phase*/ except phase2i (sha_tree.sh)
    identical before/after the suite and equal to SHA_before.txt."""
import ast, hashlib, json, os, re, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
REPO = os.path.dirname(TOFF)
sys.path.insert(0, HERE)
import run_2i as R                                                                   # noqa: E402
SCR = os.environ.get('P2I_TEST_DIR') or os.path.join(tempfile.gettempdir(), 'p2i_test')
OUT, RES = [], []


def log(s):
    print(s, flush=True); OUT.append(str(s))


def check(name, ok, detail=''):
    RES.append((name, bool(ok))); log('%s  %s  %s' % ('PASS' if ok else 'FAIL', name, detail))


def git_dirty():
    p = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=all', '--', 'translation-offline'],
                       cwd=REPO, capture_output=True, text=True)
    return sorted(l for l in p.stdout.splitlines() if 'translation-offline/phase2i/' not in l)


def fsha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def r200(text, tin=180, tout=1):
    return 200, {'candidates': [{'content': {'parts': [{'text': text}]}, 'finishReason': 'STOP'}],
                 'usageMetadata': {'promptTokenCount': tin, 'candidatesTokenCount': tout}}, '{}'


def e429(status='RESOURCE_EXHAUSTED', msg='Resource has been exhausted (e.g. check quota).', details=None):
    js = {'error': {'code': 429, 'status': status, 'message': msg, 'details': details or []}}
    return 429, js, json.dumps(js)


class Mock(object):
    def __init__(self, script=(), default=None):
        self.script, self.default, self.calls = list(script), default, 0

    def __call__(self, url, body, key):
        self.calls += 1
        assert key == 'TESTKEY'
        return self.script.pop(0) if self.script else self.default


def fixture():
    rows = [json.loads(l) for l in open(os.path.join(TOFF, 'phase2d', 'out', 'annotations_sk_final.jsonl'),
                                        encoding='utf-8')]
    items = []
    for row, jid, how in zip([rows[0], rows[1500], rows[3000], rows[4000]], ['j429', 'jx0429', 'jA1429', 'jB'],
                             ['same', 'honest', 'honest', 'same']):
        en = row['en']
        ans = en if how == 'same' else 'Honestly, ' + (en if en[:2] == 'I ' else en[0].lower() + en[1:])
        items.append({'jid': jid, 'sid': int(row['n']), 'level': row['level'], 'slovak': row['src'],
                      'topic': row['type_title'], 'answer': ans, 'annotation': row, 'judged': 'correct',
                      'type': 'LABEL-MUST-NOT-PASS'})
    return items


def fresh(name):
    d = os.path.join(SCR, name); shutil.rmtree(d, ignore_errors=True); os.makedirs(d); return d


def go(d, mock, **kw):
    R.HTTP[0], R.SLEEP[0], R.MIN_INTERVAL = mock, (lambda s: None), 0
    return R.run(SETF, d, key='TESTKEY', purpose='test_2i', **kw)


def keys_deep(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from keys_deep(v)
    elif isinstance(o, list):
        for v in o:
            yield from keys_deep(v)


def sha_tree():
    o = subprocess.run(['zsh', os.path.join(HERE, 'sha_tree.sh')], capture_output=True, text=True, check=True).stdout
    return dict(reversed(l.split('  ', 1)) for l in o.splitlines() if l.strip())


def main():
    global SETF
    os.makedirs(SCR, exist_ok=True)
    tree0 = sha_tree()
    dirty0 = git_dirty()
    pre = {p: fsha(os.path.join(TOFF, p)) for p in ('phase1p/access_log.jsonl', 'phase1p/run_1p.log')}
    items = fixture()
    SETF = os.path.join(SCR, 'set.jsonl')
    with open(SETF, 'w', encoding='utf-8') as fh:
        for it in items:
            fh.write(json.dumps(it, ensure_ascii=False) + '\n')
    n = len(items)

    # (a) + (d)
    d = fresh('a'); m = Mock([r200('Row 429: 429 Too Many Requests RESOURCE_EXHAUSTED')], r200('SAME'))
    st = go(d, m); L = R.jl_read(os.path.join(d, 'ledger.jsonl')); res = R.jl_read(os.path.join(d, 'results.jsonl'))
    check('a.requests_reach_L3', st['requests'] >= 2, 'unique requests %d (both stacks)' % st['requests'])
    check('a.429_text_not_rate_limit', st['status'] == 'COMPLETE' and not [r for r in L if not r['counted']]
          and L[0]['failed'] and L[0]['http'] == 200 and m.calls == st['requests']
          and not [f for f in os.listdir(d) if f.startswith('STOP_')],
          'status %s, calls %d, uncounted %d, first row verdict %s (%s)' % (
              st['status'], m.calls, sum(1 for r in L if not r['counted']), L[0]['verdict'], L[0]['why']))
    check('a.all_results', len(res) == 2 * n and len({(r['jid'], r['stack']) for r in res}) == 2 * n,
          '%d result lines' % len(res))
    tj = json.load(open(os.path.join(d, '_io', 'tonly_prepare_items.json')))
    fj = json.load(open(os.path.join(d, '_io', 'frozen_prepare_items.json')))
    check('a.labels_not_passed', not any(k in ('judged', 'type') for it in tj + fj for k in it))
    check('e.runner_strips_lk_for_tonly', not [k for k in keys_deep(tj) if k == 'lk' or str(k).startswith('lk_')]
          and any('lk' in it['annotation'] for it in fj))
    h0 = (fsha(os.path.join(d, 'ledger.jsonl')), fsha(os.path.join(d, 'results.jsonl')))
    m2 = Mock([], r200('SAME')); st2 = go(d, m2)
    check('d.resume_zero_calls', m2.calls == 0 and st2['status'] == 'COMPLETE' and
          (fsha(os.path.join(d, 'ledger.jsonl')), fsha(os.path.join(d, 'results.jsonl'))) == h0,
          'calls %d, ledger/results unchanged %s' % (m2.calls, (fsha(os.path.join(d, 'ledger.jsonl')),
                                                               fsha(os.path.join(d, 'results.jsonl'))) == h0))
    by = {(r['jid'], r['stack']): r for r in res}
    log('   a.verdicts: ' + json.dumps({'%s/%s' % k: [v['layer'], v['accept'], v['l3_reply']] for k, v in
                                        sorted(by.items())}, ensure_ascii=False))

    # (b)
    d = fresh('b'); m = Mock([e429()], r200('SAME')); st = go(d, m); L = R.jl_read(os.path.join(d, 'ledger.jsonl'))
    unc = [r for r in L if not r['counted']]
    check('b.real_429_retried', st['status'] == 'COMPLETE' and len(unc) == 1 and unc[0]['http'] == 429
          and unc[0]['kind'] == 'retry' and L[1]['req_key'] == unc[0]['req_key'] and L[1]['http'] == 200
          and m.calls == st['requests'] + 1 and st['counted_total'] == st['requests'],
          'uncounted rows %d, calls %d, counted %d' % (len(unc), m.calls, st['counted_total']))

    # (c) quota envelopes
    for tag, resp in (('perday', e429(details=[{'@type': 'type.googleapis.com/google.rpc.QuotaFailure',
                                                'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/'
                                                                'generate_content_free_tier_requests',
                                                                'quotaId': 'GenerateRequestsPerDayPerProjectPer'
                                                                           'Model-FreeTier'}]}])),
                      ('usage_limit', e429(msg='Your project has exceeded its monthly spending cap.'))):
        d = fresh('c_' + tag); m = Mock([], resp); st = go(d, m)
        L = R.jl_read(os.path.join(d, 'ledger.jsonl')); res = R.jl_read(os.path.join(d, 'results.jsonl'))
        check('c.quota_stop_' + tag, st['status'] == 'STOPPED' and (st['stop'] or {}).get('kind') == 'quota'
              and m.calls == 1 and len(L) == 1 and not L[0]['counted'] and st['counted_total'] == 0
              and os.path.exists(os.path.join(d, 'STOP_quota.md')) and all(r['l3_calls'] == 0 for r in res),
              'status %s, calls %d, results written %d (all without L3)' % (st['status'], m.calls, len(res)))
    m = Mock([], r200('SAME')); st = go(d, m)
    check('c.resume_after_quota', st['status'] == 'COMPLETE' and m.calls == st['requests']
          and len(R.jl_read(os.path.join(d, 'results.jsonl'))) == 2 * n, 'calls %d' % m.calls)

    # (h)
    d = fresh('h'); m = Mock([], r200('')); st = go(d, m)
    L = R.jl_read(os.path.join(d, 'ledger.jsonl')); res = R.jl_read(os.path.join(d, 'results.jsonl'))
    l3 = [r for r in res if r['l3_calls']]
    check('h.empty_200_failed_not_retried', st['status'] == 'COMPLETE' and m.calls == st['requests']
          and all(r['counted'] and r['failed'] and r['verdict'] == 'FAILED' for r in L)
          and l3 and all(r['call_failed'] and not r['accept'] for r in l3),
          'calls %d = requests %d; failed items %d all rejected' % (m.calls, st['requests'], len(l3)))
    m = Mock([], r200('SAME')); st = go(d, m)
    check('h.failed_not_retried_on_resume', m.calls == 0, 'calls %d' % m.calls)

    # (i)
    d = fresh('i'); m = Mock([], r200('SAME')); st = go(d, m, cap=1)
    check('i.hard_cap', st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and m.calls == 0
          and os.path.exists(os.path.join(d, 'STOP_cap.md')), st['stop']['why'] if st['stop'] else '')
    d = fresh('i2'); m = Mock([], r200('SAME')); st = go(d, m, spend_cap=0.0)
    check('i.spend_cap', st['status'] == 'STOPPED' and st['stop']['kind'] == 'spend' and m.calls == 0)
    d = fresh('i3'); m = Mock([], r200('SAME')); R.HTTP[0], R.SLEEP[0] = m, (lambda s: None)
    P = R.paths(d); ctx = {'P': P, 'cap': 1, 'spend_cap': 1.0, 'key': 'TESTKEY', 'last': 0.0, 'made': 0,
                           'uncounted': 0, 'counted': 1, 'spent': 0.0, 'est': 0.0005}
    try:
        R.call_one(ctx, 'k', {'sys': 's', 'user': 'u', 'gcfg': {}}, ['x']); ok = False
    except R.Stop as e:
        ok = e.kind == 'cap'
    check('i.per_call_cap_guard', ok and m.calls == 0)

    # (e) poisoned TRANSLATION-ONLY + import graph, (f) prompts
    d = fresh('e'); fi = os.path.join(d, 'items.json'); fo = os.path.join(d, 'out.json')
    json.dump([R.clean_item(it, 'frozen') for it in items], open(fi, 'w'), ensure_ascii=False)
    child = r'''
import json, os, sys
os.environ["TONLY_POISON"] = "1"
sys.path.insert(0, %r)
import stack_tonly as T
items = json.load(open(%r))
for it in items:
    it["annotation"] = dict(it["annotation"], lk=T.PoisonVal(), lk_reason=T.PoisonVal())
    it["annotation"]["hygienised"] = {"lk": T.PoisonVal()}
err = None
try:
    q = T.E.prepare_2i(items)
    res = T.E.finish_2i(items, {j: "SAME" for j in q}, [])
except BaseException as e:
    err = repr(e); q, res = {}, {}
json.dump({"hits": T.HITS, "err": err, "q": q, "n_res": len(res), "modules": T.E.loaded_files(),
           "row7": dict(sys.modules["pipeline_1i"].ROW7_FLAGS)}, open(%r, "w"), ensure_ascii=False)
''' % (HERE, fi, fo)
    p = subprocess.run([sys.executable, '-B', '-c', child], capture_output=True, text=True, cwd=HERE,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=d))
    o = json.load(open(fo)) if os.path.exists(fo) else {'err': p.stderr[-2000:], 'hits': ['no output']}
    check('e.poisoned_items_never_read', not o['hits'] and not o['err'] and o['n_res'] == n and o['q'],
          'hits %s err %s results %s requests %d' % (o['hits'][:3], o['err'], o.get('n_res'), len(o.get('q') or {})))
    mods = [os.path.relpath(x, TOFF) for x in o.get('modules', [])]
    origs = [x for x in mods if x in ('phase1i/lib_prev.py', 'phase1i/pipeline_1i.py', 'phase1p/runner_1p.py')]
    copies = [x for x in mods if x.startswith('phase2i/tonly/')]
    check('e.import_graph_uses_copies_only', not origs and len(copies) == 3, 'copies %s, originals %s' % (copies, origs))
    check('e.F2B_off_rest_unchanged', o.get('row7') == {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 0},
          str(o.get('row7')))
    fn = {'lib_prev.py': ('route', 'prompt'), 'pipeline_1i.py': ('to_item',),
          'runner_1p.py': ('build_side', 'decide', 'l3_eligible')}
    bad, elsewhere = [], {}
    for f, names in fn.items():
        src = open(os.path.join(HERE, 'tonly', f), encoding='utf-8').read()
        for node in ast.parse(src).body:
            if isinstance(node, ast.FunctionDef) and node.name in names:
                seg = ast.get_source_segment(src, node)
                if re.search(r"\blk\b|locks|lock_ok|guard_readouts|ALREADY VERIFIED|Practised grammar", seg):
                    bad.append('%s:%s' % (f, node.name))
        elsewhere[f] = len(re.findall(r"\['lk'\]|'locks'|\['lock_ok'\]", src))
    check('e.static_grep_verdict_path', not bad, 'hits in edited functions: %s; remaining textual hits in '
          'functions off the 2I path (other phases\' builders/fixtures): %s' % (bad, elsewhere))
    fr = R.stack_call('frozen', 'prepare', json.load(open(fi)), R.paths(d))
    tq = o.get('q') or {}
    common = sorted(set(fr) & set(tq))
    bad_f, bad_eq = [], []
    for j in common:
        a, b = fr[j]['user'].split('\n'), tq[j]['user'].split('\n')
        if 'ALREADY VERIFIED' in tq[j]['user'] or 'Practised grammar' in tq[j]['user'] or \
                'Practised grammar' in tq[j]['sys']:
            bad_f.append(j)
        diff = [x for x in a if x not in b]
        if not (len(a) == len(b) + 1 and len(diff) == 1 and diff[0].startswith('Practised grammar: ')
                and 'ALREADY VERIFIED' in diff[0] and [x for x in a if x != diff[0]] == b
                and fr[j]['sys'] == tq[j]['sys'] and fr[j]['gcfg'] == tq[j]['gcfg']):
            bad_eq.append(j)
    check('f.no_practised_grammar_line', common and not bad_f, '%d common prompts checked' % len(common))
    check('f.tonly_equals_frozen_minus_that_line', common and not bad_eq, 'mismatch %s' % bad_eq)
    if common:
        log('   f.removed line example: %r' % [x for x in fr[common[0]]['user'].split('\n')
                                               if x.startswith('Practised')][0])
    fm = os.path.join(d, 'mods_frozen.json'); tm = os.path.join(d, 'mods_tonly.json')
    for s, f in (('frozen', fm), ('tonly', tm)):
        subprocess.run([sys.executable, '-B', R.STACK_FILE[s], 'modules', f], cwd=HERE, check=True,
                       capture_output=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=d))
    graph = {'frozen': [os.path.relpath(x, TOFF) for x in json.load(open(fm))],
             'tonly': [os.path.relpath(x, TOFF) for x in json.load(open(tm))]}
    json.dump(graph, open(os.path.join(HERE, 'IMPORT_GRAPH.json'), 'w'), indent=1)
    check('e.import_graph_tonly_static', not [x for x in graph['tonly'] if x in (
        'phase1i/lib_prev.py', 'phase1i/pipeline_1i.py', 'phase1p/runner_1p.py')],
          'frozen %d modules, tonly %d modules' % (len(graph['frozen']), len(graph['tonly'])))

    # (g) FROZEN reproduces 1W
    d = fresh('g'); go_ = os.path.join(d, 'native.json')
    p = subprocess.run([sys.executable, '-B', R.STACK_FILE['frozen'], 'native', os.path.join(TOFF, 'phase1w', 'a4', 'data'),
                        os.path.join(TOFF, 'phase1w', 'a4', 'run', 'verdicts_1u.json'), go_], cwd=HERE,
                       capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=d))
    if p.returncode:
        check('g.frozen_reproduces_1W', False, p.stderr[-1500:])
    else:
        nat = json.load(open(go_))
        rows = {r['item_id']: r for r in json.load(open(os.path.join(TOFF, 'phase1w', 'a4', 'run', 'results_1u.json')))['rows']}
        mis = [(i, rows[i]['final_accept'], rows[i]['final_layer'], nat[i]['accept'], nat[i]['layer'])
               for i in rows if (rows[i]['final_accept'], rows[i]['final_layer']) != (nat[i]['accept'], nat[i]['layer'])]
        hm = [i for i in rows if (rows[i]['layers'] or {}).get('req_hash') != nat[i]['req_hash']]
        check('g.frozen_reproduces_1W', len(nat) == len(rows) == 900 and not mis,
              '%d/%d verdicts+layers identical; mismatches %s' % (len(rows) - len(mis), len(rows), mis[:5]))
        check('g.frozen_prompts_byte_identical_to_1W', not hm, '%d/900 request hashes identical' % (900 - len(hm)))

    # (k) 2F adapter: verbatim + reproduces the probe data
    import adapter_2f as A2F
    psrc = open(os.path.join(TOFF, 'phase2f', 'p3', 'probe', 'p3_probe.py'), encoding='utf-8').read()
    asrc = open(os.path.join(HERE, 'adapter_2f.py'), encoding='utf-8').read()
    segs = {n.name: ast.get_source_segment(psrc, n) for n in ast.parse(psrc).body
            if isinstance(n, ast.FunctionDef) and n.name in ('jdump', 'alt_dict', 'build_data')}
    check('k.adapter_verbatim', len(segs) == 3 and all(v in asrc for v in segs.values())
          and 'SID_LO, SID_HI = 220001, 220060' in psrc, 'functions %s' % sorted(segs))
    sel = json.load(open(os.path.join(TOFF, 'phase2f', 'p3', 'probe', 'set', 'selection.json'), encoding='utf-8'))
    prod = {}
    for l in open(os.path.join(TOFF, 'phase2d', 'out', 'annotations_sk_final.jsonl'), encoding='utf-8'):
        if l.strip():
            r = json.loads(l); prod.setdefault(r['exercise_id'], r)
    rows = [{'sid': r['sid'], 'exercise_id': r['exercise_id'], 'level': r['level'], 'topic': r['topic'],
             'slovak': r['slovak'], 'ann': prod[r['exercise_id']]} for r in sel['rows']]
    d = fresh('k'); A2F.convert(rows, d)
    PD = os.path.join(TOFF, 'phase2f', 'p3', 'probe', 'data')
    for f in ('annotations.json', 'sentences.json'):
        ref, new = json.load(open(os.path.join(PD, f), encoding='utf-8')), json.load(open(os.path.join(d, f), encoding='utf-8'))
        if isinstance(ref, dict):
            nm = sum(1 for k in ref if new.get(k) == ref[k]); nt = len(ref); nf = sum(1 for k in ref for x in ref[k] if (new.get(k) or {}).get(x) == ref[k][x])
        else:
            nm = sum(1 for a, b in zip(ref, new) if a == b); nt = len(ref); nf = sum(1 for a, b in zip(ref, new) for x in a if b.get(x) == a[x])
        same = fsha(os.path.join(PD, f)) == fsha(os.path.join(d, f))
        check('k.adapter_reproduces_probe_' + f, same and nm == nt == 60 and len(new) == 60,
              'byte-identical %s; sids field-for-field equal %d/%d; top-level fields equal %d' % (same, nm, nt, nf))

    # (w) write guard
    d = fresh('w'); probe = os.path.join(TOFF, 'phase1p', 'zz_2i_guard_probe.txt')
    pw = os.path.join(TOFF, 'phase1w', 'a4', 'run', 'zz_2i_probe.json')
    child = r'''
import os, sys
sys.path.insert(0, %r)
import write_guard
with open(%r, 'a') as fh:
    fh.write('x')
open(%r + '.tmp', 'w').write('{}')
os.replace(%r + '.tmp', %r)
print(open(%r).read())
''' % (HERE, probe, pw, pw, pw, pw)
    p = subprocess.run([sys.executable, '-B', '-c', child], capture_output=True, text=True, cwd=HERE,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=d))
    red = R.jl_read(os.path.join(d, '_redirected', 'REDIRECTS.jsonl'))
    check('w.write_guard_redirects', p.returncode == 0 and p.stdout.strip() == '{}' and not os.path.exists(probe)
          and not os.path.exists(pw) and not os.path.exists(pw + '.tmp')
          and os.path.exists(os.path.join(d, '_redirected', os.path.relpath(probe, REPO)))
          and os.path.exists(os.path.join(d, '_redirected', os.path.relpath(pw, REPO))) and len(red) >= 3,
          'rc %d, redirects %d, stderr %s' % (p.returncode, len(red), p.stderr[-300:]))
    chain_red = []
    for root, _ds, fs in os.walk(SCR):
        if 'REDIRECTS.jsonl' in fs and os.sep + 'w' + os.sep not in root + os.sep:
            chain_red += [x['from'] for x in R.jl_read(os.path.join(root, 'REDIRECTS.jsonl'))]
    log('   w.writes the 1W chain attempted outside phase2i during this suite (all redirected): %d %s'
        % (len(chain_red), sorted(set(chain_red))[:10]))

    # (z)
    post = {p: fsha(os.path.join(TOFF, p)) for p in pre}
    check('z.earlier_phases_untouched', git_dirty() == dirty0 and post == pre, 'dirty outside phase2i: %s' % git_dirty())
    tree1 = sha_tree()
    diff = sorted(k for k in set(tree0) | set(tree1) if tree0.get(k) != tree1.get(k))
    check('z.sha_tree_unchanged_by_suite', not diff and len(tree1) > 3000, '%d files, changed %s' % (len(tree1), diff[:5]))
    base = dict(reversed(l.split('  ', 1)) for l in open(os.path.join(HERE, 'SHA_before.txt'), encoding='utf-8').read().splitlines()
                if l.strip())
    diffb = sorted(k for k in set(base) | set(tree1) if base.get(k) != tree1.get(k))
    check('z.sha_tree_equals_SHA_before', not diffb, '%d files vs SHA_before %d; differ %s' % (len(tree1), len(base), diffb[:5]))
    check('z.phase1p_dirty_pair_as_in_SHA_before', all(tree1.get(k) == base.get(k) is not None for k in
          ('phase1p/access_log.jsonl', 'phase1p/run_1p.log')))
    nf = sum(1 for _n, ok in RES if not ok)
    log('SUMMARY: %d checks, %d FAIL, 0 real model calls (HTTP layer mocked)' % (len(RES), nf))
    return nf


if __name__ == '__main__':
    try:
        rc = main()
    except BaseException as e:
        import traceback
        log('CRASH: ' + traceback.format_exc()); rc = 99
    open(os.path.join(HERE, 'test_2i_output.txt'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
    sys.exit(1 if rc else 0)
