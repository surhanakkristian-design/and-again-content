import json
K=[(0.0,0,0.02,0.97,0.98),(0.5,0,0.02,0.97,0.98),(1.0,0,0.02,0.97,0.98),(1.5,0,0.02,0.97,0.98),(2.0,0,0.02,0.97,0.98),(2.5,0,0.02,0.97,0.98),
(3.0,0,0,1,1),(3.5,0,0,1,1),
(4.0,0.15,0.10,0.66,0.90),(4.5,0.15,0.10,0.66,0.90),(5.0,0.15,0.10,0.66,0.90),(5.5,0.15,0.10,0.66,0.90),(6.0,0.13,0.07,0.71,0.93),
(6.5,0.08,0.08,0.92,0.80),(7.0,0.08,0.13,0.92,0.77),(7.5,0.08,0.13,0.92,0.77),(8.0,0,0.10,1,0.80),(8.5,0,0.16,1,0.68),(9.0,0,0.23,1,0.55),
(9.5,0,0.30,0.98,0.57),(10.0,0,0,0.80,0.88),(10.5,0,0,1,0.75),(11.0,0,0.20,0.60,0.66),(11.5,0,0.08,1,0.70),(12.0,0,0.32,1,0.45),(12.5,0,0.37,1,0.38),(13.0,0,0.37,1,0.38)]
keys=[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in K]
d={"mediaId":4822,"level":"A","keyWord":"message","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to type a message","to smile at her phone","to hide under the blanket"]],
"stillS":7.0,
"nouns":[{"word":"a picture","x":0.72,"y":0.07,"voice":"female"},{"word":"a woman","x":0.47,"y":0.30,"voice":"female"},
{"word":"a phone","x":0.46,"y":0.51,"voice":"female"},{"word":"a bed","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the woman typing?",
"answer":["She","is","typing","a","message."],"answerVoice":"female",
"notes":"Only one person, so all three phrases share the woman. She changes into a camouflage top at 9.5-11.0 s (same woman). At 11.5-13.0 s she is under the white duvet: the box covers the duvet mound she hides in. 'blanket' used for the duvet (A level)."}
json.dump(d,open("content/4822.json","w"),indent=1)
