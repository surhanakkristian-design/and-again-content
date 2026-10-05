import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
sty={0.0:(.78,.12,.22,.88),0.5:(.80,.37,.20,.63),1.0:(.70,.37,.30,.63),1.5:(.72,.24,.20,.20),2.0:(0,.43,1.0,.57),2.5:(0,.42,1.0,.58),
3.0:(0,.44,1.0,.56),3.5:(0,.45,1.0,.55),4.0:(0,.46,.82,.54),4.5:(0,.52,.90,.48),5.0:(0,.48,.62,.52),5.5:(0,.48,.75,.52),
6.0:(0,.46,.68,.54),6.5:(0,.48,.98,.52),7.0:(0,.68,.70,.32),7.5:(.32,.62,.30,.38),8.0:None,8.5:None,9.0:None}
cli={0.0:(0,.08,.77,.80),0.5:(.02,.06,.77,.94),1.0:(.05,0,.64,1.0),1.5:(.12,0,.58,1.0),2.0:(.38,.21,.58,.21),2.5:(.38,.20,.58,.21),
3.0:(.38,.21,.62,.22),3.5:(.37,.20,.63,.24),4.0:(.37,.16,.63,.29),4.5:(.10,.13,.90,.38),5.0:(.30,.14,.70,.33),5.5:(.38,.15,.62,.32),
6.0:(.38,.19,.62,.26),6.5:(.38,.19,.62,.28),7.0:(.18,.20,.80,.47),7.5:(.20,0,.50,.61),8.0:(0,0,1.0,1.0),8.5:(.20,.08,.78,.92),9.0:(.22,.12,.72,.88)}
S=[k(t,b) for t,b in sty.items()]; C=[k(t,b) for t,b in cli.items()]
d={"mediaId":4808,"level":"B","keyWord":"braid","defaultVoice":"female",
"taps":[{"phrase":"to comb out long hair","target":"the stylist","voice":"female","keys":S},
{"phrase":"to weave a thick braid","target":"the stylist","voice":"female","keys":S},
{"phrase":"to swing her long hair","target":"the client","voice":"female","keys":C}],
"stillS":9.0,
"nouns":[{"word":"a window","x":0.18,"y":0.20,"voice":"female"},
{"word":"shampoo bottles","x":0.14,"y":0.44,"voice":"female"},
{"word":"a braid","x":0.48,"y":0.62,"voice":"female"},
{"word":"a salon chair","x":0.16,"y":0.90,"voice":"female"}],
"question":"What is the stylist doing?",
"answer":["She","is","weaving","a","thick","braid."],
"answerVoice":"female",
"notes":"Stylist is visible only as hands/arms (and patterned dress at edges); her boxes cover the hands and are split from the client's hair box where they overlap, from 2.0 to 7.0 s split horizontally: client box = hair above the hands, stylist box = hands and below. Stylist off at 8.0-9.0 (only a fingertip at 8.0). Client's face and an older woman in a headscarf are visible as reflections in the mirror (not targets). Swing happens 8.0-8.5."}
json.dump(d,open("content/4808.json","w"),indent=1)
