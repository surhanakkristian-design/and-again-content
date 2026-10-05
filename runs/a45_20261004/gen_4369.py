import json
O=None
# t: (man in tape, hoodie woman, man in blue T-shirt)
K={
0.0:((.0,.0,1.0,.75),O,O),
0.5:((.08,.0,.92,.92),O,O),
1.0:((.0,.05,1.0,.78),O,O),
1.5:((.0,.08,1.0,.70),O,O),
2.0:((.0,.02,.95,.76),O,O),
2.5:((.03,.38,.97,.24),O,O),
3.0:((.13,.52,.87,.22),O,O),
3.5:((.08,.50,.92,.38),O,O),
4.0:((.0,.38,1.0,.38),O,O),
4.5:((.03,.0,.94,1.0),O,O),
5.0:((.05,.0,.95,1.0),O,O),
5.5:((.0,.0,1.0,1.0),O,O),
6.0:((.0,.03,.95,.97),O,O),
6.5:((.30,.22,.40,.76),(.87,.56,.13,.32),(.70,.30,.17,.68)),
7.0:((.32,.26,.36,.72),(.84,.38,.16,.62),(.68,.32,.16,.65)),
7.5:((.33,.26,.29,.72),(.66,.66,.34,.31),(.62,.24,.28,.42)),
8.0:((.32,.23,.37,.73),(.69,.58,.31,.39),(.69,.29,.31,.29)),
8.5:((.31,.26,.36,.68),(.67,.49,.33,.48),(.67,.31,.22,.18)),
9.0:((.31,.28,.28,.66),(.59,.50,.39,.47),(.59,.32,.18,.18)),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4369,"level":"A","keyWord":"tape","defaultVoice":"male",
"taps":[
 {"phrase":"to stand in the middle","target":"the man in white tape","voice":"male","keys":keys(0)},
 {"phrase":"to bend down to his legs","target":"the woman in the grey hoodie","voice":"female","keys":keys(1)},
 {"phrase":"to hold a roll up high","target":"the man in the blue T-shirt","voice":"male","keys":keys(2)}],
"stillS":8.5,
"nouns":[{"word":"tape","x":0.50,"y":0.60,"voice":"male"},
 {"word":"the ceiling","x":0.30,"y":0.07,"voice":"male"},
 {"word":"windows","x":0.80,"y":0.27,"voice":"male"},
 {"word":"the floor","x":0.45,"y":0.95,"voice":"male"}],
"question":"What is the woman in blue doing?",
"answer":["She","is","putting","tape","on","his","hand."],
"answerVoice":"female",
"notes":"Cuts: 0-4.0 s close on the hand being taped (the man in tape = only his hand/arm there, box on the arm; the woman in blue scrubs is not a tap target), 4.5-5.5 s close-ups of his wrapped arm/body, 6.0-9.0 s group shot. Man in blue T-shirt lifts the roll high only around 7.5 s (holds it at chest height at 7.0 and 8.0); the hoodie woman holds a roll low. At 9.0 s he is mostly hidden behind the hoodie woman (box = head and shoulder). Hoodie woman bends from 7.5 s, stands again at 9.0. Question is about the first shots (woman in blue scrubs taping his hand)."}
json.dump(d,open("content/4369.json","w"),indent=1)
