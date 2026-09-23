#!/usr/bin/env python3
"""Wave 1 prompts (de / ua / es -> English).  Every prompt is DERIVED from a frozen sk/cz text by exact substitution,
nothing else is rewritten (brief: "the frozen sk/cz prompts adapted ONLY by: language name, the per-language list of
droppable time/degree adverbs and interjections, and decision 22"):
  L3 system      <- phase2k/spec/l3_system_cz.txt   (= phase2l/spec/l3_system_cz.txt, the frozen SOURCE-ONLY L3)
  L3 user        <- phase2k/spec/l3_user_cz.txt
  content check  <- phase2l/content_check.py SYS_TMPL / USER_TMPL (the frozen 2L Part B check, decision 2 line KEPT)
  judge          <- phase2l/partE/judge/judge_prompt.txt (2L Part E judge, decision 3 line already replaced)
  writer         <- phase2k/spec/writer_template_cz.txt (2L Part E writers)
Substitutions (each asserted to hit exactly once where it must):
  1. the sk/cz droppable-word list  ->  the language's own list (written from the owner's English list)
  2. 'Czech' -> the language name
  3. decision 22 added as ONE rule line (checker / judge) or ONE paragraph (writer)
The frozen sk/cz files are only READ.  `python3 -B prompts_w1.py` writes wave1/spec/*.txt."""
import json, os, sys
sys.dont_write_bytecode = True
TOFF = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline'
W1 = TOFF + '/wave1'
LANG = {'de': 'German', 'ua': 'Ukrainian', 'es': 'Spanish', 'fr': 'French', 'tr': 'Turkish', 'hu': 'Hungarian'}
# Wave 2 (23 Sept 2026, owner decision 52): fr / tr / hu, derived by the same substitutions as wave 1.
WAVE = {'de': 1, 'ua': 1, 'es': 1, 'fr': 2, 'tr': 2, 'hu': 2}
# written from the owner's list: now, today, already, still, finally, then, totally, completely, just, Look!
DROP = {
    'de': 'jetzt, heute, schon, noch, endlich, dann, damals, total, völlig, gerade, eben, Schau!',
    'ua': 'зараз, тепер, сьогодні, вже, ще, нарешті, тоді, зовсім, цілком, повністю, щойно, Дивись!',
    'es': 'ahora, hoy, ya, todavía, aún, por fin, finalmente, entonces, totalmente, completamente, justo, ¡Mira!',
    'fr': "maintenant, aujourd'hui, déjà, encore, toujours, enfin, finalement, alors, totalement, complètement, juste, Regarde !",
    'tr': 'şimdi, bugün, zaten, artık, hâlâ, henüz, nihayet, sonunda, o zaman, tamamen, büsbütün, az önce, Bak!',
    'hu': 'most, ma, már, még, végre, akkor, teljesen, totálisan, éppen, épp, Nézd!'}
# decision 22 examples: where the language leaves gender unmarked
G22_EX = {
    'de': '"sich", or a neuter noun for a person such as "das Kind"',
    'ua': '"свій", "себе", or a verb form without a subject pronoun',
    'es': '"su", "sus", "se", or a verb without a subject pronoun',
    'fr': '"son", "sa", "ses", "leur" (they agree with the possessed noun, not the owner), "lui", or "se"',
    'tr': '"o", "onun", "kendi", or a verb without a subject pronoun; Turkish never marks gender',
    'hu': '"ő", "övé", "maga", a possessive suffix, or a verb without a subject pronoun; Hungarian never marks gender'}
G22 = 'Genderless source: when the {L} sentence does not mark gender (e.g. {EX}), BOTH he/she and his/her are correct.'
EN_LIST = 'now, today, already, still, finally, then, totally, completely, just, Look!'
SKCZ_PAREN = ('(Slovak: teraz, dnes, už, ešte, konečne, vtedy, úplne, práve, Pozri!; Czech: teď, dnes, už, ještě, '
              'konečně, tehdy, úplně, právě, Podívej!)')
SKCZ_CC = ('now, today, already, still, finally, then, totally, completely, just, Look!; Slovak teraz, dnes, už, ešte, '
           'konečne, vtedy, úplne, práve, Pozri!; Czech teď, dnes, už, ještě, konečně, tehdy, úplně, právě, Podívej!')
SRC = {'l3_sys': TOFF + '/phase2k/spec/l3_system_cz.txt', 'l3_user': TOFF + '/phase2k/spec/l3_user_cz.txt',
       'judge': TOFF + '/phase2l/partE/judge/judge_prompt.txt', 'writer': TOFF + '/phase2k/spec/writer_template_cz.txt',
       'cc_py': TOFF + '/phase2l/content_check.py'}
GCFG_L3 = {'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}      # = stack_source.GCFG
GCFG_CC = {'temperature': 0, 'maxOutputTokens': 48, 'thinkingConfig': {'thinkingBudget': 0}}      # = content_check.GCFG
MODEL = 'gemini-3.1-flash-lite'


def _read(k):
    return open(SRC[k], encoding='utf-8').read()


def _once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise AssertionError('%s: %r found %d times (want 1)' % (what, old[:60], n))
    return text.replace(old, new)


def _check_lang(lang):
    if lang not in LANG:
        raise ValueError('language %r (de|ua|es|fr|tr|hu)' % (lang,))


def g22(lang):
    return G22.replace('{L}', LANG[lang]).replace('{EX}', G22_EX[lang])


def l3_sys(lang):
    _check_lang(lang)
    t = _read('l3_sys')
    t = _once(t, SKCZ_PAREN, '(%s: %s)' % (LANG[lang], DROP[lang]), 'l3 list')
    t = _once(t, '- Added content is WRONG.\n', '- Added content is WRONG.\n- %s\n' % g22(lang), 'l3 g22')
    assert 'Slovak' not in t
    t = t.replace('Czech', LANG[lang])
    if lang in RETRY:
        t = _once(t, '- Added content is WRONG.\n', '- %s\n- Added content is WRONG.\n' % voc_line(lang), 'l3 voc')
        t = _once(t, '\nWRONG or an ERROR = DIFF.', '\n- %s\nWRONG or an ERROR = DIFF.' % G22V[lang], 'l3 g22v')
    return t


def l3_user(lang, src, answer):
    _check_lang(lang)
    if not isinstance(src, str) or not isinstance(answer, str):
        raise TypeError('L3 takes the source sentence and the answer as plain strings only')
    t = _read('l3_user')
    assert t == 'Czech sentence: <SOURCE SENTENCE>\nLearner answer: <ANSWER>\nSAME, TIP or DIFF?', repr(t)
    return '%s sentence: %s\nLearner answer: %s\nSAME, TIP or DIFF?' % (LANG[lang], src, answer)


def _cc_frozen():
    """The frozen 2L content-check SYS_TMPL, read from content_check.py source (not imported: it only knows sk|cz)."""
    import ast
    tree = ast.parse(_read('cc_py'))
    env = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and getattr(node.targets[0], 'id', None) in (
                'RULING_LISTS', 'SYS_TMPL', 'USER_TMPL'):
            env[node.targets[0].id] = eval(compile(ast.Expression(node.value), 'cc', 'eval'), {}, dict(env))
    return env


def cc_sys(lang):
    _check_lang(lang)
    env = _cc_frozen()
    assert env['RULING_LISTS'] == SKCZ_CC
    t = env['SYS_TMPL']
    t = _once(t, SKCZ_CC, '%s; %s %s' % (EN_LIST, LANG[lang], DROP[lang]), 'cc list')
    t = _once(t, '- A synonym or paraphrase that carries the same meaning is NOT missing.\n',
              '- A synonym or paraphrase that carries the same meaning is NOT missing.\n- %s\n' % g22(lang), 'cc g22')
    assert 'Slovak' not in t and 'Czech' not in t
    t = t.replace('{L}', LANG[lang])
    if lang in RETRY:
        t = _once(t, '- A synonym or paraphrase that carries the same meaning is NOT missing.\n',
                  '- A synonym or paraphrase that carries the same meaning is NOT missing.\n- %s\n' % voc_line(lang), 'cc voc')
        t = _once(t, '\nReply with exactly NONE', '\n- %s\nReply with exactly NONE' % G22V_CC[lang], 'cc g22v')
    return t


def cc_user(lang, src, answer):
    _check_lang(lang)
    if not isinstance(src, str) or not isinstance(answer, str):
        raise TypeError('content check takes the source sentence and the answer as plain strings only')
    assert _cc_frozen()['USER_TMPL'] == '%s sentence: %s\nLearner answer: %s\nNONE or MISSING?'
    return '%s sentence: %s\nLearner answer: %s\nNONE or MISSING?' % (LANG[lang], src, answer)


# Retry brief (23 Sept 2026, owner decision 55): tr / hu ONLY.  Two additions to the L3 and content-check prompts (and
# the vocative line to the judge prompt, so the ground truth applies the same owner rule); every other language's
# output stays byte-identical.
#   1. Vocatives: an address term may be dropped like an interjection.  The terms are the ones that occur as address
#      terms in the 4,064 live selected rows (counts in retry_trhu/VOCATIVES.json).
#   2. Genderless source made effective (defect 4): an explicit verdict rule next to the verdict line, with a worked
#      example in the language.
RETRY = {'tr', 'hu'}
VOC = {'tr': 'Kanka, Kankam, Kızım, Canım, Dostum, Kardeşim, Millet',
       'hu': 'Tesó, Csajszi, Haver, Bestie, Főnök, Tanárnő'}
VOC_LINE = ('A vocative or address term ({L}: {V}) may be dropped, like an interjection; dropping it is NOT an error.')
G22V = {
    'tr': ('VERDICT RULE for gender: Turkish has no he/she. When the Turkish sentence refers to a person only with "o", '
           '"onun", "kendi" or a bare verb ending, the answer\'s he, she, his or her is ALWAYS correct (each such '
           'pronoun may be he or she) and is never a slip: reply SAME when the rest is correct, never TIP or DIFF for '
           'the gender. Worked example: Turkish sentence: O dün markete gitti. Learner answer: She went to the market '
           'yesterday. -> SAME. Learner answer: He went to the market yesterday. -> SAME. Turkish sentence: Onun '
           'kedisi bahçede uyuyor. Learner answer: Her cat is sleeping in the garden. -> SAME.'),
    'hu': ('VERDICT RULE for gender: Hungarian has no he/she. When the Hungarian sentence refers to a person only with '
           '"ő", "övé", "maga", a possessive suffix or a bare verb ending, the answer\'s he, she, his or her is ALWAYS '
           'correct (each such pronoun may be he or she) and is never a slip: reply SAME when the rest is correct, '
           'never TIP or DIFF for the gender. Worked example: Hungarian sentence: Ő tegnap a boltba ment. Learner '
           'answer: She went to the shop yesterday. -> SAME. Learner answer: He went to the shop yesterday. -> SAME. '
           'Hungarian sentence: A macskája a kertben alszik. Learner answer: Her cat is sleeping in the garden. -> SAME.')}
G22V_CC = {
    'tr': ('VERDICT RULE for gender: he, she, his or her for "o", "onun", "kendi" or a bare verb ending is never a '
           'missing or changed word. Worked example: Turkish sentence: Onun kedisi bahçede uyuyor. Learner answer: Her '
           'cat is sleeping in the garden. -> NONE. Learner answer: His cat is sleeping in the garden. -> NONE.'),
    'hu': ('VERDICT RULE for gender: he, she, his or her for "ő", "övé", "maga", a possessive suffix or a bare verb '
           'ending is never a missing or changed word. Worked example: Hungarian sentence: A macskája a kertben alszik. '
           'Learner answer: Her cat is sleeping in the garden. -> NONE. Learner answer: His cat is sleeping in the '
           'garden. -> NONE.')}


def voc_line(lang):
    return VOC_LINE.replace('{L}', LANG[lang]).replace('{V}', VOC[lang])


def l3_request(lang, src, answer):
    return {'sys': l3_sys(lang), 'user': l3_user(lang, src, answer), 'gcfg': json.loads(json.dumps(GCFG_L3))}


def cc_request(lang, src, answer):
    return {'sys': cc_sys(lang), 'user': cc_user(lang, src, answer), 'gcfg': json.loads(json.dumps(GCFG_CC))}


# Owner decisions 32 + 33 (22 Sept 2026, Wave 1 es brief; added AFTER de/ua were frozen, so only for the languages in
# JUDGE_D3233): the JUDGE prompt only.  The checker prompts (L3, content check) stay byte-identical.
# Wave 2 (brief 23 Sept 2026): decisions 32 + 33 in the JUDGE prompt of fr / tr / hu as well.  Decision 32 needs a
# grammatical gender: Turkish and Hungarian have none (decision 22 covers every tr/hu sentence), so the d32 line is
# added for fr only; d33 for all three.  es output is byte-identical to wave 1.
JUDGE_D32 = {'es', 'fr'}
JUDGE_D33 = {'es', 'fr', 'tr', 'hu'}
JUDGE_D3233 = JUDGE_D32 | JUDGE_D33
D32_EX = {'de': '"der Sportler"', 'ua': '"спортсмен"', 'es': '"el atleta"', 'fr': '"le client"'}
D32 = ('Grammatical gender decides: a grammatically masculine {L} noun (e.g. {EX}) is "he"; "she" is wrong. The '
       'genderless rule above covers only sentences that mark no gender at all.')
D33_OLD = '- Added content is wrong.\n'
D33_NEW = ('- Added content is wrong. Exception: an ADDED interjection (e.g. "Wow", "Bro") is NOT an error, just as a '
           'dropped interjection is not an error. Added content of any other kind stays wrong.\n')


def d32(lang):
    return D32.replace('{L}', LANG[lang]).replace('{EX}', D32_EX[lang])


def judge_prompt(lang):
    _check_lang(lang)
    t = _read('judge')
    t = _once(t, SKCZ_PAREN, '(%s: %s)' % (LANG[lang], DROP[lang]), 'judge list')
    t = _once(t, '- Added content is wrong.\n', '- Added content is wrong.\n- %s\n' % g22(lang), 'judge g22')
    assert 'Slovak' not in t
    t = t.replace('Czech', LANG[lang])
    if lang in JUDGE_D32:
        t = _once(t, '- %s\n' % g22(lang), '- %s\n- %s\n' % (g22(lang), d32(lang)), 'judge d32')
    if lang in JUDGE_D33:
        t = _once(t, D33_OLD, D33_NEW, 'judge d33')
    if lang in RETRY:
        t = _once(t, '- Genderless source:', '- %s\n- Genderless source:' % voc_line(lang), 'judge voc')
    assert t.rstrip().endswith('Items:')
    return t


def writer_template(lang):
    _check_lang(lang)
    t = _read('writer')
    t = _once(t, SKCZ_PAREN, '(%s: %s)' % (LANG[lang], DROP[lang]), 'writer list')
    t = _once(t, '\n\nSentences:\n{SENTENCES}', '\n\nThe owner\'s rule for genderless sources: %s\n\nSentences:\n{SENTENCES}'
              % g22(lang)[len('Genderless source: '):], 'writer g22')
    assert 'Slovak' not in t
    t = t.replace('Czech', LANG[lang])
    assert t.count('{SENTENCES}') == 1
    return t


def write_specs():
    os.makedirs(W1 + '/spec', exist_ok=True)
    out = []
    for lang in sorted(LANG):
        files = {'l3_system_%s.txt' % lang: l3_sys(lang),
                 'l3_user_%s.txt' % lang: l3_user(lang, '<SOURCE SENTENCE>', '<ANSWER>'),
                 'content_check_system_%s.txt' % lang: cc_sys(lang),
                 'content_check_user_%s.txt' % lang: cc_user(lang, '<SOURCE SENTENCE>', '<ANSWER>'),
                 'judge_prompt_%s.txt' % lang: judge_prompt(lang),
                 'writer_template_%s.txt' % lang: writer_template(lang)}
        for f, t in files.items():
            open(os.path.join(W1, 'spec', f), 'w', encoding='utf-8').write(t)
            out.append(f)
    json.dump({'model': MODEL, 'gcfg_l3': GCFG_L3, 'gcfg_cc': GCFG_CC, 'sources': SRC, 'drop': DROP, 'g22_examples': G22_EX},
              open(W1 + '/spec/SPEC_META.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return out


if __name__ == '__main__':
    print(write_specs())
