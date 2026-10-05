import json,sys
O=None
W={0.0:(0.02,0.18,0.76,0.82),0.5:(0.04,0.22,0.70,0.78),1.0:(0.0,0.20,0.80,0.80),1.5:(0.06,0.24,0.47,0.76),
 2.0:(0.0,0.20,0.37,0.78),2.5:(0.0,0.20,0.38,0.80),3.0:O,3.5:O,4.0:(0.50,0.33,0.50,0.67),4.5:(0.66,0.28,0.34,0.72),
 5.0:O,5.5:O,6.0:(0.46,0.20,0.54,0.80),6.5:(0.44,0.28,0.56,0.70),7.0:(0.25,0.62,0.75,0.32),7.5:(0.22,0.64,0.78,0.30),
 8.0:(0.05,0.56,0.95,0.34),8.5:(0.05,0.56,0.95,0.36),9.0:(0.0,0.51,0.95,0.44)}
M={0.0:O,0.5:O,1.0:O,1.5:(0.53,0.26,0.32,0.36),2.0:(0.37,0.28,0.26,0.52),2.5:(0.38,0.22,0.34,0.78),3.0:(0.0,0.0,0.56,1.0),
 3.5:(0.0,0.0,0.62,1.0),4.0:(0.0,0.0,0.50,1.0),4.5:(0.0,0.05,0.66,0.95),5.0:O,5.5:O,6.0:(0.0,0.27,0.45,0.73),
 6.5:(0.0,0.40,0.44,0.57),7.0:(0.48,0.38,0.40,0.24),7.5:(0.30,0.38,0.52,0.26),8.0:(0.38,0.31,0.62,0.18),8.5:(0.48,0.33,0.52,0.23),9.0:(0.46,0.33,0.30,0.17)}
def keys(D):
    out=[]
    for t in sorted(D):
        b=D[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
c={"mediaId":5496,"level":"A","keyWord":"adjust","defaultVoice":"female",
 "taps":[{"phrase":"to cook a pancake","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to adjust his tie","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to dance behind her","target":"the man","voice":"male","keys":keys(M)}],
 "stillS":0.0,
 "nouns":[{"word":"a woman","x":0.22,"y":0.56,"voice":"female"},{"word":"cupboards","x":0.62,"y":0.28,"voice":"female"},
  {"word":"knives","x":0.86,"y":0.53,"voice":"female"},{"word":"a pancake","x":0.70,"y":0.79,"voice":"female"}],
 "question":"What is she doing with his tie?","answer":["She","is","adjusting","his","tie."],"answerVoice":"female",
 "notes":"Man and woman overlap at 1.5-2.5 and on the sofa (7.0-9.0): boxes split, woman's box on the sofa covers legs/lower body, man's box his head and torso. 5.0-5.5 hands-only close-up: both off. 3.0-3.5 mug close-up: woman off (only a hand). 'adjust' is the key word, kept in phrase and answer although level A."}
json.dump(c,open('content/5496.json','w'),indent=1)
