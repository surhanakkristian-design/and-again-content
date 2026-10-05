import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
W={0.0:(0.29,0.25,0.54,0.63),0.5:(0.28,0.24,0.55,0.62),1.0:(0.28,0.24,0.54,0.62),1.5:(0.28,0.24,0.54,0.62),
 2.0:(0.30,0.23,0.54,0.66),2.5:(0.14,0.09,0.80,0.86),3.0:(0.0,0.0,0.82,1.0),3.5:(0.0,0.14,0.90,0.86),
 4.0:(0.0,0.20,0.92,0.80),4.5:(0.0,0.31,1.0,0.69),5.0:(0.0,0.36,1.0,0.64),5.5:(0.0,0.30,1.0,0.70),
 6.0:(0.0,0.37,0.98,0.54),6.5:(0.02,0.37,0.98,0.53),7.0:(0.0,0.39,1.0,0.48),7.5:(0.0,0.41,0.94,0.42),
 8.0:(0.0,0.47,0.97,0.37),8.5:(0.0,0.47,1.0,0.36),9.0:(0.0,0.47,1.0,0.34),9.5:(0.0,0.47,1.0,0.34),10.0:(0.0,0.47,1.0,0.33)}
k=keys(W)
c={"mediaId":5356,"level":"B","keyWord":"yoga","defaultVoice":"female",
 "taps":[
  {"phrase":"to fold forward with straight legs","target":"the woman","voice":"female","keys":k},
  {"phrase":"to raise both arms overhead","target":"the woman","voice":"female","keys":k},
  {"phrase":"to stretch along her front leg","target":"the woman","voice":"female","keys":k}],
 "stillS":10.0,
 "nouns":[{"word":"the sun","x":0.60,"y":0.18,"voice":"female"},{"word":"the skyline","x":0.25,"y":0.31,"voice":"female"},
          {"word":"flowerpots","x":0.30,"y":0.45,"voice":"female"},{"word":"a yoga mat","x":0.62,"y":0.79,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","practising","yoga","on","a","rooftop."],
 "answerVoice":"female",
 "notes":"Only one person; all three phrases on the woman (the sun sits inside/behind her outline in most frames, so it was not used as a separate target). British spelling 'practising'."}
json.dump(c,open('content/5356.json','w'),indent=1)
