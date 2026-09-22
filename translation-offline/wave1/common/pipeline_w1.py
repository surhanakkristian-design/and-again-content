#!/usr/bin/env python3
"""Wave 1 per-language pipeline (de / ua / es -> English).  Every subcommand is its own process; chain_w1.sh runs them.
  partA        SELECT only: full_sentence of the 4,064 translation_selected_exercises for the language (+ level, topic);
               data findings (empty, duplicated, English text, wrong language, truncated)      -> <lang>/partA/
  rw_pass1     Part B (ua, es): headless Claude rewrite, ONE subject pronoun where the verb implies a dropped subject;
               machine check (tokens new = tokens old + exactly the pronoun; punctuation unchanged)  -> <lang>/partB/
  rw_pass2     Part B: an independent headless pass checks every changed sentence (only a pronoun added, meaning
               unchanged, grammatical)
  rw_final     Part B: final rewritten file (change kept only if machine check AND pass 2 agree) + counts + examples
  projection   Part D token projection from 2L's actual use; STOP before any Part D session if over the budget
  make_set     100 sentences (25/level) from the 4,064 (rewritten versions for ua/es), exercise_ids used in earlier sets
               excluded (preferred), the three wave-1 languages disjoint (positions mod 3 of one seeded order)
  mock         the whole headless Part D path with a scripted spawner (0 cost)       -> <lang>/partD/_mock
  writers      4 blind writer sessions (one per level; they see wid / source / level / topic only)
  packets      4 judge packets (jid / source / level / answer / topic), 80 hidden duplicates in different sessions
  judges       4 judge sessions, ONE prompt, cap 400,000 tokens each
  labels       judge labels (originals) + duplicate-control agreement
  build_items  stack items WITHOUT any label / reference field (+ truth.jsonl kept apart) + poison check
  gemini       opens <lang>/partD/set/items.jsonl ONCE and runs stack_w1.run_full (Gemini: counted = HTTP 200 only)
  post         FINAL_RUN_DONE, ACCESS_LOG_VERBATIM.md, analysis (exact CP 95 %), 0 calls
Headless spawner = byte copy of phase2j/run_2j.py (bundled binary, token via `zsh -ic`, never printed; usage-limit
envelope -> hard stop; rate limit only from the envelope; finished sessions resume at 0 cost).
Decision 26 (22 Sept 2026): NO headless CLI sessions.  Every writer / judge session is an Opus SUBAGENT of the main
session (transport `subagent`, sub_session below): the pipeline writes <session dir>/prompt.txt and PENDING.json and
exits 6; the main session spawns one blind subagent per pending session, which reads ONLY prompt.txt and writes
reply.txt; the main session records the subagent's reported tokens in tokens.json; the next run of the same
subcommand ingests the reply (same ledger, validation, one retry `_r1`, resume at 0 cost, token caps).
  partA_live   SELECT only: the LIVE full_sentence of the 4,064 (Parts A/B done in the database, decision 26) -> <lang>/partA_live/
               Part D sets are built from this snapshot for every language (no rewritten.jsonl)."""
import argparse, glob, hashlib, json, math, os, random, re, subprocess, sys, threading, time, types
from collections import Counter, defaultdict
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import prompts_w1 as P   # noqa: E402
import stack_w1 as S     # noqa: E402
import run_2j as R       # noqa: E402
TOFF = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline'
W1 = TOFF + '/wave1'
APP = '/Users/kristiansurhanak/Projects/and-again'
SB = os.path.expanduser('~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase')
LEVELS = ['A1', 'A2', 'B1', 'B2']
TYPES = ['T', 'W', 'M', 'S']
SHIFT = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 1}
SEED, JSEED = 20261001, 20261002
LANG_ORDER = ['de', 'ua', 'es']            # position mod 3 in the shared seeded order
BUDGET_LANG = 1300000                      # Claude tokens per language (brief: about 1,300,000)
AGENT_EST = 250000                         # the language agent's own context (estimate, reserved)
HEADLESS_CAP = BUDGET_LANG - AGENT_EST     # every headless session of this language together
JUDGE_CAP = 400000
REFK = S.REF_KEYS
FORBID = set(REFK) | {'judge_label', 'judge_reason', 'judge_session', 'writer_intent', 'writer_type', 'writer_agent_drop',
                      'label', 'old_src', 'original'}
PRON = {'ua': ['я', 'ти', 'він', 'вона', 'воно', 'ми', 'ви', 'вони'],
        'es': ['yo', 'tú', 'él', 'ella', 'usted', 'nosotros', 'nosotras', 'vosotros', 'vosotras', 'ellos', 'ellas',
               'ustedes']}
RW_CHUNKS = {'ua': 3, 'es': 3}
TRANSPORT = 'subagent'                     # decision 26: no headless CLI; R.run_session is no longer called
SUB_FAKE = [None]                          # mock / test hook: prompt -> (reply_text, tokens), stands in for the subagent
RW2_CHUNKS = 3
L = {}


def setlang(lang):
    if lang not in P.LANG:
        raise SystemExit('REFUSED: language %r' % lang)
    L.update(lang=lang, name=P.LANG[lang], dir=W1 + '/' + lang, A=W1 + '/' + lang + '/partA', B=W1 + '/' + lang + '/partB',
             D=W1 + '/' + lang + '/partD')
    for k in ('dir', 'A', 'B', 'D'):
        os.makedirs(L[k], exist_ok=True)


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


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def tokens_md(line):
    with open(L['dir'] + '/TOKENS.md', 'a', encoding='utf-8') as f:
        f.write(line.rstrip('\n') + '\n')


def spent(base=None):
    base = base or L['dir']
    return sum(int(v.get('tokens') or 0) for p in glob.glob(base + '/**/sessions/*/headless_ledger.json', recursive=True)
               if '/_mock' not in p for v in json.load(open(p)).values())


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


# ------------------------------------------------------------------ Part A (SELECT only)
def sb_rows(sql):
    p = subprocess.run([SB, 'db', 'query', '--linked', '-o', 'json', sql], capture_output=True, text=True, cwd=APP,
                       timeout=600)
    if p.returncode != 0:
        raise SystemExit('query failed: %s' % p.stderr[-800:])
    d = json.loads(p.stdout)
    rows = d.get('rows') if isinstance(d, dict) else d
    assert isinstance(rows, list)
    return rows


def is_select(sql):
    s = re.sub(r'\s+', ' ', sql.strip().lower())
    return s.startswith(('select ', 'with ')) and not re.search(r'\b(insert|update|delete|alter|drop|create|grant|truncate)\b', s)


EN_STOP = {'the', 'and', 'is', 'are', 'was', 'were', 'with', 'of', 'to', 'you', 'he', 'she', 'it', 'they', 'this', 'that',
           'have', 'has', 'will', 'his', 'her', 'in', 'on', 'for', 'a'}
RU_ONLY = re.compile('[ыэёъЫЭЁЪ]')
UA_ONLY = re.compile('[іїєґІЇЄҐ]')
CYR = re.compile('[А-Яа-яІіЇїЄєҐґ]')
LATIN = re.compile('[A-Za-z]{3,}')
NOT_DE = re.compile('[ñ¿¡áéíóúàèìòùçœ]', re.I)
NOT_ES = re.compile('[äöüßœ]', re.I)
TERM = re.compile(r'[.!?…"»”\')]\s*$')


def cmd_partA(a):
    lang = L['lang']
    sql = ("select t.exercise_id, t.level, e.exercise_type_id, e.concept_id, et.title->>'en' as topic, "
           "el.id as loc_id, el.full_sentence, en.full_sentence as en_full_sentence "
           "from translation_selected_exercises t join exercises e on e.id = t.exercise_id "
           "join exercise_types et on et.id = e.exercise_type_id "
           "left join exercise_localizations el on el.exercise_id = t.exercise_id and el.language_code = '%s' "
           "left join exercise_localizations en on en.exercise_id = t.exercise_id and en.language_code = 'en' "
           "order by t.exercise_id" % lang)
    assert is_select(sql)
    rows = sb_rows(sql)
    cnt = sb_rows("select count(*) n, count(distinct exercise_id) d from exercise_localizations where language_code = '%s' "
                  "and exercise_id in (select exercise_id from translation_selected_exercises)" % lang)[0]
    assert len(rows) == 4064 and len({r['exercise_id'] for r in rows}) == 4064, len(rows)
    en_of = {r['exercise_id']: r.pop('en_full_sentence') for r in rows}
    data = [{'exercise_id': int(r['exercise_id']), 'level': r['level'], 'exercise_type_id': r['exercise_type_id'],
             'concept_id': r['concept_id'], 'topic': r['topic'], 'loc_id': r['loc_id'], 'src': r['full_sentence']} for r in rows]
    h = wjl(L['A'] + '/rows.jsonl', data)
    by_text = defaultdict(list)
    for r in data:
        if r['src'] and r['src'].strip():
            by_text[r['src'].strip()].append(r['exercise_id'])
    F = defaultdict(list)
    for r in data:
        s, eid, en = (r['src'] or ''), r['exercise_id'], (en_of.get(r['exercise_id']) or '')
        t = s.strip()
        if r['loc_id'] is None:
            F['no_row'].append(eid); continue
        if not t:
            F['empty'].append(eid); continue
        if t != s:
            F['leading_trailing_space'].append(eid)
        if en and t.lower() == en.strip().lower():
            F['identical_to_english'].append(eid)
        words = re.findall(r"[^\W\d_]+", t.lower())
        ens = [w for w in words if w in EN_STOP]
        if len(words) >= 3 and len(set(ens)) >= 3 and len(ens) / len(words) >= 0.3:
            F['looks_english'].append(eid)
        if lang == 'ua':
            if not CYR.search(t): F['no_cyrillic'].append(eid)
            if RU_ONLY.search(t): F['russian_letters'].append(eid)
            if LATIN.search(t): F['latin_word_in_ukrainian'].append(eid)
        if lang == 'de' and NOT_DE.search(t): F['foreign_letters'].append(eid)
        if lang == 'es':
            if NOT_ES.search(t): F['foreign_letters'].append(eid)
            if t.count('¿') != t.count('?'): F['unbalanced_question_marks'].append(eid)
            if t.count('¡') != t.count('!'): F['unbalanced_exclamation_marks'].append(eid)
        if CYR.search(t) and lang != 'ua': F['cyrillic_in_latin_language'].append(eid)
        if not TERM.search(t): F['no_final_punctuation'].append(eid)
        if re.search(r'(\.\.\.|…|___|\?\?|\s[,;:]\s*$|,\s*$)', t): F['ellipsis_or_gap_or_trailing_comma'].append(eid)
        if en and len(t) < 0.5 * len(en.strip()): F['much_shorter_than_english'].append(eid)
        if '  ' in t: F['double_space'].append(eid)
    dups = {k: v for k, v in by_text.items() if len(v) > 1}
    for v in dups.values():
        F['duplicated_text'].extend(v)
    txt = {r['exercise_id']: r['src'] for r in data}
    out = {'lang': lang, 'rows': len(data), 'rows_sha256': h, 'db_count': cnt, 'per_level': dict(Counter(r['level'] for r in data)),
           'counts': {k: len(v) for k, v in sorted(F.items())}, 'duplicate_groups': len(dups),
           'findings': {k: [{'exercise_id': e, 'src': txt.get(e), 'en': en_of.get(e) if k in (
               'identical_to_english', 'looks_english', 'much_shorter_than_english') else None} for e in v] for k, v in sorted(F.items())},
           'sql': sql, 'select_only': True, 'ts': now()}
    wj(L['A'] + '/partA.json', out)
    md = ['# Wave 1 Part A - %s data (SELECT only)' % P.LANG[lang], '',
          '%d rows for the 4,064 translation_selected_exercises (language_code %s); DB count %s. Per level %s. Nothing was fixed.' % (
              len(data), lang, cnt, out['per_level']), '', '| finding | rows |', '|---|---:|'] + \
         ['| %s | %d |' % (k, len(v)) for k, v in sorted(F.items())] + ['', 'Duplicate text groups: %d' % len(dups), '']
    for k, v in sorted(F.items()):
        md += ['## %s (%d)' % (k, len(v)), '']
        for e in v[:400]:
            md.append('- %s: %s%s' % (e, txt.get(e), ('  [en: %s]' % en_of.get(e)) if k in (
                'identical_to_english', 'looks_english', 'much_shorter_than_english') else ''))
        if len(v) > 400:
            md.append('- ... %d more in partA.json' % (len(v) - 400))
        md.append('')
    open(L['A'] + '/partA.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(json.dumps({'rows': len(data), 'counts': out['counts']}, ensure_ascii=False))
    return 0


# ------------------------------------------------------------------ headless helpers (2L recipe)
def extract_array(text):
    t = (text or '').strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m: t = m.group(1).strip()
    i, j = t.find('['), t.rfind(']')
    if i < 0 or j < i: raise ValueError('no array')
    return json.loads(t[i:j + 1])


def run_group(kind, jobs, base, stop_dir, est, max_turns, cap_session, spent_base=None):
    """jobs: {key: (prompt, validate_fn)} -> results {key: {...}}; threads; reservation against HEADLESS_CAP."""
    lock, inflight, results = threading.Lock(), {}, {}
    spent_base = spent_base or L['dir']

    def worker(key, prompt, vfn):
        atts = []
        for n, sid in enumerate((key, key + '_r1', key + '_r2')):
            # _r2 (22 Sept 2026, added after de/ua had finished): a third attempt ONLY when both earlier replies failed
            # on the jid set alone (es judge s4: two sessions each dropped the same one of 245 items).
            if n == 2 and not all(str(x['why']).startswith('jid set mismatch') for x in atts):
                break
            sd = os.path.join(base, kind, 'sessions', sid)
            d0 = R.read_json(os.path.join(sd, sid + '.json'), None)
            done = bool(d0 and d0.get('status') == 'ok')
            with lock:
                if not done and spent(spent_base) + sum(inflight.values()) + est > HEADLESS_CAP:
                    results[key] = {'ok': False, 'stop': 'token_cap', 'why': 'language headless reservation cap %d' % HEADLESS_CAP, 'attempts': atts}
                    return
                inflight[sid] = 0 if done else est
            try:
                d = sub_session(sid, prompt, sd, token_cap=cap_session, est=est)
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


def sub_session(sid, prompt, out_dir, token_cap=None, est=100000):
    """Subagent transport (decision 26).  Same contract as R.run_session: returns {'status': 'ok', 'result', 'tokens',
    ...} or raises R.Stop.  Missing reply -> writes prompt.txt + PENDING.json and raises Stop('pending')."""
    out_dir = os.path.abspath(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    f = os.path.join(out_dir, '%s.json' % sid)
    d = R.read_json(f, None)
    if d and d.get('status') == 'ok':
        return dict(d, resumed=True, spawns=0)
    led = os.path.join(out_dir, 'headless_ledger.json')
    Lg = R.read_json(led, {})
    used = sum(int(v.get('tokens') or 0) for v in Lg.values())
    if token_cap is not None and used + est > token_cap:
        raise R.Stop('token_cap', 'used %d + reservation %d > cap %d' % (used, est, token_cap))
    pp, rp, tp = (os.path.join(out_dir, x) for x in ('prompt.txt', 'reply.txt', 'tokens.json'))
    if os.path.exists(pp) and open(pp, encoding='utf-8').read() != prompt:
        raise R.Stop('headless_failed', 'session %s: prompt.txt differs from the prompt of this run' % sid)
    if not os.path.exists(pp):
        open(pp, 'w', encoding='utf-8').write(prompt)
    if SUB_FAKE[0] is not None and not os.path.exists(rp):
        txt, tk = SUB_FAKE[0](prompt)
        open(rp, 'w', encoding='utf-8').write(txt)
        R.write_json(tp, {'total_tokens': tk, 'agent': 'SUB_FAKE (mock)'})
    if not (os.path.exists(rp) and os.path.exists(tp)):
        R.write_json(os.path.join(out_dir, 'PENDING.json'), {'sid': sid, 'prompt': pp, 'reply': rp, 'tokens': tp, 'est': est,
                                                             'ts': now()})
        raise R.Stop('pending', 'session %s waits for its subagent (%s)' % (sid, rp))
    tk = R.read_json(tp, {})
    tok = int(tk.get('total_tokens') or 0)
    Lg['%s#sub' % sid] = {'tokens': tok, 'kind': 'ok', 'ts': now(), 'secs': tk.get('secs'), 'agent': tk.get('agent'),
                          'transport': 'subagent'}
    R.write_json(led, Lg)
    d = {'sid': sid, 'status': 'ok', 'result': open(rp, encoding='utf-8').read(), 'tokens': tok, 'usage': tk,
         'num_turns': tk.get('tool_uses'), 'attempts': 1, 'model': 'opus (subagent)', 'ts': now()}
    R.write_json(f, d)
    if os.path.exists(os.path.join(out_dir, 'PENDING.json')):
        os.remove(os.path.join(out_dir, 'PENDING.json'))
    return dict(d, spawns=1)


def handle_fail(results, stop_root, stage):
    bad = {k: r for k, r in results.items() if not r['ok']}
    if not bad:
        return 0
    kinds = {r.get('stop') for r in bad.values()}
    msg = '%s: %s' % (stage, {k: (r.get('stop'), r.get('why')) for k, r in bad.items()})
    if kinds == {'pending'}:
        print('PENDING', json.dumps({k: r.get('why') for k, r in bad.items()}))
        return 6
    if 'usage_limit' in kinds:
        open(stop_root + '/STOP_quota.md', 'w').write('# STOP quota / usage limit (%s)\n\n%s\n' % (L['lang'], msg)); return 4
    if kinds & {'headless_auth', 'headless_failed', 'headless_timeout'}:
        open(stop_root + '/STOP_headless.md', 'w').write('# STOP headless session failed\n\n%s\n' % msg); return 4
    if 'judge_cap' in kinds or 'token_cap' in kinds:
        open(stop_root + '/STOP_tokencap.md', 'w').write('# STOP token cap\n\n%s\n' % msg); return 4
    open(stop_root + '/STOP_invalid_%s.md' % stage, 'w').write('# STOP invalid output after one retry\n\n%s\n' % msg); return 3


def append_tokens(base, kind):
    for p in sorted(glob.glob(base + '/%s/sessions/*/headless_ledger.json' % kind)):
        for k, v in json.load(open(p)).items():
            tokens_md('- %s %s: %s tokens (%s, %ss)' % (kind, k, format(int(v.get('tokens') or 0), ','), v.get('kind'), v.get('secs')))
    tokens_md('- %s cumulative headless (this language) after %s: %s' % (now(), kind, format(spent(), ',')))


def token_login():
    if TRANSPORT == 'subagent':
        return 0                            # decision 26: no headless CLI, no OAuth token needed
    os.environ['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] = '64000'
    try:
        R.load_token()
    except R.Stop as e:
        open(L['dir'] + '/STOP_spawn.md', 'w').write('# STOP spawn\nOAuth token absent (%s); 0 sessions spawned, 0 cost.\n' % e.kind)
        return 4
    return 0


# ------------------------------------------------------------------ Part B (ua, es): explicit-subject rewrite
def rw_prompt1(lang):
    name, pr = P.LANG[lang], PRON[lang]
    return (
        "You are the arm-B rewrite agent of a %(n)s->English translation-checking pipeline. Do not use any tools. Reply with JSON only.\n\n"
        "For each %(n)s sentence below: if the MAIN clause drops a subject that its finite verb implies (pro-drop), insert "
        "exactly ONE nominative subject pronoun (%(p)s) agreeing with that verb, at the natural position for %(n)s. "
        "If the main clause already has an overt subject but a subordinate clause drops one, you may insert the pronoun "
        "there instead. Change NOTHING else: no other word added, removed, reordered or altered, no punctuation change; "
        "only the capital letter moves if the pronoun becomes the first word. Leave the sentence untouched when the subject "
        "is overt, when the clause is impersonal or has no subject (weather, existence, impersonal/reflexive-impersonal "
        "forms, 'one must', a passive without an agent), when the verb is an imperative, or when there is no finite verb.\n"
        "If the subject's person or gender is ambiguous from the sentence alone (e.g. a 3rd-person form that could be he, "
        "she or formal you), choose the reading the sentence most naturally has and FLAG it with a reason of at most 8 words.\n"
        "A machine check follows: the new sentence must equal the old one plus exactly the pronoun.\n\n"
        "Output: ONE JSON array containing an object ONLY for each sentence you CHANGED, exactly this shape:\n"
        '[{"id": 123, "new": "<the full new sentence>"}, {"id": 456, "new": "...", "flag": "<why ambiguous>"}]\n'
        "Omit the \"flag\" key when the choice is clear. Sentences you leave untouched are simply not listed.\n\n"
        "Sentences (one JSON object per line: id, sentence):\n") % {'n': name, 'p': '/'.join(pr)}


def rw_prompt2(lang):
    name = P.LANG[lang]
    return (
        "You are an independent second-pass checker of %(n)s sentences. Do not use any tools. Reply with JSON only.\n\n"
        "Each line below has an id, an ORIGINAL %(n)s sentence and a NEW version into which another agent inserted one "
        "subject pronoun (%(p)s) because the original dropped the subject the verb implies. For each item decide: is the "
        "NEW sentence acceptable? It is acceptable only if ALL hold: (1) exactly one subject pronoun was added and nothing "
        "else changed except the capital letter of the first word; (2) the pronoun agrees with the verb in person and "
        "number (and gender where the sentence shows it) and is the natural reading of the original; (3) the meaning is "
        "unchanged; (4) the new sentence is grammatical, natural %(n)s.\n\n"
        "Output: ONE JSON array with exactly one object per item, every id exactly once, exactly this shape:\n"
        '[{"id": 123, "ok": true}, {"id": 456, "ok": false, "why": "<at most 10 words>"}]\n\n'
        "Items:\n") % {'n': name, 'p': '/'.join(PRON[lang])}


def toks(s):
    return [w.lower() for w in re.findall(r'\w+', s or '')]


def punct(s):
    return re.sub(r'\s+', '', re.sub(r'\w+', '', s or ''))


def machine_check(lang, old, new):
    """(ok, pronoun, why): tokens(new) = tokens(old) + exactly one allowed pronoun; punctuation identical; the only
    case change allowed is the first word's capital."""
    if not isinstance(new, str) or not new.strip():
        return False, None, 'empty new'
    a, b = toks(old), toks(new)
    rest = list(b)
    for t in a:
        if t in rest:
            rest.remove(t)
        else:
            return False, None, 'old token %r missing' % t
    if len(rest) != 1:
        return False, None, 'added tokens %r' % rest
    if rest[0] not in PRON[lang]:
        return False, rest[0], 'added %r is not an allowed pronoun' % rest[0]
    if punct(old) != punct(new):
        return False, rest[0], 'punctuation changed'
    wo, wn = re.findall(r'\w+', old), re.findall(r'\w+', new)
    lo = [w.lower() for w in wo]
    ks = [k for k in range(len(wn)) if wn[k].lower() == rest[0] and [w.lower() for w in wn[:k] + wn[k + 1:]] == lo]
    if not ks:
        return False, rest[0], 'word order changed'
    stripped = wn[:ks[0]] + wn[ks[0] + 1:]
    diffcase = [i for i, (x, y) in enumerate(zip(stripped, wo)) if x != y]
    if any(i != 0 for i in diffcase) or (diffcase and ks[0] != 0):
        return False, rest[0], 'case changed'
    if ks[0] == 0 and stripped and stripped[0][:1].isupper() and not stripped[0].isupper():
        return False, rest[0], 'old first word kept its capital after the pronoun'
    return True, rest[0], None


def rows_for_rewrite():
    rows = jl(L['A'] + '/rows.jsonl')
    return [r for r in rows if (r['src'] or '').strip()]


def cmd_rw_pass1(a):
    lang = L['lang']
    assert lang in PRON
    rc = token_login()
    if rc: return rc
    rows = rows_for_rewrite()
    n = RW_CHUNKS[lang]
    size = int(math.ceil(len(rows) / float(n)))
    chunks = [rows[i:i + size] for i in range(0, len(rows), size)]
    head = rw_prompt1(lang)
    jobs = {}
    for ci, ch in enumerate(chunks, 1):
        ids = {r['exercise_id'] for r in ch}
        prompt = head + '\n'.join(json.dumps({'id': r['exercise_id'], 'sentence': r['src']}, ensure_ascii=False) for r in ch) + '\n'
        open(L['B'] + '/prompt1_c%d.txt' % ci, 'w', encoding='utf-8').write(prompt)

        def vfn(arr, ids=ids):
            if not isinstance(arr, list): return 'not a list'
            seen = set()
            for o in arr:
                if not isinstance(o, dict) or o.get('id') not in ids or not isinstance(o.get('new'), str): return 'bad object %r' % (o,)
                if o['id'] in seen: return 'duplicate id %s' % o['id']
                seen.add(o['id'])
            return None
        jobs['c%d' % ci] = (prompt, vfn)
    res = run_group('pass1', jobs, L['B'], L['dir'], est=120000, max_turns=2, cap_session=None)
    summ = {'prompt_sha': hashlib.sha256(head.encode()).hexdigest(), 'chunks': len(chunks), 'rows': len(rows),
            'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()}}
    wj(L['B'] + '/PASS1_SUMMARY.json', summ)
    append_tokens(L['B'], 'pass1')
    rc = handle_fail(res, L['dir'], 'rw_pass1')
    if rc: return rc
    by = {r['exercise_id']: r for r in rows}
    out = []
    for k in sorted(res, key=lambda x: int(x[1:])):
        for o in res[k]['arr']:
            old = by[o['id']]['src']
            ok, pr, why = machine_check(lang, old, o['new'])
            out.append({'exercise_id': o['id'], 'level': by[o['id']]['level'], 'old': old, 'new': o['new'],
                        'flag': o.get('flag'), 'pronoun': pr, 'machine_ok': ok, 'machine_why': why, 'chunk': k})
    wjl(L['B'] + '/pass1.jsonl', out)
    print(json.dumps({'changed_proposed': len(out), 'machine_ok': sum(o['machine_ok'] for o in out),
                      'flagged': sum(1 for o in out if o['flag']), 'headless_tokens': spent()}))
    return 0


def cmd_rw_pass2(a):
    lang = L['lang']
    rc = token_login()
    if rc: return rc
    p1 = [r for r in jl(L['B'] + '/pass1.jsonl') if r['machine_ok']]
    n = max(1, min(RW2_CHUNKS, int(math.ceil(len(p1) / 400.0))))
    size = int(math.ceil(len(p1) / float(n))) if p1 else 1
    chunks = [p1[i:i + size] for i in range(0, len(p1), size)]
    head = rw_prompt2(lang)
    jobs = {}
    for ci, ch in enumerate(chunks, 1):
        ids = [r['exercise_id'] for r in ch]
        prompt = head + '\n'.join(json.dumps({'id': r['exercise_id'], 'original': r['old'], 'new': r['new']}, ensure_ascii=False)
                                  for r in ch) + '\n'
        open(L['B'] + '/prompt2_c%d.txt' % ci, 'w', encoding='utf-8').write(prompt)

        def vfn(arr, ids=ids):
            if not isinstance(arr, list): return 'not a list'
            got = [o.get('id') if isinstance(o, dict) else None for o in arr]
            if len(got) != len(set(got)) or set(got) != set(ids): return 'id set mismatch (missing %d, extra %d)' % (
                len(set(ids) - set(got)), len(set(got) - set(ids)))
            if any(not isinstance(o.get('ok'), bool) for o in arr): return 'bad ok'
            return None
        jobs['c%d' % ci] = (prompt, vfn)
    res = run_group('pass2', jobs, L['B'], L['dir'], est=100000, max_turns=2, cap_session=None)
    wj(L['B'] + '/PASS2_SUMMARY.json', {'prompt_sha': hashlib.sha256(head.encode()).hexdigest(), 'items': len(p1),
                                        'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()}})
    append_tokens(L['B'], 'pass2')
    rc = handle_fail(res, L['dir'], 'rw_pass2')
    if rc: return rc
    v = {}
    for r in res.values():
        for o in r['arr']:
            v[o['id']] = {'ok': o['ok'], 'why': o.get('why')}
    wjl(L['B'] + '/pass2.jsonl', [dict(id=k, **x) for k, x in sorted(v.items())])
    print(json.dumps({'checked': len(v), 'disagree': sum(1 for x in v.values() if not x['ok'])}))
    return 0


def cmd_rw_final(a):
    lang = L['lang']
    rows = jl(L['A'] + '/rows.jsonl')
    p1 = {r['exercise_id']: r for r in jl(L['B'] + '/pass1.jsonl')}
    p2 = {r['id']: r for r in jl(L['B'] + '/pass2.jsonl')} if os.path.exists(L['B'] + '/pass2.jsonl') else {}
    out, C = [], Counter()
    for r in rows:
        eid = r['exercise_id']
        x = p1.get(eid)
        st, new = 'unchanged', r['src']
        if x is not None:
            if not x['machine_ok']:
                st = 'machine_check_fail'
            elif not p2.get(eid, {}).get('ok'):
                st = 'pass2_disagree' if eid in p2 else 'pass2_missing'
            else:
                st, new = 'changed', x['new']
        C[st] += 1
        if st == 'changed' and x.get('flag'):
            C['changed_flagged'] += 1
        out.append({'exercise_id': eid, 'level': r['level'], 'loc_id': r['loc_id'], 'old': r['src'], 'new': new,
                    'status': st, 'pronoun': x.get('pronoun') if x else None, 'flag': x.get('flag') if x else None,
                    'pass2_why': (p2.get(eid) or {}).get('why')})
    h = wjl(L['B'] + '/rewritten.jsonl', out)
    by_lv = {lv: dict(Counter(o['status'] for o in out if o['level'] == lv)) for lv in LEVELS}
    pron = Counter(o['pronoun'] for o in out if o['status'] == 'changed')
    rng = random.Random(SEED)
    def ex(st, k=10):
        c = [o for o in out if o['status'] == st]
        return rng.sample(c, min(k, len(c)))
    summ = {'lang': lang, 'rows': len(out), 'counts': dict(C), 'by_level': by_lv, 'pronouns': dict(pron), 'sha256': h,
            'proposed_by_pass1': len(p1), 'pass2_checked': len(p2),
            'examples': {'changed': ex('changed'), 'changed_flagged': rng.sample([o for o in out if o['status'] == 'changed' and o['flag']],
                                                                             min(10, sum(1 for o in out if o['status'] == 'changed' and o['flag']))),
                         'pass2_disagree': ex('pass2_disagree'), 'machine_check_fail': [dict(o, why=p1[o['exercise_id']]['machine_why'], proposed=p1[o['exercise_id']]['new'])
                                                                                      for o in ex('machine_check_fail')],
                         'unchanged': ex('unchanged')},
            'rule': 'final = new only if machine check passed AND pass 2 said ok; otherwise the original stays'}
    wj(L['B'] + '/partB.json', summ)
    md = ['# Wave 1 Part B - %s explicit-subject rewrite' % P.LANG[lang], '',
          'Rows %d; pass 1 proposed %d changes; machine check fail %d; pass 2 checked %d, disagreed %d; FINAL changed %d (flagged %d), unchanged %d.' % (
              len(out), len(p1), C['machine_check_fail'], len(p2), C['pass2_disagree'], C['changed'], C['changed_flagged'], C['unchanged']),
          '', 'By level: %s' % json.dumps(by_lv), '', 'Pronouns: %s' % json.dumps(dict(pron), ensure_ascii=False), '']
    for k, v in summ['examples'].items():
        md += ['## %s (%d examples)' % (k, len(v)), '']
        for o in v:
            md.append('- %s %s: %s -> %s%s%s' % (o['exercise_id'], o['level'], o['old'], o.get('proposed') or o['new'],
                                                  ('  [flag: %s]' % o['flag']) if o.get('flag') else '',
                                                  ('  [why: %s]' % (o.get('why') or o.get('pass2_why'))) if (o.get('why') or o.get('pass2_why')) else ''))
        md.append('')
    open(L['B'] + '/partB.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(json.dumps({k: summ[k] for k in ('counts', 'pronouns')}, ensure_ascii=False))
    return 0


# ------------------------------------------------------------------ Part D
def source_rows():
    """{exercise_id: row with 'src' = the sentence Part D measures (rewritten for ua/es)}"""
    live = L['dir'] + '/partA_live/rows.jsonl'
    if os.path.exists(live):                # decision 26: the LIVE rows (rewrite for ua/es already in the database)
        return {r['exercise_id']: dict(r) for r in jl(live)}
    rows = {r['exercise_id']: dict(r) for r in jl(L['A'] + '/rows.jsonl')}
    if L['lang'] in PRON:
        rw = jl(L['B'] + '/rewritten.jsonl')
        assert len(rw) == len(rows)
        for o in rw:
            rows[o['exercise_id']]['src_original'] = rows[o['exercise_id']]['src']
            rows[o['exercise_id']]['src'] = o['new']
            rows[o['exercise_id']]['rewrite_status'] = o['status']
    return rows


def cmd_partA_live(a):
    """SELECT only.  The live full_sentence of the 4,064 for this language, compared with the Part A snapshot."""
    lang = L['lang']
    sql = ("select t.exercise_id, t.level, e.exercise_type_id, e.concept_id, et.title->>'en' as topic, "
           "el.id as loc_id, el.full_sentence "
           "from translation_selected_exercises t join exercises e on e.id = t.exercise_id "
           "join exercise_types et on et.id = e.exercise_type_id "
           "left join exercise_localizations el on el.exercise_id = t.exercise_id and el.language_code = '%s' "
           "order by t.exercise_id" % lang)
    assert is_select(sql)
    rows = sb_rows(sql)
    assert len(rows) == 4064 and len({r['exercise_id'] for r in rows}) == 4064, len(rows)
    data = [{'exercise_id': int(r['exercise_id']), 'level': r['level'], 'exercise_type_id': r['exercise_type_id'],
             'concept_id': r['concept_id'], 'topic': r['topic'], 'loc_id': r['loc_id'], 'src': r['full_sentence']} for r in rows]
    h = wjl(L['dir'] + '/partA_live/rows.jsonl', data)
    old = {r['exercise_id']: r['src'] for r in jl(L['A'] + '/rows.jsonl')}
    cmp_ = Counter()
    for r in data:
        o, n = (old.get(r['exercise_id']) or '').strip(), (r['src'] or '').strip()
        cmp_['empty_live' if not n else 'was_empty_now_filled' if not o else 'unchanged' if o == n else 'changed'] += 1
    meta = {'lang': lang, 'rows': len(data), 'sha256': h, 'per_level': dict(Counter(r['level'] for r in data)),
            'filled_per_level': dict(Counter(r['level'] for r in data if (r['src'] or '').strip())),
            'vs_partA_snapshot': dict(cmp_), 'sql': sql, 'select_only': True, 'ts': now()}
    wj(L['dir'] + '/partA_live/META.json', meta)
    print(json.dumps(meta['vs_partA_snapshot']), meta['filled_per_level'])
    return 0


def cmd_projection(a):
    p2l = TOFF + '/phase2l/TOKENS.md'
    txt = open(p2l, encoding='utf-8').read()
    w = sum(int(x.replace(',', '')) for x in re.findall(r'- writers \w+#1: ([\d,]+) tokens', txt))
    j = sum(int(x.replace(',', '')) for x in re.findall(r'- judge s\d#1: ([\d,]+) tokens', txt))
    jmax = max(int(x.replace(',', '')) for x in re.findall(r'- judge s\d#1: ([\d,]+) tokens', txt))
    so_far = spent()
    proj = int(w * 1.15) + int(j * 1.15) + int(jmax * 1.15)
    total = so_far + proj + AGENT_EST
    ok = total <= BUDGET_LANG
    lines = ['## Part D projection (%s)' % now(), '',
             '2L actual: writers %s, judges %s (largest judge %s). Projection x1.15: writers %s + judges %s + one judge retry %s = %s.' % (
                 format(w, ','), format(j, ','), format(jmax, ','), format(int(w * 1.15), ','), format(int(j * 1.15), ','),
                 format(int(jmax * 1.15), ','), format(proj, ',')),
             'Headless used so far (this language): %s. Agent reserve: %s. Projected language total: %s of %s -> %s.' % (
                 format(so_far, ','), format(AGENT_EST, ','), format(total, ','), format(BUDGET_LANG, ','),
                 'WITHIN budget' if ok else 'EXCEEDS budget -> STOP before any Part D session'), '']
    for l_ in lines:
        tokens_md(l_)
    if not ok:
        open(L['dir'] + '/STOP_D_budget.md', 'w').write('# STOP D budget\nProjection %d > %d; 0 Part D sessions spawned; the set was never built or opened.\n' % (total, BUDGET_LANG))
        return 5
    print('projection', total)
    return 0


def used_exercise_ids():
    """exercise_ids of the earlier MEASUREMENT sets: every JSON/JSONL file inside a directory named `set` under
    phase1*/phase2* (_mock excluded).  A file with > 1,000 distinct ids would be a production corpus, not a set: skipped."""
    EID, files, skipped = set(), [], []
    for top in sorted(glob.glob(TOFF + '/phase1*') + glob.glob(TOFF + '/phase2*')):
        for dp, dn, fn in os.walk(top):
            if '/_mock' in dp or '/.git' in dp or os.path.basename(dp) != 'set':
                continue
            for f in fn:
                if not f.endswith(('.json', '.jsonl')):
                    continue
                p = os.path.join(dp, f)
                raw = open(p, encoding='utf-8', errors='replace').read()
                ids = {int(m.group(1)) for m in re.finditer(r'"exercise_id"\s*:\s*"?(\d+)', raw)}
                if len(ids) > 1000:
                    skipped.append(os.path.relpath(p, TOFF)); continue
                files.append(os.path.relpath(p, TOFF))
                EID |= ids
    return EID, files


def cmd_make_set(a):
    lang = L['lang']
    rows = source_rows()
    used, files = used_exercise_ids()
    pos = LANG_ORDER.index(lang)
    out, stats = [], {}
    for li, lv in enumerate(LEVELS):
        ids = sorted(e for e, r in rows.items() if r['level'] == lv)
        order = ids[:]
        random.Random(SEED + li).shuffle(order)
        mine = [e for i, e in enumerate(order) if i % 3 == pos]
        st = Counter(level_rows=len(ids), my_slots=len(mine))
        cand, relaxed = [], False
        for relax in (False, True):
            cand, seen = [], set()
            for e in mine:
                r = rows[e]
                s = (r.get('src') or '').strip()
                if not s: st['empty' + ('_r' if relax else '')] += 1; continue
                if not relax and e in used: st['excl_used_before'] += 1; continue
                if s in seen: continue
                seen.add(s); cand.append(e)
            if len(cand) >= 25:
                relaxed = relax; break
        if len(cand) < 25:
            print('too few at', lv); return 7
        pick = sorted(cand[:25])
        st['picked'] = 25; st['relaxed_used_before'] = relaxed
        stats[lv] = dict(st)
        for k, e in enumerate(pick, 1):
            r = rows[e]
            out.append({'sid': e, 'wid': 'w%s%02d' % (lv, k), 'level': lv, 'source': r['src'], 'topic': r['topic'],
                        'exercise_id': e, 'rewrite_status': r.get('rewrite_status'), 'src_original': r.get('src_original')})
    assert len(out) == 100 and len({o['sid'] for o in out}) == 100
    h = wjl(L['D'] + '/set/sentences.jsonl', out)
    wj(L['D'] + '/set/EXCLUSION_PROOF.json', {
        'method': 'exercise_id of every JSON/JSONL file in a directory named set under phase1*/phase2* '
                  '(_mock excluded; a file with > 1,000 ids is a corpus and skipped) is "used before" and skipped (preferred; relaxed per level only if < 25 remain). The 4,064 '
                  'ids of each level are shuffled with one seed shared by the three wave-1 languages; de takes positions 0 mod 3, '
                  'ua 1 mod 3, es 2 mod 3, so the three wave-1 sets are disjoint by construction.',
        'files_scanned': len(files), 'used_before_ids': len(used), 'per_level': stats,
        'picked_used_before': sum(1 for o in out if o['exercise_id'] in used), 'sentences_sha256': h})
    wj(L['D'] + '/set/SET_META.json', {'seed': SEED, 'lang': lang, 'position_mod3': pos, 'stats': stats, 'sha256': h,
                                       'rewritten_in_set': sum(1 for o in out if o['rewrite_status'] == 'changed')})
    print(json.dumps({'stats': stats, 'used_before': len(used)}))
    return 0


def writers(base, stop_root, mock=False):
    tmpl = P.writer_template(L['lang'])
    sents = jl(L['D'] + '/set/sentences.jsonl')
    jobs = {}
    os.makedirs(base + '/writers', exist_ok=True)
    for lv in LEVELS:
        ss = [s for s in sents if s['level'] == lv]
        prompt = tmpl.replace('{SENTENCES}', '\n'.join(json.dumps({'wid': s['wid'], 'source': s['source'], 'level': s['level'],
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
    res = run_group('writers', jobs, base, stop_root, est=80000, max_turns=12, cap_session=None,
                    spent_base=(base if mock else None))
    summ = {'template_sha': hashlib.sha256(tmpl.encode()).hexdigest(), 'model': 'opus',
            'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()}}
    rc = handle_fail(res, stop_root, 'writers')
    if rc:
        wj(base + '/writers/WRITERS_SUMMARY.json', summ); return rc
    by_wid = {s['wid']: s for s in sents}
    answers, dedup, tcount, ad = [], [], Counter(), 0
    for lv in LEVELS:
        for o in res[lv]['arr']:
            s = by_wid[o['wid']]; seen = set()
            its = [('correct', None, x, False, 'c%d' % i) for i, x in enumerate(o['correct'], 1)] + \
                  [('wrong', w['type'], w['answer'], bool(w.get('agent_drop')), w['type'].lower()) for w in o['wrong']]
            for intent, typ, x, adr, suf in its:
                x = x.strip()
                if x in seen:
                    dedup.append({'sid': s['sid'], 'intent': intent, 'type': typ, 'answer': x}); continue
                seen.add(x)
                if typ: tcount[typ] += 1
                ad += adr
                answers.append({'aid': 'A:%d:%s' % (s['sid'], suf), 'sid': s['sid'], 'level': s['level'], 'source': s['source'],
                                'topic': s['topic'], 'answer': x, 'writer_intent': intent, 'writer_type': typ, 'writer_agent_drop': adr})
    assert len({x['aid'] for x in answers}) == len(answers)
    h = wjl(base + '/set/answers.jsonl', answers)
    summ.update(answers=len(answers), correct=sum(x['writer_intent'] == 'correct' for x in answers),
                wrong=sum(x['writer_intent'] == 'wrong' for x in answers), wrong_by_type=dict(tcount), dedupes=dedup,
                agent_drop_natural=ad, answers_sha=h,
                tokens_new={k: sum(int(x.get('tokens') or 0) for x in r['attempts'] if not x['resumed']) for k, r in res.items()})
    wj(base + '/writers/WRITERS_SUMMARY.json', summ)
    print(json.dumps({k: summ[k] for k in ('answers', 'correct', 'wrong', 'wrong_by_type', 'tokens_new')}))
    return 0


def packets(base):
    ans = jl(base + '/set/answers.jsonl')
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
        pk[s].append({'jid': j, 'source': a_['source'], 'level': a_['level'], 'answer': a_['answer'], 'topic': a_['topic']})
    meta = {'seed': JSEED, 'controls': 80, 'sessions': {}}
    for s in range(4):
        rng.shuffle(pk[s])
        aids = [k['aid'] for k in key if k['session'] == s + 1]
        assert len(aids) == len(set(aids)) and {p['level'] for p in pk[s]} == set(LEVELS)
        h = wjl(base + '/judge/packet_s%d.jsonl' % (s + 1), pk[s])
        meta['sessions'][s + 1] = {'items': len(pk[s]), 'controls': sum(1 for k in key if k['session'] == s + 1 and k['is_control']),
                                   'levels': dict(Counter(x['level'] for x in pk[s])), 'sha256': h}
    wjl(base + '/judge/key.jsonl', key)
    byaid = {x['aid']: x for x in ans}
    cl = [k for k in key if k['is_control']]
    meta['controls_by_level'] = dict(Counter(byaid[k['aid']]['level'] for k in cl))
    meta['controls_by_intent'] = dict(Counter(byaid[k['aid']]['writer_intent'] for k in cl))
    meta['controls_session_pairs'] = dict(Counter('%d->%d' % (k['orig_session'], k['session']) for k in cl))
    wj(base + '/judge/PACKETS_META.json', meta)
    print(json.dumps(meta)[:400])
    return 0


def judges(base, stop_root, mock=False):
    prompt = P.judge_prompt(L['lang'])
    os.makedirs(base + '/judge', exist_ok=True)
    open(base + '/judge/judge_prompt.txt', 'w', encoding='utf-8').write(prompt)
    jobs = {}
    for s in range(1, 5):
        its = jl(base + '/judge/packet_s%d.jsonl' % s)
        for it in its:
            assert set(it) == {'jid', 'source', 'level', 'answer', 'topic'}
        full = prompt + '\n'.join(json.dumps(it, ensure_ascii=False) for it in its) + '\n'
        open(base + '/judge/prompt_s%d.txt' % s, 'w', encoding='utf-8').write(full)

        def vfn(arr, its=its):
            if not isinstance(arr, list): return 'not a list'
            want = [it['jid'] for it in its]
            got = [o.get('jid') if isinstance(o, dict) else None for o in arr]
            if len(got) != len(set(got)): return 'duplicate jid'
            if set(got) != set(want): return 'jid set mismatch (missing %d, extra %d)' % (len(set(want) - set(got)), len(set(got) - set(want)))
            for o in arr:
                if o.get('label') not in ('correct', 'wrong'): return 'bad label at %s' % o.get('jid')
                if not isinstance(o.get('reason'), str): return 'bad reason at %s' % o.get('jid')
            return None
        jobs['s%d' % s] = (full, vfn)
    res = run_group('judge', jobs, base, stop_root, est=110000, max_turns=2, cap_session=JUDGE_CAP,
                    spent_base=(base if mock else None))
    summ = {'prompt_sha': hashlib.sha256(prompt.encode()).hexdigest(), 'model': 'opus', 'max_turns': 2, 'cap_per_session': JUDGE_CAP,
            'sessions': {k: {x: r.get(x) for x in ('ok', 'stop', 'why', 'attempts')} for k, r in res.items()}}
    wj(base + '/judge/JUDGES_SUMMARY.json', summ)
    rc = handle_fail(res, stop_root, 'judges')
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
                         'source': a_['source'], 'answer': a_['answer']})
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
    print('labels', dict(Counter(r['label'] for r in rows)), 'controls disagree', len(dis))
    return 0


def all_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from all_keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from all_keys(v)


def build_items(base):
    sents = {s['sid']: s for s in jl(L['D'] + '/set/sentences.jsonl')}
    ans = jl(base + '/set/answers.jsonl')
    lab = {r['aid']: r for r in jl(base + '/judge/labels.jsonl')}
    items, truth = [], []
    for a_ in sorted(ans, key=lambda x: (x['sid'], x['aid'])):
        s = sents[a_['sid']]
        items.append({'jid': a_['aid'], 'sid': a_['sid'], 'level': a_['level'], 'src': s['source'], 'answer': a_['answer'],
                      'exercise_id': s['exercise_id']})
        Lb = lab[a_['aid']]
        truth.append({'aid': a_['aid'], 'sid': a_['sid'], 'level': a_['level'], 'judge_label': Lb['label'], 'judge_reason': Lb['reason'],
                      'judge_session': Lb['session'], 'writer_intent': a_['writer_intent'], 'writer_type': a_['writer_type'],
                      'writer_agent_drop': a_['writer_agent_drop'], 'source': s['source'], 'answer': a_['answer'], 'topic': s['topic'],
                      'rewrite_status': s.get('rewrite_status'), 'src_original': s.get('src_original')})
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
    base = L['D'] + '/_mock'
    if os.path.exists(base):
        import shutil
        shutil.rmtree(base)
    os.makedirs(base + '/set', exist_ok=True)
    import shutil
    shutil.copy(L['D'] + '/set/sentences.jsonl', base + '/set/sentences.jsonl')
    calls = {'n': 0, 'seen': set()}

    def fake(argv, timeout):
        calls['n'] += 1
        pr = argv[argv.index('-p') + 1]
        usage = {'input_tokens': 1000, 'output_tokens': 500}
        if 'Sentences:\n' in pr:
            lines = [json.loads(l) for l in pr.split('Sentences:\n', 1)[1].splitlines() if l.strip()]
            assert all(set(x) == {'wid', 'source', 'level', 'topic'} for x in lines)
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

    def sub_fake(prompt):
        env = json.loads(fake(['-p', prompt], 0).stdout)
        return env['result'], R.usage_total(env)
    SUB_FAKE[0] = sub_fake
    saveD = L['D']
    for step in (lambda: writers(base, base, True), lambda: packets(base), lambda: judges(base, base, True),
                 lambda: labels(base)):
        rc = step()
        if rc:
            print('MOCK FAIL rc', rc); return rc
    L['D'] = base
    try:
        rc = build_items(base)
    finally:
        L['D'] = saveD
    if rc:
        return rc
    # the mock items through the REAL stack with HTTP mocked (0 calls), poison-wrapped
    S.B.HTTP[0] = lambda url, body, key: (200, {'candidates': [{'content': {'parts': [{'text': 'NONE' if 'NONE or MISSING' in json.dumps(body) else 'SAME'}]}}],
                                                'usageMetadata': {'promptTokenCount': 1, 'candidatesTokenCount': 1}}, '')
    S.B.SLEEP[0] = lambda s: None
    S.B.MIN_INTERVAL = 0.0
    its = [S.PoisonDict(dict(x, en=None, v=None)) for x in jl(base + '/set/items.jsonl')]
    root = base + '/root'
    os.makedirs(root + '/' + L['lang'], exist_ok=True)
    out = S.run_full(its, root + '/' + L['lang'] + '/run/partD', 'MOCK', L['lang'], S.lang_ledger(L['lang'], root), key='MOCK', root=root)
    assert out['status'] == 'COMPLETE', out
    print('MOCK PASS spawns', calls['n'], 'stack', out['l3']['counted_total'], out['cc']['counted_total'])
    return 0


def cmd_writers(a):
    rc = token_login()
    if rc: return rc
    rc = writers(L['D'], L['dir'])
    append_tokens(L['D'], 'writers')
    return rc


def cmd_judges(a):
    rc = token_login()
    if rc: return rc
    rc = judges(L['D'], L['dir'])
    append_tokens(L['D'], 'judge')
    return rc


def cmd_gemini(a):
    RUN = L['D'] + '/run'
    if os.path.exists(RUN):
        print('REFUSED: run dir exists (the set is opened once)'); return 2
    os.makedirs(RUN)
    items = S.B.open_set(L['D'] + '/set/items.jsonl', S.B.paths(RUN),
                         'Wave 1 Part D fresh %s set, opened ONCE by the frozen wave-1 stack' % P.LANG[L['lang']])
    t0 = time.time()
    led0 = S.read_json(S.lang_ledger(L['lang']), {})
    try:
        out = S.run_full([S.PoisonDict(x) for x in items], RUN, 'D', L['lang'], S.lang_ledger(L['lang']))
    except (S.Stop, S.Refused) as e:
        wj(RUN + '/RUN_OUT.json', {'status': 'STOPPED', 'kind': getattr(e, 'kind', None), 'why': getattr(e, 'why', str(e))})
        print('STOPPED', e); return 4
    out.update(ledger_before=led0, ledger_after=S.read_json(S.lang_ledger(L['lang']), {}), secs=round(time.time() - t0, 1),
               wave_counted_after=S.wave_counted())
    wj(RUN + '/RUN_OUT.json', out)
    print(json.dumps({'status': out['status'], 'ledger_after': out['ledger_after']}))
    return 0 if out['status'] == 'COMPLETE' else 3


def block(ids, T, res):
    c = [j for j in ids if T[j]['judge_label'] == 'correct']
    w = [j for j in ids if T[j]['judge_label'] == 'wrong']
    cov = rate(sum(bool(res[j]['accept']) for j in c), len(c))
    fa = rate(sum(bool(res[j]['accept']) for j in w), len(w))
    return {'coverage': cov, 'fa': fa,
            'coverage_target_90': {'point': cov['pct'] is not None and cov['pct'] >= 90, 'interval': cov['cp95'][0] is not None and cov['cp95'][0] >= 90},
            'fa_target_5': {'point': fa['pct'] is not None and fa['pct'] < 5, 'interval': fa['cp95'][1] is not None and fa['cp95'][1] < 5}}


def cmd_post(a):
    E = L['D']
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
    H = {'label': 'Wave 1 %s: frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG), fresh production set opened ONCE' % P.LANG[L['lang']],
         'truth': 'judge_label (partD/judge/labels.jsonl, 4 opus judge sessions)',
         'pooled': block(ids, T, res), 'per_level': {lv: block([j for j in ids if T[j]['level'] == lv], T, res) for lv in LEVELS},
         'l3_only_diagnostic': block(ids, T, {j: {'accept': j in cc_ids} for j in ids}),
         'layers': dict(Counter(str(r.get('layer')) for r in res.values())),
         'gemini': {'ledger_rows': len(led), 'counted_http200': len(counted), 'by_part': dict(Counter(r['_part'] for r in counted)),
                    'failed_counted': fails, 'http': dict(Counter(str(r.get('http')) for r in led)), 'spend_usd': spend_usd},
         'ledger_language': S.read_json(S.lang_ledger(L['lang']), {}), 'access_logs': [os.path.relpath(p, E) for p in acc]}
    p_ = H['pooled']
    H['both_targets_met_on_point'] = bool(p_['coverage_target_90']['point'] and p_['fa_target_5']['point'])
    FR = [j for j in ids if T[j]['judge_label'] == 'correct' and not res[j]['accept']]
    FA = [j for j in ids if T[j]['judge_label'] == 'wrong' and res[j]['accept']]

    def cause(j):
        r, t = res[j], T[j]
        return {'aid': j, 'level': t['level'], 'layer': r.get('layer'), 'l3_reply': r.get('l3_reply'),
                'cc_state': r.get('cc_state'), 'cc_word': r.get('cc_word'), 'writer_intent': t['writer_intent'], 'writer_type': t['writer_type'],
                'source': t['source'], 'answer': t['answer'], 'judge_reason': t['judge_reason']}
    H['false_rejections'] = {'n': len(FR), 'by_layer': dict(Counter(str(res[j].get('layer')) for j in FR)),
                             'by_writer': dict(Counter('%s/%s' % (T[j]['writer_intent'], T[j]['writer_type']) for j in FR)),
                             'by_level': dict(Counter(T[j]['level'] for j in FR)), 'items': [cause(j) for j in FR]}
    H['false_acceptances'] = {'n': len(FA), 'by_layer': dict(Counter(str(res[j].get('layer')) for j in FA)),
                              'by_writer_type': dict(Counter(str(T[j]['writer_type']) for j in FA)),
                              'by_level': dict(Counter(T[j]['level'] for j in FA)), 'items': [cause(j) for j in FA]}
    H['judge_noise'] = {k: v for k, v in json.load(open(E + '/judge/controls.json')).items() if k not in ('all',)}
    wj(E + '/analysis/HEADLINE.json', H)
    raw = ''.join('## %s\n\n```\n%s```\n\n' % (os.path.relpath(p, E), open(p, encoding='utf-8').read()) for p in acc)
    open(RUN + '/ACCESS_LOG_VERBATIM.md', 'w', encoding='utf-8').write(
        '# Part D access log (verbatim copies)\n\nOpens of partD/set/items.jsonl recorded: %d (run/access_log.jsonl).\n\n%s'
        % (len(jl(RUN + '/access_log.jsonl')), raw))
    rc_ = open(E + '/RUN_COMMIT.txt').read().strip()
    open(RUN + '/FINAL_RUN_DONE', 'w').write('Part D run finished %s; status %s; results %d; counted Gemini %d (HTTP 200); spend $%.6f; RUN_COMMIT %s\n'
                                             % (now(), json.load(open(RUN + '/RUN_OUT.json')).get('status'), len(res), len(counted), spend_usd, rc_))

    def row(name, b):
        c, f = b['coverage'], b['fa']
        return '| %s | %d/%d = %.2f %% [%.2f, %.2f] | %s / %s | %d/%d = %.2f %% [%.2f, %.2f] | %s / %s |' % (
            name, c['x'], c['n'], c['pct'], c['cp95'][0], c['cp95'][1], 'MET' if b['coverage_target_90']['point'] else 'missed',
            'MET' if b['coverage_target_90']['interval'] else 'missed', f['x'], f['n'], f['pct'], f['cp95'][0], f['cp95'][1],
            'MET' if b['fa_target_5']['point'] else 'missed', 'MET' if b['fa_target_5']['interval'] else 'missed')
    esc = lambda s: (s or '').replace('|', '/')
    md = ['# Wave 1 Part D - %s, fresh production set: analysis' % P.LANG[L['lang']], '',
          'Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.', '',
          '| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |',
          '|---|---|---|---|---|', row('pooled', H['pooled'])] + [row(lv, H['per_level'][lv]) for lv in LEVELS] + \
         ['', 'Both targets met on the point (pooled): %s' % H['both_targets_met_on_point'], '',
          'Diagnostic, L3 only (before the content check): ' + row('L3 only', H['l3_only_diagnostic']), '',
          'Gemini: %d counted calls (HTTP 200; %s), %d failed-but-counted, spend $%.6f; language ledger %s.' % (
              len(counted), H['gemini']['by_part'], fails, spend_usd, H['ledger_language']), '',
          'Judge noise (80 hidden duplicates, different sessions): %d/%d disagree = %s %% %s.' % (
              H['judge_noise']['disagree'], H['judge_noise']['controls'], H['judge_noise']['disagree_rate']['pct'], H['judge_noise']['disagree_rate']['cp95']), '',
          '## False rejections (%d) by cause' % len(FR), '', 'by layer %s; by writer %s; by level %s' % (
              H['false_rejections']['by_layer'], H['false_rejections']['by_writer'], H['false_rejections']['by_level']), '',
          '| aid | lvl | layer | cc word | writer | source | answer | judge reason |', '|---|---|---|---|---|---|---|---|'] + \
         ['| %s | %s | %s | %s | %s/%s | %s | %s | %s |' % (x['aid'], x['level'], x['layer'], x['cc_word'] or '', x['writer_intent'], x['writer_type'] or '',
                                                          esc(x['source']), esc(x['answer']), esc(x['judge_reason'])) for x in H['false_rejections']['items']] + \
         ['', '## False acceptances (%d) by cause' % len(FA), '', 'by layer %s; by writer type %s; by level %s' % (
             H['false_acceptances']['by_layer'], H['false_acceptances']['by_writer_type'], H['false_acceptances']['by_level']), '',
          '| aid | lvl | layer | cc | writer type | source | answer | judge reason |', '|---|---|---|---|---|---|---|---|'] + \
         ['| %s | %s | %s | %s | %s | %s | %s | %s |' % (x['aid'], x['level'], x['layer'], x['cc_state'], x['writer_type'],
                                                       esc(x['source']), esc(x['answer']), esc(x['judge_reason'])) for x in H['false_acceptances']['items']] + \
         ['', '## Judge duplicate disagreements', ''] + \
         ['- %s (%s, %s/%s) s%d %s vs s%d %s: "%s"' % (c['aid'], c['level'], c['writer_intent'], c['writer_type'], c['orig_session'], c['orig_label'],
                                                       c['dup_session'], c['dup_label'], c['answer']) for c in H['judge_noise']['disagreements']]
    open(E + '/analysis/ANALYSIS.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    p = H['pooled']
    print('POOLED cov %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['coverage'], '| FA %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['fa'],
          '| both met on point:', H['both_targets_met_on_point'])
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lang', choices=sorted(P.LANG))
    ap.add_argument('cmd', choices=['partA', 'partA_live', 'rw_pass1', 'rw_pass2', 'rw_final', 'projection', 'make_set', 'mock', 'writers',
                                    'packets', 'judges', 'labels', 'build_items', 'gemini', 'post'])
    a = ap.parse_args()
    setlang(a.lang)
    f = {'partA': cmd_partA, 'partA_live': cmd_partA_live, 'rw_pass1': cmd_rw_pass1, 'rw_pass2': cmd_rw_pass2, 'rw_final': cmd_rw_final,
         'projection': cmd_projection, 'make_set': cmd_make_set, 'mock': cmd_mock, 'writers': cmd_writers,
         'packets': lambda a: packets(L['D']), 'judges': cmd_judges, 'labels': lambda a: labels(L['D']),
         'build_items': lambda a: build_items(L['D']), 'gemini': cmd_gemini, 'post': cmd_post}[a.cmd]
    return f(a)


if __name__ == '__main__':
    sys.exit(main())
