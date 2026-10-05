import json
T=[i*0.5 for i in range(19)]
def K(lst):
    out=[]
    for t,v in zip(T,lst):
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
N=None
sk=[(0.30,0.25,0.50,0.44),(0.08,0.0,0.92,0.67),(0.12,0.10,0.80,0.60),(0.20,0.20,0.57,0.52),(0.24,0.24,0.50,0.50)]+[N]*14
ball=[N]*7+[(0.34,0.22,0.18,0.14),(0.30,0.10,0.18,0.14),(0.37,0.26,0.18,0.14),(0.45,0.55,0.18,0.14)]+[N]*8
cap=[N]*12+[(0.0,0.32,0.36,0.64),(0.0,0.32,0.50,0.65),(0.0,0.37,0.52,0.60),(0.0,0.40,0.54,0.58),(0.0,0.39,0.56,0.58),(0.0,0.39,0.47,0.58),(0.0,0.36,0.20,0.55)]
c={"mediaId":5390,"level":"A","keyWord":"youth","defaultVoice":"male",
 "taps":[
  {"phrase":"to ride a skateboard","target":"the boy on the skateboard","voice":"male","keys":K(sk)},
  {"phrase":"to go into the basket","target":"the ball","voice":"male","keys":K(ball)},
  {"phrase":"to wear a purple cap","target":"the boy in the purple cap","voice":"male","keys":K(cap)}],
 "stillS":6.0,
 "nouns":[{"word":"a phone","x":0.62,"y":0.70,"voice":"male"},
          {"word":"a backpack","x":0.68,"y":0.92,"voice":"male"},
          {"word":"a purple cap","x":0.18,"y":0.41,"voice":"male"}],
 "question":"What are the boys doing?",
 "answer":["They","are","looking","at","a","phone."],
 "answerVoice":"male",
 "notes":"Three shots: skatepark (0-2.5), basketball (3-5.5), phone huddle (6-9). Skater hidden behind another boy at 2.5 (off). Ball small: min-size boxes 3.5-5.0; at 5.0 it is on the ground behind a boy's legs. Key word 'youth' is abstract, not placed as a noun. Cast looks young teens. 'to wear a purple cap' is a state: several boys point at the phone, so pointing is not unique. Only 3 nouns: many hoodies/caps, so only the purple cap is labelled."}
json.dump(c,open("content/5390.json","w"),indent=1)
