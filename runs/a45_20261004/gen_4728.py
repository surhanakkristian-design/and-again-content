import json
T=[i*0.5 for i in range(21)]
B=[(.26,.17,.72,.83),(.22,.15,.78,.85),(.15,.16,.82,.84),(.12,.15,.80,.85),(.12,.13,.70,.87),(.19,.12,.77,.88),
   (.09,.12,.74,.88),(0,.10,.98,.90),(0,.08,.88,.92),(0,.08,.83,.92),(0,.08,.76,.92),(0,.09,.84,.91),(.15,.08,.85,.92),
   (.12,.02,.86,.98),(.03,.08,.97,.92),(.12,.15,.88,.85),(.05,.22,.95,.78),(0,.36,1,.64),(0,.35,1,.65),(.03,.33,.97,.67),(.04,.27,.96,.73)]
def keys(): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4728,"level":"A","keyWord":"sleep","defaultVoice":"female",
 "taps":[
  {"phrase":"to open her mouth wide","target":"the woman","voice":"female","keys":keys()},
  {"phrase":"to take off her jacket","target":"the woman","voice":"female","keys":keys()},
  {"phrase":"to sleep on the sofa","target":"the woman","voice":"female","keys":keys()}],
 "stillS":10.0,
 "nouns":[{"word":"a wall","x":.60,"y":.12,"voice":"female"},{"word":"a woman","x":.35,"y":.46,"voice":"female"},
          {"word":"a phone","x":.82,"y":.81,"voice":"female"},{"word":"a sofa","x":.28,"y":.90,"voice":"female"}],
 "question":"Where is the woman sleeping?",
 "answer":["She","is","sleeping","on","the","sofa."],
 "answerVoice":"female",
 "notes":"Only one possible target (the woman), so all three phrases use her with the same keys. She yawns with her mouth wide open 0-2.5 s and again 5-7 s, takes her jacket off 3.5-4.5 s, sleeps on the sofa from 8.5 s. The answer describes the end of the clip. 'a wall' is a plain noun but clearly visible; the dark chair top left is cut off, so it was not used."}
json.dump(c,open('content/4728.json','w'),indent=1,ensure_ascii=False)
