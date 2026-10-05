import json
O=None
# (woman in blue, woman in beige)
K={
0.0:((.22,.15,.60,.85),O),0.5:((.25,.16,.58,.84),O),1.0:((.30,.17,.52,.83),O),1.5:((.25,.16,.55,.84),O),
2.0:((.27,.18,.58,.82),O),2.5:((.25,.16,.65,.84),O),3.0:((.15,.22,.68,.78),O),
3.5:((.36,.31,.64,.69),(.06,.33,.30,.67)),
4.0:((.47,.32,.45,.68),(.03,.32,.44,.68)),
4.5:((.50,.30,.50,.70),(.08,.28,.42,.72)),
5.0:((.48,.33,.52,.67),(.03,.35,.45,.65)),
5.5:((.40,.34,.60,.66),(.0,.36,.40,.64)),
6.0:((.42,.36,.46,.64),(.02,.35,.40,.65)),
6.5:((.40,.36,.36,.64),(.15,.38,.25,.60)),
7.0:((.39,.36,.36,.64),(.20,.36,.19,.64)),
7.5:((.07,.26,.48,.74),(.55,.24,.45,.76)),
8.0:((.05,.27,.47,.73),(.52,.25,.44,.75)),
8.5:((.07,.24,.55,.76),(.62,.26,.36,.74)),
9.0:((.12,.27,.48,.73),(.60,.26,.38,.74)),
9.5:((.22,.27,.39,.73),(.61,.28,.37,.72)),
10.0:((.25,.28,.31,.72),(.56,.29,.34,.71)),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4390,"level":"B","keyWord":"excitement","defaultVoice":"female",
"taps":[
 {"phrase":"to bounce in the hallway","target":"the woman in blue","voice":"female","keys":keys(0)},
 {"phrase":"to point towards the arena","target":"the woman in blue","voice":"female","keys":keys(0)},
 {"phrase":"to wear a beige jacket","target":"the woman in beige","voice":"female","keys":keys(1)}],
"stillS":4.5,
"nouns":[{"word":"the sky","x":0.40,"y":0.12,"voice":"female"},
 {"word":"a street lamp","x":0.74,"y":0.27,"voice":"female"},
 {"word":"a car","x":0.85,"y":0.43,"voice":"female"}],
"question":"What is the woman in blue doing?",
"answer":["She","is","bouncing","with","excitement."],
"answerVoice":"female",
"notes":"Only two targets (the two friends); the friend does nothing the woman in blue does not also do, so her phrase is a state (beige jacket). The woman in blue points ahead at the lit arena at 6.5-7.0 s. The two overlap in most frames from 3.5 s (walking close, hugging at 9.5-10.0 s): boxes split along a vertical line between them, in the hug between the two heads. Key word is abstract, so not a noun; it is in the answer. Still 4.5 s: both women are moving, the three nouns (sky, street lamp, car) are background."}
json.dump(d,open("content/4390.json","w"),indent=1)
