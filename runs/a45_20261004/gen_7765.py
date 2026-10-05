import json
vid=7765
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(rows): return [{"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} if r else {"t":t,"off":True} for t,r in zip(T,rows)]
scarf=[(.26,.35,.29,.25),(.25,.35,.28,.25),(.22,.37,.33,.25),(.22,.37,.42,.25),(.20,.34,.44,.26),(.22,.31,.44,.30),(.22,.32,.42,.30),(.22,.32,.50,.30)]
woman=[(.55,.25,.43,.22),(.53,.26,.45,.21),(.55,.32,.45,.16),(.71,.21,.29,.26),(.78,.21,.22,.27),(.72,.20,.28,.28),(.64,.23,.36,.35),(.74,.19,.26,.44)]
check=[(.61,.47,.39,.40),(.61,.47,.39,.40),(.62,.48,.38,.40),(.65,.47,.35,.40),(.64,.48,.36,.40),(.66,.48,.34,.40),(.62,.64,.38,.30),(.64,.64,.36,.30)]
c={"mediaId":vid,"level":"B","keyWord":"board","defaultVoice":"male",
"taps":[{"phrase":"to cut into his pancakes","target":"the man in the scarf","voice":"male","keys":keys(scarf)},
{"phrase":"to pour tea from a teapot","target":"the man in the checked shirt","voice":"male","keys":keys(check)},
{"phrase":"to serve the pancakes","target":"the red-haired woman","voice":"female","keys":keys(woman)}],
"stillS":2.7,
"nouns":[{"word":"a teapot","x":.75,"y":.69,"voice":"male"},{"word":"a jug","x":.28,"y":.71,"voice":"male"},
{"word":"a suitcase","x":.18,"y":.59,"voice":"male"},{"word":"saucepans","x":.20,"y":.21,"voice":"male"}],
"question":"What is the red-haired woman doing?",
"answer":["She","is","serving","a","stack","of","pancakes."],
"answerVoice":"female",
"notes":"Key word 'board' (verb) is not shown as a visible noun, not placed. The man in the scarf cuts into the pancakes from about 2.7 s (clearly 3.2-3.7 s). The red-haired woman sets the plate down at 0.2-1.2 s, then stands by the table; her box is cut at the top of the checked-shirt man's box (her lower body is behind him). The man in the checked shirt's head leaves the frame from 3.2 s; only his arm and the teapot remain. 'saucepans' = the copper pans hanging over the range."}
json.dump(c,open(f'content/{vid}.json','w'),indent=1)
