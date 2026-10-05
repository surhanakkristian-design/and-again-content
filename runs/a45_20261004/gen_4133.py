import json
M={0.0:(0,0.06,0.72,0.75),0.5:(0,0.07,0.74,0.70),1.0:(0,0.10,0.62,0.72),1.5:(0,0.09,0.56,0.64),
2.0:(0,0.07,0.46,0.56),2.5:(0,0.07,0.36,0.48),3.0:(0,0.09,0.40,0.48),3.5:(0.03,0.21,0.50,0.34),
4.0:(0,0.22,0.54,0.31),4.5:(0.02,0.21,0.52,0.32),5.0:(0,0.21,0.53,0.32),5.5:(0,0.17,0.47,0.42),
6.0:(0.02,0.17,0.45,0.37),6.5:(0.05,0.14,0.72,0.45),7.0:(0,0.14,0.76,0.60),7.5:(0,0.20,1.0,0.42),
8.0:(0,0.16,0.97,0.46),8.5:(0,0.16,0.88,0.46),9.0:(0,0.04,0.80,0.52),9.5:(0,0.0,0.72,0.57)}
A={0.0:(0.72,0.22,0.28,0.22),0.5:(0.74,0.24,0.26,0.24),1.0:(0.62,0.26,0.38,0.24),1.5:(0.56,0.31,0.36,0.20),
2.0:(0.46,0.31,0.38,0.21),2.5:(0.36,0.28,0.40,0.22),3.0:(0.40,0.31,0.34,0.21),3.5:(0.53,0.30,0.20,0.22),
4.0:(0.54,0.31,0.21,0.20),4.5:(0.54,0.30,0.21,0.20),5.0:(0.53,0.30,0.22,0.20),5.5:(0.47,0.25,0.27,0.24),
6.0:(0.47,0.19,0.28,0.21),7.5:(0,0.06,0.42,0.14),8.0:(0,0.02,0.46,0.14),8.5:(0,0.02,0.46,0.14)}
T=[i*0.5 for i in range(20)]
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else {"t":t,"off":True} for t in T]
d={"mediaId":4133,"level":"A","keyWord":"fridge","defaultVoice":"male",
"taps":[
 {"phrase":"to hug a big dog","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to touch the dog's head","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to lie by the fridge","target":"the dog by the fridge","voice":"male","keys":keys(A)}],
"stillS":4.0,
"nouns":[{"word":"a fridge","x":0.60,"y":0.14,"voice":"male"},
 {"word":"a man","x":0.30,"y":0.33,"voice":"male"},
 {"word":"a bowl","x":0.84,"y":0.44,"voice":"male"},
 {"word":"a dog","x":0.74,"y":0.80,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","hugging","a","big","dog."],
"answerVoice":"male",
"notes":"Two golden retrievers: only the one lying by the fridge is a tap target ('the dog by the fridge'); the front dog has no box. Man and that dog overlap for most of the clip (he leans over and hugs it), so the boxes are split along a vertical line and part of his arm / head falls outside his box in some frames (1.5-3.0, 6.0). The dog by the fridge is 'off' at 6.5, 7.0, 9.0, 9.5 where the man hides almost all of it. From 7.0 the man hugs the front dog. The noun 'a dog' sits on the front dog; the other dog is under the man at 4.0 s."}
json.dump(d,open("content/4133.json","w"),indent=1,ensure_ascii=False)
