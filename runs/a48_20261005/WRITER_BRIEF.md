# A48 content writer brief (lab, 10 videos)

Run folder: ~/Projects/and-again-content/runs/a48_20261005 (RUN). Input: RUN/source.json (each video's current
exercises 1, 2, 4: tap phrases + targets, nouns, question, model answer), RUN/frames/<id>.png (the still frame that the
carousel images will be EDITED from) and RUN/frames/<id>_sheet.jpg (12 frames across the whole clip). LOOK at both
images of every video before writing.

Each lab video gets five exercises: (1) "Tap who does it." (phrases), (2) "Place the nouns.", (3) "Choose matching
caption." (NEW: a two-way carousel of image variants made by editing the still), (4) the question with its model
answer, (5) "Fill in what you remember." (NEW: recall rows with gaps). You write (3) captions, fix (4), write (5).

## (3) Carousel captions
The original still is the first image (it gets a caption too). Swiping horizontally shows the HORIZONTAL set, swiping
vertically the VERTICAL set. Total images per word INCLUDING the original: 3 to 6 (many only when they are funny AND
instantly clear; else 3).
- Noun key word: VERTICAL = noun collocations ("blind date", "double date", "hot-air balloon"); HORIZONTAL = verb
  collocations as infinitive phrases ("to plan a date", "to pop a balloon").
- Verb key word: VERTICAL = exactly 3 forms of the verb in different tenses (the original is one of them);
  HORIZONTAL = verb collocations ("to run a race").
- The original sits in one of the two sets (say which: "originalIn": "vertical" or "horizontal") with a caption that
  truly describes the still. In the vertical set give the order top to bottom; the original's place in it is where the
  learner starts (e.g. past above, original in the middle, another below).
- Captions are the SHORTEST possible phrases, British English, correct collocations. Collocations: infinitive phrase
  ("to plan a date"). Tenses: a finite verb phrase WITHOUT subject ("ran from a dragon", "is leading a horse", "was led
  by a knight", "always runs").
- Tenses: exactly 3 per verb, varied between words. Level A: present simple (with -s, one person: "always runs"),
  present continuous, past simple, future (will). Level B mostly harder: present perfect ("has just run"), past
  continuous ONLY for an action in progress at a moment ("was running in the rain", never with a total duration),
  passive ("was calmed by ...", "is being led by ..."), past perfect continuous, future continuous. Past preferred over
  future; future rarely and only when clearly drawable.
- Time travel for tenses: past = the same person, same pose, same camera, centuries ago; future = the same, about 1000
  years ahead; only clothes, surroundings and people around change, always from the key word's own world (horse ->
  knight and castle / robot horse on Mars). Clarity of the word and the tense always wins over keeping the pose.
- Every caption must be DRAWABLE as an edit of THIS still (keep faces, pose, composition, camera) and must be
  distinguishable from every other caption of the same word at first glance by a learner who sees only the image and
  the list of captions. Avoid pairs a picture cannot separate (e.g. "to meet" vs "to greet").
- Start from this proposal and ADAPT to each clip (drop what cannot be drawn clearly from the still, replace it):
  a balloon: hot-air balloon / water balloon / balloon animal · to blow up / to pop / to let go of a balloon
  a dolphin: baby dolphin / pod of dolphins / dolphin show · to swim with / to feed / to spot a dolphin
  to run: tenses · to run a race / to run for the bus / to run out of breath
  a duke: young duke / duke and duchess / duke's castle · to bow to / to meet / to serve the duke
  a bench: park bench / weight bench / picnic bench · to sit on / to paint / to share a bench
  to calm: tenses · to calm a horse / to calm down / to calm your nerves
    OWNER CORRECTION (5 Oct 2026): children and babies MAY appear in carousel images; "to calm" may use a baby again
    ("is calming a baby", "was calmed by a nanny", "to calm a baby"). Children only in normal, safe, everyday
    situations (no danger, no distress beyond an ordinary crying baby, nothing suggestive).
  a mannequin: shop-window / dressmaker's mannequin / mannequin challenge · to dress / to carry / to pose like a mannequin
  a bag: shopping bag / sleeping bag / tea bag · to pack / to carry / to drop a bag
  a way: way out / way home / one-way street · to lose your way / to ask the way / to block the way
  to lead: tenses · to lead a horse / to lead a team / to lead the way
- Note: the stills of balloon (8055) and bench (8056) are black-and-white line drawings, bag (62), run (624), calm
  (4265, parrots), lead (432) are cartoons; dolphin (236), duke (7071), mannequin (461), way (8039) are photos. Images
  are edits of the still, so they keep the still's medium. "to calm" in the still is two cartoon parrots: say how the
  tenses are drawn there (a baby, a horse or a dog may be added; the same parrot may calm them).
- For every caption also write a one-line EDIT IDEA (what changes in the still so that this caption reads at once:
  the twist or light conflict that serves the word, never violence; no text/letters/digits; no real people, logos).
- Native speaker check of every caption: article use, -s, tense use, no "for <duration>" with past continuous.

## (4) The question and its model answer
Check the question and the model answer against the clip (frames) and grammar. Fix anything wrong: wrong preposition
or collocation ("laugh at his jokes", never "laugh about"), invented details or durations, tense that does not match
(ongoing = present continuous). Keep the level (A simple; B at least one B1/B2 word). Keep the answer 3-9 words, a full
sentence starting with a capital and ending with a full stop. Keep the question at most 7 words. Unchanged is fine
when it is right; say why.

## (5) Fill in what you remember.
Rows built from THIS video's phrases of exercises 1-4: the tap phrases, the nouns, the carousel captions, and the
model answer's key phrase. 6 to 9 rows per video. Each row is a list of parts; exactly ONE part is the gap (one word or
a short part), the rest are fixed. A leading "to" of an infinitive phrase is plain text (not a chip); every other part
is a chip. Choose gaps with ONE clear answer from the video ("to ___ a date" is weak when several verbs fit; prefer the
key verb of a phrase the learner just met, or the noun after a clear verb). Where several answers FROM THIS VIDEO fit
the same frame, list every one of them in "accept". Mark each row's source: "taps", "nouns", "carousel", "answer". At
least 2 rows must NOT come from the carousel (videos without carousel images show only the other rows; they need at
least 4 rows without the carousel source).

## Output: RUN/content/<id>.json, one file per video, exactly this shape
{
 "mediaId": 7071, "keyWord": "a duke", "level": "B",
 "carousel": {
   "originalIn": "vertical",
   "vertical": [ {"caption": "young duke", "edit": "..."}, {"caption": "old duke", "original": true}, {"caption": "duke and duchess", "edit": "..."} ],
   "horizontal": [ {"caption": "to bow to the duke", "edit": "..."}, ... ]   // the original is NOT repeated here when originalIn = vertical
 },
 "question": "...", "answer": ["He", "is", ...], "answerChanged": true, "answerWhy": "...",
 "recall": [ {"from": "taps", "parts": [ {"text": "to", "plain": true}, {"text": "wear", "gap": true, "accept": ["wear"]}, {"text": "a gold crown"} ]}, ... ],
 "voices": {"default": "male"},
 "notes": "anything the owner should know"
}
"accept" always contains the gap's own text first. Plain parts only for the leading "to". Rows keep the phrase's exact
wording. In the answer array punctuation stays on the last chip only. Write nothing else into RUN except these files.
