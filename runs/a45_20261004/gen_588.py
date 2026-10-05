import json
T=[i*0.5 for i in range(21)]
def keys(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
N=None
W=[(0,0,.80,.58),(0,0,.52,.55),N,(0,0,.18,.32),(0,0,.18,.33),(0,0,.19,.35),(0,0,.21,.39),(0,0,.25,.41),(0,0,.29,.43),(0,0,.32,.45),(0,0,.34,.46),(0,0,.39,.45),(0,0,.42,.51),(0,0,.44,.63),(0,0,.32,.72)]+[N]*6
Y=[N,N,N,(.82,.17,.18,.14),(.77,0,.23,.32),(.67,0,.33,.37),(.54,0,.46,.50),(.51,0,.49,.55),(.52,0,.48,.45),(.57,0,.43,.47),(.57,0,.43,.59),(.58,0,.42,.57),(.60,0,.40,.48),(.55,0,.45,.58),(.70,0,.30,.70)]+[N]*6
bc=[N,N,(.80,.19),(.60,.18),(.52,.19),(.43,.21),(.41,.26),(.41,.28),(.42,.30),(.45,.31),(.47,.33),(.48,.31),(.51,.31),N,(.51,.29),(.55,.26),(.54,.22),(.57,.20),(.57,.18),(.57,.17),(.57,.17)]
B=[N if c is None else (round(c[0]-.09,2),round(c[1]-.07,2),.18,.14) for c in bc]
d={"mediaId":588,"level":"A","keyWord":"puddle","defaultVoice":"female",
"taps":[
 {"phrase":"to wear red boots","target":"the woman in red boots","voice":"female","keys":keys(W)},
 {"phrase":"to wear black boots","target":"the person in black boots","voice":"female","keys":keys(Y)},
 {"phrase":"to stand far away","target":"the bird","voice":"female","keys":keys(B)}],
"stillS":5.0,
"nouns":[{"word":"a yellow raincoat","x":.78,"y":.12,"voice":"female"},{"word":"a bird","x":.47,"y":.33,"voice":"female"},{"word":"red boots","x":.13,"y":.41,"voice":"female"},{"word":"a puddle","x":.50,"y":.75,"voice":"female"}],
"question":"What are the two people doing?",
"answer":["They","are","jumping","into","a","big","puddle."],
"answerVoice":"female",
"notes":"Both people do the same actions (walk up, jump, splash), so the two person phrases are states (boot colour). Boxes hold the real people only, not their reflections in the puddle. The person in black boots / yellow raincoat: gender not clear (face never fully shown) -> default voice. The bird is small and far back (minimum box); at 6.5 s it stands in the narrow gap between the two jumping people, so it is off there. At 1.0 s only reflections of the people are visible -> off."}
json.dump(d,open("content/588.json","w"),indent=1)
