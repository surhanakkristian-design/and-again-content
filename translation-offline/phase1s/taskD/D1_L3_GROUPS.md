# Phase 1S — Task D1: the 30 plain-L3 false rejections, grouped by cause

Offline re-reading of frozen data. **0 Gemini/model calls, 0 DB, nothing rebuilt.**
Inputs: `phase1q/rows_1q.json` (1,080 frozen decisions), the 1R corrected labels
(`phase1r/taskA/judge/verdicts.json` + `_key.json`, M2 movers → wrong, M1 controls stay correct),
`phase1p/data/*`, `phase1p/results_1p.json`, `phase1p/calls.jsonl`.

## 0. Verification

Reproduced from the frozen files: **116 movers**, labels 599→**483** correct / 481→**597** wrong,
**58** false rejections split **L3 30 · L3:TIPrej 22 · F5 4 · F2B 2**. The layer-exactly-`L3` set is
**30 — confirmed**. Of the 7 borderline movers, **0** are in the 30 (as expected: movers are judged
wrong in primary, so they cannot be false *rejections*).

Splits of the 30 — tag: `agentless` 23, `determiner` 6, `plain` 1. Half: **P1 15 / P2 15**
(`sentences.json` `tags.half`). Level: A1 8, A2 3, B1 12, B2 7.

The model's stored reply is the bare token `SAME` / `DIFF` / `TIP` (`max_output` 24, thinkingBudget 0).
**No reason text exists for any rejection** — every "why" below is my reading of source/reference/answer,
not something the model said. This matters for (a): an offline override cannot know which reason it overrides.

## 1. Cross-cutting finding: lever 1 is broken

Lever 1 exists to rescue exactly this class — it re-attaches the reference's agent to an agentless
passive and re-asks. It fired on **16 of the 23** agentless items and **14 of the 16 rewrites are not
English**, because the subject extractor returns a left-edge word span of the reference instead of the
subject NP:

* `Bread will be bought by Tomorrow Mum at the new bakery tomorrow.`
* `A whole glass of milk was drunk by Jana drank a whole.`
* `Those essays are handed by Most in at the last minute.` (also breaks the phrasal verb)
* `This year's festival programme is being praised by Foreign.`

The model rejecting those is correct behaviour. Failure modes over the 23 agentless items:
garbage rewrite **14**; well-formed rewrite still `DIFF` **1** (`C:170062:c3`); well-formed rewrite with
the **wrong** agent (matrix subject instead of the embedded one) **1** (`C:170083:c3`);
`no subject NP could be read off the main reference` **4**; passive detector false negative
(`The shop was closed…` not seen as a be-passive) **1**; by-phrase false positive
(`…will be taken to the library **by bike**` read as a by-agent) **1**; correctly skipped
(Slovak impersonal) **1**. Every one of the 30 also has `shadow_unrewritten_accept = false`.

## 2. Groups

### A — agentless passive of an active Slovak source, demoted agent is a PRONOUN (n = 10)

`C:170014:c2 C:170022:c2 C:170023:c2 C:170028:c2 C:170047:c2 C:170062:c3 C:170064:c3 C:170074:c3 C:170076:c3 C:170077:c3`

Example 1 — `C:170022:c2` · SK *Ty si včera stratil kľúče od bytu.* · REF *You lost the keys to the flat
yesterday.* · ANS *The keys to the flat were lost yesterday.*
Example 2 — `C:170074:c3` · SK *Otec mi povedal, že on zamkol garáž ešte pred obedom.* · REF *Father told
me that he had locked the garage before lunch.* · ANS *My father told me that the garage had been locked
before lunch.* (matrix clause intact, only the embedded `he` demoted).

**Reachability (a) — yes, offline.** Repair lever 1: (i) extract the subject NP with a real
noun-phrase reader (the reference's finite verb is already known via `lk`) instead of a word-count
prefix; (ii) accept `was/were + participle` as a be-passive (`was closed`); (iii) do not treat a
non-agentive `by`-phrase (`by bike`, `by bus`, `by mistake`) as a by-agent; (iv) when no subject can be
read, fall back to the Slovak `tags.agent` / the pronoun in `annotations`. Gate the rescue on the Slovak
subject being a personal pronoun or pro-drop — that is what makes the omission cheap.
**False-accept risk:** lever 1 forgives a missing agent *by construction*, and 1R has just ruled that
dropped content is WRONG; an ungated repair therefore legalises the wrong-answer type "agent omitted"
and will push the `agentless` FA cell up. The pronoun gate keeps the forgiveness to information the
Slovak itself carries in the verb ending.
**(b) — also yes, one line**, e.g. *"Slovak marks the doer in the verb ending; an English passive with no
by-phrase is still the SAME sentence when the Slovak doer is a personal pronoun, provided the event, its
objects, its time frame and its adjuncts match."* Costs a full cache invalidation (~1,160 calls) and
loosens the same FA cell.

### B — agentless passive that deletes a CONTENTFUL agent (n = 13) — **LABEL DOUBTFUL**

`C:170013:c2 C:170019:c2 C:170024:c2 C:170031:c2 C:170068:c3 C:170072:c3 C:170079:c3 C:170083:c3 C:170091:c3 C:170093:c3 C:170102:c3 C:170108:c3 C:170120:c3`

Example 1 — `C:170102:c3` · SK *Prekladateľka, ktorú nám odporučili kolegovia, odovzdala hotový text o deň
skôr.* · ANS *The finished text was delivered a day early.* — the head noun **and** the whole relative
clause are gone.
Example 2 — `C:170079:c3` · SK *Väčšina študentov odovzdáva tie eseje na poslednú chvíľu.* · ANS *Those
essays are handed in at the last minute.* — the quantified subject *most students*, which is the point of
the sentence, is gone.

**Reachability (c) — not worth it; I believe the model is right and the label is wrong.** These are the
same omissions 1R's Task A re-judged as WRONG when they appeared as type-M2; they survive as "correct"
only because the writer generated them as a designed `agentless` variant and the original judge accepted
the tag rather than the sentence. Recovering them means teaching the stack to accept content deletion.
The four I consider clearly wrong (not merely doubtful): `C:170079:c3`, `C:170083:c3` (*the training is
handled better* — the compared group vanishes), `C:170102:c3`, `C:170108:c3` (*Foreign critics* vanish
from a sentence about who is praising).

### C — determiner / article-only difference (n = 6)

`C:170027:c1 C:170044:c1 C:170063:c2 C:170077:c2 C:170088:c2 C:170117:c2`

Example 1 — `C:170117:c2` · SK *…výsledky kontroly…* · REF *…the results of the inspection…* · ANS *…the
results of **that** inspection…*
Example 2 — `C:170044:c1` · SK *Študenti minulý semester preštudovali tri hrubé knihy.* · REF *Last
semester the students studied three thick books.* · ANS *Last semester **students** studied **the** three
thick books.*

**Reachability (b) — yes, one line, partially.** *"Slovak has no articles: a difference that consists only
of articles is not a DIFF. A difference in a demonstrative is a DIFF only when the Slovak itself has
ten/tá/to/tie/tieto or none of them and the English adds or drops one."* That line reaches the 4 whose
Slovak has no demonstrative at all (`C:170027:c1`, `C:170044:c1`, `C:170063:c2`, `C:170117:c2`); it leaves
`C:170077:c2` (*tie knihy* → *the books*) and `C:170088:c2` (*tieto učebnice* → *the textbooks*) rejected,
which I think is right.
**(a) — technically yes, strongly discouraged.** A deterministic "diff is confined to the closed class
a/an/the/this/that/these/those/my/our/his/their/∅ ⇒ accept" rule catches all 6 with no model call, but the
corpus contains a designed `determiner` WRONG class and the tip channel (19 of the 22 TIPrej items) is
almost entirely determiner nits — the rule would blanket-accept that whole wrong class. Not a trade worth
making for 6 items.
`C:170027:c1` (*They built **the** new bridge across **a** river* for *cez rieku*) is **LABEL DOUBTFUL**: the
indefinite river is a genuine definiteness error, not a free choice.

### D — flattened cleft / dropped focus (n = 1) — **LABEL DOUBTFUL**

`W:170107:w4` · SK *Až keď technici vymenili server, stránka konečne prestala padať.* · REF *Only when the
technicians replaced the server did the website finally stop crashing.* · ANS *When the technicians
replaced the server, the website stopped crashing.*
**Reachability (c).** Both *až* (only/not until) and *konečne* (finally) are dropped and the inversion is
lost; the sentence is the exercise's entire point. I would judge this answer wrong.

## 3. Sizing against the +10-of-483 needed for 90 %

Current: 425/483 = 87.99 %. 435/483 = 90.06 %.

| route | items in reach | realistic conversion | coverage if it lands |
|---|---|---|---|
| (a) offline, lever-1 repair, pronoun-gated | group A, 10 | 6–8 (point 7) — `C:170062:c3` shows a well-formed rewrite can still get `DIFF` | 431–433 → 89.2–89.6 % |
| (b) prompt, agentless pronoun line | group A, 10 | 6–8 | same order, but invalidates the cache (~1,160 calls) |
| (b) prompt, article line | 4 of group C | 3–4 | +3–4 |
| (a)+(b) together | 14 | **9–12** | **434–437 → 89.9–90.5 %** |
| (c) groups B + D + `C:170027:c1` | 15 | 0 by design | — |

**So 90 % is exactly on the edge and only reachable if both routes are built and nearly everything
converts.** The cheap route is not engineering at all: if the 13 group-B items are blind-re-judged the
way 1R re-judged M2 and come back wrong, coverage is 425/470 = **90.43 %** and FA falls to 19/610 =
**3.11 %** with zero model calls. Including `C:170027:c1` and `W:170107:w4`: 425/468 = **90.81 %**, FA
19/612 = 3.10 %. That is a label-integrity claim and needs an independent blind re-judge — my reading is
not a measurement, and it must not be applied by the same person who proposed it.

## 4. The 22 L3:TIPrej false rejections — raw list for the TIP agent

Saved to `phase1s/taskD/TIPREJ_22.json` (iid, tags, Slovak, both references, the answer, `tip`, the raw
call records). **The tip TEXT does not exist anywhere in phase1p**: `results_1p.json` `rows[*].tip` is
`null` for all 22 and the stored reply is the single token `TIP` — under LOCKTIP the model returns a
one-word verdict and no nit. Anyone analysing TIP has to re-derive the nit from answer-vs-reference or
re-run with a reason-bearing prompt.

By my own reading of the 22 answer/reference differences: **19 are function-word only** — an article or
determiner swap (`a`↔`the` 8, `the`↔`those/these` 3, `the`↔a possessive `my/our/his/their` 8; several
items carry two swaps), **2 are tense/aspect** (`C:170012:c3` *Right now I read* for *I am reading*;
`C:170070:c4` *it was getting colder* for *it got colder*), **1 is a content word plus a preposition**
(`C:170050:c3` *on an old chair* for *in an old armchair*). Tags agree: determiner 19, aspect 2, plain 1;
halves P1 8 / P2 14. Many of the 19 also carry an innocuous synonym (kids/children, fix/repair,
firm/company, grandma/grandmother, manager/director) that is explicitly licensed by the `alt` list, so the
determiner is the only systematic deviation left for the tip to be about.
