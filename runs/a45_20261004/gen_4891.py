import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
S={0.0:(0.20,0.25,0.80,0.75),0.5:(0.24,0.25,0.76,0.75),1.0:(0.05,0.33,0.95,0.67),1.5:(0.08,0.38,0.92,0.62),
   2.0:(0.0,0.40,1.0,0.60),2.5:(0.0,0.42,0.84,0.58),3.0:(0.0,0.30,1.0,0.70),3.5:(0.0,0.31,1.0,0.69),
   4.0:(0.0,0.37,1.0,0.63),4.5:(0.0,0.29,1.0,0.71),5.0:(0.0,0.38,1.0,0.62),5.5:(0.0,0.39,1.0,0.61),
   6.0:(0.0,0.41,1.0,0.59),6.5:(0.0,0.41,1.0,0.59),7.0:(0.0,0.45,1.0,0.55),7.5:(0.0,0.46,1.0,0.54),
   8.0:(0.0,0.47,1.0,0.53),8.5:(0.0,0.46,1.0,0.54),9.0:(0.0,0.47,1.0,0.53)}
TW={7.5:(0.82,0.02,0.18,0.14),8.0:(0.82,0.04,0.18,0.15),8.5:(0.82,0.05,0.18,0.16),9.0:(0.82,0.06,0.18,0.16)}
TR={0.0:(0,0,1,0.25),0.5:(0,0,1,0.25),1.0:(0,0,1,0.33),1.5:(0,0,1,0.38),2.0:(0,0,1,0.40),2.5:(0.13,0,0.87,0.42),
    3.0:(0,0,1,0.30),3.5:(0,0,1,0.31),4.0:(0.18,0,0.82,0.37),4.5:(0,0,1,0.29),5.0:(0,0,1,0.38),5.5:(0,0,1,0.39),
    6.0:(0,0,1,0.41),6.5:(0,0,1,0.41),7.0:(0,0,1,0.45),7.5:(0,0.16,1,0.30),8.0:(0,0.19,1,0.28),8.5:(0,0.21,1,0.25),9.0:(0,0.22,1,0.25)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":4891,"level":"A","keyWord":"campus","defaultVoice":"female",
 "taps":[
  {"phrase":"to lean to one side","target":"the students","voice":"female","keys":keys(S)},
  {"phrase":"to rise high above the trees","target":"the tall tower","voice":"female","keys":keys(TW)},
  {"phrase":"to have green leaves","target":"the trees","voice":"female","keys":keys(TR)}],
 "stillS":9.0,
 "nouns":[{"word":"the sky","x":0.30,"y":0.07,"voice":"female"},{"word":"grass","x":0.65,"y":0.92,"voice":"female"},
          {"word":"trees","x":0.30,"y":0.32,"voice":"female"},{"word":"students","x":0.50,"y":0.62,"voice":"female"}],
 "question":"What are the students doing?",
 "answer":["They","are","leaning","to","one","side."],
 "answerVoice":"female",
 "notes":"Rewrite after first FAIL: no single student is unique (all lean and laugh, many white tops), so the students are ONE group target (box = all people, like 'the group' in 166 / 'the students' in 21). Unique things: the tall tower with a spire, only visible 7.5-9.0 s (small, top right, partly behind a tree crown; off before), and the trees. Trees/students/tower boxes split along the lines between them, so a few tree crowns (top 0.10-0.20 at 7.5-9.0) and at 4.0 s the left boy's head fall outside their boxes. 'rise high above' is A2/B1, the plainest correct verb for a tower over trees; 'high' because two smaller tower blocks (9.0 s: x 0.05 y 0.17, x 0.37 y 0.25) only peek between the tree tops - they lie in the trees box. No noun 'a tower': at 9.0 s three tower blocks are visible, so it would not label one place. At 2.5 s the brunette's head (left edge, y 0.20-0.42) is outside every box so the tree area above the blonde girl is not counted as students. 'campus' is not one visible thing, so no noun for it. defaultVoice female: main person is the blonde girl; the group is mixed."}
json.dump(c,open('content/4891.json','w'),indent=1)
