import json
T=[i*0.5 for i in range(19)]
w=[(.1,.27,.67,.5),(.11,.27,.68,.5),(.11,.27,.67,.5),(.11,.28,.66,.49),(.05,.23,.77,.6),(.03,.22,.92,.62),(.03,.2,.94,.65),(0,.19,.9,.68),
(0,.18,.96,.72),(0,.18,.95,.72),(0,.18,.93,.74),(.27,.32,.67,.44),(.21,.28,.73,.46),(.19,.22,.74,.48),(.1,.24,.77,.52),(.17,.23,.48,.54),
(.19,.23,.64,.5),(.04,.22,.82,.5),(.16,.22,.81,.5)]
def keys(b): return [dict(t=t,x=x,y=y,w=ww,h=h) for t,(x,y,ww,h) in zip(T,b)]
c={"mediaId":5339,"level":"B","keyWord":"control","defaultVoice":"female",
"taps":[{"phrase":"to grip the steering wheel","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to grin at the huge wheel","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to wear a denim shirt","target":"the woman","voice":"female","keys":keys(w)}],
"stillS":8.5,
"nouns":[{"word":"a driver's seat","x":0.16,"y":0.36,"voice":"female"},{"word":"a bus","x":0.83,"y":0.38,"voice":"female"},
{"word":"a denim shirt","x":0.45,"y":0.52,"voice":"female"},{"word":"a steering wheel","x":0.5,"y":0.67,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","gripping","a","huge","steering","wheel."],"answerVoice":"female",
"notes":"Only one person in the clip, so all three phrases share her as target; phrase 3 is a state. 'Grin at the huge wheel' covers the bus shot (5.5-9 s). Car shot 0-5 s seen through the window, bus cab 5.5-9 s."}
json.dump(c,open('content/5339.json','w'),indent=1)
