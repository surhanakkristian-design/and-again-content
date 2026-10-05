import json
T=[i*0.5 for i in range(24)]
def keys(bs):
    assert len(bs)==24
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,bs)]
N=None
# ---------- 4219
beast=[(0,.20,1,.78),(.15,.17,1,.78),(.02,.13,1,.83),(.02,.11,1,.83),(0,.10,1,.78),(.15,.11,1,.78),(0,.07,1,.88),(0,.30,1,.84),
(0,.50,1,.80),(0,.52,1,.78),(0,.52,1,.78),(0,.50,1,.79),(0,.46,1,.78),(0,.46,1,.77),(0,.47,1,.75),(0,.47,1,.75),
(0,.46,1,.74),(0,.42,1,.72),(0,.44,1,.75),(0,.45,1,.74),(0,.42,1,.73),(0,.40,1,.71),(0,.37,1,.70),(0,.42,1,.70)]
hand=[(.50,.78,1,1),(.55,.78,1,1),(.60,.83,1,1),(.60,.83,1,1),(.52,.78,1,1),(.55,.78,1,1),(.40,.88,.92,1),(.03,.84,.75,1),
(.10,.80,.68,1),(.30,.78,.78,1),(.05,.78,.62,1),(.05,.79,.65,1),(.10,.78,.65,1),(.05,.77,.78,1),(.10,.75,.65,1),(.05,.75,.78,1),
(.10,.74,.65,1),(.05,.72,.70,1),(.10,.75,.66,1),(.05,.74,.70,1),(.10,.73,.62,1),(.10,.71,.65,1),(.03,.70,.68,1),(.03,.70,.66,1)]
fall=[N]*8+[(.36,.10,.66,.30),(.38,0,.64,.14),N,N,N,N,(.33,0,.67,.46),(.33,0,.67,.46),
(.30,0,.66,.34),(.33,0,.75,.38),(.30,0,.72,.42),(.26,0,.74,.44),N,N,N,N]
c={"mediaId":4219,"level":"B","keyWord":"beast","defaultVoice":"male","taps":[
{"phrase":"to turn its horned head","target":"the beast","voice":"male","keys":keys(beast)},
{"phrase":"to grip the leather harness","target":"the gloved hand","voice":"male","keys":keys(hand)},
{"phrase":"to cascade down the rocks","target":"the waterfall","voice":"male","keys":keys(fall)}],
"stillS":2.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.07,"voice":"male"},{"word":"a beast","x":0.32,"y":0.36,"voice":"male"},{"word":"a fjord","x":0.25,"y":0.55,"voice":"male"},{"word":"a glove","x":0.70,"y":0.86,"voice":"male"}],
"question":"What is the beast doing?",
"answer":["The","beast","is","diving","off","a","cliff."],
"answerVoice":"male",
"notes":"Rider's-eye view: the rider is only a gloved hand/forearm on the saddle, so no main person (defaultVoice by evenId=false). The beast and the hand overlap in the picture; boxes split along a horizontal line above the glove. Waterfall boxed only where it is clearly a waterfall (4.0-4.5, 7.0-9.5); the white streaks at 5.0-6.5 overlap the beast and are left off. The answer ('diving off a cliff') covers 3.0-4.5; the first phrase covers the head turn at 0-3 s."}
json.dump(c,open('content/4219.json','w'),indent=1)
# ---------- 4220
man=[(.57,.14,1,.90),(.52,.17,1,.90),(.55,.17,1,.93),(.57,.13,1,.92),(.70,.14,1,.87),(.61,.21,1,.87),(.25,0,1,.58),(.30,0,1,.62),
(0,0,.55,.24),N,N,(0,.42,.70,1),N,N,N,(.56,.35,.80,.55),N,N,N,N,N,N,N,N]
car=[(0,.20,.57,.95),(0,.20,.52,.95),(0,.20,.55,.95),(0,.25,.57,.95),(0,.40,.70,.95),(0,.40,.61,.95),(0,.58,1,1),(0,.62,1,1),
(0,.24,1,1),(0,.10,1,1),(0,.15,1,1),(0,0,1,.42),(0,0,1,1),(0,.36,1,1),(0,.35,1,1),(0,.38,.56,.97),
(0,.37,1,.93),(0,.37,.97,.93),(0,.32,1,.82),(0,.32,1,.82),(.04,.33,.96,.69),(.20,.38,.84,.65),(.30,.42,.74,.63),(.36,.45,.70,.62)]
c={"mediaId":4220,"level":"A","keyWord":"clean","defaultVoice":"male","taps":[
{"phrase":"to clean the white car","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to hold a black bag","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to drive down the road","target":"the car","voice":"male","keys":keys(car)}],
"stillS":2.0,
"nouns":[{"word":"hills","x":0.30,"y":0.30,"voice":"male"},{"word":"a man","x":0.90,"y":0.34,"voice":"male"},{"word":"a car","x":0.45,"y":0.66,"voice":"male"},{"word":"a wheel","x":0.14,"y":0.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","cleaning","the","white","car."],
"answerVoice":"male",
"notes":"Man and car overlap in the wide shots (0-2.5 s): boxes split along a vertical line at the man's left edge, so the car's nose under his arms belongs to his box. Close-ups 3.0-4.0: the hand with the cloth is the man, the paint below is the car. 5.5: his hand in the cockpit = the man, the steering wheel area = the car. 7.5: man boxed at the open door, car box only left of him. Man set off at 8.0-8.5 (only a dark shape behind the windscreen). The bag is held only at 0.0-0.5 s."}
json.dump(c,open('content/4220.json','w'),indent=1)
# ---------- 4221
liz=[(0,.31,.76,.84),(0,.31,.76,.83),(0,.44,.78,.99),(.07,.36,.86,.99),(0,.23,.82,.93),(.10,.18,.78,.99),(.10,.20,.72,1.0),(0,.22,.72,.80),
(0,.26,.75,.66),(0,.29,.67,.70),(.02,.26,.64,.86),(.18,.29,.78,.80),(.18,.30,.90,.66),(.12,.27,.96,.68),(.13,.28,.80,.78),(.15,.28,.82,.78),
(.15,.26,.75,.66),(.15,.29,.76,.66),(.07,.28,.75,.78),(.07,.28,.75,.78),(.07,.27,.72,.66),(.07,.27,.74,.66),(.05,.31,.66,.78),(.05,.31,.66,.78)]
c={"mediaId":4221,"level":"A","keyWord":"couch","defaultVoice":"male","taps":[
{"phrase":"to carry a bowl","target":"the lizard","voice":"male","keys":keys(liz)},
{"phrase":"to climb onto the couch","target":"the lizard","voice":"male","keys":keys(liz)},
{"phrase":"to eat from the bowl","target":"the lizard","voice":"male","keys":keys(liz)}],
"stillS":10.0,
"nouns":[{"word":"a couch","x":0.72,"y":0.28,"voice":"male"},{"word":"a lizard","x":0.36,"y":0.42,"voice":"male"},{"word":"a bowl","x":0.70,"y":0.71,"voice":"male"},{"word":"a blanket","x":0.22,"y":0.82,"voice":"male"}],
"question":"Where is the lizard sitting?",
"answer":["It","is","sitting","on","the","couch."],
"answerVoice":"male",
"notes":"Only one acting target (the lizard), so all three phrases share it. It looks rather frog-like in the face but has a long curled tail; the packet calls it a lizard. The lizard box includes its arm and, at 6.5-7.0, the remote it holds; it does not include the bowl."}
json.dump(c,open('content/4221.json','w'),indent=1)
# ---------- 4223
g=[(.15,.22,.87,.64),(.17,.21,.89,.64),(0,.18,.90,.67),(.13,.20,.90,.66),(.12,.19,.92,.67),(.10,.18,.93,.66),(.07,.17,.92,.68),(.07,.15,.94,.67),
(.05,.17,.95,.68),(.05,.08,.97,.69),(0,.08,.97,.74),(0,.15,1,.78),(0,.15,1,.70),(0,.07,1,1),(0,.24,.87,.90),(0,.05,1,.70),
(.17,.44,.82,.84),(.17,.42,.83,.84),(.17,.41,.83,.85),(.17,.41,.83,.85),(.18,.39,.82,.84),(.18,.39,.82,.84),(.23,.28,1,.98),(.23,.28,1,.98)]
ch=[(0,.64,1,.84),(0,.64,1,.83),(0,.67,1,.84),(0,.66,1,.85),(0,.67,1,.87),(0,.66,1,.88),(0,.68,1,.93),(0,.67,1,.95),
(0,.68,1,.92),(0,.69,1,.97),(0,.74,1,1),(0,.78,1,1),(0,.70,1,.98),N,N,N,N,N,N,N,N,N,(0,.42,.23,.62),(0,.42,.23,.62)]
c={"mediaId":4223,"level":"B","keyWord":"spicy","defaultVoice":"male","taps":[
{"phrase":"to swallow a spicy chilli","target":"the gecko","voice":"male","keys":keys(g)},
{"phrase":"to breathe out a flame","target":"the gecko","voice":"male","keys":keys(g)},
{"phrase":"to fill a shallow bowl","target":"the chillies","voice":"male","keys":keys(ch)}],
"stillS":0.0,
"nouns":[{"word":"a gecko","x":0.50,"y":0.42,"voice":"male"},{"word":"chillies","x":0.50,"y":0.72,"voice":"male"},{"word":"a bowl","x":0.50,"y":0.88,"voice":"male"}],
"question":"What is the gecko eating?",
"answer":["It","is","eating","a","spicy","chilli."],
"answerVoice":"male",
"notes":"The glass is not a tap target because the gecko sits inside it (boxes would overlap fully). The chillies phrase is a state (they do nothing else). 'spicy' is not visible as such, but it is the key word and the clip shows it through the red skin and the flame. The gecko's lower body is hidden behind the chillies, boxes split at the top of the pile; the stems sticking up fall into the gecko box. Only 3 nouns: nothing else in the still."}
json.dump(c,open('content/4223.json','w'),indent=1)
