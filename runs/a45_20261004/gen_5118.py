import json
B = {0.0:(0,0.43,0.54,0.31),0.5:(0,0.44,0.24,0.28),1.0:(0,0.2,0.32,0.8),1.5:(0,0.25,0.6,0.75),2.0:(0,0.19,1.0,0.81),
2.5:(0,0.2,0.78,0.8),3.0:(0.2,0.31,0.78,0.69),3.5:(0.04,0.36,0.94,0.64),4.0:(0.2,0.38,0.47,0.62),4.5:(0.08,0.37,0.79,0.63),
5.0:(0,0.37,1.0,0.63),5.5:(0,0.37,1.0,0.63),6.0:(0,0.39,1.0,0.61),6.5:(0.06,0.39,0.93,0.61),7.0:(0.31,0.44,0.38,0.56),
7.5:(0.2,0.41,0.6,0.59),8.0:(0,0.39,1.0,0.61),8.5:(0.26,0.38,0.5,0.62),9.0:(0.16,0.4,0.67,0.6),9.5:(0.05,0.41,0.85,0.59),10.0:(0,0.45,1.0,0.55)}
keys=[{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} for t,v in B.items()]
c={"mediaId":5118,"level":"A","keyWord":"sunlight","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to open the window","to smile at the camera","to stand on the balcony"]],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.65,"y":0.12,"voice":"male"},{"word":"sunlight","x":0.25,"y":0.33,"voice":"male"},
{"word":"roofs","x":0.78,"y":0.55,"voice":"male"},{"word":"a man","x":0.45,"y":0.72,"voice":"male"}],
"question":"Where is the man standing?","answer":["He","is","standing","on","the","balcony."],"answerVoice":"male",
"notes":"Only one person, so all three phrases target the man. 'sunlight' pill sits on the bright sun glare in the sky (t=10); 'the sky' pill is higher right in clear blue sky. t=0/0.5 only his arm and hand are visible at the window."}
json.dump(c,open('content/5118.json','w'),indent=1)
