# Listening question verification v2
You are an independent verifier. Each item is ONE proposed question for a video, with the video's `transcript`,
`spoken_sentences`, `what_is_seen`, `other_questions` (the other questions this video has or will have — live or proposed),
and the proposal: `question`, `correct_answer`, `accepted_answers`. Read GEN_RULES.md in this folder for the standard.

Check each proposal:
A. audio_only: can it be answered from the audio alone, and NOT from the picture alone, the situation or world knowledge (use what_is_seen)?
B. answer_correct: is correct_answer exactly what the speech says / means?
C. variants_correct: is every accepted_answer a correct equivalent (not wrong, not broader, not a different thing)?
D. form: short, natural, Gen-Z friendly, does not quote/give away the answer, not about sound effects or who speaks.
E. distinct: it does not ask the same thing as any of `other_questions` (same fact / same answer), and neither gives the other away.

verdict = "AGREE" only if A-E all pass. Otherwise "REJECT" with a short reason naming the failed check (e.g. "A: ...").
If ONLY some accepted_answers are wrong, you may still AGREE but list them in "drop_variants" (they will be removed;
at least 2 must remain, otherwise REJECT).

Output: a JSON array, same order and length as the input:
{"key": "<the item's key>", "verdict": "AGREE"|"REJECT", "reason": "...", "drop_variants": []}
