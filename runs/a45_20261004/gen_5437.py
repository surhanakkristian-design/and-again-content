import json
T=[i*0.5 for i in range(25)]
w={0.0:(0.24,0.44,0.42,0.56),0.5:(0.20,0.43,0.43,0.57),1.0:(0.21,0.43,0.40,0.57),1.5:(0.22,0.44,0.44,0.56),
2.0:(0.21,0.43,0.49,0.57),2.5:(0.20,0.45,0.55,0.55),3.0:(0.22,0.44,0.62,0.56),3.5:(0.20,0.44,0.56,0.56),
4.0:(0.26,0.43,0.53,0.57),4.5:(0.27,0.42,0.52,0.58),5.0:(0.18,0.41,0.78,0.59),5.5:(0.28,0.40,0.50,0.60),
6.0:(0.30,0.43,0.62,0.55),6.5:(0.30,0.45,0.36,0.53),7.0:(0.25,0.47,0.56,0.53),7.5:(0.30,0.48,0.38,0.50),
8.0:(0.42,0.48,0.24,0.42),8.5:(0.38,0.31,0.34,0.32),9.0:(0.27,0.28,0.55,0.45),9.5:(0.24,0.23,0.56,0.49),
10.0:(0.25,0.19,0.52,0.52),10.5:(0.27,0.19,0.51,0.52),11.0:(0.24,0.21,0.53,0.50),11.5:(0.23,0.21,0.55,0.50),12.0:(0.24,0.21,0.52,0.50)}
p={4.0:(0.0,0.55,0.25,0.40),4.5:(0.0,0.54,0.26,0.33),5.0:(0.0,0.52,0.18,0.40),5.5:(0.0,0.28,0.27,0.40),
6.0:(0.0,0.25,0.29,0.45),6.5:(0.0,0.05,0.29,0.40),7.0:(0.0,0.02,1.0,0.44),7.5:(0.0,0.10,1.0,0.37),8.0:(0.0,0.22,1.0,0.25)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,ww,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(ww,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5437,"level":"B","keyWord":"courtyard","defaultVoice":"female",
"taps":[{"phrase":"to stroll among sunflowers","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to raise a braided loaf","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to flutter into the air","target":"the pigeons","voice":"female","keys":keys(p)}],
"stillS":10.0,
"nouns":[{"word":"fairy lights","x":0.45,"y":0.10,"voice":"female"},{"word":"a braided loaf","x":0.55,"y":0.27,"voice":"female"},
{"word":"a courtyard","x":0.20,"y":0.42,"voice":"female"},{"word":"a long table","x":0.50,"y":0.72,"voice":"female"}],
"question":"What is the woman raising?","answer":["She","is","raising","a","braided","loaf."],"answerVoice":"female",
"notes":"The woman leading the camera (0-8.0) is taken to be the same woman who lifts the loaf in the courtyard (8.5-12.0). Pigeons are a scattered flock around her; their box only covers the part of the flock that does not touch her box (left side at 4.0-6.5, the sky above her at 7.0-8.0), off before 4.0 and in the courtyard. 'a courtyard' pill sits on the lawn of the enclosed space left of the woman, verifier please check it reads as the courtyard."}
json.dump(c,open('content/5437.json','w'),indent=1)
