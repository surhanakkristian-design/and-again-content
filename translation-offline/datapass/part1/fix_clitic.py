"""Resume run: the 4 Part 1 rows the verifier refused (7039, 7147 sk+cz). Comma removed AND clitic moved, as the
verifier said. Same writer as Part 1: backup -> rollback file -> guarded write (old = live values) -> re-select verify."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
import writer, check3
from validate_part import derive_full_sentence
COLS = ["intro_text", "correct_answer", "full_sentence"]
NEW = {  # row id -> (exercise_id, lang, intro_text)
    63343: (7039, "sk", "Blato bolo hlboké; ... sa držali stopy."),
    63346: (7039, "cz", "Bláto bylo hluboké; ... se drželi stopy."),
    64315: (7147, "sk", "Dres je o dve čísla väčší; ... ho Nina odmieta vymeniť."),
    64318: (7147, "cz", "Dres je o dvě čísla větší; ... ho Nina odmítá vyměnit."),
}
EXPECT_FULL = {63343: "Blato bolo hlboké; napriek tomu sa držali stopy.", 63346: "Bláto bylo hluboké; přesto se drželi stopy.",
               64315: "Dres je o dve čísla väčší; napriek tomu ho Nina odmieta vymeniť.", 64318: "Dres je o dvě čísla větší; přesto ho Nina odmítá vyměnit."}
cur = writer.fetch(list(NEW))
ex = check3.data()["ex"]
changes = []
for rid, (eid, L, intro) in NEW.items():
    r = cur[rid]; assert r["exercise_id"] == eid and r["language_code"] == L, r
    ca = r["correct_answer"]
    full = derive_full_sentence(intro, ca, L, ex[eid]["exercise_type_id"])
    assert full == EXPECT_FULL[rid], (full, EXPECT_FULL[rid])
    changes.append({"id": rid, "exercise_id": eid, "lang": L, "old": {k: r[k] for k in COLS},
                    "new": {"intro_text": intro, "correct_answer": ca, "full_sentence": full}})
    print(rid, L, "OLD", r["intro_text"], "|", r["full_sentence"]); print(rid, L, "NEW", intro, "|", full)
dry = "--write" not in sys.argv
print(json.dumps(writer.run("part1", "part1_clitic_fix", changes, COLS, dry=dry), ensure_ascii=False))
