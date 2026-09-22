"""Part 4 inputs: the selected exercises that already have text in es/ua/tr/hu (fresh from the DB)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
import db
sel = [r["exercise_id"] for r in json.load(open(os.path.join(ROOT, "snapshot/sets.json")))["selected"]]
rows = []
for i in range(0, len(sel), 1500):
    rows += db.rows(f"""select id, exercise_id, language_code, intro_text, correct_answer, full_sentence from exercise_localizations
      where language_code in ('es','ua','tr','hu') and exercise_id in ({','.join(map(str, sel[i:i+1500]))})
      and coalesce(btrim(full_sentence),'')<>'' order by exercise_id""")
json.dump(rows, open(os.path.join(HERE, "rows_before.json"), "w"), ensure_ascii=False)
for L in ("es", "ua", "tr", "hu"):
    rs = [r for r in rows if r["language_code"] == L]
    h = (len(rs) + 1) // 2
    for k, part in enumerate((rs[:h], rs[h:]), 1):
        with open(os.path.join(HERE, f"in_{L}_{k}.txt"), "w") as f:
            for r in part:
                f.write(f"{r['exercise_id']}|{r['intro_text'] or ''}|{r['correct_answer'] or ''}|{r['full_sentence']}\n")
    print(L, len(rs))
