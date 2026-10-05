import json
T=[i*0.5 for i in range(25)]
W={0.0:(0.37,0,0.26,0.27),0.5:(0.3,0,0.4,0.31),1.0:(0.25,0,0.47,0.37),1.5:(0.25,0,0.48,0.41),2.0:(0.25,0,0.49,0.46),2.5:(0.25,0,0.5,0.48),
   3.0:(0.27,0,0.46,0.55),3.5:(0.29,0.01,0.45,0.55),4.0:(0.27,0.02,0.47,0.53),4.5:(0.27,0.02,0.48,0.52),5.0:(0.27,0.02,0.48,0.53),5.5:(0.27,0.02,0.48,0.53),
   6.0:(0.27,0.03,0.48,0.51),6.5:(0.31,0.1,0.42,0.44),7.0:(0.36,0.16,0.31,0.38),7.5:(0.39,0.22,0.25,0.31),8.0:(0.41,0.27,0.2,0.26),8.5:(0.41,0.3,0.2,0.23),
   9.0:(0.41,0.33,0.18,0.2),9.5:(0.41,0.36,0.18,0.18),10.0:(0.41,0.39,0.18,0.15),10.5:(0.41,0.4,0.18,0.14),11.0:(0.4,0.41,0.18,0.14),11.5:(0.39,0.41,0.2,0.14),12.0:(0.39,0.4,0.2,0.15)}
def wy(b): return round(b[1]+b[3]+0.01,2)
def K(f):
    return [dict(t=t,**dict(zip("xywh",f(t)))) for t in T]
wk=K(lambda t:W[t])
water=K(lambda t:(0,max(wy(W[t]),0.5) if t>=3.0 else wy(W[t]),1,round(1-(max(wy(W[t]),0.5) if t>=3.0 else wy(W[t])),2)))
c={"mediaId":5201,"level":"A","keyWord":"reflect","defaultVoice":"female",
 "taps":[
  {"phrase":"to touch the water","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to walk away","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to reflect the sky","target":"the water","voice":"female","keys":water}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.5,"y":0.12,"voice":"female"},{"word":"a woman","x":0.52,"y":0.37,"voice":"female"},
          {"word":"a mountain","x":0.78,"y":0.46,"voice":"female"},{"word":"water","x":0.5,"y":0.8,"voice":"female"}],
 "question":"What is the woman touching?",
 "answer":["She","is","touching","the","water."],
 "answerVoice":"female",
 "notes":"Only one person; two phrases on the woman, one on the water (which mirrors her, the mountain and the sky). Woman box = her real body above the waterline only; the water box starts just below her feet, so her mirror image belongs to the water. 'to walk away' happens from about 7 s on."}
json.dump(c,open('content/5201.json','w'),indent=1)
