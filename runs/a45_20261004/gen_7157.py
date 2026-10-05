import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
woman=[(0,.31,.50,.94),(.02,.31,.50,.94),(.06,.30,.50,.99),(.05,.29,.53,.99),(0,.28,.69,.96),(.06,.27,.69,.98),(0,.27,.61,1.0),(.07,.27,.55,1.0)]
pole=[(.66,.18,.84,.38),(.66,.19,.84,.39),(.66,.22,.84,.44),(.68,.24,.86,.50),(.69,.27,.86,.60),(.70,.29,.88,.61),(.72,.35,.88,.75),None]
dog=[(.56,.55,.80,.76),(.51,.55,.73,.74),(.50,.56,.68,.72),None,None,None,(.61,.50,.72,.64),(.62,.49,.82,.65)]
c={"mediaId":7157,"level":"A","keyWord":"get dressed","defaultVoice":"female",
"taps":[
 {"phrase":"to put on a jacket","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to slide down a pole","target":"the man on the pole","voice":"male","keys":K(pole)},
 {"phrase":"to walk across the floor","target":"the dog","voice":"female","keys":K(dog)}],
"stillS":0.2,
"nouns":[{"word":"a fire engine","x":0.55,"y":0.40,"voice":"female"},
 {"word":"a jacket","x":0.12,"y":0.48,"voice":"female"},
 {"word":"a dog","x":0.68,"y":0.66,"voice":"female"},
 {"word":"a light","x":0.83,"y":0.20,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","getting","dressed","in","a","fire","station."],
"answerVoice":"female",
"notes":"Dog hidden behind the woman 1.7-2.7 s (off); at 3.2 s its box is narrow (squeezed between the woman and the man at the pole). Man on the pole set off at 3.7 s: several firefighters stand near the pole and it is unclear which one slid down."}
json.dump(c,open('content/7157.json','w'),indent=1)
