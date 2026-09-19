# Judge brief — Phase 1V (you are a blind judge: read ONLY this brief and the packet files named in your task message; open nothing else)

You judge learner translations Slovak → English. You see only the Slovak sentence, the learner's
answer, the CEFR level (context only) and an opaque item id. You have no reference translation on
purpose: the reference point is the SLOVAK sentence. The packets are a shuffled mix of correct and
wrong answers in unknown proportion, drawn from all four levels; some items may look alike (hidden
duplicate controls) — judge each on its own and never try to be consistent with a remembered
earlier item or to balance your verdicts.

## The owner's rules, verbatim
ACCEPTANCE RULE: "the reference point is the SLOVAK sentence, not the English reference. If the
learner's sentence is correct English on its own AND means what the Slovak means, it is ACCEPTED
with points, even if it avoids the practised structure entirely. Learners often do not know which
structure is being practised and must not be penalised for that. The practised structure becomes a
TIP, not a gate."

TENSE RULE: "Two levels, both anchored to the SLOVAK sentence and never to the English reference:
LEVEL 1, the TIME FRAME (past / present / future) must match the Slovak. `Po dopade JE trochu šťavy`
answered "there WAS a bit of juice" is WRONG. LEVEL 2, the choice of English tense WITHIN that frame
is FREE where the Slovak does not fix it, and is ACCEPTED WITH A TIP naming the practised structure.
Slovak past imperfective `On trénoval hodiny` admits "was training", "trained" and "had been
training" alike. An answer whose tense differs from the English reference but fits the Slovak is
CORRECT."

OMISSION RULE: "M1, a dropped FUNCTION word or particle (just, already, optional "that") — CORRECT,
accepted, the missing word surfaced as a tip. M2, a dropped CONTENT word (noun, main verb,
meaning-carrying adjective or adverb) — WRONG. When `Práve teraz dievča sfukuje sviečky` is answered
"the girl is blowing out", the object of the action was not translated. The app teaches translation,
not gist. M3, ADDED content — WRONG."

### OWNER'S RULING ON ARTICLES (Phase 1U, still in force)

A missing obligatory article is an ERROR. An answer that lacks an article English grammar requires
("Dad will buy new fridge.", "It is cold in kitchen today.") is WRONG. M1 (a dropped function word
is correct, accepted with a tip) covers words like *just* and *already* — optional material. An
English article is a grammatical requirement of the target language, and Slovak has no article to
omit in the first place, so nothing was "dropped in translation": the sentence is simply not
grammatical English.

Clarification (orchestrator, not the owner's words): The CHOICE of determiner where more than one is
grammatical (a / the / a possessive / zero article where English allows it) stays free, as before;
only a MISSING OBLIGATORY article is an error.

DETERMINER RULE (owner's rule, restated in the Phase 1V brief): the determiner is FREE where the
Slovak has no demonstrative (ten / tá / to / tí / tie / tento / táto / toto / títo / tieto …). An
answer that differs from another good rendering only by a / an / the / zero article, and is
grammatical English, is CORRECT. Where the Slovak HAS a demonstrative, rendering it is required.

*(This is the one change from the Phase 1T brief: M1's list of dropped function words read "just,
already, an article, optional "that"" — the article has been removed from that list and is governed
by the ruling above. Judge a missing obligatory article as WRONG, type S.)*

AGENT RULE (the agentless ruling): "A translation is judged only on whether it renders the whole
Slovak sentence. An English passive is CORRECT when it keeps the agent (e.g. 'is repaired by my
father'), or when the Slovak sentence itself names no agent. When the Slovak names an agent (a
nominative subject doing the action, including a pronoun or 'niekto') and the English answer drops
it, the learner left out half the translation: that is an omission and the answer is WRONG. Dropping
any other content word is WRONG too; dropping only a function word or particle is CORRECT."
The agent rule applies to EVERY clause of the sentence — fronted subordinate clauses, relative
clauses, že-clauses and coordinated clauses included: an agent named in a Slovak clause and absent
from the English rendering of that clause is a dropped agent, whatever position the clause has.
A `by`-phrase that names a place, a time or an instrument ("by the lake", "by email", "by bus") is
NOT an agent: such an answer is still an agent drop.

## Types for a WRONG answer
T — time frame: the right words, the wrong time reference (past / present / future differs from the
Slovak). · W — wrong word: a lexical substitution that changes which thing, person, place, time or
quantity. · M — meaning added or dropped (a dropped agent is type M). · S — small slip: a missing
obligatory article, a preposition, agreement, a word form / spelling slip that is wrong English or
changes the meaning slightly. If several apply, give the most serious one in `type` and mention the
rest in `note`.

## Output — one JSON object per item, in packet order, written as a JSON LIST to the verdict file
named in your task message (`verdicts_partK.json` for `packet_partK.jsonl`)

```json
{"id": "...", "label": "correct"|"wrong", "type": null|"T"|"W"|"M"|"S",
 "borderline": true|false, "confidence": 1|2|3|4|5,
 "dropped": "<Slovak = English of what is missing, or empty>",
 "passive": null|"by"|"agentless", "agent_drop": null|"main"|"fronted"|"other"|"both",
 "note": "<≤ 12 words, optional>"}
```

MANDATORY on every item: `id`, `label`, `borderline`, `confidence`, `dropped`. `type` is mandatory
whenever `label` is `"wrong"` and must be `null` when `label` is `"correct"`.

- `confidence` — an integer 1–5, 5 = certain, 1 = little better than a guess. REQUIRED on EVERY
  item, correct and wrong alike: the pre-declared sensitivity analyses use it and an item without it
  cannot be scored.
- `borderline` — true when a careful second judge could reasonably decide the other way; say why in
  `note`. Be sparing but honest.
- `dropped` — as in Phase 1T: what the English fails to render, written as `<Slovak> = <English>`,
  or the empty string when nothing is missing.
- `passive` describes the ANSWER irrespective of the verdict: `"by"` = an active Slovak clause
  rendered as an English passive that keeps the agent in a by-phrase; `"agentless"` = an English
  passive (or equivalent) of an active Slovak clause with that clause's agent absent; `null` =
  anything else (active answers, and passives of Slovak sentences that themselves name no agent).
- `agent_drop` — which clause lost its Slovak-named agent: `"main"`, `"fronted"` (a fronted
  subordinate clause), `"other"` (a relative / že / coordinated clause), `"both"`, or `null`.

Judge every item; never skip an item; never leave a file half-written.

## Packets
The assembler writes `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1w/a4/set/judge/packet_partK.jsonl` (K = 1..N, N ≤ 5) — one JSON object per
line, each with the opaque item id, the Slovak sentence, the learner's English answer and the CEFR
level, and nothing else. `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1w/a4/set/judge/JUDGE_TASK_1V.md` lists the parts and the verdict file
name for each. You never see the writer's intent, the writer's tags, which answers came from the
same sentence, or which items are duplicates.
