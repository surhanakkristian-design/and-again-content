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
woman={0.0:(0.53,0.4,1,1),0.5:(0.5,0.38,1,1),1.0:(0.62,0.5,1,1),1.5:(0.4,0.05,1,1),2.0:(0.3,0.19,1,1),2.5:(0.3,0.04,1,1),
 3.0:(0.12,0.33,0.66,1),3.5:(0.06,0.32,0.65,1),4.0:(0.03,0.3,0.65,1),4.5:(0.13,0.28,0.73,1),5.0:(0.18,0.3,0.8,1),
 5.5:(0.16,0.26,0.87,1),6.0:(0.04,0.24,0.95,1),6.5:(0,0.07,0.62,1),7.0:(0,0.17,0.67,1),7.5:(0,0.22,0.6,1),
 8.0:(0,0.25,0.61,1),8.5:(0,0.26,0.6,1),9.0:(0,0.28,0.6,1),9.5:(0.06,0.33,0.6,1),10.0:(0.15,0.32,0.68,1),
 10.5:(0.15,0.37,0.74,1),11.0:(0.04,0.37,0.81,1),11.5:(0.1,0.39,0.92,1),12.0:(0.2,0.4,0.97,1)}
lock={6.5:(0.82,0.62,1,0.8),7.0:(0.68,0.56,0.86,0.71),7.5:(0.61,0.55,0.79,0.7),8.0:(0.62,0.54,0.8,0.68),
 8.5:(0.61,0.58,0.79,0.72),9.0:(0.61,0.6,0.79,0.76),9.5:(0.61,0.6,0.79,0.76)}
tree={10.5:(0.52,0.1,0.74,0.33),11.0:(0.44,0.1,0.63,0.34),11.5:(0.36,0.1,0.54,0.34),12.0:(0.28,0.1,0.47,0.34)}
c={"mediaId":5449,"level":"B","keyWord":"doorway","defaultVoice":"female",
 "taps":[
  {"phrase":"to turn a huge iron key","target":"the woman","voice":"female","keys":K(woman)},
  {"phrase":"to dangle from an iron bolt","target":"the padlock","voice":"female","keys":K(lock)},
  {"phrase":"to tower over the courtyard","target":"the cypress tree","voice":"female","keys":K(tree)}],
 "stillS":12.0,
 "nouns":[{"word":"a doorway","x":0.18,"y":0.08,"voice":"female"},
  {"word":"a cypress tree","x":0.38,"y":0.2,"voice":"female"},
  {"word":"wisteria","x":0.65,"y":0.36,"voice":"female"},
  {"word":"gravel","x":0.72,"y":0.7,"voice":"female"}],
 "question":"Where is the woman standing?",
 "answer":["She","is","standing","in","the","doorway."],
 "answerVoice":"female",
 "notes":"Only one person, so targets are woman, padlock (6.5-9.5 s) and cypress (10.5-12 s). 0-1.0 s only her hand/arm is visible (box on hand+arm). 'a doorway' pill sits on the stone arch of the opening at the top-left; the opening itself is filled by the courtyard view. At 9.0-9.5 s her hand on the door reaches just past her box edge so it does not touch the padlock box."}
json.dump(c,open('content/5449.json','w'),indent=1)
