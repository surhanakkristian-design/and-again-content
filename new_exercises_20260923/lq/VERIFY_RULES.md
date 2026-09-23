# Listening question verification
You are an independent verifier. For each item you get the video's `transcript`, `spoken_sentences`, `what_is_seen`
and a proposed `question`, `correct_answer`, `accepted_answers`. Read GEN_RULES.md for the standard.

Check each proposal:
A. audio_only: can it be answered from the audio alone, and NOT from the picture alone (use what_is_seen)?
B. answer_correct: is correct_answer exactly what the speech says / means?
C. variants_correct: is every accepted_answer a correct equivalent (not wrong, not broader, not a different thing)?
D. form: short, natural, Gen-Z friendly, does not quote/give away the answer, not about sound effects.

verdict = "AGREE" only if A-D all pass. Otherwise "REJECT" with a short reason naming the failed check.
If ONLY some accepted_answers are wrong, you may still AGREE but list them in "drop_variants" (they will be removed;
at least 2 must remain, otherwise REJECT).

Output JSON array, same order: {"media_id": 123, "verdict": "AGREE"|"REJECT", "reason": "...", "drop_variants": []}
