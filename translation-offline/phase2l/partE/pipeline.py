#!/usr/bin/env python3
"""Phase 2L S3 / Part E: measure the FROZEN Czech SOURCE-ONLY + B checker (stack_2l_cz.py) ONCE on a fresh production set.
Mirror of 2J Part D (phase2j/partD/make_set.py, run_writers.py, judge/make_packets.py, run_judges.py, analyze.py,
s8_chain.sh, s8_post.py), Czech version.  Subcommands (each its own process; chain.sh runs them in order):
  projection   token projection from phase2j/TOKENS.jsonl -> phase2l/TOKENS.md (STOP_E_budget.md if > 1,400,000)
  make_set     100 Czech sentences (25/level) from phase2h/out/annotations_cz_final.jsonl, seeded, exclusion proof
  mock         the whole headless path (writers -> packets -> judges -> labels -> items) with a scripted spawner, into partE/_mock
  writers      4 blind writer sessions (phase2k/spec/writer_template_cz.txt; they see wid / czech / level / topic only)
  packets      4 judge packets (jid / czech / level / answer / topic), 80 hidden duplicates in different sessions
  judges       4 judge sessions, ONE prompt (phase2k/spec/judge_prompt_cz.txt minus 2K defect 3's older line), cap 400,000 each
  labels       judge labels (originals) + duplicate-control agreement
  build_items  stack items WITHOUT any label or reference field (+ truth.jsonl kept apart) + poison check
  gemini       opens partE/set/items.jsonl ONCE via open_set and runs stack_2l_cz.run  (Gemini: counted = HTTP 200 only)
  post         FINAL_RUN_DONE, ACCESS_LOG_VERBATIM.md, analysis (CP 95 %), 0 calls
Headless spawner = phase2j/run_2j.run_session (2J/2K recipe: bundled binary, token via `zsh -ic`, never printed;
usage-limit envelope -> hard stop; rate limit only from the envelope; finished sessions resume at 0 cost)."""
import argparse, glob, hashlib, json, math, os, random, re, sys, threading, time, types
from collections import Counter, defaultdict
sys.dont_write_bytecode = True
ROOT = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline'
P2L = ROOT + '/phase2l'
E = P2L + '/partE'
P2J = ROOT + '/phase2j'
ANN = ROOT + '/phase2h/out/annotations_cz_final.jsonl'
WT = ROOT + '/phase2k/spec/writer_template_cz.txt'
JP = ROOT + '/phase2k/spec/judge_prompt_cz.txt'
DROP_OLD = '- A dropped function word is correct, a dropped content word is wrong, added content is wrong.\n'
DROP_NEW = '- Added content is wrong.\n'
SEED, JSEED = 20260926, 20260927
LEVELS = ['A1', 'A2', 'B1', 'B2']
TYPES = ['T', 'W', 'M', 'S']
SHIFT = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 1}
BUDGET = 1400000
OWN_EST = 200000
HEADLESS_CAP = BUDGET - OWN_EST
JUDGE_CAP = 400000
REFK = ('en', 'v', 'alt', 'lk')
FORBID = set(REFK) | {'judge_label', 'judge_reason', 'judge_session', 'writer_intent', 'writer_type', 'writer_agent_drop',
                      'label', 'reference', 'references'}


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


def wjl(p, rows):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    open(p + '.sha256', 'w').write('%s  %s\n' % (h, os.path.basename(p)))
    return h


def wj(p, o):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(o, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)


def is_ref(k):
    return k in REFK or str(k).startswith('lk_')


def strip_refs(o):
    if isinstance(o, dict):
        return {k: strip_refs(v) for k, v in o.items() if not is_ref(k)}
    if isinstance(o, list):
        return [strip_refs(v) for v in o]
    return o


def all_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from all_keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from all_keys(v)


def cdf(k, n, p):
    if p <= 0: return 1.0
    if p >= 1: return 0.0 if k < n else 1.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def cp(x, n, a=0.05):
    if n == 0: return [None, None]
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            m = (lo + hi) / 2
            if f(m): hi = m
            else: lo = m
        return (lo + hi) / 2
    lo = 0.0 if x == 0 else bis(lambda p: 1 - cdf(x - 1, n, p) >= a / 2)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, n, p) <= a / 2)
    return [round(100 * lo, 2), round(100 * hi, 2)]


def rate(x, n):
    return {'x': x, 'n': n, 'pct': round(100 * x / n, 2) if n else None, 'cp95': cp(x, n)}


def tokens_md(line):
    with open(P2L + '/TOKENS.md', 'a', encoding='utf-8') as f:
        f.write(line.rstrip('\n') + '\n')


# ------------------------------------------------------------------ projection
def cmd_projection(a):
    rows = jl(P2J + '/TOKENS.jsonl')
    by = {r['stage']: r for r in rows}
    w, j = int(by['S6']['headless_tokens']), int(by['S7']['headless_tokens'])
    jsum = json.load(open(P2J + '/partD/judge/JUDGES_SUMMARY.json'))
    jmax = max(int(v.get('tokens_new') or 0) for v in jsum['sessions'].values())
    proj_w, proj_j, retry = int(w * 1.15), int(j * 1.15), int(jmax * 1.15)
    total = proj_w + proj_j + retry + OWN_EST
    ok = total <= BUDGET
    txt = ['# Phase 2L S3 (Part E) Claude token budget', '',
           'Budget for this stage: %s tokens incl. every headless session and the S3 agent.' % format(BUDGET, ','), '',
           '## Projection (from phase2j/TOKENS.jsonl, the 2J Part D writer + judge sessions)', '',
           '| item | 2J actual | projection (x1.15) |', '|---|---:|---:|',
           '| 4 blind writers (S6) | %s | %s |' % (format(w, ','), format(proj_w, ',')),
           '| 4 judges (S7, opus, max_turns 2) | %s | %s |' % (format(j, ','), format(proj_j, ',')),
           '| reserve: one judge retry (largest 2J judge %s) | - | %s |' % (format(jmax, ','), format(retry, ',')),
           '| S3 agent (own context) | - | %s |' % format(OWN_EST, ','),
           '| **total** | | **%s** |' % format(total, ','), '',
           'Verdict: %s. Headless reservation cap enforced in pipeline.py = %s; each judge session capped at %s '
           '(reservation before spawn + wall kill 2,400 s + post-hoc check; a breach is recorded and stops the chain).'
           % ('WITHIN budget' if ok else 'EXCEEDS budget -> STOP', format(HEADLESS_CAP, ','), format(JUDGE_CAP, ',')),
           '', '## Actual (appended per session)', '']
    open(P2L + '/TOKENS.md', 'w', encoding='utf-8').write('\n'.join(txt) + '\n')
    if not ok:
        open(P2L + '/STOP_E_budget.md', 'w').write('# STOP E budget\nProjection %d > %d; 0 sessions spawned.\n' % (total, BUDGET))
        return 5
    print('projection', total)
    return 0


# ------------------------------------------------------------------ set + exclusion proof
SPLIT = re.compile(r'[\n"\t|\\]')
BUL = re.compile(r'^\s*(?:[-*>•]|\d+[.)]|[A-Z]\d?[:.)])\s+')
CZRE = re.compile('[ěřůĚŘŮ]')
CZID = re.compile(r'\bCZ:(\d+)')


def harvest(o, S, EID, PAIRS, depth=0):
    if isinstance(o, dict):
        if 'exercise_id' in o:
            try: EID.add(int(o['exercise_id']))
            except Exception: pass
        if 'concept_id' in o and 'exercise_type_id' in o:
            try: PAIRS.add((int(o['concept_id']), int(o['exercise_type_id'])))
            except Exception: pass
        for v in o.values():
            harvest(v, S, EID, PAIRS, depth)
    elif isinstance(o, list):
        for v in o:
            harvest(v, S, EID, PAIRS, depth)
    elif isinstance(o, str):
        t = o.strip()
        S.add(t)
        if len(t) > 30:
            for seg in SPLIT.split(t):
                seg = BUL.sub('', seg).strip()
                if seg: S.add(seg)
            if depth < 3 and t[:1] in '[{':
                try: harvest(json.loads(t), S, EID, PAIRS, depth + 1)
                except Exception: pass


def cmd_make_set(a):
    rows = jl(ANN)
    assert len(rows) == 4064
    src_set = {r['src'] for r in rows}
    en_set = {r['en'] for r in rows if r.get('en')}
    src_list = sorted(src_set)
    files = []
    for top in sorted(glob.glob(ROOT + '/phase1*') + glob.glob(ROOT + '/phase2*')):
        for dp, dn, fn in os.walk(top):
            if dp == E or dp.startswith(E + '/') or '/.git' in dp:
                continue
            for f in fn:
                if f.endswith(('.json', '.jsonl', '.md', '.txt', '.py', '.csv', '.tsv', '.sh')):
                    files.append(os.path.join(dp, f))
    ex_src, ex_en, ex_eid, ex_pairs, ex_czid = set(), set(), set(), set(), set()
    contrib, corpus, skipped = [], [], []
    for p in files:
        rel = os.path.relpath(p, ROOT)
        sz = os.path.getsize(p)
        if sz > 60e6:
            skipped.append({'file': rel, 'why': 'size %d' % sz}); continue
        raw = open(p, encoding='utf-8', errors='replace').read()
        obj = None
        if p.endswith('.json'):
            try: obj = json.loads(raw)
            except Exception: obj = None
        elif p.endswith('.jsonl'):
            try: obj = [json.loads(l) for l in raw.splitlines() if l.strip()]
            except Exception: obj = None
        S, EID, PAIRS = set(), set(), set()
        harvest(obj if obj is not None else raw, S, EID, PAIRS)
        scan = json.dumps(obj, ensure_ascii=False) if obj is not None else raw
        hs, he = S & src_set, S & en_set
        if len(hs) > 1000 or len(he) > 1000:
            corpus.append({'file': rel, 'src_hits': len(hs), 'en_hits': len(he)}); continue
        sub = 0
        if sz < 3e6 and CZRE.search(scan):
            extra = {s for s in src_list if s not in hs and s in scan}
            sub = len(extra); hs = hs | extra
        cz = {int(x) for x in CZID.findall(scan)}
        if hs or he or cz:
            contrib.append({'file': rel, 'src_hits': len(hs), 'src_substring_hits': sub, 'en_hits': len(he),
                            'exercise_ids': len(EID), 'concept_type_pairs': len(PAIRS), 'cz_ids': len(cz)})
        if hs or he or EID or PAIRS or cz:
            ex_src |= hs; ex_en |= he; ex_eid |= EID; ex_pairs |= PAIRS; ex_czid |= cz
    out, stats, gseen = [], {}, set()
    for li, lv in enumerate(LEVELS):
        lvrows = sorted([r for r in rows if r['level'] == lv], key=lambda r: int(r['n']))
        st = Counter(rows=len(lvrows))
        cand = []
        for r in lvrows:
            why = None
            if not (r.get('src') or '').strip(): why = 'empty_src'
            elif r['src'] in ex_src: why = 'excl_src'
            elif r.get('en') in ex_en: why = 'excl_en'
            elif int(r['exercise_id']) in ex_eid: why = 'excl_exercise_id'
            elif int(r['exercise_id']) in ex_czid or int(r['n']) in ex_czid: why = 'excl_cz_id'
            elif (int(r['concept_id']), int(r['exercise_type_id'])) in ex_pairs: why = 'excl_concept_type'
            elif r['src'] in gseen: why = 'dup_src'
            if why:
                st[why] += 1; continue
            gseen.add(r['src']); cand.append(r)
        st['eligible'] = len(cand)
        if len(cand) < 25:
            print('too few eligible at', lv, dict(st)); return 3
        pick = sorted(random.Random(SEED + li).sample(cand, 25), key=lambda r: int(r['n']))
        st['picked'] = 25
        stats[lv] = dict(st)
        for k, r in enumerate(pick, 1):
            out.append({'sid': int(r['n']), 'wid': 'w%s%02d' % (lv, k), 'level': lv, 'czech': r['src'], 'topic': r['type_title'],
                        'exercise_id': r['exercise_id'], 'n': r['n'], 'annotation': r})
    assert len(out) == 100 and len({o['czech'] for o in out}) == 100 and len({o['sid'] for o in out}) == 100
    proof = {o['sid']: {'src_used_before': o['czech'] in ex_src, 'en_used_before': o['annotation'].get('en') in ex_en,
                        'eid_used_before': int(o['exercise_id']) in ex_eid,
                        'concept_type_used_before': (int(o['annotation']['concept_id']), int(o['annotation']['exercise_type_id'])) in ex_pairs}
             for o in out}
    assert not any(any(v.values()) for v in proof.values())
    h = wjl(E + '/set/sentences.jsonl', out)
    wj(E + '/set/EXCLUSION_PROOF.json', {
        'method': 'Every .json/.jsonl/.md/.txt/.py/.csv/.tsv/.sh file under phase1*/ and phase2*/ (partE excluded) scanned: '
                  'exact string values + line/quote segments (JSON parsed, nested JSON strings parsed) matched against the 4,064 '
                  'Czech src and their en; small files with Czech letters also substring-scanned for every src; exercise_id and '
                  '(concept_id, exercise_type_id) of every dict, CZ:<id> tokens. A file hitting > 1,000 src or en is the '
                  'production corpus itself (not a set) and is listed in corpus_wide_files, not used. A Czech row is excluded '
                  'if its src, en, exercise_id, concept+type pair or id appears in any other file.',
        'files_scanned': len(files), 'skipped_large': skipped, 'corpus_wide_files': corpus, 'contributing_files': contrib,
        'excluded': {'src': len(ex_src), 'en': len(ex_en), 'exercise_ids': len(ex_eid), 'concept_type_pairs': len(ex_pairs),
                     'cz_ids': len(ex_czid)},
        'per_level': stats, 'picked_overlap_with_anything_used': 0, 'per_sentence': proof, 'sentences_sha256': h})
    wj(E + '/set/SET_META.json', {'seed': SEED, 'per_level_seed': {lv: SEED + i for i, lv in enumerate(LEVELS)}, 'stats': stats,
                                  'source': ANN, 'sha256': h})
    print(json.dumps({'stats': stats, 'files': len(files), 'corpus_wide': len(corpus), 'skipped': len(skipped)}))
    return 0


# ------------------------------------------------------------------ headless
def load_R():
    if P2J not in sys.path:
        sys.path.insert(0, P2J)
    import run_2j as R
    return R


def extract_array(text):
    t = (text or '').strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m: t = m.group(1).strip()
    i, j = t.find('['), t.rfind(']')
    if i < 0 or j < i: raise ValueError('no array')
    return json.loads(t[i:j + 1])


def spent(base):
    return sum(int(v.get('tokens') or 0) for p in glob.glob(base + '/*/sessions/*/headless_ledger.json')
               for v in json.load(open(p)).values())


def run_group(R, kind, jobs, base, stop_dir, est, max_turns, cap_session):
    """jobs: {key: (prompt, validate_fn)} -> results {key: {...}}; threads; reservation against HEADLESS_CAP."""
    lock, inflight, results = threading.Lock(), {}, {}

    def worker(key, prompt, vfn):
        atts = []
        for sid in (key, key + '_r1'):
            sd = os.path.join(base, kind, 'sessions', sid)
            d0 = R.read_json(os.path.join(sd, sid + '.json'), None)
            done = bool(d0 and d0.get('status') == 'ok')
            with lock:
                if not done and spent(base) + sum(inflight.values()) + est > HEADLESS_CAP:
                    results[key] = {'ok': False, 'stop': 'token_cap', 'why': 'stage headless reservation cap %d' % HEADLESS_CAP, 'attempts': atts}
                    return
                inflight[sid] = 0 if done else est
            try:
                d = R.run_session(sid, prompt, sd, stop_dir=stop_dir, model='opus', max_turns=max_turns, wall=2400,
                                  token_cap=cap_session, est=est)
            except R.Stop as e:
                results[key] = {'ok': False, 'stop': e.kind, 'why': e.why, 'attempts': atts}
                return
            finally:
                with lock: inflight.pop(sid, None)
            tok = int(d.get('tokens') or 0)
            try:
                arr = extract_array(d.get('result')); why = vfn(arr)
            except Exception as ex:
                arr, why = None, 'parse: %s' % ex
            atts.append({'sid': sid, 'tokens': tok, 'resumed': bool(d.get('resumed')), 'spawns': d.get('spawns'),
                         'num_turns': d.get('num_turns'), 'why': why})
            if cap_session and tok > cap_session:
                results[key] = {'ok': False, 'stop': 'judge_cap', 'why': 'session %s used %d > cap %d (recorded, output discarded)' % (sid, tok, cap_session), 'attempts': atts}
                return
            if not why:
                results[key] = {'ok': True, 'arr': arr, 'attempts': atts}
                return
        results[key] = {'ok': False, 'why': atts[-1]['why'], 'attempts': atts}

    th = [threading.Thread(target=worker, args=(k, p, v)) for k, (p, v) in jobs.items()]
    for t in th: t.start()
    for t in th: t.join()
    return results


def handle_fail(results, stop_root, stage):
    bad = {k: r for k, r in results.items() if not r['ok']}
    if not bad:
        return 0
    kinds = {r.get('stop') for r in bad.values()}
    msg = '%s: %s' % (stage, {k: (r.get('stop'), r.get('why')) for k, r in bad.items()})
    if 'usage_limit' in kinds:
        open(stop_root + '/STOP_E_quota.md', 'w').write('# STOP E quota / usage limit\n\n%s\n' % msg); return 4
    if kinds & {'headless_auth', 'headless_failed', 'headless_timeout'}:
        open(stop_root + '/STOP_E_headless.md', 'w').write('# STOP E headless session failed\n\n%s\n' % msg); return 4
    if 'judge_cap' in kinds or 'token_cap' in kinds:
        open(stop_root + '/STOP_E_tokencap.md', 'w').write('# STOP E token cap\n\n%s\n' % msg); return 4
    open(stop_root + '/STOP_E_invalid.md', 'w').write('# STOP E invalid output after one retry\n\n%s\n' % msg); return 3


def append_tokens(base, kind):
    for p in sorted(glob.glob(base + '/%s/sessions/*/headless_ledger.json' % kind)):
        for k, v in json.load(open(p)).items():
            tokens_md('- %s %s: %s tokens (%s, %ss)' % (kind, k, format(int(v.get('tokens') or 0), ','), v.get('kind'), v.get('secs')))
    tokens_md('- cumulative headless after %s: %s' % (kind, format(spent(base), ',')))


def writers(R, base, stop_root, mock=False):
    tmpl = open(WT, encoding='utf-8').read()
    assert tmpl.count('{SENTENCES}') == 1
    sents = jl(E + '/set/sentences.jsonl')
    jobs = {}
    os.makedirs(base + '/writers', exist_ok=True)
    for lv in LEVELS:
        ss = [s for s in sents if s['level'] == lv]
        prompt = tmpl.replace('{SENTENCES}', '\n'.join(json.dumps({'wid': s['wid'], 'czech': s['czech'], 'level': s['level'],
                                                                    'topic': s['topic']}, ensure_ascii=False) for s in ss))
        open(base + '/writers/prompt_%s.txt' % lv, 'w', encoding='utf-8').write(prompt)

        def vfn(arr, ss=ss):
            if not isinstance(arr, list) or [o.get('wid') if isinstance(o, dict) else None for o in arr] != [s['wid'] for s in ss]:
                return 'wid list mismatch'
            for o in arr:
                c, w = o.get('correct'), o.get('wrong')
                if not (isinstance(c, list) and len(c) == 5 and all(isinstance(x, str) and x.strip() for x in c)):
                    return 'correct != 5 at %s' % o.get('wid')
                if not (isinstance(w, list) and len(w) == 4 and all(isinstance(x, dict) for x in w)
                        and sorted(x.get('type') or '' for x in w) == sorted(TYPES)
                        and all(isinstance(x.get('answer'), str) and x['answer'].strip() for x in w)):
                    return 'wrong != T/W/M/S at %s' % o.get('wid')
            return None
        jobs[lv] = (prompt, vfn)
    res = run_group(R, 'writers', jobs, base, stop_root if not mock else base, est=80000, max_turns=12, cap_session=None)
    summ = {'template': WT, 'template_sha': hashlib.sha256(tmpl.encode()).hexdigest(), 'model': 'opus',
            'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()},
            'headless_tokens_total_ledger': spent(base)}
    rc = handle_fail(res, stop_root if not mock else base, 'writers')
    if rc:
        wj(base + '/writers/WRITERS_SUMMARY.json', summ); return rc
    by_wid = {s['wid']: s for s in sents}
    answers, dedup, tcount, ad = [], [], Counter(), 0
    for lv in LEVELS:
        for o in res[lv]['arr']:
            s = by_wid[o['wid']]; seen = set()
            items = [('correct', None, x, False, 'c%d' % i) for i, x in enumerate(o['correct'], 1)] + \
                    [('wrong', w['type'], w['answer'], bool(w.get('agent_drop')), w['type'].lower()) for w in o['wrong']]
            for intent, typ, x, adr, suf in items:
                x = x.strip()
                if x in seen:
                    dedup.append({'sid': s['sid'], 'intent': intent, 'type': typ, 'answer': x}); continue
                seen.add(x)
                if typ: tcount[typ] += 1
                ad += adr
                answers.append({'aid': 'A:%d:%s' % (s['sid'], suf), 'sid': s['sid'], 'level': s['level'], 'czech': s['czech'],
                                'topic': s['topic'], 'answer': x, 'writer_intent': intent, 'writer_type': typ, 'writer_agent_drop': adr})
    assert len({x['aid'] for x in answers}) == len(answers)
    h = wjl(base + '/set/answers.jsonl', answers)
    summ.update(answers=len(answers), correct=sum(x['writer_intent'] == 'correct' for x in answers),
                wrong=sum(x['writer_intent'] == 'wrong' for x in answers), wrong_by_type=dict(tcount), dedupes=dedup,
                agent_drop_natural=ad, answers_sha=h,
                tokens_new={k: sum(int(x.get('tokens') or 0) for x in r['attempts'] if not x['resumed']) for k, r in res.items()})
    wj(base + '/writers/WRITERS_SUMMARY.json', summ)
    print(json.dumps({k: summ[k] for k in ('answers', 'correct', 'wrong', 'wrong_by_type', 'tokens_new', 'headless_tokens_total_ledger')}))
    return 0


def packets(base):
    ans = jl(base + '/set/answers.jsonl')
    assert len({a['aid'] for a in ans}) == len(ans)
    rng = random.Random(JSEED)
    order = ans[:]; rng.shuffle(order)
    sess_of = {a['aid']: i % 4 for i, a in enumerate(order)}
    entries = [(a, sess_of[a['aid']], False) for a in order]
    controls = []
    for s in range(4):
        for lv in LEVELS:
            nc = 3 if s % 2 == 0 else 2
            pc = sorted([a for a in ans if sess_of[a['aid']] == s and a['level'] == lv and a['writer_intent'] == 'correct'], key=lambda a: a['aid'])
            pw = sorted([a for a in ans if sess_of[a['aid']] == s and a['level'] == lv and a['writer_intent'] == 'wrong'], key=lambda a: a['aid'])
            for a_ in rng.sample(pc, nc) + rng.sample(pw, 5 - nc):
                t = (s + SHIFT[lv]) % 4
                assert t != s
                controls.append((a_, t, True))
    assert len(controls) == 80
    entries += controls
    jids, key, pk = set(), [], {s: [] for s in range(4)}
    for a_, s, dup in entries:
        while True:
            j = 'j%05x' % rng.randrange(16 ** 5)
            if j not in jids:
                jids.add(j); break
        key.append({'jid': j, 'aid': a_['aid'], 'session': s + 1, 'is_control': dup, 'orig_session': sess_of[a_['aid']] + 1})
        pk[s].append({'jid': j, 'czech': a_['czech'], 'level': a_['level'], 'answer': a_['answer'], 'topic': a_['topic']})
    meta = {'seed': JSEED, 'controls': 80, 'sessions': {}}
    for s in range(4):
        rng.shuffle(pk[s])
        aids = [k['aid'] for k in key if k['session'] == s + 1]
        assert len(aids) == len(set(aids)) and {p['level'] for p in pk[s]} == set(LEVELS)
        p = base + '/judge/packet_s%d.jsonl' % (s + 1)
        h = wjl(p, pk[s])
        meta['sessions'][s + 1] = {'items': len(pk[s]), 'controls': sum(1 for k in key if k['session'] == s + 1 and k['is_control']),
                                   'levels': dict(Counter(x['level'] for x in pk[s])), 'sha256': h}
    wjl(base + '/judge/key.jsonl', key)
    byaid = {x['aid']: x for x in ans}
    cl = [k for k in key if k['is_control']]
    meta['controls_by_level'] = dict(Counter(byaid[k['aid']]['level'] for k in cl))
    meta['controls_by_intent'] = dict(Counter(byaid[k['aid']]['writer_intent'] for k in cl))
    meta['controls_session_pairs'] = dict(Counter('%d->%d' % (k['orig_session'], k['session']) for k in cl))
    wj(base + '/judge/PACKETS_META.json', meta)
    print(json.dumps(meta)[:600])
    return 0


def judge_prompt():
    old = open(JP, encoding='utf-8').read()
    assert old.count(DROP_OLD) == 1, 'defect-3 line not found exactly once'
    new = old.replace(DROP_OLD, DROP_NEW)
    assert new.rstrip().endswith('Items:')
    return old, new


def judges(R, base, stop_root, mock=False):
    old, prompt = judge_prompt()
    os.makedirs(base + '/judge', exist_ok=True)
    open(base + '/judge/judge_prompt.txt', 'w', encoding='utf-8').write(prompt)
    open(base + '/judge/PROMPT_CHANGE.md', 'w', encoding='utf-8').write(
        '# Judge prompt: 2K defect 3 line dropped\n\nSource: %s (sha256 %s)\nUsed: judge_prompt.txt (sha256 %s)\n\n'
        'Removed (2K report section 9 defect 3: the older, redundant dropped-word line before the owner\'s KIND ruling):\n\n'
        '```\n%s```\n\nReplaced by (its one clause the ruling does not restate is kept, verbatim wording):\n\n```\n%s```\n\n'
        'Every other byte is the 2K Czech judge prompt; the owner\'s KIND ruling line and the OUT OF SCOPE practised-structure '
        'paragraph are unchanged.\n' % (JP, hashlib.sha256(old.encode()).hexdigest(), hashlib.sha256(prompt.encode()).hexdigest(), DROP_OLD, DROP_NEW))
    jobs = {}
    for s in range(1, 5):
        items = jl(base + '/judge/packet_s%d.jsonl' % s)
        for it in items:
            assert set(it) == {'jid', 'czech', 'level', 'answer', 'topic'}
        full = prompt + '\n'.join(json.dumps(it, ensure_ascii=False) for it in items) + '\n'
        open(base + '/judge/prompt_s%d.txt' % s, 'w', encoding='utf-8').write(full)

        def vfn(arr, items=items):
            if not isinstance(arr, list): return 'not a list'
            want = [it['jid'] for it in items]
            got = [o.get('jid') if isinstance(o, dict) else None for o in arr]
            if len(got) != len(set(got)): return 'duplicate jid'
            if set(got) != set(want): return 'jid set mismatch (missing %d, extra %d)' % (len(set(want) - set(got)), len(set(got) - set(want)))
            for o in arr:
                if o.get('label') not in ('correct', 'wrong'): return 'bad label at %s' % o.get('jid')
                if not isinstance(o.get('reason'), str): return 'bad reason at %s' % o.get('jid')
            return None
        jobs['s%d' % s] = (full, vfn)
    res = run_group(R, 'judge', jobs, base, stop_root if not mock else base, est=110000, max_turns=2, cap_session=JUDGE_CAP)
    summ = {'prompt_sha': hashlib.sha256(prompt.encode()).hexdigest(), 'model': 'opus', 'max_turns': 2, 'cap_per_session': JUDGE_CAP,
            'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()},
            'headless_tokens_total_ledger': spent(base)}
    wj(base + '/judge/JUDGES_SUMMARY.json', summ)
    rc = handle_fail(res, stop_root if not mock else base, 'judges')
    if rc: return rc
    for k, r in res.items():
        json.dump(r['arr'], open(base + '/judge/verdicts_%s.json' % k, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(json.dumps({k: [x['tokens'] for x in r['attempts']] for k, r in res.items()}))
    return 0


def labels(base):
    key = jl(base + '/judge/key.jsonl')
    ans = {a['aid']: a for a in jl(base + '/set/answers.jsonl')}
    verd = {}
    for s in range(1, 5):
        for o in json.load(open(base + '/judge/verdicts_s%d.json' % s, encoding='utf-8')):
            verd[o['jid']] = o
    assert all(k['jid'] in verd for k in key)
    lab, ctrl = {}, []
    for k in key:
        if not k['is_control']:
            v = verd[k['jid']]
            lab[k['aid']] = {'aid': k['aid'], 'label': v['label'], 'reason': v['reason'], 'session': k['session'], 'jid': k['jid']}
    assert set(lab) == set(ans)
    for k in key:
        if k['is_control']:
            o, d = lab[k['aid']], verd[k['jid']]
            a_ = ans[k['aid']]
            ctrl.append({'aid': k['aid'], 'level': a_['level'], 'writer_intent': a_['writer_intent'], 'writer_type': a_['writer_type'],
                         'orig_session': o['session'], 'dup_session': k['session'], 'orig_label': o['label'], 'dup_label': d['label'],
                         'agree': o['label'] == d['label'], 'orig_reason': o['reason'], 'dup_reason': d['reason'],
                         'czech': a_['czech'], 'answer': a_['answer']})
    rows = sorted(lab.values(), key=lambda r: (ans[r['aid']]['sid'], r['aid']))
    wjl(base + '/judge/labels.jsonl', rows)
    dis = [c for c in ctrl if not c['agree']]
    inten = Counter('%s/%s->%s' % (ans[r['aid']]['writer_intent'], ans[r['aid']]['writer_type'], r['label']) for r in rows)
    wj(base + '/judge/controls.json', {'controls': len(ctrl), 'agree': len(ctrl) - len(dis), 'disagree': len(dis),
                                        'disagree_rate': rate(len(dis), len(ctrl)),
                                        'by_level': {lv: {'n': sum(c['level'] == lv for c in ctrl), 'disagree': sum(c['level'] == lv for c in dis)} for lv in LEVELS},
                                        'by_intent': {i: {'n': sum(c['writer_intent'] == i for c in ctrl), 'disagree': sum(c['writer_intent'] == i for c in dis)} for i in ('correct', 'wrong')},
                                        'disagreements': dis, 'all': ctrl})
    wj(base + '/judge/intent_agreement.json', dict(inten))
    print('labels', Counter(r['label'] for r in rows), 'controls disagree', len(dis))
    return 0


def build_items(base):
    sents = {s['sid']: s for s in jl(E + '/set/sentences.jsonl')}
    ans = jl(base + '/set/answers.jsonl')
    lab = {r['aid']: r for r in jl(base + '/judge/labels.jsonl')}
    items, truth = [], []
    for a_ in sorted(ans, key=lambda x: (x['sid'], x['aid'])):
        s = sents[a_['sid']]
        items.append({'jid': a_['aid'], 'sid': a_['sid'], 'level': a_['level'], 'czech': s['czech'], 'src': s['czech'],
                      'answer': a_['answer'], 'exercise_id': s['exercise_id'], 'n': s['n'], 'annotation': strip_refs(s['annotation'])})
        L = lab[a_['aid']]
        truth.append({'aid': a_['aid'], 'sid': a_['sid'], 'level': a_['level'], 'judge_label': L['label'], 'judge_reason': L['reason'],
                      'judge_session': L['session'], 'writer_intent': a_['writer_intent'], 'writer_type': a_['writer_type'],
                      'writer_agent_drop': a_['writer_agent_drop'], 'czech': s['czech'], 'answer': a_['answer'], 'topic': s['topic']})
    bad = [k for it in items for k in all_keys(it) if k in FORBID or str(k).startswith('lk_')]
    assert not bad, bad[:10]
    h1 = wjl(base + '/set/items.jsonl', items)
    h2 = wjl(base + '/set/truth.jsonl', truth)
    wj(base + '/set/ITEMS_META.json', {'items': len(items), 'items_sha256': h1, 'truth_sha256': h2,
                                       'poison_check': 'no key in %s nor lk_* anywhere in items.jsonl (recursive): PASS' % sorted(FORBID),
                                       'labels': dict(Counter(t['judge_label'] for t in truth))})
    print('items', len(items), h1[:12])
    return 0


def cmd_mock(a):
    R = load_R()
    base = E + '/_mock'
    os.makedirs(base, exist_ok=True)
    calls = {'n': 0, 'seen': set()}

    def fake(argv, timeout):
        calls['n'] += 1
        pr = argv[argv.index('-p') + 1]
        usage = {'input_tokens': 1000, 'output_tokens': 500}
        if 'Sentences:\n' in pr:
            lines = [json.loads(l) for l in pr.split('Sentences:\n', 1)[1].splitlines() if l.strip()]
            lv = lines[0]['level']
            arr = [{'wid': s['wid'], 'correct': ['c%d %s' % (i, s['wid']) for i in range(1, 6)],
                    'wrong': [{'type': t, 'answer': '%s %s' % (t, s['wid']), 'agent_drop': False} for t in TYPES]} for s in lines]
            if lv == 'A1' and 'wA1' not in calls['seen']:
                calls['seen'].add('wA1'); arr[0]['wrong'] = arr[0]['wrong'][:3]
        else:
            its = [json.loads(l) for l in pr.split('Items:\n', 1)[1].splitlines() if l.strip()]
            k = its[0]['jid']
            arr = [{'jid': it['jid'], 'label': 'correct' if it['answer'].startswith('c') else 'wrong', 'reason': 'mock row 429'} for it in its]
            if k not in calls['seen'] and len(calls['seen']) == 1:
                arr = arr[:-1]
            calls['seen'].add(k)
        env = {'type': 'result', 'is_error': False, 'subtype': 'success', 'result': '```json\n%s\n```' % json.dumps(arr), 'usage': usage}
        return types.SimpleNamespace(returncode=0, stdout=json.dumps(env), stderr='429 in stderr ignored')
    R.SPAWN[0] = fake; R.SLEEP_H[0] = lambda s: None; R.ENV[0] = dict(os.environ)
    for step in (lambda: writers(R, base, base, True), lambda: packets(base), lambda: judges(R, base, base, True),
                 lambda: labels(base), lambda: build_items(base)):
        rc = step()
        if rc:
            print('MOCK FAIL rc', rc); return rc
    print('MOCK PASS spawns', calls['n'])
    return 0


def cmd_writers(a):
    R = load_R()
    try:
        R.load_token()
    except R.Stop as e:
        open(P2L + '/STOP_E_spawn.md', 'w').write('# STOP E spawn\nOAuth token absent (%s); 0 sessions spawned, 0 cost.\n' % e.kind)
        return 4
    rc = writers(R, E, P2L)
    append_tokens(E, 'writers')
    return rc


def cmd_judges(a):
    R = load_R()
    try:
        R.load_token()
    except R.Stop as e:
        open(P2L + '/STOP_E_spawn.md', 'w').write('# STOP E spawn\nOAuth token absent (%s); 0 judge sessions spawned.\n' % e.kind)
        return 4
    rc = judges(R, E, P2L)
    append_tokens(E, 'judge')
    return rc


# ------------------------------------------------------------------ Gemini (frozen Czech stack), opened once
def cmd_gemini(a):
    sys.path.insert(0, P2L)
    import stack_2l_cz as SC
    R2 = SC.R; B = R2.B
    RUN = E + '/run'
    if os.path.exists(RUN):
        print('REFUSED: run dir exists (the set is opened once)'); return 2
    os.makedirs(RUN)
    spend = sorted({os.path.dirname(p) for p in glob.glob(P2L + '/**/ledger.jsonl', recursive=True)
                    if '/_test' not in p and not p.startswith(E + '/')})
    led0 = json.load(open(P2L + '/GEMINI_LEDGER.json'))
    items = B.open_set(E + '/set/items.jsonl', B.paths(RUN), 'Phase 2L Part E fresh Czech set, S3, opened ONCE by the frozen Czech stack')
    t0 = time.time()
    try:
        out = SC.run(items, RUN, 'S3E', spend_dirs=spend)
    except (R2.Stop, R2.Refused) as e:
        wj(RUN + '/RUN_OUT.json', {'status': 'STOPPED', 'kind': getattr(e, 'kind', None), 'why': getattr(e, 'why', str(e))})
        print('STOPPED', e); return 4
    out['ledger_before'] = led0; out['ledger_after'] = json.load(open(P2L + '/GEMINI_LEDGER.json'))
    out['spend_dirs'] = spend; out['secs'] = round(time.time() - t0, 1)
    wj(RUN + '/RUN_OUT.json', out)
    print(json.dumps({'status': out['status'], 'ledger_after': out['ledger_after']}))
    return 0 if out['status'] == 'COMPLETE' else 3


# ------------------------------------------------------------------ post + analysis
def block(ids, T, res):
    c = [j for j in ids if T[j]['judge_label'] == 'correct']
    w = [j for j in ids if T[j]['judge_label'] == 'wrong']
    cov = rate(sum(bool(res[j]['accept']) for j in c), len(c))
    fa = rate(sum(bool(res[j]['accept']) for j in w), len(w))
    return {'coverage': cov, 'fa': fa,
            'coverage_target_90': {'point': cov['pct'] is not None and cov['pct'] >= 90, 'interval': cov['cp95'][0] is not None and cov['cp95'][0] >= 90},
            'fa_target_5': {'point': fa['pct'] is not None and fa['pct'] < 5, 'interval': fa['cp95'][1] is not None and fa['cp95'][1] < 5}}


def cmd_post(a):
    RUN = E + '/run'
    res = {r['jid']: r for r in jl(RUN + '/final_tiprej.jsonl')}
    T = {t['aid']: t for t in jl(E + '/set/truth.jsonl')}
    assert set(res) == set(T), (len(res), len(T))
    ccp = RUN + '/cc/replies.jsonl'
    cc_ids = {r['jid'] for r in jl(ccp)} if os.path.exists(ccp) else set()
    led = []
    for sub in ('l3', 'cc'):
        p = RUN + '/%s/ledger.jsonl' % sub
        if os.path.exists(p):
            led += [dict(r, _part=sub) for r in jl(p)]
    counted = [r for r in led if r.get('http') == 200 and r.get('counted', True)]
    spend_usd = round(sum(float(r.get('cost_usd') or 0) for r in counted), 6)
    fails = sum(1 for r in counted if r.get('failed'))
    acc = sorted(glob.glob(RUN + '/**/access_log.jsonl', recursive=True))
    ids = list(T)
    H = {'label': 'FIRST OUT-OF-SAMPLE measurement of the SOURCE-ONLY design (Czech, frozen stack_2l_cz.py: SOURCE-ONLY + B content check, TIP rejected), fresh production set opened ONCE',
         'truth': 'judge_label (partE/judge/labels.jsonl, 4 opus judge sessions)',
         'pooled': block(ids, T, res), 'per_level': {lv: block([j for j in ids if T[j]['level'] == lv], T, res) for lv in LEVELS},
         'l3_only_diagnostic': block(ids, T, {j: {'accept': j in cc_ids} for j in ids}),
         'layers': dict(Counter(str(r.get('layer')) for r in res.values())),
         'gemini': {'ledger_rows': len(led), 'counted_http200': len(counted), 'by_part': dict(Counter(r['_part'] for r in counted)),
                    'failed_counted': fails, 'http': dict(Counter(str(r.get('http')) for r in led)), 'spend_usd': spend_usd},
         'ledger_phase': json.load(open(P2L + '/GEMINI_LEDGER.json')), 'access_logs': [os.path.relpath(p, E) for p in acc]}
    FR = [j for j in ids if T[j]['judge_label'] == 'correct' and not res[j]['accept']]
    FA = [j for j in ids if T[j]['judge_label'] == 'wrong' and res[j]['accept']]
    def cause(j):
        r, t = res[j], T[j]
        return {'aid': j, 'level': t['level'], 'layer': r.get('layer'), 'l3_layer': r.get('l3_layer'), 'l3_reply': r.get('l3_reply'),
                'cc_state': r.get('cc_state'), 'cc_word': r.get('cc_word'), 'writer_intent': t['writer_intent'], 'writer_type': t['writer_type'],
                'czech': t['czech'], 'answer': t['answer'], 'judge_reason': t['judge_reason']}
    H['false_rejections'] = {'n': len(FR), 'by_layer': dict(Counter(str(res[j].get('layer')) for j in FR)),
                             'by_writer': dict(Counter('%s/%s' % (T[j]['writer_intent'], T[j]['writer_type']) for j in FR)),
                             'by_level': dict(Counter(T[j]['level'] for j in FR)), 'items': [cause(j) for j in FR]}
    H['false_acceptances'] = {'n': len(FA), 'by_layer': dict(Counter(str(res[j].get('layer')) for j in FA)),
                              'by_writer_type': dict(Counter(str(T[j]['writer_type']) for j in FA)),
                              'by_level': dict(Counter(T[j]['level'] for j in FA)), 'items': [cause(j) for j in FA]}
    H['judge_noise'] = {k: v for k, v in json.load(open(E + '/judge/controls.json')).items() if k not in ('all',)}
    os.makedirs(E + '/analysis', exist_ok=True)
    wj(E + '/analysis/HEADLINE.json', H)
    raw = ''.join('## %s\n\n```\n%s```\n\n' % (os.path.relpath(p, E), open(p, encoding='utf-8').read()) for p in acc)
    open(RUN + '/ACCESS_LOG_VERBATIM.md', 'w', encoding='utf-8').write(
        '# Part E access log (verbatim copies)\n\nOpens of partE/set/items.jsonl recorded: %d (run/access_log.jsonl). No dry run and '
        'no other process opened the set.\n\n%s' % (len(jl(RUN + '/access_log.jsonl')), raw))
    rc_ = open(E + '/RUN_COMMIT.txt').read().strip()
    open(RUN + '/FINAL_RUN_DONE', 'w').write('Part E run finished %s; status %s; results %d; counted Gemini %d (HTTP 200); spend $%.6f; RUN_COMMIT %s\n'
                                             % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), json.load(open(RUN + '/RUN_OUT.json')).get('status'),
                                                len(res), len(counted), spend_usd, rc_))
    def row(name, b):
        c, f = b['coverage'], b['fa']
        return '| %s | %d/%d = %.2f %% [%.2f, %.2f] | %s / %s | %d/%d = %.2f %% [%.2f, %.2f] | %s / %s |' % (
            name, c['x'], c['n'], c['pct'], c['cp95'][0], c['cp95'][1], 'MET' if b['coverage_target_90']['point'] else 'missed',
            'MET' if b['coverage_target_90']['interval'] else 'missed', f['x'], f['n'], f['pct'], f['cp95'][0], f['cp95'][1],
            'MET' if b['fa_target_5']['point'] else 'missed', 'MET' if b['fa_target_5']['interval'] else 'missed')
    md = ['# Phase 2L Part E - Czech, fresh production set: analysis', '',
          '**This is the FIRST OUT-OF-SAMPLE measurement of the SOURCE-ONLY design** (frozen Czech stack_2l_cz.py, '
          'SOURCE-ONLY + B content check, TIP rejected; set opened once; truth = 4 opus judge sessions).', '',
          '| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |',
          '|---|---|---|---|---|', row('pooled', H['pooled'])] + [row(lv, H['per_level'][lv]) for lv in LEVELS] + \
         ['', 'Diagnostic, L3 only (before the content check): ' + row('L3 only', H['l3_only_diagnostic']), '',
          'Gemini: %d counted calls (HTTP 200; %s), %d failed-but-counted, spend $%.6f; phase ledger %s.' % (
              len(counted), H['gemini']['by_part'], fails, spend_usd, H['ledger_phase']), '',
          'Judge noise (80 hidden duplicates, different sessions): %d/%d disagree = %s %% %s.' % (
              H['judge_noise']['disagree'], H['judge_noise']['controls'], H['judge_noise']['disagree_rate']['pct'], H['judge_noise']['disagree_rate']['cp95']), '',
          '## False rejections (%d) by cause' % len(FR), '', 'by layer %s; by writer %s; by level %s' % (
              H['false_rejections']['by_layer'], H['false_rejections']['by_writer'], H['false_rejections']['by_level']), '',
          '| aid | lvl | layer | cc word | writer | Czech | answer | judge reason |', '|---|---|---|---|---|---|---|---|'] + \
         ['| %s | %s | %s | %s | %s/%s | %s | %s | %s |' % (x['aid'], x['level'], x['layer'], x['cc_word'] or '', x['writer_intent'], x['writer_type'] or '',
                                                          x['czech'].replace('|', '/'), x['answer'].replace('|', '/'), x['judge_reason'].replace('|', '/'))
          for x in H['false_rejections']['items']] + \
         ['', '## False acceptances (%d) by cause' % len(FA), '', 'by layer %s; by writer type %s; by level %s' % (
             H['false_acceptances']['by_layer'], H['false_acceptances']['by_writer_type'], H['false_acceptances']['by_level']), '',
          '| aid | lvl | layer | cc | writer type | Czech | answer | judge reason |', '|---|---|---|---|---|---|---|---|'] + \
         ['| %s | %s | %s | %s | %s | %s | %s | %s |' % (x['aid'], x['level'], x['layer'], x['cc_state'], x['writer_type'],
                                                       x['czech'].replace('|', '/'), x['answer'].replace('|', '/'), x['judge_reason'].replace('|', '/'))
          for x in H['false_acceptances']['items']] + \
         ['', '## Judge duplicate disagreements', ''] + \
         ['- %s (%s, %s/%s) s%d %s vs s%d %s: "%s"' % (c['aid'], c['level'], c['writer_intent'], c['writer_type'], c['orig_session'], c['orig_label'],
                                                       c['dup_session'], c['dup_label'], c['answer']) for c in H['judge_noise']['disagreements']]
    open(E + '/analysis/ANALYSIS.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    p = H['pooled']
    print('POOLED cov %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['coverage'], '| FA %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['fa'])
    for lv in LEVELS:
        L = H['per_level'][lv]
        print(lv, 'cov %(x)d/%(n)d %(pct).2f %(cp95)s' % L['coverage'], 'FA %(x)d/%(n)d %(pct).2f %(cp95)s' % L['fa'])
    print('FR', H['false_rejections']['by_layer'], H['false_rejections']['by_writer'], '| FA', H['false_acceptances']['by_layer'],
          H['false_acceptances']['by_writer_type'], '| gemini', len(counted), spend_usd, '| noise', H['judge_noise']['disagree'])
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['projection', 'make_set', 'mock', 'writers', 'packets', 'judges', 'labels', 'build_items', 'gemini', 'post'])
    a = ap.parse_args()
    f = {'projection': cmd_projection, 'make_set': cmd_make_set, 'mock': cmd_mock, 'writers': cmd_writers,
         'packets': lambda a: packets(E), 'judges': cmd_judges, 'labels': lambda a: labels(E),
         'build_items': lambda a: build_items(E), 'gemini': cmd_gemini, 'post': cmd_post}[a.cmd]
    return f(a)


if __name__ == '__main__':
    sys.exit(main())
