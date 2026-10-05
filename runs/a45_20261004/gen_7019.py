import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(b): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,b)]
man=[(.21,.22,.52,.78),(.20,.21,.52,.79),(.18,.21,.55,.79),(.12,.19,.62,.81),(.12,.18,.63,.82),(.14,.18,.66,.82)]
pigeon=[(.44,.07,.26,.14),(.41,.08,.32,.13),(.40,.07,.30,.14),(.53,.01,.27,.17),None,None]
woman=[(.73,.32,.24,.30),(.72,.32,.23,.30),(.73,.32,.24,.30),(.74,.33,.22,.28),(.75,.34,.20,.28),(.80,.35,.18,.24)]
c={"mediaId":7019,"level":"B","keyWord":"danish","defaultVoice":"male",
"taps":[
 {"phrase":"to balance a tray of pastries","target":"the man","voice":"male","keys":K(man)},
 {"phrase":"to snatch a pastry","target":"the pigeon with the pastry","voice":"male","keys":K(pigeon)},
 {"phrase":"to burst out laughing","target":"the woman","voice":"female","keys":K(woman)}],
"stillS":0.7,
"nouns":[{"word":"a pigeon","x":0.58,"y":0.16,"voice":"male"},{"word":"danishes","x":0.82,"y":0.26,"voice":"male"},
 {"word":"a bicycle","x":0.47,"y":0.88,"voice":"male"},{"word":"tulips","x":0.13,"y":0.66,"voice":"male"}],
"question":"What is the man balancing?",
"answer":["He","is","balancing","a","tray","of","danishes."],
"answerVoice":"male",
"notes":"Pigeon leaves the picture after 1.7 s (off). Other pigeons fly at the left edge at 0.2 s, hence the target name. Woman is partly hidden by the man's raised arm at 2.7 s; boxes split at his arm."}
json.dump(c,open('content/7019.json','w'),indent=1)
