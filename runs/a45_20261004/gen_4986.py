import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=v; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(0,.26,.40,1),0.5:(0,.26,.40,1),1.0:(0,.26,.32,1),1.5:(0,.27,.30,1),2.0:(0,.27,.30,1),
   3.5:(.24,.40,1,1),4.0:(.40,.42,1,.88),4.5:(.68,.22,1,.95),5.0:(.62,.33,1,1),5.5:(.66,.33,1,1),6.0:(.62,.29,1,1),
   6.5:(.72,.22,1,.88),7.0:(.74,.30,1,1),7.5:(.70,.30,1,1),8.0:(.62,.32,1,1),8.5:(.76,.38,1,.95),9.0:(.80,.40,1,1),9.5:(.82,.40,1,1),10.0:(.78,.41,1,.93)}
M={0.0:(.41,.16,.95,.80),0.5:(.41,.16,.95,.80),1.0:(.33,.16,.95,.90),1.5:(.31,.17,.95,.75),2.0:(.31,.17,.92,.90),
   2.5:(.12,.02,1,.98),3.0:(.25,.28,1,1),4.5:(0,.19,.36,.92),5.0:(0,.30,.40,1),5.5:(0,.33,.34,1),6.0:(0,.30,.33,1),
   6.5:(0,.30,.32,.75),7.0:(0,.62,.30,.82),7.5:(0,.64,.28,.80),8.0:(0,.44,.28,.70),8.5:(0,.32,.32,.95),9.0:(0,.36,.25,1),9.5:(0,.37,.22,1),10.0:(0,.38,.26,.88)}
c={"mediaId":4986,"level":"A","keyWord":"bright","defaultVoice":"female",
 "taps":[
  {"phrase":"to hold a drill","target":"the woman","voice":"female","keys":K(W)},
  {"phrase":"to touch the ceiling","target":"the man","voice":"male","keys":K(M)},
  {"phrase":"to give a thumbs up","target":"the woman","voice":"female","keys":K(W)}],
 "stillS":10.0,
 "nouns":[{"word":"the ceiling","x":0.30,"y":0.09,"voice":"female"},
          {"word":"screens","x":0.49,"y":0.48,"voice":"female"},
          {"word":"a man","x":0.13,"y":0.62,"voice":"male"},
          {"word":"a woman","x":0.85,"y":0.55,"voice":"female"}],
 "question":"What colour are the screens?",
 "answer":["The","screens","are","bright","blue."],
 "answerVoice":"female",
 "notes":"Man and woman overlap at 0.0-2.0 (she stands in front of him); boxes split vertically, so her drill hand / thumb partly falls in his box. Thumbs up only at t=2.0. Man touches the ceiling camera at 2.5-3.0. Slots: two ceiling cameras at 10.0, so no camera noun. 'bright' is an adjective, used in the answer."}
json.dump(c,open('content/4986.json','w'),indent=1)
