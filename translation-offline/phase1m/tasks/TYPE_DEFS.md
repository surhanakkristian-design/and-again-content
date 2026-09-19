# Wrong-answer types and writer intents (Phase 1k conventions, carried into Phase 1m)

Read together with `ACCEPTANCE_RULE.md`. An **intent** is the writer's design intent; it is never a
label. The blind judge's verdict is the only truth, and the judge never sees an intent.

## The six types used by the judge: T / W / M / S / V / E

T / W / M / S verbatim as used since Phase 1c, restated in
`phase1j/CONTEXT_1J.md` lines 212-217 (the source the Phase 1k materials point to):

- **T** — tense / aspect: the right words, the wrong time reference.
- **W** — wrong word: a lexical substitution that changes which thing, person, place, time or quantity.
- **M** — meaning added or dropped: information in the answer that is not in the Slovak, or Slovak
  information missing from the answer (a single adverb, particle, place or time word counts).
- **S** — small slip family: article, preposition, agreement, word form / spelling slips that are still
  wrong English or change the meaning slightly.

**V** — voice, added in Phase 1k. Declared verbatim in `phase1k/taskA/TASK_A_RELABEL.md:10` /
`phase1k/HANDOFF_R.md:13` only as the type list "T / W / M / S / V (voice, new) / E". Its content is
boundary B1 of the acceptance rule, verbatim:

> B1 VOICE. If the Slovak names an agent in the nominative and the answer moves that agent out of subject
>    position or drops it (active -> passive), that is a MISTRANSLATION: WRONG, no points. Where the
>    Slovak is itself impersonal or passive, an English passive is correct.

**E** — appears in the declared type set "T / W / M / S / V (voice, new) / E" and nowhere else:
**no verbatim definition of E exists in the Phase 1k materials.** It was used on a single judged item.
Do not invent one; if a Phase 1m judge needs a residual bucket, the owner must define it first.

## The two Phase 1k writer intents

Verbatim, `phase1k/CONTEXT_1K.md` lines 85-87:

> **Intents** on fresh answers: `C` correct · `T` tense/aspect wrong · `W` wrong word · `M` meaning
> added/dropped · `S` small slip · **`V` active→passive recast** (B1 probe) · **`TF` time-frame shift**
> (B2 probe). `T`/`W`/`M`/`S` keep their Phase 1c–1j definitions (`$J/CONTEXT_1J.md` §6). An intent is
> the writer's *design intent*, never a label: the blind judge's verdict is the only truth.

- **V (active→passive recast / agent demotion)**: take a Slovak sentence that names a nominative agent
  with a transitive verb and write English that moves that agent out of subject position or drops it.
- **TF (time-frame shift)**: keep the words, move the answer into a different time frame (past /
  present / future) than the one the Slovak fixes. By design a TF probe is judged type **T** when the
  judge agrees it is wrong — TF is a writer intent, not a judge type.

## Writer quotas as enforced in Phase 1k (`phase1k/HANDOFF_P.md` §4, `judge/build_judge_input.py:43-46`)

Per sentence: **>= 3 answers with intent C and >= 4 wrong answers**. Overall over the whole set:
**>= 30 V** and **>= 30 TF**. Exact duplicate texts inside one sentence are dropped before the quota
check. Allowed intent values, exactly: `C`, `T`, `W`, `M`, `S`, `V`, `TF`.

One note for consistency: a table in the Phase 1k report labels intent S "subject recast". That is a
label slip in the report; the canonical S definition is the small-slip family quoted above.
