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
woman={0.0:(.05,.12,.85,.54),0.5:(.10,.18,.95,.47),1.0:(.56,.10,.98,.98),1.5:(.66,.25,.98,.98),
 2.0:(.55,.06,1,1),2.5:(.60,.06,1,1),3.0:(.62,.09,1,1),3.5:(.60,.09,1,1),4.0:(.62,.07,1,1),
 4.5:(0,0,.5,.62),5.0:(0,0,.6,.6),5.5:(0,0,.68,.58),6.0:(0,0,.4,.82),6.5:(0,0,.4,.85),
 7.0:(.18,.25,.82,.76),7.5:(.28,.30,.76,.64),8.0:(.24,.31,.62,.62),8.5:(.25,.34,.60,.58),9.0:(.30,.40,.55,.62)}
baby={0.0:(0,.55,1,1),0.5:(.12,.48,.86,.97),1.0:(.02,.02,.55,.85),1.5:(.02,.25,.65,.98)}
girl={4.5:(.5,0,1,1),5.0:(.6,.1,1,1),5.5:(.68,.12,1,1),6.0:(.4,0,1,1),6.5:(.4,0,1,1)}
c={"mediaId":5089,"level":"A","keyWord":"mother","defaultVoice":"female",
 "taps":[
  {"phrase":"to cook a pancake","target":"the woman","voice":"female","keys":keys(woman)},
  {"phrase":"to hug her mother","target":"the baby","voice":"female","keys":keys(baby)},
  {"phrase":"to have a sore knee","target":"the girl on the floor","voice":"female","keys":keys(girl)}],
 "stillS":3.0,
 "nouns":[{"word":"a mother","x":0.82,"y":0.33,"voice":"female"},
          {"word":"a fridge","x":0.25,"y":0.25,"voice":"female"},
          {"word":"a pancake","x":0.28,"y":0.70,"voice":"female"}],
 "question":"What is the mother making?",
 "answer":["She","is","making","pancakes."],"answerVoice":"female",
 "notes":"Clip has 4 shots (living room, stove, knee on carpet, school gate). The woman is boxed in every shot; at 0.0-1.5 her box is split from the baby's (baby in front of her). 'the girl on the floor' boxed only in the knee shot (4.5-6.5); she may be the girl in pink at the stove but is off there. At 7.0-9.0 other parents also hug children, so no hug phrase for the woman. The answer says 'pancakes' though only one pancake is in the pan at a time."}
json.dump(c,open('content/5089.json','w'),indent=1)
