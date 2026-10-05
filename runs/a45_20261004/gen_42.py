import json
T=[i*0.5 for i in range(13)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0,0.18,0.52),0.5:(0,0.02,0.33,0.50),1.0:(0,0,0.60,0.54),1.5:(0.03,0.13,0.90,0.41),2.0:(0.20,0.15,0.72,0.37),3.0:(0.18,0.19,0.70,0.37),3.5:(0.18,0.19,0.74,0.38),
     4.0:(0.03,0.02,0.86,0.56),4.5:(0.07,0,0.72,0.58),5.0:(0,0.04,0.50,0.54),5.5:(0,0.16,0.20,0.40)}
pen={0.0:(0.40,0.52,0.20,0.14),0.5:(0.40,0.52,0.20,0.14),1.0:(0.38,0.54,0.20,0.14),1.5:(0.36,0.54,0.20,0.14),2.0:(0.35,0.52,0.20,0.14),2.5:(0.41,0.48,0.26,0.30),
     3.0:(0.33,0.56,0.20,0.14),3.5:(0.33,0.57,0.20,0.14),4.0:(0.34,0.58,0.20,0.14),4.5:(0.33,0.58,0.20,0.14),5.0:(0.34,0.59,0.20,0.14),5.5:(0.34,0.58,0.20,0.14),6.0:(0.34,0.57,0.20,0.14)}
pap={0.0:(0,0.66,1,0.24),0.5:(0,0.66,1,0.24),1.0:(0,0.68,1,0.22),1.5:(0,0.68,1,0.22),2.0:(0,0.66,1,0.24),2.5:(0,0.03,1,0.44),3.0:(0,0.70,1,0.24),3.5:(0,0.71,1,0.23),
     4.0:(0,0.72,1,0.22),4.5:(0,0.72,1,0.22),5.0:(0,0.73,1,0.22),5.5:(0,0.72,1,0.22),6.0:(0,0.71,1,0.24)}
c={"mediaId":42,"level":"A","keyWord":"exam","defaultVoice":"male",
 "taps":[{"phrase":"to look at his exam","target":"the man","voice":"male","keys":keys(man)},
         {"phrase":"to lie on the papers","target":"the pen","voice":"male","keys":keys(pen)},
         {"phrase":"to cover the whole table","target":"the papers","voice":"male","keys":keys(pap)}],
 "stillS":6.0,
 "nouns":[{"word":"a door","x":0.12,"y":0.33,"voice":"male"},{"word":"a chair","x":0.70,"y":0.47,"voice":"male"},{"word":"a pen","x":0.43,"y":0.63,"voice":"male"},{"word":"papers","x":0.50,"y":0.83,"voice":"male"}],
 "question":"What is the man looking at?",
 "answer":["He","is","looking","at","his","exam."],"answerVoice":"male",
 "notes":"Dark clip. The pen lies on the papers, so the papers box is only the part of the pile below the pen box (at the 2.5 s close-up: the part above the pen). The man is a sliver at the left edge at 0.0 and 5.5 s, gone at 2.5 and 6.0 s. 'his exam' = the papers on the table (key word; the picture alone shows printed and handwritten sheets). The door on the left is dark but recognisable in the still."}
json.dump(c,open('content/42.json','w'),indent=1,ensure_ascii=False)
