# Verify b001 de -> fr

Texts checked: 1305 (100 videos: phrases, nouns, question, answer, recall). tr_check57: ok, 100 ids.

## Fixes (7 changes, 12 fields)
- 82, phrases[2] + recall[2]: "ramper dans la ruche" -> "se glisser dans la ruche" (in den Bienenstock = motion into the hive; "ramper dans" reads as crawling around inside)
- 4941, phrases[0] + recall[0]: "monter à une échelle" -> "grimper à une échelle" (hochklettern = climb, grimper is the natural verb)
- 819, phrases[1] + recall[1]: "venir sous le parapluie" -> "se mettre sous le parapluie" (natural French for getting under an umbrella)
- 741, phrases[0] + recall[0]: "se plier sous le vent" -> "se courber sous le vent" (a tree bends = se courbe; se plier = to fold)
- 741, answer: "Il se plie sous la tempête." -> "Il se courbe dans la tempête." (same verb as the phrase; im Sturm)
- 741, recall[3]: "se plie sous la tempête" -> "se courbe dans la tempête" (matches the answer)
- 5660, phrases[1] + recall[1]: "éclairer le mur de la maison" -> "éclairer la façade" (Hauswand of an apartment building = la façade)

## Doubts left unchanged
- 4941 answer "Elle sauve un chat perché dans l'arbre." ("aus dem Baum"): "perché" adds a nuance but reads naturally; literal "sauve un chat de l'arbre" is less idiomatic.
- 7853 "Le vase grandit vite en hauteur." slightly redundant but faithful to "wächst schnell in die Höhe".
- 852 "apporter des assiettes de nourriture" vs answer "apporte les plats" (Essen rendered two ways); both correct in context, phrase is a different text from the answer.
- 4788 "De quoi les femmes ont-elles l'air ?" is correct, slightly colloquial; kept.
