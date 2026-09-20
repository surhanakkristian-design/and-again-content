# Phase 2F §3.2 — Pricing de, fr, es, tr, hu, ua: guard audit and cost table

**0 Gemini calls. 0 headless Claude sessions. 0 model calls of any kind. Nothing written to the
database.** This document is source reading and arithmetic. Every line number below was read out of
the working tree at the time of writing.

The frozen stack is `phase1w/stack_1w.py` = AG v4 (`phase1u/taskA/agent_drop_v4.py`) + v5 `refsubj`
`rs_nom` + the TIP determiner rule (`phase1v/trackA_loop/stack_1v.py`) + the nominative reader
(`phase1w/reader_nom.py`), resting on `phase1t/taskA/agent_drop_v3.py`,
`phase1s/taskC/agent_drop_v2.py`, `phase1i/checker_1i.py` (F4v2) and `phase1n/f9.py` (aspect /
l-participle).

---

## 0. The shape of the risk

1T's four Czech bugs (`em`, `se`, `jestli`, `aspect` — `phase1v/trackC/SECTION.md` §C1) all failed the
same way: the guard did not raise, did not abstain, did not log a language mismatch. It returned a
confident verdict computed from Slovak evidence that happened to be absent, or present with a
different meaning. `em` read a Czech **instrumental** `-em` as a Slovak **1sg** and recovered a person
that was not there. `se` was missing from `SK_REFLEX`, so every Czech reflexive passive read as an
active with a nameable agent — 23 missed reflexives, all silent.

That is the failure mode to price. The audit below is organised by *which Slovak literal is consulted*,
because a literal that never matches is not a null result — in this stack an unmatched literal almost
always flips a veto **off**.

---

## 1. Guard audit

### 1.1 The entry point is hard-wired to Slovak

`phase1w/stack_1w.py:23`:

```python
with R.installed(S.V3.V2, 'sk', READER_VARIANT):
```

`stack_1w.decide()` takes no `lang`. The literal `'sk'` selects every per-language table in
`reader_nom` (`PRON`, `PREP`, `SUB`, `IMPER`, `STOP`, `DET`, `PLNUM`, `QUANT`, `BYT`, `MODAL`, `VEND`,
`OBLEND`, `PLEND`, `AMBI`, `AUX1`, `AUX2`, `REFLEX`). The dicts are keyed `{'sk': ..., 'cz': ...}`
only — `reader_nom.py:109` builds `STOPALL` with `for L in ('sk', 'cz')`. A seventh key raises
`KeyError` inside `read()`, which is caught at `reader_nom.py:286-287` and returned as
`abstain:crash`. So a new language does not fail loudly at the entry point; it abstains, and the AG
verdict falls through to whatever the *English-side* guards decide on their own. **Any new language
requires editing the frozen entry point**, which is the thing 1W froze.

### 1.2 The three guards that silently invert on all six languages

These are the important ones. Each is a **veto** whose trigger is a Slovak literal. When the literal
cannot match, the veto is permanently off and the guard returns a confident *positive*.

**(a) `tip_det_rule` — `phase1v/trackA_loop/stack_1v.py:130-134`**

```python
def tip_det_rule(sk, answer, reference, layer):
    if layer != 'L3:TIPrej' or SK_DEM.search(sk or ''):
        return False
    return det_swap_only(answer, reference) and ...
```

with `SK_DEM` at `stack_1v.py:107-109`:
`ten|tá|to|tie|tí|tieto|títo|tento|táto|toto|toho|tej|tú|tom|tým|tou|tých|tými|tohto|tejto|túto|
tomto|týmto|touto|týchto|týmito|onen|oná|ono|tamten|tamtá|tamto|tamtie`.

The rule exists **because Slovak has no articles**: if the English answer and the reference differ only
by a determiner swap (`a`↔`the`↔`this`…, `DETS` at `stack_1v.py:106`), the Slovak source carried no
information to choose between them, *unless* it used a demonstrative — hence the `SK_DEM` veto.

For **de, fr, es** the premise is simply false: the source has a full article system, and the article
in the source *is* the evidence. For **tr, hu** the premise is half false: no articles in Turkish, but
Turkish marks definiteness with the **accusative `-(y)ı/-i/-u/-ü`** on the object, and Hungarian has a
definite article `a/az` **plus** a definite conjugation that marks the object's definiteness on the
verb. For **ua** the premise is true (no articles) but `SK_DEM` is Latin-script and cannot match
`цей/ця/це/ці/той/та/те/ті`.

In **all six**, `SK_DEM.search()` returns `None` on every sentence. The veto is off. The rule fires on
**100 % of `L3:TIPrej` rows** and overturns each one. Silent, confident, wrong on de/fr/es/hu — and on
ua wrong exactly where Ukrainian *does* use a demonstrative.

**(b) `sk_clause_is_passive` — `phase1t/taskA/agent_drop_v3.py:279-287`**, over
`SK_BYT` (`:85-86`: `je sú som sme ste bol bola bolo boli budem budeš …`) and
`SK_PPART` (`:87`: `re.compile(r'(ný|ná|né|ní|tý|tá|té|tí|ných|nými|tých|tými)$', re.I)`).

Consumed at `agent_drop_v3.py:478-479` ("the Slovak counterpart clause is itself passive") and at
`agent_drop_v4.py:251`. It is the abstain that stops AG from charging an English agentless passive as a
dropped agent when **the source clause was passive too**.

German `wird … gebaut`, French `est construit`, Spanish `es construido`, Turkish `yapılıyor` (passive
**infix** `-ıl-`, no auxiliary at all), Hungarian `-va/-ve` + `van`, Ukrainian `будується` / the
impersonal `-но/-то` (`збудовано` — an agentless participle with **no copula whatsoever**): none of
these produce a `SK_BYT` token followed by a `SK_PPART` ending. `sk_clause_is_passive` returns `False`
on every clause of every one of the six. AG then charges correct agentless English as a meaning
omission. Silent false reject.

Turkish and Ukrainian `-но/-то` are the worst of these, because the construction is *morphologically
invisible to any auxiliary-plus-participle detector* — not a table to re-fill but a different search.

**(c) `SK_REFLEX` — `phase1s/taskC/agent_drop_v2.py:62`**

```python
SK_REFLEX = re.compile(r'(^|\s)(sa|si)(\s|[.,!?]|$)', re.I)
```

plus the reader's own copy, `reader_nom.py:107`:
`REFLEX = {'sk': re.compile(r'(^|\s)(sa|si)(\s|$)'), 'cz': ... (se|si) ...}`.

Consumed at `agent_drop_v2.py:128`, `agent_drop_v3.py:486`, `agent_drop_v4.py:251`, and
`reader_nom.py:224-225` (`abstain:reflexive clause`). This is the guard whose Czech miss cost 23 silent
errors in 1T, and 2B settled g4's residual error (22.0 % / 26.0 % in `phase2f/gates_2f_cz.json`) as
"the reflexive si/sa/se pattern". It is the single highest-value abstain in the stack.

- **es**: free clitic `se` in exactly the same syntactic slot → re-table only. Cheapest case.
- **fr**: free clitic `se/s'` → re-table, but must be disentangled from the object clitics (§1.4).
- **de**: free `sich/mich/dich/uns/euch` → re-table, though the German reflexive is far less often a
  passive than the Slavic one, so the abstain will over-fire.
- **ua**: the reflexive is a **bound suffix `-ся/-сь`**, not a free word. A whitespace-delimited regex
  **can never fire**. The highest-value abstain in the stack goes permanently silent on Ukrainian
  unless it is rewritten as a suffix test. This is a rewrite, not a patch.
- **tr, hu**: no free reflexive particle at all (Turkish `-in-` infix, Hungarian `-kodik/-kezik`
  derivation). Same rewrite.

### 1.3 The morphology tables — every literal is Slovak

`phase1w/reader_nom.py` is one long Slovak (and patched-Czech) lexicon. Nothing in it is derived; every
entry is a hand-written string.

| Lines | Table | What it encodes |
|---|---|---|
| 49-54 | `PRON` | `ja/ty/on/ona/ono/my/vy/oni/ony` → (person, number, gender) |
| 55-58 | `PREP` | `na nad pod pred za v vo do z zo s so k ku …` |
| 59-62 | `SUB` | `že keď keďže lebo pretože hoci kým ak aby …` + `V3.SK_CONN` |
| 63-66 | `IMPER` | `pozri pozrite hádaj daj poď počkaj sleduj …` |
| 67-81 | `STOP` | ~200 Slovak adverbs, particles and **oblique pronoun forms** (`ma mňa mi mne ťa teba ti tebe ho jeho mu jemu ju jej ich im nás nám vás vám …`) |
| 82-87 | `DET` | `ten tá tí tie tento … každý všetci môj tvoj náš váš svoj …` |
| 88 | `PLNUM` | `dva dve dvaja traja tri štyri štyria oba obe obaja` |
| 89-90 | `QUANT` | `viac veľa málo niekoľko pár päť … desať` |
| 91-92 | `BYT` | `je sú som sme ste bol bola bolo boli budem …` |
| 93-94 | `MODAL` | `môže môžu musí musia chce chcú vie vedia má majú treba smie` |
| 95-97 | `VEND` | **verb endings**: `ajú ujú ejú ieme íme áme eme ete íte áte iete ieš íš áš eš ujem uje` |
| 98-101 | `OBLEND` | **oblique-case endings**: `om ou ov ami ách och iach ím ým ých ymi imi ej ého ému ho mu ovi u ú` |
| 102 | `PLEND` | `i y ia ovia atá ata` |
| 103 | `AMBI` | `e` (sk) / `e a` (cz) |
| 104 | `ADJEND` | `ý á é í` |
| 105-106 | `AUX1`/`AUX2` | `som sme` / `ste` |

`OBLEND` (`:98-101`) is the load-bearing one. `_np()` at `reader_nom.py:199`:

```python
if not quant and h.endswith(OBLEND[L]) and not (t[j][:1].isupper() and h.endswith('om')):
    return None
```

This is the entire case filter: *a noun whose suffix is in the oblique list is not a nominative, so it
is not a subject.* It is a pure suffix test over a fixed list of literal Slovak strings. It is the
mechanism by which reader_nom avoids reading a prepositional object as the agent.

- **de**: German **case syncretism** defeats a suffix test in principle. `der` is nom.m.sg **and**
  gen.f.sg **and** dat.f.sg **and** gen.pl; `die` is nom/acc f.sg and nom/acc pl; nouns themselves are
  largely uninflected (`dem Mann` marks case on the article, not the noun, except the dative-`-n`
  plural and weak masculines). There is no suffix on the head noun to test. `OBLEND` has no German
  analogue — the equivalent guard has to read the **article**, which means re-architecting `_np()`,
  not re-filling a tuple.
- **fr, es**: **no case morphology on nouns at all**. `OBLEND` is vacuous. Its protective job — "this
  NP is a prepositional object, skip it" — is done today by `_skip_pp()` (`reader_nom.py:204-210`)
  over `PREP`, which does transfer. But the belt (`PREP`) survives and the braces (`OBLEND`) do not.
- **tr, hu**: **agglutinative with vowel harmony**. Turkish locative is `-da/-de/-ta/-te`; Hungarian
  inessive is `-ban/-ben`, superessive `-on/-en/-ön/-n`. An ending is an *allomorph set selected by the
  stem's vowels*, and endings **stack** (`ev-ler-im-iz-de-ki-ler-den`). A fixed tuple of literal
  suffixes cannot express this. Hungarian has roughly 18 cases; Turkish 6 core plus a large
  postpositional system. `OBLEND`, `PLEND`, `AMBI`, `VEND` and `ADJEND` are all **unrepresentable** as
  literal tuples in these two languages. They need a morphological analyser or a finite-state
  transducer — a different kind of artefact than anything in this repo.
- **ua**: the *architecture* transfers exactly (a genuine nominative/oblique case system, an l-participle
  past, aspect pairs, pro-drop, no articles) but every literal is Cyrillic: `-ом/-ою/-ів/-ами/-ах/-ій/
  -ого/-ому/-ові/-у/-ю`. Re-table, not re-architect. Ukrainian adds one hazard Slovak lacks: the
  **vocative** (`Оксано!`, `брате!`), which is neither nominative nor in any oblique list and will pass
  `_np()`'s filter as a subject candidate.

### 1.4 The `reader_nom` subject-recovery rules, step by step

`_decide_clause()` at `reader_nom.py:213-256`:

1. **`:215-219` — overt nominative personal pronoun agreeing in person/number/gender.**
   `if pr and (p is None or p == pr[0]) and (n is None or n == pr[1]) and not (pr[2] and g and n != 'pl' and g != pr[2])`.
   - **tr, hu**: `o` / `ő` are **genderless**. The gender discriminator at `:218` is inert — no false
     accepts from it, but the reader loses the one test that stops it matching a 3sg pronoun to the
     wrong referent in an object-fronted clause.
   - **fr**: `on` is an overt nominative pronoun with **impersonal** meaning. The reader returns `on`
     as the agent, and AG v4 then charges the English agentless passive ("the window was broken") as a
     dropped agent against `On a cassé la fenêtre` — where agentless English is the *correct*
     translation. Silent false reject, and `on` is extremely common in the register these exercises use.
   - **de**: `man`, same problem, same construction.
   - **es**: `usted/ustedes` are 3rd-person forms with 2nd-person reference — the person feature
     recovered from the verb and the person feature of the pronoun agree, but both are wrong about who
     the agent is.

2. **`:222-223` — `if p in ('1','2'): return None, 'abstain:1st/2nd person pro-drop'`.**
   This abstain exists **only because Slovak drops subject pronouns**. It depends on F4v2 having
   recovered a person from the verb ending.
   - **de, fr**: **MOOT.** Both are non-pro-drop; the subject pronoun is obligatory, so step 1 always
     resolves and step 2 is dead code. This is a genuine saving.
   - **es, tr, hu, ua**: pro-drop **persists**, so the abstain is still required — but the person must be
     recovered from a *different* morphology (§1.5).

3. **`:224-225` — reflexive abstain.** See §1.2(c).

4. **`:226-244` — the pre-verbal NP.** `vidx = {i for i in range(len(low)) if _verbish(...)}`, then
   `vi = min(vidx)`, then scan `i` from 0 to `vi` taking the first `_np()` that agrees in number. This
   is "**the first nominative-shaped NP before the first finite verb is the subject**".
   - **de**: German is **V2** with free topicalisation. `Den Mann sieht die Frau` = *the woman sees the
     man*, object first. The first pre-verbal NP is the **object** roughly as often as the syntax is
     interesting, and §1.3 established there is no suffix to tell them apart. Worse, **separable verbs**
     (`Sie macht das Fenster **auf**`) put the verb's particle at the clause end, so the clause's finite
     verb is at position 2 and its lexical content at position *n* — `_verbish()` will classify the
     particle (`auf`, `zu`, `an`, `mit`) as a preposition at `reader_nom.py:159` and the finite carrier
     (`macht`) as the verb, which is right by accident; but `_skip_pp()` at `:204-210` will then treat
     the clause-final particle as opening a prepositional phrase and consume the token after it.
     Subordinate clauses are **verb-final**, so `vi = min(vidx)` finds the *auxiliary* rather than the
     main verb, and the whole pre-verbal window becomes the entire clause.
   - **fr**: strict SVO, so the heuristic is nearly always right — **except for clitics**.
     `Je **la** vois`, `Il **leur** a donné`, `On **en** parle`. The object clitics `le/la/les/lui/leur/
     en/y` sit **between the subject and the verb**, which is precisely the window `:233-244` scans, and
     `la`/`les` are **homographs of the definite articles**. `_np()` at `:186-190` accepts a
     `DET`-shaped token as an NP modifier, so a French `DET` table containing `la/les` will make the
     reader treat the object clitic as the start of a subject NP. This is the French analogue of the
     Czech `em` bug: a token that exists in the table with the wrong analysis.
   - **tr, hu**: **verb-final**. `vi = min(vidx)` is essentially always the last token, so the
     "pre-verbal window" is the whole clause and the "first NP" heuristic degenerates to "the first
     noun". Turkish marks the subject by the **absence** of an overt case suffix (bare nominative) and
     the definite object by the **presence** of the accusative — the exact inverse of `OBLEND`'s logic,
     and unreadable without a morphological analyser.
   - **ua**: transfers.

5. **`:245-255` — the post-copula NP after a `BYT` form** (`Na stole je modrá miska`). Requires
   `BYT` to be populated and requires the language to permit existential inversion. German `es gibt`,
   French `il y a`, Spanish `hay`, Turkish `var`, Hungarian `van` are all **existential predicates that
   are not copulas** — each needs its own entry and its own reading. Hungarian additionally has **zero
   copula** in the 3rd person present (`A ház nagy` = "the house [is] big"), so `BYT` has no token to
   match and `_verbish()` finds **no finite verb at all** → `abstain:no finite verb token` at `:228` on
   a large slice of ordinary Hungarian sentences.

6. **`:230` — `if low[0] in ('to','toto','tohle') and low[1] in BYT[L]`** — a hard-coded Slovak/Czech
   demonstrative-plus-copula literal, in the body of the function, not in a table.

7. **`:265` and `:269`** — sentence split on `[.!?…]`, then `V3.split_sk`. `split_sk`
   (`agent_drop_v3.py:274-276`) is `re.split(r'[,;:]', sk)` with the docstring *"commas (mandatory
   before Slovak subordinate clauses)"*. That property holds for **de** (German comma rules before
   subordinate clauses are mandatory — a genuine freebie) and **ua**, partially for **hu**. It is
   **false for fr and es**, where a comma is neither required before a relative clause nor forbidden
   inside an NP — the splitter will over-split French enumerations and under-split relative clauses.
   For **tr**, subordination is by **participial/converbial suffix with no comma at all**
   (`-dığı`, `-ınca`, `-erek`), so `split_sk` returns the whole sentence as one clause and the
   clause-aware machinery of AG v3/v4 — which was the entire point of v3 over v2 — silently
   degenerates to v2's flat reading.

8. **`:273` and `:275`** — `if low[0] in SUB[L]` and `if low[0] in IMPER[L]`, both Slovak word lists.
   `IMPER` (`:63-66`) is a hand-written list of 20 Slovak imperative *forms*; the equivalent in Turkish
   and Hungarian is a productive suffix, not a closed list.

### 1.5 F4v2 — person/number recovery, `phase1i/checker_1i.py`

`sk_features()` at `:536-570`, with the ending tests at `:559-568`:

```python
if x.endswith('š'):                     -> 2sg
if x.endswith('me') and len(x) >= 5:    -> 1pl
if x.endswith('te') and len(x) >= 5:    -> 2pl
if (x.endswith(('ím','ám','iem','em')) and len(x) >= 4
        and not x.endswith(('om','ním','tím','ctvom'))):  -> 1sg
```

plus `SK_PRON` `:458-460`, `SK_AUX` `:461` (`som/si/sme/ste`), `SK_PART` `:465`
(`re.compile(r'(al|il|ol|ul|el|yl|ml|dl|tl|sl|hl|žl|čl)(a|o|i)?$')`), `SK_PREP` `:524`,
`SK_NOT_VERB` `:526` (`sedem osem sem tam dom program problém systém krém sám iba` — a hand-written
anti-list of Slovak nouns that end like verbs), `SK_L_PART` `:529`.

The `em` line at `:568` **is the Czech bug**: `phase1v/trackC/cz_reader.py:32-35` patches exactly that
string out for Czech, because Czech `-em` is instrumental and Czech 1sg is `-ím/-ám/-u`. One character
class, four silent errors.

- **de, fr**: F4v2's *purpose* is **MOOT** — both mark person on the verb, but the subject is overt, so
  there is nothing to recover. What replaces it: in German, the need to read **case off the determiner**
  (§1.3) rather than person off the verb; in French, the need to distinguish the **three homophonous
  and near-homographic** forms `parle/parles/parlent` (1sg = 3sg = 3pl in writing after the stem) —
  a suffix test cannot separate `il parle` from `ils parlent` except by the `-nt`, and French
  orthography has whole paradigms where singular and plural are identical (`il finit` / … `ils
  finissent` is fine, but `il/ils` for `-er` verbs in the *passé simple* and the whole `être/avoir`
  compound system need the auxiliary).
- **es**: person marking is **clean and suffixal** (`-o/-as/-a/-amos/-áis/-an`) and pro-drop persists.
  F4v2's shape transfers better to Spanish than to anything else on the list. This is Spanish's one
  large advantage.
- **tr, hu**: person is suffixal and regular, but **vowel-harmonic** (Turkish 1sg `-ım/-im/-um/-üm`;
  Hungarian 1sg `-ok/-ek/-ök`) and **stacked after tense/aspect/evidentiality**. Turkish additionally
  has the **evidential `-mış`** (`gitmiş` = "he went, apparently / I'm told") which carries no direct
  English exponent and will interact badly with F9's tense/aspect machinery. Hungarian's **definite
  conjugation** (`látom` "I see it" vs `látok` "I see") means the verb ending encodes the *object's*
  definiteness — information the stack has no slot for, and which happens to be the exact information
  `tip_det_rule` assumes the source does not carry (§1.2(a)).
- **ua**: transfers; re-table in Cyrillic. Ukrainian 1sg is `-ю/-у`, 2sg `-єш/-еш/-иш` — note the
  Ukrainian 2sg ends in `ш`, and `checker_1i.py:559`'s `x.endswith('š')` is the right *rule* in the
  wrong *alphabet*.

### 1.6 F9 — aspect and the l-participle, `phase1n/f9.py`

~20 hand-written Slovak lexical sets: `BUD` `:21`, `COP` `:22`, `MOD` `:23`, `GO` `:26`, `CHYSTA` `:27`,
`PERF_LEX` `:30`, `IMPF_EXC` `:39`, `IMPF_LEX` `:53`, `PREF` `:65` (the perfectivising prefixes
`roz pri pre nad pod ob od do na po vy za vz`), `IMPF_SUF` `:66`, `FUT_ANCHOR` `:69`, `DO_TIME` `:71`,
`SUB_MARK` `:75`, `REPORT_V` `:79`, `L_NONVERB` `:83` (`svetlo číslo jedlo kreslo zrkadlo …` — nouns
that end in `-lo` and would otherwise be read as l-participles), `DET` `:90`, `PREPS` `:93`,
`ADJ_END` `:95`, `NON_VERB_I` `:96`. Then `_is_l_part()` `:124-145`, `_looks_present()` `:147-174`,
`_prefixed()` `:176-181`, `aspect()` `:183-208`.

The **entire aspect module is Slavic-specific by construction**. Perfective/imperfective as a
grammaticalised binary on every verb exists in **ua** (transfers, re-table) and in nothing else on the
list. German, French, Spanish, Turkish and Hungarian encode the same distinctions **periphrastically or
lexically** (French `imparfait` vs `passé composé`; Spanish `imperfecto` vs `pretérito` — genuinely
close in function; German has no aspect at all; Hungarian has verbal prefixes `meg-/el-/fel-` that are
*aspect-like* and, notably, sit in the same structural slot as `PREF` `:65`; Turkish has
`-yor/-ar/-dı/-mış` as a tense-aspect-evidentiality fusion).

`f9.py:100` `CLAUSE_SPLIT = re.compile(r"[,;!?…]|—|–|\s-\s|\bale\b|\btakže\b|\blebo\b|\bpreto\b|
\bpretože\b|\ba\b", re.I)` — the alternation is five Slovak conjunctions plus `a`. On any other
language it degrades to punctuation-only splitting. Note `\ba\b` is also the **Spanish preposition
`a`** and the **Hungarian definite article `a`**, both extremely frequent: the Slovak splitter will
shred Spanish and Hungarian sentences at every `a`. That is a Czech-`em`-class collision, in the
splitter.

### 1.7 Arm B — explicit subject insertion

`TRANSLATION_OFFLINE_PHASE1J_REPORT.md:12` (frozen configuration) and `:145`: *"Slovak sentences
rewritten with an explicit subject pronoun by a fixed rule; annotations (refs/`g`) were swapped
accordingly."* 1J measured arm B as buying FA 6.55 % → 5.05 % at no coverage cost (`:42`, `:400`).

- **de, fr**: **MOOT.** The rewrite is a no-op — the subject pronoun is already obligatory and already
  present. Arm B's 1.5 points of FA reduction are simply **not available**, because they were bought by
  fixing a problem these languages do not have. What replaces the risk: German's object-fronting under
  V2 (§1.4.4) and French's `on` and clitics (§1.4.1, §1.4.4) — both of which produce an *overt* but
  *wrong* subject, which arm B cannot help with and in fact makes more confident.
- **es, tr, hu, ua**: pro-drop persists, so arm B is still worth its 1.5 points — but "insert the
  pronoun a fixed rule recovers from the verb ending" requires the language's own person morphology to
  be readable first, i.e. it is downstream of F4v2 (§1.5) and cannot be built before it.
- Spanish note: inserting `yo/tú/él` where Spanish drops them is **pragmatically marked** (it reads as
  contrastive emphasis). The rewrite is grammatical but changes register — arm B's Slovak rewrite had
  the same property and 1J accepted it; worth re-checking, not assuming.

### 1.8 v5 `refsubj` / `rs_nom` — `stack_1v.py:43-90`

`ref_subject_heads()` reads the **English reference**, not the source — mostly language-neutral. The
one source-side dependency is `stack_1v.py:61`:

```python
if head in V4.EN_PRON:
    if not (sk_low & SK_PRON):
        continue
```

`SK_PRON` at `stack_1v.py:23` = `{'ja','ty','on','ona','ono','my','vy','oni','ony'}` (also
`agent_drop_v2.py:56`, imported by v3 `:34` and v4 `:59`, and consumed at `agent_drop_v3.py:370`,
`agent_drop_v4.py:263`). The test is *"only treat a reference pronoun subject as real if the source has
an overt pronoun"* — a pro-drop safeguard.

On all six this set never matches (Latin-script but wrong words for de/fr/es/tr/hu; Cyrillic for ua),
so the `continue` fires on **every pronoun-headed reference subject** and `rs_nom` never fires for them.
That is the *safe* direction (a missed catch, not a false one), but it silently removes the v5 patch's
coverage on exactly the pronoun rows 1V selected it for. For **de/fr** this is also arguably correct
behaviour by accident, since those languages always have the overt pronoun — the test would want to be
"always true", and it will be "always false".

`agent_drop_v3.py:370` — `if a[:1].isupper() and la not in SK_PRON: c.add(la)` — "a capitalised
non-pronoun is a proper name and has the same form in English". **German capitalises every noun.**
Every common noun in a German sentence passes this test and is added to the agent-candidate set as if it
were a proper name. This is a one-line, high-frequency, silent German bug of exactly the 1T kind.

### 1.9 Character-class dependence — the Cyrillic question for `ua`

There is **no `unicodedata` call and no `isascii()` call anywhere in the stack** (verified by grep over
all of the above files). Normalisation is not a lever; the character classes are written out as literal
ranges. Three of them are Latin-only:

| File:line | Regex | Effect on Cyrillic |
|---|---|---|
| `phase1i/checker_1i.py:469` | `re.findall(r"[a-záäčďéěíľĺňóôöŕřšťúůüýž]+", (sk or '').lower())` | returns `[]` |
| `phase1i/checker_1i.py:533` | same class, inside `sk_features` | returns `[]` |
| `phase1n/f9.py:99` | `WORD = re.compile(r"[a-záäčďéěíĺľňóôŕšťúýžô]+", re.I)` | returns `[]` |
| `phase1s/taskC/agent_drop_v2.py:66` | `re.findall(r"[A-Za-z']+", s)` | English side only — correct as is |

Two are script-agnostic and therefore **more** dangerous:

| File:line | Regex | Effect on Cyrillic |
|---|---|---|
| `phase1w/reader_nom.py:114` | `re.findall(r"[^\s.,!?;:()\"]+", s or '')` | tokenises Cyrillic fine |
| `phase1s/taskC/agent_drop_v2.py:127` | `re.findall(r"[^\s.,!?;:]+", sk or '')` | tokenises Cyrillic fine |

The combination is the specific Ukrainian failure path, and it is worth stating exactly:
`checker_1i.sk_features()` returns no features → `reader_nom._feats()` returns `None` at `:148-149` →
`read()` takes the `if f is None` branch at `:280` and never reaches `_decide_clause` → the loop ends
and `:285` returns `abstain:no main clause with a finite verb`. Meanwhile `_verbish()` at `:156-168`
also consults `sk_features` and finds nothing, so `vidx` would be empty anyway (`:228`).

**So `reader_nom` degrades to 100 % abstention on Ukrainian, not to silent error.** That is the benign
half. The malign half is that the three guards in §1.2 — `tip_det_rule`, `sk_clause_is_passive`,
`SK_REFLEX` — **do not go through the Latin tokenizer**: `tip_det_rule` runs `SK_DEM.search()` straight
on the raw string, `sk_clause_is_passive` uses `agent_drop_v3.sk_toks` (`:98`, script-agnostic), and
`SK_REFLEX` runs on the raw clause. All three therefore run, all three find nothing, and all three
return their confident negative. Ukrainian gets the worst of both: no subject reading at all, and all
three vetoes off.

For **ua**, every one of the ~35 tables in §1.3, §1.5 and §1.6 is **rewritten, not patched** — there is
no Czech-style "drop `em` from one tuple" available, because no Slovak string is a substring of any
Ukrainian word. The upside is that rewriting a table is mechanical and reviewable, and the *architecture*
around it is correct for Ukrainian in a way it is not correct for any of the other five.

### 1.10 Summary — which guards survive, moot, or break, per language

| Guard (file:line) | de | fr | es | tr | hu | ua |
|---|---|---|---|---|---|---|
| `tip_det_rule` `stack_1v.py:130` | **BREAKS** (articles) | **BREAKS** | **BREAKS** | **BREAKS** (acc. definiteness) | **BREAKS** (article + def. conj.) | **BREAKS** (Cyrillic `SK_DEM`) |
| `sk_clause_is_passive` `v3.py:279` | **BREAKS** | **BREAKS** | **BREAKS** | **BREAKS** (infix passive) | **BREAKS** | **BREAKS** (`-но/-то`) |
| `SK_REFLEX` `v2.py:62` | re-table | re-table | re-table (best case) | **REWRITE** (infix) | **REWRITE** | **REWRITE** (bound `-ся`) |
| arm B explicit subject (1J) | **MOOT** | **MOOT** | keep, rebuild | keep, rebuild | keep, rebuild | keep, re-table |
| F4v2 person/number `checker_1i.py:536` | **MOOT (purpose)** | **MOOT (purpose)** | re-table (clean) | **REWRITE** (harmony) | **REWRITE** (def. conj.) | re-table (Cyrillic) |
| `OBLEND` case filter `reader_nom.py:98,199` | **REWRITE** (syncretism) | vacuous | vacuous | **REWRITE** (agglut.) | **REWRITE** | re-table + vocative |
| pre-verbal NP scan `reader_nom.py:233` | **REWRITE** (V2, separable) | patch (clitics, `on`) | transfers | **REWRITE** (verb-final) | **REWRITE** | transfers |
| `split_sk` comma rule `v3.py:274` | transfers | patch | patch | **REWRITE** (converbs) | patch | transfers |
| F9 aspect `f9.py:183` | drop | re-model (tense) | re-model (tense) | **REWRITE** (TAE fusion) | **REWRITE** (prefixes) | re-table |
| `f9.CLAUSE_SPLIT` `f9.py:100` | patch | patch | **collides** (`a` prep) | patch | **collides** (`a` article) | patch |
| `v3.py:370` capitalised = proper name | **BREAKS** (noun caps) | transfers | transfers | transfers | transfers | transfers |
| `rs_nom` pro-drop safeguard `stack_1v.py:61` | silently off (harmless) | silently off | silently off (loses catches) | silently off | silently off | silently off |
| `stack_1w.py:23` hard-wired `'sk'` | edit required | edit | edit | edit | edit | edit |

---

## 2. Cost table — owner's variant 2, 1,000 concepts per language

### 2.1 Rates used, and why

**Annotation: 1,800 tokens/sentence — the Slovak rate.**
2E `:173`: *"Cost per sentence: 885 against Slovak's ≈ 1,800 (2D's Slovak total 6.84 M over 4,064 rows,
both passes)."* The Czech 885 is **not usable as a from-scratch rate**: most of Czech's `v` sessions were
already paid for inside 2D's run, and 92 % of 2E's own annotation spend went to `cz_0003_s04_v`, which
burned 527,721 tokens and 4,613 s and **returned zero rows** (2E `:40`, `:47`). A language started from
scratch pays the Slovak rate.

One honesty note on the anchor. 6,840,000 / 4,064 = **1,683**, not 1,800, and that 1,683 is explicitly
*"both passes"*, i.e. it already contains the `lk` pass (2D `:160`: `lk` = 1,924,126 tok = 473.5
tok/sentence). Annotation alone is therefore 6.84 M − 1.92 M = 4.92 M → **1,210 tok/sentence**, and
all-in is 1,683. Pricing at 1,800 **plus** a separate `lk` line double-counts `lk` and over-states the
model spend by roughly 35 %. I use the briefed 1,800 + 470 = **2,270 tok/sentence** as the headline
because that is the figure the owner asked for and it is the conservative direction, and I record
**1,683 tok/sentence all-in** as the low bracket. Both are shown below.

**`lk`: 470 tokens/sentence.** 2D `:160` Slovak 473.5; 2E `:100` Czech 465.6 — *"the same pass at the
same price"*. Midpoint 470.

**GATE 3: 0 model tokens.** 2C `:50` and 2E `:66`: random 50 rows per batch, scored by AG v4 and
`reader_nom` against that batch's **own stored model annotation**, bar 12 %. It is deterministic
re-scoring of work already paid for. `phase2f/gates_2f_cz.json` confirms the shape (50 scored per
batch). It costs **harness** tokens only — reading the gate file, writing the verdict, handling a STOP.
I charge **20,000 harness tokens** per language (1,000 concepts = 1 batch = 1 gate, plus one
re-run allowance), estimated, not measured.

**Engineering: 400,000 harness tokens per phase.** This is the one number with **no measurement behind
it**. 1T, 1V track C and 2C's GATE-1 fixes were all 0-model-call phases, so their cost was entirely
harness tokens and none of them recorded it. 400 k/phase is my estimate of a code-writing phase in this
repo. It is a **linear scale factor**: if the owner's own figure is 250 k or 600 k, multiply the
engineering column and the totals move proportionally. The **phase counts** below are the substantive
claim; the token conversion is not.

### 2.2 The Czech anchor for the engineering estimate

Czech is the closest language to Slovak that exists, and it still cost:

- **1T** — built the Czech validation set and **found four named bugs** (`em`, `se`, `jestli`, `aspect`;
  `phase1v/trackC/SECTION.md:34-50`). ≈ 1 phase.
- **1V track C** — `cz_reader.build()` re-executing the four Slovak source files into patched copies,
  with sha-verified non-mutation of the originals. ≈ 0.5 phase.
- **2C** — **three more fixes** (`phase2c/derive_2c.py:231-235`, `MODES = {"before": dict(tok=False,
  verbish=False, agent=False), … "after": dict(tok=True, verbish=True, agent=True)}`). ≈ 1 phase.

**≈ 2.5 phases**, seven named defects, and the result is still the **weaker** of the two languages:
Czech `agent_nom` **21.05 % [9.55, 37.32]** against Slovak **11.63 % [3.89, 25.08]**, Czech `gender`
**19.23 % [6.55, 39.35]** against Slovak **11.63 %** (2C report `:106-107`, both **FAIL**). Merged-file
AG v4 on Czech **10.40 % [6.91, 14.87]** against Slovak **10.00 %** on a 12 % bar (2E) — passing, but
with the discrepancy 2E `:152` records as *"unexplained and unmeasured at scale"*.

**Czech — a language that shares Slovak's alphabet, case system, aspect system, pro-drop and clause
punctuation — cost 2.5 phases and is still failing two GATE-1 fields.** No language below is closer to
Slovak than Czech is. 2.5 phases is the floor, not the estimate.

### 2.3 Phase counts, and what drives each one up

| Lang | Phases | Drivers |
|---|---|---|
| **ua** | **4.0** | Architecture transfers whole (case, aspect, l-participle, pro-drop, no articles, comma-before-subordinate). Work is: rewrite ~35 literal tables into Cyrillic; widen three tokenizer character classes (`checker_1i.py:469,533`; `f9.py:99`); rewrite `SK_REFLEX` as a **suffix** test for bound `-ся/-сь`; add the **vocative** to the oblique filter; write a new detector for the **`-но/-то` impersonal** (no auxiliary — genuinely new). 1.5 phases over Czech's 2.5 for the script rewrite and the two genuinely new guards. |
| **es** | **5.0** | Pro-drop architecture survives (arm B, F4v2 shape, `se` reflexive as a free clitic in the Slavic slot — the single best transfer on the list). Against it: **no case morphology**, so `OBLEND` is vacuous and the subject filter must be rebuilt on word order + `PREP`; **articles** kill `tip_det_rule`'s premise outright; `ser/estar` + participle is ambiguous between passive and predicative in a way `SK_BYT`+`SK_PPART` cannot express; `f9.CLAUSE_SPLIT`'s `\ba\b` collides with the preposition `a`; aspect must be re-modelled as `imperfecto`/`pretérito`. |
| **fr** | **5.5** | Everything in `es`, **minus** arm B and F4v2's purpose (non-pro-drop — a real saving), **plus**: **object clitics** `le/la/les/lui/leur/en/y` sitting in the pre-verbal scan window with `la/les` homographic with the articles (the French `em` bug, §1.4.4); **`on`** producing an overt nominative with impersonal meaning and inverting AG's verdict (§1.4.1); `être` + participle ambiguous between compound past and passive; written person syncretism (`parle/parles/parlent`); comma rules that do not mark subordination, so `split_sk` mis-splits. |
| **de** | **6.0** | Non-pro-drop saves arm B and F4v2's purpose, and German's mandatory comma before subordinate clauses makes `split_sk` transfer cleanly — the two genuine freebies. Against them, the three most expensive items on the whole audit: **V2 with object-fronting** and **verb-final subordinate clauses** break the "first NP before the first finite verb" reading outright; **case syncretism** means there is no noun suffix to filter on, so `_np()` must be rebuilt to read case off the **article** — a different algorithm, not a different table; **separable verbs** scatter the predicate; **`man`** mirrors French `on`; and `agent_drop_v3.py:370`'s "capitalised = proper name" is wrong on **every German common noun**. |
| **tr** | **8.0** | Nothing transfers. **Agglutination with vowel harmony** makes every fixed-suffix tuple (`VEND`, `OBLEND`, `PLEND`, `AMBI`, `ADJEND`, `SK_PART`, `IMPF_SUF`) unrepresentable — this needs a **morphological analyser**, an artefact class that does not exist anywhere in this repo. **Verb-final** collapses the pre-verbal window. **Passive is an infix** (`-il/-in/-n`), invisible to any auxiliary+participle detector. **Subordination is suffixal with no comma**, so `split_sk` returns one clause and AG v3/v4's clause-awareness — v3's entire reason for existing over v2 — silently degenerates. **Evidential `-mış`** has no English exponent and no slot in F9. Definiteness lives on the **accusative suffix**, the inverse of `OBLEND`'s logic. Pro-drop persists, so arm B and F4v2 must both be rebuilt on top of the analyser. |
| **hu** | **8.0** | Everything in `tr` — agglutination, harmony, ~18 cases, pro-drop, no cognate to the Slavic case table — **plus**: **definite conjugation** (`látom`/`látok`), where the verb ending encodes the *object's* definiteness, i.e. precisely the information `tip_det_rule` assumes the source cannot carry, and for which the stack has no slot at all; **zero copula in the 3rd person present**, so `_verbish()` finds no finite verb and `reader_nom` abstains at `:228` across a large slice of ordinary sentences; **no grammatical gender**, so `reader_nom.py:218`'s gender discriminator is inert; `f9.CLAUSE_SPLIT`'s `\ba\b` collides with the Hungarian **definite article `a`**, shredding sentences at every article. Verbal prefixes (`meg-/el-/fel-`) sit in `PREF`'s structural slot, which is the one small transfer. |

### 2.4 The table

Per language, 1,000 concepts. Annotation = 1,000 × 1,800. `lk` = 1,000 × 470. GATE 3 = 20,000 harness.
Engineering = phases × 400,000 harness.

| Lang | Annotation | `lk` | GATE 3 | Engineering | **Total** |
|---|---:|---:|---:|---:|---:|
| **ua** | 1,800,000 | 470,000 | 20,000 | 4.0 × 400,000 = 1,600,000 | **3,890,000** |
| **es** | 1,800,000 | 470,000 | 20,000 | 5.0 × 400,000 = 2,000,000 | **4,290,000** |
| **fr** | 1,800,000 | 470,000 | 20,000 | 5.5 × 400,000 = 2,200,000 | **4,490,000** |
| **de** | 1,800,000 | 470,000 | 20,000 | 6.0 × 400,000 = 2,400,000 | **4,690,000** |
| **tr** | 1,800,000 | 470,000 | 20,000 | 8.0 × 400,000 = 3,200,000 | **5,490,000** |
| **hu** | 1,800,000 | 470,000 | 20,000 | 8.0 × 400,000 = 3,200,000 | **5,490,000** |
| **grand total** | **10,800,000** | **2,820,000** | **120,000** | **36.5 phases = 14,600,000** | **28,340,000** |

Arithmetic:

```
model spend per language   = 1,800,000 + 470,000              = 2,270,000
harness per language       = 20,000 + phases × 400,000
ua 3,890,000 + es 4,290,000                                   =  8,180,000
        + fr 4,490,000                                        = 12,670,000
        + de 4,690,000                                        = 17,360,000
        + tr 5,490,000                                        = 22,850,000
        + hu 5,490,000                                        = 28,340,000
phases  4.0 + 5.0 + 5.5 + 6.0 + 8.0 + 8.0                     = 36.5
```

**Low bracket**, using 2D's own all-in 1,683 tok/sentence (annotation + `lk` together, no
double-count) instead of 1,800 + 470:

```
model spend per language   = 1,683,000   (saves 587,000 each, 3,522,000 across six)
grand total                = 28,340,000 - 3,522,000           = 24,818,000
```

So: **24.8 M – 28.3 M tokens for all six at 1,000 concepts each**, of which **14.6 M (52–59 %) is
engineering, not annotation**. The engineering dominates, and it is the least measured number in the
table.

---

## 3. Which single language is cheapest to do next

**Ukrainian, at 3,890,000 tokens (4 phases of engineering).** The argument is the guard audit, not
intuition: Ukrainian is the only one of the six for which the *architecture* of the frozen stack is
correct. It is pro-drop, so arm B's 1.5 points of FA reduction and F4v2's whole purpose survive intact
rather than going moot as they do in German and French. It has a real nominative/oblique case system, so
`_np()`'s suffix filter at `reader_nom.py:199` is the right *kind* of test and needs only Cyrillic
strings. It has grammaticalised perfective/imperfective aspect, so F9's twenty lexical sets are a
translation job rather than a redesign. It has no articles, so `tip_det_rule`'s founding premise — the
one thing that is false in de, fr, es and hu — is **true**. And it marks subordination with a mandatory
comma, so `split_sk` transfers, which is the guard whose loss silently reduces Turkish to AG v2. Against
that, Ukrainian's costs are real but *bounded and mechanical*: rewriting ~35 literal tables, widening
three Latin-only character classes (`checker_1i.py:469`, `checker_1i.py:533`, `f9.py:99`), converting
`SK_REFLEX` from a whitespace-delimited particle regex to a suffix test for bound `-ся/-сь`, adding the
vocative to the oblique filter, and writing one genuinely new detector for the `-но/-то` impersonal.
Those are table-shaped tasks with reviewable diffs, which is why I price Ukrainian at 4 phases against
Czech's actual 2.5 rather than at Spanish's 5 — and the Cyrillic tokenizer break is, unusually, in the
*safe* direction: `reader_nom` abstains on everything rather than erring (§1.9), so the Ukrainian
failure mode during development is loud, which is worth a great deal given that all seven Czech bugs
were silent.

The runner-up is **Spanish at 4,290,000**, which wins on the single most valuable guard in the stack:
its reflexive `se` is a free clitic in the same syntactic slot as Slovak `sa`, so `SK_REFLEX` — the
guard whose Czech miss produced 23 silent errors and which 2B settled as the cause of g4's 22–26 %
residual — is a one-line re-table rather than a rewrite. Spanish also keeps pro-drop with clean suffixal
person marking, so arm B and F4v2 transfer better than to anything else on the list. It loses to
Ukrainian on three counts: no case morphology at all, so `OBLEND` is vacuous and the subject filter must
be rebuilt from scratch; articles, so `tip_det_rule` is broken rather than merely re-tabled; and
`f9.CLAUSE_SPLIT`'s `\ba\b` colliding with the Spanish preposition `a`.

**What would change the answer.** Two things, and one of them is cheap to check. First, if the 400,000
tokens/phase conversion is badly wrong in the *upward* direction, the engineering column dominates even
harder and Ukrainian's 4-vs-5-phase edge over Spanish widens — the answer is robust to that. But if
engineering is much *cheaper* than 400 k/phase, the model spend (identical 2,270,000 for every language)
swamps the difference and the six become nearly indistinguishable on cost, at which point the decision
should be made on **whose FA rate will be worse**, not on price — and there Spanish's `se` advantage
probably beats Ukrainian's script tax. Second, and more decisively: this whole ranking assumes the
stack is worth porting at all. 2C's own §7 recommendation (`:243-244`) is to *"decide whether a
44 %-abstaining reader is worth keeping or whether voice/agent_nom should simply be model-authored
everywhere."* If the answer to that is "model-authored", the engineering column **goes to zero for all
six**, every language costs the same 2,290,000, and the cheapest-next question dissolves — which is
itself a reason to settle 2C §7 before spending 14.6 M tokens porting guards.
