import json
A="a";B="b";P="p"
PB=(0.13,0.0,0.24,0.15)
F={
0.0:{A:(0,0,0.42,0.95),B:(0.43,0,0.57,0.44)},
0.5:{A:(0,0,0.60,0.95),B:(0.61,0,0.39,0.36)},
1.0:{A:(0,0,0.58,0.90),B:(0.59,0,0.41,0.27)},
1.5:{A:(0,0,0.58,0.90),B:(0.60,0,0.40,0.28)},
2.0:{A:(0,0,1.0,0.66)},
2.5:{A:(0,0.15,1.0,0.70),B:(0.66,0,0.34,0.14)},
3.0:{A:(0,0,0.66,0.88),B:(0.68,0,0.32,0.27)},
3.5:{A:(0,0.03,0.66,0.92),B:(0.68,0.03,0.32,0.45)},
4.0:{A:(0,0.15,0.66,0.85),B:(0.68,0.08,0.32,0.72),P:(0.13,0,0.24,0.14)},
4.5:{A:(0,0.15,0.65,0.85),B:(0.67,0.10,0.33,0.72),P:(0.13,0,0.24,0.14)},
5.0:{A:(0,0.18,0.60,0.82),B:(0.62,0.14,0.38,0.70),P:(0.13,0.02,0.24,0.15)},
5.5:{A:(0,0.18,0.60,0.82),B:(0.62,0.17,0.38,0.31),P:(0.13,0.02,0.24,0.15)},
6.0:{A:(0,0.16,0.58,0.84),B:(0.60,0.15,0.40,0.38),P:PB},
6.5:{A:(0,0.16,0.52,0.84),B:(0.54,0.15,0.46,0.37),P:PB},
7.0:{A:(0,0.16,0.53,0.84),B:(0.56,0.17,0.44,0.28),P:PB},
7.5:{A:(0,0.18,0.52,0.82),B:(0.54,0.18,0.46,0.48),P:PB},
8.0:{A:(0,0.16,0.50,0.84),B:(0.52,0.17,0.48,0.40),P:PB},
8.5:{A:(0,0.16,0.49,0.84),B:(0.51,0.09,0.49,0.50),P:PB},
9.0:{A:(0,0.16,0.47,0.84),B:(0.49,0.15,0.51,0.60),P:PB},
9.5:{A:(0,0.17,0.48,0.83),B:(0.50,0.18,0.50,0.60),P:PB},
10.0:{A:(0,0.16,0.46,0.84),B:(0.48,0.18,0.52,0.60),P:PB},
}
def keys(k):
    out=[]
    for t in sorted(F):
        if k in F[t]:
            x,y,w,h=F[t][k]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
d={"mediaId":95,"level":"B","keyWord":"blush","defaultVoice":"female",
"taps":[
 {"phrase":"to apply blush with a brush","target":"the girl with the braid","voice":"female","keys":keys(A)},
 {"phrase":"to peer over her shoulder","target":"the girl with short hair","voice":"female","keys":keys(B)},
 {"phrase":"to perch on a cage","target":"the bird","voice":"female","keys":keys(P)}],
"stillS":3.0,
"nouns":[{"word":"a braid","x":0.15,"y":0.62,"voice":"female"},
 {"word":"a brush","x":0.78,"y":0.30,"voice":"female"},
 {"word":"blush","x":0.60,"y":0.91,"voice":"female"}],
"question":"What is the girl in green doing?",
"answer":["She","is","applying","blush","with","a","brush."],
"answerVoice":"female",
"notes":"Two young women; the question names 'the girl in green' (olive T-shirt, braid). The two overlap all the time: boxes split along the line between their heads, so the braid girl's brush hand, when it is in front of her friend, falls outside her box (0.0, 3.0-8.0 s). 2.0 s: friend only a strip of beige fabric -> off. 2.5 s: friend only chin, top right. Bird (budgie on a cage, background) visible from 4.0 s, small. Still 3.0 s: 'a brush' pill sits on the brush ferrule in front of the friend's chin."}
json.dump(d,open("content/95.json","w"),indent=1,ensure_ascii=False)
