import json
T=[i/2 for i in range(21)]
W={0.0:(.02,.23,.85,.77),0.5:(0,.24,.75,.76),1.0:(0,.27,.70,.73),1.5:(0,.27,.42,.73),2.0:(.02,.26,.68,.74),2.5:(.22,.27,.60,.70),
3.0:(0,.26,.95,.74),3.5:(.08,.22,.92,.78),4.0:(0,.19,.87,.81),4.5:(.37,.24,.60,.76),5.0:(.17,.22,.72,.78),5.5:(0,.14,.48,.86),
6.0:(0,.10,.55,.90),6.5:(.07,.10,.74,.90),7.0:(.05,.12,.72,.68),7.5:(.08,.14,.64,.86),8.0:(.06,.14,.64,.86),8.5:(.08,.14,.66,.86),
9.0:(.22,.24,.58,.76),9.5:(.21,.24,.60,.76),10.0:(.20,.22,.62,.78)}
M={5.5:(.48,.28,.52,.72),6.0:(.55,.25,.45,.75),6.5:(.82,.72,.18,.28),7.0:(.42,.80,.58,.20),7.5:(.72,.72,.28,.28),8.0:(.70,.62,.30,.38),8.5:(.75,.62,.25,.38)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4426,"level":"A","keyWord":"meeting","defaultVoice":"female",
"taps":[{"phrase":"to point at the board","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to cross her arms","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to shake the woman's hand","target":"the man in the blue shirt","voice":"male","keys":keys(M)}],
"stillS":6.5,
"nouns":[{"word":"a folder","x":.74,"y":.69,"voice":"female"},{"word":"glasses","x":.42,"y":.15,"voice":"female"},
{"word":"a jacket","x":.30,"y":.47,"voice":"female"}],
"question":"What is the woman pointing at?","answer":["She","is","pointing","at","the","board."],"answerVoice":"female",
"notes":"The man in the blue shirt is the seated bearded man at 5.5-6.0 s; at 6.5-8.5 s only his hand / forearm reaches in from the right or below, boxed there (split from the woman at the joined hands; at 7.0 s the woman's box ends at y .82 above his arm). He is off in the last shot (9-10 s) and at 5.0 s: several men in light blue shirts, identity not certain. Key word 'meeting' is not a visible noun and is not used in the texts. Nouns only 3: all on the woman at 6.5 s but well apart (glasses on her head, jacket, folder)."}
json.dump(c,open('content/4426.json','w'),indent=1)
