import json, os, sys, collections
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts'))
import validate_part as vp
H = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(H)
LANGS = ['en', 'de', 'ua', 'es', 'fr', 'tr', 'hu', 'sk', 'cz']

def derive(intro, ca, lang, t):
    return vp.derive_full_sentence(intro or '', ca or '', lang, t)

def load(name='before'):
    rows = json.load(open(f'{H}/work/snapshot_{name}.json'))
    by = collections.defaultdict(dict)
    for r in rows:
        by[r['exercise_id']][r['language_code']] = r
    return by

def check_row(r):
    """Invariants of the brief for one row dict (intro_text, correct_answer, full_sentence, exercise_type_id, language_code)."""
    errs = []
    t = r['exercise_type_id']; it = r['intro_text'] or ''; ca = r['correct_answer'] or ''; fs = r['full_sentence'] or ''
    if t in vp.NO_INTRO_TYPES:
        return ['no-intro type']
    if t not in vp.STEM_TYPES and it.count('...') - ca.count('...') != 1:
        errs.append('gap marker count != 1')
    want = derive(it, ca, r['language_code'], t)
    if want != fs:
        errs.append(f'full_sentence != derive: {want!r}')
    if ca.strip():
        for part in ca.split('...'):
            if part.strip() and part.strip().rstrip('.!?').lower() not in fs.lower():
                errs.append(f'gap word {part!r} not in sentence')
    for d in ('distractor_1', 'distractor_2'):
        if r.get(d) and ca.strip() and r[d].strip().lower() == ca.strip().lower():
            errs.append(f'{d} equals correct_answer')
    if '  ' in fs or '...' in fs:
        errs.append('bad spacing / leftover gap')
    return errs
