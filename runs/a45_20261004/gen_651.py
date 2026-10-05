import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0,0.45,0.32,0.55),0.5:(0,0.45,0.38,0.55),1.0:(0,0.46,0.47,0.54),1.5:(0,0.46,0.78,0.3),2.0:(0,0.41,0.78,0.33),
2.5:(0,0.46,0.78,0.26),3.0:(0,0.44,0.78,0.3),3.5:(0,0.46,0.8,0.27),4.0:(0,0.47,0.68,0.53),4.5:(0,0.45,0.68,0.55),
5.0:(0,0.46,0.68,0.54),5.5:(0,0.45,0.78,0.5),6.0:(0,0.45,0.8,0.3),6.5:(0,0.07,0.6,0.5),
7.5:(0,0.08,0.11,0.92),8.0:(0,0.1,0.36,0.9),8.5:(0.12,0.11,0.46,0.47),9.0:(0.13,0.13,0.42,0.46),9.5:(0.15,0.08,0.55,0.5),10.0:(0,0.06,0.46,0.94)}
man={0.0:(0.03,0.12,0.47,0.32),0.5:(0.12,0.14,0.48,0.3),1.0:(0.21,0.17,0.3,0.28),1.5:(0,0.08,0.36,0.37),2.0:(0,0.06,0.3,0.34),
2.5:(0,0.06,0.28,0.39),3.0:(0,0.08,0.3,0.35),3.5:(0,0.08,0.36,0.37),4.0:(0.22,0.19,0.28,0.26),4.5:(0.27,0.24,0.2,0.2),
5.0:(0.28,0.25,0.18,0.2),5.5:(0.11,0.1,0.25,0.34),6.0:(0,0.08,0.36,0.36),7.0:(0,0.08,0.56,0.5),7.5:(0.12,0.1,0.34,0.5),
8.5:(0,0.13,0.11,0.87),9.0:(0,0.18,0.12,0.82),9.5:(0,0.16,0.14,0.84)}
cat={6.5:(0.14,0.58,0.2,0.16),7.0:(0.08,0.59,0.25,0.16),7.5:(0.2,0.61,0.2,0.16),8.0:(0.37,0.6,0.18,0.17),8.5:(0.47,0.6,0.18,0.16),
9.0:(0.47,0.6,0.18,0.16),9.5:(0.48,0.6,0.18,0.16),10.0:(0.47,0.58,0.18,0.16)}
c={"mediaId":651,"level":"B","keyWord":"screwdriver","defaultVoice":"female",
"taps":[{"phrase":"to tighten a screw","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to steady the wooden shelf","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to perch on the sofa","target":"the cat","voice":"female","keys":keys(cat)}],
"stillS":8.0,
"nouns":[{"word":"a screwdriver","x":0.33,"y":0.5,"voice":"female"},{"word":"books","x":0.76,"y":0.52,"voice":"female"},
{"word":"a cat","x":0.42,"y":0.67,"voice":"female"},{"word":"a houseplant","x":0.5,"y":0.39,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","tightening","a","screw","with","a","screwdriver."],"answerVoice":"female",
"notes":"The two people overlap in most shots: 0.0-6.0 s the woman's box is the lower part (her body and the hands with the screwdriver), the man's box his head and the hand on the shelf; her face at the left edge is not boxed there. 6.5 s man almost hidden -> off; 7.0 s only her hand at the edge -> woman off; 8.0 and 10.0 s man hidden / a sliver -> off. Whose hands stack the books (6.5-7.5 s) is unclear, so no phrase uses it. The cat sits on the back of a dark sofa/armchair, small in the picture."}
json.dump(c,open('content/651.json','w'),ensure_ascii=False,indent=1)
