# writer helper for media 52, 53, 55, 56
import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)

# ---- 52
M={0:(0,.30,.39,1),.5:(0,.26,.41,1),1:(0,.17,.42,1),1.5:(0,.17,.42,1),2:(0,.16,.40,1),2.5:(0,.22,.41,1),3:(0,.30,.40,1),3.5:(0,.26,.40,1),
   4:(0,.20,.39,1),4.5:(0,.16,.42,1),5:(0,.15,.42,1),5.5:(0,.15,.42,1),6:(0,.16,.42,1),6.5:(0,.15,.41,1),7:(0,.15,.42,1),7.5:(0,.15,.43,1),
   8:(0,.08,.39,1),8.5:(0,.08,.39,1),9:(0,.18,.42,1),9.5:(0,.25,.41,1),10:(0,.28,.39,1)}
B={0:(.40,.44,1,1),.5:(.61,.28,1,1),1:(.62,.23,1,1),1.5:(.62,.20,1,1),2:(.60,.19,1,1),2.5:(.61,.26,1,1),3:(.60,.30,1,1),3.5:(.60,.30,1,1),
   4:(.59,.22,1,1),4.5:(.62,.26,1,1),5:(.62,.27,1,1),5.5:(.62,.27,1,1),6:(.62,.25,1,1),6.5:(.61,.20,1,1),7:(.43,.20,1,1),7.5:(.44,.20,1,1),
   8:(.59,.10,1,1),8.5:(.59,.13,1,1),9:(.62,.24,1,1),9.5:(.61,.30,1,1),10:(.59,.33,.97,1)}
Y={0:(.40,.25,.60,.43),.5:(.42,.25,.60,.46),1:(.43,.24,.61,.53),1.5:(.43,.22,.61,.41),2:(.41,.22,.59,.45),2.5:(.42,.21,.60,.45),3:(.41,.22,.59,.55),
   3.5:(.41,.21,.59,.55),4:(.40,.19,.58,.44),4.5:(.43,.19,.61,.43),5:(.43,.19,.61,.55),5.5:(.43,.19,.61,.55),6:(.43,.19,.61,.44),6.5:(.42,.19,.60,.44),
   8:(.40,.18,.58,.44),8.5:(.40,.18,.58,.42),9:(.43,.19,.61,.55),9.5:(.42,.19,.60,.46),10:(.40,.20,.58,.45)}
save({"mediaId":52,"level":"A","keyWord":"assistant","defaultVoice":"male",
 "taps":[{"phrase":"to carry the bags","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to take photos","target":"the blond woman","voice":"female","keys":keys(B)},
         {"phrase":"to stand on a rock","target":"the woman in yellow","voice":"female","keys":keys(Y)}],
 "stillS":0.0,
 "nouns":[{"word":"an assistant","x":.22,"y":.52,"voice":"male"},{"word":"a camera","x":.55,"y":.63,"voice":"male"},
          {"word":"a bag","x":.14,"y":.80,"voice":"male"},{"word":"a dress","x":.50,"y":.37,"voice":"male"}],
 "question":"Who is carrying the bags?","answer":["The","assistant","is","carrying","the","bags."],"answerVoice":"male",
 "notes":"Photographer read as a woman (blond, leather jacket; packet says 'his'). The three targets overlap in the picture, so the boxes are three vertical strips; the blond woman's outstretched arm/camera left of x~.6 falls outside her box in several frames. Model in yellow is OFF at 7.0/7.5 (blurred sliver between the two heads). The man carries two bags at t=0; 'a bag' pill sits on the left one. defaultVoice male = the assistant (key word person)."})

# ---- 53
G={0:(.24,.24,.70,.75),.5:(.24,.21,.61,.78),1:(.03,.18,.85,.63),1.5:(.08,.20,.54,.90),2:(0,.17,.88,.77),9.5:(.05,.23,.31,1),10:(.02,.27,.38,1)}
O={2.5:(.03,.20,.64,.95),3:(.05,.08,.97,.86),3.5:(0,.40,.90,.77),4:(0,.40,1,.83),4.5:(.22,.06,1,1),9:(.82,.47,1,1),9.5:(.61,.30,.80,1),10:(.66,.33,.88,.97)}
P={5:(.08,.23,.95,1),5.5:(.12,.24,.78,1),6:(.24,.29,.72,.95),6.5:(.07,.32,.67,.93),7:(0,.31,.52,1),7.5:(.02,.29,.49,1),8:(.05,.28,.51,.93),
   8.5:(0,.15,.56,.93),9:(0,.40,.68,1),9.5:(.32,.28,.60,1),10:(.39,.27,.65,.98)}
save({"mediaId":53,"level":"B","keyWord":"athletics","defaultVoice":"male",
 "taps":[{"phrase":"to clear a hurdle","target":"the woman in green","voice":"female","keys":keys(G)},
         {"phrase":"to leap into the sand","target":"the man in orange","voice":"male","keys":keys(O)},
         {"phrase":"to hurl a heavy ball","target":"the woman in dark red","voice":"female","keys":keys(P)}],
 "stillS":0.0,
 "nouns":[{"word":"hurdles","x":.72,"y":.53,"voice":"male"},{"word":"a scoreboard","x":.18,"y":.40,"voice":"male"},
          {"word":"clouds","x":.55,"y":.12,"voice":"male"},{"word":"a running track","x":.55,"y":.88,"voice":"male"}],
 "question":"What is the woman in green doing?","answer":["She","is","clearing","a","hurdle."],"answerVoice":"female",
 "notes":"Hurdler's kit is turquoise/teal, named 'in green'; shot-putter's kit is maroon, named 'in dark red'. Key word 'athletics' is not a placeable noun. In the group hug (9.5, 10.0) the three overlap: boxes are vertical strips. An official in purple (4.0, 5.0-6.5, 10.0) is not a target. Still is t=0.0 (hurdler mid-jump, but hurdles/scoreboard/track are sharp)."})

# ---- 55
R={0: (0.13, 0.38, 0.74, 1), 0.5: (0.22, 0.08, 0.76, 1), 1: (0.2, 0.1, 0.75, 1), 1.5: (0.25, 0.46, 0.76, 1), 3: (0.1, 0.04, 0.74, 1), 3.5: (0.17, 0.1, 0.73, 1), 4: (0.13, 0.1, 0.71, 1), 4.5: (0.19, 0.43, 0.73, 1), 5: (0.05, 0.58, 0.5, 1), 5.5: (0.12, 0.48, 0.71, 1), 6: (0.18, 0.42, 0.68, 1), 6.5: (0.18, 0.02, 0.71, 1), 7: (0.16, 0.03, 0.7, 1), 7.5: (0.16, 0.03, 0.7, 1), 8: (0.15, 0.03, 0.72, 1), 8.5: (0.18, 0.03, 0.73, 1), 9: (0.03, 0.27, 1, 1), 9.5: (0.03, 0.27, 1, 1), 10: (0.03, 0.27, 1, 1)}
W={0: (0.75, 0.31, 1, 0.62), 0.5: (0.77, 0.33, 1, 0.66), 1: (0.76, 0.36, 1, 0.72), 1.5: (0.77, 0.35, 1, 0.7), 3: (0.75, 0.32, 1, 0.7), 3.5: (0.74, 0.34, 1, 0.72), 4: (0.72, 0.32, 1, 0.68), 4.5: (0.74, 0.31, 1, 0.66), 5.5: (0.72, 0.42, 1, 0.8), 6: (0.69, 0.31, 1, 0.66), 6.5: (0.72, 0.3, 1, 0.66), 7: (0.71, 0.4, 1, 0.76), 7.5: (0.71, 0.4, 1, 0.76), 8: (0.73, 0.3, 1, 0.64), 8.5: (0.74, 0.3, 1, 0.64)}
save({"mediaId":55,"level":"B","keyWord":"auction","defaultVoice":"female",
 "taps":[{"phrase":"to bid with number nineteen","target":"the red-haired woman","voice":"female","keys":keys(R)},
         {"phrase":"to hug a wooden paddle","target":"the red-haired woman","voice":"female","keys":keys(R)},
         {"phrase":"to wear a striped top","target":"the woman in purple","voice":"female","keys":keys(W)}],
 "stillS":5.0,
 "nouns":[{"word":"a grandfather clock","x":.62,"y":.29,"voice":"female"},{"word":"a flat cap","x":.31,"y":.41,"voice":"female"},
          {"word":"a paddle","x":.38,"y":.57,"voice":"female"},{"word":"a window","x":.13,"y":.30,"voice":"female"}],
 "question":"What is the red-haired woman doing?","answer":["She","is","bidding","at","an","auction."],"answerVoice":"female",
 "notes":"Only two usable targets: many people raise paddles, several clap at the end, two men wear flat caps, so the crowd offers no unique action. Third phrase is a state (striped top under the purple jacket). Lowered paddle reads 17/12 in some frames, raised it reads 19. The purple woman's head overlaps the red-haired woman's hair: split by a vertical line (~x .70-.76), cutting the right edge of the red hair/braid. Red-haired woman at 5.0 is seen from behind, bottom left. Purple woman OFF 9.0-10.0 (only a sleeve). 'a window' / 'a paddle' are plain words in a B video."})

# ---- 56
Wm={0:(0,.62,.34,1),.5:(.02,.54,.83,1),1.5:(0,.50,.38,1),2:(0,.32,.58,1),2.5:(0,.14,.58,1),3:(0,.19,.66,1),3.5:(0,.19,.53,1),4:(0,.22,.58,1),4.5:(0,.21,.53,1),
    5:(0,.17,.43,1),5.5:(0,.17,.41,1),6:(0,.15,.43,1),6.5:(0,.30,.60,1),7:(.12,.39,.76,1),7.5:(.24,.27,.67,.88),8:(.12,.47,.64,.88),8.5:(.14,.45,.62,.90),
    9:(.14,.47,.60,.90),9.5:(.34,.50,.62,.95),10:(.12,.41,.57,.81)}
Mn={4.5:(.82,.22,1,.80),5:(.80,.22,1,.92),5.5:(.76,.22,1,.92),6:(.70,.26,1,.83),6.5:(.72,.27,1,.83),7:(.80,.29,1,.97),7.5:(.82,.30,1,.95),
    8.5:(.82,.36,1,.54),9:(.72,.44,1,.93),9.5:(.63,.28,1,.82),10:(.82,.34,1,.83)}
save({"mediaId":56,"level":"A","keyWord":"autumn","defaultVoice":"female",
 "taps":[{"phrase":"to jump into the leaves","target":"the woman","voice":"female","keys":keys(Wm)},
         {"phrase":"to catch a leaf","target":"the woman","voice":"female","keys":keys(Wm)},
         {"phrase":"to hold a rake","target":"the man","voice":"male","keys":keys(Mn)}],
 "stillS":5.5,
 "nouns":[{"word":"leaves","x":.62,"y":.60,"voice":"female"},{"word":"a rake","x":.86,"y":.75,"voice":"female"},
          {"word":"a coat","x":.17,"y":.70,"voice":"female"},{"word":"trees","x":.45,"y":.12,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","jumping","into","the","leaves."],"answerVoice":"female",
 "notes":"Key word 'autumn' is not a placeable noun. Woman at 0.0-2.0 is only a sleeve / leg / hand (first-person shots); OFF at 1.0. Man is at the right edge and mostly cut off; OFF before 4.5 and at 8.0; at 7.5/8.5/10.0 only a sliver of head, hand or rake is visible. Both people smile, so no laugh phrase."})
