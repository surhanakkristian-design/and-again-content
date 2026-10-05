import json
T=[i*0.5 for i in range(25)]
trav={0.0:(.44,.28,.18,.37),0.5:(.33,.33,.40,.38),1.0:(.10,.13,.70,.76),1.5:(.37,.18,.36,.62),2.0:(.35,.18,.40,.54),
2.5:(.28,.05,.46,.70),3.0:(.37,.08,.41,.62),3.5:(.28,.28,.40,.63),4.0:(.34,.30,.34,.43),4.5:(.35,.32,.28,.33),
5.0:(.14,.32,.44,.44),5.5:(.25,.32,.31,.51),6.0:(.33,.30,.31,.42),6.5:(.30,.28,.31,.41),7.0:(.31,.32,.25,.29),7.5:None,
8.0:(.22,.34,.26,.37),8.5:(.21,.34,.50,.47),9.0:(.36,.31,.45,.66),9.5:(.36,.33,.38,.50),10.0:(.38,.27,.32,.43),
10.5:(.32,.31,.41,.36),11.0:(.38,.36,.26,.33),11.5:(.29,.33,.38,.43),12.0:(.25,.32,.46,.55)}
ferry={8.5:(.73,.08,.27,.48),9.0:(0,.15,.35,.45),9.5:(0,.15,.35,.50),10.0:(0,.24,.37,.32),10.5:(0,.24,.30,.33),
11.0:(0,.28,.26,.32),11.5:(0,.25,.22,.36),12.0:(0,.22,.22,.38)}
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
V="female"
c={"mediaId":5419,"level":"B","keyWord":"transfer","defaultVoice":V,
"taps":[{"phrase":"to sprint up the stairs","target":"the traveller","voice":V,"keys":keys(trav)},
{"phrase":"to rush up the gangway","target":"the traveller","voice":V,"keys":keys(trav)},
{"phrase":"to float beside the quay","target":"the ferry","voice":V,"keys":keys(ferry)}],
"stillS":10.0,
"nouns":[{"word":"a ferry","x":.15,"y":.33,"voice":V},{"word":"a backpack","x":.52,"y":.42,"voice":V},
{"word":"a gangway","x":.50,"y":.78,"voice":V},{"word":"the sky","x":.50,"y":.12,"voice":V}],
"question":"What is the traveller doing?",
"answer":["The","traveller","is","rushing","to","catch","a","ferry."],
"answerVoice":V,
"notes":"Packet says 'a man' but the close face at 11.5-12.0 looks like a young woman with a shaved head; I used the neutral target 'the traveller' and female voices - verifier please check gender/voice. Traveller hidden inside the tram at 7.5 (off). Ferry only from 8.5 (right edge) to the end; its box is the left/visible part only, split from the traveller at 9.0-9.5. Other trams and a bus appear, so no tram/bus phrase. Key word 'transfer' is not a visible noun."}
json.dump(c,open('content/5419.json','w'),indent=1)
