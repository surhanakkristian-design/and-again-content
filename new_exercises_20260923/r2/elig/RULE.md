# Eligibility rule v2 (owner decision 66, 23 Sept 2026; replaces decision-61 rule)
Each item is one video: `sentences` = what is actually spoken (sound-effect markers already removed).

A video is ELIGIBLE (`full: true`) if AT LEAST ONE of its sentences contains a FINITE VERB.
An explicit subject is NOT required any more.

Finite verb = a verb form that carries tense or mood: present/past forms (is, 's, are, was, got, looks, made),
modals (can, will, 'll, must), imperatives (look, take, come, hold, don't, let's), including in questions and
in a subordinate clause.

Counts (true):
- everything with subject + verb: "It's alive!", "I trust you.", "Is it hot?", "Here it is.", "There we go."
- imperatives and set phrases: "Take me to the tower.", "Hold them like this, slowly.", "Look at that!", "Come on!",
  "Let's go!", "Pour it all.", "Look!", "Wait!", "Thank you.", "Bless you.", "Watch out!"
- subject-less ellipsis with a finite verb: "Got it.", "Sounds good.", "Love it.", "Made it!", "Works every time!"
- a finite verb only inside a subordinate clause: "Heavier than it looked!"
- slightly ungrammatical speech that still has a clear finite verb: "Yes, I defeat you again."

Does NOT count (false):
- no verb at all: "Awesome!", "Two coffees.", "Oh!", "Wow, so good.", "No way!", "Ta-da!", "Perfect foam.",
  "Best cut in town.", "Brand new car!", "Ready?", "Mine now.", "Worth every bit."
- only NON-finite verb forms (participle, gerund, infinitive, with no finite verb): "Well done!", "Perfectly cooked.",
  "Going up!", "Almost there.", "To the moon!", "Freshly baked."
- a word that is a noun/adjective here, not a verb: "Nice shot.", "Game over.", "Good job.", "Check!" (chess call),
  "Cheers!"
- sound markers, humming, singing syllables, counting ("One, two, three!")
- a word-salad line where no word clearly works as a verb.

Judge each item independently. When a sentence qualifies, copy it exactly as `sentence`.
Output: a JSON array, one object per input item, same order:
  {"id": <id>, "full": true|false, "sentence": "<the qualifying sentence>" | null}
