import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def W(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4262
t=T(24)
raven={0.0:(.68,.50,.20,.15),0.5:(.70,.52,.20,.15),1.0:(.68,.54,.20,.15),1.5:(.60,.53,.20,.15),2.0:(.57,.52,.20,.15),
 2.5:(.56,.52,.20,.15),3.0:(.58,.50,.25,.15),3.5:(.55,.50,.32,.15),4.0:(.53,.51,.20,.15),4.5:(.49,.51,.20,.15),
 5.0:(.28,.40,.42,.19),5.5:(.22,.46,.26,.18),6.0:(.11,.59,.24,.15),6.5:(.00,.57,.18,.15)}
mom={8.0:(0,.43,.27,.24),8.5:(0,.43,.53,.27),9.0:(.12,.46,.53,.24),9.5:(.18,.47,.49,.24),10.0:(.26,.46,.44,.26),
 10.5:(.31,.49,.41,.25),11.0:(.31,.53,.40,.24),11.5:(.30,.54,.39,.24)}
W({"mediaId":4262,"level":"B","keyWord":"wildlife","defaultVoice":"female",
 "taps":[{"phrase":"to spread its wings","target":"the raven","voice":"female","keys":K(t,raven)},
  {"phrase":"to flutter above the cubs","target":"the raven","voice":"female","keys":K(t,raven)},
  {"phrase":"to tower over her cubs","target":"the mother bear","voice":"female","keys":K(t,mom)}],
 "stillS":1.0,
 "nouns":[{"word":"a raven","x":.78,"y":.62,"voice":"female"},{"word":"cubs","x":.36,"y":.62,"voice":"female"},
  {"word":"snow","x":.15,"y":.05,"voice":"female"},{"word":"a mountainside","x":.55,"y":.30,"voice":"female"}],
 "question":"What is the raven doing?",
 "answer":["It","is","fluttering","above","the","cubs."],"answerVoice":"female",
 "notes":"Only two single targets (raven until 6.5 s, mother bear from 8.0 s); the cubs are 2 then 3 animals, so no cub phrase. The raven flutters above the cubs only around 5.0-5.5 s. Key word 'wildlife' is not one visible thing, so it is not a noun slot. Mother bear box includes the cubs standing in front of her."})

# 4263
t=T(25)
pink={1.5:(.73,0,.27,.54),2.0:(.46,0,.54,.54),2.5:(.21,0,.79,.54),3.0:(0,0,1,.54),3.5:(0,0,1,.54),4.0:(0,0,1,.54),
 4.5:(0,0,.84,.54),5.0:(0,0,.56,.54),5.5:(0,0,.28,.32)}
green={};blue={}
for x in t:
    y=.54 if 1.5<=x<=5.0 else .50
    s=.50
    if x in (10.0,10.5,11.0): s=.45
    if x==12.0: s=.48
    green[x]=(0,y,s,round(.94-y,2)); blue[x]=(s,y,round(1-s,2),round(.94-y,2))
W({"mediaId":4263,"level":"A","keyWord":"admire","defaultVoice":"male",
 "taps":[{"phrase":"to walk through the shop","target":"the pink bird","voice":"male","keys":K(t,pink)},
  {"phrase":"to open its eyes first","target":"the blue bird","voice":"male","keys":K(t,blue)},
  {"phrase":"to get a red face","target":"the green bird","voice":"male","keys":K(t,green)}],
 "stillS":6.0,
 "nouns":[{"word":"a green bird","x":.25,"y":.78,"voice":"male"},{"word":"a blue bird","x":.74,"y":.78,"voice":"male"},
  {"word":"shelves","x":.50,"y":.36,"voice":"male"},{"word":"the floor","x":.50,"y":.94,"voice":"male"}],
 "question":"What are the two small birds doing?",
 "answer":["They","are","admiring","the","pink","bird."],"answerVoice":"male",
 "notes":"Pink bird overlaps the small birds in the picture at 2.0-4.5 s: split at y .54. Shelves are blurred background. The two bird nouns carry a colour to tell them apart. The pink bird is not in the still (6.0 s) but the answer names it."})

# 4264
t=T(14)
woman={0.0:(.40,.43,.22,.20),0.5:(.40,.52,.20,.17),1.0:(.38,.57,.24,.22),1.5:(.39,.56,.21,.19),2.0:(.38,.54,.21,.19),
 2.5:(.38,.50,.21,.21),3.0:(.39,.50,.21,.20),3.5:(.39,.50,.21,.19),4.0:(.40,.50,.21,.20),4.5:(.42,.55,.20,.17),
 5.0:(.40,.60,.22,.23),5.5:(.41,.56,.22,.21),6.0:(.39,.57,.21,.20),6.5:(.38,.54,.21,.21)}
ball={0.0:(.39,.17,.18,.14),0.5:(.37,.07,.19,.15),1.0:(.32,.10,.27,.20),1.5:(.38,.23,.18,.14),2.0:(.38,.40,.18,.14),
 2.5:(.40,.33,.18,.14),3.0:(.40,.26,.18,.14),3.5:(.41,.36,.18,.14),4.0:(.41,.26,.18,.14),4.5:(.42,.11,.18,.15),
 5.0:(.36,.11,.33,.24),5.5:(.41,.21,.18,.14),6.0:(.41,.42,.18,.14),6.5:(.41,.39,.18,.14)}
hands={0.5:(0,.69,1,.31),1.0:(.08,.38,.78,.16),1.5:(.08,.77,.92,.23),4.5:(0,.72,1,.28),5.0:(.18,.38,.68,.19),5.5:(.10,.84,.75,.16)}
W({"mediaId":4264,"level":"A","keyWord":"volleyball","defaultVoice":"female",
 "taps":[{"phrase":"to fly through the air","target":"the ball","voice":"female","keys":K(t,ball)},
  {"phrase":"to wear white trousers","target":"the woman","voice":"female","keys":K(t,woman)},
  {"phrase":"to wear gold rings","target":"the hands","voice":"female","keys":K(t,hands)}],
 "stillS":3.0,
 "nouns":[{"word":"a volleyball","x":.49,"y":.33,"voice":"female"},{"word":"a woman","x":.49,"y":.61,"voice":"female"},
  {"word":"a car","x":.12,"y":.70,"voice":"female"},{"word":"clouds","x":.20,"y":.17,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","playing","volleyball","in","the","road."],"answerVoice":"female",
 "notes":"Two state phrases (woman, hands): every action in the clip (hit / push the ball) is done by both players. The person down the road is small; read as a woman (white top, white trousers, cap). Hands box at 1.0 and 5.0 s covers only the two fists, not the arms, so it does not overlap the woman. 'a car' slot is on the near white car; other parked cars are small."})

# 4266
t=T(24)
dog={0.0:(.43,.36,.19,.14),0.5:(.39,.36,.19,.14),1.0:(.38,.38,.19,.14),1.5:(.40,.38,.19,.15),2.0:(.41,.38,.20,.15),
 2.5:(.42,.38,.21,.15),3.0:(.42,.39,.19,.14),3.5:(.40,.39,.19,.14),4.0:(.35,.38,.20,.15),4.5:(.33,.41,.23,.15),
 5.0:(.36,.48,.21,.16),5.5:(.36,.50,.19,.14),6.0:(.35,.41,.24,.20),6.5:(.26,.34,.34,.38),7.0:(.16,.25,.68,.75),
 7.5:(0,0,1,1),8.0:(0,0,1,1),8.5:(0,0,1,1),9.0:(0,.28,1,.72),9.5:(0,.46,1,.54),10.0:(0,.42,.98,.50),
 10.5:(0,.29,1,.52),11.0:(0,.36,.94,.57),11.5:(0,.34,.90,.66)}
W({"mediaId":4266,"level":"A","keyWord":"energetic","defaultVoice":"female",
 "taps":[{"phrase":"to run across the beach","target":"the dog","voice":"female","keys":K(t,dog)},
  {"phrase":"to stick out its tongue","target":"the dog","voice":"female","keys":K(t,dog)},
  {"phrase":"to roll on its back","target":"the dog","voice":"female","keys":K(t,dog)}],
 "stillS":2.0,
 "nouns":[{"word":"a dog","x":.50,"y":.45,"voice":"female"},{"word":"a hill","x":.28,"y":.17,"voice":"female"},
  {"word":"sand","x":.35,"y":.63,"voice":"female"},{"word":"grass","x":.72,"y":.90,"voice":"female"}],
 "question":"What is the dog doing?",
 "answer":["It","is","running","across","the","beach."],"answerVoice":"female",
 "notes":"The dog is the only target, so all three phrases share it. At 7.5-8.5 s the dog fills the whole (blurred) picture: full-frame box. Key word 'energetic' is an adjective, not used in the texts. Two tiny figures far away on the beach at 1.5-5.0 s are ignored."})
