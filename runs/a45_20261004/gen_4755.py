import json
D="d";M="m";X="x"
F={
0.0:{D:(0,0.22,0.34,0.78),X:(0.35,0.23,0.36,0.31),M:(0.72,0.40,0.28,0.60)},
0.5:{D:(0,0.22,0.34,0.78),X:(0.35,0.23,0.34,0.32),M:(0.70,0.41,0.30,0.59)},
1.0:{D:(0,0.22,0.32,0.78),X:(0.33,0.23,0.33,0.44),M:(0.67,0.55,0.33,0.45)},
1.5:{D:(0,0.25,0.27,0.75),X:(0.28,0.22,0.36,0.47),M:(0.65,0.55,0.35,0.45)},
2.0:{D:(0,0.59,0.40,0.41),X:(0.19,0.18,0.42,0.40),M:(0.62,0.43,0.38,0.57)},
2.5:{D:(0,0.62,0.40,0.38),X:(0.14,0.15,0.52,0.46),M:(0.67,0.43,0.33,0.57)},
3.0:{D:(0,0.64,0.40,0.36),X:(0.07,0.10,0.60,0.53),M:(0.68,0.40,0.32,0.60)},
3.5:{D:(0,0.63,0.25,0.37),X:(0,0.08,0.63,0.54),M:(0.64,0.37,0.36,0.63)},
4.0:{X:(0,0.05,0.53,0.56),M:(0.54,0.32,0.46,0.68)},
4.5:{X:(0,0,0.40,0.54),M:(0.41,0.20,0.59,0.80)},
5.0:{X:(0,0,0.22,0.42),M:(0.23,0.04,0.77,0.96)},
5.5:{M:(0,0,1,1)},6.0:{M:(0,0,1,1)},6.5:{M:(0,0,1,1)},7.0:{M:(0,0,1,1)},7.5:{M:(0,0,1,1)},8.0:{M:(0,0,1,1)},
8.5:{M:(0,0.05,1,0.95)},9.0:{M:(0,0.12,1,0.88)},9.5:{M:(0,0.12,1,0.88)},10.0:{M:(0,0.10,1,0.90)},
}
def keys(k):
    out=[]
    for t in sorted(F):
        if k in F[t]:
            x,y,w,h=F[t][k]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
d={"mediaId":4755,"level":"B","keyWord":"fracture","defaultVoice":"male",
"taps":[
 {"phrase":"to point at the X-ray","target":"the doctor","voice":"female","keys":keys(D)},
 {"phrase":"to wince in pain","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to reveal a fracture","target":"the X-ray","voice":"male","keys":keys(X)}],
"stillS":0.5,
"nouns":[{"word":"an X-ray","x":0.56,"y":0.32,"voice":"male"},
 {"word":"a doctor","x":0.15,"y":0.65,"voice":"female"},
 {"word":"a cast","x":0.60,"y":0.84,"voice":"male"},
 {"word":"a sling","x":0.83,"y":0.94,"voice":"male"}],
"question":"What is the doctor pointing at?",
"answer":["She","is","pointing","at","a","fracture","on","the","X-ray."],
"answerVoice":"female",
"notes":"Doctor points with her finger (packet says pen). 0-3.5 s all three targets overlap in the picture: doctor box = her head and body on the left (0-1.5 s) or her hands (2.0-3.5 s, head out of frame), her pointing hand on the film lies in the X-ray box; the man's box 0-0.5 s is his head and right side, his cast arm in front of the doctor is left out. From 5.5 s only a dark sliver of the film is left at the top-left edge: X-ray set off, man full frame. 'fracture' not used as a noun slot (it sits on the X-ray), used in the answer instead. defaultVoice male: the man is in the whole clip."}
json.dump(d,open("content/4755.json","w"),indent=1,ensure_ascii=False)
