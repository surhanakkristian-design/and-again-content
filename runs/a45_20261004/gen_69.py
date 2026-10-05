import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
W={0.0:(0.0,0.02,0.22,0.48),0.5:(0.0,0.0,0.50,0.68),1.0:(0.0,0.0,0.38,0.80),1.5:(0.0,0.0,0.46,0.77),2.0:(0.0,0.0,0.22,0.70),2.5:(0.0,0.0,0.26,0.70),
   4.0:(0.24,0.20,0.47,0.63),4.5:(0.24,0.34,0.48,0.50),5.0:(0.24,0.30,0.48,0.63),5.5:(0.24,0.28,0.48,0.65),6.0:(0.24,0.25,0.48,0.58),
   6.5:(0.24,0.23,0.48,0.60),7.0:(0.24,0.17,0.48,0.77),7.5:(0.26,0.09,0.47,0.85),8.0:(0.25,0.10,0.48,0.74),8.5:(0.24,0.31,0.48,0.53),
   9.0:(0.24,0.17,0.48,0.78),9.5:(0.30,0.11,0.45,0.84),10.0:(0.19,0.10,0.57,0.75)}
M={0.0:(0.68,0.0,0.32,0.63),0.5:(0.78,0.0,0.22,0.60),2.5:(0.78,0.34,0.22,0.32),
   4.0:(0.73,0.29,0.27,0.28),4.5:(0.73,0.30,0.27,0.28),5.0:(0.73,0.30,0.27,0.28),5.5:(0.73,0.30,0.27,0.30),6.0:(0.73,0.31,0.27,0.27),
   6.5:(0.73,0.31,0.27,0.28),7.0:(0.73,0.30,0.27,0.33),7.5:(0.78,0.28,0.22,0.18),8.0:(0.80,0.28,0.20,0.16),8.5:(0.73,0.29,0.27,0.30),
   9.0:(0.73,0.29,0.27,0.33),9.5:(0.76,0.29,0.24,0.36),10.0:(0.77,0.24,0.23,0.38)}
c={"mediaId":69,"level":"B","keyWord":"barbell","defaultVoice":"female",
 "taps":[
  {"phrase":"to lift a heavy barbell","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to have a thick beard","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to bend over the bar","target":"the woman","voice":"female","keys":keys(W)}],
 "stillS":6.0,
 "nouns":[{"word":"a hillside","x":0.17,"y":0.33,"voice":"female"},{"word":"a braid","x":0.50,"y":0.41,"voice":"female"},{"word":"a beard","x":0.90,"y":0.45,"voice":"female"},
          {"word":"a barbell","x":0.80,"y":0.66,"voice":"female"}],
 "question":"What is the blonde woman doing?",
 "answer":["She","is","lifting","a","heavy","barbell."],
 "answerVoice":"female",
 "notes":"Two targets. The man's phrase is a state: his only actions (crouching, watching, cheering) are either shared with the woman's bent stance or need the sound. At 2.5 s only two hands at the right edge are visible; boxed as the man (the woman's hand with the clip is on the left) - verifier may set it off. At 0.5 s only his beard tip and forearm show. 3.0-3.5 s: nobody in the picture. Where the two stand close (4.0-10.0) the boxes are split near x = 0.72-0.76, so her right hand on the bar is cut at some frames. Barbell pill sits on the right plate."}
json.dump(c,open('content/69.json','w'),indent=1)
