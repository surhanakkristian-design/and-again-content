You write extra English reference translations for Slovak sentences.
Read the file enrich_input.json in the current directory. It is a JSON list of objects {sid, sk, refs}:
sk = a Slovak sentence, refs = the English rendering(s) already accepted for it (the first is the main one).
For EVERY object, write exactly (3 - number of refs) NEW English renderings (none if it already has 3 or more), so that each sentence ends with 3.
Each new rendering must be a complete, natural, faithful English translation of the Slovak: same meaning, same persons and subjects, same number, same definiteness where Slovak makes it clear,
same time frame and tense as the main reference (present stays present, past stays past, future stays future), same voice where it matters; vary only wording, word order, synonyms, contractions or legitimately alternative constructions.
Never add or drop content. Never repeat an existing ref. Keep interjections/second sentences if the Slovak has them.
Write the result with the Write tool to enrich_output.json in the current directory as ONE JSON object mapping the sid (as a string) to a list of the new English strings, e.g. {"220001": ["...", "..."], ...}. Include every sid, even with an empty list.
No other files, no commentary; the file must parse as JSON.