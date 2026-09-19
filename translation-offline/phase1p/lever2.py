#!/usr/bin/env python3
"""Phase 1P — LEVER 2: "the Slovak does not fix X" annotations, passed exactly as the gender chain.

pipeline_1i.GENDER_TMPL is inserted into the user prompt as one extra line before GROUND_LINE;
these lines are inserted at the same place, by script, from the Slovak morphology already recorded
in the annotation (`voice_sk`, `tf_gold`, `tense_open`, `perfective_present`) plus a closed word
list. 0 model calls.

Three open points, each an owner rule:
  DEFINITENESS  Slovak has no articles                       (determiner class, +11 at L3 in 1O)
  ASPECT        owner rule B3: any grammatically possible English tense INSIDE the Slovak's frame
                is accepted with a tip.  The line NAMES the frame and says a different frame is
                DIFF, so it cannot relax the TIME FRAME.
  NUMBER        mass / collective nouns
"""
import re

DEF_LINE = ('Definiteness: Slovak has no articles, so the Slovak does not fix the English article '
            'here — "the", "a"/"an" and no article at all can all render it. An answer that keeps '
            'the meaning but chooses a different article is SAME on that point.')

ASPECT_TMPL = ('Aspect: the Slovak does not fix which English aspect is used inside its own time '
               'frame. The time frame here is the {frame}; any grammatically possible English '
               '{frame} form of the same event (simple, continuous or perfect) is SAME. A form '
               'that moves the event into a different time frame is DIFF.')

NUMBER_TMPL = ('Number: the Slovak does not fix the English number on {words} — the singular and '
               'the plural of the same idea are SAME on that point.')

ARTICLES = ('the', 'a', 'an')

MASS = {'water', 'money', 'bread', 'furniture', 'information', 'advice', 'luggage', 'baggage',
        'news', 'hair', 'fruit', 'work', 'coffee', 'tea', 'sugar', 'salt', 'rice', 'milk', 'paper',
        'equipment', 'homework', 'traffic', 'weather', 'music', 'food', 'wood', 'glass', 'soup',
        'cheese', 'meat', 'butter', 'snow', 'rain', 'sand', 'dust', 'ice', 'juice', 'wine', 'beer',
        'petrol', 'fuel', 'cash', 'rubbish', 'litter', 'stuff', 'knowledge', 'help', 'time'}
COLLECTIVE = {'staff', 'team', 'family', 'police', 'people', 'government', 'crew', 'class',
              'audience', 'committee', 'group', 'public', 'company', 'crowd', 'youth'}

CFG = {'definiteness': True, 'aspect': True, 'number': True}


def toks(s):
    return re.findall(r"[A-Za-z']+", (s or '').lower())


def _frame_word(ann):
    tf = (ann or {}).get('tf_gold')
    return {'past': 'past', 'present': 'present', 'future': 'future'}.get(tf)


def aspect_open(ann):
    """True when the Slovak leaves the aspect open INSIDE a frame we can name.

    Never fired for a Slovak perfective present (the 'dokonci' = future class the TIME FRAME rule
    protects) — that class is exactly where a loosened reading costs FA.
    """
    ann = ann or {}
    if ann.get('perfective_present'):
        return False
    if _frame_word(ann) is None:
        return False
    return bool(ann.get('tense_open')) or _frame_word(ann) in ('past', 'present')


def open_points(sk, ann, reference, answer=None, cfg=None):
    """(lines, fired) — the extra prompt lines, in a fixed order, plus which points fired."""
    cfg = dict(CFG, **(cfg or {}))
    lines, fired = [], []
    text = ' '.join(filter(None, [reference or '', answer or '']))
    t = toks(text)
    if cfg['definiteness'] and any(w in ARTICLES for w in t):
        lines.append(DEF_LINE)
        fired.append('definiteness')
    if cfg['aspect'] and aspect_open(ann):
        lines.append(ASPECT_TMPL.format(frame=_frame_word(ann)))
        fired.append('aspect')
    if cfg['number']:
        hits, seen = [], set()
        for w in toks(reference):
            if (w in MASS or w in COLLECTIVE) and w not in seen:
                seen.add(w)
                hits.append(w)
        if hits:
            lines.append(NUMBER_TMPL.format(words=', '.join('"%s"' % w for w in hits[:3])))
            fired.append('number')
    return lines, fired
