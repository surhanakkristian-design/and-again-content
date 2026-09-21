#!/usr/bin/env python3
"""Phase 1P — LEVER 3: stored reference variants with a deterministic TIME-FRAME filter.

Finding recorded in DEV_READOUT_1P.md: under P-FROZEN / P-FROZEN-1N the model saw exactly ONE
English rendering (checker_1i.prompt(it,'P-B') interpolates it['reference'] only; runner_1k.build_req
adds the gender line, GROUND_LINE and WORDING_LINE and NEVER pipeline_1i.ALT_TMPL). The lever is
therefore live.

The lever shows the main reference plus up to `CAP` further STORED renderings (annotation key `v`),
equally ranked, and removes any variant whose time frame differs from the main reference's.
0 model calls; pure string work.
"""
import re

CAP = 2                                  # extra variants shown beside the main reference
ALT_TMPL = 'Also accepted English: {alts}'

FUT = {'will', 'shall', "'ll", "will've", 'wo'}
PAST_AUX = {'was', 'were', 'had', 'did'}
PRES_AUX = {'am', 'is', 'are', 'have', 'has', 'do', 'does', "'s", "'re", "'m", "'ve"}
MODAL_PRES = {'can', 'may', 'must', 'shall', 'will'}
MODAL_PAST = {'could', 'might', 'would', 'should'}
IRREG_PAST = {
    'was', 'were', 'had', 'did', 'went', 'saw', 'came', 'took', 'made', 'said', 'told', 'got',
    'gave', 'found', 'thought', 'knew', 'wrote', 'read', 'left', 'felt', 'kept', 'held', 'brought',
    'bought', 'caught', 'taught', 'sent', 'spent', 'built', 'lost', 'met', 'paid', 'put', 'ran',
    'sat', 'stood', 'understood', 'won', 'wore', 'broke', 'chose', 'drove', 'ate', 'fell', 'flew',
    'forgot', 'grew', 'heard', 'hid', 'let', 'lay', 'led', 'rang', 'rose', 'sang', 'sold', 'shut',
    'slept', 'spoke', 'swam', 'threw', 'woke', 'drank', 'began', 'became', 'brought', 'cut',
    'showed', 'drew'}


def toks(s):
    return re.findall(r"[A-Za-z']+", (s or '').lower())


def time_frame(sentence):
    """'future' | 'past' | 'present' — the frame of the FIRST finite verb. Deterministic."""
    t = toks(sentence)
    for i, w in enumerate(t):
        if w in FUT:
            return 'future'
        if w == 'going' and i + 1 < len(t) and t[i + 1] == 'to':
            return 'future'
    for w in t:
        if w in PAST_AUX:
            return 'past'
        if w in PRES_AUX or w in MODAL_PRES:
            return 'present'
        if w in MODAL_PAST:
            return 'past'
    for w in t:
        if w in IRREG_PAST:
            return 'past'
        if w.endswith('ed') and len(w) > 4:
            return 'past'
    return 'present'


def pick(reference, refs, cap=CAP):
    """(shown, removed) — stored renderings other than the main reference, tense-filtered."""
    main = (reference or '').strip()
    mtf = time_frame(main)
    shown, removed, seen = [], [], {main}
    for v in (refs or []):
        if not isinstance(v, str):
            continue
        v = v.strip()
        if not v or v in seen:
            continue
        seen.add(v)
        if time_frame(v) != mtf:
            removed.append({'variant': v, 'tf': time_frame(v), 'main_tf': mtf})
            continue
        if len(shown) < cap:
            shown.append(v)
    return shown, removed


def line(reference, refs, cap=CAP):
    """(prompt line or None, shown, removed)."""
    shown, removed = pick(reference, refs, cap)
    if not shown:
        return None, shown, removed
    return ALT_TMPL.format(alts=' | '.join('"%s"' % a for a in shown)), shown, removed
