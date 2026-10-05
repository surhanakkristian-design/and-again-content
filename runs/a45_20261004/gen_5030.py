import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
cos={0.0:(.18,0,.82,1),0.5:(.15,0,.85,1),1.0:(.12,0,.88,1),1.5:(.14,0,.86,1),2.0:(.19,0,.72,1),2.5:(.16,0,.68,1),
 6.5:(.35,0,.26,.95),7.0:(.37,.01,.26,.98),7.5:(.38,.01,.27,.96),8.0:(.38,.01,.26,.93),8.5:(.37,.01,.26,.91),9.0:(.37,.05,.26,.92)}
drum={3.0:(.17,.55,.74,.34),3.5:(.10,.54,.80,.38),4.0:(.07,.50,.82,.34),4.5:(0,.49,.79,.38),5.0:(0,.49,.69,.51),
 5.5:(0,.49,.47,.51),6.0:(.33,.48,.37,.33)}
grn={4.5:(.80,.49,.18,.28),5.0:(.70,.48,.20,.49),5.5:(.48,.49,.26,.50),6.0:(0,.46,.32,.54),
 6.5:(.71,.55,.19,.27),7.0:(.68,.57,.19,.29),7.5:(.75,.57,.19,.29),8.0:(.78,.55,.19,.28),8.5:(.78,.55,.19,.27),9.0:(.78,.54,.19,.28)}
c={"mediaId":5030,"level":"B","keyWord":"costume","defaultVoice":"female",
"taps":[
 {"phrase":"to carry a tall banner","target":"the woman in the feather costume","voice":"female","keys":K(cos)},
 {"phrase":"to march with their drums","target":"the drummers","voice":"male","keys":K(drum)},
 {"phrase":"to run past the drummers","target":"the woman in green","voice":"female","keys":K(grn)}],
"stillS":0.0,
"nouns":[{"word":"a costume","x":.55,"y":.62,"voice":"female"},{"word":"a pole","x":.37,"y":.30,"voice":"female"},
 {"word":"bunting","x":.66,"y":.19,"voice":"female"},{"word":"balconies","x":.88,"y":.38,"voice":"female"}],
"question":"What is the woman in feathers doing?",
"answer":["She","is","carrying","a","banner","down","the","street."],"answerVoice":"female",
"notes":"Cut at 3.0: drummer shot 3.0-6.0 (costume woman OFF), wide crowd shot 6.5-9.0 (drummers only tiny in background, OFF). 'the woman in green' (grey curly hair, green top, denim shorts) runs between the drummers 5.0-6.0 and reappears in the crowd at right 6.5-9.0 - check it is the same person. At 5.5 she stands among drummers; drummers box split at x .47 (one drummer behind her excluded). Drummers voice male (all men)."}
json.dump(c,open('content/5030.json','w'),indent=1)
