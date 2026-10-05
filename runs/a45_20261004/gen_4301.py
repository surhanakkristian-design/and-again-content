import json
def keys(T,b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
def R(x1,y1,x2,y2): return (round(x1,2),round(y1,2),round(x2-x1,2),round(y2-y1,2))
T=[i*0.5 for i in range(19)]
man=[(.33,.35,.38,.63),(.38,.34,.4,.64),(.38,.34,.38,.6),(.4,.32,.35,.55),(.27,.27,.4,.45),(.38,.3,.36,.58),(.34,.32,.37,.65),(.3,.28,.44,.72),
(.3,.27,.45,.73),(.32,.27,.47,.73),(.32,.28,.45,.72),(.35,.28,.42,.72),(.33,.28,.42,.72),(.36,.27,.38,.73),(.3,.27,.42,.73),(.26,.29,.45,.71),
(.38,.22,.4,.78),(.38,.22,.62,.78),(.4,.26,.6,.74)]
cat=[None,None,(.16,.55,.2,.14),(.15,.57,.25,.19),(0,.72,.46,.23)]+[None]*14
lau=[(.2,.04,.58,.31),(.03,0,.97,.34),(.2,0,.78,.34),(0,0,.75,.32),(.47,0,.48,.18)]+[None]*11+[(.2,.33,.18,.15),(.18,.33,.2,.16),(.1,.33,.3,.16)]
d={"mediaId":4301,"level":"B","keyWord":"gap","defaultVoice":"male",
"taps":[{"phrase":"to squeeze through a gap","target":"the man","voice":"male","keys":keys(T,man)},
{"phrase":"to dart across the alley","target":"the cat","voice":"male","keys":keys(T,cat)},
{"phrase":"to dry on a clothesline","target":"the laundry","voice":"male","keys":keys(T,lau)}],
"stillS":2.0,
"nouns":[{"word":"laundry","x":.7,"y":.07,"voice":"male"},{"word":"a gap","x":.42,"y":.22,"voice":"male"},
{"word":"a backpack","x":.57,"y":.43,"voice":"male"},{"word":"a cat","x":.25,"y":.82,"voice":"male"}],
"question":"What is the man squeezing through?","answer":["He","is","squeezing","through","a","narrow","gap."],"answerVoice":"male",
"notes":"The cat is visible only 1.0-2.0 s (at 1.0 s just its front emerging behind the corner; it crosses at 1.5 s and stops at 2.0 s). Laundry: 0-2.0 s overhead, then again small behind the man at 8.0-9.0 s, where the man's box is cut at its right edge (his right arm / hand at 8.5-9.0 s is outside his box). At 2.0 s the man's box ends at the cat's ears (his shoes slightly clipped). Still 2.0 s: 'a gap' pill sits on the bright slit between the walls he is entering."}
json.dump(d,open("content/4301.json","w"),indent=1)
