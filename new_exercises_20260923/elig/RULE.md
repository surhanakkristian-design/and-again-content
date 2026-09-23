# Eligibility rule (owner brief, decision 61)
Each item is one video: `sentences` = what is actually spoken (sound-effect markers already removed).

A video is ELIGIBLE (`full: true`) only if AT LEAST ONE of its sentences is a full sentence:
an EXPLICIT subject AND a finite verb.

Counts as full:
- "It's alive!", "I trust you.", "You bet.", "School has many subjects.", "There's the problem."
- questions with inversion or a subject: "Is it hot?", "What are you doing?", "Who wants cake?", "You feel good?"
- slightly ungrammatical speech that still has subject + verb: "Yes, I defeat you again."
- "Here it is.", "There we go.", "This one's beautiful!"

Does NOT count:
- exclamations and interjections alone: "Oh!", "Awesome!", "Wow, so good.", "No way!", "Ta-da!"
- imperatives with the subject only implied: "Look at that!", "Take me to the tower.", "Come on!", "Let's go!", "Pour it all."
- elliptical sentences with the subject dropped: "Got it.", "Sounds good.", "Love it.", "Mine now.", "Heavier than it looked!"
  (NB: the verb inside a subordinate clause like "than it looked" does not make the main sentence full)
- noun phrases / fragments: "Best cut in town.", "Brand new car!", "Perfect foam."
- a word-salad line with no clear subject-verb structure ("Listen that sound Golden to the table").

Judge each item independently. When a sentence qualifies, copy it exactly as `sentence`.
Output: a JSON array, one object per input item, same order:
  {"id": <id>, "full": true|false, "sentence": "<the qualifying sentence>" | null}
