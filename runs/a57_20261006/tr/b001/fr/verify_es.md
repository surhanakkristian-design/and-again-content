# Verify fr -> es, batch b001

Texts checked: 1301 (100 videos: phrases, nouns, question, answer, recall rows; captions empty).

## Fixes
- 4243, phrases[1] + recall[1]: "hacer salchichas" -> "cocinar salchichas" (faire cuire = cook; "hacer salchichas" reads as manufacturing sausages)
- 365, answer: "Lleva unos auriculares grandes blancos." -> "Lleva unos grandes auriculares blancos." (natural adjective order)
- 365, recall[3]: "lleva unos auriculares grandes blancos" -> "lleva unos grandes auriculares blancos" (same)
- 57, phrases[0] + recall[0]: "subir los escalones la primera" -> "subir los escalones primero" (entry form has no subject; "la primera" imposed a feminine subject)
- 30, phrases[1] + recall[1]: "dormirse sobre el libro de texto" -> "dormir sobre el libro de texto" (dormir = sleep, not fall asleep)
- 358, question: "¿Dónde golpea el martillo?" -> "¿Qué golpea el martillo?" (matches "Sur quoi" and the answer "golpea un clavo")

## Doubts left unchanged
- 155 question "¿Qué está haciendo el hombre en la sartén?": adds "en la sartén" to make "faire cuire" clear; meaning kept.
- 38 "bastones naranjas": "naranja" invariable is also correct; plural accepted by RAE.
- 602 "un libro gordo": colloquial Spain usage for "un gros livre"; "grueso" would be more formal.
- 4055 "tener los ojos rojos": matches the French source although the clip shows a blue-eyed husky (source issue, not translation).
