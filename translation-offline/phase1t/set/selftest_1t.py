#!/usr/bin/env python3
"""Phase 1T self-test of assemble_1t.py / build_packets_1t.py / floor_check_1t.py.
0 model calls, synthetic fixtures only (never a measurement).  Reads no real writer file.

    python3 phase1t/set/selftest_1t.py
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
ST = os.path.join(HERE, 'selftest')
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
OK, FAIL = [], []


def sh(args):
    p = subprocess.run([PY] + args, capture_output=True, text=True, env=ENV, cwd=HERE)
    return p.returncode, p.stdout + p.stderr


def check(name, cond, extra=''):
    (OK if cond else FAIL).append(name)
    print('  %s  %-46s %s' % ('PASS' if cond else 'FAIL', name, extra))


def fixture(tag, violate=None):
    d = os.path.join(ST, tag, 'data')
    shutil.rmtree(os.path.join(ST, tag), ignore_errors=True)
    args = ['floor_check_1t.py', '--make-fixture', d]
    if violate:
        args += ['--violate', violate]
    rc, out = sh(args)
    return d, rc, out


def main():
    print('1. clean fixture -> assemble')
    d, rc, _ = fixture('fx')
    rc, out = sh(['assemble_1t.py', '--data-dir', d])
    rep = json.loads(out[out.index('{'):out.rindex('}') + 1]) if '{' in out else {}
    check('assemble accepts the clean fixture', rc == 0, 'rc=%d' % rc)
    check('100 sentences / 900 items', rep.get('sentences') == 100 and rep.get('items') == 900,
          '%s/%s' % (rep.get('sentences'), rep.get('items')))
    check('levels 25/25/25/25', sorted(rep.get('levels', {}).values()) == [25, 25, 25, 25])
    check('halves 50/50', sorted(rep.get('halves', {}).values()) == [50, 50])
    check('earlier sentences ~570',
          550 <= rep.get('earlier_sentences_checked_against', 0) <= 620,
          str(rep.get('earlier_sentences_checked_against')))
    check('outputs written', rep.get('outputs_written') is True)

    print('2. refusals (one fixture per violation)')
    cases = {'counts': 'answer_count_not_4_5', 'dupanswer': 'duplicate_answer',
             'unknowntag': 'unknown_tag', 'missingann': 'missing_annotation_field',
             'dupslovak': 'duplicate_slovak', 'overlap': 'overlap_exact',
             'jaccard': 'overlap_jaccard'}
    for v, kind in cases.items():
        dv, _, _ = fixture('v_' + v, v)
        rc, out = sh(['assemble_1t.py', '--data-dir', dv])
        check('REFUSE on %s' % v, rc == 2 and kind in out, 'rc=%d' % rc)
        rc2, out2 = sh(['assemble_1t.py', '--data-dir', dv, '--report'])
        md = os.path.join(os.path.dirname(dv), 'ASSEMBLE_REPORT_1T.md')
        txt = open(md, encoding='utf-8').read() if os.path.exists(md) else ''
        check('--report lists %s by sid' % v,
              rc2 == 0 and kind in txt and '1T00' in txt, 'rc=%d' % rc2)
        check('--report writes no data outputs on %s' % v,
              not os.path.exists(os.path.join(dv, 'items.json')))
    dm, _, _ = fixture('v_missing')
    os.remove(os.path.join(dm, 'writer_W3_part2.json'))
    rc, out = sh(['assemble_1t.py', '--data-dir', dm])
    check('REFUSE on a missing writer file', rc == 2 and 'missing_file' in out, 'rc=%d' % rc)

    print('3. packets')
    rc, out = sh(['build_packets_1t.py', '--data-dir', d])
    prep = json.loads(out[out.index('{'):out.rindex('}') + 1]) if '{' in out else {}
    check('build_packets rc=0', rc == 0, 'rc=%d' % rc)
    check('4 packets of 245', prep.get('packet_sizes') == [245, 245, 245, 245])
    check('980 jids = 900 + 80 controls',
          prep.get('total_jids') == 980 and prep.get('duplicate_controls') == 80)
    check('20 duplicate controls per level',
          sorted((prep.get('duplicates_per_level') or {}).values()) == [20, 20, 20, 20])
    check('packet items carry only jid/slovak/answer/level', prep.get('packet_keys_clean') is True)
    check('levels shuffled across packets',
          all(len(x) == 4 for x in prep.get('levels_per_packet', [])),
          str(prep.get('levels_per_packet', [{}])[0]))
    jd = os.path.join(os.path.dirname(d), 'judge')
    p1 = json.load(open(os.path.join(jd, 'packet_P1.json'), encoding='utf-8'))
    check('key is outside judge/ reading list',
          os.path.exists(os.path.join(jd, '_private', '_key.json'))
          and not os.path.exists(os.path.join(jd, '_key.json')))
    check('no item id or tags leak into a packet',
          not any(k in json.dumps(p1) for k in ('"id"', '"tags"', '"intent"', 'agentdrop')))

    print('4. floors')
    rc, out = sh(['floor_check_1t.py', '--make-verdicts', d])
    rc, out = sh(['floor_check_1t.py', '--data-dir', d])
    frep = json.load(open(os.path.join(os.path.dirname(d), 'FLOOR_CHECK_1T.json'),
                          encoding='utf-8'))
    check('floors pass on the meeting fixture', rc == 0 and frep['floors_pass'] is True,
          json.dumps(frep['floors_got'], sort_keys=True))
    check('no STOP_FLOOR.txt when floors pass',
          not os.path.exists(os.path.join(os.path.dirname(d), 'STOP_FLOOR.txt')))
    check('FLOOR_CHECK_1T.md written',
          os.path.exists(os.path.join(os.path.dirname(d), 'FLOOR_CHECK_1T.md')))
    check('T/W/M/S + cross-tables per level and half',
          set(frep['judged_wrong_TWMS']) >= {'all', 'level:A1', 'half:P1'}
          and set(frep['intent_x_judged']) >= {'all', 'level:B2', 'half:P2'})
    rc, out = sh(['assemble_1t.py', '--data-dir', d, '--labels'])
    lab = json.loads(out[out.index('{'):out.rindex('}') + 1]).get('labels', {})
    check('--labels joins verdicts + duplicate-control noise',
          rc == 0 and lab.get('items_labelled') == 900 and lab.get('duplicate_controls') == 80
          and lab.get('label_disagreements') is not None,
          'noise=%s%%' % lab.get('judge_noise_pct'))
    for f in ('F1', 'F2', 'F3', 'F4', 'F5'):
        sh(['floor_check_1t.py', '--make-verdicts', d, '--break-floor', f])
        rc, out = sh(['floor_check_1t.py', '--data-dir', d])
        fr = json.load(open(os.path.join(os.path.dirname(d), 'FLOOR_CHECK_1T.json'),
                            encoding='utf-8'))
        named = [k for k in fr['floors_failed'] if k.startswith(f + '_')]
        check('STOP when %s is short' % f,
              rc == 2 and named and os.path.exists(os.path.join(os.path.dirname(d),
                                                                'STOP_FLOOR.txt')),
              str(fr['floors_failed'].get(named[0]) if named else fr['floors_failed']))
    sh(['floor_check_1t.py', '--make-verdicts', d])          # leave the fixture in the good state
    sh(['floor_check_1t.py', '--data-dir', d])

    print('\nself-test: %d checks, %d passed, %d FAILED %s'
          % (len(OK) + len(FAIL), len(OK), len(FAIL), FAIL or ''))
    return 0 if not FAIL else 1


if __name__ == '__main__':
    raise SystemExit(main())
