import json
OFF="off"
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t,OFF)
        if v==OFF: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 893
t=T(9)
p={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),2.0:(0,0.03,1,0.97),2.5:(0,0.08,1,0.92),3.0:(0,0.10,1,0.90),3.5:(0,0.10,1,0.90),4.0:(0,0.10,1,0.90)}
k=keys(t,p)
dump({"mediaId":893,"level":"A","keyWord":"zip","defaultVoice":"male",
 "taps":[{"phrase":"to zip up a jacket","target":"the person","voice":"male","keys":k},
         {"phrase":"to put up a hood","target":"the person","voice":"male","keys":k},
         {"phrase":"to smile in the snow","target":"the person","voice":"male","keys":k}],
 "stillS":4.0,
 "nouns":[{"word":"a hood","x":0.50,"y":0.17,"voice":"male"},{"word":"a face","x":0.50,"y":0.31,"voice":"male"},
          {"word":"a jacket","x":0.50,"y":0.70,"voice":"male"},{"word":"snow","x":0.87,"y":0.86,"voice":"male"}],
 "question":"What is the person doing?",
 "answer":["The","person","is","zipping up","a","jacket."],
 "answerVoice":"male",
 "notes":"Only one possible target (one animated person fills the frame), so all three phrases share it; the box is nearly the whole picture. Gender of the character is not clear (packet says 'young person'), so I used 'the person' and the default voice (odd id -> male). 'zipping up' is kept as ONE chip so the particle cannot be placed after the object. First two frames are a close-up of the torso and hand only."})

# 894
t=T(21)
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),2.0:(0.11,0.07,0.89,0.93),2.5:(0.27,0.20,0.73,0.80),3.0:(0.30,0.22,0.70,0.78),
   3.5:(0.25,0.28,0.75,0.72),4.0:(0.30,0.18,0.70,0.82),4.5:(0.20,0.08,0.80,0.92),5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:(0,0,1,1),6.5:(0,0,1,1),7.0:(0,0,1,1),
   7.5:(0.27,0.30,0.63,0.70),8.0:(0.25,0.38,0.63,0.62),8.5:(0.24,0.40,0.60,0.60),9.0:(0.31,0.43,0.69,0.57),9.5:(0.40,0.41,0.60,0.59),10.0:(0.43,0.40,0.57,0.60)}
M={2.0:(0,0.20,0.11,0.55),2.5:(0,0.24,0.27,0.74),3.0:(0,0.27,0.30,0.73),3.5:(0,0.24,0.25,0.36),4.0:(0,0.20,0.30,0.38),4.5:(0,0.17,0.20,0.35),
   7.5:(0,0.30,0.27,0.32),8.0:(0,0.37,0.25,0.63),8.5:(0,0.39,0.24,0.61),9.0:(0,0.40,0.31,0.60),9.5:(0,0.40,0.40,0.60),10.0:(0,0.40,0.43,0.60)}
B={8.0:(0.30,0.03,0.26,0.16),8.5:(0.31,0.07,0.24,0.16),9.0:(0.31,0.09,0.25,0.16),9.5:(0.28,0.07,0.29,0.18)}
dump({"mediaId":894,"level":"A","keyWord":"zipper","defaultVoice":"female",
 "taps":[{"phrase":"to pull up a zipper","target":"the woman","voice":"female","keys":keys(t,W)},
         {"phrase":"to watch the woman","target":"the man","voice":"male","keys":keys(t,M)},
         {"phrase":"to sit on the roof","target":"the bird","voice":"female","keys":keys(t,B)}],
 "stillS":8.0,
 "nouns":[{"word":"a bird","x":0.43,"y":0.11,"voice":"female"},{"word":"a hat","x":0.53,"y":0.45,"voice":"female"},
          {"word":"a man","x":0.14,"y":0.58,"voice":"male"},{"word":"a zipper","x":0.52,"y":0.76,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","closing","the","zipper","on","her","jacket."],
 "answerVoice":"female",
 "notes":"Frames 0.0-1.0 are an extreme close-up of the woman's jacket only (box = whole picture). Man and woman overlap in most frames: boxes are split along a vertical line, so parts of her left arm fall outside her box. Man is 'off' at 5.0-7.0 where only a blurred dark edge of him shows. The bird (a magpie on the roof) appears only from 8.0 and lifts its wings at 9.5. Answer avoids 'pulling up' so the particle position is not ambiguous."})

# 4001
t=T(15)
J={0.0:(0,0.25,1,0.55),0.5:(0,0.32,1,0.48),1.0:(0.46,0.27,0.54,0.59),1.5:(0.47,0.28,0.53,0.58),2.0:(0,0.25,1,0.55),2.5:(0,0.25,1,0.40),3.0:(0,0.26,1,0.36),
   3.5:(0,0.27,1,0.36),4.0:(0,0.26,1,0.33),4.5:(0,0.25,1,0.45),5.0:(0,0.26,1,0.54),5.5:(0,0.27,1,0.60),6.0:(0.33,0.26,0.67,0.54),6.5:(0,0.36,1,0.44),7.0:(0,0.42,1,0.50)}
H={0.5:(0,0.10,0.68,0.22),1.0:(0,0.18,0.46,0.32),1.5:(0,0.28,0.47,0.30),6.0:(0,0.12,0.33,0.27),6.5:(0,0.12,0.56,0.24),7.0:(0,0.04,0.48,0.38)}
F={2.5:(0.30,0.65,0.37,0.35),3.0:(0.32,0.62,0.34,0.38),3.5:(0.34,0.63,0.34,0.37),4.0:(0.33,0.59,0.34,0.36)}
dump({"mediaId":4001,"level":"B","keyWord":"fighter","defaultVoice":"male",
 "taps":[{"phrase":"to toast slices of bread","target":"the fighter","voice":"male","keys":keys(t,J)},
         {"phrase":"to insert two slices","target":"the hand","voice":"male","keys":keys(t,H)},
         {"phrase":"to burst from the exhaust","target":"the flame","voice":"male","keys":keys(t,F)}],
 "stillS":3.0,
 "nouns":[{"word":"cabinets","x":0.55,"y":0.15,"voice":"male"},{"word":"a fighter","x":0.50,"y":0.46,"voice":"male"},
          {"word":"a flame","x":0.48,"y":0.72,"voice":"male"},{"word":"a countertop","x":0.76,"y":0.84,"voice":"male"}],
 "question":"What is the fighter doing?",
 "answer":["The","fighter","is","toasting","slices","of","bread."],
 "answerVoice":"male",
 "notes":"The fighter is a model jet that works as a toaster. The hand covers part of the jet at 0.5-1.5 and 6.0-7.0: boxes are split, at 1.0/1.5 along a vertical line (the fingertips reach a little into the jet box), at 6.0 the jet's left wing is outside its box. The flame leaves the nozzle and runs down the counter: jet box ends and flame box starts at the nozzle. The slice the hand holds counts to the hand box. No person visible except the hand -> default voice by odd id."})

# 4002
t=T(15)
Mo={0.0:(0.74,0.34,0.26,0.44),0.5:(0.74,0.34,0.26,0.44),1.0:(0.75,0.35,0.25,0.44),1.5:(0.69,0.34,0.31,0.45)}
A={3.0:(0.46,0.39,0.24,0.30),3.5:(0.35,0.27,0.27,0.42),4.0:(0.37,0.23,0.25,0.46),4.5:(0.40,0.24,0.24,0.45),5.0:(0.40,0.24,0.22,0.46),5.5:(0.42,0.24,0.22,0.46),
   6.0:(0.40,0.24,0.24,0.46),6.5:(0.42,0.25,0.22,0.45),7.0:(0.40,0.25,0.22,0.45)}
Ta={3.0:(0.18,0.69,0.76,0.31),3.5:(0.10,0.69,0.76,0.31),4.0:(0.10,0.69,0.76,0.31),4.5:(0.10,0.69,0.76,0.31),5.0:(0.10,0.70,0.77,0.30),5.5:(0.10,0.70,0.78,0.30),
    6.0:(0.10,0.70,0.78,0.30),6.5:(0.10,0.70,0.78,0.30),7.0:(0.10,0.70,0.78,0.30)}
dump({"mediaId":4002,"level":"B","keyWord":"balance","defaultVoice":"female",
 "taps":[{"phrase":"to balance on her hands","target":"the woman on the table","voice":"female","keys":keys(t,A)},
         {"phrase":"to support her weight","target":"the table","voice":"female","keys":keys(t,Ta)},
         {"phrase":"to display lines of text","target":"the monitor","voice":"female","keys":keys(t,Mo)}],
 "stillS":5.5,
 "nouns":[{"word":"the ceiling","x":0.45,"y":0.10,"voice":"female"},{"word":"boots","x":0.52,"y":0.32,"voice":"female"},
          {"word":"a tabletop","x":0.46,"y":0.74,"voice":"female"},{"word":"chairs","x":0.88,"y":0.85,"voice":"female"}],
 "question":"What is happening on the table?",
 "answer":["A","woman","is","keeping","her","balance","on","her","hands."],
 "answerVoice":"female",
 "notes":"Two shots joined by a whip pan (2.0 and 2.5 are pure blur: everything off). Shot 1: two women typing (both do the same, so neither is a target) -> the monitor is the target there. Shot 2: the cheering colleagues all film and raise their arms, no action fits only one of them, so the second and third targets are the gymnast and the table. The table box starts just under her hands, so the far end of the tabletop behind her is not in it and legs of bystanders are. 'chairs' sits on the group at the right; a few chairs also stand at the left edge."})
