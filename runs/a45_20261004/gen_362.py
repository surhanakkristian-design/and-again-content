import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
W={0.5:(.46,.27,.33,.60),1.0:(.29,.28,.47,.71),1.5:(.26,.25,.56,.75),2.0:(.04,.25,.81,.75),2.5:(.07,.25,.93,.75),
3.0:(.12,.25,.72,.75),3.5:(.0,.22,1.0,.78),4.0:(.03,.20,.80,.80),4.5:(.0,.23,.84,.77),5.0:(.04,.25,.96,.75),
5.5:(.0,.25,.92,.75),6.0:(.0,.27,.79,.73),6.5:(.29,.18,.47,.80),7.0:(.26,.18,.50,.82),7.5:(.28,.18,.48,.82),
8.0:(.26,.18,.37,.80),8.5:(.26,.18,.48,.36),9.0:(.23,.19,.48,.34),9.5:(.23,.21,.50,.32),10.0:(.21,.19,.52,.34)}
D={8.0:(.63,.54,.37,.44),8.5:(.36,.54,.64,.44),9.0:(.32,.53,.68,.45),9.5:(.31,.53,.69,.45),10.0:(.30,.53,.70,.44)}
c={"mediaId":362,"level":"A","keyWord":"happy","defaultVoice":"female",
"taps":[{"phrase":"to dance in the street","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to eat a peach","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to come to the woman","target":"the dog","voice":"female","keys":keys(D)}],
"stillS":10.0,
"nouns":[{"word":"a peach","x":.29,"y":.45,"voice":"female"},{"word":"a dog","x":.72,"y":.66,"voice":"female"},
{"word":"a boat","x":.80,"y":.35,"voice":"female"},{"word":"shoes","x":.47,"y":.93,"voice":"female"}],
"question":"How does the woman look?",
"answer":["She","looks","very","happy."],"answerVoice":"female",
"notes":"Only two targets: the old men in the street are several (two seated men at 3.5-4.0 s, others walking), so none could be a unique target. From 8.5 s the dog's head lies on the woman's knees: her box is cut to the upper body (above the dog's head) and her legs fall inside the dog's box. At 8.0 s her right shoulder is cut by the dog box. 'to dance in the street' = 1.5-5 s (she spins and skips; verifier please judge whether 'dance' is clear enough). Question is in the present simple because it asks about a state; the answer carries the key word. 'a boat' is on the white motor boat; a small sailing boat is also far left."}
json.dump(c,open("content/362.json","w"),indent=1)
