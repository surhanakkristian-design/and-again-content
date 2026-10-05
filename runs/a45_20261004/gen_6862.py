import json
def keys(times, boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(times,boxes)]
T=[0.2,0.7,1.2,1.7,2.2,2.7]
man=[(0.33,0.37,0.36,0.35),(0.32,0.09,0.38,0.55),(0.33,0.06,0.36,0.57),(0.07,0.12,0.69,0.51),(0.15,0.39,0.48,0.43),(0.20,0.31,0.51,0.49)]
k=keys(T,man)
c={"mediaId":6862,"level":"B","keyWord":"bars","defaultVoice":"male",
 "taps":[
  {"phrase":"to do a perfect handstand","target":"the man","voice":"male","keys":k},
  {"phrase":"to swing off the bars","target":"the man","voice":"male","keys":k},
  {"phrase":"to celebrate with raised fists","target":"the man","voice":"male","keys":k}],
 "stillS":0.2,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},
          {"word":"a man","x":0.50,"y":0.54,"voice":"male"},
          {"word":"parallel bars","x":0.66,"y":0.74,"voice":"male"},
          {"word":"salt","x":0.22,"y":0.92,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","doing","a","handstand","on","the","bars."],
 "answerVoice":"male",
 "notes":"Only one person, so all three phrases share the man's keys. Handstand 0.7-1.2 s, swing off at 1.7 s, landing and raised fists 2.2-2.7 s (camera angle changes, bars only partly visible on the right). 'salt' = the white salt ground."}
json.dump(c,open('content/6862.json','w'),indent=1)
