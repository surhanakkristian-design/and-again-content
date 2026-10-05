import json
T=[i*0.5 for i in range(19)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
couple=[(0,0,1,1)]*6+[None]*13
twins=[None]*6+[(0,.23,1,.73)]*3+[None]*10
d={"mediaId":5107,"level":"B","keyWord":"cradle","defaultVoice":"male",
"taps":[
 {"phrase":"to cradle a newborn","target":"the couple","voice":"male","keys":K(couple)},
 {"phrase":"to gaze at their baby","target":"the couple","voice":"male","keys":K(couple)},
 {"phrase":"to sleep side by side","target":"the twins","voice":"male","keys":K(twins)}],
"stillS":1.0,
"nouns":[{"word":"curly hair","x":0.14,"y":0.26,"voice":"male"},
 {"word":"a newborn","x":0.71,"y":0.48,"voice":"male"},
 {"word":"a wedding ring","x":0.47,"y":0.76,"voice":"male"}],
"question":"What are the man and woman doing?",
"answer":["They","are","cradling","a","newborn","baby."],
"answerVoice":"male",
"notes":"Video differs from the description: shot 1 (0-2.5) couple cradling a swaddled newborn, shot 2 (3.0-4.0) two newborns side by side in one bassinet (no parents, no reflections), shot 3 (4.5-9.0) nursery rows. The couple is one target (both cradle the baby, they fill the frame). Twins box covers both babies in shot 2. Mixed couple -> defaultVoice male (evenId false). Unsure whose hand wears the ring (probably the man's); pill is on the ring itself."}
json.dump(d,open("content/5107.json","w"),indent=1)
