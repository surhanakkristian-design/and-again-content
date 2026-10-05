import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(19)]
boy={0.0:b(0,0.2,0.29,0.24),0.5:b(0,0.2,0.40,0.30),1.0:b(0,0.25,0.44,0.75),1.5:b(0,0.22,0.46,0.78),2.0:b(0,0.22,0.45,0.78),2.5:b(0,0.22,0.45,0.78),3.0:b(0,0.24,0.45,0.76),
3.5:b(0.08,0.24,0.84,0.40),4.0:b(0.08,0.24,0.84,0.40),4.5:b(0.08,0.24,0.84,0.40),5.0:O,5.5:O,6.0:O,
6.5:b(0,0.23,0.56,0.77),7.0:b(0,0.25,0.55,0.75),7.5:b(0,0.25,0.56,0.75),8.0:b(0,0.24,0.66,0.76),8.5:b(0,0.24,0.51,0.76),9.0:b(0,0.28,0.49,0.72)}
mw={0.0:b(0.30,0,0.70,0.47),0.5:b(0.41,0,0.59,0.46),1.0:b(0.46,0.49,0.54,0.39),1.5:b(0.47,0.48,0.53,0.40),2.0:b(0.46,0.41,0.54,0.36),2.5:b(0.46,0.41,0.54,0.36),3.0:b(0.46,0.43,0.54,0.45),
3.5:O,4.0:O,4.5:O,5.0:b(0.18,0.33,0.82,0.62),5.5:b(0,0.08,1.0,0.87),6.0:b(0,0.08,1.0,0.50),
6.5:b(0.57,0.47,0.43,0.33),7.0:b(0.56,0.47,0.44,0.32),7.5:b(0.57,0.47,0.43,0.33),8.0:b(0.67,0.47,0.33,0.32),8.5:b(0.67,0.51,0.33,0.28),9.0:b(0.64,0.51,0.36,0.27)}
girl={t:O for t in times}; girl[8.5]=b(0.52,0.20,0.48,0.30); girl[9.0]=b(0.50,0.20,0.50,0.30)
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":788,"level":"B","keyWord":"to microwave","defaultVoice":"male",
"taps":[{"phrase":"to microwave his noodles","target":"the boy","voice":"male","keys":keys(boy)},
{"phrase":"to grin at the boy","target":"the girl","voice":"female","keys":keys(girl)},
{"phrase":"to light up inside","target":"the microwave","voice":"male","keys":keys(mw)}],
"stillS":8.0,
"nouns":[{"word":"a microwave","x":0.80,"y":0.64,"voice":"male"},{"word":"noodles","x":0.50,"y":0.55,"voice":"male"},{"word":"a shelf","x":0.84,"y":0.27,"voice":"male"},{"word":"a hoodie","x":0.16,"y":0.84,"voice":"male"}],
"question":"What is the boy doing?","answer":["He","is","microwaving","a","bowl","of","noodles."],"answerVoice":"male",
"notes":"Boy box = only his hand at 0.0/0.5; off at 5.0-6.0 (only arms in front of the microwave). Microwave off at 3.5-4.5 (view from inside the oven). The girl appears only at 8.5 and 9.0. Boy's mitts/bowl reach in front of the microwave at 7.5-9.0; boxes split, small gap at 8.5."}
json.dump(c,open('content/788.json','w'),indent=1)
