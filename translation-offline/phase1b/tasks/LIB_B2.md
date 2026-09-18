# Task: mistake library, topics 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 (Opus). Budget: at most ~20 tool calls.
Write one file per topic: `mistakes/<type_id>.json` in the FORMAT_SPEC §2 format, about 20 items per topic
(topic names/levels: selection/topics.json).
Source material: the reviewed Phase 1 per-sentence mistakes. Dump them compactly with ONE python command per few topics:
for `../pilot/generated/*.json` with that type_id print kind | verdict | text | feedback_sk (do not open files one by one).
Feedback rules: ../GENERATION_SPEC.md "feedback" rules (lines ~100–130) — only what is wrong, no praise, English tense
names (never "příčestí"/"príčastie": say "past participle"), gender-neutral Slovak/Czech (no "urobil si"/"napsala jsi"
addressed to the learner), never the whole reference, ≤150 characters AFTER filling slots with realistic long values.
Items: generalise the Phase 1 mistakes into reusable patterns and add the typical ones they miss (wrong tense/form, missing
auxiliary, wrong participle, word order, wrong preposition/article typical for SK/CZ learners, the practised structure
avoided → `correct_with_tip`, e.g. "is able to" for CAN, locative inversion for THERE IS). Keep Phase 1's reviewed verdict
boundaries. Prefer only {right}/{wrong} slots; extra slots only when necessary. `pattern` = one short line telling an
annotator what wrong text to produce. Check the 150-char limit with a short script before finishing.
Then run `python3 scripts/make_indexes.py`. Final message: topics written, items per topic, problems.
