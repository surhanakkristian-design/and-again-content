import json
times=[i*0.5 for i in range(25)]
H={0.0:(.16,.36,.45,.27),0.5:(.16,.36,.45,.27),1.0:(.14,.36,.46,.27),1.5:(.12,.36,.47,.27),2.0:(.08,.35,.47,.27),2.5:(.07,.34,.47,.28),
3.0:(.07,.35,.45,.28),3.5:(.07,.35,.44,.28),4.0:(.08,.34,.39,.29),4.5:(.09,.34,.38,.29),5.0:(.10,.34,.37,.29),5.5:(.11,.33,.36,.30),
6.0:(.14,.33,.36,.30),6.5:(.15,.33,.39,.30),7.0:(.11,.32,.42,.31),7.5:(.11,.30,.43,.33),
8.0:(.12,.28,.55,.21),8.5:(.13,.28,.60,.21),9.0:(.13,.28,.62,.21),9.5:(.13,.28,.62,.21),
10.0:(.14,.15,.36,.45),10.5:(.14,.14,.36,.46),11.0:(.09,.30,.62,.19),11.5:(.60,.35,.40,.28)}
B={2.0:(.80,.44,.20,.18),2.5:(.66,.44,.34,.19),3.0:(.58,.49,.42,.16),3.5:(.51,.49,.47,.17),4.0:(.47,.47,.45,.19),4.5:(.47,.47,.45,.19),
5.0:(.47,.49,.44,.18),5.5:(.47,.49,.46,.18),6.0:(.50,.48,.45,.18),6.5:(.54,.47,.44,.20),7.0:(.53,.48,.43,.19),7.5:(.54,.47,.43,.20),
8.0:(.45,.49,.53,.17),8.5:(.45,.49,.54,.17),9.0:(.45,.49,.54,.17),9.5:(.45,.49,.54,.17),10.0:(.50,.44,.50,.22),10.5:(.50,.44,.48,.22),11.0:(.47,.49,.52,.19)}
W={3.0:(.82,.36,.18,.14),3.5:(.78,.36,.22,.14),4.0:(.74,.36,.26,.14),4.5:(.78,.36,.22,.14),5.0:(.78,.38,.22,.14),5.5:(.80,.38,.20,.14),
6.0:(.80,.36,.20,.14),6.5:(.82,.36,.18,.14),7.0:(.82,.36,.18,.14)}
for t in W:
    x,y,w,h=B[t]; top=round(W[t][1]+W[t][3],2); B[t]=(x,top,w,round(y+h-top,2))
def keys(m):
    out=[]
    for t in times:
        if t in m:
            x,y,w,h=m[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":4225,"level":"A","keyWord":"dish","defaultVoice":"male",
"taps":[{"phrase":"to eat from a dish","target":"the orange hamster","voice":"male","keys":keys(H)},
{"phrase":"to hide behind the box","target":"the white hamster","voice":"male","keys":keys(W)},
{"phrase":"to open at the top","target":"the box","voice":"male","keys":keys(B)}],
"stillS":10.5,
"nouns":[{"word":"a hamster","x":.36,"y":.33,"voice":"male"},{"word":"a dish","x":.20,"y":.60,"voice":"male"},
{"word":"a box","x":.76,"y":.59,"voice":"male"}],
"question":"What is the orange hamster doing?",
"answer":["The","orange","hamster","is","eating","from","a","dish."],
"answerVoice":"male",
"notes":"Only 3 nouns: the other clear thing at 10.5 s is a sponge, not an A-level word. The white (white-and-brown) hamster is only partly visible behind/right of the box at 3.0-7.0 s, its head shows above the box top, the two boxes are split on that line (y 0.50-0.52). From 6.5 s the orange hamster's head leans over the box: 6.5-7.5 s split on a vertical line (nose slightly cut), 8.0-9.5 and 11.0 s split on the box top (y 0.49), so the hamster's lower body behind the dish is outside its box. The box opens only at 10.0 s (lid flies off, blurred). What the hamster eats is a green scouring pad, not named."}
json.dump(c,open("content/4225.json","w"),indent=1,ensure_ascii=False)
