#!/usr/bin/env python3
"""Phase 2J S4 / B2 - model audit of every SLOVAK reference (headless Claude, run_2j spawner = 2H recipe).
  python3 -B /abs/phase2j/partB/audit/audit_2j.py drive --cap 1500000      (nohup; resume-safe)
  python3 -B /abs/phase2j/partB/audit/audit_2j.py build                    (PROMPT.txt/.sha256, PACKETS.json only)
Packets: N=100 sentences, seeded shuffle (SEED) of all exercise_ids, levels mixed; item = id + Slovak + stored refs ONLY.
Waves of 4 parallel sessions. Token cap by reservation: a wave starts only if spent + (#todo x max observed packet cost)
<= cap (wave 1 reserved at FIRST_EST). Usage-limit envelope = hard STOP (run_2j writes phase2j/STOP_usage_limit.md);
rate limit only from the envelope (run_2j.classify_headless). Invalid output -> one retry (<pid>_r1)."""
import argparse, hashlib, json, os, random, re, sys, threading
sys.dont_write_bytecode = True
AUD = os.path.dirname(os.path.abspath(__file__)); P2J = os.path.dirname(os.path.dirname(AUD)); TOFF = os.path.dirname(P2J)
sys.path.insert(0, P2J)
import run_2j as R                                                              # noqa: E402
Stop = getattr(R, 'Stop', None) or R.B.Stop
SEED, N, WAVE, FIRST_EST = 20260921, 100, 4, 150000
CLASSES = ('F', 'A', 'N', 'W', 'O')
SK_UP = TOFF + '/phase2i/upload/annotations_sk_fixed.jsonl'; CZ_UP = TOFF + '/phase2i/upload/annotations_cz_fixed.jsonl'
TEMPLATE = """You are auditing stored English reference translations of Slovak sentences for a language-learning app. \
A learner's English answer is later compared with these references, so a reference that adds meaning, narrows a word, \
or fixes a person/gender wrongly makes correct answers look wrong.

PACKET ID: {PID}

Each line under ITEMS is one JSON object: "id" (exercise id), "sk" (the Slovak sentence), "refs" (its stored English \
references, in order). Judge EVERY reference against the Slovak ONLY and give it exactly one class:
  F  faithful: correct English that means what the Slovak means; nothing added, no word narrower than the Slovak, \
person/number/gender as in the Slovak. Natural idiom, word order and equally broad synonyms are fine.
  A  adds content: the English contains meaning the Slovak does not have (e.g. "her brother" for "brat"). span = the added words.
  N  narrows a word: an English word is narrower than the Slovak word, so the plain broader translation would be rejected \
(e.g. "fetched" for "nosila", broader "carried"). span = the narrow word(s); alt = the broader word(s).
  W  wrong person or gender: person/number/gender differs from the Slovak, OR the reference fixes he/she where the Slovak \
leaves the gender open (e.g. present tense with no subject). span = the pronoun/words; alt = the other-gender or correct form.
  O  other error (wrong meaning, different time frame, dropped content, ungrammatical English). span = the words concerned \
(from the reference, or from the Slovak if something was dropped); note = at most 12 words.

Do not use any tools. Output ONLY one JSON object - no prose, no code fences - of this shape:
{"packet": "{PID}", "results": [{"id": <id>, "refs": [{"c": "F"}, {"c": "N", "span": "fetched", "alt": "carried"}]}]}
One results entry per item, in the given order; one refs entry per stored reference, in order. span must be copied \
verbatim. alt is required for N and W.

ITEMS:
"""
TSHA = hashlib.sha256(TEMPLATE.encode('utf-8')).hexdigest()


def load_rows(path):
    return [json.loads(l) for l in open(os.path.abspath(path), encoding='utf-8')]


def build_packets(rows, n=N, seed=SEED):
    by = {r['exercise_id']: r for r in rows}
    assert len(by) == len(rows), 'duplicate exercise_id'
    ids = sorted(by); random.Random(seed).shuffle(ids)
    return [{'packet': 'p%03d' % k, 'items': [{'id': i, 'sk': by[i]['src'], 'refs': list(by[i]['v'])} for i in ids[s:s + n]]}
            for k, s in enumerate(range(0, len(ids), n))]


def prompt_of(p):
    return TEMPLATE.replace('{PID}', p['packet']) + '\n'.join(json.dumps(i, ensure_ascii=False) for i in p['items']) + '\n'


def _norm(s):
    return re.sub(r'\s+', ' ', str(s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()


def _int(x):
    try:
        return int(str(x).strip())
    except Exception:
        return x


def validate(text, p):
    """-> (hard_errors, soft_errors, parsed). Valid = no hard errors. soft = span not found verbatim."""
    s = re.sub(r'^```(?:json)?\s*|\s*```$', '', (text or '').strip())
    try:
        js = json.loads(s)
    except Exception as e:
        return ['not JSON: %r' % (e,)], [], None
    if not isinstance(js, dict) or not isinstance(js.get('results'), list):
        return ['no results list'], [], None
    hard, soft = [], []
    if js.get('packet') != p['packet']:
        hard.append('packet id %r' % js.get('packet'))
    want = [i['id'] for i in p['items']]
    got = [_int(r.get('id')) if isinstance(r, dict) else None for r in js['results']]
    if got != want:
        hard.append('ids differ: missing %s extra %s' % (sorted(set(want) - set(got))[:10], [g for g in got if g not in set(want)][:10]))
    by = {i['id']: i for i in p['items']}
    for r in js['results']:
        if not isinstance(r, dict) or _int(r.get('id')) not in by:
            continue
        it = by[_int(r['id'])]; rr = r.get('refs')
        if not isinstance(rr, list) or len(rr) != len(it['refs']):
            hard.append('%s: refs count' % it['id']); continue
        for k, (x, ref) in enumerate(zip(rr, it['refs'])):
            c = x.get('c') if isinstance(x, dict) else None
            if c not in CLASSES:
                hard.append('%s#%d: class %r' % (it['id'], k, c)); continue
            if c == 'F':
                continue
            sp = x.get('span')
            if not isinstance(sp, str) or not sp.strip():
                hard.append('%s#%d: span missing' % (it['id'], k))
            elif _norm(sp) not in _norm(ref) and not (c == 'O' and _norm(sp) in _norm(it['sk'])):
                soft.append('%s#%d: span not verbatim %r' % (it['id'], k, sp))
            if c in ('N', 'W') and not (isinstance(x.get('alt'), str) and x['alt'].strip()):
                hard.append('%s#%d: alt missing' % (it['id'], k))
    return hard, soft, js


def spent_tokens(out):
    t, sd = 0, os.path.join(out, 'sessions')
    if os.path.isdir(sd):
        for d in os.listdir(sd):
            L = R.read_json(os.path.join(sd, d, 'headless_ledger.json'), {})
            t += sum(int(v.get('tokens') or 0) for v in L.values())
    return t


def attempt(p, out, stop_dir, model, max_turns, wall):
    rec, prompt = {'packet': p['packet'], 'spawns': 0, 'tries': [], 'cost': 0}, prompt_of(p)
    for sid in (p['packet'], p['packet'] + '_r1'):
        d = R.run_session(sid, prompt, os.path.join(out, 'sessions', sid), stop_dir=stop_dir, model=model,
                          max_turns=max_turns, wall=wall)
        rec['spawns'] += d.get('spawns', 0); rec['cost'] += int(d.get('tokens') or 0)
        hard, soft, js = validate(d.get('result'), p)
        rec['tries'].append({'sid': sid, 'tokens': d.get('tokens'), 'resumed': bool(d.get('resumed')), 'hard': hard[:20], 'soft': soft[:20]})
        if not hard:
            R.write_json(os.path.join(out, 'results', p['packet'] + '.json'), {'packet': p['packet'], 'sid': sid, 'soft': soft, 'parsed': js})
            rec.update(status='valid', sid=sid, soft=len(soft))
            return rec
    rec['status'] = 'invalid'
    return rec


def drive(upload=SK_UP, out=AUD, cap=1500000, wave=WAVE, stop_dir=P2J, model='opus', max_turns=3, wall=1800,
          cz_upload=CZ_UP, first_est=FIRST_EST):
    out, stop_dir = os.path.abspath(out), os.path.abspath(stop_dir)
    os.makedirs(os.path.join(out, 'results'), exist_ok=True)
    packets = build_packets(load_rows(upload))
    setup(out, packets)
    ps_path = os.path.join(out, 'PACKET_STATUS.json')
    recs = R.read_json(ps_path, {})
    waves = [packets[i:i + wave] for i in range(0, len(packets), wave)]
    stop, lock, status = None, threading.Lock(), {}
    if R.ENV[0] is None:
        R.load_token()
    for w_i, W in enumerate(waves):
        if os.path.exists(os.path.join(stop_dir, 'STOP_usage_limit.md')):
            stop = {'kind': 'usage_limit', 'why': 'STOP_usage_limit.md present', 'before_wave': w_i + 1}; break
        todo = [p for p in W if (recs.get(p['packet']) or {}).get('status') not in ('valid', 'invalid', 'failed')]
        spent = spent_tokens(out)
        costs = [r['cost'] for r in recs.values() if r.get('cost')]
        est = max(costs) if costs else first_est
        if todo and spent + est * len(todo) > cap:
            stop = {'kind': 'token_cap', 'why': 'spent %d + %d x %d > cap %d' % (spent, len(todo), est, cap), 'before_wave': w_i + 1}
            break

        def work(p):
            try:
                r = attempt(p, out, stop_dir, model, max_turns, wall)
            except Stop as e:
                r = {'packet': p['packet'], 'status': 'failed', 'kind': e.kind, 'why': e.why, 'cost': 0}
            except Exception as e:                                          # noqa
                r = {'packet': p['packet'], 'status': 'failed', 'kind': 'crash', 'why': repr(e)[:300], 'cost': 0}
            with lock:
                recs[p['packet']] = r
        th = [threading.Thread(target=work, args=(p,)) for p in todo]
        [x.start() for x in th]; [x.join() for x in th]
        R.write_json(ps_path, recs)
        status = summary(out, packets, recs, cap, w_i + 1, len(waves), cz_upload)
        if w_i == 0:
            R.write_json(os.path.join(out, 'WAVE1.json'), status)
        if any(r.get('kind') == 'usage_limit' for r in recs.values()):
            stop = {'kind': 'usage_limit', 'why': 'usage-limit envelope', 'after_wave': w_i + 1}; break
    status = summary(out, packets, recs, cap, None, len(waves), cz_upload)
    valid = [p for p in packets if (recs.get(p['packet']) or {}).get('status') == 'valid']
    cov = {'complete': len(valid) == len(packets), 'stop': stop, 'packets_total': len(packets), 'packets_valid': [p['packet'] for p in valid],
           'packets_not_audited': [p['packet'] for p in packets if p not in valid], 'n_audited': sum(len(p['items']) for p in valid),
           'audited_exercise_ids': sorted(i['id'] for p in valid for i in p['items']), 'prompt_sha256': TSHA, 'seed': SEED}
    R.write_json(os.path.join(out, 'COVERAGE.json'), cov)
    with open(os.path.join(out, 'AUDIT_RESULTS.jsonl'), 'w', encoding='utf-8') as fh:
        for p in valid:
            js = R.read_json(os.path.join(out, 'results', p['packet'] + '.json'), {})['parsed']
            it = {i['id']: i for i in p['items']}
            for r in js['results']:
                i = it[_int(r['id'])]
                for k, x in enumerate(r['refs']):
                    fh.write(json.dumps({'exercise_id': i['id'], 'ref_index': k, 'ref': i['refs'][k], 'sk': i['sk'], 'packet': p['packet'],
                                         'c': x.get('c'), 'span': x.get('span'), 'alt': x.get('alt'), 'note': x.get('note')}, ensure_ascii=False) + '\n')
    status['coverage'] = {k: cov[k] for k in ('complete', 'stop', 'n_audited', 'packets_not_audited')}
    R.write_json(os.path.join(out, 'DRIVER_DONE.json'), status)
    return status


def setup(out, packets):
    pt = os.path.join(out, 'PROMPT.txt')
    if os.path.exists(pt) and open(pt, encoding='utf-8').read() != TEMPLATE:
        raise SystemExit('REFUSED: PROMPT.txt differs from the frozen template')
    open(pt, 'w', encoding='utf-8').write(TEMPLATE)
    open(os.path.join(out, 'PROMPT.sha256'), 'w').write(TSHA + '  PROMPT.txt\n')
    R.write_json(os.path.join(out, 'PACKETS.json'), {'seed': SEED, 'n': N, 'prompt_sha256': TSHA,
                 'packets': [{'packet': p['packet'], 'ids': [i['id'] for i in p['items']],
                              'prompt_sha256': hashlib.sha256(prompt_of(p).encode('utf-8')).hexdigest()} for p in packets]})


def summary(out, packets, recs, cap, wave_done, n_waves, cz_upload):
    done = [recs[p['packet']] for p in packets if p['packet'] in recs]
    costs = [r['cost'] for r in done if r.get('cost')]
    sess = {t['sid']: t['tokens'] for r in done for t in r.get('tries', [])}
    spent = spent_tokens(out)
    mean = sum(costs) / len(costs) if costs else None
    remaining = len(packets) - len([r for r in done if r.get('status') in ('valid', 'invalid')])
    st = {'wave_done': wave_done, 'n_waves': n_waves, 'cap': cap, 'spent': spent, 'per_session_tokens': sess,
          'per_packet_cost': {r['packet']: r.get('cost') for r in done}, 'mean_packet_cost': mean, 'max_packet_cost': max(costs) if costs else None,
          'projection_all_packets': spent + (max(costs) if costs else 0) * remaining if costs else None,
          'projection_all_packets_mean': spent + mean * remaining if costs else None,
          'status_counts': {s: sum(1 for r in done if r.get('status') == s) for s in ('valid', 'invalid', 'failed')},
          'failed': {r['packet']: [r.get('kind'), r.get('why')] for r in done if r.get('status') == 'failed'}}
    st['fits_cap_full'] = bool(costs) and st['projection_all_packets'] <= cap
    st['full_waves_fitting_estimate'] = None
    if costs:
        mx, w, s = max(costs), 0, spent
        pend = [p for p in packets if (recs.get(p['packet']) or {}).get('status') not in ('valid', 'invalid', 'failed')]
        for i in range(0, len(pend), WAVE):
            k = len(pend[i:i + WAVE])
            if s + mx * k > cap:
                break
            s += mx * k; w += 1
        st['further_waves_fitting_estimate'] = w
    if cz_upload and costs:
        skc = [len(prompt_of(p)) for p in packets]; czp = build_packets(load_rows(cz_upload))
        czc = [len(prompt_of(p)) for p in czp]
        st['cz_sizing'] = {'packets': len(czp), 'chars_sk_total': sum(skc), 'chars_cz_total': sum(czc),
                           'tokens_projection_mean': round(mean * len(czp) * (sum(czc) / len(czc)) / (sum(skc) / len(skc))),
                           'tokens_projection_max': round(max(costs) * len(czp) * (sum(czc) / len(czc)) / (sum(skc) / len(skc))), 'run': False}
    R.write_json(os.path.join(out, 'STATUS.json'), st)
    return st


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=('drive', 'build'))
    ap.add_argument('--upload', default=SK_UP); ap.add_argument('--out', default=AUD); ap.add_argument('--cap', type=int, default=1500000)
    ap.add_argument('--stop-dir', default=P2J); ap.add_argument('--cz-upload', default=CZ_UP)
    a = ap.parse_args(argv)
    if a.cmd == 'build':
        pk = build_packets(load_rows(a.upload)); setup(os.path.abspath(a.out), pk)
        print(json.dumps({'packets': len(pk), 'sha': TSHA, 'items': sum(len(p['items']) for p in pk)})); return 0
    st = drive(a.upload, a.out, a.cap, stop_dir=a.stop_dir, cz_upload=a.cz_upload)
    print(json.dumps(st['coverage'])); return 0


if __name__ == '__main__':
    sys.exit(main())
