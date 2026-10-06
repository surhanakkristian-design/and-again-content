# Verify b001 de -> en

Texts checked: 1305 (100 videos: phrases, nouns, question, answer, recall). Checker: `tr_check57.py b001 de en` ok, 100 ids.

## Fixes (17)
- 646 phrases[1] + recall[1]: "to come out of the jar" -> "to come out of the glass" (Glas = glass; the clip shows a beaker, not a jar)
- 646 phrases[2] + recall[2]: "to open the mouth wide" -> "to open one's mouth wide" (natural English entry form, as "to brush one's teeth" elsewhere)
- 5616 phrases[0] + recall[0]: "to raise the arms" -> "to raise one's arms" (same reason)
- 5456 phrases[1] + recall[1]: "to go through the check" -> "to go through the checkpoint" ("the check" is not idiomatic for die Kontrolle)
- 5382 phrases[0] + recall[0]: "to argue with a young man" -> "to have a discussion with a young man" (diskutieren = discuss; "argue" suggests a quarrel)
- 5382 answer + recall[3]: "...sitting at the table and arguing" -> "...sitting at the table and having a discussion" (same word as the phrase)
- 721 question, answer, recall[3]: "What falls over / A glass falls over / falls over" -> "What is falling over / A glass is falling over / is falling over" (happening now: progressive, as the rest of the set)
- 4658 answer + recall[3]: "driving along the sea" -> "driving along by the sea" ("along the sea" is unnatural)

## Doubts left unchanged
- 121: "What has the man let burn? / He has let a pancake burn." Faithful to the German Perfekt and grammatical, though a native might say "What did the man let burn?"
- 5660 noun "the block of houses" for der Häuserblock: acceptable; "the block" alone would be ambiguous.
- 4243 / 4055 / 7999: animals referred to as "it", per English grammatical gender, although the animals are anthropomorphic.
- 10: target "die Frau" while the clip context says a male botanist (source issue, not translation).
