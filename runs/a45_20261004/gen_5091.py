import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
man={0.0:(.1,.07,1,.7),0.5:(.05,.16,.98,.72),1.0:(.05,.14,.95,.72),1.5:(.05,.18,.96,.72),2.0:(0,.2,.9,.7),2.5:(.03,.19,.8,1),
 3.0:(.18,.43,.58,.93),3.5:(.18,.41,.6,.93),4.0:(.13,.27,.52,.95),4.5:(.11,.25,.56,.98),5.0:(.06,.24,.56,1)}
bike={0.0:(.18,.7,.95,1),0.5:(.22,.72,.97,1),1.0:(.15,.72,.97,1),1.5:(.22,.72,1,1),2.0:(.3,.7,.95,1),2.5:(.8,.75,1,1)}
red={6.5:(0,.48,.17,.8),7.0:(0,.5,.21,.8),7.5:(.02,.52,.24,.74),8.0:(.07,.53,.27,.7),8.5:(.12,.54,.31,.69),9.0:(.16,.55,.34,.69)}
c={"mediaId":5091,"level":"A","keyWord":"motorbike","defaultVoice":"male",
 "taps":[
  {"phrase":"to smile at the camera","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to have a round light","target":"the green motorbike","voice":"male","keys":keys(bike)},
  {"phrase":"to wear a red helmet","target":"the rider in the red helmet","voice":"male","keys":keys(red)}],
 "stillS":4.0,
 "nouns":[{"word":"a man","x":0.27,"y":0.40,"voice":"male"},
          {"word":"a motorbike","x":0.55,"y":0.66,"voice":"male"},
          {"word":"the sea","x":0.85,"y":0.45,"voice":"male"},
          {"word":"the sky","x":0.50,"y":0.12,"voice":"male"}],
 "question":"What is the man riding?",
 "answer":["He","is","riding","a","motorbike."],"answerVoice":"male",
 "notes":"Three shots: man on a small green motorbike in town (0-2.5), man sitting on a big black motorbike by the sea (3.0-5.0), group of helmeted riders (5.5-9.0). The man is off in the group shot (cannot tell if he is among the riders). Man and green motorbike boxes are split horizontally (his hands on the bars sit near the split line). The red-helmet rider is small at 8.0-9.0 and close to other riders; at 6.5 only partly visible at the left edge. Phrase 2 is a state (round headlight); no action fits the bike alone. Smile at the camera is clearest at 1.5-2.5; at 3.0-5.0 he smiles looking aside."}
json.dump(c,open('content/5091.json','w'),indent=1)
