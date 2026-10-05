import json
T=[i*0.5 for i in range(21)]
bale=[(.02,.29,.19,.15),(.02,.29,.18,.15),(.02,.31,.18,.15),(.04,.33,.18,.15),(.04,.33,.18,.15),(.05,.34,.18,.15),(.05,.35,.19,.15),(.04,.36,.19,.15),
(.03,.38,.19,.15),(0,.39,.19,.15),(0,.40,.18,.15),(0,.40,.18,.15),(0,.41,.18,.16),(0,.42,.18,.16),(.04,.45,.20,.15),(.09,.46,.22,.16),
(.11,.45,.24,.15),(.13,.44,.24,.15),(.12,.43,.24,.16),(.09,.43,.24,.16),(.06,.40,.23,.15)]
# archer: x0,y0,x1
ar=[(.22,.07,.90),(.21,.09,.89),(.20,.06,.90),(.22,.03,.91),(.22,.02,.90),(.24,.03,.91),(.25,.04,.91),(.24,.03,.90),
(.23,0,.90),(.20,0,.93),(.19,0,.91),(.19,0,.93),(.19,0,.92),(.19,0,1.0),(.25,0,1.0),(.32,.33,1.0),
(.40,.31,1.0),(.42,.31,1.0),(.39,.30,1.0),(.35,.03,1.0),(.30,.03,1.0)]
wo=[(.90,.28,.10,.48),(.89,.28,.11,.48),(.90,.30,.10,.50),(.91,.31,.09,.50),(.90,.33,.10,.50),(.91,.34,.09,.50),(.91,.34,.09,.60),(.90,.35,.10,.62),
(.90,.37,.10,.53),(.93,.40,.07,.52),(.91,.58,.09,.36),(.93,.60,.07,.30),(.92,.63,.08,.34)]+[None]*8
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
kb=[k(t,b) for t,b in zip(T,bale)]
ka=[k(t,(a[0],a[1],round(a[2]-a[0],2),round(1-a[1],2))) for t,a in zip(T,ar)]
kw=[k(t,b) for t,b in zip(T,wo)]
d={"mediaId":106,"level":"B","keyWord":"aim","defaultVoice":"male",
"taps":[{"phrase":"to aim at the target","target":"the archer","voice":"male","keys":ka},
{"phrase":"to serve as a target","target":"the hay bale","voice":"male","keys":kb},
{"phrase":"to observe the young archer","target":"the woman","voice":"female","keys":kw}],
"stillS":0.0,
"nouns":[{"word":"a bow","x":0.33,"y":0.18,"voice":"male"},{"word":"a hay bale","x":0.15,"y":0.36,"voice":"male"},
{"word":"an arrow","x":0.16,"y":0.55,"voice":"male"},{"word":"an archer","x":0.70,"y":0.62,"voice":"male"}],
"question":"What is the archer doing?",
"answer":["He","is","aiming","at","the","hay","bale."],
"answerVoice":"male",
"notes":"The woman stands at the right edge, partly behind the archer's shoulder: her box is a narrow strip split from his box along a vertical line (narrower than the usual minimum). From 6.5 s only her clapping hands or a sliver of her jacket show at the edge -> off. The archer's box includes the bow but is cut on the left where the hay bale sits right behind the bow hand (bale box wins that strip). The target rings on the bale are clearly visible only from 7.5 s. Noun pill 'an arrow' sits on the front of the shaft left of the bow."}
json.dump(d,open("content/106.json","w"),indent=1)
