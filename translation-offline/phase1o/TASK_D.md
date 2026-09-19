# Phase 1O Task D — the agentless passive (0 extra model calls)

22 judged-correct 1N items carry passive tag `agentless`: 6 accepted, **16 rejected**. How the 16 were rejected under `P-FROZEN-1N`: `{"L3 DIFF": 14, "guard F4v2": 2}`.

## Plain answer

**Yes — the stack rejects the agentless passive outright; it is never "tolerated with a tip".** The deciding layer is **L3, the model's one-word verdict**: 14 of the 16 rejections are a raw `DIFF` reply from `gemini-3.1-flash-lite` under `P-FROZEN-1N`. The other 2 never reached the model: the **F4v2 subject-mismatch guard** rejected them before L3. **0 of the 16 are TIP-turned-rejection** (`model_tip` false on every row, no item carries a tip) — so switching TIP-as-rejection OFF would rescue none of them.

## What machinery exists for a dropped agent / missing meaning, and whether it fired

Read from the routing code the runner executes (`pipeline_1i.run_pipeline`, `runner_1k.configure_row / apply_guards / locktip_decide`, the guard docstrings of `checker_1i` / `guards_c`):

* **There is no "type M, accept with a tip" path at all.** `M` exists only as a JUDGE label on items judged wrong. Nothing in the stack classifies an accepted answer as "meaning dropped but tolerable".
* The only tip sources are (a) the model replying `TIP` ("same meaning and acceptable, but with a small slip" — the system text says nothing about a dropped agent), (b) a `correct_with_tip` chk from the checker, (c) the LOCKTIP lock tip. None fired on the 16. With TIP-as-rejection ON a model `TIP` would have been a rejection anyway.
* The missing-meaning guards are **rejecting** guards, not tolerating ones: `F5` (adjunct deletion — fires only when the answer is an order-preserving subsequence of a reference/variant and the deleted span carries information), `F5t` (diff-based deletion, not in the 1N guard set), `F2B` (a with-tip acceptance downgraded when the Slovak carries a duration the answer lost). **None of them fired on the 16** (layers are `L3` x14 and `F4v2` x2). A passive is not a subsequence of the active reference, so F5 cannot see a dropped agent by construction.
* `F4v2` (answer subject pronoun contradicts a feature the Slovak determines) fired on 2 — a subject guard misreading the passive's new subject, not a meaning guard. The pipeline row keeps no guard trace, so the exact clash is not stored.
* F8v1 / F8v2 / F9 are readouts only in 1N and decide nothing; their per-item readouts are listed below.
* The stored model reply is the bare word (`maxOutputTokens` 24, "No explanation"): **no reason text exists** for any of the 14 DIFFs.

## What this means for the owner's expectation

The owner expected: agentless passive = dropped agent = type M, tolerated with a tip. The stack does neither. The 1N voice line tells the model that dropping the agent "is SAME, provided the meaning is preserved", and the model still answers DIFF on 14 of the 22 agentless items judged correct (6 accepted, 2 stopped earlier by F4v2) — while the `by`-passives, which keep the agent, pass 78 of 83 with 0 L3 rejections. The model is treating the lost agent as lost meaning (DIFF), which is the prompt's own wording line at work ("a word that changes which thing, person ... the Slovak names is DIFF"), and no layer downstream can turn a DIFF into an accept-with-tip. The reply under `P-FROZEN` is in the per-item list once Task A has run; until then it reads "not run".

## The 16 rejected items

### C:160012:2176442930

* Slovak: Zuzana bude tie medené kľučky leštiť celé popoludnie.
* answer: The copper door handles will be polished all afternoon.
* reference(s): Zuzana will be polishing those copper handles all afternoon. | Zuzana will polish those copper handles all afternoon.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160012:2176442930", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "A2", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "leštiť", "voice_sk": "active", "reason": "noun \"leštiť\" before the active verb \"popoludnie\""}, "en": {"passive": true, `, F8v2 `{"sk": {"agent_nom": true, "agent": "leštiť", "voice_sk": "active", "reason": "noun \"leštiť\" before the active verb \"popoludnie\""}, "en": {"passive": true, `, F9 `{"verdict": "tip", "sk": {"frames": ["future"], "verdict": "future", "reported": false, "main": "Zuzana bude tie medené kľučky leštiť celé popoludnie.", "reason`

### C:160020:3352119485

* Slovak: Keď sme my dorazili, Janka už rozložila celý stánok.
* answer: When we arrived, the whole stall had already been set up.
* reference(s): When we arrived, Janka had already set up the whole stall. | By the time we arrived, Janka had already put up the entire stand. | When we got there, Janka had already assembled the whole stall.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160020:3352119485", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "my", "voice_sk": "active", "reason": "explicit nominative pronoun \"my\""}, "en": {"passive": true, "reason": "\"been set\"`, F8v2 `{"sk": {"agent_nom": true, "agent": "my", "voice_sk": "active", "reason": "explicit nominative pronoun \"my\""}, "en": {"passive": true, "reason": "\"been set\"`, F9 `{"verdict": "tip", "sk": {"frames": ["past"], "verdict": "past", "reported": false, "main": "Janka už rozložila celý stánok.", "reason": "l-participle \"rozloži`

### C:160024:2621707485

* Slovak: Klára nám povedala, že ona tú starú violu priniesla na skúšku sama.
* answer: Klára told us that the old viola had been brought to the rehearsal without any help.
* reference(s): Klára told us that she had brought that old viola to the rehearsal herself. | Klára told us that she brought the old viola to the rehearsal herself.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok True
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160024:2621707485", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "ona", "voice_sk": "active", "reason": "explicit nominative pronoun \"ona\""}, "en": {"passive": false, "reason": "no passiv`, F8v2 `{"sk": {"agent_nom": true, "agent": "ona", "voice_sk": "active", "reason": "explicit nominative pronoun \"ona\""}, "en": {"passive": false, "reason": "no passiv`, F9 `{"verdict": "accept", "sk": {"frames": ["past"], "verdict": "past", "reported": true, "main": "Klára nám povedala", "reason": "l-participle \"povedala\"", "clau`

### C:160036:2901324230

* Slovak: Ona mala ten rám vystužiť ešte pred prevozom do galérie.
* answer: The frame was supposed to be reinforced before it was moved to the gallery.
* reference(s): She should have reinforced that frame before the transport to the gallery. | She was supposed to reinforce the frame before the move to the gallery. | She ought to have strengthened that frame before transporting it to the gallery.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160036:2901324230", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B2", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "ona", "voice_sk": "active", "reason": "explicit nominative pronoun \"ona\""}, "en": {"passive": true, "reason": "\"was supp`, F8v2 `{"sk": {"agent_nom": true, "agent": "ona", "voice_sk": "active", "reason": "explicit nominative pronoun \"ona\""}, "en": {"passive": true, "reason": "\"was supp`, F9 `{"verdict": "tip", "sk": {"frames": ["past"], "verdict": "past", "reported": false, "main": "Ona mala ten rám vystužiť ešte pred prevozom do galérie.", "reason"`

### C:160040:3346784148

* Slovak: Keď zazvonil zvonec, Emma ešte ukladala tie nástroje do skrinky.
* answer: When the bell rang, the tools were still being put away in the cabinet.
* reference(s): When the bell rang, Emma was still putting the instruments into the cupboard. | Emma was still putting those tools away in the locker when the bell rang.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160040:3346784148", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "keď", "voice_sk": "active", "reason": "noun \"keď\" before the active verb \"zazvonil\""}, "en": {"passive": true, "reason"`, F8v2 `{"sk": {"agent_nom": true, "agent": "keď", "voice_sk": "active", "reason": "noun \"keď\" before the active verb \"zazvonil\""}, "en": {"passive": true, "reason"`, F9 `{"verdict": "tip", "sk": {"frames": ["past"], "verdict": "past", "reported": false, "main": "Emma ešte ukladala tie nástroje do skrinky.", "reason": "l-particip`

### C:160044:1984378852

* Slovak: On bude zajtra celý deň voziť svoje náradie do novej dielne.
* answer: Tomorrow his tools will be carried to the new workshop all day.
* reference(s): Tomorrow he will be taking his tools to the new workshop all day. | He will be carrying his tools to the new workshop all day tomorrow.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok True
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160044:1984378852", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "A1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": true, "reason": "\"be carried`, F8v2 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": true, "reason": "\"be carried`, F9 `{"verdict": "accept", "sk": {"frames": ["future"], "verdict": "future", "reported": false, "main": "On bude zajtra celý deň voziť svoje náradie do novej dielne.`

### C:160048:2251836920

* Slovak: Krajčírka skracuje nohavice vždy v stredu popoludní.
* answer: Trousers are always shortened on Wednesday afternoons.
* reference(s): The seamstress always shortens trousers on Wednesday afternoons. | The dressmaker always takes up trousers on Wednesday afternoons. | The seamstress shortens the trousers every Wednesday afternoon.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160048:2251836920", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "krajčírka", "voice_sk": "active", "reason": "noun \"krajčírka\" before the active verb \"skracuje\""}, "en": {"passive": fa`, F8v2 `{"sk": {"agent_nom": true, "agent": "krajčírka", "voice_sk": "active", "reason": "noun \"krajčírka\" before the active verb \"skracuje\""}, "en": {"passive": fa`, F9 `{"verdict": "tip", "sk": {"frames": ["future", "present"], "verdict": "{'future', 'present'}", "reported": false, "main": "Krajčírka skracuje nohavice vždy v st`

### C:160052:1176203340

* Slovak: Ty si v sobotu prebrúsil tú drevenú lavicu na terase.
* answer: The wooden bench on the terrace was sanded down on Saturday.
* reference(s): You sanded down the wooden bench on the terrace on Saturday. | On Saturday you sanded that wooden bench on the terrace. | You sanded down the wooden bench on the patio on Saturday.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok True
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160052:1176203340", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "A2", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "ty", "voice_sk": "active", "reason": "explicit nominative pronoun \"ty\""}, "en": {"passive": true, "reason": "\"was sanded`, F8v2 `{"sk": {"agent_nom": true, "agent": "ty", "voice_sk": "active", "reason": "explicit nominative pronoun \"ty\""}, "en": {"passive": true, "reason": "\"was sanded`, F9 `{"verdict": "abstain", "sk": {"frames": [], "verdict": null, "reported": false, "main": null, "reason": "no finite verb signal found -> abstain", "clauses": [{"`

### C:160060:4058632457

* Slovak: Kým vlak stál v stanici, rušňovodič doplnil vodu do nádrže.
* answer: While the train stood in the station, the water in the tank was topped up.
* reference(s): While the train was standing in the station, the driver topped up the water in the tank. | While the train stood at the station, the engine driver filled the tank with water. | The driver topped up the water in the tank while the train was waiting at the station.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok True
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160060:4058632457", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "vlak", "voice_sk": "active", "reason": "noun \"vlak\" before the active verb \"stál\""}, "en": {"passive": true, "reason": `, F8v2 `{"sk": {"agent_nom": true, "agent": "vlak", "voice_sk": "active", "reason": "noun \"vlak\" before the active verb \"stál\""}, "en": {"passive": true, "reason": `, F9 `{"verdict": "accept", "sk": {"frames": ["past"], "verdict": "past", "reported": false, "main": "rušňovodič doplnil vodu do nádrže.", "reason": "l-participle \"d`

### C:160064:489138833

* Slovak: Moja teta pletie deťom hrubé vlnené ponožky každú zimu.
* answer: Thick woolen socks are knitted for the kids every winter.
* reference(s): My aunt knits thick woollen socks for the children every winter. | Every winter my aunt knits the children thick woollen socks.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160064:489138833", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "A1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": null, "agent": null, "voice_sk": null, "reason": "no clear finite verb / subject signal"}, "en": {"passive": true, "reason": "\"are knitted`, F8v2 `{"sk": {"agent_nom": null, "agent": null, "voice_sk": null, "reason": "no clear finite verb / subject signal"}, "en": {"passive": true, "reason": "\"are knitted`, F9 `{"verdict": "abstain", "sk": {"frames": [], "verdict": null, "reported": false, "main": null, "reason": "no finite verb signal found -> abstain", "clauses": [{"`

### C:160076:1794710932

* Slovak: Neboj sa, on ti to predné koleso nafúka ešte dnes večer.
* answer: Don't worry, that front wheel will be pumped up for you this evening.
* reference(s): Do not worry, he will pump up the front wheel for you this evening. | Do not worry, he will inflate your front tyre tonight.
* rejecting layer (1N): **F4v2**; L3-eligible: False; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict None, raw `None`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160076:1794710932", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "A2", "accepted": false, "verdict": "wrong", "layer": "F4v2", "model": null, "tip": false, "model_tip": false, "reached_l3": false}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": false, "reason": "no passive `, F8v2 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": false, "reason": "no passive `, F9 `{"verdict": "tip", "sk": {"frames": ["future", "present"], "verdict": "{'future', 'present'}", "reported": false, "main": "on ti to predné koleso nafúka ešte dn`

### C:160080:488008841

* Slovak: Kiežby on ten starý orech nebol vyrúbal tak skoro.
* answer: I wish that old walnut tree hadn't been cut down so soon.
* reference(s): I wish he had not cut down that old walnut tree so soon. | If only he had not felled the old walnut tree so early.
* rejecting layer (1N): **F4v2**; L3-eligible: False; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict None, raw `None`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160080:488008841", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B2", "accepted": false, "verdict": "wrong", "layer": "F4v2", "model": null, "tip": false, "model_tip": false, "reached_l3": false}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": false, "reason": "no passive `, F8v2 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": false, "reason": "no passive `, F9 `{"verdict": "tip", "sk": {"frames": ["conditional"], "verdict": "conditional", "reported": false, "main": "Kiežby on ten starý orech nebol vyrúbal tak skoro.", `

### C:160084:2484737775

* Slovak: Oni hovoria, že on ten čln lakuje už druhý týždeň.
* answer: They say the boat is being varnished for the second week already.
* reference(s): They say that he has been varnishing that boat for two weeks now. | They say he has been varnishing the boat for the second week already. | They are saying that he has been lacquering that boat for two weeks.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160084:2484737775", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "oni", "voice_sk": "active", "reason": "explicit nominative pronoun \"oni\""}, "en": {"passive": true, "reason": "\"being va`, F8v2 `{"sk": {"agent_nom": true, "agent": "oni", "voice_sk": "active", "reason": "explicit nominative pronoun \"oni\""}, "en": {"passive": true, "reason": "\"being va`, F9 `{"verdict": "tip", "sk": {"frames": ["present"], "verdict": "present", "reported": false, "main": "Oni hovoria", "reason": "imperfective present \"hovoria\"", "`

### C:160088:2020139039

* Slovak: Náš ujo strúha deťom drevené píšťalky každé leto.
* answer: Every summer wooden whistles are carved for the children.
* reference(s): Our uncle carves wooden whistles for the children every summer. | Every summer our uncle whittles wooden whistles for the kids.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160088:2020139039", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": null, "agent": null, "voice_sk": null, "reason": "no clear finite verb / subject signal"}, "en": {"passive": true, "reason": "\"are carved\`, F8v2 `{"sk": {"agent_nom": null, "agent": null, "voice_sk": null, "reason": "no clear finite verb / subject signal"}, "en": {"passive": true, "reason": "\"are carved\`, F9 `{"verdict": "abstain", "sk": {"frames": [], "verdict": null, "reported": false, "main": null, "reason": "no finite verb signal found -> abstain", "clauses": [{"`

### C:160096:4258255142

* Slovak: Ak my zoženieme dlhší rebrík, tú anténu na streche upevníme sami.
* answer: If we get a longer ladder, the antenna on the roof will be fixed.
* reference(s): If we get a longer ladder, we will fix the aerial on the roof ourselves. | If we find a longer ladder, we will secure the antenna on the roof ourselves.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160096:4258255142", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B1", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "my", "voice_sk": "active", "reason": "explicit nominative pronoun \"my\""}, "en": {"passive": true, "reason": "\"be fixed\"`, F8v2 `{"sk": {"agent_nom": true, "agent": "my", "voice_sk": "active", "reason": "explicit nominative pronoun \"my\""}, "en": {"passive": true, "reason": "\"be fixed\"`, F9 `{"verdict": "tip", "sk": {"frames": ["future", "present"], "verdict": "{'future', 'present'}", "reported": false, "main": "tú anténu na streche upevníme sami.",`

### C:160100:3987111647

* Slovak: Budúcu sezónu on bude viesť tú dielňu a školiť dvoch nových učňov.
* answer: Next season the workshop will be run and two new apprentices will be trained.
* reference(s): Next season he will be running that workshop and training two new apprentices. | Next season he will run the workshop and train two new apprentices.
* rejecting layer (1N): **L3**; L3-eligible: True; chk `{"verdict": "wrong", "step": "auto", "feedback": ""}`; lock_ok False
* model reply under `P-FROZEN-1N`: verdict DIFF, raw `DIFF`
* model reply under `P-FROZEN`: not run
* pipeline row (1N): `{"item_id": "C:160100:3987111647", "kind": "C", "judged": "correct", "wrong_type": null, "half": "NEW", "level": "B2", "accepted": false, "verdict": "wrong", "layer": "L3", "model": "DIFF", "tip": false, "model_tip": false, "reached_l3": true}`
* readouts (decide nothing): F8v1 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": true, "reason": "\"be run\"",`, F8v2 `{"sk": {"agent_nom": true, "agent": "on", "voice_sk": "active", "reason": "explicit nominative pronoun \"on\""}, "en": {"passive": true, "reason": "\"be run\"",`, F9 `{"verdict": "tip", "sk": {"frames": ["future"], "verdict": "future", "reported": false, "main": "Budúcu sezónu on bude viesť tú dielňu", "reason": "future auxil`
