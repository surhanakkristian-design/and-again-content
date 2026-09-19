# Phase 1T / Task B2 — Czech gold validation of the deterministic guards (PROBE, 0 model calls)

## 0. What ran
`phase1t/taskB/cz_validate.py` runs every **source-side** guard reader UNCHANGED over the 120 pairs of
`cz_sample_numbered.json`: once on `cz`, once on the Slovak sibling `sk` (control). Readers: `phase1n/f9.py`
`sk_frame`; `phase1i/checker_1i.py:536` `sk_features`; `phase1s/taskC/agent_drop_v2.py:118` `slovak_agent` /
`:136` `has_nominative_agent` / `:62` `SK_REFLEX`; `phase1t/taskA/agent_drop_v3.py` (**exists**, v3 was run:
`:384/:424` delegate to `V2.slovak_agent`, `:157` `parse_agent_tokens`, `:276` `sk_clause_is_passive`,
`:320` `agent_gate`, `:462` clause-scoped `SK_REFLEX`). **`ann = {}` and `wtags = {}` everywhere**, as in
production today — no Czech annotation exists (INVENTORY §2), and none of the Slovak annotation files is
keyed to these exercise ids either, so the Slovak control runs annotation-free as well. No crashes.
Gold: `cz_gold.json` / `sk_gold.json`, written blind by two annotators. Full per-row output:
`cz_validation.json` (`safe_dump`). 0 fragments in either gold, so "excluding fragments" = the same 120.

## 1. Definitions
Exactly `phase1k/taskB/validate_f9.py:36-44`: AGREE = predicted set == gold set; CONSERVATIVE = predicted
set empty **or** gold ⊆ predicted; ERROR = the gold value is not in the predicted set.
**Deviations, stated:** (a) for gold `tf = "none"` (conditional / no finite verb) the gold set is empty, so
validate_f9's ordering scores *any* asserted frame as CONSERVATIVE; I keep that, and report the asserted-on-
gold-none cases separately (7 cz, 7 sk) because they are silent over-assertions. (b) For guard 2 I score an
assertion against gold `person = "none"` as ERROR (there is no finite verb to have a person). (c) Guard 3/4
use the class definitions given in the task, not validate_f9's. CIs are exact Clopper-Pearson, n = 120.

## 2. Results (n = 120 per language; no fragments to exclude)
| guard | lang | AGREE | CONSERVATIVE | ERROR | ERROR rate [95 % CI] |
|---|---|---|---|---|---|
| 1 F9 time frame | cz | 82 | 35 | 3 | 2.5 % [0.5, 7.1] |
| 1 F9 time frame | sk | 96 | 23 | 1 | 0.8 % [0.0, 4.6] |
| 2 F4v2 person/number | cz | 17 (9 partial) | 83 | 20 | 16.7 % [10.5, 24.6] |
| 2 F4v2 person/number | sk | 17 (7 partial) | 87 | 16 | 13.3 % [7.8, 20.7] |
| 3 AG agent reader (v2 = v3) | cz | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| 3 AG agent reader (v2 = v3) | sk | 55 | 18 | 47 | 39.2 % [30.4, 48.5] |
| 4 voice, v2 (`SK_REFLEX`) | cz | 108 | — | 12 (6 as_active / 6 as_passive) | 10.0 % [5.3, 16.8] |
| 4 voice, v2 (`SK_REFLEX`) | sk | 98 | — | 22 (4 / 18) | 18.3 % [11.9, 26.4] |
| 4 voice, v3 (+`sk_clause_is_passive`) | cz | 105 | — | 15 (5 / 10) | 12.5 % [7.2, 19.8] |
| 4 voice, v3 (+`sk_clause_is_passive`) | sk | 98 | — | 22 (2 / 20) | 18.3 % [11.9, 26.4] |

Guard 3 v3 is byte-identical to v2 on every row: v3 reads the agent through `V2.slovak_agent` and only
re-tokenises the same string. Gold distribution (cz): tf present 70 / past 27 / future 16 / none 7;
voice active_agent 66 / active_prodrop 48 / impersonal 2 / passive 2 / reflexive_passive 2.
The two blind golds differ in 5 tf cells (15, 26, 28, 31, 46 — perfective-present judgement) and 3 person
cells (92, 115, 118 — real language differences, e.g. cz `záda` 3pl vs sk `chrbát` 3sg); voice and
agent_nom agree on all 120. Cross-language deltas of ≤ 3 rows are inside that annotator noise.

## 3. Guard 1 — F9 time frame: every ERROR
- cz n=15 `Dokáže herec zaplakat na kameru napoprvé? Ano, dokáže.` gold future — guard `['present']`,
  reason *imperfective present "dokáže"*. Spot: `f9.py:30` `PERF_LEX` + `:183 aspect()`; the Slovak
  perfective lexicon has no Czech `dokáže`-type entry. (sk gold says present here — annotator delta.)
- cz n=29 `Jestli vydrží slunce, zkusíme po téhle ještě jednu aktivitu.` gold future — guard `['past']`,
  reason *l-participle "jestli"*. Spot: `f9.py:75` `SUB_MARK` (Slovak `ak`, no Czech `jestli`) feeding
  `:124 _is_l_part` + the `:85-86` `L_NONVERB` exception list, which is Slovak-only. **Czech-specific.**
- cz n=68 and sk n=68 `„barbell“ znamená …` gold present — guard `['past']`, *l-participle "barbell"*.
  Same `:85-86` list; an English loanword, so this one is **not** Czech-specific (it breaks Slovak too).
Net Czech-specific F9 damage on this set: 2 sentences (15, 29). Everything else the Czech gaps cost is
CONSERVATIVE: 35 cz abstentions vs 23 sk (+12 sentences of lost coverage, the `BUD`/`COP`/`MOD`/aspect-list
gaps at `f9.py:21-33, 72, 79, 86`).

## 4. Guard 2 — F4v2 person/number: every ERROR
cz (20): n=17 `…chce stát hercem.` 3sg→**1sg** (`present -m hercem`) · n=21 `Herec čeká v křesle před
záběrem.` 3sg→1sg (`záběrem`) · n=31 3sg→2sg (`pronoun ty`, here the demonstrative "ty rakety") ·
n=36 `Tráva je mokrá. …si musíš obout boty.` 3sg→2sg (`musíš`, second sentence) · n=47 3sg→2sg (`pronoun
ty`) · n=49 3sg→2 (`present -te certificate` — the English headword) · n=50 3sg→2sg (`sedíš`,`opíráš`) ·
n=51 3sg→2sg (`dostaneš`) · n=54 3sg→2sg (`ukážeš`) · n=55 3sg→2 (`present -te roste`) · n=56 3sg→2sg
(`musíš`) · n=61 `„arena“ znamená velká krytá hala se sedadly kolem hřiště` 3sg→**1sg** (`present -m
kolem`, a preposition) · n=62 3sg→2sg (`vystřelíš`) · n=67 3sg→2sg (`pečeš`) · n=79 3sg→1sg (`present -m
sestřenicím`, dative plural) · n=83 3sg→1sg (`present -m ředitelem`, instrumental in a passive) · n=87
3sg→1sg (`present -m jsem`) · n=105 same shape · n=111 3sg→2sg (`pronoun ty`) · n=112 3sg→1sg
(`dalším`,`certifikátem`) · n=118 gold "none" (conditional) → number sg asserted from three l-participles.
sk (16): n=3, 32, 84 (`present -te aktivite/certifikáte` — locative nouns) · n=36, 49, 50, 51, 54, 56, 62,
67 (`-š` inside a relative clause, identical to Czech) · n=87 1sg from `past auxiliary som` · n=96, 116
(`present -š vankúš`) · n=112 (`present -m ďalším`) · n=118 (conditional).
Code spots: `checker_1i.py:555-573` present-ending rules (the `-em` exclusion list `('om','ním','tím',
'ctvom')` is Slovak; Czech instrumental is `-em` and Czech dative pl is `-ím`), `:524` `SK_PREP` (missing
`se/ze/ke/ve`, and it never shields a bare `kolem`), `:458` `SK_PRON` (Czech demonstrative `ty` read as the
pronoun "you"), `:461` `SK_AUX` (Czech `jsem/jsi/jsme/jste` unknown → `jsem` falls through to the `-em`
rule), `:575` `past_marker` (Czech `si` is dative-only), `:529` `SK_L_PART`.
Shared defect, both languages: the whole relative-clause class (`znamená … na které sedíš`) — the guard has
no clause scope, so a 2sg verb in a relative clause overrides the 3sg main clause (11 cz, 8 sk).

## 5. Guard 3 — the AG nominative-agent reader
With `ann = {}` and `wtags = {}` the annotation path is dead, so `slovak_agent` always falls to
`agent_drop_v2.py:124` *"first word of the sentence, unless `SK_REFLEX` matches"*. That heuristic is wrong
on half the corpus in both languages:
- cz 61 ERROR = 40 pro-drop sentences where gold has no nominative subject at all (first word asserted as
  agent: `Na`, `Nudíme`, `Zítra`, `Když`, `Jestli`, `Podívej`, `„Opravdu`…), 17 active_agent sentences where
  the first word is not the subject (n=16 `Na`, 40 `Po`, 73 `Zatímco`, 75 `Ve`, 77 `Než`, 92 `Zatímco`…),
  2 impersonal (32, 48), 2 reflexive_passive (102, 120).
  n = 2,4,6,9,10,11,15,16,17,20,25,27,29,30,31,32,33,34,38,40,41,42,44,45,46,48,73,74,75,76,77,78,79,80,81,
  85,87,88,89,92,93,94,95,98,99,100,101,102,103,105,107,109,110,111,112,113,114,116,117,119,120.
- sk 47 ERROR = 32 pro-drop, 13 wrong-word, 2 impersonal; n = 2,9,10,11,15,16,20,25,29,31,32,33,34,38,40,
  41,42,46,48,74,76,77,78,79,80,81,82,85,87,88,89,92,93,95,98,99,100,101,103,105,107,109,110,113,116,117,119.
- The 53 cz / 55 sk AGREEs are accidental — they are the sentences that happen to start with their subject.
- CONSERVATIVE 6 cz vs 18 sk: Slovak abstains far more often because `SK_REFLEX (sa|si)` fires on `sa`;
  Czech reaches the heuristic instead. This is the Czech delta (+11.7 pp ERROR), and it is caused by the
  missing `se`, not by anything else.
- v3 identical (same reader). v3's `agent_gate` (`:320`) returns `False, 'no annotation evidence of a
  nominative agent'` for all 240 rows, exactly like v2's `has_nominative_agent` — **the whole AG rule is
  inert today in both languages**, which is why none of this reaches the learner yet.

## 6. Guard 4 — passive / reflexive-passive / subjectless: every ERROR
cz, v2 (`SK_REFLEX` only), 12: ERROR_as_active n=32 (impersonal `Po té aktivitě jim nezbylo…`), 48
(impersonal `Na tomhle malém place není moc herců`), 83 (passive `je podepsán ředitelem`), 84 (passive `je
vytištěné`), **102 (`O ní se říká, že…`, reflexive_passive)**, **120 (`O tom žlutém polštáři se věří…`,
reflexive_passive)** — the last two are the predicted `se` miss; their Slovak siblings are caught.
ERROR_as_passive n=5, 8, 18, 19, 36, 118 — all gold active_agent, all fired only on the Czech **dative
clitic `si`** (`si vyberou`, `si myslí`, `si nechává`, `si stoupne`, `si musíš`, `Kdyby si koupil`).
cz, v3 adds 3 (`sk_clause_is_passive`, `:276`/`:86 SK_PPART`): n=7 `je lepší než ležení`, 12 `je
připravený`, 20 `je smutná`, 90 `To je směšné množství` (adjective read as a passive participle), and
recovers 84 (`je vytištěné` correctly seen as passive) — 15 total.
sk, v2 and v3, 22: ERROR_as_active 32, 48 (+83, 84 in v2 only); ERROR_as_passive 3, 5, 8, 18, 19, 27, 36,
43, 44, 49, 50, 59, 60, 71, 73, 75, 97, 118 (+12, 20 in v3) — Slovak `sa/si` on ordinary reflexive verbs.
So on voice the Slovak control is *worse* overall (18.3 % vs 10.0 %), but the Czech errors are of the
dangerous kind: Czech **misses** agentless/reflexive passives (2/2 of them), Slovak over-abstains.

## 7. End-to-end: AG fed the English reference as the learner's answer
`decide(src, {}, {}, en, en, 'primary')`, v2 and v3, both languages: **0 false rejections on cz, 0 on sk.**
Only 4/120 references are marked agentless passives at all under v2's `find_passive` (9/120 under v3's
clause-split), and for those the gate closes with *"no annotation evidence of a nominative agent"*.
Counterfactual (not production): injecting the gold voice/agent_nom as `ann` still yields **0** rejections
on both languages — the references that are agentless passives are not the sentences whose gold says
active_agent-with-agent. So today the AG source-side reader costs nothing on Czech; its 61 wrong agent
reads are latent, and would only fire once Czech annotation is written (INVENTORY §4 said the same).

## 8. Every place a guard reads Slovak-specific material, and what Czech does
Confirmed (with the actual triggering sentences):
1. `f9.py:85-86` `L_NONVERB` — **confirmed, but weaker than predicted.** Only one of the 120 Czech
   sentences contains a Czech `-l/-lo` noun that the Slovak list does not block: n=67 `jídlo` (sk `jedlo`
   *is* listed), and there the frame did not flip (still `present`). The list's real Czech damage on this
   set came from a different token class: the Czech subordinator `jestli` (n=29) and the loanword `barbell`
   (n=68) read as l-participles → asserted `past`.
2. `checker_1i.py:555-573` instrumental `-em` — **confirmed, Czech-only.** 8 Czech sentences produce an
   `-em/-ím` noun signal (17 `hercem`, 21 `záběrem`, 61 `kolem`, 79 `sestřenicím`, 80 `jménem`, 83
   `ředitelem`, 87/105 `jsem`, 112 `dalším`+`certifikátem`); 6 of them become a false 1sg → guard ERROR.
   Slovak: **0** such signals. This is the single clearest Czech-only misfire measured.
3. `agent_drop_v2.py:62` `SK_REFLEX = (sa|si)` missing `se` — **confirmed.** 23 Czech sentences contain a
   standalone `se` that the regex does not see; 2 of them are gold reflexive_passive (n=102, 120) and are
   therefore treated as ordinary active sentences with an agent, both in v2 and in v3's clause-scoped use
   at `:462`. Slovak: 0 missed. The mirror-image effect: Czech `si` (dative only) fires the regex on 6
   active sentences (5, 8, 18, 19, 36, 118).
Other Slovak-specific spots exercised here: `f9.py:21-23` `BUD`/`COP`/`MOD`, `:30-71` aspect lexicon,
`:72` time nouns, `:75` `SUB_MARK`, `:79` `REPORT_V`, `:100` `CLAUSE_SPLIT`, `:484` `WISH_SK` → all
**ABSTAIN** on Czech (35 vs 23 CONSERVATIVE); `checker_1i.py:458` `SK_PRON` (Czech `já` invisible; Czech
demonstrative `ty` misread — n=31, 47, 111 → **MISFIRE**), `:461` `SK_AUX` (`jsem/jsi/jsme/jste`
invisible → **ABSTAIN**, and `jsem` then **MISFIRES** through the `-em` rule at n=87, 105), `:575`
`past_marker` (Czech `si` arms the participle reader on 5, 8, 18, 19, 36, 118; Czech `jsem` does not arm it
on 87, 105 → both directions observed), `:524` `SK_PREP` (`se/ze/ke/ve` missing → the `-em` shield fails),
`agent_drop_v2.py:56-58` `SK_PRON`/`PRON_EQ` (`já` missing → the 1sg mapping abstains), v3 `:84-87`
`SK_BYT`/`SK_PPART`/`SK_CONN` (Czech `byl/byla/je` match, Czech participles in `-ný/-tý` match, so v3's
Slovak passive detector transfers — it over-fires on adjectives in both languages, n=7, 12, 20, 90).
**No crash on any of the 240 runs.**

## 9. Caveats
PROBE, not a measurement: one 120-sentence stratified sample, single blind gold per language, no model
calls, no re-annotation. Guard-3/4 classes follow the task's definitions, not `validate_f9`'s. The two
golds are independent, so a handful of cz/sk cells differ for annotator reasons (§2). `ann = {}` means the
annotation-driven halves of F9's `check`, F4v2's `g` chain and AG's gate were never exercised; everything
above is the surface reader only.
