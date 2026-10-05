import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0,0.08,1,0.82),0.5:(0,0,1,0.72),1.0:(0,0,0.62,0.93),1.5:(0.03,0.08,0.97,0.8),2.0:(0,0,1,0.85),2.5:(0,0.02,0.33,0.7),
3.0:(0,0.48,0.34,0.3),3.5:(0,0,0.57,1),4.0:(0.2,0.57,0.8,0.43),4.5:(0.66,0,0.2,0.25),5.0:(0.53,0,0.31,0.27),5.5:(0.53,0,0.34,0.22),
6.0:(0,0,0.75,1),7.0:(0,0.16,0.49,0.84),7.5:(0,0.23,0.52,0.52),8.0:(0,0.2,0.42,0.8),8.5:(0,0.1,0.24,0.9),9.5:(0,0.08,0.18,0.92),10.0:(0,0.2,0.38,0.8)}
man={4.5:(0,0.26,0.92,0.5),5.0:(0,0.28,0.88,0.58),5.5:(0.02,0.23,0.9,0.63),6.5:(0.08,0.23,0.92,0.77),7.0:(0.6,0.16,0.4,0.53),
7.5:(0.54,0.23,0.46,0.52),8.0:(0.6,0.19,0.4,0.53),8.5:(0.5,0.1,0.5,0.7),9.0:(0.66,0.42,0.34,0.2),9.5:(0.56,0,0.44,1),10.0:(0.5,0.19,0.5,0.57)}
cat={7.0:(0.5,0.7,0.25,0.14),7.5:(0.44,0.76,0.27,0.14),8.0:(0.43,0.73,0.25,0.15),8.5:(0.36,0.81,0.32,0.18),10.0:(0.39,0.77,0.25,0.15)}
c={"mediaId":653,"level":"A","keyWord":"searching","defaultVoice":"male",
"taps":[{"phrase":"to pick up a pillow","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to point at the keys","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to lie by the door","target":"the cat","voice":"male","keys":keys(cat)}],
"stillS":10.0,
"nouns":[{"word":"keys","x":0.52,"y":0.57,"voice":"male"},{"word":"a door","x":0.42,"y":0.25,"voice":"male"},
{"word":"a cat","x":0.48,"y":0.85,"voice":"male"},{"word":"a man","x":0.82,"y":0.45,"voice":"male"}],
"question":"What is the man pointing at?","answer":["He","is","pointing","at","the","keys","in","the","door."],"answerVoice":"male",
"notes":"The key word 'searching' is not a visible noun, so it is not among the nouns. The keys are small in the still (hanging in the lock at the man's hand). 2.5-3.0 s and 4.0 s show only the woman's hands / the back of her head. 6.5 s: the cat is a tiny blur behind the man -> cat off. Where the cat lies between the two people (7.0-10.0 s) the people's boxes end above it, their lower legs are not boxed. 9.0 s: only the man's hand and sleeve."}
json.dump(c,open('content/653.json','w'),ensure_ascii=False,indent=1)
