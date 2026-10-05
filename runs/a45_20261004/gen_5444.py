import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; x=max(0,x);y=max(0,y);x2=min(1,x2);y2=min(1,y2)
            out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
pink={0.0:(0,0.28,0.53,0.98),0.5:(0,0.26,0.58,0.97),1.0:(0,0.28,0.74,0.66),1.5:(0.18,0.2,0.95,0.56),
 2.0:(0.36,0.23,1,0.74),2.5:(0.36,0.17,1,0.72),7.0:(0,0.53,0.18,0.77),7.5:(0,0.38,0.17,0.67),8.0:(0,0.4,0.15,0.68),
 8.5:(0,0.26,0.1,0.67),9.5:(0,0.27,0.16,0.86),10.0:(0,0.28,0.26,0.74),10.5:(0.08,0.3,0.32,0.74),
 11.0:(0.08,0.31,0.39,0.9),11.5:(0.14,0.31,0.39,0.9),12.0:(0.05,0.31,0.34,0.77)}
green={0.0:(0.56,0,1,0.99),0.5:(0.6,0,1,0.66),1.0:(0.78,0,1,0.67),3.0:(0.21,0.31,0.49,0.67),3.5:(0.16,0.22,0.42,0.64),
 4.0:(0.16,0.14,0.39,0.5),4.5:(0.13,0.13,0.39,0.34),5.0:(0.2,0.14,0.45,0.37),5.5:(0.27,0.17,0.57,0.54),
 6.0:(0.03,0.18,0.34,0.49),6.5:(0.05,0.23,0.37,0.48),7.0:(0,0.25,0.31,0.47),7.5:(0.18,0.28,0.41,0.52),
 8.0:(0.16,0.3,0.4,0.53),8.5:(0.1,0.19,0.31,0.55),9.0:(0.04,0.32,0.32,0.69),9.5:(0.17,0.31,0.4,0.73),
 10.0:(0.26,0.22,0.55,0.67),10.5:(0.33,0.23,0.54,0.67),11.0:(0.4,0.24,0.55,0.72),11.5:(0.4,0.15,0.56,0.72),12.0:(0.34,0.24,0.6,0.72)}
scarf={2.0:(0,0.13,0.17,0.59),2.5:(0.04,0.09,0.26,0.54),4.0:(0,0.27,0.15,0.84),4.5:(0,0.35,0.44,0.82),
 5.0:(0,0.38,0.35,0.9),5.5:(0,0.26,0.18,0.84),6.0:(0.82,0.18,1,0.47),6.5:(0.82,0.23,1,0.47),7.0:(0.79,0.24,0.97,0.43)}
c={"mediaId":5444,"level":"B","keyWord":"cooperate","defaultVoice":"female",
 "taps":[
  {"phrase":"to wear a red headscarf","target":"the woman in the headscarf","voice":"female","keys":K(scarf)},
  {"phrase":"to wear a cable-knit jumper","target":"the man in green","voice":"male","keys":K(green)},
  {"phrase":"to have dyed pink hair","target":"the pink-haired woman","voice":"female","keys":K(pink)}],
 "stillS":9.0,
 "nouns":[{"word":"passers-by","x":0.52,"y":0.36,"voice":"female"},
  {"word":"a giant jigsaw","x":0.5,"y":0.63,"voice":"female"},
  {"word":"floor tiles","x":0.35,"y":0.92,"voice":"female"}],
 "question":"What are the young people doing?",
 "answer":["They","are","cooperating","to","build","a","giant","jigsaw."],
 "answerVoice":"female",
 "notes":"All three phrases are states: nearly every action (lifting, laying, pushing pieces, high fives) is shared by several people. Green man's legs pass behind the headscarf woman at 4.5-5.0 s: boxes split horizontally there. Pink-haired woman only partly at the left edge 7.0-9.5 s (off at 9.0, only a sliver of arm/jeans)."}
json.dump(c,open('content/5444.json','w'),indent=1)
