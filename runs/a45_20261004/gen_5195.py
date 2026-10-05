import json
def K(rows): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in rows]
man=[(0.0,(.18,.21,.60,.79)),(0.5,(.18,.21,.60,.79)),(1.0,(.18,.21,.62,.79)),(1.5,(.18,.21,.62,.79)),
(2.0,(.13,.18,.86,.82)),(2.5,(.11,.15,.88,.85)),(3.0,(.13,.24,.77,.76)),(3.5,(.12,.23,.78,.77)),
(4.0,(.14,.12,.86,.88)),(4.5,(.12,.16,.88,.84)),(5.0,(.14,.19,.86,.81)),(5.5,(.05,.21,.95,.79)),
(6.0,(.20,.26,.80,.74)),(6.5,(.19,.34,.81,.66)),(7.0,(.06,.31,.94,.69)),(7.5,(.09,.25,.88,.75)),
(8.0,(.07,.18,.87,.82)),(8.5,(.09,.27,.85,.73)),(9.0,(.10,.32,.82,.68))]
pig=[(0.0,(0,.43,.18,.14)),(0.5,(0,.43,.18,.14)),(1.0,(0,.44,.18,.14)),(1.5,(0,.44,.18,.14)),
(2.0,(0,.44,.13,.14)),(2.5,(0,.44,.11,.14)),(3.0,(0,.44,.13,.14)),(3.5,(0,.44,.12,.14)),
(4.0,(0,.43,.14,.14)),(4.5,(0,.46,.12,.14)),(5.0,(0,.46,.14,.14)),(5.5,None),
(6.0,(0,.48,.20,.14)),(6.5,(0,.50,.19,.14)),(7.0,None),(7.5,None),(8.0,None),(8.5,None),(9.0,(0,.77,.10,.14))]
c={"mediaId":5195,"level":"A","keyWord":"bench","defaultVoice":"male",
"taps":[{"phrase":"to sit on a bench","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to lift a big book","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to stand behind the bench","target":"the bird","voice":"male","keys":K(pig)}],
"stillS":1.0,
"nouns":[{"word":"a bench","x":.85,"y":.59,"voice":"male"},{"word":"a bird","x":.13,"y":.50,"voice":"male"},
{"word":"a hat","x":.53,"y":.30,"voice":"male"},{"word":"trees","x":.78,"y":.12,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","sitting","on","a","bench."],"answerVoice":"male",
"notes":"bird (pigeon) stands on the path behind the bench, small; partly hidden behind the man's arm at 2.0-5.0 so its box is narrow there; off at 5.5 and from 7.0 (back at the left edge at 9.0). Man boxes include the big book he holds up at 7.0-9.0."}
json.dump(c,open('content/5195.json','w'),indent=1)
