import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={0.0:(0.18,0.02,0.95,0.49),0.5:(0.15,0.02,0.98,0.49),1.0:(0.15,0.02,0.95,0.49),1.5:(0.15,0.03,0.98,0.5),
 2.0:(0.1,0.08,0.9,1.0),2.5:(0.12,0.08,0.86,1.0),3.0:(0.1,0.1,0.95,1.0),3.5:(0.15,0.12,0.98,1.0),
 7.5:(0.0,0.25,0.37,1.0),8.0:(0.0,0.45,0.1,1.0)}
syr={0.0:(0.48,0.5,0.88,0.64),0.5:(0.52,0.5,0.88,0.64),1.0:(0.5,0.5,0.86,0.64),1.5:(0.48,0.51,0.86,0.65),
 4.5:(0.47,0.47,0.81,0.61),5.0:(0.54,0.47,0.9,0.61),5.5:(0.55,0.48,0.85,0.62),6.0:(0.84,0.55,1.0,0.7),
 6.5:(0.56,0.45,0.84,0.6),7.0:(0.53,0.47,0.84,0.61)}
woman={5.5:(0.3,0.12,0.99,0.47),6.0:(0.24,0.14,0.83,1.0)}
c={"mediaId":4981,"level":"B","keyWord":"vaccine","defaultVoice":"male",
 "taps":[
  {"phrase":"to grin over his shoulder","target":"the young man","voice":"male","keys":keys(man)},
  {"phrase":"to pierce the skin","target":"the syringe","voice":"male","keys":keys(syr)},
  {"phrase":"to clench her fist","target":"the woman in the grey top","voice":"female","keys":keys(woman)}],
 "stillS":2.0,
 "nouns":[{"word":"a tank top","x":0.25,"y":0.62,"voice":"male"},
          {"word":"a window","x":0.80,"y":0.27,"voice":"male"},
          {"word":"a nurse","x":0.82,"y":0.43,"voice":"female"},
          {"word":"a bin","x":0.77,"y":0.76,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","getting","a","vaccine","in","his","upper","arm."],
 "answerVoice":"male",
 "notes":"Syringe sits on the arm: at 0.0-1.5 the young man's box is cut above it (head/shoulders), at 5.5 the grey-top woman's box is cut above it (head + raised fist). At 6.0 the syringe is only a small piece in the nurse's hand at the right edge. The young man reappears at the left of the line-up (7.5) and as a sliver of arm at the left edge (8.0). The group at the end also hold fists on their arms, but against their own plasters, not clenched and raised like the grey-top woman. 'a nurse' = the nurse in blue scrubs in the background (2.0)."}
json.dump(c,open('content/4981.json','w'),indent=1)
