"""Per-row md5 of every exercise_localizations row (all languages) + whole-table md5 of neighbouring tables.
Usage: rowhash.py <label>   -> snapshot/rowhash_<label>.json"""
import hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import db
label = sys.argv[1]
out = {"loc": {}, "tables": {}}
for L in ["sk", "en", "de", "cz", "fr", "es", "ua", "tr", "hu"]:
    r = db.rows(f"select id, md5(l::text) h from exercise_localizations l where language_code='{L}' order by id")
    out["loc"][L] = {str(x["id"]): x["h"] for x in r}
for t in ["exercises", "word_localizations", "translation_selected_exercises", "media", "word_concepts", "exercise_types"]:
    r = db.rows(f"select count(*) n, md5(coalesce(string_agg(md5(x::text), '' order by md5(x::text)),'')) h from {t} x")
    out["tables"][t] = r[0]
p = os.path.join(os.path.dirname(__file__), "..", "snapshot", f"rowhash_{label}.json")
json.dump(out, open(p, "w"))
print(label, {L: len(v) for L, v in out["loc"].items()}, out["tables"])
