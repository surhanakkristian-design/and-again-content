from lib_7820_7821_7823_7824 import *
wo=[(.26,.13,.52,.74),(.27,.13,.52,.74),(.26,.12,.52,.74),(.26,.13,.52,.75),(.21,.17,.51,.77),(.22,.17,.50,.78),(.21,.16,.49,.78),(.20,.16,.48,.78)]
mn=[(.52,.37,.91,.93),(.52,.37,.92,.95),(.52,.41,.91,.95),(.52,.41,.91,.96),(.52,.39,.93,.97),(.52,.38,.93,.99),(.52,.39,.95,.99),(.52,.38,.94,.99)]
save({"mediaId":7820,"level":"B","keyWord":"eve","defaultVoice":"female",
 "taps":[tap("to string lights along a branch","the woman","female",wo),
         tap("to balance on a stepladder","the woman","female",wo),
         tap("to grin up at her","the man","male",mn)],
 "stillS":0.2,
 "nouns":[nn("the sky",.15,.12,"female"),nn("a tablecloth",.16,.74,"female"),nn("a stepladder",.30,.88,"female"),nn("a crate",.75,.93,"female")],
 "question":"What is the man holding?",
 "answer":["He","is","holding","a","string","of","glowing","bulbs."],
 "answerVoice":"male",
 "notes":"Woman hangs the lights only 0.2-1.7 s, then stands and chats. Her raised arm (0.2-1.7 s) reaches to x 0.62 above the man; her box is cut at x 0.52 so it does not overlap the man's box (his left hand rests near the ladder top). Key word 'eve' is not visible as a noun; not used. Man grins up at her most of the clip, at 1.2-1.7 s he looks up more neutrally."})
