import json
times=[i*0.5 for i in range(19)]
tops=[.23,.23,.23,.23,.22,.22,.22,.21,.19,.18,.17,.17,.15,.15,.14,.13,.13,.13,.13]
keys=[{"t":t,"x":0.0,"y":round(tp-.03,2),"w":1.0,"h":round(1-(tp-.03),2)} for t,tp in zip(times,tops)]
c={"mediaId":5194,"level":"A","keyWord":"novel","defaultVoice":"female",
 "taps":[
  {"phrase":"to read a novel","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to turn a page","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to close her book","target":"the woman","voice":"female","keys":keys}],
 "stillS":2.5,
 "nouns":[{"word":"a novel","x":0.40,"y":0.70,"voice":"female"},{"word":"a sofa","x":0.12,"y":0.48,"voice":"female"},
  {"word":"a window","x":0.47,"y":0.12,"voice":"female"},{"word":"curtains","x":0.85,"y":0.30,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","reading","a","novel."],
 "answerVoice":"female",
 "notes":"Only one person; all three phrases target the woman (the book stays in her hands, so it is part of her box). She turns pages at 1.5 s and 3.5-6.5 s and closes the book at 7.5-8.0 s."}
json.dump(c,open('content/5194.json','w'),indent=1)
