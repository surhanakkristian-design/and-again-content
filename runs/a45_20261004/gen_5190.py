import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,0,1,1),0.5:(0,.04,1,.96),1.0:(0,.06,1,.94),1.5:(0,.03,1,.97),2.0:(0,.05,1,.95),2.5:(0,.06,1,.94),3.0:(0,.07,1,.93),
3.5:(0,.09,1,.91),4.0:(0,.08,1,.92),4.5:(0,.10,1,.90),5.0:(0,.13,1,.87),5.5:(0,.18,1,.82),6.0:(0,.20,1,.80),6.5:(.17,.24,.62,.73),
7.0:(.15,.25,.66,.73),7.5:(0,.27,1,.71),8.0:(0,.26,1,.68),8.5:(0,.25,1,.69),9.0:(0,.25,1,.69)}
k=[dict(t=t,x=W[t][0],y=W[t][1],w=W[t][2],h=W[t][3]) for t in T]
c={"mediaId":5190,"level":"A","keyWord":"windy","defaultVoice":"female",
"taps":[{"phrase":"to pull up her hood","target":"the woman","voice":"female","keys":k},
{"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":k},
{"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":k}],
"stillS":8.5,
"nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"female"},{"word":"a raincoat","x":0.48,"y":0.50,"voice":"female"},
{"word":"the sea","x":0.85,"y":0.65,"voice":"female"},{"word":"boots","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","opening","her","arms","wide."],"answerVoice":"female",
"notes":"One person in three shots (clear raincoat 0-2.5, yellow raincoat 3.0-6.0, orange raincoat on the seafront 6.5-9.0), so all three phrases on her. Waves were not used as a target because their spray overlaps her. Key word 'windy' is an adjective, not used. Hood goes up 4.5-5.5; arms open 7.5-9.0."}
json.dump(c,open('content/5190.json','w'),indent=1)
