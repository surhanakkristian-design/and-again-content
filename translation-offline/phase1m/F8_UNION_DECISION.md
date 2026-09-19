# Phase 1M — F8u (F8v2 OR F8v1) union: measurement and DECISION

**DECIDED ON ALREADY-SEEN DATA, BEFORE THE NEW PHASE 1M SET WAS OPENED.**
Every number below comes from `dev`, `replay1j` and `fresh1l` — CLOSED sets whose model verdicts
were produced and whose judge labels were read in earlier phases — plus the 210-sentence blind
hand gold of `phase1m/f8gold`, which was also built and used before this decision. Nothing here
is evidence about an unseen set. It can only *rank* two candidate guards. 0 model calls, 0
network, 0 DB; label `f8-union`; every data read is in `phase1m/access_log.jsonl`.

## 0. The pre-registered rule (set by the main session BEFORE this measurement)

> ADOPT `f8u` iff
> (a) union gold ERRORs <= 4 of 210 (i.e. <= 2 %), AND
> (b) `f8u` fires on at most 1 judged-CORRECT item over the three sides combined, AND
> (c) `f8u.selftest()` passes.
> Otherwise keep `f8v2` alone.

## 1. Why a union was considered

`TIP_READOUT.md` finding (a): F8v2 is **not** a superset of F8v1 on FRESH1L. It catches the 8
known agent-demotion false acceptances, but it LOSES four plain `be + PP + by` passives that the
1L F8 rejected (`W:140001:3226349339`, `W:140003:312397117`, `W:140012:213263887`,
`W:140021:1964329415`) — the gold-validation fixes made `sk_clauses()` abstain on their Slovak
side (a clause-initial common noun is no longer asserted as the agent, only a mid-clause proper
name). The brief defines F8v2 as agent demotion INCLUDING the passive, so the candidate fix is
`f8u` = reject if F8v2 rejects OR F8v1 rejects.

## 2. The module

`phase1m/f8u.py`: same interface and return shape as `f8` / `f8v2`
(`check`, `sk_agent`, `en_passive`, `sk_clauses`, `en_clauses`). `check()` returns the F8v2
rejection unchanged if F8v2 rejects; otherwise the F8v1 rejection (`f8_source = "f8v1"`, reason
prefixed `F8v1:`, the v1 dict kept under `v1`) if F8v1 rejects; otherwise the F8v2 pass/abstain
result unchanged. Every result carries `f8_source`.

**selftest: 49 / 50 pass — criterion (c) FAILS.** All 43 inherited F8v2 cases still hold (the
union never turns an F8v2 `accept` into a `reject` on them) and 6 of the 7 new cases pass,
including all four real lost by-passives. The failure is a *new* synthetic case I added,
`Peter napísal ten list.` -> `That letter was written by Peter.`, which f8u leaves at `abstain`:
F8v2 abstains on the Slovak side (`content token before the verb may be the subject`) and F8v1
fails on the ENGLISH side — `f8.en_passive()` counts the leading determiner "That" in its
relative/subordinate-marker counter (`rel`), and that counter then swallows the very next
`was written` verb group (probe: `written` IS in `f9.PP_ALL`, the subject is read as `letter`,
and the returned reason is `no passive main clause found`). So F8v1's passive detector is itself
determiner-fragile: it catches `An apple cake was baked ...` but not `That letter was written ...`.
The failing case is therefore a genuine gap of the union, not a harness artefact, and it is
reported rather than removed.

## 3. Gold validation — the F8v1 Slovak side and the union, same gold, same definitions

`phase1m/validate_f8u_gold.py` imports `validate_f8v2.py` and reuses its `cp()`, `same()`,
`g_val()`, `s_val()`, `show_*()` and its AGREE / CONSERVATIVE / ERROR rules verbatim; inputs are
`existing_210.json` (Slovak only) and `f8gold/gold_part{1,2}.json`. `f8.sk_agent()` is
SENTENCE-level (at most one agent per sentence), so it is scored as a ONE-clause readout: with a
one-clause gold the equal-length branch applies, with a multi-clause gold the clause split
differs and validate_f8v2's split-mismatch branch applies (an asserted agent must match SOME
gold agent of the sentence). `agent_nom = False` ("passive"/"impersonal") asserts no agent and
can never make `f8.check()` reject, so it counts as an abstention.
UNION row class = ERROR if either readout errs, else AGREE if either agrees, else CONSERVATIVE.

### F8v1 (`f8.sk_agent`)

| side | n | agree | conservative | error | error rate | CP 95 % (exact) |
|---|---|---|---|---|---|---|
| DEV | 70 | 19 | 44 | 7 | 10.00 % | [4.12, 19.52] |
| HOLDOUT | 70 | 21 | 38 | 11 | 15.71 % | [8.11, 26.38] |
| FRESH1K | 70 | 46 | 22 | 2 | 2.86 % | [0.35, 9.94] |
| ALL | 210 | 86 | 104 | 20 | 9.52 % | [5.91, 14.33] |

### F8v2 (`f8v2.sk_clauses`, re-measured by this script — reproduces F8V2_VALIDATION.md)

| side | n | agree | conservative | error | error rate | CP 95 % (exact) |
|---|---|---|---|---|---|---|
| DEV | 70 | 34 | 36 | 0 | 0.00 % | [0.00, 5.13] |
| HOLDOUT | 70 | 30 | 40 | 0 | 0.00 % | [0.00, 5.13] |
| FRESH1K | 70 | 43 | 27 | 0 | 0.00 % | [0.00, 5.13] |
| ALL | 210 | 107 | 103 | 0 | 0.00 % | [0.00, 1.74] |

### F8u UNION

| side | n | agree | conservative | error | error rate | CP 95 % (exact) |
|---|---|---|---|---|---|---|
| DEV | 70 | 38 | 25 | 7 | 10.00 % | [4.12, 19.52] |
| HOLDOUT | 70 | 32 | 27 | 11 | 15.71 % | [8.11, 26.38] |
| FRESH1K | 70 | 54 | 14 | 2 | 2.86 % | [0.35, 9.94] |
| ALL | 210 | 124 | 66 | 20 | 9.52 % | [5.91, 14.33] |

**Union gold ERRORs = 20 / 210 = 9.52 % — criterion (a) FAILS (bar: <= 4 / 210 = 2 %).**
All of them are F8v1's: F8v2 contributes 0. The causes are the ones F8v2 was built to remove and
that `f8.sk_agent()` still has — adverbs and particles taken as the noun agent (`práve`, `úplne`,
`zvyčajne`, `keby`, `nedeľu`), fronted obliques / objects taken as the agent (`značke`, `záhone`,
`grimasu`), and an agent asserted on copular `byť` clauses (`je biely`, `je rýchly`).

### Every union error (20)

* **6265** (dev) `Nikto nemá rád, keď ho na takomto výlete naháňajú.`
  * F8v1 clause 0 (split mismatch): asserts noun=nikto, no gold clause of the sentence has it
  * F8v1 readout: agent=`nikto` voice=active — noun "nikto" before the active verb "nemá"
  * gold: [0/main] pronoun=nobody("Nikto") ; [1/sub] no-agent (impersonal)
* **6971** (dev) `Keby ona bola robot, žiadosti by jej neprekážali.`
  * F8v1 clause 0 (split mismatch): asserts pron=she, no gold clause of the sentence has it
  * F8v1 readout: agent=`ona` voice=active — explicit nominative pronoun "ona"
  * gold: [0/sub] no-agent (copular-state) ; [1/main] no-agent (dative-experiencer)
* **7037** (dev) `Jeleň, ktorého parohy boli obrovské, stál medzi lístím.`
  * F8v1 clause 0 (split mismatch): asserts noun=parohy, no gold clause of the sentence has it
  * F8v1 readout: agent=`parohy` voice=active — noun "parohy" before the active verb "boli"
  * gold: [0/main] noun=deer("Jelen") ; [1/sub] no-agent (copular-state)
* **7752** (dev) `Vydra ma dnes ráno šťuchla do rukáva už trikrát.`
  * F8v1 clause 0: asserts noun=ráno vs gold noun=otter("Vydra")
  * F8v1 readout: agent=`ráno` voice=active — noun "ráno" before the active verb "šťuchla"
  * gold: [0/main] noun=otter("Vydra")
* **8017** (dev) `Brankár práve stál na čiare, keď rozhodca ukázal na biely bod.`
  * F8v1 clause 0 (split mismatch): asserts noun=práve, no gold clause of the sentence has it
  * F8v1 readout: agent=`práve` voice=active — noun "práve" before the active verb "stál"
  * gold: [0/main] noun=goalkeeper("Brankar") ; [1/sub] noun=referee("rozhodca")
* **15954** (dev) `Pozri! Predavač práve spúšťa kôš do oleja.`
  * F8v1 clause 0 (split mismatch): asserts noun=práve, no gold clause of the sentence has it
  * F8v1 readout: agent=`práve` voice=active — noun "práve" before the active verb "spúšťa"
  * gold: [0/main] no-agent (imperative) ; [1/main] noun=vendor("Predavac")
* **24101** (dev) `Pri tejto vtipnej červenej značke zastaví veľa ľudí.`
  * F8v1 clause 0: asserts noun=značke vs gold noun=people("vela ludi")
  * F8v1 readout: agent=`značke` voice=active — noun "značke" before the active verb "zastaví"
  * gold: [0/main] noun=people("vela ludi")
* **2929** (holdout) `Desivé svetlo úplne zhaslo a nádražie je zase tmavé.`
  * F8v1 clause 0 (split mismatch): asserts noun=úplne, no gold clause of the sentence has it
  * F8v1 readout: agent=`úplne` voice=active — noun "úplne" before the active verb "zhaslo"
  * gold: [0/main] noun=light("Desive svetlo") ; [1/main] no-agent (copular-state)
* **7458** (holdout) `Tú grimasu robí každý, však?`
  * F8v1 clause 0: asserts noun=grimasu vs gold pronoun=everyone("kazdy")
  * F8v1 readout: agent=`grimasu` voice=active — noun "grimasu" before the active verb "robí"
  * gold: [0/main] pronoun=everyone("kazdy")
* **9992** (holdout) `Členok, ktorý opuchol, bol ten ľavý.`
  * F8v1 clause 0 (split mismatch): asserts noun=opuchol, no gold clause of the sentence has it
  * F8v1 readout: agent=`opuchol` voice=active — noun "opuchol" before the active verb "bol"
  * gold: [0/main] no-agent (copular-state) ; [1/sub] pronoun=ankle("ktorý")
* **11348** (holdout) `Pozri! Asistent práve drží odrazovú dosku hore.`
  * F8v1 clause 0 (split mismatch): asserts noun=práve, no gold clause of the sentence has it
  * F8v1 readout: agent=`práve` voice=active — noun "práve" before the active verb "drží"
  * gold: [0/main] no-agent (imperative) ; [1/main] noun=assistant("Asistent")
* **12831** (holdout) `Mrkva v záhone je neuveriteľne veľká.`
  * F8v1 clause 0: asserts noun=záhone, gold has NO agent (copular-state)
  * F8v1 readout: agent=`záhone` voice=active — noun "záhone" before the active verb "je"
  * gold: [0/main] no-agent (copular-state)
* **14182** (holdout) `Pozri, mačka práve vyplazuje jazyk!`
  * F8v1 clause 0 (split mismatch): asserts noun=práve, no gold clause of the sentence has it
  * F8v1 readout: agent=`práve` voice=active — noun "práve" before the active verb "vyplazuje"
  * gold: [0/main] no-agent (imperative) ; [1/main] noun=cat("mačka")
* **16009** (holdout) `Zvyčajne sedí ticho, ale teraz hlasno kváka`
  * F8v1 clause 0 (split mismatch): asserts noun=zvyčajne, no gold clause of the sentence has it
  * F8v1 readout: agent=`zvyčajne` voice=active — noun "zvyčajne" before the active verb "sedí"
  * gold: [0/main] pronoun=it("(pro-drop)") ; [1/main] pronoun=it("(pro-drop)")
* **18789** (holdout) `Včera ona bola v tých istých pretekoch druhá.`
  * F8v1 clause 0: asserts pron=she, gold has NO agent (copular-state)
  * F8v1 readout: agent=`ona` voice=active — explicit nominative pronoun "ona"
  * gold: [0/main] no-agent (copular-state)
* **20435** (holdout) `Ten veľký tanier je biely a úplne čistý.`
  * F8v1 clause 0: asserts noun=tanier, gold has NO agent (copular-state)
  * F8v1 readout: agent=`tanier` voice=active — noun "tanier" before the active verb "je"
  * gold: [0/main] no-agent (copular-state)
* **24741** (holdout) `Veslársky tím je rýchly a veľmi silný.`
  * F8v1 clause 0: asserts noun=tím, gold has NO agent (copular-state)
  * F8v1 readout: agent=`tím` voice=active — noun "tím" before the active verb "je"
  * gold: [0/main] no-agent (copular-state)
* **32342** (holdout) `Dôkaz je na korkovej tabuli.`
  * F8v1 clause 0: asserts noun=dôkaz, gold has NO agent (copular-state)
  * F8v1 readout: agent=`dôkaz` voice=active — noun "dôkaz" before the active verb "je"
  * gold: [0/main] no-agent (copular-state)
* **140021** (fresh1k) `Moja babka nám každú nedeľu piekla jablkový koláč.`
  * F8v1 clause 0: asserts noun=nedeľu vs gold noun=grandmother("Moja babka")
  * F8v1 readout: agent=`nedeľu` voice=active — noun "nedeľu" before the active verb "piekla"
  * gold: [0/main] noun=grandmother("Moja babka")
* **140058** (fresh1k) `Keby sme boli odišli skôr, neboli by sme zmeškali ten let.`
  * F8v1 clause 0 (split mismatch): asserts noun=keby, no gold clause of the sentence has it
  * F8v1 readout: agent=`keby` voice=active — noun "keby" before the active verb "sme"
  * gold: [0/sub] pronoun=we("(pro-drop)") ; [1/main] pronoun=we("(pro-drop)")

## 4. Guard-level evaluation on dev / replay1j / fresh1l (stored labels, `eval_f8u.py`)

| side | items | judged wrong | v1 fired | v2 fired | u fired | v1 COST | v2 COST | u COST |
|---|---|---|---|---|---|---|---|---|
| dev | 490 | 301 | 1 | 25 | 25 | 0 | 0 | 0 |
| replay1j | 490 | 294 | 0 | 20 | 20 | 1 | 0 | 1 |
| fresh1l | 600 | 383 | 23 | 46 | 56 | 0 | 0 | 0 |
| **total** | | | 24 | 91 | 101 | **1** | **0** | **1** |

## Cost: guards firing on judged-CORRECT items
* **replay1j C:10107:3602000965** (v1=reject, v2=accept, u=reject via f8v1)
  * SK: `Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.`
  * EN: `The terminal was deserted; nevertheless, she had the feeling someone was watching her.`
  * reason: F8v1: Slovak agent "ona" is not the subject of the passive English clause

The 8 named FRESH1L items: **8 / 8** sids rejected by f8u (all via F8v2).
The 4 lost items: **4 / 4** sids rejected again by f8u (all via F8v1) — the union does repair
exactly what it was built to repair.
Totals: fires on judged-WRONG 24 (v1) / 91 (v2) / **101** (f8u); fires on judged-CORRECT
1 (v1) / 0 (v2) / **1** (f8u).
**Criterion (b) PASSES**: one judged-correct item over the three sides combined, inherited from
F8v1 (it is on REPLAY1J — the runner's coverage on that side drops by exactly 1).

## 5. Runner, `python3 runner_1m.py --dev --f8 f8u --f9 off --tip reject`

| side | metric | f8v2 (+F9 off, TIP reject) | f8u (+F9 off, TIP reject) |
|---|---|---|---|
| dev | coverage | 182/189 = 96.30 % | 182/189 = 96.30 % |
| dev | FA | 11/301 = 3.65 % | 11/301 = 3.65 % |
| dev | FA type T | 0/54 = 0.00 % | 0/54 = 0.00 % |
| dev | FA type V | 0/6 | 0/6 |
| replay1j | coverage | 182/196 = 92.86 % | **181/196 = 92.35 %** |
| replay1j | FA | 17/294 = 5.78 % | 17/294 = 5.78 % |
| replay1j | FA type T | 3/59 = 5.08 % | 3/59 = 5.08 % |
| replay1j | FA type V | 0/1 | 0/1 |
| fresh1l | coverage | 194/217 = 89.40 % | 194/217 = 89.40 % |
| fresh1l | FA | 12/383 = 3.13 % [1.63, 5.41] | **7/383 = 1.83 % [0.74, 3.73]** |
| fresh1l | FA type T | 3/130 = 2.31 % | 3/130 = 2.31 % |
| fresh1l | FA type V | 5/44 = 11.36 % | **0/44 = 0.00 % [0.00, 8.04]** |

Snapshots: `dev_regression_f8u.json`, `dev_regression_f8v2_f9off.json`. The runner overwrites
`dev_regression_1m.json`; the pre-existing file was backed up and restored byte-for-byte.
0 new model calls, 0 cache misses in both runs.

## 6. DECISION

**DO NOT ADOPT `f8u`. Keep `f8v2` alone.** The pre-registered rule needs all three criteria:

| criterion | bar | measured | verdict |
|---|---|---|---|
| (a) union gold ERRORs | <= 4 / 210 | **20 / 210 = 9.52 %** | **FAIL** |
| (b) fires on judged-CORRECT | <= 1 over three sides | 1 | PASS |
| (c) selftest | passes | 49 / 50 | **FAIL** |

Two of three fail, so the rule decides: `FROZEN_CONFIG_1M.json` keeps `"f8_module": "f8v2"`.
This is deliberately a rule and not a judgement call. The temptation to adopt is real — on
FRESH1L the union halves the FA (12/383 -> 7/383) and empties type V (5/44 -> 0/44) at zero
coverage cost — but that gain is measured on the very set the four lost items were found on,
and the price is importing a Slovak agent readout that contradicts a blind hand gold on 20 of
210 sentences. A guard that asserts a wrong agent on ~10 % of sentences can only be safe while
the English side happens not to be passive; on an unseen set it is a live false-rejection risk,
and 1L-style coverage loss is exactly what Phase 1M is trying to avoid. The honest repair is not
a union but a v3 that re-admits clause-initial common-noun agents with a gold-validated test —
not to be built on this data, and not by this agent.

Recorded for the main session: the four lost `be + PP + by` items stay un-caught under `f8v2`,
which is a known, quantified cost of the freeze (on FRESH1L: FA 12/383 instead of 7/383).

## 7. What changed outside `f8u.py`

* `runner_1m.py`: one line, `--f8` choices `('f8', 'f8v2')` -> `('f8', 'f8v2', 'f8u')`. Pre-freeze.
  `select_f8()` already loads any module by name from `phase1m/`, so nothing else was needed.
* `FREEZE_FILES`: added `f8u.py`, `eval_f8u.py`, `validate_f8u_gold.py` to the
  "present but NOT executed by --final" block (`check_freeze_1m()` refuses on any unlisted .py).
  Since the decision is NOT to adopt, `f8u.py` stays in that non-executed block.
* New files: `f8u.py`, `validate_f8u_gold.py`, `eval_f8u.py`, `f8u_validation.json`,
  `f8u_eval.json`, `dev_regression_f8u.json`, `dev_regression_f8v2_f9off.json`, this file.
* `FROZEN_CONFIG_1M.json` was NOT touched. No earlier phase directory was touched.
