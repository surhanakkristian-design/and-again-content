# b002 es -> en verification

Texts checked: 1308 (100 videos: phrases, nouns, question, answer, recall rows).

## Fixes
- 7239, phrases[2] + recall[2]: "to rub its head" -> "to rub his head" (frotarle la cabeza: the car-wash brush rubs the man's head, not the dog's)
- 5594, answer: "The magnificent dragon lands on the ridge." -> "The magnificent dragon is landing on the ridge." (question asks "What is the dragon doing?"; ongoing-action rule)
- 5594, recall[3]: "lands on the ridge" -> "is landing on the ridge" (same as the answer)
- 7835, recall[4]: "runs down the slope" -> "is running down the slope" (must match the answer "is running")
- 7835, phrases[0] + recall[0]: "to flow down the slope" -> "to run down the slope" (same verb for descender por la ladera everywhere in the video)
- 7453, question: "What does the cook do?" -> "What is the cook doing?" (answer is progressive "She is cooking"; tense must match)
- 7744, phrases[2] + recall[2]: "to stand open-mouthed" -> "to be left open-mouthed" (quedarse con la boca abierta; she is sitting in a kayak; same wording as 5117)
- 7154, question: "How does the businessman get around?" -> "How is the businessman getting about?" (se desplaza here is the ongoing ride in the clip, not a habit)
- 7154, answer + recall[3]: "He gets around on a unicycle(.)" -> "He is getting about on a unicycle(.)" (same reason)

## Doubts left unchanged
- Spanish simple-present questions with simple-present answers (e.g. 36, 7239, 8032, 7932, 7870, 2 others) kept as English narrative present ("What does the dog do? It stares..."): natural for describing a clip and consistent inside each video; only mismatched pairs were changed.
- 5594 "to land" for posarse (the clip shows the dragon perched): posarse covers both; kept.
- 5310 "to hug her son": su is ambiguous, the question names the woman.
- 7119 "yellow waterproofs" while the clip shows orange: faithful to the Spanish source (amarilla); a source issue, not a translation one.

tr_check57.py b002 es en: ok, 100 ids.
