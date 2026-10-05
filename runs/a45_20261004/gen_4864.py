import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
w={0.0:(0.15,0.24,0.67,0.54),0.5:(0.15,0.23,0.69,0.55),1.0:(0.14,0.22,0.71,0.55),1.5:(0.12,0.22,0.74,0.57),
2.0:(0.48,0.30,0.44,0.52),2.5:(0.50,0.29,0.48,0.53),3.0:(0.53,0.31,0.43,0.55),3.5:(0.53,0.32,0.44,0.53),
4.0:(0.02,0.28,0.81,0.52),4.5:(0.08,0.30,0.56,0.52),5.0:(0.20,0.39,0.72,0.56),5.5:(0.58,0.26,0.40,0.50),
6.0:(0.62,0.73,0.38,0.24),6.5:(0.54,0.72,0.46,0.28),7.0:(0.19,0.55,0.81,0.45),7.5:(0.19,0.55,0.81,0.45),
8.0:(0.62,0.66,0.38,0.34),8.5:(0.10,0.27,0.90,0.58),9.0:(0.02,0.27,0.95,0.63)}
m={2.0:(0.30,0.25,0.18,0.20),2.5:(0.31,0.25,0.19,0.20),3.0:(0.31,0.26,0.22,0.24),3.5:(0.32,0.27,0.21,0.24)}
b={4.5:(0.64,0.26,0.22,0.24),5.0:(0.04,0.24,0.86,0.15),5.5:(0.0,0.27,0.58,0.40)}
c={"mediaId":4864,"level":"A","keyWord":"uniform","defaultVoice":"female",
"taps":[
 {"phrase":"to raise one finger","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to smile behind the woman","target":"the man in the black T-shirt","voice":"male","keys":keys(m)},
 {"phrase":"to carry a big box","target":"the man with the box","voice":"male","keys":keys(b)}],
"stillS":6.5,
"nouns":[{"word":"a plant","x":0.22,"y":0.25,"voice":"female"},
 {"word":"a trumpet","x":0.17,"y":0.35,"voice":"female"},
 {"word":"a uniform","x":0.38,"y":0.55,"voice":"female"},
 {"word":"a hand","x":0.64,"y":0.83,"voice":"female"}],
"question":"What is the second man carrying?",
"answer":["He","is","carrying","a","big","box."],
"answerVoice":"male",
"notes":"Question says 'the second man' (the box man comes after the man in the black T-shirt). Band members all play instruments, so no band phrase (would fit several players). The man in the black T-shirt is visible only 2.0-3.5 s and stands right behind the woman: boxes split (his = head/shoulders left of her head). Man with the box 4.5-5.5 s; at 5.0 s his box is a thin strip above her head, at 4.5 s her shoulder is cut at x 0.64. 'a uniform' pill on the trumpet player in front; the other players also wear uniforms but no other noun names them."}
json.dump(c,open('content/4864.json','w'),indent=1)
