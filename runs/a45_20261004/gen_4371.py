import json
O=None
# t: (woman, clerk, screen)
K={
0.0:((.28,.32,.54,.68),O,O),
0.5:((.22,.30,.78,.70),O,O),
1.0:((.15,.28,.85,.72),O,O),
1.5:((.28,.28,.70,.72),O,O),
2.0:((.33,.24,.59,.40),(.0,.64,.60,.36),O),
2.5:((.40,.24,.54,.40),(.0,.18,.40,.82),O),
3.0:((.40,.26,.54,.47),(.0,.20,.40,.80),O),
3.5:((.40,.26,.56,.47),(.0,.20,.40,.80),O),
4.0:((.57,.31,.43,.69),O,(.12,.25,.45,.19)),
4.5:((.57,.30,.43,.70),O,(.12,.25,.45,.19)),
5.0:((.57,.30,.43,.70),O,(.10,.24,.47,.21)),
5.5:((.57,.28,.43,.72),O,(.10,.24,.47,.21)),
6.0:((.59,.26,.41,.74),O,(.09,.23,.50,.21)),
6.5:((.0,.33,.31,.67),O,O),
7.0:((.0,.45,.29,.55),O,O),
7.5:((.0,.44,.32,.56),O,O),
8.0:((.0,.30,.40,.70),O,O),
8.5:((.0,.29,.50,.71),O,O),
9.0:((.0,.34,.55,.66),O,O),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4371,"level":"B","keyWord":"lobby","defaultVoice":"female",
"taps":[
 {"phrase":"to stare into the vault","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to operate a counting machine","target":"the clerk","voice":"male","keys":keys(1)},
 {"phrase":"to display rows of figures","target":"the information screen","voice":"female","keys":keys(2)}],
"stillS":4.5,
"nouns":[{"word":"spotlights","x":0.40,"y":0.11,"voice":"female"},
 {"word":"a screen","x":0.33,"y":0.35,"voice":"female"},
 {"word":"swivel chairs","x":0.26,"y":0.58,"voice":"female"},
 {"word":"a lobby","x":0.28,"y":0.80,"voice":"female"}],
"question":"What is the woman staring into?",
"answer":["She","is","staring","into","a","bank","vault."],
"answerVoice":"female",
"notes":"Cuts: door 0-1.0 s, counter 1.5-3.5 s, lobby 4.0-6.0 s, vault 6.5-9.0 s. The clerk is seen from behind in the foreground (2.0-3.5 s): box = his hands at 2.0 s, his head/shoulder column at 2.5-3.5 s; his watch hand at the bottom right is outside the box there. Woman box cut short at the counter so it does not overlap the clerk. Information screen box = the part left of her head only. The man in the suit who turns the vault wheel (6.5 s, a sliver at 7.0 s) is not a target. The key word \"a lobby\" labels the whole hall: pill placed on the open marble floor - weak spot. The clerks at the back desks are small and blurred, so only one woman is identifiable."}
json.dump(d,open("content/4371.json","w"),indent=1)
