import json
O=None
# t: (man in blue shirt, barman, lights)
K={
0.0:(O,O,O),
0.5:((.42,.21,.58,.79),O,O),
1.0:((.10,.29,.90,.71),O,O),
1.5:((.20,.28,.80,.72),O,O),
2.0:((.22,.23,.78,.77),O,O),
2.5:((.0,.18,.55,.52),(.55,.13,.45,.50),O),
3.0:((.0,.16,.42,.56),(.42,.10,.58,.42),O),
3.5:((.0,.11,.41,.60),(.41,.03,.59,.42),O),
4.0:((.0,.08,.40,.60),(.40,.0,.60,.42),O),
4.5:((.0,.06,.41,.62),(.41,.0,.59,.40),O),
5.0:((.0,.58,.62,.42),O,O),
5.5:((.25,.75,.75,.25),O,O),
6.0:((.42,.0,.20,.22),O,O),
6.5:((.42,.20,.18,.19),O,(.0,.02,1.0,.18)),
7.0:((.43,.31,.19,.22),O,(.0,.11,1.0,.20)),
7.5:((.44,.35,.22,.20),O,(.0,.14,1.0,.21)),
8.0:((.45,.35,.22,.22),O,(.0,.11,1.0,.24)),
8.5:((.37,.30,.29,.29),O,(.0,.10,1.0,.20)),
9.0:((.36,.35,.27,.26),O,(.0,.14,1.0,.21)),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4373,"level":"A","keyWord":"gather","defaultVoice":"male",
"taps":[
 {"phrase":"to hold a beer bottle","target":"the man in the blue shirt","voice":"male","keys":keys(0)},
 {"phrase":"to pour an orange drink","target":"the barman","voice":"male","keys":keys(1)},
 {"phrase":"to hang over the bar","target":"the lights","voice":"male","keys":keys(2)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.55,"y":0.08,"voice":"male"},
 {"word":"lights","x":0.50,"y":0.27,"voice":"male"},
 {"word":"drinks","x":0.45,"y":0.45,"voice":"male"}],
"question":"What are the friends doing?",
"answer":["They","are","gathering","for","drinks."],
"answerVoice":"male",
"notes":"Cuts: street bar 0.5-2.0 s (0.0 s = blurred street, nothing on), cocktail bar 2.5-4.5 s, walk 5.0-5.5 s (camera looks down: only his legs and shoes, box on them - weak spot, could be set off), rooftop 6.0-9.0 s (6.0 s blurred). The barman = the man with the shaker, mostly hands, arm and shaker at the right edge; the hand that slides the bottle at 0.5-1.0 s belongs to another bar worker and is not boxed. On the rooftop the man in the blue shirt stands in the middle of the group (small box, neighbours close). Lights box ends just above his head / raised glass. Only 3 nouns: the long marble bar has no safe A-level name (table / bar / counter). The answer uses the key word gather."}
json.dump(d,open("content/4373.json","w"),indent=1)
