# PROMPT_english_pass v2 — English content pass under the style system (final draft, 10 September 2026)

Status: **installed 10 September 2026 for the rerun of part 1.** The v1 it replaced is kept as
`partsA/work/rerun/PROMPT_english_pass_v1_record.md` (md5 67ed5827cf825db11743bbed2a3751bb).
Machine source of the style rules: `Cursor App/and-again/supabase/functions/_shared/toneStyles.json` (v1.4).
Prose source: `docs/style-system/STYLE_MATRIX.md` (v1.5). Where this file and the JSON differ, the JSON wins.
Everything below marked BINDING is a rule the validator or a checker enforces, or a rule the product owner set on
10 September 2026; the rerun that ignores one of them undoes that day's work.

---

# English content pass — write the `en` row of every exercise for your assigned media

You are writing the English exercises for short vocabulary clips in a language-learning app
for 15–25-year-olds. Each clip teaches ONE target word. Every exercise lives inside that clip's
world, tests its grammar topic cleanly, and is written in the voice assigned to it.

## Inputs
- `work/briefs/brief_<media_id>.txt` — word, part of speech, level, meaning, category, voiceover,
  the scene (explanation, props, actions), and the exercise list (id, type id, title, level).
- `work/asset_classes.csv` — per media: `asset_class` 0–4 (0 abstract, 1 object, 2 creature,
  3 one person, 4 people), `has_minor`, `basis`.
- `work/styles/styles_<media_id>.csv` — per exercise: `exercise_id, style`. Assigned before
  writing by `work/rerun/assign_styles.py`. You write in the style you are given. You never
  pick one and never change one. `chill` on a row marked KEEP means the row is already written
  and you leave it.
- `work/exercise_types_reference.txt` — one example row per type. FORM only.
- The STYLE blocks at the end of this file.

## Output
One file per media item, `work/en_<media_id>.txt`. One three-line block per exercise, in
exercise-id order, the `# style:` line first and naming the style the assignment file gives
that exercise:

    # style: <style>
    E <exercise_id>
    en|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>
    # style: <style>
    E <next_exercise_id>
    en|...

Every grammar exercise id (types 1-26) from the brief appears exactly once, except ids on the
KEEP list, which you do not write at all. Type-27 ids are never written. A clip whose only
exercise is the type-27 label produces no file. The `# style:` line is read by the checkers; `apply_en.py` ignores it.
Then run, and fix until every one is clean:

    python3 ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/apply_en.py "<workbook>" work/en_<media_id>.txt --check
    python3 work/t23/check_t23.py  work/en_<media_id>.txt      # type-23 rows only are judged
    python3 work/rerun/check_t6.py work/en_<media_id>.txt      # type-6 rows only are judged

NEVER run `apply_en.py` without `--check`; never open or write the workbook — the caller applies.

---

## BINDING 1 — The writing rule (Kristian, 10 September 2026), in full
> Each sentence must hold on to something in the video. It may invent an object if that is apt
> and funny — "and why didn't you use this tool too?" — and the tool need not be in the clip.
> The only requirement is that it connects to the video and follows on from it, and ideally it
> is a little funny and carries some emotion. For a picture the story before and after is free;
> for a video the sentence should work with what the video actually shows and not stray far
> from it.

## BINDING 2 — The anchor rule and the swap test (`toneStyles.json`, `anchor_rule`), quoted
> Every generated Tier 1 sentence must contain the keyword, or a directly visible element of the
> asset, as a real participant. Invented context must be plausible for this specific asset and
> must never contradict what is visible.

> Swap test: Would this sentence work equally well under a completely different picture? If
> yes, reject and retry.

Three layers: L1 the frame (always there), L2 the moment (our clips are videos, so nearly
always there), L3 the story around the frame — before, after, why, who said what — always
inventable, never visible, and the layer part 1 almost never used. Use it, under the anchor.

## BINDING 3 — The scene goes into the sentence once, as the anchor
Name the one prop, action or line that makes the sentence this clip's, and stop describing.
The deciding fact — the rule, the source of the obligation, the character's own decision, the
cue the type needs — is a label (`Show rule:`, `Dig rules:`) or a single clause. Do not describe
the scene a second time after the anchor is in place: no trailing "and fans the notes", no "or
they burn", no second sentence that only restates the first. Measured on part 1: 20 of 20
sampled long items lost three to seven words this way with nothing lost, and so did 158 more.
**Check, not rule:** an `intro_text` over 13 words is the sign to look for the second copy. The
part's mean is 9.8 words; the rerun is measured against that.

## BINDING 4 — The four global rules (`toneStyles.json`, `global_rules`)
- **Level beats style.** Never exceed the level's grammar or vocabulary ceiling to fit a style.
  If the style cannot be expressed inside the level, write at the level, drop the markers, and
  say so in your report. **No silent fallback:** never quietly swap the style.
- **Truth beats style.** The correct answer must be factually and linguistically correct.
- **Style colours `intro_text` and the sentence only. It never decides which option is
  correct.** No marker inside the correct answer alone; the options stay what the grammar
  point needs.
- **Never pad.** A class-0 asset gets a plain sentence, not an invented scene.

## BINDING 5 — The distractor rule
Exactly one option is right in **both form and meaning**. Every distractor is wrong: in a
**form item** it is a form a learner produces (`I opens`, `more easy`, `musts`); in a
**contrast item** it is grammatical in the sentence and wrong for the scene (`must` where the
sign imposes `has to`; `the` where the thing is being introduced). Never a defensible second
answer, never a distractor that is merely a different grammatical choice with no cue in the
sentence. Same shape for all three options (two-part answers, two-part distractors).

## BINDING 6 — Contrast items: aim above 50% where the scene allows (recommendation, not gate)
An exercise may test the form; a share of the exercises must test the contrast, where both
options are grammatical and only the scene decides. Aim for more than 50% contrast items per
type per part on the types that exist for a contrast; accept less where the scene does not
allow it; the validator prints the share as a number, nobody fails on it. Part 1 stands at
57% (type 23) and 54% (type 6); the rerun must not fall below them.
- **Type 23 (Must, Have to):** the gap covers the whole modal phrase (never `... to`); options
  such as `has to | must | should`; the source of the obligation is in the sentence (a rule,
  a sign, a boss, the situation forcing it → `has to / have to`; the character's own decision
  → `must`); agreement never decides (third-person singular with `has to`, plural or `you`
  or `I` with `have to`); never `musts`, `must to`, bare `have/has/need`. `check_t23.py`
  refuses anything else. Mix must-items and have-to items; about a third must.
- **Type 6 (A, AN, THE):** options a / an / the; the reason for the article is in the sentence
  (a classification "X is ... Y", a first introduction against a stated contrast, one of
  several, a comparison; a second mention or the one known object for `the`); never `What
  ... !`, `such ...`, `There is ...`, `half ...` or anything that makes `the` ungrammatical.
  `check_t6.py` refuses forcers.

## BINDING 7 — Where a style lives, and the level gates
- **Grammar types 1–26:** the assigned style shapes `intro_text`, the sentence and the
  flavour of the distractors. Nine styles exist.
- **Type 27 (Label the video): kept as written in this pass.** The 237 label rows are already
  chill and stay exactly as they are. Do not write a type-27 row; it must not appear in your file.
- **A1 types 1–11:** chill, slang, dramatic, business, flirt, clueless. **A2 types 12–26:** those
  plus ironic and gossip. Nerd never at A. Flirt off on classes 0–2 and when `has_minor`. The
  assignment file already respects these; if you find a row that does not, stop and report it.

## Hard limits (validated) — unchanged
`intro_text` ≤ 90 characters, options ≤ 50; exactly one gap `...` (three dots) on grammar
types; one sentence, two at most; three options, all filled, all different; type 27 empty
intro; no pipe character in any text.

## Writing rules
- **Video alignment.** Every sentence is about THIS clip (BINDING 1 and 2). The target word,
  or a form of it, appears in every sentence.
- **The gap tests the type, not the word.** Use the reference row for the gap's slot.
- **Level register.** A1/A2 English whatever the style: the style changes which words, never
  the ceiling (A1 present simple / to be / have got; A2 one connector, past simple, going to).
- **The voice.** Write the sentence in the assigned style using its STYLE block: Voice, MUST
  markers (checked), NEVER, Per level. Markers go in `intro_text` and the sentence, never in
  the correct answer alone. If the type's grammar and the style collide, the type wins and the
  rest of the sentence carries the style.
- **Choice types** (13, 15, 18, 23, 6): the sentence contains the cue that makes exactly one
  option right; for 18, a spontaneous decision, promise or opinion cue → will, visible evidence
  or a plan → going to, and do not open every going-to row with "Look".
- Before you finish a clip: audit every exercise as an English teacher, then once more with
  the swap test, then once more for the second copy of the scene.

## Rhythm and report
Work clip by clip in media_id order: brief, style file, write, three checks, fix, next. Report
at the end, briefly: clips and exercises written; any style you could not deliver inside the
level and what you wrote instead; anything you had to bend; any distractor you are unsure is
clearly wrong. No sentence text in the report.

---

## How styles were assigned (the caller did this; you do not repeat it)
`work/rerun/assign_styles.py`: styles with fit ≥ 1 for the media's class (`toneStyles.json`
`recommendations.fit`), minus the level's OFF styles, minus flirt on classes 0–2 or `has_minor`,
minus nerd; weighted by fit; chill at least a quarter of a clip's grammar exercises; the rest
dealt round-robin over the types with a media-id offset; type 27 and KEEP rows chill.
Part 1 assignment: chill 2433, dramatic 769, slang 584, flirt 515, gossip 414, ironic 369,
clueless 321, business 318, over 5,723 exercises.

## The nine STYLE blocks (verbatim from STYLE_MATRIX.md §2, A levels; full marker lists in `toneStyles.json` `styles[].marker_groups`)

### chill — Chill
**Voice.** A normal person describing what they see, the way a textbook or a friendly caption would. The neutral baseline.
**MUST.** Plain standard English; one main clause, optionally one subordinate clause; concrete high-frequency vocabulary; full stop or question mark.
**NEVER.** Slang, abbreviations, jargon; intensifiers (absolutely, literally, completely, totally); exclamation marks; emoji; second person; opinion, judgement, jokes.
**Per level.** A1 ≤ 8 words, present simple / to be / have got. A2 ≤ 12 words, one connector (and, but, because, so).
**Example.** The turkey walks across the yard and stops in front of the barn.

### slang — Slang
**Voice.** A 20-year-old talking to a friend in a voice note or a comment section.
**MUST.** At least two markers from: reduced forms (gonna, wanna, gotta, kinda, ain't, 'cause, y'all, lemme, tryna, dunno); Gen Z lexis (cringe, delulu, rizz, mid, sus, no cap, lowkey, highkey, slay, ate, flex, ghosted, vibe(s), bet, fr, iconic, unhinged, cooked, glazing, npc, based, goated, side quest); address / interjections (bro, bruh, dude, man, nah, yo, ok but, not me…, POV:). Profanity whitelist only: damn, hell, crap, sucks, screwed, ass, asshole, freaking, pissed.
**NEVER.** Corporate, academic or literary vocabulary; passive voice, inversion, advanced linkers; anything outside the profanity whitelist, no slurs, no symbol substitutions.
**Per level.** A1: reduced forms + one address marker only (gonna, gotta, bro, nah, cool, so bad), no idiomatic Gen Z lexis. A2: + comparison and past simple slang (way better, kinda ate, that was mid).
**Example.** Bro, this turkey ain't got no chill — he's straight up strutting to the barn.

### ironic — Ironic (A2 only)
**Voice.** Someone whose words say one thing while the video shows another. Dry, calm, never mean towards the learner.
**MUST.** A visible mismatch between sentence and scene, built with ONE of: overpraise (obviously, clearly, of course, great job, flawless, a real professional, exactly what we needed, love that for him, no notes) or understatement (a bit of a situation, slightly unplanned, could be worse, mildly chaotic, not ideal).
**NEVER.** Irony inside the correct answer or the distractors; sarcasm aimed at the learner; naming an object that competes with a vocabulary answer; irony at A1.
**Per level.** A2: overpraise variant only, one short line.
**Example.** A very humble entrance, obviously. The whole yard is honoured.

### dramatic — Dramatic
**Voice.** A telenovela trailer. Everything is the end of the world.
**MUST.** ONE extreme verb or noun (kill, destroy, ruin, betray, scream, collapse, burn, disaster, nightmare, catastrophe, revenge, the end, forever…) or an intensifier/absolute (absolutely, completely, literally, never again, the worst…); plus at least one exclamation mark or an ellipsis.
**NEVER.** Neutral reporting verbs (walks, says, is) as the only verb; actual violence against a real person, self-harm, death of a named character, weapons, medical emergencies — telenovela level, not graphic.
**Per level.** A1: short exclamations with A1 verbs (No! Stop! This is the worst day!). A2: past simple catastrophes + comparison (It was the worst day of my life!).
**Example.** He storms across the yard, screaming, ready to burn the barn to the ground!

### business — Business
**Voice.** A corporate update. Deadpan, quantified, faintly absurd because the subject is a turkey.
**MUST.** Exactly ONE quantity (a number, a percentage, an amount of money, a date, a deadline, a quarter) and exactly ONE corporate term (target, deadline, budget, alignment, stakeholder, quarterly, roadmap, or similar). More markers make it a parody of a memo, not more Business.
**NEVER.** Slang, exclamation marks, emotion words, second-person insults; real company names, brands, people.
**Per level.** A1: numbers and money only — cardinal numbers, prices, to be / have got plus one corporate noun (The target is 100 euros. We have got a meeting.). A2: + must / have to, there is/are, going to (We have to finish the report by Friday.).
**Example.** Q3 target achieved: 47 metres to the barn, zero delays, full alignment.

### gossip — Gossip (A2 only)
**Voice.** Telling a friend something you just heard, with total commitment and zero verification.
**MUST.** Exactly ONE address / hook (bestie, girl, listen, guess what, ok so, or similar) and exactly ONE attribution (she said, he told me, apparently, I heard, or similar). The listener and the event are real: a friend is being told something that happened in the scene.
**NEVER.** Neutral third-person narration with no listener; formal syntax; gossip about a real named person; cruelty about appearance, weight, or anything a 13-year-old could copy at school — gossip is about events, not bodies.
**Per level.** A2: past simple + say/tell without backshift (She said he is weird!).
**Example.** Bestie, you won't believe it — she told me he walked into that barn like he owns it.

### nerd — Nerd
Not available at A level (B1/B2 only). Listed so the writer knows it exists.

### flirt — Flirt (classes 3 and 4 only; hard OFF when has_minor)
**Voice.** Light, playful, complimentary. The energy of a nice comment under someone's post — not a chat-up line.
**MUST.** The sentence is spoken TO the person in the scene, never about them: second person, direct or implied (you, your, the way you…, POV: you…). Plus ONE light compliment marker (honestly, not gonna lie, low-key, kind of, impressed, charming, smooth, iconic, that's actually cool, respect).
**NEVER.** Any reference to a body, body part, appearance beyond clothes/style, physical attractiveness, age, anything sexual or suggestive — compliment actions, skills, style, taste, energy, confidence only; possessiveness, jealousy, pressure, persistence, negging; alcohol, nightlife, meeting up, phone numbers, DMs; any line addressed to or about a child.
**Per level.** A1: You are so cool. I like your hat. A2: + comparison and going to (You are better than everyone here.).
**Example.** Okay but the way he walks into that barn? Kind of impressive, not gonna lie.

### clueless — Low IQ
**Voice.** Someone completely confident whose thoughts carry no information. The comedy is in the emptiness of the reasoning, never in the grammar and never in absurdity.
**MUST.** Exactly ONE of two moves: vacuously obvious (The chair is for sitting. That is why she sits on it.) or a believable mistake a real person could hold (A ponytail is a small horse.). The empty reasoning is marked with because / so / that's why. Test: could a real person say this and mean it?
**NEVER.** A claim nobody could believe (hair is made of clock); broken grammar — the sentence must be flawless, countability included; wrong about the target word; wrong about anything with real consequences (health, food safety, electricity, water, traffic, money, law, dangerous animals); mocking a person, nationality or job; hedged language (might, may, probably).
**Per level.** A1: The chair is for sitting. That is why she sits on it. A2: past simple + because (She sat down because she was not standing.).
**Example.** A ponytail is hair. The hair is on her head, so that is where the ponytail is.
