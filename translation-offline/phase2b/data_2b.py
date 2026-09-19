#!/usr/bin/env python3
"""Phase 2B DATA worker: selection rule (7,200 target), sample 200, relation to 39,498 / 5,895. DB read-only SELECTs
via the linked Supabase CLI (`db query --linked -o json`, run from ~/Projects/and-again). 0 Gemini calls."""
import json, os, re, glob, hashlib, subprocess, itertools, collections
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(H)
APP = os.path.expanduser("~/Projects/and-again")
SB = os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")
def q(sql):
    p = subprocess.run([SB, "db", "query", sql, "--linked", "-o", "json"], cwd=APP, capture_output=True, text=True)
    o = p.stdout
    if "{" not in o: raise SystemExit("query failed: " + (p.stderr or "")[-400:])
    return json.loads(o[o.find("{"):])["rows"]
md5 = lambda s: hashlib.md5(s.encode()).hexdigest()

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
rk as (select ge.*, cc.clevel, cc.level_source,
         row_number() over (partition by ge.concept_id, ge.level
                            order by md5(ge.concept_id::text || ge.exercise_id::text || 'phase2b'), ge.exercise_id) r
       from ge join cc on cc.concept_id = ge.concept_id and cc.crk <= 3600 and left(ge.level, 1) = cc.clevel)
"""
FINAL = """select rk.concept_id, rk.clevel, rk.level_source, rk.exercise_id, rk.level, rk.exercise_type_id,
  t.title->>'en' type_title, t.level type_level, w.word headword,
  en.full_sentence en, en.correct_answer ca_en, sk.full_sentence sk, sk.correct_answer ca_sk,
  cz.full_sentence cz, cz.correct_answer ca_cz
from rk join exercise_types t on t.id = rk.exercise_type_id join word_concepts w on w.id = rk.concept_id
join exercise_localizations en on en.exercise_id = rk.exercise_id and en.language_code = 'en'
left join exercise_localizations sk on sk.exercise_id = rk.exercise_id and sk.language_code = 'sk'
left join exercise_localizations cz on cz.exercise_id = rk.exercise_id and cz.language_code = 'cz'
where rk.r = 1
order by rk.concept_id, rk.level"""
open(f"{H}/selection_2b.sql", "w").write("-- Phase 2B selection rule (read-only). Czech language_code in the live DB is 'cz'.\n"
    "-- There is no sentence_translations table live: sentences live in exercise_localizations.\n" + CTE + FINAL + ";\n")

sel = q(CTE + FINAL)
stats = q(CTE + """select json_build_object(
 'concepts_total', (select count(*) from word_concepts),
 'concept_level', (select json_agg(x) from (select clevel, level_source, count(*) n from cl group by 1,2 order by 1,2) x),
 'concepts_with_grammar_by_clevel', (select json_agg(x) from (select cl.clevel, count(*) n from cl where cl.concept_id in (select concept_id from ge) group by 1) x),
 'grammar_topic_types_per_level', (select json_agg(x) from (select level, count(*) n from exercise_types where focus_category->>'en'='Grammar' and level in ('A1','A2','B1','B2') and title->>'en'<>'Random' group by 1 order by 1) x),
 'ge_total', (select count(*) from ge),
 'scope_2a_by_level', (select json_agg(x) from (select t.level, count(*) n from exercise_localizations sk join exercise_localizations en on en.exercise_id=sk.exercise_id and en.language_code='en' join exercises e on e.id=sk.exercise_id join exercise_types t on t.id=e.exercise_type_id where sk.language_code='sk' and t.level in ('A1','A2','B1','B2') and coalesce(sk.full_sentence,'')<>'' group by 1 order by 1) x),
 'probe', json_build_object(
   'exercises_total', (select count(*) from exercises),
   'vocab_exercises', (select count(*) from vt),
   'distinct_en_fs_grammar', (select count(distinct en.full_sentence) from ge join exercise_localizations en on en.exercise_id=ge.exercise_id and en.language_code='en'),
   'distinct_sk_fs_grammar', (select count(distinct sk.full_sentence) from ge join exercise_localizations sk on sk.exercise_id=ge.exercise_id and sk.language_code='sk'),
   'distinct_concept_type_grammar', (select count(*) from (select distinct concept_id, exercise_type_id from ge) x),
   'distinct_concept_level_grammar', (select count(*) from (select distinct concept_id, level from ge) x),
   'concepts_with_grammar', (select count(distinct concept_id) from ge),
   'grammar_video_concepts', (select count(*) from ge where concept_id in (select cm.concept_id from concept_media cm join media m on m.id=cm.media_id where m.media_type='video')),
   'grammar_image_concepts', (select count(*) from ge where concept_id in (select cm.concept_id from concept_media cm join media m on m.id=cm.media_id where m.media_type='image')),
   'media_total', (select count(*) from media), 'concept_media', (select count(*) from concept_media),
   'word_localizations', (select count(*) from word_localizations),
   'word_localizations_sk', (select count(*) from word_localizations where language_code='sk'),
   'grammar_en_ca_multiword', (select count(*) from ge join exercise_localizations en on en.exercise_id=ge.exercise_id and en.language_code='en' where en.correct_answer like '% %'),
   'grammar_sk_fs_ne_en_fs_len_lt_60', (select count(*) from ge join exercise_localizations en on en.exercise_id=ge.exercise_id and en.language_code='en' where length(en.full_sentence)<60),
   'grammar_prompt_version', (select json_object_agg(coalesce(pv,'null'), n) from (select e.prompt_version pv, count(*) n from ge join exercises e on e.id=ge.exercise_id group by 1) x),
   'per_type', (select json_object_agg(exercise_type_id, n) from (select exercise_type_id, count(*) n from ge group by 1) x),
   'per_level_grammar', (select json_object_agg(level, n) from (select level, count(*) n from ge group by 1) x),
   'per_level_concepts', (select json_object_agg(level, n) from (select level, count(distinct concept_id) n from ge group by 1) x)
 )) s""")[0]["s"]

# ---- selection summary
by_c = collections.defaultdict(list)
for r in sel: by_c[r["concept_id"]].append(r)
cl_counts = collections.Counter(); cl_src = collections.Counter()
for x in stats["concept_level"]: cl_counts[x["clevel"]] += x["n"]; cl_src[f"{x['clevel']}:{x['level_source']}"] += x["n"]
got = collections.Counter(len(v) for v in by_c.values())
per_clevel_got = {L: collections.Counter(len(v) for v in by_c.values() if v[0]["clevel"] == L) for L in "AB"}
n2 = got[2]; n1 = got[1]; n0 = stats["concepts_total"] - len(by_c)
topics = {}
ntypes = {x["level"]: x["n"] for x in stats["grammar_topic_types_per_level"]}
for L in ("A1", "A2", "B1", "B2"):
    c = collections.Counter(r["exercise_type_id"] for r in sel if r["level"] == L)
    topics[L] = {"selected": sum(c.values()), "distinct_topics_hit": len(c), "topics_available": ntypes.get(L),
                 "min_per_topic": min(c.values()) if c else 0, "max_per_topic": max(c.values()) if c else 0,
                 "per_topic": {str(k): v for k, v in sorted(c.items())}}
nonempty = lambda s: bool((s or "").strip())
scope_total = sum(x["n"] for x in stats["scope_2a_by_level"])
sel_in_scope = sum(1 for r in sel if nonempty(r["sk"]))
# 5,895 probe: every probe value + every sum of subsets of per-level counts (grammar & scope) + selection counts
cands = {}
def flat(pfx, v):
    if isinstance(v, dict):
        for k, w in v.items(): flat(f"{pfx}.{k}", w)
    elif isinstance(v, (int, float)): cands[pfx] = v
flat("probe", stats["probe"])
for nm, dct in (("grammar", stats["probe"]["per_level_grammar"]), ("grammar_concepts", stats["probe"]["per_level_concepts"])):
    for k in range(1, 5):
        for comb in itertools.combinations(sorted(dct), k): cands[f"{nm}[{'+'.join(comb)}]"] = sum(dct[c] for c in comb)
cands["selection_total"] = len(sel); cands["concepts_total"] = stats["concepts_total"]
for L in topics: cands[f"selection[{L}]"] = topics[L]["selected"]
pt = stats["probe"]["per_type"]
# any subset of topic types summing to 5,895 is trivially likely, so only report contiguous type-id runs
ids = sorted(pt, key=int)
for i in range(len(ids)):
    s = 0
    for j in range(i, len(ids)):
        s += pt[ids[j]]; cands[f"types[{ids[i]}..{ids[j]}]"] = s
exact = {k: v for k, v in cands.items() if v == 5895}
near = sorted(cands.items(), key=lambda kv: abs(kv[1] - 5895))[:8]
try:
    ph1 = subprocess.run(["grep", "-rn", "5,895\\|5895", f"{APP}/docs/features/reports", f"{APP}/docs/features/PROJECT_HANDOFF_CHAT.md"], capture_output=True, text=True).stdout.splitlines()[:6]
except Exception: ph1 = []
summary = {
    "rule": "3,600 concepts ranked by md5(concept_id||'phase2b-concept'); A-concept -> one A1 + one A2, B-concept -> one B1 + one B2 grammar-topic exercise; within (concept, level) lowest md5(concept_id::text||exercise_id::text||'phase2b'), ties by exercise_id",
    "sentence_table": "exercise_localizations (no sentence_translations table exists live)", "czech_code": "cz",
    "concept_level_source": "no level column on word_concepts; derived from vocabulary exercise level (A/B), else grammar family, else A",
    "concepts_total": stats["concepts_total"], "concepts_by_level": dict(cl_counts), "concepts_by_level_source": dict(cl_src),
    "concepts_with_grammar_by_clevel": {x["clevel"]: x["n"] for x in stats["concepts_with_grammar_by_clevel"]},
    "concepts_2_sentences": n2, "concepts_1_sentence": n1, "concepts_0_sentences": n0,
    "per_clevel_sentences": {L: dict(v) for L, v in per_clevel_got.items()},
    "selected_total": len(sel), "target": 7200, "shortfall": 7200 - len(sel),
    "topics_per_level": topics,
    "selected_with_sk_full_sentence": sum(nonempty(r["sk"]) for r in sel), "selected_with_cz_full_sentence": sum(nonempty(r["cz"]) for r in sel),
    "scope_39498_rerun": {"by_level": stats["scope_2a_by_level"], "total": scope_total, "selection_in_scope": sel_in_scope,
                           "selection_share_of_scope_pct": round(100 * sel_in_scope / scope_total, 2)},
    "probe_5895": {"exact_hits": exact, "nearest": near, "doc_mentions": ph1, "n_candidates": len(cands),
                    "verdict": "reproduced" if exact else "unreproducible from the live DB (no probed count equals 5,895)"},
    "probe_values": stats["probe"],
}
json.dump(summary, open(f"{H}/selection_2b_summary.json", "w"), ensure_ascii=False, indent=1)
with open(f"{H}/selection_2b_ids.tsv", "w") as f:
    f.write("concept_id\tconcept_level\texercise_id\texercise_level\texercise_type_id\n")
    for r in sel: f.write(f"{r['concept_id']}\t{r['clevel']}\t{r['exercise_id']}\t{r['level']}\t{r['exercise_type_id']}\n")

# ---- exclusions
d2a = json.load(open(f"{TO}/phase2a/selection.json"))
ex_2a_excl = set(d2a["excluded"]["test_sets"]) | set(d2a["excluded"]["trackB_120"])
ex_2a_sel = {r["exercise_id"] for r in d2a["rows"]}
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
            try: walk(json.load(open(fp))); scanned += 1
            except Exception: pass
excl = ex_2a_excl | ex_2a_sel | scan
pool = [r for r in sel if r["exercise_id"] not in excl]
sample = []; used = set()
for lang, lo in (("sk", 0), ("cz", 100)):
    k = lo
    for L in ("A1", "A2", "B1", "B2"):
        c = [r for r in pool if r["level"] == L and r["exercise_id"] not in used and nonempty(r[lang]) and nonempty(r["en"])]
        c.sort(key=lambda r: (md5(f"{r['exercise_id']}phase2b-sample-{lang}"), r["exercise_id"]))
        for r in c[:25]:
            k += 1; used.add(r["exercise_id"])
            sample.append({"n": k, "lang": lang, "exercise_id": r["exercise_id"], "concept_id": r["concept_id"], "concept_level": r["clevel"],
                "level": L, "exercise_type_id": r["exercise_type_id"], "type_title": r["type_title"], "type_level": r["type_level"],
                "type_missing": not (r["type_title"] and r["type_level"]), "src": r[lang], "en": r["en"],
                "correct_answer_en": r["ca_en"], "correct_answer_sk": r["ca_sk"], "correct_answer_cz": r["ca_cz"], "headword": r["headword"]})
sids = [s["exercise_id"] for s in sample]
out = {"seed": "md5(exercise_id::text||'phase2b-sample-sk') / '-cz', ties by exercise_id; cz drawn after sk, disjoint",
       "exclusions": {"phase2a_excluded_list": len(ex_2a_excl), "phase2a_selected": len(ex_2a_sel), "file_scan_ids": len(scan),
                      "file_scan_json_files": scanned, "union": len(excl), "selection_hit_by_exclusion": len(sel) - len(pool), "pool_after_exclusion": len(pool)},
       "overlap_check": {"with_exclusions": len(set(sids) & excl), "sk_cz_shared": len({s['exercise_id'] for s in sample if s['lang']=='sk'} & {s['exercise_id'] for s in sample if s['lang']=='cz'}),
                         "duplicates": len(sids) - len(set(sids))},
       "composition": {f"{l}_{L}": sum(1 for s in sample if s["lang"] == l and s["level"] == L) for l in ("sk", "cz") for L in ("A1", "A2", "B1", "B2")},
       "exercise_types_covered": len({s["exercise_type_id"] for s in sample}), "type_missing": sum(s["type_missing"] for s in sample),
       "rows": sample}
json.dump(out, open(f"{H}/sample_2b.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in summary.items() if k not in ("probe_values",)}, ensure_ascii=False)[:5000])
print(json.dumps({k: v for k, v in out.items() if k != "rows"}))
