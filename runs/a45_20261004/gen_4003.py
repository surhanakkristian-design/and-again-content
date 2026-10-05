import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T15=[i*0.5 for i in range(15)]; T17=[i*0.5 for i in range(17)]
# 4003
split={0.0:(.28,.68),0.5:(.29,.69),1.0:(.41,.58),1.5:(.48,.53),2.0:(.52,.52),2.5:(.52,.52),3.0:(.52,.52),3.5:(.50,.50),4.0:(.46,.46),4.5:(.47,.47),5.0:(.49,.49),5.5:(.49,.49),6.0:(.49,.49),6.5:(.49,.49),7.0:(.49,.49)}
top={t:(0.02,0.0,0.96,a) for t,(a,b) in split.items()}
bot={t:(0.02,b,0.96,round(1-b,2)) for t,(a,b) in split.items()}
kt=K(T15,top); kb=K(T15,bot)
json.dump({"mediaId":4003,"level":"A","keyWord":"pair","defaultVoice":"male",
 "taps":[{"phrase":"to wear yellow slippers","target":"the person at the top","voice":"male","keys":kt},
         {"phrase":"to wear green slippers","target":"the person at the bottom","voice":"male","keys":kb},
         {"phrase":"to wear red trousers","target":"the person at the bottom","voice":"male","keys":kb}],
 "stillS":0.0,
 "nouns":[{"word":"slippers","x":0.50,"y":0.15,"voice":"male"},{"word":"the floor","x":0.50,"y":0.45,"voice":"male"},{"word":"a rug","x":0.15,"y":0.85,"voice":"male"}],
 "question":"What are the two people wearing?",
 "answer":["Each","person","is","wearing","a","pair","of","slippers."],"answerVoice":"male",
 "notes":"Top-down view, only legs and feet of two people; genders not visible, so default voice (odd id -> male). No action fits only one person (both shuffle forward), so three states. Boxes split along the line where the two pairs of slippers meet. 'slippers' pill sits on the yellow pair; the green pair is not used as a noun."},
 open("content/4003.json","w"),indent=1)
# 4004
full=(0,.20,1,.60)
jet={0.0:(0,.20,1,.58),0.5:(0,.25,1,.52),1.0:(0,.38,1,.40),1.5:(0,.40,1,.38),2.0:(0,.22,.62,.54),2.5:full,3.0:(0,.20,1,.65),3.5:(0,.20,1,.65),4.0:full,4.5:full,5.0:(0,.20,1,.65),5.5:full,6.0:(0,.30,1,.46),6.5:(0,.38,1,.40),7.0:(0,.26,1,.52)}
hand={0.5:(.45,0,.55,.24),1.0:(.36,.08,.64,.30),1.5:(.36,.10,.64,.30),2.0:(.62,.44,.38,.26),6.0:(.82,.12,.18,.18),6.5:(.43,.12,.57,.26),7.0:(.50,0,.50,.24)}
kj=K(T15,jet); kh=K(T15,hand)
json.dump({"mediaId":4004,"level":"B","keyWord":"heat","defaultVoice":"female",
 "taps":[{"phrase":"to heat slices of bread","target":"the model jet","voice":"female","keys":kj},
         {"phrase":"to shoot out blue flames","target":"the model jet","voice":"female","keys":kj},
         {"phrase":"to insert slices of bread","target":"the hand","voice":"female","keys":kh}],
 "stillS":5.5,
 "nouns":[{"word":"a cabinet","x":0.25,"y":0.12,"voice":"female"},{"word":"toast","x":0.45,"y":0.40,"voice":"female"},{"word":"a fighter jet","x":0.60,"y":0.58,"voice":"female"},{"word":"a countertop","x":0.50,"y":0.82,"voice":"female"}],
 "question":"What is the model jet doing?",
 "answer":["It","is","heating","two","slices","of","bread."],"answerVoice":"female",
 "notes":"Only a hand and forearm are shown, no main person: default voice by even id (female). The hand overlaps the jet in the picture at 1.0, 1.5 and 6.5 s; boxes are split on a horizontal line under the hand, at 2.0 s on a vertical line (hand presses the lever on the right). The held bread hangs into the jet box at 0.5 and 7.0 s. Jet box includes the flames."},
 open("content/4004.json","w"),indent=1)
# 4005
c={0.0:(0,.66,1,.34),0.5:(0,.70,.95,.30),1.0:(.05,.20,.95,.80),1.5:(0,.24,1,.76),2.0:(0,.22,1,.78),2.5:(0,.07,1,.93),3.0:(0,.08,1,.92),3.5:(0,.17,1,.83),4.0:(0,.36,1,.64),4.5:(0,.42,1,.58),5.0:(.05,.32,.95,.68),5.5:(.02,.40,.98,.60),6.0:(0,.33,1,.67),6.5:(0,.29,1,.71),7.0:(0,.37,1,.63),7.5:(0,.29,1,.71),8.0:(0,.40,1,.60)}
kc=K(T17,c)
json.dump({"mediaId":4005,"level":"A","keyWord":"frozen","defaultVoice":"male",
 "taps":[{"phrase":"to climb a frozen wall","target":"the person","voice":"male","keys":kc},
         {"phrase":"to hit the ice","target":"the person","voice":"male","keys":kc},
         {"phrase":"to wear a red jacket","target":"the person","voice":"male","keys":kc}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.60,"y":0.05,"voice":"male"},{"word":"ice","x":0.50,"y":0.25,"voice":"male"},{"word":"a glove","x":0.72,"y":0.74,"voice":"male"},{"word":"trousers","x":0.45,"y":0.92,"voice":"male"}],
 "question":"What is the person doing?",
 "answer":["The","person","is","climbing","a","frozen","wall."],"answerVoice":"male",
 "notes":"First-person view: the only possible target is the climber (arms, legs, ice axes), so all three phrases share it; the box is the union of the visible body and axes and is large (ice inside the box between the arms). Gender not visible -> default voice by odd id (male). 'a glove' sits on the right glove; a second glove is on the left, not used as a noun. 'axe' avoided as not A level."},
 open("content/4005.json","w"),indent=1)
# 4006
p={0.0:(.08,.63,.74,.37),0.5:(.10,.64,.90,.36),1.0:(.30,.66,.60,.34),1.5:(.16,.70,.56,.30),2.0:(.32,.84,.36,.16)}
m={2.0:(.12,0,.76,.27),2.5:(.15,0,.75,.39),3.0:(.15,0,.75,.47),3.5:(.15,.08,.72,.45),4.0:(.15,.12,.70,.44),4.5:(.15,.14,.70,.44),5.0:(.15,.16,.70,.44)}
f={5.5:(.32,.42,.36,.18),6.0:(.27,.39,.41,.20),6.5:(.20,.38,.53,.30),7.0:(0,0,1,.68)}
json.dump({"mediaId":4006,"level":"B","keyWord":"transparent","defaultVoice":"female",
 "taps":[{"phrase":"to balance on a log","target":"the person","voice":"female","keys":K(T15,p)},
         {"phrase":"to tower over the lake","target":"the mountain","voice":"female","keys":K(T15,m)},
         {"phrase":"to swim towards the camera","target":"the frog","voice":"female","keys":K(T15,f)}],
 "stillS":4.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.07,"voice":"female"},{"word":"a mountain","x":0.45,"y":0.24,"voice":"female"},{"word":"a reflection","x":0.45,"y":0.44,"voice":"female"},{"word":"a log","x":0.50,"y":0.80,"voice":"female"}],
 "question":"What is the water like?",
 "answer":["The","water","in","the","lake","is","transparent."],"answerVoice":"female",
 "notes":"Only bare feet and legs of the person are seen (gender unknown -> default by even id, female); person off from 2.5 s. The mountain box covers the mountain AND its mirror image (at 2.0 s only the mirror image is in the picture). Frog and mountain are never in one frame, so the still (4.0 s) has no frog."},
 open("content/4006.json","w"),indent=1)
