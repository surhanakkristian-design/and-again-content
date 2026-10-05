import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
w={0.0:(.12,.26,.8,.88),0.5:(0,.21,.9,1),1.0:(0,.12,.98,1),1.5:(.05,.16,1,1),2.0:(0,.25,.86,1),2.5:(.2,.24,.62,1),
 3.0:(.3,.26,.65,.9),3.5:(.6,.32,.91,.97),4.0:(.62,.33,.9,.92),4.5:(.6,.32,.9,.9),5.0:(.6,.3,.86,.95),5.5:(.55,.29,.82,.8),
 6.0:(.52,.31,.78,.8),6.5:(.3,.18,.95,.9),7.0:(.6,.33,1,1),7.5:(.48,.24,1,.96),8.0:(.44,.28,.81,1),8.5:(.26,.3,.81,1),
 9.0:(0,.27,.81,1),9.5:(.2,.25,.79,1),10.0:(.2,.22,.71,1)}
g={8.0:(.82,.3,1,.48),8.5:(.82,.3,1,.48),9.0:(.82,.3,1,.47),9.5:(.8,.29,.99,.45),10.0:(.72,.25,.9,.42)}
c={"mediaId":5092,"level":"A","keyWord":"helper","defaultVoice":"female",
 "taps":[
  {"phrase":"to carry a big box","target":"the woman","voice":"female","keys":keys(w)},
  {"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":keys(w)},
  {"phrase":"to water the plants","target":"the man in the garden","voice":"male","keys":keys(g)}],
 "stillS":4.0,
 "nouns":[{"word":"a truck","x":0.50,"y":0.12,"voice":"female"},
          {"word":"a helper","x":0.20,"y":0.36,"voice":"female"},
          {"word":"a sofa","x":0.42,"y":0.52,"voice":"female"},
          {"word":"a ladder","x":0.72,"y":0.86,"voice":"female"}],
 "question":"What is the woman carrying?",
 "answer":["She","is","carrying","a","big","box."],"answerVoice":"female",
 "notes":"The men who help with the sofa share every action with the woman (push/pull the sofa) and two of them wear red caps, so no phrase targets them; the background man with a hose (white shirt, red cap) waters the plants at 8.0-10.0. He is also tiny behind the woman's head at 2.0-2.5 but set OFF there (cannot be boxed without cutting her face). His box cuts off the woman's right glove/arm at 8.0-10.0 (split line). 'a helper' pill sits on the man in the red cap inside the truck at 4.0; a second man (black shirt) is right next to him and a green-shirt helper is at the right edge. Smile at the camera is clearest at 2.5 and 8.5-10.0."}
json.dump(c,open('content/5092.json','w'),indent=1)
