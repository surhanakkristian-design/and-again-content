#!/usr/bin/env python3
"""Wave 1 Part E: write the Part B rewrite (full_sentence) for ONE language (ua | es) that met BOTH Part D targets.
Brief: back up the current full_sentence rows of the 4,064 exercises (jsonl + SHA-256), write rollback.sql (NOT run),
dry run (counts per change), then UPDATE full_sentence in batches of at most 500, each its own transaction, idempotent.
Verify: re-select equals the rewritten file, all other languages and all other exercises unchanged (checksums before and
after).  A language that failed Part D gets NO write (checked here from its HEADLINE.json before anything else).
    python3 -B partE_db.py <lang> gate|backup|rollback|dryrun|write|verify
Every UPDATE touches ONLY public.exercise_localizations.full_sentence, ONLY rows with language_code = <lang>, ONLY ids
of the backup (the 4,064 selected exercises), and ONLY where full_sentence still equals the backed-up old value."""
import hashlib, json, os, subprocess, sys, time
sys.dont_write_bytecode = True
W1 = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/wave1'
APP = '/Users/kristiansurhanak/Projects/and-again'
SB = os.path.expanduser('~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase')
BATCH = 500


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def q(sql=None, file=None):
    args = [SB, 'db', 'query', '--linked', '-o', 'json'] + (['--file', file] if file else [sql])
    p = subprocess.run(args, capture_output=True, text=True, cwd=APP, timeout=900)
    if p.returncode != 0:
        raise SystemExit('query failed: %s' % p.stderr[-1500:])
    out = p.stdout.strip()
    if not out:
        return []
    d = json.loads(out)
    rows = d.get('rows') if isinstance(d, dict) else d
    return rows if isinstance(rows, list) else []


def lit(s):
    return 'NULL' if s is None else "'" + s.replace("'", "''") + "'"


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


def log(E, msg):
    with open(E + '/partE.log', 'a', encoding='utf-8') as f:
        f.write('%s %s\n' % (now(), msg))
    print(msg)


SEL = "select exercise_id from public.translation_selected_exercises"


def checksums(lang):
    per_lang = q("select language_code, count(*) as n, md5(string_agg(md5(to_jsonb(el)::text), '' order by el.id)) as h "
                 "from public.exercise_localizations el group by 1 order by 1")
    split = q("select (exercise_id in (%s)) as selected, count(*) as n, "
              "md5(string_agg(md5(to_jsonb(el)::text), '' order by el.id)) as h_full, "
              "md5(string_agg(md5((to_jsonb(el) - 'full_sentence')::text), '' order by el.id)) as h_without_full_sentence "
              "from public.exercise_localizations el where language_code = '%s' group by 1 order by 1" % (SEL, lang))
    other_tables = q("select (select count(*) from public.exercises) as exercises, "
                     "(select count(*) from public.translation_selected_exercises) as selected, "
                     "(select count(*) from public.exercise_localizations) as localizations")
    return {'per_language': per_lang, 'target_split': split, 'counts': other_tables[0], 'ts': now()}


def main():
    lang, cmd = sys.argv[1], sys.argv[2]
    if lang not in ('ua', 'es'):
        raise SystemExit('REFUSED: Part E is only for ua / es (de has no rewrite)')
    D = W1 + '/' + lang
    E = D + '/partE'
    os.makedirs(E, exist_ok=True)
    H = json.load(open(D + '/partD/analysis/HEADLINE.json'))
    met = bool(H['pooled']['coverage_target_90']['point'] and H['pooled']['fa_target_5']['point'])
    if cmd == 'gate':
        log(E, 'gate: %s coverage %s %% FA %s %% -> both targets met on the point: %s' % (
            lang, H['pooled']['coverage']['pct'], H['pooled']['fa']['pct'], met))
        return 0 if met else 9
    if not met:
        log(E, 'REFUSED: %s did not meet both Part D targets; NO write' % lang)
        return 9
    rw = {o['exercise_id']: o for o in jl(D + '/partB/rewritten.jsonl')}
    if cmd == 'backup':
        rows = q("select id, exercise_id, language_code, full_sentence from public.exercise_localizations "
                 "where language_code = '%s' and exercise_id in (%s) order by id" % (lang, SEL))
        assert len(rows) == 4064 and len({r['exercise_id'] for r in rows}) == 4064, len(rows)
        p = E + '/backup_full_sentence_%s.jsonl' % lang
        with open(p, 'w', encoding='utf-8') as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        open(p + '.sha256', 'w').write('%s  %s\n' % (h, os.path.basename(p)))
        cs = checksums(lang)
        json.dump(cs, open(E + '/checksums_before.json', 'w'), indent=1)
        log(E, 'backup: %d rows, sha256 %s; checksums_before written' % (len(rows), h))
        return 0
    bk = {r['exercise_id']: r for r in jl(E + '/backup_full_sentence_%s.jsonl' % lang)}
    change = []
    conflicts = []
    for eid, o in sorted(rw.items()):
        b = bk[eid]
        if o['status'] != 'changed':
            continue
        if b['id'] != o['loc_id']:
            conflicts.append({'exercise_id': eid, 'why': 'loc id differs'})
        elif b['full_sentence'] == o['new']:
            continue                                   # already written (idempotent)
        elif b['full_sentence'] != o['old']:
            conflicts.append({'exercise_id': eid, 'why': 'live full_sentence differs from the Part A value',
                              'live': b['full_sentence'], 'partA': o['old']})
        else:
            change.append({'id': b['id'], 'exercise_id': eid, 'old': o['old'], 'new': o['new']})
    if cmd == 'rollback':
        allc = [dict(id=bk[e]['id'], exercise_id=e, old=o['old'], new=o['new']) for e, o in sorted(rw.items()) if o['status'] == 'changed']
        lines = ['-- Wave 1 Part E ROLLBACK for %s (NOT run). Restores the backed-up full_sentence of every changed row.' % lang,
                 '-- Backup: backup_full_sentence_%s.jsonl. Only rows that still hold the rewritten value are touched.' % lang,
                 'begin;']
        for c in allc:
            lines.append("update public.exercise_localizations set full_sentence = %s where id = %d and language_code = '%s' "
                         "and full_sentence = %s;" % (lit(c['old']), c['id'], lang, lit(c['new'])))
        lines.append('commit;')
        open(E + '/rollback.sql', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        h = hashlib.sha256(open(E + '/rollback.sql', 'rb').read()).hexdigest()
        log(E, 'rollback.sql written (NOT run): %d updates, sha256 %s' % (len(allc), h))
        return 0

    def batch_sql(bt, tail):
        vals = ',\n'.join('(%d, %s, %s)' % (c['id'], lit(c['old']), lit(c['new'])) for c in bt)
        return ("begin;\nwith v(id, old, new) as (values\n%s\n), u as (\n update public.exercise_localizations el set full_sentence = v.new "
                "from v where el.id = v.id and el.language_code = '%s' and el.full_sentence = v.old\n returning el.id)\n"
                "select count(*) as updated from u;\n%s;\n" % (vals, lang, tail))
    batches = [change[i:i + BATCH] for i in range(0, len(change), BATCH)]
    if cmd == 'dryrun':
        res = []
        for k, bt in enumerate(batches, 1):
            p = E + '/dryrun_batch_%02d.sql' % k
            open(p, 'w', encoding='utf-8').write(batch_sql(bt, 'rollback'))
            r = q(file=p)
            res.append({'batch': k, 'rows': len(bt), 'would_update': r[0]['updated'] if r else None})
        out = {'lang': lang, 'changed_in_file': sum(1 for o in rw.values() if o['status'] == 'changed'),
               'to_update': len(change), 'conflicts': conflicts, 'batches': res, 'ts': now()}
        json.dump(out, open(E + '/dryrun.json', 'w'), indent=1, ensure_ascii=False)
        log(E, 'dryrun: to_update %d, conflicts %d, batches %s' % (len(change), len(conflicts), res))
        return 0 if not conflicts and all(b['would_update'] == b['rows'] for b in res) else 8
    if cmd == 'write':
        if conflicts:
            log(E, 'STOP: %d conflicts, NO write' % len(conflicts)); return 8
        done = []
        for k, bt in enumerate(batches, 1):
            p = E + '/write_batch_%02d.sql' % k
            open(p, 'w', encoding='utf-8').write(batch_sql(bt, 'commit'))
            r = q(file=p)
            n = r[0]['updated'] if r else None
            done.append({'batch': k, 'rows': len(bt), 'updated': n, 'ts': now()})
            log(E, 'write batch %d: %s of %d rows' % (k, n, len(bt)))
        json.dump(done, open(E + '/write_batches.json', 'w'), indent=1)
        return 0
    if cmd == 'verify':
        live = q("select id, exercise_id, full_sentence from public.exercise_localizations where language_code = '%s' "
                 "and exercise_id in (%s) order by id" % (lang, SEL))
        lv = {r['exercise_id']: r for r in live}
        bad = [e for e, o in rw.items() if lv[e]['full_sentence'] != o['new']]
        cs0 = json.load(open(E + '/checksums_before.json'))
        cs1 = checksums(lang)
        json.dump(cs1, open(E + '/checksums_after.json', 'w'), indent=1)
        other0 = {r['language_code']: r for r in cs0['per_language'] if r['language_code'] != lang}
        other1 = {r['language_code']: r for r in cs1['per_language'] if r['language_code'] != lang}
        sp0 = {str(r['selected']): r for r in cs0['target_split']}
        sp1 = {str(r['selected']): r for r in cs1['target_split']}
        res = {'lang': lang, 'rows': len(live), 'mismatch_vs_rewritten_file': bad,
               'other_languages_identical': other0 == other1,
               'target_non_selected_identical': sp0.get('False') == sp1.get('False'),
               'target_selected_identical_without_full_sentence': sp0['True']['h_without_full_sentence'] == sp1['True']['h_without_full_sentence'],
               'counts_identical': cs0['counts'] == cs1['counts'],
               'changed_rows_now_new': sum(1 for e, o in rw.items() if o['status'] == 'changed' and lv[e]['full_sentence'] == o['new']),
               'ts': now()}
        json.dump(res, open(E + '/verify.json', 'w'), indent=1, ensure_ascii=False)
        ok = not bad and res['other_languages_identical'] and res['target_non_selected_identical'] and \
            res['target_selected_identical_without_full_sentence'] and res['counts_identical']
        log(E, 'verify: %s' % json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in res.items()}))
        return 0 if ok else 7
    raise SystemExit('unknown command')


if __name__ == '__main__':
    sys.exit(main())
