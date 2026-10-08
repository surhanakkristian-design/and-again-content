# A67 translations: the new exercise-4 row of each lab item (8 app languages)

RUN = ~/Projects/and-again-content/runs/a67_20261008/. Input tr67_source.json: `rows` = the 8 new English rows (one per
item id, the caption of a carousel picture, e.g. "to land a balloon", "people bowing to the king"); `existing_rows_for_style`
= how the item's other rows are already translated (follow their style: infinitive phrases stay infinitives, a full
sentence stays a full sentence with its tense, noun phrases stay noun phrases, natural everyday words; 7071 Turkish keeps
"ATV" for the quad bike, others use their usual word).
Languages: de, fr, es, sk, cz, ua, tr, hu. Each translation is shown in small grey type under the English row so the learner
understands it: natural, short, the same meaning, no explanations.
Write tr/tr67_writer.json: {"<id>": {"de": "...", "fr": "...", ...}}. Reply with one line.
