import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
T21=[i*0.5 for i in range(21)]; T19=[i*0.5 for i in range(19)]
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)
F=(0,0,1,1)
# 776
man={0.0:(0.10,0.05,0.90,0.95),0.5:(0.08,0.05,0.92,0.95),1.0:(0.0,0.05,1.0,0.95),1.5:(0.08,0.10,0.92,0.90),
 2.0:(0.0,0.12,0.95,0.88),2.5:(0.0,0.10,0.95,0.90),3.0:F,3.5:F,4.0:F,4.5:F,5.0:F,5.5:F,6.0:(0.35,0,0.65,1.0),
 6.5:(0.76,0,0.24,1.0),7.0:(0.66,0,0.34,1.0),7.5:(0.28,0,0.72,1.0),8.0:F,8.5:F,9.0:F,9.5:F,10.0:F}
spr={6.5:(0.0,0.36,0.74,0.30),7.0:(0.0,0.38,0.64,0.34)}
save({"mediaId":776,"level":"B","keyWord":"thirst","defaultVoice":"male","taps":[
 {"phrase":"to tip up a bottle","target":"the cyclist","voice":"male","keys":K(T21,man)},
 {"phrase":"to suffer from thirst","target":"the cyclist","voice":"male","keys":K(T21,man)},
 {"phrase":"to spray a distant field","target":"the sprinkler","voice":"male","keys":K(T21,spr)}],
 "stillS":0.0,"nouns":[{"word":"a plastic bottle","x":0.76,"y":0.54,"voice":"male"},{"word":"a wire basket","x":0.40,"y":0.79,"voice":"male"},{"word":"a bicycle bell","x":0.27,"y":0.62,"voice":"male"}],
 "question":"What is the cyclist suffering from?","answer":["He","is","suffering","from","thirst."],"answerVoice":"male",
 "notes":"Sprinkler only visible at 6.5 and 7.0 s (short tap window). 'to suffer from thirst' rests on the grimace, tongue out and empty bottle. Bell and bottle pills are close in y (0.08) but 0.49 apart in x."})
# 777
m={0.0:(0.08,0.14,0.92,0.74),0.5:(0.10,0.14,0.90,0.74),1.0:(0.05,0.15,0.90,0.78),1.5:(0.13,0.16,0.83,0.78),2.0:(0.05,0.16,0.88,0.70),
 2.5:(0.18,0.21,0.82,0.65),3.0:(0.0,0.08,0.92,0.88),3.5:(0.0,0.08,1.0,0.88),4.0:(0.0,0.17,0.93,0.72),4.5:(0.02,0.19,0.95,0.74),
 5.0:(0.02,0.17,0.90,0.78),5.5:(0.04,0.17,0.88,0.72),6.0:(0.0,0.15,1.0,0.70),6.5:(0.0,0.17,1.0,0.72),7.0:(0.0,0.19,0.98,0.76),
 7.5:(0.0,0.18,0.96,0.76),8.0:(0.0,0.12,0.98,0.78),8.5:(0.0,0.20,0.98,0.70),9.0:(0.15,0.20,0.80,0.75),9.5:(0.06,0.19,0.90,0.78),10.0:(0.0,0.17,0.92,0.72)}
save({"mediaId":777,"level":"A","keyWord":"thirsty","defaultVoice":"male","taps":[
 {"phrase":"to drink from a glass","target":"the man","voice":"male","keys":K(T21,m)},
 {"phrase":"to wipe his mouth","target":"the man","voice":"male","keys":K(T21,m)},
 {"phrase":"to hold an empty bottle","target":"the man","voice":"male","keys":K(T21,m)}],
 "stillS":10.0,"nouns":[{"word":"a glass","x":0.20,"y":0.42,"voice":"male"},{"word":"a bottle","x":0.15,"y":0.92,"voice":"male"},{"word":"tomatoes","x":0.80,"y":0.93,"voice":"male"},{"word":"a shirt","x":0.50,"y":0.67,"voice":"male"}],
 "question":"What is the thirsty man doing?","answer":["He","is","drinking","water","from","a","glass."],"answerVoice":"male",
 "notes":"Only one clear target (the seller); background people are blurred. All three phrases use him."})
# 778
beige={0.0:(0.0,0.0,0.37,1.0),0.5:(0.40,0.13,0.60,0.87),1.0:(0.66,0.19,0.34,0.81),1.5:(0.65,0.21,0.35,0.79),2.0:(0.30,0.22,0.70,0.78),
 2.5:(0.30,0.22,0.70,0.78),3.0:(0.30,0.22,0.70,0.78),3.5:(0.36,0.18,0.64,0.82),4.0:(0.43,0.16,0.57,0.84),4.5:(0.43,0.14,0.57,0.86),
 5.0:(0,0,1,0.70),5.5:(0,0,1,0.70),6.0:(0,0,1,0.62),6.5:(0,0,1,0.62),7.0:(0,0,1,0.68),7.5:(0,0,1,0.68),8.0:(0,0,1,0.56),8.5:(0,0,1,0.52),9.0:(0,0,1,0.63),
 9.5:(0.0,0.12,0.30,0.54),10.0:(0.0,0.12,0.29,0.52)}
green={0.0:(0.38,0.27,0.25,0.37),0.5:(0.08,0.23,0.31,0.43),1.0:(0.03,0.25,0.46,0.51),1.5:(0.0,0.26,0.43,0.50),2.0:(0.0,0.24,0.25,0.60),
 2.5:(0.0,0.24,0.24,0.58),3.0:(0.0,0.24,0.25,0.66),3.5:(0.0,0.22,0.35,0.32),4.0:(0.05,0.20,0.37,0.33),4.5:(0.05,0.20,0.37,0.33),
 9.5:(0.56,0.16,0.44,0.35),10.0:(0.50,0.15,0.50,0.33)}
cat={0.0:(0.64,0.47,0.18,0.14),1.0:(0.50,0.48,0.15,0.14),1.5:(0.44,0.47,0.20,0.14),9.5:(0.56,0.52,0.44,0.14),10.0:(0.30,0.49,0.60,0.19)}
save({"mediaId":778,"level":"B","keyWord":"thread","defaultVoice":"female","taps":[
 {"phrase":"to hold up a spool","target":"the woman in green","voice":"female","keys":K(T21,green)},
 {"phrase":"to snip off the thread","target":"the woman in beige","voice":"female","keys":K(T21,beige)},
 {"phrase":"to wander across the table","target":"the cat","voice":"female","keys":K(T21,cat)}],
 "stillS":2.5,"nouns":[{"word":"thread","x":0.47,"y":0.25,"voice":"female"},{"word":"a basket","x":0.25,"y":0.82,"voice":"female"},{"word":"a tape measure","x":0.78,"y":0.70,"voice":"female"}],
 "question":"What is the woman in beige holding?","answer":["She","is","holding","a","long","red","thread."],"answerVoice":"female",
 "notes":"Hard clip for boxes: the two women overlap at 0.0-4.5 s (split along the line between them; at 3.5-4.5 the beige woman's left hand lies in front of the green woman's face and is outside the beige box). 5.0-9.0 s close-up shows only the beige woman's hands and torso (identified by the tape measure). Cat is small behind the basket at 0.0/1.0/1.5 s, hidden at 0.5 s, on the table at 9.5-10.0 s; at 1.0 s its box is squeezed between the women (0.15 wide). 'to wander across the table' rests on the cat's change of position between 9.5 and 10.0 s."})
# 779
ot={0.0:(0.25,0.12,0.75,0.74),0.5:(0.14,0.17,0.86,0.80),1.0:(0.0,0.19,1.0,0.59),1.5:(0.0,0.17,1.0,0.58),2.0:(0.03,0.14,0.97,0.60),2.5:(0.04,0.13,0.96,0.62),
 3.0:(0.04,0.13,0.96,0.65),3.5:(0.21,0.21,0.79,0.47),4.0:(0.16,0.21,0.84,0.50),4.5:(0.16,0.23,0.84,0.50),5.0:(0.16,0.24,0.84,0.50),5.5:(0.16,0.26,0.84,0.50),
 6.0:(0.16,0.24,0.84,0.48),6.5:(0.16,0.24,0.84,0.48),7.0:(0.16,0.24,0.84,0.48),7.5:(0.11,0.17,0.71,0.68),8.0:(0.08,0.16,0.61,0.70),8.5:(0.08,0.15,0.59,0.70),9.0:(0.10,0.16,0.61,0.70)}
hand={7.5:(0.83,0.27,0.17,0.28),8.0:(0.70,0.17,0.30,0.50),8.5:(0.68,0.14,0.32,0.55),9.0:(0.72,0.17,0.28,0.58)}
save({"mediaId":779,"level":"B","keyWord":"otter","defaultVoice":"male","taps":[
 {"phrase":"to snuggle against an arm","target":"the otter","voice":"male","keys":K(T19,ot)},
 {"phrase":"to doze off peacefully","target":"the otter","voice":"male","keys":K(T19,ot)},
 {"phrase":"to stroke a furry cheek","target":"the hand","voice":"male","keys":K(T19,hand)}],
 "stillS":8.0,"nouns":[{"word":"an otter","x":0.38,"y":0.30,"voice":"male"},{"word":"an arm","x":0.30,"y":0.80,"voice":"male"},{"word":"a thumb","x":0.84,"y":0.55,"voice":"male"},{"word":"a sleeve","x":0.17,"y":0.12,"voice":"male"}],
 "question":"What is the otter doing?","answer":["It","is","snuggling","against","an","arm."],"answerVoice":"male",
 "notes":"The stroking hand is only visible from 7.5 s; at 8.0-9.0 the otter's right paw below the hand falls partly outside the otter box (split along the hand). The person is only an arm and a grey sleeve, so not used as a target."})
