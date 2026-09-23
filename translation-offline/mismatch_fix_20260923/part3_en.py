# Part 3: the two English rows that change (208, 22111). Builds work/p3_en_changes.json; checks gap + build invariants.
import json, fixlib
by = fixlib.load('before')
NEW = {
    208: {"intro_text": "Her hands are shaking on the clicker, so she ... as calm as she sounds.",
          "correct_answer": "can't be", "distractor_1": "mustn't be", "distractor_2": "shouldn't be",
          "chunks": ["Her hands are shaking", "on the clicker,", "so she", "can't be", "as calm", "as she sounds."],
          "correct_alternative": []},
    22111: {"intro_text": "He circles one date in ... schedule.",
            "correct_answer": "his", "distractor_1": "her", "distractor_2": "their",
            "chunks": ["He circles", "one date", "in his schedule."],
            "correct_alternative": []},
}
out = []
for eid, n in NEW.items():
    r = by[eid]['en']
    n = dict(n)
    n["full_sentence"] = fixlib.derive(n["intro_text"], n["correct_answer"], 'en', r['exercise_type_id'])
    chk = {**r, **n}
    errs = fixlib.check_row(chk)
    assert " ".join(n["chunks"]) == n["full_sentence"], (eid, n)          # E16: chunks join back to the sentence
    assert not errs, errs
    cols = ["intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence", "chunks", "correct_alternative"]
    out.append({"id": r["id"], "exercise_id": eid, "lang": "en", "key": f"P3-{eid}-en",
                "new": {k: n[k] for k in cols}, "old": {k: r[k] for k in cols},
                "reason": "English was the odd one out against all 8 natives (report 2.3); English rewritten to the natives"})
    print(eid, r['full_sentence'], '->', n['full_sentence'])
json.dump(out, open('work/p3_en_changes.json', 'w'), ensure_ascii=False, indent=1)
