import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x1,y1,x2,y2=v
            out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
F={0.0:(.40,.72,.62,.94),0.5:(.42,.83,.63,1.0),1.0:(.39,.69,.59,.91),1.5:(.37,.68,.57,.90),2.0:(.40,.71,.60,.93),
2.5:(.40,.74,.61,.97),3.0:(.40,.86,.62,1.0),3.5:(.36,.86,.54,1.0),4.0:(.36,.86,.60,1.0),4.5:(.43,.71,.65,.94),
6.0:(.42,.83,.62,1.0),6.5:(.44,.86,.68,1.0),7.0:(.38,.86,.56,1.0),7.5:(.40,.86,.61,1.0),8.5:(.45,.81,.65,1.0),
9.5:(.52,.86,.74,1.0),10.0:(.27,.86,.47,1.0),10.5:(.24,.76,.42,1.0),11.0:(.48,.66,.70,.94),
13.5:(.50,.86,.68,1.0),14.0:(.42,.86,.60,1.0)}
R={6.5:(.41,.06,.59,.36),7.0:(.41,0,.59,.36),7.5:(.41,0,.59,.42),8.0:(.42,0,.64,.51),8.5:(.40,0,.64,.81),
9.0:(.40,0,.67,1.0),9.5:(.31,0,.52,1.0),10.0:(.47,0,.66,1.0),10.5:(.36,0,.60,.76),11.0:(.29,0,.48,1.0),
11.5:(.23,0,.49,1.0),12.0:(.28,.09,.54,1.0),12.5:(.38,.15,.60,1.0),13.0:(.45,.50,.67,1.0),13.5:(.36,.56,.82,.86),
14.0:(.08,.72,.42,1.0),14.5:(.36,.74,.56,1.0),15.0:(.35,.74,.55,1.0)}
kf=K(F)
d={"mediaId":4035,"level":"A","keyWord":"step","defaultVoice":"male",
"taps":[{"phrase":"to step on a block","target":"the foot","voice":"male","keys":kf},
{"phrase":"to hang from the tower","target":"the rope","voice":"male","keys":K(R)},
{"phrase":"to wear a black sandal","target":"the foot","voice":"male","keys":kf}],
"stillS":8.5,
"nouns":[{"word":"a rope","x":.52,"y":.25,"voice":"male"},{"word":"a foot","x":.55,"y":.91,"voice":"male"},
{"word":"a hand","x":.86,"y":.62,"voice":"male"},{"word":"the sky","x":.17,"y":.05,"voice":"male"}],
"question":"What is the man stepping on?",
"answer":["He","is","stepping","on","blue","blocks."],"answerVoice":"male",
"notes":"First-person clip: the only person is the filmer (legs, hands), so the targets are his foot and the rope; two phrases share the foot (second one is a state). Foot is off whenever no sandal is in the picture; at 3.0-4.0, 6.5-7.5 and 14.0 s only a sliver of the sandal shows at the bottom edge; at 11.5 s the sandal is mostly hidden behind the rope (off). At 4.0 s both feet are in the box. Rope is on from 6.5 s (thin line on the tower) to the end. Question says 'the man' although only his legs and hands are seen."}
json.dump(d,open("content/4035.json","w"),indent=1)
