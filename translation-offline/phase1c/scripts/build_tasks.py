#!/usr/bin/env python3
"""Phase 1c: build the self-contained annotation task files tasks/batchS.md and tasks/batchL.md
from selection.json, phase1b/selection/all230.json and the mistake library (batch topics only)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); P1C = os.path.dirname(HERE); P1B = os.path.join(os.path.dirname(P1C), 'phase1b')
sel = json.load(open(os.path.join(P1C, 'selection.json')))
a = {r['exercise_id']: r for r in json.load(open(os.path.join(P1B, 'selection', 'all230.json')))}
lib = {}
for f in os.listdir(os.path.join(P1B, 'mistakes')):
    if f.endswith('.json'):
        d = json.load(open(os.path.join(P1B, 'mistakes', f))); lib[int(d['type_id'])] = d

RULES = r'''# Task: annotate batch {B} ({N} sentences) — Phase 1c

Budget: ONE read (this file, already done) and ONE write. Do not open any other file, do not search, do not run code.
Write `{OUT}`: a JSON array, one compact object per line, one per sentence below, same order. Nothing else.

## What an annotation is
For each English reference sentence (`en`, a translation of the Slovak `sk`), describe every English sentence a learner may
correctly write for `sk`, compactly. The checker matches patterns; it never expands rows.

## Output schema (omit a key when empty; all anchors case-insensitive whole words/phrases)
```
{{"id":10860,"t":44,"lv":"B1",
 "v":["The officer who stamped his passport barely raised her eyes.","The officer that stamped his passport barely raised her eyes."],
 "lk":["who stamped","that stamped"],
 "alt":{{"raised":["lifted"],"barely":["hardly","scarcely"],"stamped":["checked"]}},
 "g":[["his"],["her"]],
 "o":{{}},
 "d":{{"The":"A"}},
 "p":["+even","-barely"],
 "m":[["44.01","which stamped"],["44.03","who he stamped"],["44.07","stamped","who stamped"]]}}
```
- `id`,`t`,`lv`: copy from the input.
- `v` — `v[0]` = `en` EXACTLY. At most 3 more variants, each STRUCTURALLY different (another construction or word order a
  learner would write for `sk`: when/if, passive/active, "would already be"/"would be … by now", relative clause with/without
  pronoun, reported-speech alternatives…). NEVER a variant that differs only by a word swap, article, pronoun or optional word —
  those go in alt/d/g/o/p.
- `lk` — the LOCKED span per variant (same order as `v`): the practised grammar = the exercise answer `ans` located in that
  variant (and its counterpart in the other variants). Must occur verbatim in the variant. Discontinuous: pieces joined with
  ` .. ` ("would .. have been"). Nothing inside a lock may vary.
- Anchors (keys of alt/o/d, entries of g, `-` entries of p, 3rd element of m): a word or phrase that occurs in the variants,
  written exactly as there; `word#2` = its second occurrence. An anchor applies in every variant containing it. An anchor must
  NEVER lie inside a locked span.
- `alt` — THE MAIN JOB. For EVERY content word or phrase outside the lock that a learner could plausibly render differently
  from `sk` (nouns, verbs, adjectives, adverbs, phrasal verbs, set phrases), list the alternatives a learner would really write,
  as SHORT FREE TEXT, in the SAME grammatical form as the anchor so each can replace it in place ("dropped" → ["lowered","reduced"],
  "spines" → ["thorns"], "grin" → ["smirk"], "cancelled" → ["called off"], "whole" → ["entire"], "muddy" → ["covered in mud"]).
  Same meaning in THIS sentence only. Think of the Slovak word and every common English rendering of it. A phrase may replace a
  word and vice versa. Be generous with real everyday alternatives, strict about meaning: nothing that changes the meaning
  (drop ≠ lower when it means letting fall; interrupt ≠ cancel). Do not list pure BrE/AmE spelling variants (colour/color,
  cancelled/canceled — handled automatically), nor someone/somebody-type pairs. Words inside the lock are never keys.
- `g` — gender chains: each inner list = anchors that switch masculine↔feminine together (he↔she, him↔her, his↔her,
  himself↔herself). ONLY when `sk` does NOT fix the gender (no pronoun, verb form not gendered, e.g. "tlačí", "premenila" IS
  gendered → fixed). Omit when fixed. Put pronouns that must flip together in ONE chain.
- `o` — single pronoun alternatives: anchor → "her|it" (sk "ju", thing or person), "him|it" (sk "ho"), "them|it".
- `d` — determiner freedom where `sk` has no demonstrative/possessive for that noun: anchor → `A` (the|a/an|this|that),
  `P` (plural: the|these|those|∅), `Z` (the|∅) or an explicit list "the|her|his". Anchor = the determiner itself ("The"), or
  the bare noun when the reference has none (a determiner may then be inserted before it).
- `p` — small meaning-neutral optional words: `+w` may be inserted anywhere outside the lock (at most once), `+w@anchor` only
  right after anchor, `-anchor` may be dropped. Multi-word allowed ("+of them", "-for"). Only words like already, just, even,
  ever, really, up, of them, at all, for, then, so, right, now.
- `m` — 3–8 library mistakes from the LIBRARY INDEX below (only this sentence's topic `t`) that a learner of this sentence
  would plausibly make, with the concrete wrong text: `[libId, wrongText]` replaces the locked span in every variant;
  `[libId, wrongText, anchor]` replaces the anchor text instead; optional 4th element `{{"slot":"value"}}` for every extra slot
  listed after `slots:` in the index (e.g. `{{"base":"stamp"}}`). `[libId, "=full wrong sentence"]` when a replacement cannot
  express it. `[tip]` items are correct-but-not-practised (verdict correct_with_tip); `[wrong]` items are errors. The wrong
  text must really be wrong for the item's kind (never a correct sentence under a [wrong] item).
- Be terse; do not deliberate at length per sentence. Output only the file.

## Sentences (one JSON object per line; `long` = 13–16-word sentence)
'''

def build(batch):
    ids = sel['batches'][batch]
    out = os.path.join(P1C, 'annotated', f'batch{batch}.json')
    text = RULES.format(B=batch, N=len(ids), OUT=out)
    long = {x['id']: x['long'] for x in sel['items']}
    for i in ids:
        r = a[i]
        text += json.dumps({'id': i, 't': r['type_id'], 'topic': r['topic'], 'lv': r['level'], 'long': long[i], 'en': r['en'], 'ans': r['en_answer'], 'sk': r['sk']}, ensure_ascii=False) + '\n'
    text += '\n## LIBRARY INDEX (topics of this batch only): id [wrong|tip] pattern (slots: extra slots to fill)\n'
    for t in sorted({a[i]['type_id'] for i in ids}):
        d = lib.get(t)
        if not d: text += f'## {t} (library missing — use no m)\n'; continue
        text += f"## {t} {d.get('topic','')}\n"
        for it in d['items']:
            extra = [s for s in it.get('slots', []) if s not in ('right', 'wrong')]
            text += f"{it['id']} [{'tip' if it['verdict']=='correct_with_tip' else 'wrong'}] {it.get('pattern') or it.get('kind')}" + (f" slots:{','.join(extra)}" if extra else '') + '\n'
    path = os.path.join(P1C, 'tasks', f'batch{batch}.md')
    open(path, 'w').write(text)
    print(path, len(ids), 'sentences', len(text), 'chars', len({a[i]['type_id'] for i in ids}), 'topics')

for b in ('S', 'L'): build(b)
