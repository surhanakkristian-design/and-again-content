import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
coord=K([(.20,.29,.42,.55),(.22,.28,.42,.57),(.22,.28,.42,.56),(.22,.27,.44,.59),(.22,.27,.46,.71),(.22,.26,.50,.73),(.22,.24,.52,.76),(.24,.22,.55,.78)])
man=K([(0,.11,.19,.38),(0,.07,.21,.42),(0,.03,.21,.48),(0,0,.21,.49),(0,0,.20,.49),(0,0,.20,.49),(0,0,.20,.49),None])
cat=K([(.62,.34,.20,.28),(.64,.34,.18,.24),(.64,.34,.18,.27),(.66,.34,.18,.27),(.69,.34,.18,.29),(.73,.34,.19,.29),(.75,.36,.20,.40),(.80,.34,.20,.42)])
c={"mediaId":6988,"level":"B","keyWord":"coordinator","defaultVoice":"female",
"taps":[
 {"phrase":"to direct the crew","target":"the woman with the headset","voice":"female","keys":coord},
 {"phrase":"to balance on a ladder","target":"the man on the ladder","voice":"male","keys":man},
 {"phrase":"to hold a serving tray","target":"the woman in the apron","voice":"female","keys":cat}],
"stillS":0.7,
"nouns":[{"word":"a tent","x":0.75,"y":0.17,"voice":"female"},
 {"word":"a coordinator","x":0.52,"y":0.48,"voice":"female"},
 {"word":"a ladder","x":0.20,"y":0.66,"voice":"female"},
 {"word":"a flight case","x":0.75,"y":0.62,"voice":"female"}],
"question":"What is the coordinator doing?",
"answer":["She","is","directing","the","crew."],
"answerVoice":"female",
"notes":"Coordinator's outstretched arm tip near the ladder and her raised right hand over the caterer are cut out of her box so it does not overlap the ladder man (x<0.21) or the caterer. Ladder man is only his legs at the left edge from 2.2 on, off at 3.7. Caterer partly behind the coordinator's arm early on."}
json.dump(c,open('content/6988.json','w'),indent=1)
