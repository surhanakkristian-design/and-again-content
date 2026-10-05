import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
W={6.5:(0.38,0.08,0.52,0.29),7.0:(0.28,0.08,0.54,0.3)}
D={6.5:(0.3,0.37,0.44,0.3),7.0:(0.15,0.38,0.52,0.28)}
c={"mediaId":5482,"level":"A","keyWord":"bath","defaultVoice":"female",
 "taps":[
  {"phrase":"to wash a dog","target":"the woman with the dog","voice":"female","keys":K(W)},
  {"phrase":"to hold a wet dog","target":"the woman with the dog","voice":"female","keys":K(W)},
  {"phrase":"to sit in a bath","target":"the dog","voice":"female","keys":K(D)}],
 "stillS":6.5,
 "nouns":[{"word":"flowers","x":0.35,"y":0.08,"voice":"female"},{"word":"a woman","x":0.66,"y":0.27,"voice":"female"},
   {"word":"a dog","x":0.56,"y":0.46,"voice":"female"},{"word":"a bath","x":0.45,"y":0.75,"voice":"female"}],
 "question":"What is sitting in the bath?",
 "answer":["A","dog","is","sitting","in","the","bath."],
 "answerVoice":"female",
 "notes":"Montage of five washing shots; only the dog shot (6.5-7.0, two frames) has clear unique targets, the other shots (plate, car, shirt in metal tub, car wash crowd) have only hands or many people doing the same thing, so all three phrases sit in 6.5-7.0. The dog sits in front of the woman: boxes split horizontally at the dog's head/ears (woman box = head and shoulders). 'a bath' labels the large grey plastic tub the dog is bathed in (key word); a verifier may prefer 'a tub'. Taps are only possible for ~1 s."}
json.dump(c,open('content/5482.json','w'),indent=1)
