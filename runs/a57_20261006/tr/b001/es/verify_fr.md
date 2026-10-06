# b001 es -> fr verification

Texts checked: 1305 (100 videos: phrases, nouns, question, answer, recall; captions empty). tr_check57.py: ok, 100 ids.

## Fixes (12 texts in 5 videos)
- 209 phrases[2] + recall[2]: "sentir la caméra" -> "renifler la caméra" (the cat sniffs the lens; "renifler" is the natural verb for an animal)
- 5456 phrases[2] + recall[2]: "porter l'uniforme" -> "porter un uniforme" (generic "llevar uniforme", indefinite article reads naturally)
- 5382 phrases[0] + recall[0]: "se disputer avec un jeune homme" -> "discuter avec un jeune homme" (the clip shows a friendly, laughing discussion; English "talk/discuss", not an argument)
- 5382 answer + recall[3]: "Elles se disputent à table(.)" -> "Elles discutent à table(.)" (same reason, same word inside the video)
- 741 phrases[0] + recall[0]: "se plier sous le vent" -> "se courber sous le vent" (a tree bending in the wind is "se courber")
- 741 answer + recall[3]: "(L'arbre) se plie sous la tempête" -> "(L'arbre) se courbe sous la tempête" (same verb inside the video)
- 4788 question: "Comment sont les femmes ?" -> "Comment se sentent les femmes ?" ("¿Cómo están?" asks about their state; "Comment sont" reads as a description of character)

## Doubts left unchanged
- 852 "porter un collier blanc": the source "llevar un collar blanco" means a necklace (English agrees), though the waiter wears a bow tie. Translation is faithful; the source sense may not match the clip.
- 4055 "avoir les yeux rouges": the husky has blue eyes per the description; faithful to the source, flagged only.
- 852 "Il apporte à manger à la table": natural French for "llevando comida a la mesa"; kept.
- 5007 "rentrer chez soi" for "entrar en casa": idiomatic, kept.
- 449 "porter les mains aux oreilles": correct, slightly literary; "mettre les mains sur les oreilles" would mean covering the ears, so kept.
