import json
W="w";M="m";S="s"
def sun(cx,cy): return (round(cx-0.10,2),round(cy-0.08,2),0.20,0.16)
F={
0.0:{W:(0.32,0.34,0.18,0.14),M:(0.51,0.34,0.18,0.14)},
0.5:{W:(0.41,0.41,0.18,0.14)},
1.0:{W:(0.41,0.51,0.18,0.14)},
1.5:{W:(0.39,0.62,0.20,0.22)},
2.0:{W:(0.36,0.74,0.24,0.26)},
2.5:{W:(0.30,0.86,0.20,0.14),M:(0.51,0.84,0.18,0.14)},
3.0:{W:(0.25,0.78,0.24,0.22),M:(0.50,0.77,0.18,0.16)},
3.5:{W:(0.20,0.73,0.26,0.27),M:(0.47,0.72,0.18,0.15)},
4.0:{W:(0.12,0.70,0.37,0.30),M:(0.50,0.70,0.18,0.17),S:sun(0.53,0.34)},
4.5:{W:(0.07,0.66,0.40,0.34),M:(0.48,0.67,0.18,0.20),S:sun(0.55,0.33)},
5.0:{W:(0.08,0.67,0.36,0.33),M:(0.46,0.65,0.20,0.35),S:sun(0.57,0.31)},
5.5:{W:(0,0.65,0.44,0.35),M:(0.46,0.64,0.24,0.36),S:sun(0.58,0.31)},
6.0:{W:(0.03,0.67,0.42,0.33),M:(0.47,0.65,0.32,0.35),S:sun(0.63,0.33)},
6.5:{W:(0.05,0.68,0.39,0.32),M:(0.45,0.65,0.37,0.35),S:sun(0.62,0.33)},
7.0:{W:(0.07,0.67,0.38,0.33),M:(0.46,0.66,0.44,0.34),S:sun(0.62,0.37)},
7.5:{W:(0.07,0.69,0.36,0.31),M:(0.44,0.68,0.44,0.32),S:sun(0.62,0.36)},
8.0:{W:(0.07,0.69,0.40,0.31),M:(0.48,0.68,0.42,0.32),S:sun(0.63,0.36)},
8.5:{W:(0.07,0.69,0.40,0.31),M:(0.48,0.68,0.42,0.32),S:sun(0.64,0.36)},
9.0:{W:(0.07,0.69,0.40,0.31),M:(0.48,0.68,0.42,0.32),S:sun(0.64,0.37)},
9.5:{W:(0.07,0.69,0.40,0.31),M:(0.48,0.68,0.42,0.32),S:sun(0.63,0.37)},
10.0:{W:(0.07,0.68,0.40,0.32),M:(0.48,0.65,0.44,0.35),S:sun(0.62,0.36)},
}
def keys(k):
    out=[]
    for t in sorted(F):
        if k in F[t]:
            x,y,w,h=F[t][k]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
d={"mediaId":137,"level":"B","keyWord":"canyon","defaultVoice":"male",
"taps":[
 {"phrase":"to touch the canyon wall","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to shout through cupped hands","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to shine between the rocks","target":"the sun","voice":"male","keys":keys(S)}],
"stillS":6.5,
"nouns":[{"word":"the sky","x":0.47,"y":0.12,"voice":"male"},
 {"word":"the sun","x":0.64,"y":0.33,"voice":"male"},
 {"word":"a canyon","x":0.48,"y":0.56,"voice":"male"},
 {"word":"a woman","x":0.27,"y":0.90,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","shouting","through","cupped","hands."],
"answerVoice":"male",
"notes":"0-2.0 s the couple is tiny and seen from behind; the man walks in front of the woman and is almost fully hidden 0.5-2.0 s -> off there. Woman touches the wall 2.5-5.0 s; man cups his hands 7.0-9.5 s. Third target = the sun (glow at the rock edge from 4.0 s, clear starburst from 6.0 s; faint at 3.5 s, left off). A small bird crosses the sky 8.5-9.5 s, not used. 'a canyon' pill sits on the narrow gap between the walls; no 'rock' noun to avoid a double label. Mixed couple, evenId false -> defaultVoice male."}
json.dump(d,open("content/137.json","w"),indent=1,ensure_ascii=False)
