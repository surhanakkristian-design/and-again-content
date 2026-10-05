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
woman={0.0:(0.26,0.39,0.82,1),0.5:(0.27,0.38,0.84,1),1.0:(0.28,0.38,0.83,1),1.5:(0.29,0.39,0.84,1),2.0:(0.29,0.39,0.84,1),
 2.5:(0.16,0.26,0.97,1),3.0:(0.36,0.29,0.98,1),3.5:(0.38,0.26,1,1),4.0:(0.24,0.24,1,1),4.5:(0.33,0.27,1,1),5.0:(0.33,0.29,1,1),
 5.5:(0.38,0.29,1,1),6.0:(0.45,0.3,1,1),6.5:(0.53,0.3,1,1),7.0:(0.6,0.32,1,1),7.5:(0.24,0.27,0.97,1),8.0:(0.28,0.27,0.97,1),
 8.5:(0.26,0.33,0.95,1),9.0:(0.28,0.32,0.97,1),9.5:(0.29,0.3,0.98,1),10.0:(0.24,0.3,0.95,1),10.5:(0.32,0.3,0.98,1),
 11.0:(0.3,0.31,0.96,1),11.5:(0.25,0.31,0.95,1),12.0:(0.23,0.3,0.95,1)}
gull={8.0:(0,0.32,0.27,0.5),8.5:(0,0,0.25,0.6)}
bus={0.0:(0,0.39,0.24,0.83),0.5:(0,0.29,0.24,0.93),1.0:(0,0.22,0.25,0.97),1.5:(0,0.22,0.25,0.97),2.0:(0,0.23,0.25,0.96)}
c={"mediaId":5446,"level":"B","keyWord":"misty","defaultVoice":"female",
 "taps":[
  {"phrase":"to snack on chips","target":"the woman","voice":"female","keys":K(woman)},
  {"phrase":"to swoop towards her chips","target":"the seagull","voice":"female","keys":K(gull)},
  {"phrase":"to drive along the street","target":"the double-decker bus","voice":"female","keys":K(bus)}],
 "stillS":6.0,
 "nouns":[{"word":"mist","x":0.42,"y":0.36,"voice":"female"},
  {"word":"a lake","x":0.22,"y":0.58,"voice":"female"},
  {"word":"a raincoat","x":0.8,"y":0.7,"voice":"female"},
  {"word":"ferns","x":0.22,"y":0.82,"voice":"female"}],
 "question":"What is she looking at?",
 "answer":["She","is","looking","at","a","misty","valley."],
 "answerVoice":"female",
 "notes":"Seagull only visible 8.0-8.5 s (brief). Bus only in the first shot 0-2 s, partly hidden behind the phone box; it moves between frames. Question refers to the hillside shot 2.5-7 s. Gull wing tip at 8.5 s (x up to 0.36, top) left outside its box to avoid the woman's box."}
json.dump(c,open('content/5446.json','w'),indent=1)
