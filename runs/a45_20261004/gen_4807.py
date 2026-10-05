import json
tops={0.0:.06,0.5:.06,1.0:.06,1.5:.11,2.0:.10,2.5:.07,3.0:.08,3.5:.06,4.0:.08,4.5:.10,5.0:.04,5.5:.0,6.0:.0,6.5:.0,7.0:.0,7.5:.0,8.0:.13,8.5:.09,9.0:.10,9.5:.10,10.0:.12}
keys=[{"t":t,"x":0.0,"y":y,"w":1.0,"h":round(0.86-y,2)} for t,y in tops.items()]
d={"mediaId":4807,"level":"A","keyWord":"orange","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to drink orange juice","to lift a big jug","to wipe his mouth"]],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.07,"voice":"male"},
{"word":"an orange top","x":0.38,"y":0.62,"voice":"male"},
{"word":"a jug","x":0.83,"y":0.76,"voice":"male"},
{"word":"glasses","x":0.18,"y":0.84,"voice":"male"}],
"question":"What is the man drinking?",
"answer":["He","is","drinking","orange","juice."],
"answerVoice":"male",
"notes":"Only one person in the clip (background players are tiny and blurred), so all three phrases target the man. Key word 'orange' is an adjective; used in 'an orange top' and 'orange juice'. Wipe happens at 8.0-9.0 s."}
json.dump(d,open("content/4807.json","w"),indent=1)
