# Phase 2F Part 2 - judge brief

You are the single blind judge.  For every packet line you see a Czech sentence, its CEFR level,
its grammar topic and ONE English answer.  You do not see who wrote it, whether it was meant to be
correct, or any reference translation.  Decide whether a careful teacher marking this exercise
would accept that English as a translation of that Czech sentence.

## The acceptance rules (the owner's words, verbatim - apply exactly these)
the Czech sentence is the ground truth, not the English reference; a passive is acceptable; a
dropped agent where the Czech names one is WRONG; a missing obligatory English article is an
ERROR; the time frame must match the Czech while the English tense inside that frame is free; a
dropped function word is correct, a dropped content word is wrong, added content is wrong.

A determiner difference (a/an/the/this/that/my/...) is NOT by itself wrong unless the Czech fixes
it - Czech has no articles, and a demonstrative difference counts only where the Czech carries
ten / ta / to / ti / ty / tento / tato / toto / tihle / tenhle / tahle / tohle / tamten.

## What you write
For every jid in the packet, one object:
  {"jid": "Q0001", "judged": "correct" | "wrong",
   "type": null | "T" | "W" | "M" | "S",   (null iff judged is correct;
        T = the time frame is wrong, W = a wrong or swapped content word,
        M = a doer the Czech names has been dropped, S = a slip such as a missing article)
   "confidence": 1..5, "borderline": true|false, "dropped": "" }
Judge every line on its own.  Some lines repeat on purpose; judge them again, do not look back.
Write ONLY the JSON array, no prose, no fences.


## Your task
1. Read /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/packet_part1.json (254 lines) and write /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/verdicts_part1.json - the JSON array of verdicts, one object per jid, in the same order.
1. Read /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/packet_part2.json (256 lines) and write /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/verdicts_part2.json - the JSON array of verdicts, one object per jid, in the same order.
1. Read /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/packet_part3.json (257 lines) and write /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/verdicts_part3.json - the JSON array of verdicts, one object per jid, in the same order.
1. Read /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/packet_part4.json (213 lines) and write /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/judge/verdicts_part4.json - the JSON array of verdicts, one object per jid, in the same order.
Reply in <= 6 lines with the counts.
