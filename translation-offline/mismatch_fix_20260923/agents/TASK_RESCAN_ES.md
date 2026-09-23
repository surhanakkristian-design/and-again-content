# Task: scan Spanish rows for a wrong subject pronoun (read-only, no database)

Context: in the And Again app a Spanish speaker READS the Spanish sentence and must translate it into English; the
English sentence is the reference. On 22 Sept an automatic rewrite added an explicit subject pronoun to these Spanish
rows, and in many rows it picked the wrong person or gender (en "she" vs es «él», en "He wishes he had…" vs es
«Ojalá yo hubiera…»). Those were fixed today. Your job: find ANY row where a defect of this kind still exists.

Input: blocks `### <exercise_id>` with `en:` and `es:` (full sentence + [gap: …]).
Flag a row only when a Spanish SUBJECT (pronoun, or the person of the verb) has a different person, number or gender
than the English subject it corresponds to (él vs she, ella vs he, ellos vs she, yo vs he, tú vs he, nosotros vs they,
ellas vs they-for-a-mixed/male group when the English makes it clear, …). Also flag an explicit pronoun that refers to
the wrong entity (e.g. «él» for "the drone" is fine only if the Spanish noun is masculine and it is clearly the drone;
flag when it turns a thing/animal into a person or changes who acts). English "they" for one person of unknown gender,
or a group: ellos/ellas are both acceptable unless the English makes the gender clear. "It" for an animal: él/ella by
the Spanish noun's gender is fine. Do NOT flag anything else (wording, tense, vocabulary, articles) — pronouns only.
When unsure, do not flag.

Write `<OUT>` as TSV: header `exercise_id<TAB>en_subject<TAB>es_subject<TAB>proposed_fix`, one line per flagged row
(nothing else). No tabs inside fields. Do not modify any other file, no network, no database.
Reply with one line: `<n> rows scanned, <m> flagged`.
