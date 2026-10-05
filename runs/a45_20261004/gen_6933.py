import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
curly=k([(.18,.21,.52,.58),(.18,.30,.62,.48),(.18,.29,.64,.50),(.18,.29,.64,.51),(.18,.30,.60,.56),(.18,.31,.52,.55),(.18,.27,.54,.62),(.18,.27,.44,.60)])
blonde=k([(.72,.36,.28,.62),(.80,.35,.20,.62),(.82,.34,.18,.64),(.82,.34,.18,.65),(.78,.34,.22,.64),(.70,.30,.30,.70),(.72,.29,.28,.71),(.78,.38,.22,.45)])
chair=k([(0,.47,.18,.25),(0,.48,.18,.24),(0,.47,.18,.25),(0,.48,.18,.25),(0,.47,.18,.25),(0,.46,.18,.26),(0,.46,.18,.26),(0,.47,.18,.26)])
d={"mediaId":6933,"level":"B","keyWord":"catch","defaultVoice":"female",
 "taps":[
  {"phrase":"to start a pillow fight","target":"the woman with curly hair","voice":"female","keys":curly},
  {"phrase":"to flinch from the blow","target":"the blonde woman","voice":"female","keys":blonde},
  {"phrase":"to watch from an armchair","target":"the woman in the armchair","voice":"female","keys":chair}],
 "stillS":2.2,
 "nouns":[{"word":"a window","x":0.86,"y":0.18,"voice":"female"},{"word":"a wardrobe","x":0.45,"y":0.29,"voice":"female"},
          {"word":"a pillow","x":0.58,"y":0.72,"voice":"female"},{"word":"croissants","x":0.14,"y":0.86,"voice":"female"}],
 "question":"What are the two women doing?",
 "answer":["They","are","having","a","pillow","fight."],
 "answerVoice":"female",
 "notes":"Woman in the armchair is small at the left edge; her box (min width 0.18) cuts into the curly woman's knee/hair, so the curly box starts at x 0.18. Blonde is half out of frame at the right; at 2.7-3.7 her pillow covers the middle, split at x 0.70-0.78. 'Flinch from the blow' fits 0.2-0.7 s only."}
json.dump(d,open("content/6933.json","w"),indent=1)
