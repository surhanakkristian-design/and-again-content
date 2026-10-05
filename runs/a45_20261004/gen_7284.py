import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
woman=[(.27,.18,.43,.46),(.28,.17,.43,.47),(.26,.16,.46,.50),(.24,.12,.49,.52),(.26,.09,.49,.51),(.26,.09,.49,.51),(.25,.09,.55,.52),(.24,.08,.56,.52)]
lantern=[(.74,.20,.20,.15),(.74,.20,.20,.15),(.75,.20,.20,.15),(.76,.19,.20,.15),(.81,.18,.18,.15),(.79,.19,.19,.15),(.81,.19,.19,.15),(.81,.21,.19,.15)]
kettle=[(.71,.49,.20,.17),(.72,.50,.20,.17),(.73,.50,.21,.18),(.74,.51,.22,.18),(.76,.51,.24,.18),(.76,.52,.24,.19),(.81,.53,.19,.20),(.81,.54,.19,.20)]
c={"mediaId":7284,"level":"B","keyWord":"lay","defaultVoice":"female",
"taps":[
 {"phrase":"to lay sticks in a cone","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to glow at the tent entrance","target":"the lantern","voice":"female","keys":K(lantern)},
 {"phrase":"to rest beside the frying pan","target":"the kettle","voice":"female","keys":K(kettle)}],
"stillS":0.7,
"nouns":[{"word":"a lantern","x":0.80,"y":0.28,"voice":"female"},
 {"word":"an axe","x":0.17,"y":0.46,"voice":"female"},
 {"word":"a kettle","x":0.80,"y":0.58,"voice":"female"},
 {"word":"birch bark","x":0.38,"y":0.71,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","laying","sticks","over","birch","bark."],
"answerVoice":"female",
"notes":"Single shot, slow push-in. Only one person; lantern and kettle used as thing targets. Woman box trimmed on the right where it meets the kettle box (knee/sleeve edge) and the lantern box at 3.2-3.7. From ~1.7 s she sits up and takes the match from her lips; laying happens 0.2-1.7."}
json.dump(c,open('content/7284.json','w'),indent=1)
