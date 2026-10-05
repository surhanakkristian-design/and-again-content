# A49 carousel pictures - rules written into every edit prompt up front

Model: Nano Banana Pro (`nano_banana_pro`), edit of the video's still (`--image <still>`), 9:16, 2K, 2 credits per job.
Budget: the 56 credits left of A48's 100 (balance 9056 on 5 Oct 2026 = floor 9000). At most 2 paid attempts per picture;
a word starts only when the credits left cover all its planned edits once plus one spare edit.

## Why A48's edits failed (DETAILS.md, report open points 6-7, ledger) -> rule
| A48 failure | rule in every prompt |
|---|---|
| grille emblem / oval badge copied from the source still | R1: name every logo, badge, emblem, sticker, label, decal, lettering visible in THIS still and say it is removed and replaced by plain material of the same colour |
| hood mark and a warning sticker on the quad survived several edits | R1 again, per location ("the front grille", "the rear fender") - not a generic "no logos" line only |
| clean-up edits re-rendered other details (the duke's tunic changed) and one re-render kept the sticker | R2: never plan a separate clean-up edit; one edit does the change AND the removal; a tiny leftover is removed by a local pixel retouch (free) |
| a duchess resembling a real royal | R3: every added person is fictional and described by concrete, ordinary features (age, hair, face shape, clothes); "not resembling any real person, royal, celebrity or public figure"; no famous costumes or signature looks |
| framing / camera distance changed | R4: "keep the exact framing, camera position, lens and angle of the source; the main subject keeps the same size and place in the frame" - only a prompt that needs room says how much the camera may step back |
| eyelines wrong (people looking at nothing / at the camera) | R5: state where EVERY person and animal looks (at whom/what) |
| bad hands in early rounds | R6: "correct hands with five fingers, each hand holding only what is named; correct arms, legs, paws, wings; no extra limbs" |
| blind test hesitated (bow vs serve; tourists too small) | R7: the caption's cue is LARGE in the frame (foreground, at least about a quarter of the picture), readable at thumbnail size, and it must exclude the sibling captions (the prompt names what must NOT be there) |
| photoreal look on a drawing / AI-plastic look | R8: keep the still's own medium and style exactly (line drawing stays a line drawing, cartoon stays the same cartoon, photo stays a phone photo) |
| text-like marks | R9: no text, letters, digits, signs, numbers on bibs, logos or brand names anywhere |
| duplicated people, split frames | R10: no duplicated people, no split frame, no collage, no mirrored copy, nothing floating; every person stands or sits with contact |

Carousel rules (decisions 360-366): every variant is an EDIT of the still (faces, pose, composition, camera kept unless the change needs it);
time travel for tenses (past = centuries ago, future = about 1000 years ahead; only clothes, surroundings, people around change);
children and babies allowed only in normal, safe, everyday situations; no violence, nothing gross, nothing scary;
adults look fictional; no real people; no text.

## Process per picture
1. Prompt (writer) -> 2. free pre-check (separate verifier reads prompt + still, predicts failures; the prompt is fixed first)
-> 3. paid job (balance read before and after, `gen.sh` refuses past the cap) -> 4. QC (text verdict) + blind verifier
-> 5. if failed: one more paid attempt with a fixed prompt, else the variant is dropped.

## Owner decision 370 (5 Oct 2026, during A49) - replaces the QC part above
QC = HARD fails only: text/letters/digits; word or tense not readable at first glance; broken anatomy or physics;
violence or gross. ALLOWED: faces resembling real people, logos/stickers carried over from the source, framing
differences, imperfect eyelines (prompts still ask for clear eyelines). Blind verifier 3x per picture, pass = right
caption in at least 2 of 3; a single miss = UNSURE for the owner, never a remake. Reuse earlier paid generations first.

## A51 (decisions 373-380, 5 Oct 2026) - replaces the carousel shape above
- A carousel has exactly 3 pictures = 3 answers; the video's still is NOT shown (every picture is still an edit of it).
- Per word at most ONE future, ONE present, ONE past form (distinct in de / es / fr); far future and centuries ago allowed;
  infinitive collocations are not tense forms.
- Common phrases only, no idioms. The native caption must contain the word the video teaches in that language = the
  concept's `word_localizations.translation` (not the noun the video's own exercises happen to use: 8039's "way" is
  Durchgang / paso / passage / geçit / átjáró, 8055's "balloon" is Heißluftballon / montgolfière / hőlégballon).
  One native verifier per language checks every caption (`../verify/out2_<lang>.json`).
- Budget A51: 22 credits (`gen51.sh`: floor 9000 and at most 11 jobs; the balance is read before every job).
- Never deliberately depict a recognisable celebrity or add a large famous brand logo (accidental resemblance and logos
  carried over from the video stay allowed).
- Contact sheet per word: every kept picture with its caption, tense / collocation type and UNSURE mark.
