# Translation offline – Phase 1e: three-layer hybrid, measured

18 Sept 2026. Data: frozen Phase 1c sets (235 held-out correct translations, 105 wrong ones). No new
annotations, translations, reviews, sentences or synonym groups. No DB writes, no app code, nothing deployed.
Script and raw logs: `and-again-content/translation-offline/phase1e/` (`run_phase1e.py`, `calls.jsonl`,
`decisions.jsonl`, `results.md`, `results.json`).

Headline: **the hybrid as specified does not reach the target.** Best coverage 76.6 % (target 90 %), and
the cheap model's real false acceptance is 12–14 % (target ≤ 2 %). Latency and cost of Flash-Lite are fine.
Both misses have a specific, offline-fixable cause (§2, §7).

## 1. Results per model × prompt variant

Sanity first: L1 reproduces Phase 1c exactly — 100/235 = 42.6 %, 0 real false acceptances of 105.

Routing (identical for every configuration, no model involved):

| set | L1 offline accept | L2 grammar veto | reaches L3 |
|---|---|---|---|
| 235 correct | 100 (42.6 %) | 48 (20.4 %) | 87 (37.0 %) |
| 105 wrong | 9 (all judged not-real in Phase 1c) | 39 (37.1 %) caught, no model call | 57 (54.3 %) |
| all 340 | 109 (32.1 %) | 87 (25.6 %) | 144 (42.4 %) |

Wrong answers by type — L1 / L2 / L3: T 6/20/2 of 28 · W 0/10/16 of 26 · M 2/1/21 of 24 · S 1/8/18 of 27.
**Model call rate in production: 37 % of correct answers, 54 % of wrong ones.**

| configuration | L3 items | coverage /235 (baseline 42.6 %) | REAL false acceptance /105 | by type (accepted / reached L3) | L2 caught, no call | latency warm median / p95 (cold) | tokens in / out / thoughts | $ per L3 call | $ per active user / month |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 Flash-Lite × P-A | 144 | **76.6 %** (180) | **15 = 14.3 %** | T 1/2 · W 0/16 · M 11/21 · S 3/18 | 39 | 815 / 1104 ms (908) | 123.0 / 1.0 / 0 | $0.000032 | $0.0072 |
| 3.1 Flash-Lite × P-B | 144 | 75.3 % (177) | **13 = 12.4 %** | T 0/2 · W 0/16 · M 11/21 · S 2/18 | 39 | 875 / 1239 ms (–) | 148.5 / 1.0 / 0 | $0.000039 | $0.0086 |
| 3.7 Flash × P-B | 144, **38 unparsed** | 66.0 % (155) – not valid, see note | 2 = 1.9 % – lower bound, see note | T 1/2 · W 0/16 · M 1/21 · S 0/18 | 39 | 2362 / 9178 ms (2076; probe 7435) | 148.5 / 1.1 / 46.3 | $0.000289 | $0.0643 |
| 3.7 Flash × P-A | CUT – 4 × 144 = 576 calls would exceed the 500 cap | | | | | | | | |

Notes.
- "Real" false acceptance excludes the 9 L1 accepts that Phase 1c already judged valid readings / tip-accepts
  (they are carried unchanged into every row; the script's raw FA column shows 24 / 22 / 11 including them).
  Every L3 accept of a wrong-set item is counted as real – no re-review was done.
- **3.7 Flash row is a damaged measurement.** The model ignores `thinkingBudget: 0` and rejects
  `thinkingLevel: "minimal"` with HTTP 400, so it always thinks (46 thought tokens per call on average, billed
  as output). With the cap raised from 8 to 64 tokens, 38 of 144 replies were still cut off before the verdict
  (27 on correct items, 11 on wrong items) and were counted as rejections. On the parsed items only: 55 of 60
  correct accepted (→ about 76 % end-to-end if the rest behaved alike) and 2 of 46 wrong accepted (→ about
  2.4 %; hard bounds 1.9 %–12.4 %). This is an apparatus failure, not a model verdict.
- Cost: 20 exercises × 30 days × 37.0 % L3 share = 222 calls per user per month. At the wrong-answer share
  (54 %) it would be 324 calls: $0.010–0.013 on Flash-Lite. Cached tokens were 0 on every call: a 125–150 token
  prompt is below the implicit-caching minimum, so the $0.025 cached rate never applies. The brief assumed
  330 in / 5 out; measured is 123–150 in / 1 out.
- 3.7 Flash price from ai.google.dev/gemini-api/docs/pricing (fetched 18 Sept 2026): $0.75 in / $3.75 out incl.
  thinking, doubling on 1 Jan 2027.
- Latency is measured from this Mac straight to AI Studio, sequential calls. The extra hop through an edge
  function is not included.

## 2. Best safe configuration

**There is none yet.** No configuration meets ≤ 2 % real false acceptance with a valid measurement.

Closest: **3.1 Flash-Lite × P-B** – coverage 75.3 %, real false acceptance 12.4 % (13/105), split L1 42.6 % /
L2 20.4 % / L3 37.0 % of correct answers, 875 ms median / 1239 ms p95, $0.000039 per call, $0.0086 per user per
month. P-B (grammar declared as already verified) removed the one tense acceptance P-A made ("she will came
back" → TIP) and cost 3 correct answers; it is the better prompt.

Why it misses, precisely:
1. **False acceptance is one failure class.** 11 of the 13 are type M, and all 11 are pure deletions from the
   reference ("the whole chair wobbles" → "the chair wobbles", "…would be on the floor by now" → "…on the
   floor"). The model calls a dropped modifier TIP. The other 2 are subject swaps (I for you, they for she).
   **Wrong word: 0 of 16 accepted, in all three configurations.** A deletion check is offline work: learner
   tokens are a subsequence of the reference tokens and a content word is missing → reject with "missing
   meaning" feedback, no model call. By eye that would leave 2/105 = 1.9 % – a projection, NOT measured, and
   its effect on correct answers ("blowing out candles" vs "the candles") is unmeasured, so it must ignore
   articles.
2. **Coverage is capped at 79.6 % by L2, not by the model.** L2 vetoes 48 correct translations before the model
   ever sees them. I listed them (audit, main session): the veto as implemented tests whether the literal `lk`
   span from the Phase 1c annotation occurs in the answer, and that span contains the lexical verb. Rough
   by-eye split of the 48: about 17 have the practised grammar intact with a different verb or word inside the
   span ("will lower" vs lock "will drop", "will have reserved" vs "will have booked"); about 10 are pure
   string artefacts (contractions "she's dancing", an adverb inside the span "has finally stamped", the gap
   pattern "had .. filmed", a pronoun inside the span); 4 are article/quantifier alternatives; about 18 really
   use a different grammar ("have to" for "must", "is able to" for "can", "rolled" for "were rolling", zero
   relative clause). So roughly 27 of the 48 are false vetoes of a too-literal lock, not grammar departures.
   The L3 model accepted 89–92 % of the correct answers it saw. If those ~27 reached it, coverage would be about
   86–87 %; the last ~18 are a product decision (valid English that avoids the practised structure: reject, or
   accept with a "use the target structure" tip → about 93 %). Projections, not measurements.
3. The rule "grammar is never judged by the model" is confirmed: only 2 tense errors leaked to L3 and each was
   accepted once ("will came" by Flash-Lite P-A, "must held" by 3.7 Flash). Any loosening of L2 must stay an
   offline structural check (auxiliary pattern + any verb in the right form), never a hand-over to the model.

## 3. Disagreements with the Phase 1c judgement

A = Flash-Lite P-A, B = Flash-Lite P-B, F = 3.7 Flash P-B. "–" = agreed with Phase 1c (or, for F, unparsed).

**Correct translations the model rejected (DIFF)** – 7 / 10 / 5:

| id | Slovak | reference | learner answer | A | B | F |
|---|---|---|---|---|---|---|
| 29691 | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He's going to drop his guide on the church steps! A total catastrophe! | DIFF | DIFF | unparsed |
| 29691 | 〃 | 〃 | He will drop his guidebook on the church steps! A complete catastrophe! | – | DIFF | unparsed |
| 16261 | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | She's got a plan. She is going to accompany her home. | DIFF | DIFF | unparsed |
| 16403 | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say goodbye - he will return in an hour. | DIFF | DIFF | DIFF |
| 27628 | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven o'clock in the morning. | DIFF | DIFF | unparsed |
| 27628 | 〃 | 〃 | The children will wake up at seven in the morning. | DIFF | DIFF | – |
| 26084 | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find her before he gets home. | DIFF | DIFF | DIFF |
| 26084 | 〃 | 〃 | He can find it before he comes home. | DIFF | DIFF | DIFF |
| 21124 | Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi. | She usually stays dry, but today she is dancing in the rain. | He usually stays under the roof, but today he is dancing in the rain. | – | DIFF | – |
| 21124 | 〃 | 〃 | She usually stays indoors under the roof, but today she is dancing in the rain. | – | – | DIFF |
| 8293 | Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný. | She never shares food, so this one must be special. | He never shares food, so this particular croissant must be exceptional. | – | DIFF | unparsed |

Pattern: nearly all are cases where the learner follows the SLOVAK and the reference does not – the dropped
Slovak subject (he/she/it), a reference in present tense for a Slovak future, "stays dry" for "pod strechou".
The model sides with the English reference. A prompt line saying that the Slovak is the ground truth and that
an unmarked subject may be he, she or it would address this; not tested (variant list was fixed, budget left).

**Wrong translations the model accepted** – 15 / 13 / 2:

| id | type | reference | learner answer | A | B | F |
|---|---|---|---|---|---|---|
| 16403 | S | Say bye now and she will come back in an hour. | Say bye now and they will come back in an hour. | TIP | – | – |
| 16403 | T | 〃 | Say bye now and she will came back in an hour. | TIP | – | – |
| 24733 | T | The glass is hot, so you must hold it carefully. | The glass is hot, so you must held it carefully. | – | – | TIP |
| 4612 | M | If he held the screwdriver, that shelf would be on the floor by now. | …that shelf would be on the floor. | TIP | TIP | – |
| 9907 | M | If she had taken the beige jacket, this look would never have happened. | …this would never have happened. | TIP | TIP | – |
| 14266 | M | What do they dance? — Salsa. | What do they dance? | TIP | – | – |
| 11348 | M | Look! The assistant is holding the reflector up now. | Look! The assistant is holding the reflector. | TIP | TIP | – |
| 11980 | M | Wait a minute and the water will boil! | Wait and the water will boil! | TIP | TIP | – |
| 1452 | M | …he will spend the evening pulling spines out of his finger. | …pulling spines out. | TIP | TIP | – |
| 9244 | M | …the black cat did not move a whisker. | …the black cat did not move. | TIP | TIP | – |
| 4571 | M | If you leave one screw loose, the whole chair wobbles. | …the chair wobbles. | TIP | TIP | TIP |
| 4571 | S | 〃 | If I leave one screw loose, the whole chair wobbles. | TIP | SAME | – |
| 7238 | M | …your feet stay completely dry. | …your feet stay dry. | TIP | TIP | – |
| 8824 | M | While the chain was swinging, he pushed the bag into place. | …he pushed the bag. | – | TIP | – |
| 3494 | M | …she would have gone home with empty pockets. | …she would have gone home. | TIP | TIP | – |
| 3494 | S | 〃 | …they would have gone home with empty pockets. | SAME | SAME | – |
| 8209 | M | By Friday she will have booked a fifth appointment at the studio. | …a fifth appointment. | TIP | TIP | – |

Note that the model almost always says TIP, not SAME, on the omissions – it sees the difference and rates it
minor. Whether "the chair wobbles" for "the whole chair wobbles" is wrong or a tip is your call; under the
Phase 1c judgement it is wrong and is counted so here.

3.7 Flash unparsed replies, 27 on correct items (ids: 8812, 1018, 29691 ×2, 23026, 11348, 7716, 10167, 2955,
8293, 8756, 13034, 27628, 7238, 2874, 21467, 8799, 9966 ×2, 9913 ×2, 9038, 11216, 16261 ×2, 10959, 13395, 7998)
and 11 on wrong items. Full rows in `phase1e/results.md`.

## 4. Harvesting design (not built)

Goal: every L3 SAME on a one-word difference teaches the offline layer, so the same answer is an L1 accept
next time and the 37 % call rate falls with use.

Trigger, all conditions offline and cheap: verdict is SAME (never TIP); after normalisation the learner answer
differs from the reference, or from a stored accepted variant, by exactly one token replaced by one token
(or one stored multi-word unit); the token is outside the locked span; both sides are content words of the same
word class by the lemma list; neither side is in the mistake library.

Flow: the pair does not enter the synonym table. It is written to a candidate table with lemma pair, sentence
id, user id, model, date. A candidate is promoted only when (a) it was seen in at least 3 different sentences
from at least 3 different users, (b) no DIFF verdict exists for the same pair, and (c) a nightly offline batch
– not the runtime path – asks the stronger model about the pair in both directions and gets SAME twice.
Promotion is sentence-scoped first ("lower" accepted for "drop" in sentence 5959 only); a pair becomes a global
synonym group only after it holds in N sentences or after a human look.

What stops a wrong pair:
- The measured weakness of the model is omission and subject leniency (11/21 and 2–3/18 accepted), not word
  substitution (0/16 wrong words accepted in all three configurations, small n). Harvesting uses only the class
  where the model was reliable, and only SAME, which it rarely gave wrongly (2 of 28 accepts).
- Hard exclusions: pronouns, auxiliaries, modals, negation, numbers, prepositions, articles, anything inside
  the lock, antonym list. These carry grammar or meaning flips, and the model must never decide them.
- Sense dependence ("drop the price" = "lower the price", "drop the guidebook" ≠ "lower the guidebook") is
  why scope starts at the sentence, not the word.
- One user can never promote a pair; candidates per user per day are rate-limited (poisoning).
- Every harvested row carries source = harvest, evidence ids and date; one switch disables all harvested rows;
  a later DIFF from the strong model or a content report on a sentence demotes its pairs.
- Audit: 20 promoted pairs sampled weekly; more than 1 wrong in 20 stops automatic promotion.
Residual risk: a systematic model blind spot shared by both models passes (c). The weekly sample is the only
defence against that, so it cannot be skipped.

## 5. Model calls and spend

- **436 of 500 calls used** (4 probe + 288 Flash-Lite + 144 3.7 Flash). 436 HTTP attempts, 0 rate-limit (429)
  responses, free tier throughout – **actual spend $0.00**. List-price equivalent of the same traffic: about
  $0.053 (Flash-Lite 289 calls ≈ $0.010, 3.7 Flash 147 calls ≈ $0.043).
- Variant list cut to fit the cap: 3.7 Flash × P-A not run. Flash-Lite output cap 8 tokens, no thinking, as
  specified. 3.7 Flash could not meet "no thinking / 8 tokens" (see §1 note); its cap was 64.
- A second `--run` with the 3.7 cap at 256 to recover the 38 unparsed replies made **no calls**: the planner
  re-plans from the remaining budget and skipped the stage. It overwrote `results.md` with a reduced table; the
  first-run files were kept and restored. 64 calls remain unused.
- Key handling: read only inside `run_phase1e.py` from `.env.local`, sent as an HTTP header, redacted from all
  error text. `.env.local` is git-ignored (checked with `git check-ignore`: PASS). The script's self-check scans
  every file in `phase1e/`, including a copy of this report, for the key value: PASS. No file created or
  committed contains the key. Edge function untouched.

## 6. Own tokens and call counts

Tool calls: main session 8 (limit 8): 1 agent, 5 shell, 1 read, 1 write. One agent (`tx-opus`, built the script,
dry-run, probe): 10 tool calls (limit 12), 73,698 tokens as reported by the harness. No script-running agents.

`tokens.py` (Phase 1c script, method corrected = final record per message), run at commit time, so the main
session's last message is not included:

```
untagged       calls=  11 in=     22 cc=    71379 cr=    451815 out=  30220 total=    553436 start=14309
main           calls=   9 in=     20 cc=    88486 cr=    760986 out=  36027 total=    885519 start=71390
TOTAL {'input': 42, 'cache_creation': 159865, 'cache_read': 1212801, 'output': 66247, 'total': 1438955, 'calls': 20, 'share_pct': {'input': 0.0, 'cache_creation': 11.1, 'cache_read': 84.3, 'output': 4.6}}
```

## 7. Judgement

1. No. As specified the hybrid reaches 76.6 %, not 90 %, and Flash-Lite's real false acceptance is 12–14 %, not
   under 2 %. 3.7 Flash may be near 2 % but its measurement is damaged and it cannot run without thinking.
2. Both misses are offline problems, not model problems: L2's literal lock vetoes 48 correct answers (ceiling
   79.6 %), and 11 of 13 false acceptances are plain deletions a subsequence check catches without a model.
3. Latency is acceptable on Flash-Lite (0.8–0.9 s median, 1.1–1.2 s p95, only for 37 % of correct answers) and not
   acceptable on 3.7 Flash (2.4 s median, 9.2 s p95). Cost is a non-issue: under one cent per user per month.
4. Synonym annotation at scale is no longer worth doing – the model handled vocabulary (0/16 wrong words
   accepted, ~90 % of correct answers accepted) and harvesting can fill the table from use. What is still worth
   doing is small and structural: locks as grammar patterns instead of literal spans, a deletion guard, a
   subject rule, and one prompt line making the Slovak the ground truth.
5. Those four are cheap to measure on the same frozen sets with the 64 calls left plus a fresh cap; projected
   landing zone is 86–93 % coverage at about 2 % – a projection until measured.
