# Listening question rules v2 (owner decisions 62 + 67, 23 Sept 2026)
For each video write English listening questions for learners (Gen Z, 15-25, A/B level): UP TO 3 per video IN TOTAL.
Inputs per item: `transcript` (raw), `spoken_sentences` (what is actually said), `what_is_seen` (the visual description),
`existing_questions` (questions already live for this video — they count towards the 3 and must NOT be repeated), `max_new`
(how many you may add: 3 minus the existing ones).

How many: write as many as the speech GENUINELY carries, never pad. A line like "Come on!" or "Thank you." carries none;
"I finished school. This is my degree!" carries one; a longer dialogue may carry two or three. Zero is fine (skip).

Every question MUST:
1. be answerable ONLY from what is SAID. A viewer with the sound OFF must NOT be able to answer it
   (use `what_is_seen`: if the answer is visible, e.g. the colour of a shirt, the object held up, the action performed,
   or it is guessable from the situation or world knowledge, pick another question or skip).
2. have ONE clear, short correct answer taken from the speech (a word, a number, a short phrase).
3. NOT contain or quote the answer, and not give it away by its wording.
4. be short (max ~12 words), natural, casual, Gen-Z friendly, simple English (A2-B1). Tone examples:
   "What does she say it costs?", "Where does he say they're going?", "What does he call his dog?", "How does she feel, according to her?"
5. never ask about sound effects, music, or who speaks; never ask "what is the first/last word".
6. avoid yes/no questions when possible.

Within ONE video (including `existing_questions`):
7. no two questions may ask the same thing: each must target a DIFFERENT piece of the speech, with a different answer,
   and no question may give away the answer of another one.

`correct_answer`: the canonical short answer as a learner would type it (e.g. "250 euros").
`accepted_answers`: 2-5 OTHER correct phrasings a learner might type (digits vs words, with/without unit or article,
common synonyms that mean exactly the same). Do not repeat correct_answer. No wrong or broader answers.

If a video has no fair NEW audio-only question, set "skip": true with a short "reason"
(e.g. "speech too thin", "answer visible", "only remaining fact already asked").

Output: a JSON array, one object per input item, same order:
{"media_id": 123, "questions": [{"question": "...", "correct_answer": "...", "accepted_answers": ["..",".."]}], "skip": false, "reason": null}
("questions" has 0..max_new entries; when skip is true it is [].)
