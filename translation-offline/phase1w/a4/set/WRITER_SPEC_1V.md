# Phase 1V — fresh Slovak set, WRITER SPEC (adapted from 1U; only change: determiner-difference answers) (you are a blind writer)

Read ONLY this file. Do not open any other file or directory of this repo, do not look for earlier
sets, and never read another writer's output. You have Read and Write only. Your LEVEL (A1 / A2 /
B1 / B2) and your two output paths are in your task message.

You write test material for a checker of learner translations Slovak → English (the learner sees the
Slovak sentence and types English). You invent NEW Slovak sentences and, for each, 4 CORRECT and 5
WRONG English learner answers plus a small annotation. Natural, everyday, idiomatic Slovak with full
diacritics; natural learner-like English (British or American — be consistent inside one sentence).
Vary the topics widely (home, school, work, shopping, travel, weather, sport, food, neighbours,
transport, hobbies, health, money, pets, holidays…). No two sentences about the same event. Keep
everything level-appropriate: A1 ≤ 9 Slovak words and the simplest vocabulary; A2 ≤ 13; B1 ≤ 18;
B2 ≤ 22 words.

## The owner's rules (verbatim) — what CORRECT and WRONG mean
ACCEPTANCE RULE: "the reference point is the SLOVAK sentence, not the English reference. If the
learner's sentence is correct English on its own AND means what the Slovak means, it is ACCEPTED
with points, even if it avoids the practised structure entirely. Learners often do not know which
structure is being practised and must not be penalised for that. The practised structure becomes a
TIP, not a gate."

TENSE RULE: LEVEL 1, the TIME FRAME (past / present / future) must match the Slovak — a frame shift
is WRONG. LEVEL 2, the choice of English tense WITHIN that frame is FREE where the Slovak does not
fix it (Slovak past imperfective `On trénoval hodiny` admits "was training", "trained" and "had been
training" alike) — CORRECT.

OMISSION RULE: "M1, a dropped FUNCTION word or particle (just, already, optional "that") — CORRECT,
accepted, the missing word surfaced as a tip. M2, a dropped CONTENT word (noun, main verb,
meaning-carrying adjective or adverb) — WRONG. The app teaches translation, not gist. M3, ADDED
content — WRONG."
*(Changed from Phase 1T: "an article" has been REMOVED from M1's list of dropped function words. See
the owner's ruling below.)*

AGENT RULE: "A translation is judged only on whether it renders the whole Slovak sentence. An
English passive is CORRECT when it keeps the agent (e.g. 'is repaired by my father'), or when the
Slovak sentence itself names no agent. When the Slovak names an agent (a nominative subject doing
the action, including a pronoun or 'niekto') and the English answer drops it, the learner left out
half the translation: that is an omission and the answer is WRONG. Dropping any other content word
is WRONG too; dropping only a function word or particle is CORRECT." The agent rule applies to
EVERY clause of the sentence, embedded and coordinated clauses included.

## OWNER'S RULING ON ARTICLES (Phase 1U, still in force)

A missing obligatory article is an ERROR. An answer that lacks an article English grammar requires
("Dad will buy new fridge.", "It is cold in kitchen today.") is WRONG. M1 (a dropped function word
is correct, accepted with a tip) covers words like *just* and *already* — optional material. An
English article is a grammatical requirement of the target language, and Slovak has no article to
omit in the first place, so nothing was "dropped in translation": the sentence is simply not
grammatical English.

Clarification (orchestrator, not the owner's words): The CHOICE of determiner where more than one is
grammatical (a / the / a possessive / zero article where English allows it) stays free, as before;
only a MISSING OBLIGATORY article is an error.

Consequence for you: a `missing-article` answer is a WRONG answer of type S and must be written as
such. A correct answer may still vary the determiner freely.

## Error types for WRONG answers
T = time frame shifted (past / present / future differs from the Slovak) · W = wrong word (a lexical
substitution changing which thing, person, place, time or quantity) · M = meaning added or dropped
(a dropped agent is M) · S = small slip (missing obligatory article, preposition, agreement, word
form / spelling: wrong English or slightly changed meaning).

## Arm-B convention for the Slovak (mandatory)
Write an explicit subject personal pronoun (ja / ty / on / ona / my / vy / oni) wherever Slovak would
normally drop the subject. Sentences with a noun subject stay as they are. A genuinely impersonal,
subjectless, passive or reflexive-passive Slovak sentence gets NO added subject. This applies to
EVERY finite clause, embedded ones included ("On povedal, že ona opraví…").

## The build — 29 sentences, local ids s01–s29
(An assembler later keeps 25 of them per level — 8 FR + 6 MC + 6 MN + 5 SKP — and assigns the public
ids; you write 29 and never assign public ids.)

**s01–s09 — kind `FR` (fronted subordinate clause).** The Slovak sentence STARTS with a subordinate
clause introduced by a subordinator (vary them across the nine: keď, kým, keďže, pretože, hoci, ak,
len čo, aj keď, odkedy, zatiaľ čo, kedykoľvek). The subordinate clause's verb is an ACTIVE
TRANSITIVE verb and its overt NOMINATIVE AGENT stands right after the subordinator:
"Keď starosta otvorí nový most, …". The main clause that follows has its OWN subject, different
from the fronted agent. Example: "Keď starosta otvorí nový most, obyvatelia usporiadajú veľkú
oslavu."

**s10–s16 — kind `MC` (two clauses, agent clause NOT fronted).** Two clauses, each with its OWN
overt subject. Use main + relative clause (ktorý / ktorá / ktoré), main + že-clause (at least 3 of
your 7 MC sentences must be že-clauses), or two coordinated clauses (a / ale / a preto). The agent
clause — the clause whose agent the wrong answers will drop — has an active transitive verb with an
overt nominative agent and is NOT the first clause of the sentence. Example: "Riaditeľka oznámila,
že školník opraví strechu cez prázdniny."

**s17–s23 — kind `MN` (single main clause).** One main clause, an active transitive verb, an overt
nominative agent (noun, proper name or arm-B pronoun; at least 2 of the 7 with a pronoun agent).

**s24–s29 — kind `SKP` (the Slovak itself names no agent).** A true passive (bol postavený, je
zatvorené), a reflexive passive (Dom sa stavia už dva roky. Tu sa predáva chlieb.) or a
subjectless / impersonal sentence (Prší. Je tu zima. Treba to opraviť. Hovorí sa, že…). Mix the
three; prefer passive and reflexive passive. A 3rd-plural impersonal ("Včera nám ukradli bicykel")
is NOT allowed — it is ambiguous.

Time frames across your 29: about 40 % past, 35 % present, 25 % future.

## Determiner-difference answers (NEW in Phase 1V — mandatory)
OWNER'S RULE: the choice of English determiner is FREE where the Slovak has no demonstrative
(ten / tá / to / tí / tie / tento / táto / toto / títo / tieto / tamten …). Such an answer is CORRECT.
- Every FR, MC and MN sentence has its `c2` as a determiner difference (23 per writer). In addition,
  in at least 3 of your 6 SKP sentences `c4` is an skp-passive rendering that differs from another
  correct answer only by a determiner; tag it `["skp-passive", "determiner"]`.
- The Slovak noun phrase whose English determiner you vary must carry NO Slovak demonstrative, and
  NO possessive (môj, tvoj, jeho, náš …). Do not introduce this / that / these / those, and do not
  introduce a possessive: those add meaning. Only a / an / the / zero article.
- The varied answer must stay fully grammatical English and must still mean what the Slovak means;
  never drop an obligatory article to create the variant (that is a WRONG `missing-article` answer).
- Why: the new set must contain at least 60 determiner-difference answers the judge calls CORRECT.
  Aim for 26 per writer; a correct answer with `determiner` is never also given a wrong-answer tag.

## Answers — exactly 4 correct (c1–c4) and 5 wrong (w1–w5) per sentence, all DIFFERENT strings

### FR, MC and MN sentences
CORRECT:
- `c1` plain faithful translation.
- `c2` **in EVERY FR, MC and MN sentence: a DETERMINER DIFFERENCE and nothing else**, tag
  `determiner` (see "Determiner-difference answers" below). It is c1 with one English article
  changed where English grammar allows both (the <-> a, a <-> the, the <-> zero article with a plural
  or mass noun where both are natural). Everything else is identical to c1.
- `c3` **exactly one correct answer per sentence is a BY-PASSIVE that KEEPS the agent**, tag
  `by-passive`. In FR sentences passivise the FRONTED clause ("When the new bridge is opened by the
  mayor, the residents will hold a big celebration."); in MC sentences passivise the agent clause;
  in MN sentences the main clause.
- `c4` a faithful paraphrase (word order, synonym, contraction). Tag `plain` or `paraphrase`.
Never write an agent-dropping passive as a correct answer.

WRONG:
- `w1` and `w2` — **AGENT DROPS, type M**. A grammatical English rendering (agentless passive, or an
  equivalent construction that loses the agent) in which everything else — time frame, objects,
  place and time phrases, and the other clause in full — is faithfully kept, but the Slovak-named
  agent of the target clause is ABSENT, with no leftover pronoun or possessive referring to it
  anywhere in that clause. `w1` and `w2` must be built DIFFERENTLY from each other (e.g. be-passive
  vs get-passive, different within-frame tense, reduced relative, different clause order,
  nominalisation).
  - FR: both drop the agent of the FRONTED clause; the main clause keeps its own subject.
    Tag `drop-fronted`.
  - MC: both drop the agent of the agent clause while the OTHER clause's subject stays in the
    answer (passivised clause + the other clause, clauses reordered, etc.). Tag `drop-misaligned`.
  - MN: tag `drop-main`.
  - If an agent drop you wrote fits none of these three shapes, tag it `drop-other`.
  Use VARIED participles across your 29 sentences, deliberately including closed, rewritten, and
  re-/over-/un-prefixed irregulars (reopened, rewritten, overcharged, undone, unlocked, rebuilt,
  overheard, misread…), reduced relatives ("the letter written last week…"), and at least four
  answers that contain a LOCATIVE or INSTRUMENT by-phrase ("by the lake", "by email", "by bus",
  "by hand") but NO agent — these are agent drops all the same.
- `w3` — **time-frame shift, type T**, tag `time-frame`: the right words, the wrong time reference;
  not a within-frame tense change.
- `w4` — **slip, type S**. In at least 20 of your 23 FR/MC/MN sentences this slip is A MISSING
  OBLIGATORY ARTICLE AND NOTHING ELSE — one article that English grammar requires is simply absent,
  everything else perfect ("Dad will buy new fridge." / "She put keys on table."). Tag
  `missing-article`. Under the ruling above these answers are WRONG. In the remaining FR/MC/MN
  sentences `w4` is a DIFFERENT slip — subject–verb agreement, a wrong preposition, or a wrong word
  order — tag `agreement`, `preposition` or `word-order`.
- `w5` — **wrong word, type W**, tag `wrong-word`: a lexical substitution changing which thing,
  person, place, time or quantity.

### SKP sentences
CORRECT: at least 3 of the 4 render the Slovak passive / reflexive / subjectless structure faithfully
and agentlessly ("Bread is sold here." / "The house has been under construction for two years.");
tag those `skp-passive`. Everything in the Slovak must be rendered.
WRONG: `w1` and `w2` = type T, tag `time-frame` (two DIFFERENT frame shifts, or the same frame built
differently). `w3` = type S, a MISSING OBLIGATORY ARTICLE and nothing else, tag `missing-article`.
`w4` and `w5` = type W, tag `wrong-word`.

Each wrong answer must be wrong for EXACTLY ONE reason and otherwise perfect, and must be something a
real learner would plausibly type. A possessive must never smuggle the agent back in ("My bike was
sold" for *Ja som predal bicykel*) — in agent-drop items the agent must be absent altogether.

## Annotation per sentence
`"annotation": {"v": [two good English reference translations, the first = c1], "lk": [the finite
verb group of each v, e.g. "will bring"], "alt": {an English word or phrase in v[0]: [acceptable
alternatives], … 3–6 entries}, "voice_sk": "active_agent" | "passive" | "impersonal" (reflexive
passive = "passive"), "agent_nom": true|false (true iff the target agent clause has an explicit
nominative agent), "tf_gold": "past"|"present"|"future" (time frame of the MAIN clause),
"tense_open": true iff the Slovak does not fix the English tense inside the frame (e.g. past
imperfective), "perfective_present": true iff a Slovak perfective present form expresses the future
(príde, kúpi, opraví)}`

## Output — exactly two files, valid JSON, each a JSON LIST of sentence objects
- `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1w/a4/set/writers/writer_<LEVEL>_part1.json` — s01 … s15
- `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1w/a4/set/writers/writer_<LEVEL>_part2.json` — s16 … s29

Sentence object schema (every key mandatory; `null` where not applicable):

```json
{
  "lid": "s01",
  "level": "A2",
  "kind": "FR",
  "topic": "future after keď",
  "slovak": "Keď starosta otvorí nový most, obyvatelia usporiadajú veľkú oslavu.",
  "tags": {
    "agent_clause": "fronted",
    "agent": "starosta",
    "other_subject": "obyvatelia",
    "subordinator": "keď",
    "passivizable": true,
    "impersonal_or_passive": false
  },
  "annotation": {
    "v": ["When the mayor opens the new bridge, the residents will hold a big celebration.",
          "When the mayor opens the new bridge, the locals are going to hold a big celebration."],
    "lk": ["opens / will hold", "opens / are going to hold"],
    "alt": {"residents": ["locals", "people of the town"],
            "hold": ["throw", "organise"],
            "big celebration": ["large celebration", "big party"]},
    "voice_sk": "active_agent",
    "agent_nom": true,
    "tf_gold": "future",
    "tense_open": false,
    "perfective_present": true
  },
  "answers": [
    {"aid": "c1", "kind": "C", "intent": "plain faithful translation", "type": null,
     "tags": ["plain"],
     "answer": "When the mayor opens the new bridge, the residents will hold a big celebration."},
    {"aid": "c2", "kind": "C", "intent": "different determiner choice", "type": null,
     "tags": ["determiner"],
     "answer": "When the mayor opens a new bridge, the residents will hold a big celebration."},
    {"aid": "c3", "kind": "C", "intent": "by-passive keeping the agent of the fronted clause",
     "type": null, "tags": ["by-passive"],
     "answer": "When the new bridge is opened by the mayor, the residents will hold a big celebration."},
    {"aid": "c4", "kind": "C", "intent": "faithful paraphrase", "type": null, "tags": ["paraphrase"],
     "answer": "The residents will throw a big celebration when the mayor opens the new bridge."},
    {"aid": "w1", "kind": "W", "intent": "agent of the fronted clause dropped (be-passive)",
     "type": "M", "tags": ["drop-fronted"],
     "answer": "When the new bridge is opened, the residents will hold a big celebration."},
    {"aid": "w2", "kind": "W", "intent": "agent of the fronted clause dropped (get-passive, reordered)",
     "type": "M", "tags": ["drop-fronted"],
     "answer": "The residents will hold a big celebration once the new bridge gets reopened."},
    {"aid": "w3", "kind": "W", "intent": "time frame shifted to the past", "type": "T",
     "tags": ["time-frame"],
     "answer": "When the mayor opened the new bridge, the residents held a big celebration."},
    {"aid": "w4", "kind": "W", "intent": "missing obligatory article and nothing else", "type": "S",
     "tags": ["missing-article"],
     "answer": "When the mayor opens new bridge, the residents will hold a big celebration."},
    {"aid": "w5", "kind": "W", "intent": "wrong word: bridge -> tunnel", "type": "W",
     "tags": ["wrong-word"],
     "answer": "When the mayor opens the new tunnel, the residents will hold a big celebration."}
  ]
}
```

Field rules: `kind` of an answer is `"C"` or `"W"`. `type` is `null` on every correct answer and one
of `"T"`, `"W"`, `"M"`, `"S"` on every wrong answer. `intent` is a short human-readable reason
(≤ 12 words). `tags` is a non-empty list drawn from: `plain`, `determiner`, `aspect`, `paraphrase`,
`by-passive`, `skp-passive`, `drop-fronted`, `drop-misaligned`, `drop-main`, `drop-other`,
`time-frame`, `missing-article`, `agreement`, `preposition`, `word-order`, `wrong-word`. The exact
tag strings matter: the floor check counts them.

`tags.agent_clause` on the sentence is `"fronted"` (FR), `"misaligned"` (MC), `"main"` (MN) or
`null` (SKP). `tags.other_subject` is the other clause's subject as written in the Slovak, or null.

After writing the two files, re-read nothing. Finish with a message of ≤ 8 lines: counts of
FR / MC / MN / SKP sentences, of `drop-fronted` / `drop-misaligned` / `drop-main` / `drop-other`,
`time-frame`, `missing-article`, `by-passive`, `skp-passive` answers, how many of your FR/MC/MN
sentences have a `missing-article` w4, the count of `determiner` answers, and anything you could
not do.
