import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L):
    return [{"t":t,"x":round(a,2),"y":round(b,2),"w":round(c-a,2),"h":round(d-b,2)} for t,(a,b,c,d) in zip(T,L)]
M=[(.33,.53,.70,.86),(.28,.51,.58,.83),(.27,.51,.52,.77),(.29,.51,.52,.75),(.33,.51,.55,.73),(.37,.50,.57,.70),(.40,.50,.60,.70),(.41,.50,.61,.68)]
G=[(0,0,1,.29),(0,0,1,.28),(0,.01,1,.31),(.04,.07,.97,.34),(.11,.12,.93,.36),(.17,.16,.91,.38),(.22,.19,.89,.40),(.26,.22,.87,.42)]
S=[(.80,.49,1,.63),(.82,.49,1,.63),(.82,.50,1,.64),(.82,.50,1,.64),(.82,.51,1,.65),(.81,.51,1,.65),(.79,.51,.99,.65),(.76,.51,.96,.65)]
c={"mediaId":7200,"level":"B","keyWord":"gulf","defaultVoice":"male",
"taps":[
{"phrase":"to run off a rocky ledge","target":"the man in the red jacket","voice":"male","keys":K(M)},
{"phrase":"to lift the pilot upwards","target":"the orange wing","voice":"male","keys":K(G)},
{"phrase":"to flutter in the breeze","target":"the windsock","voice":"male","keys":K(S)}],
"stillS":2.2,
"nouns":[{"word":"a paraglider","x":.50,"y":.20,"voice":"male"},
{"word":"a windsock","x":.86,"y":.58,"voice":"male"},
{"word":"a gulf","x":.60,"y":.67,"voice":"male"},
{"word":"a rocky ledge","x":.60,"y":.85,"voice":"male"}],
"question":"What is the pilot doing?",
"answer":["He","is","gliding","over","a","turquoise","gulf."],
"answerVoice":"male",
"notes":"Windsock box (min size) reaches down to the heads of the two spectators standing under it; they are not a target. 'a paraglider' pill sits on the wing. 'to run off a rocky ledge' is true only in the first frames (0.2 s), afterwards he is airborne. Two spectators not used (two people, one phrase)."}
json.dump(c,open("content/7200.json","w"),indent=1,ensure_ascii=False)
