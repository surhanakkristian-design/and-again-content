# Phase 1T / Task B — INVENTORY (3.1 report + 3.2 preparation). 0 model calls, DB read-only (SELECT only).

## 0. What the translate-the-sentence format actually reads
`supabase/functions/check-translation/index.ts:166-178` selects
`exercise_localizations ( language_code, full_sentence )` for exactly two codes and never trusts the client:
reference = learning-language `full_sentence`, prompt = native `full_sentence` (`.in(... [learningLanguage, nativeLanguage])`).
Allowed natives, `check-translation/logic.ts:33`: `en, sk, cz, fr, ua, de, es, tr, hu` ("every language the
exercise_localizations table holds"). Level is NOT on `exercises`; it comes from `exercise_types.level`.
There is no separate "translate" exercise type — any exercise whose native row and `en` row both carry a
`full_sentence` is usable; `chunks` is only for the chunk/tile variant (`lib/translateExercise.ts`).

## 1. Language / count table
SQL used (one statement, read-only; `| lvl=… | rows=… |` lines):
```sql
select el.language_code, et.level, count(*) rows,
       count(*) filter (where nullif(trim(el.full_sentence),'') is not null) with_sentence,
       count(*) filter (where el.chunks is not null) with_chunks,
       count(*) filter (where nullif(trim(el.full_sentence),'') is not null and exists (
         select 1 from exercise_localizations en where en.exercise_id=el.exercise_id
           and en.language_code='en' and nullif(trim(en.full_sentence),'') is not null)) translatable_pair
from exercise_localizations el join exercises e on e.id=el.exercise_id
left join exercise_types et on et.id=e.exercise_type_id group by 1,2;
```
Sentences (= non-empty `full_sentence`) per native language, per `exercise_types.level`.
Every level-`A` row (3,854 exercises) is empty in every language, so it is dropped from the totals.

| lang | A1 | A2 | B | B1 | B2 | total sentences | of them paired with EN | with `chunks` |
|---|---|---|---|---|---|---|---|---|
| en | 9,999 | 13,591 | 1,740 | 8,906 | 7,002 | 41,238 | — | 23,672 |
| sk | 9,999 | 13,591 | 1,740 | 8,906 | 7,002 | 41,238 | 41,238 | 0 |
| cz | 9,999 | 13,591 | 1,740 | 8,906 | 7,002 | 41,238 | 41,238 | 0 |
| de | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 23,689 |
| es | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 23,595 |
| fr | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 23,638 |
| hu | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 0 |
| tr | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 0 |
| ua | 8,523 | 11,627 | 1,740 | 4,655 | 4,410 | 30,955 | 30,955 | 0 |

`supported_languages`: all nine are `is_native_option=true`; only `en, de, es, fr` are learning options
(`available_levels` is NULL for all nine). No language is empty. Czech is the ONLY other native with the
same 41,238-sentence coverage as Slovak — every Slovak sentence has a Czech sibling on the same exercise id.

## 2. Annotation fields the offline stack needs
Checked the live schema for annotation-like columns
(`column_name ilike` any of voice/agent/tense/aspect/perfect/gender/person/annotat in `public`) → **NONE**.
So every field below is offline-file-only and Slovak-only; nothing is per-language in the DB.

| field | where it lives | made how | languages |
|---|---|---|---|
| `voice_sk` (active_agent / agentless / …) | `phase1p/data/annotations.json` (120 sids), `annotations_src_part1..4.json`, `phase1m/data/annotations*.json` | hand annotation over the Slovak | Slovak only |
| `agent_nom` (bool, nominative agent present) | same files | hand | Slovak only |
| `tf_gold` (gold time frame) + `phase1k/taskB/gold_tf.jsonl` | same files / that gold | hand | Slovak only |
| `tense_open` (bool) | same files | hand | Slovak only |
| `perfective_present` (bool) | same files | hand | Slovak only |
| `p` chain (person/number of the subject) | code `phase1j/taskA/p_chain.py` (`derive_p`), stored `phase1j/taskA/annotations_p_dev.json` | DERIVED from the Slovak string only | Slovak only |
| `g` chain (gender openness) | annotation key `g`, carried `phase1j/make_split_1j.py:221`, rendered `phase1i/pipeline_1i.py:40,220` (`GENDER_TMPL`) | hand | Slovak only |

For Czech: sentences exist (41,238) but **zero annotation of any kind exists**. Every annotation-driven
guard would run on `ann = {}`.

## 3. Guard table (current / frozen versions) and how gold validation was run on Slovak
| guard | file | entry | inputs | gold validation |
|---|---|---|---|---|
| Time frame (F9) | `phase1n/f9.py` (latest; older `phase1l/f9.py`, `phase1k/taskB/f9.py`) | `sk_frame(slovak, annotation=None)` → frames+reason; `check(slovak, annotation, answer)` → reject/accept/tip/abstain (`f9.py:284,493`) | raw Slovak string; annotation optional (not required) | `phase1k/taskB/validate_f9.py` vs `gold_tf.jsonl` (140 lines, `{"sid","gold_frames":[…],"gold_voice":"active|impersonal|…"}`) over `sentences_140.jsonl`; re-run `phase1l/validate_f9_1l.py`, `phase1m/validate_f9_1l.py` |
| Person/number (F4v2) | `phase1i/checker_1i.py:523-660` | `sk_features(sk)` (line 536) → person/number/gender or None; `f4v2_subject_mismatch(it)` (line 608) reads item `sk` + `answer` | raw Slovak + the learner answer; no annotation | no jsonl gold: an assertion block in `checker_1i.py:1182-1212` writes `f4v2_verification.json` — requirement "all C:9498 answers abstain; W:4571:… and W:3494:… still fire", plus cost_on_235 / kills_on_105 counts; verdict PASS/FAIL |
| `p` chain guard (f4p) | `phase1j/taskA/p_chain.py` | `derive_p(sk, annotation)`, `f4p_guard(answer, p, annotation)` | Slovak string + annotation `g` | `phase1j/taskA/measure_a.py` → `results_offline.json` (offline counts, 0 model calls) |
| AG (nominative-agent / agent drop) | v1 `phase1s/taskA/agent_drop.py`, v2 (current) `phase1s/taskC/agent_drop_v2.py`; applied by `phase1s/taskC/ag_apply.py` | `decide(sk, ann, wtags, answer, reference, variant)` (v2 line 154); helpers `slovak_agent` (118), `has_nominative_agent` (136) | Slovak string, annotation (`agent_nom`, `voice_sk`), writer_tags, answer, reference | `preflight()` (v2 line 254) over the `SYN` synthetic rows (line 204) — PASS/FAIL per row, primary+noun variants; then re-score of the frozen 1P items + LLM judge (`phase1s/taskC/judge/verdicts.json`, `RESCORE_1S_C_JUDGED.md`) |
| Passive / reflexive-passive detection | `phase1s/taskC/agent_drop_v2.py:76` `find_passive(answer)` (ENGLISH side: BE+participle, lists at 19-53); Slovak side = `SK_REFLEX` (62) + `voice_sk` annotation; withdrawn lever `phase1p/lever1.py:69,86` | answer (EN) for `find_passive`; Slovak + annotation for the voice call | inside the same AG `preflight()` SYN rows; the Slovak voice itself was validated via `gold_voice` in `gold_tf.jsonl` (`validate_f9.py`, using `f8.sk_agent`) |

Validation vocabulary used by `validate_f9.py` (lines 36-44): `AGREE` = predicted frame set == gold set;
`CONSERVATIVE` = predicted set empty, or gold ⊂ predicted (guard widened / abstained);
`ERROR` = the gold frame is NOT in the predicted set (an asserted wrong frame). Only ERROR counts as a
guard defect; CIs via Clopper-Pearson (`cp()`).

## 4. Every Slovak-specific spot in those guards, and what Czech would do
`ABSTAIN` = silently stops firing (coverage loss); `MISFIRE` = silently asserts something false. No crashes
found: everything is `dict.get` + regex, and the token regex
(`checker_1i.py:532`, `p_chain.py:26`) already contains `ě ř ů`, so Czech tokenises fine.

F9 time frame (`phase1n/f9.py`):
- `:21` `BUD` = budem/budeš/bude/budeme/budete/budú (+ne-). Czech budu/budeš/bude/budeme/budete/budou — 1sg and 3pl never match → **ABSTAIN** on those futures.
- `:22` `COP` = je/sú/som/sme/ste/niet. Czech je/jsou/jsem/jsme/jste — only `je` matches → copula frame lost → **ABSTAIN**.
- `:23` `MOD` musí/môže/chce/vie… Czech musí, chce, myslí match; **môže→může, vie→ví, dokáže→dokáže(ok)** → partial **ABSTAIN**.
- `:30` `PERF_LEX` and `:33-71` the imperfective present lists (kúpi, dá, vráti, žije, varí…). Czech koupí, dá, vrátí, žije, vaří → large majority miss → aspect "unknown" → frame widens → **ABSTAIN** (conservative by design).
- `:72` time nouns (desiatej, siedmej, leta, jesene) → Czech desáté, sedmé, léta, podzimu → **ABSTAIN**.
- `:75` `SUB_MARK` ak/keď/keby/kým/až/že/prečo/kedy/či/ktorý/lebo/pretože/hoci/keďže. Czech: `že`, `až`, `aby` match; keď→**když**, keby→**kdyby**, ak→**jestli**, prečo→**proč**, kedy→**kdy**, či→**zda/jestli**, ktorý→**který**, lebo/pretože→**protože**, hoci→**ačkoli** → subordinate clauses unseen → **ABSTAIN**, and in a reported-speech sentence (`:287`, `že/prečo/kedy/či/ako`) the `že` branch still fires so behaviour is uneven.
- `:85-86` the "-l is a NOUN not a participle" exception list (stôl, uhol, kotol, popol, orol, posol, apríl, hotel, model, bicykel, kúpeľ, bol/bola/boli). Czech stůl, úhel, kotel, popel, orel, posel, duben, byl/byla/byli → the Czech nouns are NOT excluded → read as l-participles → **MISFIRE** (asserted past frame on a present sentence). This is the sharpest risk in F9.
- `:100` `CLAUSE_SPLIT` includes `ale|takže|lebo|preto|pretože|a`. Czech has ale/takže/proto/a; `lebo`,`pretože` never occur, `protože` is not in the alternation → coarser clauses → **ABSTAIN**.
- `:79` `REPORT_V` povedal/spýtal/myslel… Czech řekl/zeptal (miss), myslel/věděl-ish (partial) → **ABSTAIN**.
- `:484` `WISH_SK` prial/želal/chcel/kiež → Czech přál/přála/chtěl/kéž → **ABSTAIN** (the wish/conditional softener disappears, so a conditional could reach the `reject` branch at `:538` → possible **MISFIRE**).
- `:493` `check(slovak, annotation, answer)` takes the annotation but tolerates `None`, so Czech-without-annotation runs.

F4v2 person/number (`phase1i/checker_1i.py`):
- `:458` `SK_PRON` (ja, ty, on, ona, ono, my, vy, oni, ony). Czech **já** (with á) misses → 1sg pronoun lost → **ABSTAIN**; ty/on/ona/ono/my/vy/oni/ony are spelled identically → those keep working.
- `:461` `SK_AUX` som/si/sme/ste → Czech **jsem/jsi/jsme/jste**: no match, and Czech `si` is only the reflexive-dative clitic → past auxiliaries invisible.
- `:575` `past_marker` = by/keby/aby/zeby/som/si/sme/ste → Czech `by`,`aby` match, `kdyby` does not, `jsem/jsme/jste` do not, but Czech reflexive **`si`** does → the marker fires on the WRONG evidence: "Dal si kávu" arms the participle reader, while "Koupil jsem knihu" does not → mixed **ABSTAIN** + **MISFIRE**.
- `:596` `ambiguous_si` / `has_aux`: with Czech `si` meaning only "for oneself", the guard will keep suppressing the 3rd-person default exactly where Czech is unambiguous → **ABSTAIN**.
- `:529` `SK_L_PART` `(l|la|lo|li|ly)$`: Czech uses the same -l participles (dělal/-a/-o/-i/-y) → transfers, but only behind the broken `past_marker`.
- present-ending rules `:555-573`: `-š`, `-me`, `-te`, `-ím/-ám/-iem/-em` all exist in Czech with the same person/number → these transfer. BUT the exclusion list `not x.endswith(('om','ním','tím','ctvom'))` is Slovak: the Czech **instrumental is `-em`** (autem, vlakem, bratrem, večerem) where Slovak has `-om` → any Czech instrumental noun ≥4 chars not directly after a preposition is read as a 1sg present verb → **MISFIRE** (false person clash → false reject). Czech 1sg `-u` (nesu, píšu) and 3pl `-ou/-í` (nesou, dělají) are not read → **ABSTAIN**.
- `:524` `SK_PREP` s/so/z/zo/k/ku/v/vo/na/do/od/po/…: Czech s/se, z/ze, k/ke, v/ve, na, do, od, po → `so/zo/ku/vo` miss their Czech `se/ze/ke/ve`, which is also how the instrumental misfire above escapes the `after_prep` shield → **MISFIRE**.
- `:526` `SK_NOT_VERB` (sedem, osem, sám, však, iba, práve, ešte, aspoň) → Czech sedm, osm, sám, však, jenom, právě, ještě, aspoň; the numerals lose their `-em` shape so no harm, the rest are ≥4 chars but don't hit an ending rule.

AG / passive (`phase1s/taskC/agent_drop_v2.py`, same lines in `taskA/agent_drop.py`):
- `:56` `SK_PRON`, `:58` `PRON_EQ` (ja→i/me …) → Czech `já` misses → **ABSTAIN** on the 1sg mapping.
- `:62` `SK_REFLEX = (sa|si)` and its use at `:128`. Czech reflexive is **`se`** (`si` = dative). A Czech reflexive passive ("Dveře se zavírají", "Prodává se dům") is NOT recognised as reflexive → the `not SK_REFLEX.search(sk)` branch treats it as an ordinary active with a subject → **MISFIRE**, the exact class (agentless/reflexive passive) that Phase 1S identified as the open wound.
- `:118` `slovak_agent`, `:136` `has_nominative_agent` read `ann['agent_nom']` / `ann['voice_sk']`, which do not exist for Czech → with `ann={}` both go falsy → **ABSTAIN** (whole AG rule inert), so the reflexive misfire above only surfaces once Czech annotation is written.
- `:76` `find_passive`, `:19-53` BE/IRREG_PP/FINITE/DET_START lists are ENGLISH-side → language-neutral, unaffected.

## 5. Sample for 3.2
`phase1t/taskB/cz_sample.json` — 120 rows, stratified 24 per `exercise_types.level` (A1, A2, B, B1, B2),
ordered by exercise id; each row = `{exercise_id, level, exercise_type_id, cz, en, sk, rn}`.
All 120 have a Slovak sibling. Nothing invented: every string is a live `exercise_localizations.full_sentence`.
No guard was run on Czech and no gold was written, per the task.
