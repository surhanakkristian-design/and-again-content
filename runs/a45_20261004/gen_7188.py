import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
b=[(0.34,0.27,0.66,0.44),(0.32,0.39,0.68,0.37),(0.31,0.46,0.69,0.29),(0.31,0.35,0.69,0.43),(0.29,0.45,0.71,0.40),(0.29,0.44,0.71,0.41),(0.29,0.42,0.71,0.45),(0.29,0.41,0.71,0.48)]
keys=[{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} for t,v in zip(T,b)]
taps=[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to glide beneath the ice","to stretch an arm upwards","to wear a black wetsuit"]]
c={"mediaId":7188,"level":"B","keyWord":"go under","defaultVoice":"female","taps":taps,"stillS":2.7,
"nouns":[{"word":"an iceberg","x":0.50,"y":0.15,"voice":"female"},{"word":"sunbeams","x":0.40,"y":0.38,"voice":"female"},
{"word":"bubbles","x":0.83,"y":0.57,"voice":"female"},{"word":"a diver","x":0.55,"y":0.68,"voice":"female"}],
"question":"What is the diver doing?","answer":["She","is","gliding","beneath","the","ice."],"answerVoice":"female",
"notes":"Only one target (the woman diver), so all three phrases use her. Arm stretches upwards from about 2.2 s; at 0.2-1.7 the arm points forward/up only a little. 'a diver' is the woman (female voice)."}
json.dump(c,open('content/7188.json','w'),indent=1)
