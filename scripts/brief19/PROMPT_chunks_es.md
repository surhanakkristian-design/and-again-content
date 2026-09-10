You split SPANISH sentences into pieces for a "build the sentence" exercise. The learner
sees the pieces shuffled and must put them back in order. You return JSON only.

INPUT: a JSON array of items `{ "id", "sentence", "answer" }`. `answer` is the grammar
target that a previous exercise tested (e.g. "estaba sosteniendo", "habría", "una"); it
appears verbatim inside `sentence`.

OUTPUT: a JSON array, one object per input item, same order, same ids:
`{ "id": <id>, "chunks": ["piece", "piece", ...], "alternatives": [["piece", ...], ...] }`

Rules for `chunks` — every one of them is checked by a script; a violation rejects the row:

1. Joining the pieces with single spaces must reproduce the sentence EXACTLY: every
   character, accent (á é í ó ú ñ ü), capital, ¿ ¡ « » and punctuation mark. Never
   rewrite, drop, add or normalise anything.
2. 4 to 7 pieces. Four is the floor of that range, not the target. As a guide, longer
   sentences get more pieces: up to 9 words about 4; 10 to 13 words about 5; 14 to 17
   words about 6; 18 words or more SEVEN. PRECEDENCE: meaning beats the count, always. First cut the sentence
   at its natural phrase boundaries; then, if the count is above the guide, merge the
   two shortest neighbours; if it is below the guide, split only where another natural
   boundary exists. If the guide cannot be reached without breaking a phrase, do not
   reach it.
   THE FLOOR DEPENDS ON LENGTH: a sentence of up to 8 words may have THREE pieces when
   that is its natural split ("¿Cuántos pañuelos | hay | en el suelo?" is right; forcing a
   fourth piece by cutting "en el | suelo?" is wrong and rejected). From 9 words on, four
   is the floor. Never go below three. On a short sentence prefer a one-word verb,
   adverb or pronoun piece ("Ella | lee | toda la noche | los mismos tres libros.") over
   a cut inside a phrase, and prefer three whole phrases over four broken ones.
3. Keep phrases together. A noun with its article and adjectives ("la cúpula dorada",
   "un montón enorme"), a prepositional phrase ("en la mesita del café", "en el medio"),
   a fixed expression: each stays whole. Cut at phrase boundaries, never inside a phrase.
   An article, preposition or possessive is never left without its noun: "en la" |
   "mesita." is wrong, "en la mesita." is right.
   A PIECE NEVER ENDS ON A DETERMINER, on a preposition + determiner, or on a numeral
   whose noun starts the next piece ("en el" | "suelo?", "no una" | "ciudad nueva.",
   "esa" | "pausa corta?", "dos" | "plantitas", "con este" | "tiempo caluroso" are all
   rejected by the script), and a piece is never
   a bare article ("La" | "barbera.") or a bare preposition ("auf" | "dem Tablett.", "in" | "the kitchen.", "en" | "la mesa." are rejected too). The
   noun phrase is the unit, whatever the piece count. Spanish spreads meaning over many
   short function words (el, la, de, en, un): that is exactly where this rule bites.
   SPANISH SPECIFICS:
   - Clitic pronouns stay with their verb: "se lo dio", "me levanto", "no lo sé",
     "está lavándose" are never cut between pronoun and verb. "no" stays with the verb
     it negates ("no quiere", "no lo ha visto").
   - Verb periphrases (tener que, ir a, poder, deber, acabar de, estar + gerund, haber +
     participle) MAY be cut between the conjugated part and the infinitive, gerund or
     participle: "tiene que | salir", "va a | llover", "está | durmiendo", "acaba de |
     llegar", "ha estado | esperando". That cut is the Spanish counterpart of the German
     verb bracket and is exactly what the exercise should teach; PREFER it over an
     unbalanced split or a piece that holds half the sentence. The conjugated part keeps
     its clitics and "no" ("no lo puede | ver", "se tiene que | ir"). What is never cut is
     a piece that ends on a bare "a" or "de" alone: "va a" | "llover" is fine, "va" | "a
     llover" is not.
   - Opening marks glue to the first word of the clause: "¿Qué quieres?" is "¿Qué" |
     "quieres?" at most; never a piece that is only "¿" or "¡". A sentence that starts a
     question or exclamation mid-string ("Ya es tarde, ¿no crees?") keeps "¿no crees?"
     whole or cuts only before the "¿".
   - A subordinate clause keeps its conjunction or relative at the front of its first
     piece ("que no viste", "cuando llegue", "si tuviera"); the comma stays attached to
     the piece before it.
   - Two sentences in one string ("¿Qué bebe ella? Agua mineral fría.") are cut at the
     sentence boundary at least; each half then follows the same rules.
4. Punctuation stays attached to its word: "en el medio." not "en el medio" + ".".
   A comma, dash (—, -) or quotation mark ends or starts the piece it is glued to.
5. `answer` must never be split across two pieces. That is the ONLY rule about it: the
   answer does NOT need a piece of its own, and it normally SHARES its piece with the
   words around it ("deberías salir pronto", "la cúpula dorada", "se mueve ahora").
   A two-word answer like "va a" or "está comiendo" stays in one piece.
   An answer written with "..." ("no ... nada", "ni ... ni") has TWO parts that sit in
   two different places of the sentence: each part stays whole inside one piece, and
   the two parts normally land in different pieces.
6. Roughly even piece lengths, but meaning wins: aim for similar sizes and give that up
   the moment it would break a phrase.
7. No piece longer than about half the sentence (in words). If one piece held six of
   eleven words, the exercise would be solved the moment that piece is placed. If your
   split has a dominant piece, redo it with more, smaller pieces.
8. No two pieces of one sentence may be byte-identical (same letters, same case, same
   punctuation): two such chips are a coin flip. Pieces that differ by a capital or a
   full stop ("dijo ella." and "Ella dijo") are FINE: the capital opens the sentence and
   the period closes it, and noticing that is part of the exercise.
9. Pieces that could be swapped are ALLOWED. Do not merge pieces just to make one order
   the only possible one; that produces the dominant piece rule 7 forbids.

Rules for `alternatives` — other orders of the SAME pieces that are also correct Spanish:

10. Each alternative is a full ordering of exactly the same pieces (a permutation of
    `chunks`), different from `chunks`. Nothing rephrased, no piece changed.
11. The pieces are used exactly as cut, punctuation and capitals included. So a piece
    that carries the full stop can only stand last, a piece that starts with a capital
    letter or with ¿ ¡ can only stand first, and a piece that ends with ? or ! can only
    close its clause. Spanish word order is freer than English (adverbials and some
    subjects move), so a swap of two adverbial phrases is often valid; a swap that moves
    a clitic away from its verb or an adjective away from its noun never is.
12. Most sentences still have none: return `[]`. Include an alternative only when the
    resulting sentence is genuinely correct, natural Spanish. Do not list orders that
    merely parse.
13. At most two. If you can see three or more valid orders, your split is too loose:
    re-split so that fewer orders are valid (for example keep two swappable adverbials
    in one piece), but never at the price of rule 7.

Examples

Input:  { "id": 1, "sentence": "Mientras ella sostenía el tercer certificado ante la cámara, el primero se cayó del estante.", "answer": "sostenía" }
Output: { "id": 1, "chunks": ["Mientras ella sostenía", "el tercer certificado", "ante la cámara,", "el primero", "se cayó", "del estante."], "alternatives": [] }

Input:  { "id": 2, "sentence": "Si tuviera tantos certificados, los guardaría en una caja, no en los brazos.", "answer": "tuviera" }
Output: { "id": 2, "chunks": ["Si tuviera", "tantos certificados,", "los guardaría", "en una caja,", "no en los brazos."], "alternatives": [] }

Input:  { "id": 3, "sentence": "Cada mañana él revisa el buzón antes del desayuno.", "answer": "revisa" }
Output: { "id": 3, "chunks": ["Cada mañana", "él revisa", "el buzón", "antes del desayuno."], "alternatives": [] }
(No alternative: "Cada mañana" cannot move to the end without the full stop, and "antes del desayuno." can only stand last.)

Input:  { "id": 4, "sentence": "Corrí en el parque el lunes y ella se quedó en casa.", "answer": "Corrí" }
Output: { "id": 4, "chunks": ["Corrí", "en el parque", "el lunes", "y ella se quedó", "en casa."], "alternatives": [["Corrí", "el lunes", "en el parque", "y ella se quedó", "en casa."]] }

Input:  { "id": 5, "sentence": "¿Qué se pone ella en la piel? Crema y loción.", "answer": "Qué" }
Output: { "id": 5, "chunks": ["¿Qué se pone ella", "en la piel?", "Crema", "y loción."], "alternatives": [] }

Input:  { "id": 6, "sentence": "Hay un gallo en su jardín soleado.", "answer": "Hay" }
Output: { "id": 6, "chunks": ["Hay", "un gallo", "en su jardín soleado."], "alternatives": [] }
(Six words: three whole phrases. "en su" | "jardín soleado." is rejected.)

Input:  { "id": 7, "sentence": "El café está en la mesita del café.", "answer": "en" }
Output: { "id": 7, "chunks": ["El café", "está", "en la mesita del café."], "alternatives": [] }
(Seven words: three pieces; "en la mesita del café." is one prepositional phrase.)

Input:  { "id": 9, "sentence": "¿Quién lo afeita? La barbera.", "answer": "Quién" }
Output: { "id": 9, "chunks": ["¿Quién", "lo afeita?", "La barbera."], "alternatives": [] }
(Never "La" | "barbera.")

Input:  { "id": 8, "sentence": "No le dijo nada a su hermana sobre el regalo.", "answer": "No ... nada" }
Output: { "id": 8, "chunks": ["No le dijo", "nada", "a su hermana", "sobre el regalo."], "alternatives": [] }
(Two-part answer: "No" and "nada" each stay whole, in different pieces.)

Return ONLY the JSON array. No commentary, no markdown fences.
