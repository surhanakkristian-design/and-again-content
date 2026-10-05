import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=[(l,0.0,round(1-l,2),0.46) for l in (0.22,0.26,0.21,0.20,0.18,0.15,0.14,0.12)]
pup=[(0.21,0.47,0.46,0.33),(0.37,0.47,0.30,0.33),(0.36,0.48,0.27,0.34),(0.30,0.52,0.36,0.30),
     (0.27,0.53,0.36,0.30),(0.26,0.48,0.28,0.35),(0.20,0.47,0.37,0.35),(0.18,0.48,0.34,0.35)]
pig=[(0.68,0.55,0.32,0.27),(0.69,0.53,0.31,0.29),(0.69,0.51,0.31,0.31),(0.67,0.53,0.33,0.30),
     (0.65,0.53,0.35,0.30),(0.61,0.52,0.39,0.31),(0.58,0.52,0.42,0.31),(0.54,0.53,0.46,0.30)]
c={"mediaId":7476,"level":"B","keyWord":"puppet","defaultVoice":"male",
 "taps":[{"phrase":"to pull the puppet's strings","target":"the puppeteer","voice":"male","keys":K(man)},
         {"phrase":"to bow to the pigeon","target":"the puppet","voice":"male","keys":K(pup)},
         {"phrase":"to stare at the puppet","target":"the pigeon","voice":"male","keys":K(pig)}],
 "stillS":3.2,
 "nouns":[{"word":"onlookers","x":0.17,"y":0.38,"voice":"male"},{"word":"a puppet","x":0.33,"y":0.65,"voice":"male"},
          {"word":"a pigeon","x":0.80,"y":0.68,"voice":"male"},{"word":"crumbs","x":0.55,"y":0.84,"voice":"male"}],
 "question":"What is the pigeon staring at?",
 "answer":["The","pigeon","is","staring","at","the","puppet."],"answerVoice":"male",
 "notes":"Puppet kicks 0.2-0.7, bows towards the pigeon 1.7-2.2, reaches out 3.2-3.7. Puppeteer box covers only his upper body/hand/control bar (y 0-.46) so it does not overlap the puppet or the pigeon in front of his torso. Background onlookers (two young men, woman, old man) laugh; none pulls strings."}
json.dump(c,open('content/7476.json','w'),indent=1)
