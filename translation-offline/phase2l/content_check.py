#!/usr/bin/env python3
"""Phase 2L Part B1 - the SOURCE-SIDE content check (brief B1).
ONE further call (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0) for an answer the SOURCE-ONLY stack accepted,
given ONLY the source sentence, its language name and the answer.  Reply exactly `NONE` or `MISSING: <source word>`.
Parse is strict: whitespace trimmed, then one trailing period; anything else = FAILED call (counted by the transport,
never retried, never guessed) and the item keeps its L3 verdict.  MISSING -> reject.  Language param: sk | cz.
Pure module: no I/O, no reference field can reach it (it takes two strings)."""
import contextlib, json, re
LANG = {'sk': 'Slovak', 'cz': 'Czech'}
MODEL = 'gemini-3.1-flash-lite'
GCFG = {'temperature': 0, 'maxOutputTokens': 48, 'thinkingConfig': {'thinkingBudget': 0}}
RULING_LISTS = ("now, today, already, still, finally, then, totally, completely, just, Look!; Slovak teraz, dnes, už, "
                "ešte, konečne, vtedy, úplne, práve, Pozri!; Czech teď, dnes, už, ještě, konečně, tehdy, úplně, právě, "
                "Podívej!")
SYS_TMPL = (
    "You check a learner's English translation of a {L} sentence. There is no reference translation: use the {L} "
    "sentence only. One question: is any NOUN, ADJECTIVE, MAIN VERB or PLACE/DIRECTION PHRASE of the {L} sentence "
    "missing from the answer, or its meaning changed?\n"
    "Rules:\n"
    "- The owner's ruling: time adverbs, degree adverbs and interjections do NOT count (" + RULING_LISTS + "). "
    "If only such a word is absent, the answer is NONE.\n"
    "- A synonym or paraphrase that carries the same meaning is NOT missing.\n"
    "- Judge word meaning only; tense, articles and word order are not part of this question.\n"
    "Reply with exactly NONE, or exactly MISSING: <source word> naming the {L} word that is missing or changed. "
    "No explanation.")
USER_TMPL = '%s sentence: %s\nLearner answer: %s\nNONE or MISSING?'
_MISS = re.compile(r'MISSING: (\S(?:[^\r\n]*\S)?)')


def sys_text(lang):
    if lang not in LANG:
        raise ValueError('language %r (sk|cz)' % (lang,))
    return SYS_TMPL.replace('{L}', LANG[lang])


def user_text(lang, src, answer):
    if not isinstance(src, str) or not isinstance(answer, str):
        raise TypeError('content check takes the source sentence and the answer as plain strings only')
    return USER_TMPL % (LANG[lang], src, answer)


def request(lang, src, answer):
    return {'sys': sys_text(lang), 'user': user_text(lang, src, answer), 'gcfg': json.loads(json.dumps(GCFG))}


def parse(text):
    s = (text or '').strip()
    if s.endswith('.'):
        s = s[:-1].rstrip()
    if s == 'NONE':
        return 'NONE'
    m = _MISS.fullmatch(s)
    return 'MISSING: ' + m.group(1) if m else None


def word_of(v):
    return v[len('MISSING: '):] if isinstance(v, str) and v.startswith('MISSING: ') else None


@contextlib.contextmanager
def transport(B):
    """Reuse run_2i_base.call_one unchanged; only its reply parser is swapped for the duration of the check calls."""
    old = B.parse_reply
    B.parse_reply = parse
    try:
        yield
    finally:
        B.parse_reply = old


def l3_ok(r, tip_accept):
    return bool(r.get('accept')) or (bool(tip_accept) and r.get('layer') == 'L3:TIPrej')


def decide(r, cc, tip_accept):
    """r = SOURCE-ONLY stack result row, cc = content-check reply row or None -> (accept|None, layer, cc_state)."""
    if not l3_ok(r, tip_accept):
        return False, r.get('layer'), 'not_checked'
    if cc is None:
        return None, 'CC:pending', 'pending'
    if cc.get('failed'):
        return True, '%s+CC:failed' % r.get('layer'), 'failed'
    if cc.get('verdict') == 'NONE':
        return True, '%s+CC:NONE' % r.get('layer'), 'none'
    return False, 'CC:MISSING', 'missing'


def spec_text():
    return ('# Phase 2L content check prompt (%s, generationConfig %s)\n\n## system (Slovak)\n%s\n\n## system (Czech)\n%s'
            '\n\n## user\n%s\n\n## parse\nStrip whitespace, then one trailing period; exactly NONE or exactly '
            '"MISSING: <word>" on one line. Anything else = FAILED call: counted, never retried, never guessed; the item '
            'keeps its L3 verdict.\n' % (MODEL, json.dumps(GCFG, sort_keys=True), sys_text('sk'), sys_text('cz'),
                                          user_text('sk', '<SOURCE SENTENCE>', '<ANSWER>')))


if __name__ == '__main__':
    import os, sys
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec', 'content_check_prompt.txt')
    open(p, 'w', encoding='utf-8').write(spec_text())
    print('wrote', p)
