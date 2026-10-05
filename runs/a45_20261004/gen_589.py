import json
T=[i*0.5 for i in range(21)]
def keys(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
N=None
W=[(.17,.07,.41,.59),(.18,.05,.42,.58),(.18,0,.41,.64),(.17,0,.42,.43),(.10,0,.48,.35),(.10,0,.45,.32),(.14,0,.40,.42),(.15,0,.39,.36),(.17,0,.39,.35),(.19,0,.36,.38),(.24,0,.29,.40),(.27,0,.31,.47),(.17,.15,.33,.43),(0,.23,.47,.41),(0,.32,.39,.66),(0,.40,.46,.56),(0,.37,.46,.46),(.03,.38,.47,.46),(0,.43,.46,.53),(0,.37,.46,.50),(.03,.40,.46,.44)]
M=[(.59,.10,.30,.49),(.61,.08,.30,.48),(.60,.02,.26,.58),(.60,0,.28,.42),(.59,0,.25,.30),(.56,0,.29,.28),(.55,0,.27,.38),(.55,0,.28,.39),(.57,0,.25,.31),(.56,0,.29,.35),(.54,0,.31,.40),(.58,0,.30,.47),(.51,.11,.39,.48),(.48,.33,.52,.34),(.40,.45,.60,.50),(.47,.43,.53,.54),(.47,.38,.53,.44),(.50,.39,.50,.43),(.47,.35,.51,.54),(.47,.42,.53,.48),(.50,.37,.50,.47)]
D=[N]*14+[(.82,.28,.18,.14),(.70,.21,.30,.19),(.66,.14,.22,.17),(.71,.15,.18,.14),(.67,.17,.18,.14),(.62,.19,.18,.14),(.60,.23,.18,.14)]
d={"mediaId":589,"level":"A","keyWord":"pulling","defaultVoice":"male",
"taps":[
 {"phrase":"to hold something red","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to have a short beard","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to run across the grass","target":"the dog","voice":"male","keys":keys(D)}],
"stillS":8.0,
"nouns":[{"word":"a dog","x":.76,"y":.24,"voice":"male"},{"word":"grass","x":.25,"y":.29,"voice":"male"},{"word":"a man","x":.78,"y":.58,"voice":"male"},{"word":"a rope","x":.40,"y":.90,"voice":"male"}],
"question":"What are the man and woman doing?",
"answer":["They","are","pulling","a","thick","rope."],
"answerVoice":"male",
"notes":"The man and the woman do the same things (pull, fall, laugh), so their phrases are what only one of them has: she holds the red marker cloth (from 6.5 s), he has a beard (state). The dog appears from 7.0 s (at the right edge first). The two stand/lie close: boxes are split between them, the rope runs through both. The applauding onlookers at the back are not a target; tiny, some may also have beards but it cannot be seen. Mixed pair -> default voice by id (male)."}
json.dump(d,open("content/589.json","w"),indent=1)
