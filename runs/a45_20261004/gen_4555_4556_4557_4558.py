import json
def keys(T,d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
T21=[i*0.5 for i in range(21)]; T25=[i*0.5 for i in range(25)]
def save(c): json.dump(c,open("content/%d.json"%c["mediaId"],"w"),indent=1)

# ---- 4555
man={0.0:(0,0.33,0.72,0.67),0.5:(0,0.34,0.70,0.66),1.0:(0,0.34,0.66,0.66),1.5:(0,0.33,0.70,0.67),2.0:(0,0.32,0.56,0.68),
2.5:(0,0.35,0.44,0.65),3.0:(0,0.37,0.50,0.63),4.5:(0.32,0.34,0.36,0.44),5.0:(0.38,0.36,0.38,0.53),5.5:(0.42,0.38,0.34,0.60),
6.0:(0.46,0.39,0.42,0.50),6.5:(0.48,0.39,0.44,0.53),7.0:(0.52,0.40,0.46,0.60),7.5:(0.74,0.48,0.26,0.52),8.0:(0.62,0.38,0.38,0.62),
8.5:(0.62,0.38,0.38,0.62),9.0:(0.62,0.38,0.38,0.62),9.5:(0.54,0.34,0.46,0.66),10.0:(0.50,0.31,0.50,0.69)}
car={2.5:(0.45,0.14,0.45,0.34),3.0:(0.17,0.22,0.20,0.15),7.5:(0.24,0.50,0.18,0.14),8.0:(0.33,0.48,0.20,0.14),8.5:(0.33,0.48,0.20,0.14),
9.0:(0.33,0.51,0.20,0.14),9.5:(0.30,0.52,0.20,0.14),10.0:(0.31,0.52,0.18,0.14)}
save({"mediaId":4555,"level":"B","keyWord":"pine","defaultVoice":"male",
"taps":[
 {"phrase":"to grin at the camera","target":"the man","voice":"male","keys":keys(T21,man)},
 {"phrase":"to board a white gondola","target":"the man","voice":"male","keys":keys(T21,man)},
 {"phrase":"to glide past the pines","target":"the red cable car","voice":"male","keys":keys(T21,car)}],
"stillS":8.5,
"nouns":[{"word":"peaks","x":0.35,"y":0.23,"voice":"male"},{"word":"pines","x":0.20,"y":0.44,"voice":"male"},
 {"word":"a cable car","x":0.44,"y":0.56,"voice":"male"},{"word":"a slope","x":0.30,"y":0.76,"voice":"male"}],
"question":"What is the red cable car doing?",
"answer":["It","is","gliding","past","the","snowy","pines."],
"answerVoice":"male",
"notes":"Red cable car: the one passing the window at 2.5 s (left ninth of it is cut off the box where it touches the man's hat/hand; a sliver behind the pillar at 3.0 s) and the small distant cabins on the line at 7.5-10 s (min-size boxes). The man's own cabin is not a target. 3.5-4.0 s station shot without the man = off. He boards the white gondola at 4.5-5.5 s. 'pines' pill on the left stand of trees at 8.5 s; more pines stand right of the slope."})

# ---- 4556
woman={3.0:(0.10,0.0,0.90,1.0),3.5:(0.10,0.12,0.82,0.88),4.0:(0.28,0.17,0.57,0.68),4.5:(0.06,0.17,0.35,0.45),5.0:(0.02,0.20,0.47,0.66),
5.5:(0,0.21,0.45,0.60),6.0:(0,0.18,0.44,0.56),6.5:(0,0.23,0.45,0.59),7.0:(0,0.23,0.44,0.65),7.5:(0.06,0.24,0.33,0.52),
8.0:(0.09,0.26,0.29,0.40),8.5:(0.17,0.28,0.24,0.36),9.0:(0.20,0.32,0.21,0.34),9.5:(0.23,0.33,0.20,0.33),10.0:(0.26,0.33,0.19,0.30)}
mn={4.0:(0,0.21,0.27,0.67),4.5:(0.42,0.21,0.52,0.67),5.0:(0.50,0.22,0.50,0.75),5.5:(0.46,0.21,0.54,0.72),6.0:(0.45,0.24,0.55,0.58),
6.5:(0.46,0.26,0.54,0.52),7.0:(0.45,0.29,0.55,0.60),7.5:(0.42,0.33,0.50,0.52),8.0:(0.40,0.33,0.36,0.36),8.5:(0.43,0.34,0.28,0.30),
9.0:(0.43,0.37,0.26,0.30),9.5:(0.44,0.39,0.26,0.28),10.0:(0.46,0.37,0.22,0.25)}
scr={0.0:(0.02,0.27,0.96,0.66),0.5:(0.02,0.27,0.96,0.66),1.0:(0.02,0.28,0.96,0.66),1.5:(0.02,0.28,0.96,0.66),2.0:(0.0,0.30,0.98,0.62),2.5:(0,0.33,0.98,0.60)}
save({"mediaId":4556,"level":"B","keyWord":"praise","defaultVoice":"female",
"taps":[
 {"phrase":"to display a rising chart","target":"the laptop screen","voice":"female","keys":keys(T21,scr)},
 {"phrase":"to deliver two takeaway coffees","target":"the woman in glasses","voice":"female","keys":keys(T21,woman)},
 {"phrase":"to concentrate on his screen","target":"the man at the laptop","voice":"male","keys":keys(T21,mn)}],
"stillS":6.0,
"nouns":[{"word":"blinds","x":0.50,"y":0.13,"voice":"female"},{"word":"glasses","x":0.30,"y":0.33,"voice":"female"},
 {"word":"takeaway cups","x":0.28,"y":0.61,"voice":"female"},{"word":"a laptop","x":0.62,"y":0.75,"voice":"female"}],
"question":"What is the whole team doing?",
"answer":["They","are","praising","the","man","at","the","laptop."],
"answerVoice":"female",
"notes":"Key word 'praise' is a verb: used in the answer (the team applauds the seated man at 7.5-10 s). The clip differs from the description: the woman carries TWO takeaway cups and sets them on the desk. defaultVoice: no single main person (woman acts, man is praised) -> evenId true -> female. 'the laptop screen' = the chart laptop of the first shot (0-2.5 s, whole laptop boxed); afterwards only the lid's back is seen -> off. The man is off in 0-3.0 s (only hands / a shoulder). At 4.0-5.0 s woman and man overlap: split by a vertical line between their heads, so part of his shoulder lies in her box. Everybody claps at the end, the man too, so no 'applaud' phrase."})

# ---- 4557
m={0.0:(0,0.07,0.95,0.86),0.5:(0,0.18,0.95,0.70),1.0:(0,0.18,0.93,0.76),1.5:(0,0.14,0.94,0.86),2.0:(0,0.14,0.92,0.76),2.5:(0,0.12,0.90,0.78),
3.0:(0,0.14,0.90,0.84),3.5:(0,0.14,0.90,0.84),4.0:(0,0.12,0.97,0.76),4.5:(0,0.12,1.0,0.76),5.0:(0.04,0.14,0.86,0.84),5.5:(0.24,0.14,0.66,0.84),
6.0:(0.04,0.14,0.86,0.35),6.5:(0.04,0.14,0.86,0.30),7.0:(0.04,0.18,0.86,0.29),7.5:(0.04,0.16,0.86,0.32),8.0:(0.03,0.14,0.86,0.37),
8.5:(0.03,0.14,0.86,0.43),9.0:(0.02,0.16,0.86,0.43),9.5:(0.02,0.16,0.86,0.43),10.0:(0.02,0.14,0.86,0.45)}
dog={5.5:(0,0.55,0.23,0.37),6.0:(0,0.50,0.62,0.36),6.5:(0,0.45,0.94,0.40),7.0:(0,0.48,0.92,0.40),7.5:(0.15,0.49,0.82,0.48),
8.0:(0.07,0.52,0.82,0.36),8.5:(0.09,0.58,0.86,0.31),9.0:(0.08,0.60,0.84,0.37),9.5:(0.08,0.60,0.86,0.37),10.0:(0.08,0.60,0.84,0.31)}
save({"mediaId":4557,"level":"B","keyWord":"lap","defaultVoice":"male",
"taps":[
 {"phrase":"to unfold a tartan blanket","target":"the man","voice":"male","keys":keys(T21,m)},
 {"phrase":"to sip from a mug","target":"the man","voice":"male","keys":keys(T21,m)},
 {"phrase":"to curl up on his lap","target":"the dog","voice":"male","keys":keys(T21,dog)}],
"stillS":10.0,
"nouns":[{"word":"a mug","x":0.48,"y":0.43,"voice":"male"},{"word":"a blanket","x":0.30,"y":0.54,"voice":"male"},
 {"word":"a retriever","x":0.50,"y":0.68,"voice":"male"},{"word":"a footstool","x":0.50,"y":0.90,"voice":"male"}],
"question":"What is the retriever doing?",
"answer":["It","is","curling","up","on","the","man's","lap."],
"answerVoice":"male",
"notes":"Key word 'lap' is not placed as a noun (it is the spot the dog lies on, would collide with 'a retriever'); it is in a phrase and in the answer. From 6.0 s the dog lies across the man's legs: boxes split by a horizontal line, man = upper body, dog = everything below, so his socks fall into the dog's box. At 5.5 s the dog's head enters bottom left and the man's box starts right of it."})

# ---- 4558
M={0.0:(0,0.28,0.49,0.72),0.5:(0,0.26,0.49,0.74),1.0:(0,0.24,0.50,0.76),1.5:(0,0.21,0.55,0.79),2.0:(0,0.18,0.55,0.82),2.5:(0,0.16,0.55,0.84),
3.0:(0,0.16,0.53,0.84),3.5:(0,0.16,0.55,0.84),4.0:(0,0.16,0.56,0.84),4.5:(0.28,0.30,0.44,0.60),5.0:(0.24,0.31,0.44,0.62),5.5:(0.30,0.30,0.39,0.64),
6.0:(0.30,0.28,0.38,0.64),6.5:(0.38,0.26,0.25,0.62),7.0:(0.40,0.24,0.22,0.64),7.5:(0.39,0.22,0.23,0.66),8.0:(0.38,0.18,0.24,0.72),
8.5:(0.38,0.16,0.26,0.76),9.0:(0.32,0.14,0.34,0.84),9.5:(0.30,0.12,0.37,0.88),10.0:(0.27,0.10,0.42,0.90),10.5:(0.26,0.08,0.43,0.92),
11.0:(0.24,0.08,0.45,0.92),11.5:(0.24,0.08,0.45,0.92),12.0:(0.24,0.06,0.47,0.94)}
W={0.0:(0.50,0.03,0.50,0.62),0.5:(0.50,0.02,0.50,0.64),1.0:(0.51,0.10,0.49,0.72),1.5:(0.56,0.10,0.44,0.60),2.0:(0.56,0.10,0.44,0.55),
2.5:(0.56,0.10,0.44,0.50),3.0:(0.54,0.12,0.46,0.52),3.5:(0.56,0.14,0.44,0.52),4.0:(0.57,0.13,0.43,0.55),4.5:(0.73,0.30,0.27,0.58),
5.0:(0.69,0.33,0.31,0.60),5.5:(0.70,0.32,0.30,0.60),6.0:(0.69,0.29,0.31,0.50),6.5:(0.64,0.28,0.21,0.36),7.0:(0.63,0.29,0.19,0.36),
7.5:(0.63,0.28,0.19,0.36),8.0:(0.63,0.26,0.20,0.38),8.5:(0.65,0.25,0.21,0.40),9.0:(0.67,0.25,0.29,0.42),9.5:(0.68,0.22,0.32,0.48),
10.0:(0.70,0.21,0.30,0.50),10.5:(0.70,0.21,0.30,0.52),11.0:(0.70,0.22,0.30,0.50),11.5:(0.70,0.22,0.30,0.50),12.0:(0.72,0.20,0.28,0.50)}
save({"mediaId":4558,"level":"B","keyWord":"support","defaultVoice":"male",
"taps":[
 {"phrase":"to sob on the sofa","target":"the young man","voice":"male","keys":keys(T25,M)},
 {"phrase":"to clutch a mug of tea","target":"the young man","voice":"male","keys":keys(T25,M)},
 {"phrase":"to wrap him in a blanket","target":"the woman with braids","voice":"female","keys":keys(T25,W)}],
"stillS":5.0,
"nouns":[{"word":"fairy lights","x":0.55,"y":0.12,"voice":"male"},{"word":"a blanket","x":0.40,"y":0.50,"voice":"male"},
 {"word":"a mug","x":0.50,"y":0.62,"voice":"male"},{"word":"a coffee table","x":0.40,"y":0.95,"voice":"male"}],
"question":"What are the friends around him doing?",
"answer":["They","are","hugging","him","to","show","support."],
"answerVoice":"male",
"notes":"Key word 'support' is abstract: only in the answer. The woman with braids wraps the blanket round him at 0-1.5 s and holds him afterwards; her arm lies across him, boxes split by a vertical line between the two heads (in the first shot his mug hand lies below her box, in neither). Three more women join from 4.5 s; they are not targets. Two phrases share the young man."})
