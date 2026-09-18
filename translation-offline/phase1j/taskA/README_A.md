# Task A — the `p` (person / number) chain: API and limits

Agent A, Phase 1j, 18 Sept 2026. Files: `p_chain.py` (the chain), `measure_a.py` (zero-call DEV
measurement), `annotations_p_dev.json` (the DEV chains), `TASK_A_OFFLINE.md` + `results_offline.json`
(the measurement). No model call was made by this task; the holdout was touched once, count only.

## 1 What `p` is

`p` is the sibling of the `g` (gender) chain: a per-SENTENCE fact derived from the **Slovak only** — the
English reference is never consulted, as in `checker_1i.sk_features` and `taskC` F4v3. It exists because
10 of the 23 Phase 1i holdout false acceptances were singular -> plural recasts (8 of them he/she -> they),
every one on a Slovak sentence with a dropped subject: the P-E4b gender line licences the other gender and
the model generalised that licence to person and number. `p` states the person/number and withdraws the
licence there; `f4p` rejects an answer whose main-clause subject pronoun contradicts it.

## 2 API

```python
import p_chain as PC

PC.derive_p(sk, annotation) -> dict | None
# {'person': 1|2|3|None, 'number': 'sg'|'pl'|None, 'gender': 'm'|'f'|'n'|None,
#  'subject': 'dropped'|'explicit', 'en_subjects': ['he','she','it','you'],
#  'evidence': 'l-participle trénoval -> person 3, number sg, gender m', 'signals': [...],
#  'has_g': True}            # None = ambiguous; `annotation` is the loader entry (used for has_g only)

PC.explain_p(sk, annotation) -> (p|None, reason)      # same, plus why it stays ambiguous
PC.p_prompt_line(p)          -> str                   # ONE line, '' when p is None
PC.f4p_guard(answer_en, p, annotation) -> (reject: bool, reason: str)
PC.f4p_subject_mismatch(it, annotation) -> (hit, trace)    # guards_c-compatible adapter, it = {sk, answer}
PC.annotate(annotations, sentences, out_path) -> {sid(str): p|None}   # also sets ann[sid]['p_chain']
PC.p_of(ann_entry, sk) -> p|None                      # stored chain, else derived on the fly
```

CLI (0 calls): `PYTHONDONTWRITEBYTECODE=1 python3 p_chain.py --side dev` writes `annotations_p_dev.json`.
**Holdout entry point, to be run mechanically by the final-run agent (agent A never ran it):**
`PHASE1J_FINAL=1 PYTHONDONTWRITEBYTECODE=1 python3 p_chain.py --side holdout` writes
`annotations_p_holdout.json`. `--count-all` prints counts only over all 140.

## 3 How agent R plugs it in

**Flag names: `p_prompt` (the prompt line) and `f4p` (the guard). They are independent rows.**

*Prompt* — in `pipeline_1i.build_prompt`, P-E4b branch, the p line sits **immediately after the gender
line**, i.e. in the same slot, before `GROUND_LINE`:

```python
gline = GENDER_TMPL.format(...) if g else None
pline = PC.p_prompt_line(PC.p_of(st['ann'].get(str(r['sid'])), r['sk'])) if flags.get('p_prompt') else ''
extra = ([gline] if gline else []) + ([pline] if pline else []) + [GROUND_LINE, WORDING_LINE]
```

The call shape is unchanged (same system instruction, same `generationConfig`, still one word back).
**Any prompt text change invalidates the stored P-E4b verdicts for that item** — a `p_prompt` row must be
called fresh and counted against the 1,400 cap; an `f4p`-only row reuses the stored verdicts (0 calls).

*Guard* — same mechanism as `taskC/guards_c.apply` (a guard only turns an acceptance into a rejection):

```python
import guards_c as G
G.GUARDS['f4p'] = lambda it: PC.f4p_subject_mismatch(it, ANN.get(str(it['sid'])))
G.ORDER = G.ORDER + ('f4p',)          # after F4v3
G.apply(checker_module, guards=('F5t', 'F6', 'F4v3', 'f4p'))
```

`f4p` is *not* a superset of F4v3: it reads more sentences (3sg present in -í/-i, clause selection) but
checks **person and number only, never gender** — gender stays with the `g` chain and with F4v2/F4v3, so
the two guards cannot contradict each other.

## 4 What the derivation does and does not claim

Signals (Slovak only): nominative pronouns, past auxiliaries `som/sme/ste` (`si` is ambiguous and blocks
the person), `byť`-futures `budem…budú`, a closed list of frequent finite forms (`má, musí, môže, chce,
vie, ide, príde, dá` + plurals + `ne-`), present endings `-š / -me / -te / -m / -ujú / -ajú / -uje` and
3sg `-í / -i`, and l-participles `-l/-la/-lo/-li` (which also give the gender). Every signal must agree;
one disagreement cancels that feature; if neither person nor number survives, `p` is `None`.

Conservative by construction, i.e. `None` on: imperatives and the impersonal `hovorí sa` (no signal at
all), impersonals `prší / treba`, dative-experiencer recasts (`podarilo sa jej`, `bude sa ti to páčiť`),
the present copula `je/sú` (existentials, explicit noun subjects), quantified subjects (`veľa ľudí` takes
a 3sg verb but is plural English — the number claim is dropped), and **any clause introduced by a
subordinator**: only the first clause plus coordinated/unmarked clauses are read, because
`Naniesla si už tri vrstvy, takže jej riasy vyzerajú obrovské` would otherwise claim 3pl from the lashes
and reject the correct singular answer (sid 7444).

`f4p` fires only when **every** main-clause subject pronoun of the answer contradicts the person or the
number. It abstains on: no `p`; no pronoun subject (noun subjects are never numbered); any compatible
pronoun anywhere (the F4v2 rule); `you` always; `I`/`we` against a Slovak generic 2nd person; an
indefinite antecedent anywhere in the answer (`everyone … they` — singular *they* cannot be separated, so
the guard stays silent); a pronoun after a reporting verb (`The director said that they would film …` has
no main-clause pronoun subject); and the impersonal frame `they say / people say`.

## 5 Known limits

- **Coverage is morphological, not lexical.** 19 of 70 DEV and 23 of 70 holdout sentences stay ambiguous,
  almost all with "no readable person/number morphology" (3sg present in `-e`/`-á`, 3-letter participles
  `mal/bol/dal`, `-ia` 3pl which collides with the `-cia` nouns). Raising coverage needs a verb lexicon.
- **l-participle false friends.** A noun or adjective in vowel + `l(a|o|i)` can look like a participle
  (`škola`, `sila`, `telo`, `biela`). Handled by a stoplist, by refusing `-lá` (adjectives) and `-ly`
  (modern Slovak has only `-li`), and by the consonant-stem test; a stoplist is not a lexicon, so a new
  noun of that shape on an unseen sentence can produce a wrong 3sg claim. The DEV hand-check found 0 such
  errors in 70 sentences, which bounds the rate loosely at a few percent.
- **The reference is deliberately not consulted** (the `derive_p` signature has no reference). Using the
  reference's subject number as a *veto* would be a cheap accuracy gain and stays conservative; it was not
  built because it changes the signature and the F4 family's honesty rule.
- **Multi-subject sentences yield an open feature, not a claim**, so `f4p` then only checks the person.
- **`any compatible pronoun -> abstain`** costs recall: `They kept throwing the same combination until it
  went smoothly` is not rejected because the subordinate `it` fits (DEV item `W:8799:1222448868`).
- **The prompt line cannot be measured offline.** Its effect (does stating the person/number stop the
  recast without losing correct answers?) needs agent R's DEV run; only `f4p` was measurable here.
