import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
G={0.0:(0.13,0.27,0.42,0.45),0.5:(0.22,0.27,0.38,0.50),1.0:(0.08,0.27,0.58,0.68),1.5:(0.33,0.29,0.48,0.65),2.0:(0.40,0.31,0.34,0.49),2.5:(0.38,0.31,0.37,0.49),
   3.0:(0.25,0.31,0.42,0.62),3.5:(0.0,0.13,0.52,0.86),4.0:(0.12,0.23,0.55,0.77),4.5:(0.15,0.19,0.54,0.81),5.0:(0.17,0.12,0.83,0.88),5.5:(0.20,0.17,0.80,0.83),
   6.0:(0.31,0.05,0.69,0.72),6.5:(0.32,0.17,0.48,0.75),7.0:(0.33,0.50,0.40,0.50),7.5:(0.34,0.38,0.33,0.60),8.0:(0.39,0.40,0.18,0.47),8.5:(0.38,0.33,0.18,0.53),9.0:(0.40,0.34,0.18,0.63)}
N={0.0:(0.72,0.17,0.28,0.61),0.5:(0.67,0.23,0.33,0.57),1.0:(0.69,0.18,0.31,0.77),1.5:(0.82,0.19,0.18,0.45),2.0:(0.75,0.19,0.25,0.63),2.5:(0.76,0.23,0.24,0.60),
   3.0:(0.68,0.25,0.32,0.70),3.5:(0.53,0.17,0.47,0.80),4.0:(0.68,0.39,0.32,0.56),4.5:(0.70,0.64,0.30,0.36),
   6.0:(0.0,0.40,0.30,0.60),6.5:(0.0,0.35,0.31,0.60),7.0:(0.0,0.35,0.31,0.65),7.5:(0.71,0.38,0.29,0.60),8.0:(0.58,0.40,0.26,0.47),8.5:(0.57,0.29,0.22,0.57),9.0:(0.59,0.32,0.22,0.65)}
c={"mediaId":72,"level":"A","keyWord":"basketball","defaultVoice":"female",
 "taps":[
  {"phrase":"to bounce a basketball","target":"the girl","voice":"female","keys":keys(G)},
  {"phrase":"to jump very high","target":"the girl","voice":"female","keys":keys(G)},
  {"phrase":"to wear glasses","target":"the man with glasses","voice":"male","keys":keys(N)}],
 "stillS":5.0,
 "nouns":[{"word":"the sky","x":0.22,"y":0.06,"voice":"female"},{"word":"a basketball","x":0.33,"y":0.20,"voice":"female"},
          {"word":"a net","x":0.75,"y":0.26,"voice":"female"},{"word":"a girl","x":0.58,"y":0.60,"voice":"female"}],
 "question":"What is the girl doing?",
 "answer":["She","is","playing","basketball","with","two","men."],
 "answerVoice":"female",
 "notes":"Two targets only: the big man has nothing that only he does (both men wear blue shirts and headbands), so the girl has two phrases. 'to wear glasses' is a state. Man with glasses is off at 5.0-5.5 (5.5 shows a blue player from behind with the head hidden). In the hug (8.0-9.0) the girl's box is narrow (0.18) between the two men. At 4.5 her raised elbow is cut to keep clear of the man's box."}
json.dump(c,open('content/72.json','w'),indent=1)
