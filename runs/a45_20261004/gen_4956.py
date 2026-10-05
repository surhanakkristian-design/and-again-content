import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
W={0.5:(.35,.38,.78,.88),1.0:(.08,.39,.64,1.0),1.5:(.02,.42,.67,1.0),2.0:(.0,.40,.50,1.0),2.5:(.0,.38,.99,1.0),
3.0:(.0,.40,.99,1.0),3.5:(.0,.55,.48,1.0),4.0:(.20,.19,.89,.99),4.5:(.14,.40,1.0,1.0),5.0:(.26,.36,.86,1.0),
5.5:(.43,.40,.88,.99),6.0:(.42,.37,.80,.98),6.5:(.42,.41,.95,.95),7.0:(.57,.42,1.0,.97),7.5:(.82,.40,1.0,.78),
8.0:(.80,.36,1.0,.80),8.5:(.79,.34,1.0,.70),9.0:(.80,.34,1.0,.78)}
S={6.5:(.40,.26,.60,.40),7.0:(.40,.27,.60,.41),7.5:(.39,.27,.59,.41),8.0:(.38,.25,.58,.39),8.5:(.36,.24,.56,.38),9.0:(.35,.23,.55,.37)}
wk=K(W)
c={"mediaId":4956,"level":"A","keyWord":"reception","defaultVoice":"female",
"taps":[
 {"phrase":"to carry a big backpack","target":"the traveller","voice":"female","keys":wk},
 {"phrase":"to touch a world map","target":"the traveller","voice":"female","keys":wk},
 {"phrase":"to go down over the city","target":"the sun","voice":"female","keys":K(S)}],
"stillS":1.5,
"nouns":[{"word":"a screen","x":0.76,"y":0.31,"voice":"female"},
 {"word":"a backpack","x":0.24,"y":0.62,"voice":"female"},
 {"word":"a reception desk","x":0.70,"y":0.79,"voice":"female"}],
"question":"What is the traveller carrying?",
"answer":["She","is","carrying","a","big","backpack."],
"answerVoice":"female",
"notes":"Many cuts (door, reception, map, dorm, rooftop). Traveller identified on the rooftop at 7.5-9.0 s as the blonde woman at the right edge with the stacked bracelets (same person, backpack off) - verifier please confirm. Food is pasta, not paella as the description says; not used. Key word reception placed as 'a reception desk'."}
json.dump(c,open("content/4956.json","w"),indent=1)
