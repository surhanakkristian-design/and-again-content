# Listening question rules (owner decision 62)
For each video write ONE English listening question for learners (Gen Z, 15-25, A/B level).
Inputs per item: `transcript` (raw), `spoken_sentences` (what is actually said), `what_is_seen` (the visual description).

The question MUST:
1. be answerable ONLY from what is SAID. A viewer with the sound OFF must NOT be able to answer it
   (use `what_is_seen` to check: if the answer is visible, e.g. the colour of a shirt or the object held up, pick another question).
2. have ONE clear, short correct answer taken from the speech (a word, a number, a short phrase).
3. NOT contain or quote the answer, and not give it away by its wording.
4. be short (max ~12 words), natural, casual, Gen-Z friendly, simple English (A2-B1). Examples of tone:
   "What does she say it costs?", "Where does he say they're going?", "What does he call his dog?", "How does she feel, according to her?"
5. never ask about sound effects, music, or who speaks; never ask "what is the first/last word".
6. avoid yes/no questions when possible.

`correct_answer`: the canonical short answer as a learner would type it (e.g. "250 euros").
`accepted_answers`: 2-5 OTHER correct phrasings a learner might type (digits vs words, with/without unit or article,
common synonyms that mean exactly the same). Do not repeat correct_answer. No wrong or broader answers.

If a video truly has no fair audio-only question (e.g. the only full sentence is visible on screen anyway, or the speech
is too thin), set "skip": true with a "reason".

Output JSON array, one object per input item, same order:
{"media_id": 123, "question": "...", "correct_answer": "...", "accepted_answers": ["..",".."], "skip": false, "reason": null}
