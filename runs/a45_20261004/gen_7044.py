import json
def K(times, d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
def B(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:B(.0,.28,.24,.60),0.7:B(.03,.27,.32,.60),1.2:B(.06,.28,.37,.62),1.7:B(.08,.27,.40,.62),
     2.2:B(.06,.25,.43,.60),2.7:B(.01,.23,.43,.66),3.2:B(.0,.20,.42,.76),3.7:B(.0,.19,.42,.76)}
dog={0.2:B(.39,.39,.64,.58),0.7:B(.39,.39,.67,.58),1.2:B(.38,.39,.66,.58),1.7:B(.41,.39,.68,.58),
     2.2:B(.43,.39,.70,.60),2.7:B(.43,.39,.76,.60),3.2:B(.42,.39,.80,.64),3.7:B(.42,.40,.85,.66)}
cat={0.2:B(.0,.69,.52,.99),0.7:B(.0,.73,.55,1.0),1.2:B(.0,.80,.57,1.0)}
c={"mediaId":7044,"level":"A","keyWord":"dining room","defaultVoice":"female",
 "taps":[
  {"phrase":"to carry a roast chicken","target":"the woman","voice":"female","keys":K(T,wom)},
  {"phrase":"to smell the butter","target":"the cat","voice":"female","keys":K(T,cat)},
  {"phrase":"to sit on a chair","target":"the dog","voice":"female","keys":K(T,dog)}],
 "stillS":1.7,
 "nouns":[{"word":"a window","x":.88,"y":.16,"voice":"female"},{"word":"a door","x":.12,"y":.24,"voice":"female"},
          {"word":"a dog","x":.55,"y":.44,"voice":"female"},{"word":"potatoes","x":.60,"y":.83,"voice":"female"}],
 "question":"What is the woman carrying?",
 "answer":["She","is","carrying","a","roast","chicken."],
 "answerVoice":"female",
 "notes":"Cat only in the picture 0.2-1.2 s (at 1.2 only its back at the bottom edge, butter out of frame). From 2.2 s the chicken plate reaches under the dog's nose: woman/dog boxes split at x 0.42-0.43, so the plate tip and dog's nose are cut slightly. Key word 'dining room' is the whole room, so not a noun pill. defaultVoice female (woman and man, woman is the main person)."}
json.dump(c,open("content/7044.json","w"),indent=1,ensure_ascii=False)
