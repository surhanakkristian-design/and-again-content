#!/usr/bin/env python3
"""Phase 1W §4 driver: open the fresh set A4 ONCE with 1V's A4 tooling (copied unchanged into
phase1w/a4/) and the 1W stack (1V round 2 + §2, phase1w/stack_1w.py; §3 reverted).
Resumable: every stage skips work whose output is already valid.  --final is never run twice
(the copied 1U runner refuses on its own).  Writes phase1w/S4_RESULT.md in every outcome."""
import collections, datetime, glob, json, os, re, shutil, subprocess, sys, time

TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
REPO = os.path.dirname(TOFF)
W = os.path.join(TOFF, 'phase1w')
A4 = os.path.join(W, 'a4')
SET = os.path.join(A4, 'set')
RUN = os.path.join(A4, 'run')
DATA = os.path.join(A4, 'data')
SESS = os.path.join(A4, 'sessions')
V = os.path.join(TOFF, 'phase1v', 'trackA_set')
U = os.path.join(TOFF, 'phase1u', 'run')
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/'
                         'Contents/MacOS/claude')
LOG = os.path.join(A4, 'driver_1w.log')
STATE = os.path.join(A4, 'driver_state.json')
CAP_RUN = 800
LEVELS = ('A1', 'A2', 'B1', 'B2')
COAUTH = 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'
R = {'status': None, 'notes': [], 'sessions': []}
TOK = None


def say(s):
    line = '[%s] %s' % (datetime.datetime.now().strftime('%H:%M:%S'), s)
    print(line, flush=True)
    with open(LOG, 'a') as fh:
        fh.write(line + '\n')


def save_state():
    with open(STATE, 'w') as fh:
        json.dump(R, fh, indent=1, ensure_ascii=False, default=str)


def sh(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    out = (p.stdout or '') + (p.stderr or '')
    say('$ %s -> exit %d' % (' '.join(cmd) if isinstance(cmd, list) else cmd, p.returncode))
    with open(LOG, 'a') as fh:
        fh.write(out[-8000:] + '\n')
    return p.returncode, out


def jload(p, default=None):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return default


# ------------------------------------------------------------------ setup (copies, one patch)
REPL = lambda s: s.replace('phase1v/trackA_set', 'phase1w/a4/set')

PATCH_RUNNER = r'''

# ======================================================================================
# Phase 1W §4 - the ONLY functional change to the copied 1U runner: the stack.
# Stack = 1V round 2 (AG v4 full + v5 refsubj rs_nom + TIP determiner rule) + §2 (reader_nom),
# entry phase1w/stack_1w.py.  §3 was REVERTED: the L3 prompt is P-FROZEN-1U unchanged.
# AG primary = stack_1w.decide (so rs_nom rejects land before L3, 0 calls); after the rows are
# built, stack_1w.final_accept(row) is applied to every row (TIPdet / AGv5), 0 calls.
# Run cap for this phase: 800 counted calls (brief §4 instruction), enforced by cap_check.
# ======================================================================================
_P1W = os.path.join(TOFF, 'phase1w')
if _P1W not in sys.path:
    sys.path.insert(0, _P1W)
import stack_1w as SW1W                                                        # noqa: E402


class _AG1W(object):
    @staticmethod
    def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None):
        return SW1W.decide(sk, ann, wtags, answer, reference, 'primary',
                           tuple(AG4.ALL_FLAGS), ('rs_nom',))


AG_CFG['primary'] = (_AG1W, tuple(AG4.ALL_FLAGS))
CAP_1U = 800
_build_rows_1u = build_rows


def build_rows(recs, res, ag, planned, labels, hmap, failed):
    rows, _agg = _build_rows_1u(recs, res, ag, planned, labels, hmap, failed)
    agg = collections.Counter()
    for r in rows.values():
        r['stack_in'] = {'final_accept': r['final_accept'], 'final_layer': r['final_layer']}
        acc, lay = SW1W.final_accept(r, ('rs_nom',), True)
        r['final_accept'], r['final_layer'] = acc, lay
        agg['%s/%s' % ('accept' if acc else 'reject', r.get('judged') or 'unlabelled')] += 1
    return rows, dict(agg)

'''

PATCH_SCORE = r'''

# Phase 1W §4 - S7 (declared in phase1v/trackA_set/SENSITIVITIES_1V.json, "the run agent's scorer
# must implement S7"): determiner-difference items judged CORRECT rescored as WRONG.
_labellers_1u = labellers


def labellers(rows):
    out, moved = _labellers_1u(rows)
    det = {r['item_id'] for r in rows
           if 'determiner' in (r.get('tags') or []) and base_label(r) == 'correct'}
    out['S7_determiner_correct_as_wrong'] = (
        lambda r: 'wrong' if r['item_id'] in det else base_label(r), lambda r: True,
        'determiner-difference items (writer tag determiner) judged CORRECT rescored as WRONG')
    moved['S7_determiner_correct_as_wrong'] = sorted(det)
    return out, moved

'''


def insert_before_main(src, patch):
    i = src.rindex("\nif __name__ == '__main__':")
    return src[:i] + patch + src[i:]


def setup():
    for d in (A4, SESS, DATA):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(SET):
        for d in ('briefs', 'judge', 'writers', 'data'):
            os.makedirs(os.path.join(SET, d))
        for f in ('assemble_1v.py', 'build_packets_1v.py', 'join_labels_1v.py', 'floors_1v.py',
                  'selftest_1v.py', 'FLOORS_DECLARED_1V.json', 'SENSITIVITIES_1V.json'):
            shutil.copy2(os.path.join(V, f), os.path.join(SET, f))
        for f in ('SPLIT_1V.md', 'WRITER_SPEC_1V.md', 'judge/JUDGE_BRIEF_1V.md') + tuple(
                'briefs/WRITER_TASK_%s.md' % L for L in LEVELS):
            open(os.path.join(SET, f), 'w', encoding='utf-8').write(
                REPL(open(os.path.join(V, f), encoding='utf-8').read()))
        say('setup: 1V A4 tooling copied to %s (md paths repointed phase1v/trackA_set -> '
            'phase1w/a4/set; .py byte-identical)' % SET)
    if not os.path.exists(RUN):
        os.makedirs(RUN)
        for f in ('loader_1u.py', 'article_line_1u.py', 'selftest_1u_run.py',
                  'FROZEN_CONFIG_1U.json'):
            shutil.copy2(os.path.join(U, f), os.path.join(RUN, f))
        src = open(os.path.join(U, 'runner_1u.py'), encoding='utf-8').read()
        a = "TASKA = os.path.join(P1U, 'taskA')"
        assert a in src
        src = src.replace(a, "TASKA = os.path.join(TOFF, 'phase1u', 'taskA')   # 1W: AG v4 home", 1)
        open(os.path.join(RUN, 'runner_1u.py'), 'w', encoding='utf-8').write(
            insert_before_main(src, PATCH_RUNNER))
        src = open(os.path.join(U, 'score_1u.py'), encoding='utf-8').read()
        open(os.path.join(RUN, 'score_1u.py'), 'w', encoding='utf-8').write(
            insert_before_main(src, PATCH_SCORE))
        say('setup: 1U runner/loader/scorer copied to %s; runner patched (TASKA path, stack, cap '
            '800), scorer patched (S7)' % RUN)
    # selftest of the copied set tooling, in a throwaway copy (0 calls)
    if 'selftest_1v' not in R:
        tmp = os.path.join(A4, '_selftest_tmp', 'set')
        shutil.rmtree(os.path.dirname(tmp), ignore_errors=True)
        shutil.copytree(SET, tmp)
        rc, out = sh(['python3', os.path.join(tmp, 'selftest_1v.py')], cwd=tmp)
        R['selftest_1v'] = {'exit': rc, 'tail': out.strip().splitlines()[-1:] if out else []}
        shutil.rmtree(os.path.dirname(tmp), ignore_errors=True)
        save_state()


# ------------------------------------------------------------------ headless sessions
def token():
    global TOK
    if TOK is None:
        TOK = subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'],
                             capture_output=True, text=True).stdout.strip()
    return TOK


def child_env():
    e = {k: v for k, v in os.environ.items()
         if not (k.startswith('CLAUDECODE') or k.startswith('CLAUDE_CODE_SDK')
                 or k in ('CLAUDE_CODE_ENTRYPOINT', 'ANTHROPIC_API_KEY'))}
    e['CLAUDE_CODE_OAUTH_TOKEN'] = token()
    e['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] = '64000'
    return e


def redact(path):
    if not os.path.exists(path):
        return
    s = open(path, encoding='utf-8', errors='replace').read()
    t = s.replace(TOK, '[REDACTED]') if TOK else s
    t = re.sub(r'sk-ant-[A-Za-z0-9_\-]+', 'sk-ant-[REDACTED]', t)
    if t != s:
        open(path, 'w', encoding='utf-8').write(t)


def spawn(name, prompt):
    out = os.path.join(SESS, name + '.json')
    err = os.path.join(SESS, name + '.err')
    open(os.path.join(SESS, name + '.prompt.md'), 'w', encoding='utf-8').write(prompt)
    cmd = [BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', 'opus',
           '--permission-mode', 'acceptEdits', '--allowedTools', 'Read,Write',
           '--disallowedTools', 'Bash,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit']
    p = subprocess.Popen(cmd, cwd=SET, env=child_env(), stdout=open(out, 'w'),
                         stderr=open(err, 'w'), stdin=subprocess.DEVNULL)
    say('spawned headless session %s (pid %d)' % (name, p.pid))
    return {'name': name, 'p': p, 'out': out, 'err': err, 't0': time.time()}


def wait_all(procs, timeout):
    for s in procs:
        left = max(1, timeout - (time.time() - s['t0']))
        try:
            s['p'].wait(timeout=left)
        except subprocess.TimeoutExpired:
            s['p'].kill()
            s['p'].wait()
            say('session %s KILLED after %ds' % (s['name'], timeout))
        redact(s['out']); redact(s['err'])
        j = jload(s['out'], {}) or {}
        u = j.get('usage') or {}
        rec = {'session': s['name'], 'exit': s['p'].returncode, 'is_error': j.get('is_error'),
               'subtype': j.get('subtype'), 'num_turns': j.get('num_turns'),
               'duration_ms': j.get('duration_ms'), 'total_cost_usd': j.get('total_cost_usd'),
               'input_tokens': u.get('input_tokens'),
               'cache_creation_input_tokens': u.get('cache_creation_input_tokens'),
               'cache_read_input_tokens': u.get('cache_read_input_tokens'),
               'output_tokens': u.get('output_tokens'),
               'models': sorted((j.get('modelUsage') or {}).keys()),
               'permission_denials': len(j.get('permission_denials') or []),
               'result_head': (j.get('result') or '')[:600]}
        if not j:
            rec['stderr_tail'] = open(s['err'], encoding='utf-8', errors='replace').read()[-600:]
        R['sessions'].append(rec)
        say('session %s done: %s' % (s['name'], json.dumps({k: rec[k] for k in (
            'exit', 'is_error', 'num_turns', 'input_tokens', 'cache_read_input_tokens',
            'output_tokens')})))
    save_state()


def writer_ok(L):
    for k in (1, 2):
        o = jload(os.path.join(SET, 'writers', 'writer_%s_part%d.json' % (L, k)))
        if not o:
            return False
    return True


def writers():
    for attempt in (1, 2):
        todo = [L for L in LEVELS if not writer_ok(L)]
        if not todo:
            return True
        if attempt == 2:
            R['notes'].append('writer retry (whole task re-run) for levels %s after a missing or '
                              'unparsable writer file' % todo)
        procs = [spawn('writer_%s_try%d' % (L, attempt),
                       open(os.path.join(SET, 'briefs', 'WRITER_TASK_%s.md' % L),
                            encoding='utf-8').read()) for L in todo]
        wait_all(procs, 3600)
    return all(writer_ok(L) for L in LEVELS)


def packet_sizes():
    rep = jload(os.path.join(SET, 'build_packets_1v.json'), {})
    return {s['part']: s['items'] for s in rep.get('part_sizes', [])}


def verdict_ok(k, n):
    o = jload(os.path.join(SET, 'judge', 'verdicts_part%d.json' % k))
    if isinstance(o, dict):
        o = o.get('verdicts') or list(o.values())
    return isinstance(o, list) and len(o) == n


def judge():
    sizes = packet_sizes()
    task = open(os.path.join(SET, 'judge', 'JUDGE_TASK_1V.md'), encoding='utf-8').read()
    for n in (1, 2, 3):
        miss = [k for k, m in sorted(sizes.items()) if not verdict_ok(k, m)]
        if not miss:
            return True
        if n == 1:
            prompt = task
        else:
            done = [k for k in sizes if k not in miss]
            R['notes'].append('judge continuation session %d for parts %s (parts %s already '
                              'written)' % (n, miss, done))
            keep = []
            for line in task.splitlines():
                m = re.match(r'\s+- part (\d+) ', line)
                if m and int(m.group(1)) not in miss:
                    continue
                keep.append(line)
            prompt = ('CONTINUATION: an earlier session of this same task already wrote the '
                      'verdict files for parts %s. Judge ONLY the parts listed in step 2 below.\n\n'
                      % done) + '\n'.join(keep) + '\n'
        wait_all([spawn('judge_s%d' % n, prompt)], 5400)
    return all(verdict_ok(k, m) for k, m in sizes.items())


# ------------------------------------------------------------------ stage A: the set
def stage_a():
    if not writers():
        return stop('STOP: writers did not deliver valid files (see sessions)')
    rc, out = sh(['python3', os.path.join(SET, 'assemble_1v.py')], cwd=SET)
    asm = jload(os.path.join(SET, 'assemble_1v.json'), {})
    R['assemble'] = {k: asm.get(k) for k in (
        'sentences_read', 'sentences_kept', 'items', 'levels', 'halves', 'kinds',
        'earlier_sentences_checked_against', 'overlaps_total', 'violations_total',
        'hard_violations', 'hard_violations_by_kind', 'floor_counts_by_construction', 'loud',
        'answer_kinds', 'wrong_types')}
    R['assemble']['exit'] = rc
    save_state()
    if rc != 0:
        return stop('STOP: assembler exit %d (set incomplete, not opened)' % rc)
    if not packet_sizes():
        rc, out = sh(['python3', os.path.join(SET, 'build_packets_1v.py')], cwd=SET)
        if rc != 0:
            return stop('STOP: packet build exit %d' % rc)
    R['packets'] = {k: v for k, v in (jload(os.path.join(SET, 'build_packets_1v.json'), {})
                                      or {}).items() if k in (
        'items', 'duplicate_controls', 'duplicates_per_level', 'total_qids', 'parts', 'seed',
        'packet_fields_clean', 'levels_per_part')}
    if not judge():
        return stop('STOP: the judge did not deliver all verdict files (see sessions)')
    rc, out = sh(['python3', os.path.join(SET, 'join_labels_1v.py')], cwd=SET)
    jl = jload(os.path.join(SET, 'join_labels_1v.json'), {})
    R['join'] = {k: jl.get(k) for k in (
        'key_entries', 'verdict_rows', 'items_labelled', 'unlabelled_items', 'judged', 'types',
        'confidence', 'borderline', 'duplicate_controls', 'duplicate_controls_judged',
        'label_disagreements', 'judge_noise_pct', 'type_only_disagreements', 'REFUSED')}
    R['join']['exit'] = rc
    save_state()
    if rc != 0:
        return stop('STOP: label join refused (exit %d)' % rc)
    rc, out = sh(['python3', os.path.join(SET, 'floors_1v.py')], cwd=SET)
    fl = jload(os.path.join(SET, 'floors_1v.json'), {})
    R['floors'] = fl
    R['floors_exit'] = rc
    save_state()
    if rc != 0 or not fl.get('all_pass'):
        return stop('STOP: a floor failed on JUDGED counts - set NOT opened, 0 model calls')
    # data twin for the runner + 1U-named aliases the copied runner/loader read
    for f in ('sentences.json', 'annotations.json', 'items.json', 'labels.json'):
        shutil.copy2(os.path.join(SET, 'data', f), os.path.join(DATA, f))
    for f in glob.glob(os.path.join(SET, '*_1v.json')) + glob.glob(os.path.join(SET, '*_1V.json')):
        b = os.path.basename(f)
        shutil.copy2(f, os.path.join(SET, b.replace('_1v.json', '_1u.json')
                                     .replace('_1V.json', '_1U.json')))
    return True


# ------------------------------------------------------------------ stage B: freeze + run
def git(*a):
    return sh(['git'] + list(a), cwd=REPO)


def stage_b():
    # chmod earlier phase dirs BEFORE the run
    dirs = sorted(d for d in glob.glob(os.path.join(TOFF, 'phase1[a-v]*')) if os.path.isdir(d))
    for d in dirs:
        subprocess.run(['chmod', '-R', 'a-w', d])
    ev = []
    for d in dirs:
        ev.append(subprocess.run(['stat', '-f', '%Sp %N', d], capture_output=True,
                                 text=True).stdout.strip().replace(TOFF + '/', ''))
    try:
        open(os.path.join(TOFF, 'phase1v', 'WRITE_TEST'), 'w').close()
        wt = 'WRITE SUCCEEDED (chmod ineffective)'
        os.remove(os.path.join(TOFF, 'phase1v', 'WRITE_TEST'))
    except Exception as e:
        wt = 'write test into phase1v refused: %s' % type(e).__name__
    R['chmod'] = {'dirs': len(dirs), 'stat': ev, 'write_test': wt}
    save_state()
    runner = os.path.join(RUN, 'runner_1u.py')
    # preflight 1 (0 calls) -> module list for the freeze
    rc, out = sh(['python3', runner, '--preflight', '--data-dir', DATA], cwd=RUN)
    if rc != 0:
        R['preflight_stop'] = out[-1500:]
        return stop('STOP: preflight refused/stopped (0 model calls): %s'
                    % out.strip().splitlines()[-1:] if out else rc)
    mods = open(os.path.join(RUN, 'MODULES_1U.txt')).read().split()
    with open(os.path.join(RUN, 'FREEZE_FILES'), 'w') as fh:
        fh.write('# Phase 1W FREEZE_FILES - every .py the run imports, relative to the repository '
                 'root.\n')
        for f in sorted(set(mods + ['translation-offline/phase1w/a4/run/score_1u.py',
                                    'translation-offline/phase1w/a4/run/selftest_1u_run.py'])):
            fh.write(f + '\n')
    save_state()
    git('add', 'translation-offline/phase1w')
    git('commit', '-m', 'Phase 1W §4: FREEZE - A4 fresh set judged, floors pass, stack 1V r2 + '
        '§2 (prompt unchanged), before opening\n\n' + COAUTH, '--', 'translation-offline/phase1w')
    fh_ = git('rev-parse', 'HEAD')[1].strip()
    R['freeze_hash'] = fh_
    open(os.path.join(RUN, 'FREEZE_HASH'), 'w').write(fh_ + '\n')
    # step 5 preflight (after the freeze, 0 calls)
    rc, out = sh(['python3', runner, '--preflight', '--data-dir', DATA], cwd=RUN)
    pf = jload(os.path.join(RUN, 'PREFLIGHT_1U.json'), {})
    R['preflight'] = {k: pf.get(k) for k in (
        'n_items', 'l2_firings', 'l3_eligible', 'ag_rejected_before_l3',
        'reach_l3_planned_calls', 'unique_requests', 'PLANNED_CALLS', 'counted_ledger_dev', 'cap',
        'chk', 'ag')}
    R['preflight']['exit'] = rc
    save_state()
    if rc != 0:
        return stop('STOP: preflight (step 5) stopped, 0 model calls')
    if not pf.get('l3_eligible'):
        return stop('STOP: L3-eligible 0, 0 model calls')
    if (pf.get('ag') or {}).get('errors'):
        return stop('STOP: the stack raised AG errors on %s items, 0 model calls'
                    % pf['ag']['errors'])
    if (pf.get('PLANNED_CALLS') or 0) > CAP_RUN:
        return stop('STOP: planned %s calls > run cap %d, 0 calls' % (pf.get('PLANNED_CALLS'),
                                                                      CAP_RUN))
    with open(os.path.join(RUN, 'FREEZE_1W.txt'), 'w') as fh:
        fh.write(fh_ + '\n')
        for f in open(os.path.join(RUN, 'FREEZE_FILES')).read().split('\n'):
            if f and not f.startswith('#'):
                fh.write('%s %s\n' % (git('hash-object', f)[1].strip(), f))
    git('add', 'translation-offline/phase1w')
    rc_d, _ = git('diff', '--cached', '--quiet', '--', 'translation-offline/phase1w')
    if rc_d != 0:
        git('commit', '-m', 'Phase 1W §4: RUN commit (FREEZE_HASH, preflight, freeze manifest)\n\n'
            + COAUTH, '--', 'translation-offline/phase1w')
    R['run_commit'] = git('rev-parse', 'HEAD')[1].strip()
    open(os.path.join(RUN, 'RUN_COMMIT'), 'w').write(R['run_commit'] + '\n')
    save_state()
    # --final ONCE
    R['final_started'] = datetime.datetime.now().isoformat(timespec='seconds')
    save_state()
    rc, out = sh(['python3', runner, '--final', '--data-dir', DATA], cwd=RUN)
    R['final_exit'] = rc
    R['final_tail'] = out.strip().splitlines()[-6:]
    done = os.path.exists(os.path.join(RUN, 'FINAL_RUN_DONE'))
    if not done and os.path.exists(os.path.join(RUN, 'calls.jsonl')) and rc != 3:
        R['notes'].append('the run CRASHED (exit %d); rows recomputed from the stored verdicts '
                          'with score_1u.py --recover (0 calls)' % rc)
        R['crashed'] = True
        sh(['python3', os.path.join(RUN, 'score_1u.py'), '--recover', '--data-dir', DATA], cwd=RUN)
    elif rc == 3:
        R['notes'].append('the run PAUSED (quota wall); not resumed by the driver')
    save_state()
    if os.path.exists(os.path.join(RUN, 'results_1u.json')):
        rc, out = sh(['python3', os.path.join(RUN, 'score_1u.py'), '--data-dir', DATA], cwd=RUN)
        R['score_exit'] = rc
    return True


def stop(msg):
    R['status'] = msg
    say(msg)
    save_state()
    return False


# ------------------------------------------------------------------ result file
def fk(d):
    try:
        if not d or not d.get('n'):
            return 'n = 0'
        return '%d/%d = %.2f %% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'], d['ci'][0], d['ci'][1])
    except Exception:
        return json.dumps(d)


def tg(d):
    t = (d or {}).get('target') or {}
    return '' if not t else ' - target %s: point %s, interval %s' % (t.get('rule'), t.get('point'),
                                                                      t.get('interval'))


def flat(prefix, obj, out, depth=0):
    if isinstance(obj, dict) and 'k' in obj and 'n' in obj:
        out.append('- %s: %s' % (prefix, fk(obj)))
    elif isinstance(obj, dict) and depth < 4:
        for k in sorted(obj, key=str):
            flat('%s %s' % (prefix, k), obj[k], out, depth + 1)
    elif isinstance(obj, (int, float, str, bool)) or obj is None:
        out.append('- %s: %s' % (prefix, obj))


def calls_stats():
    p = os.path.join(RUN, 'calls.jsonl')
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    ok = [r for r in rows if r.get('http') == 200]
    failed = [r for r in ok if r.get('empty') or r.get('verdict') not in ('SAME', 'TIP', 'DIFF')]
    tin = sum((r.get('prompt_tokens') or 0) for r in ok)
    tout = sum((r.get('candidates_tokens') or 0) for r in ok)
    return {'lines': len(rows), 'counted_http200': len(ok),
            'uncounted_retries': sum(1 for r in rows if r.get('http') != 200),
            'uncounted_by_http': dict(collections.Counter(str(r.get('http')) for r in rows
                                                          if r.get('http') != 200)),
            'failed_empty_or_unparsable_200': len(failed), 'tokens_in': tin, 'tokens_out': tout,
            'models': dict(collections.Counter(r.get('model') for r in ok)),
            'spend_usd_list_price': round(tin * 0.10e-6 + tout * 0.40e-6, 5)}


def write_result():
    L = ['# Phase 1W §4 result: fresh set A4 %s' % (
        'OPENED ONCE' + (' (CRASH, recomputed from stored verdicts)' if R.get('crashed') else '')
        if R.get('final_started') else 'NOT OPENED'), '',
        '- Status: %s' % (R.get('status') or 'completed')]
    L += ['- Note: %s' % n for n in R['notes']]
    L += ['- Stack: phase1w/stack_1w.py = 1V round 2 + §2 (reader_nom, variant full); §3 REVERTED, '
          'L3 prompt P-FROZEN-1U unchanged',
          '- Tooling: phase1v/trackA_set copied to phase1w/a4/set (.py byte-identical; .md paths '
          'repointed); 1U runner/loader/scorer copied to phase1w/a4/run with one stack patch '
          '(AG primary = stack_1w.decide, rows re-scored with stack_1w.final_accept, cap 800), '
          'TASKA path -> phase1u/taskA, and S7 added to the scorer (declared in 1V)',
          '- selftest_1v (on a throwaway copy): %s' % json.dumps(R.get('selftest_1v')), '',
          '## Headless sessions (harness usage, bundled binary, --output-format json, '
          '--max-turns 12, --model opus)', '']
    for s in R['sessions']:
        L.append('- %s: exit %s, is_error %s, turns %s, input %s, cache_creation %s, cache_read %s, '
                 'output %s, cost_usd %s, duration_ms %s, permission_denials %s, models %s'
                 % (s['session'], s['exit'], s['is_error'], s['num_turns'], s['input_tokens'],
                    s['cache_creation_input_tokens'], s['cache_read_input_tokens'],
                    s['output_tokens'], s['total_cost_usd'], s['duration_ms'],
                    s['permission_denials'], s['models']))
    L.append('- judge sessions used: %d' % sum(1 for s in R['sessions']
                                               if s['session'].startswith('judge')))
    L += ['', '## Set build', '']
    for k, v in (R.get('assemble') or {}).items():
        L.append('- assemble %s: %s' % (k, json.dumps(v, ensure_ascii=False)))
    for k, v in (R.get('packets') or {}).items():
        L.append('- packets %s: %s' % (k, json.dumps(v)))
    for k, v in (R.get('join') or {}).items():
        L.append('- join %s: %s' % (k, json.dumps(v)))
    L += ['', '## Floors on JUDGED counts (F1-F6)', '']
    for k, v in (R.get('floors') or {}).items():
        L.append('- %s: %s' % (k, json.dumps(v)))
    L += ['', '## Freeze / chmod / preflight', '',
          '- FREEZE hash: %s' % R.get('freeze_hash'),
          '- RUN commit: %s' % R.get('run_commit'),
          '- chmod: %s dirs made read-only BEFORE the run; %s'
          % ((R.get('chmod') or {}).get('dirs'), (R.get('chmod') or {}).get('write_test'))]
    L += ['- chmod stat: %s' % x for x in (R.get('chmod') or {}).get('stat', [])]
    for k, v in (R.get('preflight') or {}).items():
        L.append('- preflight %s: %s' % (k, json.dumps(v)))
    if R.get('preflight_stop'):
        L.append('- preflight stop output: %s' % R['preflight_stop'].replace('\n', ' | ')[-800:])
    cs = calls_stats()
    L += ['', '## Model calls (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0)', '',
          '- final started: %s; runner exit %s; FINAL_RUN_DONE %s'
          % (R.get('final_started'), R.get('final_exit'),
             os.path.exists(os.path.join(RUN, 'FINAL_RUN_DONE')))]
    L += ['- %s: %s' % (k, json.dumps(v)) for k, v in cs.items()]
    L += ['- phase total counted (194 §3 + this run): %d of the 1,200 hard cap'
          % (194 + cs['counted_http200']),
          '- access log (verbatim): phase1w/a4/run/access_log.jsonl; call log: '
          'phase1w/a4/run/calls.jsonl']
    L += ['- runner tail: %s' % x for x in (R.get('final_tail') or [])]
    sc = jload(os.path.join(RUN, 'score_1u.json'))
    if sc:
        L += ['', '## Headline and sensitivities S1-S7 (pooled / P1 / P2, exact Clopper-Pearson '
              '95 %; coverage >= 90 %, FA < 5 %)', '']
        for name, blk in sc.items():
            if not (name == 'headline' or re.match(r'S\d', name)) or not isinstance(blk, dict):
                continue
            for h in ('pooled', 'P1', 'P2'):
                for m in ('coverage', 'fa'):
                    d = (blk.get(h) or {}).get(m)
                    L.append('- %s %s %s: %s%s' % (name, h, m, fk(d), tg(d)))
            for m, pv in (blk.get('fisher_P1_vs_P2') or {}).items():
                L.append('- %s Fisher P1 vs P2 %s: p = %s' % (name, m, pv))
            if name != 'headline':
                L.append('- %s items moved: %s' % (name, blk.get('n_moved')))
        if sc.get('SENSITIVITY_EMPTY'):
            L.append('- SENSITIVITY_EMPTY: %s' % sc['SENSITIVITY_EMPTY'])
        L += ['', '## Every cell, one per line (headline labels)', '']
        flat('cell', sc.get('cells'), L)
        L += ['', '## AG block', '']
        flat('ag', sc.get('ag'), L)
        L += ['', '## Model block', '']
        flat('model', sc.get('model'), L)
        L.append('- failed calls (detail): %s' % json.dumps(((sc.get('detail') or {})
                                                             .get('failed_calls')))[:600])
    open(os.path.join(W, 'S4_RESULT.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    say('S4_RESULT.md written')


def main():
    old = jload(STATE)
    if old:
        R.update(old)
        R['status'] = None
    setup()
    try:
        if stage_a():
            stage_b()
    except Exception as e:
        import traceback
        R['status'] = 'DRIVER EXCEPTION: %s' % e
        say(traceback.format_exc())
    save_state()
    write_result()


if __name__ == '__main__':
    main()
