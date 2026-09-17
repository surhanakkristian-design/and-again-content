# Offline translation check – generation spec (pilot, Phase 1)

The app shows a learner (native Slovak or Czech, or another language) a sentence in their
native language; the learner types the English translation. There is **no AI at runtime**.
The phone decides the verdict from data you write now:

1. the answer matches the English reference or one of your **acceptable translations** → `correct`
2. it matches one of your **typical mistakes** → that mistake's verdict and prepared feedback
3. exactly one word has a one-letter typo → `correct_with_tip` (automatic)
4. anything else → `wrong` with an automatic word-by-word tip

Matching already ignores case, punctuation, apostrophe styles, diacritics, English
contractions (don't ↔ do not, she's ↔ she is/has, I'd ↔ I would/had) and numbers 0–100
as digits or words. **Never list variants that differ only in those.**

Every exercise practises one grammar topic (`topic`) at one CEFR level (`level`); `en_answer`
is the part of the reference that carries the practised grammar.

## Output: one JSON file per exercise

```json
{
  "exercise_id": 20435,
  "type_id": 1,
  "topic": "TO BE",
  "level": "A1",
  "reference": "The big plate is white and very clean.",
  "sk": "Ten veľký tanier je biely a úplne čistý.",
  "cz": "Ten velký talíř je bílý a úplně čistý.",
  "acceptable": [
    "The {big|large} plate is white and {very|completely|totally|really|perfectly} clean."
  ],
  "mistakes": [
    {
      "text": "The {big|large} plate white and {very|completely} clean.",
      "kind": "missing to be",
      "verdict": "wrong",
      "feedback_sk": "Chýba sloveso „is“: „The plate is white…“.",
      "feedback_cz": "Chybí sloveso „is“: „The plate is white…“.",
      "feedback_en": null
    }
  ],
  "source_issues": []
}
```

Copy `exercise_id`, `type_id`, `topic`, `level`, `reference` (= `en`), `sk`, `cz` from the input
unchanged.

### Slot syntax `{a|b|c}`

Inside `acceptable` and `mistakes[].text` you may write alternatives in braces. Every
combination of all slots is expanded (an empty option `{really |}` means "leave out").
Spaces are collapsed after expansion. No nesting. Use slots only for **independent** choices:
every single combination must be a natural, correct sentence (for `acceptable`) or must
contain exactly the described mistake (for `mistakes`). If two choices depend on each other,
write separate lines instead. Keep the product of one line at or below 96 combinations.

## acceptable – what goes in

Every natural, grammatically correct English translation that a learner could plausibly type
and that has **the same meaning as BOTH the Slovak and the Czech sentence** and **uses the
practised grammar**:

- synonyms a learner would really use (big/large, pick up/lift, film/movie, flat/apartment),
  British and American words and spellings (colour/color, flatmate/roommate, grey/gray),
- other natural word orders (adverb positions: "Yesterday she bought…" / "She bought … yesterday"),
- small optional words the native sentence implies or allows (just, still, already, really, now),
  article or determiner choices that keep the meaning (the/this when the native "ten/tá"
  points at something), possessive vs. article where both are natural,
- the reference wording itself is always accepted – do not repeat it.

What does NOT go in:
- unnatural, rare, bookish or regional-only phrasing; literal calques;
- a different meaning or tense meaning (after "By the end of…" only the Future Perfect);
- a correct sentence that avoids the practised grammar ("He is able to find her" in a CAN
  exercise, active voice in a Passive exercise, Past Simple in a Present Perfect exercise when
  English allows both) → that is a `correct_with_tip` **mistake**, not acceptable;
- variants that differ only in case, punctuation, contractions or digits.

Be generous with real synonyms – a correct answer that is rejected is the main risk of this
design – but every line must be something a careful native teacher marks fully correct.

Where the Slovak and Czech sentences differ from each other or from the English reference
(an extra word, a different detail), accept translations that fit the native sentences as
well as the reference, and write one short English line into `source_issues`.

## mistakes – 3 to 6 per exercise

Typical mistakes a Slovak or Czech learner at this level would **really** make for **this**
sentence, focused on the practised grammar first (then common L1 transfer errors: missing
articles, calqued word order, wrong preposition, tense of the native verb, double negation,
"will" after if/when, 3rd person -s, more + short adjective, gerund/infinitive, question word
order in reported questions, avoiding the structure).

- `text`: the whole sentence as the learner would type it – otherwise correct, containing only
  this mistake. Slots are allowed. It must never match an acceptable translation.
- `kind`: 2–6 English words describing the mistake.
- `verdict`:
  - `wrong` – ungrammatical, or the meaning changes (other tense meaning, other word, missing
    part), or the practised grammar is used incorrectly;
  - `correct_with_tip` – grammatically correct AND the same meaning, but it avoids the
    practised grammar, or a clearly more natural wording exists.
- `feedback_sk`, `feedback_cz`: always. `feedback_en`: only for B1 and B2, `null` for A1/A2.

### Feedback rules (all mandatory)

1. Only what is wrong or could be better. Never praise or describe the correct parts
   ("Veta je správna, ale…" is forbidden).
2. Names of tenses and structures ALWAYS in English: Present Simple, Past Continuous,
   Future Perfect, Passive, Reported speech, Gerund, Infinitive, First Conditional… Never
   "prítomný čas", "trpný rod", "činný rod", "budúci čas", "předpřítomný čas".
3. Gender-neutral: never a past-tense form addressed to the learner ("použil si", "použila si",
   "napísal si", "použil jsi", "zapomněla jsi"). Write impersonally ("patrí tu", "chýba",
   "treba", "je potřeba", "sem patří") or in the imperative/present ("použi", "pozor na").
4. Never repeat the whole reference sentence. Quote only the words that matter, in „…“
   for Slovak and Czech and “…” for English.
5. At most 150 characters per feedback (count them).
6. A1/A2: very simple words, one short sentence, no grammar jargon beyond the tense/structure
   name (no "3. osoba jednotného čísla", "jednoslabičné prídavné mená", "modálne sloveso").
   B1/B2: say briefly WHY the form is needed ("po „if“ patrí Present Simple").
7. Slovak must be correct Slovak, Czech must be correct Czech (no Slovak forms in Czech, no
   Czech forms in Slovak). English feedback is plain, learner-friendly English.
8. The feedback must fit every expansion of the `text` slots.

## Hard constraints for this job

- Read ONLY the batch input file you are given and this spec. Do not open any other file in
  either repository (in particular nothing under `scripts/translation-bench/`, nothing under
  `pilot/generated/` except the files you write, nothing under `measurements/`).
- Never call any external model API. Do not use the network.
- Write exactly one file per exercise: `pilot/generated/<exercise_id>.json` (UTF-8, pretty
  printed, valid JSON). Do not touch other files.
