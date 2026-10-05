import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
# boxes as x0,y0,x1,y1
W={0.0:(0,.22,.68,1),0.5:(0,.22,.66,1),1.0:(0,.24,.62,1),1.5:(.05,.27,.66,1),2.0:(0,.33,.55,1),
   2.5:(0,.35,.60,1),3.0:(0,.38,.50,1),3.5:(0,.38,.52,1),4.0:(0,.33,.52,1),4.5:(0,.37,.33,1),5.0:(0,.68,.30,1),
   5.5:(.48,.35,1,1),6.0:(.25,.28,1,1),6.5:(.25,.32,1,1),7.0:(.22,.35,1,1),7.5:(.18,.35,1,1),8.0:(.22,.32,1,1),
   8.5:(.40,.32,1,1),9.0:(.32,.43,1,1),9.5:(.10,.42,1,1),10.0:(.12,.26,.82,1)}
M={0.0:(.68,.12,1,.70),0.5:(.66,.12,1,.72),1.0:(.62,.10,1,.78),1.5:(.66,.18,1,.92),2.0:(.57,.13,1,1),10.0:(.82,.26,1,.86)}
B={2.5:(.60,0,1,.88),3.0:(.50,0,.92,.90),3.5:(.52,0,1,.88),4.0:(.52,0,.95,.78),4.5:(.33,0,.85,.84),5.0:(.30,0,.88,.96)}
c={"mediaId":111,"level":"A","keyWord":"boxing","defaultVoice":"female",
 "taps":[{"phrase":"to hit a big bag","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to hold two black pads","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to hang on chains","target":"the big bag","voice":"female","keys":keys(B)}],
 "stillS":4.0,
 "nouns":[{"word":"a bag","x":.70,"y":.45,"voice":"female"},{"word":"a window","x":.42,"y":.20,"voice":"female"},
          {"word":"a woman","x":.28,"y":.45,"voice":"female"},{"word":"a glove","x":.50,"y":.67,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","hitting","a","big","bag."],"answerVoice":"female",
 "notes":"Man (coach) is visible only 0-2.0 s and at the right edge at 10.0 s; at 2.5-4.5 and 9.5 only his pads peek in, marked off. Woman and bag boxes split along a vertical line at 2.5-5.0 s (her punching glove falls in the bag box). The small speed ball (5.5 s on) hangs from a board, not chains. Key word boxing is not a visible noun."}
json.dump(c,open("content/111.json","w"),indent=1)
