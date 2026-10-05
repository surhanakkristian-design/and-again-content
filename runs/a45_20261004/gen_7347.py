import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
W={0.2:(0.51,0.31,0.24,0.23),0.7:(0.53,0.33,0.24,0.21),1.2:(0.47,0.34,0.29,0.23),1.7:(0.48,0.36,0.30,0.22),
   2.2:(0.47,0.36,0.31,0.22),2.7:(0.48,0.38,0.31,0.22),3.2:(0.47,0.40,0.30,0.21),3.7:(0.49,0.40,0.31,0.23)}
split={0.2:0.56,0.7:0.56,1.2:0.57,1.7:0.58,2.2:0.58,2.7:0.60,3.2:0.61,3.7:0.63}
WH={t:(0.24,split[t],0.43,round(0.91-split[t],2)) for t in T}
H={t:((0.03,0.46,0.20,0.14) if t<2.0 else (0.03,0.43,0.20,0.15)) for t in T}
c={"mediaId":7347,"level":"B","keyWord":"a mill","defaultVoice":"female",
 "taps":[
  {"phrase":"to swing on a rope","target":"the woman","voice":"female","keys":[k(t,W[t]) for t in T]},
  {"phrase":"to turn under rushing water","target":"the waterwheel","voice":"female","keys":[k(t,WH[t]) for t in T]},
  {"phrase":"to stand harnessed to a cart","target":"the horse","voice":"female","keys":[k(t,H[t]) for t in T]}],
 "stillS":1.2,
 "nouns":[{"word":"flour","x":0.56,"y":0.18,"voice":"female"},
          {"word":"a mill","x":0.25,"y":0.36,"voice":"female"},
          {"word":"a horse","x":0.13,"y":0.52,"voice":"female"},
          {"word":"a waterwheel","x":0.42,"y":0.74,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","swinging","on","a","rope","over","the","waterwheel."],
 "answerVoice":"female",
 "notes":"Single shot. Waterwheel box top is cut along the line under the woman's sack (she swings down over the wheel at 2.7-3.7), so the top rim is outside the box late. Horse is small and stands still at the far left with the cart edge. 'a mill' pill sits on the stone wall of the building; flour pill on the white cloud."}
json.dump(c,open('content/7347.json','w'),indent=1)
