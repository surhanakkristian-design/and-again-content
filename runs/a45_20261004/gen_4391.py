import json
O=None
# (woman, candle, pizza)
K={
0.0:((.03,.17,.97,.83),O,O),0.5:((.0,.17,1.0,.83),O,O),1.0:((.0,.08,1.0,.92),O,O),1.5:((.0,.12,1.0,.88),O,O),
2.0:((.03,.20,.97,.80),O,O),2.5:((.15,.0,.85,1.0),O,O),
3.0:((.18,.15,.82,.51),(.0,.34,.18,.33),(.0,.67,1.0,.25)),
3.5:((.18,.10,.82,.57),(.0,.33,.18,.34),(.0,.67,1.0,.26)),
4.0:((.18,.08,.82,.57),(.0,.33,.18,.33),(.0,.66,1.0,.26)),
4.5:((.18,.08,.82,.57),(.0,.33,.18,.33),(.0,.66,1.0,.26)),
5.0:((.18,.08,.82,.58),(.0,.33,.18,.34),(.0,.67,1.0,.26)),
5.5:((.18,.08,.82,.58),(.0,.33,.18,.34),(.0,.67,1.0,.26)),
6.0:((.18,.07,.82,.57),(.0,.32,.18,.33),(.0,.65,1.0,.27)),
6.5:((.0,.12,1.0,.50),O,O),
7.0:((.0,.33,1.0,.36),O,O),7.5:((.0,.32,1.0,.37),O,O),8.0:((.0,.32,1.0,.37),O,O),
8.5:((.0,.32,1.0,.37),O,O),9.0:((.0,.32,1.0,.37),O,O),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4391,"level":"A","keyWord":"alone","defaultVoice":"female",
"taps":[
 {"phrase":"to sing into a brush","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to burn next to the pizza","target":"the candle","voice":"female","keys":keys(1)},
 {"phrase":"to lie in a box","target":"the pizza","voice":"female","keys":keys(2)}],
"stillS":4.0,
"nouns":[{"word":"a candle","x":0.10,"y":0.52,"voice":"female"},
 {"word":"a pizza","x":0.45,"y":0.75,"voice":"female"},
 {"word":"a box","x":0.62,"y":0.88,"voice":"female"},
 {"word":"a hand","x":0.74,"y":0.46,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","a","pizza","alone."],
"answerVoice":"female",
"notes":"Candle and pizza are only in the table shot (3.0-6.0 s). The woman's jumper runs behind the candle at the left edge: split at x 0.18. At 6.0 s the candle is half out of the picture at the left edge. 6.5 s is a blurred transition to the bed (pizza box corner visible, pizza itself not: off). 'a box' pill sits on the cardboard front edge below the pizza; 'a hand' is the hand holding the slice. Key word 'alone' is in the answer."}
json.dump(d,open("content/4391.json","w"),indent=1)
