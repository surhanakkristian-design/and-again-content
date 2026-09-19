#!/usr/bin/env python3
"""Phase 2C SELECTION (§3.1). 2B's rule verbatim (data_2b.py CTE, byte-identical), plus:
  - exclusion of the union of every test-set id, 2A's selected rows and 2B's 200-row sample;
  - if a (concept, level) pick is excluded, the next-lowest md5 non-excluded candidate is taken;
  - if no candidate remains, the slot is dropped and recorded.
DB read-only SELECTs via the linked Supabase CLI (`db query --linked -o json`, cwd ~/Projects/and-again). 0 Gemini calls."""
import json, os, re, glob, subprocess, collections
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(H)
APP = os.path.expanduser("~/Projects/and-again")
SB = os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")
def q(sql):
    p = subprocess.run([SB, "db", "query", sql, "--linked", "-o", "json"], cwd=APP, capture_output=True, text=True)
    o = p.stdout
    if "{" not in o: raise SystemExit("query failed: " + (p.stderr or "")[-400:])
    return json.loads(o[o.find("{"):])["rows"]

# ---------------------------------------------------------------- 2B rule, verbatim (phase2b/data_2b.py)
CTE = """with vt as (
  select e.concept_id, t.level from exercises e join exercise_types t on t.id = e.exercise_type_id
  where t.focus_category->>'en' = 'Vocabulary'),
vl as (select concept_id,
         case when bool_or(level = 'A') and not bool_or(level = 'B') then 'A'
              when bool_or(level = 'B') and not bool_or(level = 'A') then 'B' end vlev
       from vt group by 1),
ge as (  -- grammar-topic exercises (focus Grammar, level A1..B2, not the 'Random' pseudo-topic) with an en full_sentence
  select e.id exercise_id, e.concept_id, t.level, e.exercise_type_id
  from exercises e join exercise_types t on t.id = e.exercise_type_id
  join exercise_localizations en on en.exercise_id = e.id and en.language_code = 'en'
  where t.focus_category->>'en' = 'Grammar' and t.level in ('A1','A2','B1','B2') and t.title->>'en' <> 'Random'
    and coalesce(en.full_sentence, '') <> ''),
gf as (select concept_id,
         case when bool_and(level like 'A%') then 'A' when bool_and(level like 'B%') then 'B' end glev
       from ge group by 1),
-- concept level: no column exists; = level of the concept's vocabulary exercises (types 27/74/76 = A, 68/69/75/77 = B);
-- if it has both, the family of its grammar exercises; if still ambiguous, A (lower level)
cl as (select w.id concept_id, coalesce(vl.vlev, gf.glev, 'A') clevel,
         case when vl.vlev is not null then 'vocab' when gf.glev is not null then 'grammar' else 'tie_A' end level_source
       from word_concepts w left join vl on vl.concept_id = w.id left join gf on gf.concept_id = w.id),
cc as (select cl.*, row_number() over (order by md5(concept_id::text || 'phase2b-concept'), concept_id) crk from cl),
rk as (select ge.*, cc.clevel, cc.level_source, cc.crk,
         row_number() over (partition by ge.concept_id, ge.level
                            order by md5(ge.concept_id::text || ge.exercise_id::text || 'phase2b'), ge.exercise_id) r
       from ge join cc on cc.concept_id = ge.concept_id and cc.crk <= 3600 and left(ge.level, 1) = cc.clevel)
"""

# ---------------------------------------------------------------- exclusions (2B's scan + 2A rows + the 2B sample)
d2a = json.load(open(f"{TO}/phase2a/selection.json", encoding="utf-8"))
ex_2a_excl = set(d2a["excluded"]["test_sets"]) | set(d2a["excluded"]["trackB_120"])
ex_2a_sel = {r["exercise_id"] for r in d2a["rows"]}
ex_2b_sample = {r["exercise_id"] for r in json.load(open(f"{TO}/phase2b/sample_2b.json", encoding="utf-8"))["rows"]}
KEY = re.compile(r"^(exercise_?id|ex_?id|eid)$", re.I)
scan = set(); scanned = 0
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if KEY.match(str(k)):
                if isinstance(v, int): scan.add(v)
                elif isinstance(v, str) and v.isdigit(): scan.add(int(v))
                elif isinstance(v, list): scan.update(int(x) for x in v if isinstance(x, int) or (isinstance(x, str) and x.isdigit()))
            walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
roots = sorted(glob.glob(f"{TO}/phase1*")) + [f"{TO}/pilot", f"{TO}/measurements"]
for root in roots:
    for fp in glob.glob(f"{root}/**/*", recursive=True):
        if not os.path.isfile(fp): continue
        b = os.path.basename(fp)
        if re.fullmatch(r"\d+\.json", b): scan.add(int(b[:-5]))
        if fp.endswith(".json"):
            try: walk(json.load(open(fp, encoding="utf-8"))); scanned += 1
            except Exception: pass
excl = ex_2a_excl | ex_2a_sel | scan | ex_2b_sample
EXVALS = ",".join(f"({i})" for i in sorted(excl))

FINAL = """, ex(exercise_id) as (values """ + EXVALS + """),
rk2 as (select rk.*, row_number() over (partition by rk.concept_id, rk.level
                                        order by md5(rk.concept_id::text || rk.exercise_id::text || 'phase2b'), rk.exercise_id) r2
        from rk where rk.exercise_id not in (select exercise_id from ex))
select rk2.concept_id, rk2.crk, rk2.clevel, rk2.level_source, rk2.exercise_id, rk2.level, rk2.exercise_type_id, rk2.r, rk2.r2,
  t.title->>'en' type_title, t.level type_level, w.word headword,
  en.full_sentence en, en.correct_answer ca_en, sk.full_sentence sk, sk.correct_answer ca_sk,
  cz.full_sentence cz, cz.correct_answer ca_cz
from rk2 join exercise_types t on t.id = rk2.exercise_type_id join word_concepts w on w.id = rk2.concept_id
join exercise_localizations en on en.exercise_id = rk2.exercise_id and en.language_code = 'en'
left join exercise_localizations sk on sk.exercise_id = rk2.exercise_id and sk.language_code = 'sk'
left join exercise_localizations cz on cz.exercise_id = rk2.exercise_id and cz.language_code = 'cz'
where rk2.r2 = 1
order by rk2.crk, rk2.level"""
SQL = (f"-- Phase 2C selection (read-only). 2B's rule verbatim + exclusion of {len(excl)} ids\n"
       "-- (2A test sets + 2A trackB_120 + 2A's 1,000 selected rows + a fresh phase1*/pilot/measurements scan + 2B's 200-row sample).\n"
       "-- Within a (concept, level) the lowest-md5 NON-EXCLUDED candidate wins (r = original 2B rank, r2 = rank after exclusion).\n"
       "-- Czech language_code is 'cz'. Sentences live in exercise_localizations (no sentence_translations table live).\n"
       + CTE + FINAL + ";\n")
open(f"{H}/selection_2c.sql", "w").write(SQL)

sel = q(CTE + FINAL)
miss = q(CTE + """select w.id concept_id, w.word from word_concepts w
where not exists (select 1 from ge where ge.concept_id = w.id) order by w.id""")
tot = q("select count(*) n from word_concepts")[0]["n"]

# ---------------------------------------------------------------- compare with 2B's slot list (every (concept, level) partition)
slots_2b = {}
for ln in open(f"{TO}/phase2b/selection_2b_ids.tsv", encoding="utf-8").read().splitlines()[1:]:
    c, cl, e, lv, ty = ln.split("\t"); slots_2b[(int(c), lv)] = int(e)
got = {(r["concept_id"], r["level"]): r for r in sel}
dropped = sorted(k for k in slots_2b if k not in got)
repicked = sorted(k for k in got if k in slots_2b and got[k]["exercise_id"] != slots_2b[k])
new_slots = sorted(k for k in got if k not in slots_2b)

nonempty = lambda s: bool((s or "").strip())
gaps = collections.Counter(); gap_rows = []
for r in sel:
    g = [f for f, v in (("sk", r["sk"]), ("cz", r["cz"]), ("en", r["en"]), ("ca_en", r["ca_en"]),
                        ("ca_sk", r["ca_sk"]), ("ca_cz", r["ca_cz"]), ("type_title", r["type_title"]),
                        ("type_level", r["type_level"]), ("headword", r["headword"])) if not nonempty(v)]
    for f in g: gaps[f] += 1
    if g: gap_rows.append({"exercise_id": r["exercise_id"], "concept_id": r["concept_id"], "level": r["level"], "missing": g})
    r["_gaps"] = g

# ---------------------------------------------------------------- jsonl: one row per exercise x language
n = 0; per = collections.Counter()
with open(f"{H}/selection_2c.jsonl", "w", encoding="utf-8") as f:
    for lang in ("sk", "cz"):
        for r in sorted(sel, key=lambda r: (r["crk"], r["level"])):
            n += 1; per[f"{lang}_{r['level']}"] += 1; per[lang] += 1
            src = r[lang]
            if nonempty(src): per[f"{lang}_runnable"] += 1
            f.write(json.dumps({
                "n": n, "lang": lang, "exercise_id": r["exercise_id"], "concept_id": r["concept_id"],
                "concept_rank": r["crk"], "concept_level": r["clevel"], "concept_level_source": r["level_source"],
                "level": r["level"], "exercise_type_id": r["exercise_type_id"], "type_title": r["type_title"],
                "type_level": r["type_level"], "headword": r["headword"], "src": src, "en": r["en"],
                "correct_answer_en": r["ca_en"], "correct_answer_sk": r["ca_sk"], "correct_answer_cz": r["ca_cz"],
                "md5_rank_original": r["r"], "repicked": r["r"] != 1, "src_missing": not nonempty(src),
                "field_gaps": r["_gaps"]}, ensure_ascii=False) + "\n")

with open(f"{H}/MISSING_CONCEPTS.txt", "w", encoding="utf-8") as f:
    f.write(f"# Phase 2C: concept ids with NO grammar-topic sentence (no row in the 2B `ge` CTE), one per line.\n"
            f"# {len(miss)} of {tot} concepts. No sentence exists for them and none was invented. 19 Sept 2026.\n")
    for m in miss: f.write(f"{m['concept_id']}\n")

by_c = collections.defaultdict(list)
for r in sel: by_c[r["concept_id"]].append(r)
summary = {
 "rule": "2B verbatim: concepts ranked by md5(concept_id||'phase2b-concept') (cut 3,600 = all concepts); A-concept -> one A1 + one A2, "
         "B-concept -> one B1 + one B2 grammar-topic exercise; within (concept, level) lowest md5(concept_id::text||exercise_id::text||'phase2b'), "
         "ties by exercise_id; excluded ids skipped, next-lowest taken; slot dropped if none remains",
 "sentence_table": "exercise_localizations", "czech_code": "cz",
 "exclusions": {"phase2a_test_sets_and_trackB": len(ex_2a_excl), "phase2a_selected": len(ex_2a_sel),
                "file_scan_ids": len(scan), "file_scan_json_files": scanned, "phase2b_sample": len(ex_2b_sample),
                "union": len(excl), "hit_the_2b_picks": len([k for k in slots_2b if slots_2b[k] in excl])},
 "concepts_total": tot, "concepts_with_a_selected_exercise": len(by_c),
 "concepts_2_sentences": sum(1 for v in by_c.values() if len(v) == 2),
 "concepts_1_sentence": sum(1 for v in by_c.values() if len(v) == 1),
 "concepts_0_sentences": tot - len(by_c), "concepts_without_any_grammar_sentence": len(miss),
 "selected_exercises": len(sel), "expected_2b": 4109, "delta_vs_2b": len(sel) - 4109,
 "rows_jsonl": n, "source_sentences": n,
 "per_level": dict(collections.Counter(r["level"] for r in sel)),
 "per_language_level": {k: v for k, v in sorted(per.items())},
 "slots": {"partitions_in_2b": len(slots_2b), "same_pick": len(slots_2b) - len(dropped) - len(repicked),
           "repicked_after_exclusion": len(repicked), "dropped_no_candidate_left": len(dropped),
           "dropped_slots": [{"concept_id": c, "level": l} for c, l in dropped],
           "new_slots_not_in_2b": [{"concept_id": c, "level": l} for c, l in new_slots]},
 "field_gaps": {"rows_with_any_gap": len(gap_rows), "by_field": dict(gaps), "rows": gap_rows[:200]},
 "both_sk_and_cz": sum(1 for r in sel if nonempty(r["sk"]) and nonempty(r["cz"])),
 "order": "language (sk, cz), then concept rank md5(concept_id||'phase2b-concept'), then level",
}
json.dump(summary, open(f"{H}/selection_2c_summary.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in summary.items() if k not in ("field_gaps", "slots")}, ensure_ascii=False))
print(json.dumps({"slots": {k: v for k, v in summary["slots"].items() if not isinstance(v, list)},
                  "field_gaps": summary["field_gaps"]["by_field"], "gap_rows": len(gap_rows)}, ensure_ascii=False))
