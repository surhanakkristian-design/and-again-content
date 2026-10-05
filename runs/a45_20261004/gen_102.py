import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n,step=0.5,start=0.0): return [round(start+i*step,1) for i in range(n)]
def write(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 102
t=T(21)
man={0.0:(0,0.35,0.95,0.65),0.5:(0,0.35,0.95,0.65),1.0:(0,0.35,0.95,0.65),1.5:(0,0.35,0.95,0.65),
 2.5:(0,0.32,0.96,0.68),3.0:(0.20,0.18,0.80,0.82),3.5:(0,0.20,1.0,0.80),4.0:(0,0.27,0.88,0.60),
 4.5:(0.08,0.24,0.92,0.62),5.0:(0.08,0.34,0.92,0.62),5.5:(0.36,0.51,0.34,0.49),6.0:(0.36,0.53,0.36,0.47),
 6.5:(0.05,0.18,0.90,0.82),7.0:(0,0.22,0.70,0.76),8.0:(0.46,0.08,0.54,0.72),8.5:(0.50,0.08,0.50,0.80),
 9.0:(0.50,0.08,0.50,0.84),9.5:(0.05,0.53,0.90,0.47),10.0:(0,0.53,0.95,0.47)}
sock={0.0:(0.49,0.19,0.20,0.14),0.5:(0.51,0.15,0.19,0.14),1.0:(0.22,0.16,0.20,0.14),1.5:(0.10,0.20,0.20,0.14),
 7.5:(0.25,0.60,0.22,0.17),8.0:(0.20,0.56,0.25,0.20),8.5:(0.12,0.36,0.28,0.32),9.0:(0.12,0.37,0.30,0.32),
 9.5:(0.50,0.39,0.38,0.14),10.0:(0.50,0.39,0.38,0.14)}
bag={5.5:(0.14,0.35,0.80,0.16),6.0:(0.17,0.17,0.73,0.36),6.5:(0.18,0.0,0.66,0.17)}
write({"mediaId":102,"level":"B","keyWord":"boredom","defaultVoice":"male",
 "taps":[
  {"phrase":"to slump in a plastic chair","target":"the man","voice":"male","keys":keys(t,man)},
  {"phrase":"to dangle from his fingers","target":"the sock","voice":"male","keys":keys(t,sock)},
  {"phrase":"to spin on his fingertip","target":"the laundry bag","voice":"male","keys":keys(t,bag)}],
 "stillS":0.0,
 "nouns":[{"word":"a sock","x":0.59,"y":0.26,"voice":"male"},
  {"word":"washing machines","x":0.24,"y":0.50,"voice":"male"},
  {"word":"a tracksuit","x":0.48,"y":0.71,"voice":"male"},
  {"word":"a sneaker","x":0.15,"y":0.86,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","slumping","in","a","plastic","chair."],
 "answerVoice":"male",
 "notes":"Cartoon with many cuts. Key word 'boredom' is abstract, so it is not a noun slot and not in the answer. The man is boxed also where only a part of him is shown (4.5/5.0 only his shoes, 5.5/6.0 only his arm and hand under the spinning bag). 2.0 is a clock close-up: all targets off. 7.5 only the sock in the drum. At 9.5/10.0 the sock lies on his head: boxes split at y 0.53, so the man's box loses his head there. At 8.0-9.0 the man's box is cut on the left (x 0.46/0.50) to leave the sock and the hand holding it to the sock box. The bag at 5.5 is a motion-blurred disc; at 6.5 it is cut by the top edge. The feather (3.0/3.5) is not used. 'to dangle' is true at 8.5-9.0, 'to spin on his fingertip' at 5.5-6.0."})

# ---------- 7088
t=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:(0.04,0.16,0.42,0.42),0.7:(0.03,0.15,0.44,0.42),1.2:(0,0.13,0.50,0.48),1.7:(0,0.11,0.40,0.52),
 2.2:(0,0.17,0.43,0.47),2.7:(0.02,0.22,0.43,0.43),3.2:(0.03,0.23,0.45,0.40),3.7:(0.03,0.23,0.46,0.40)}
kn={0.2:(0.57,0.33,0.18,0.14),0.7:(0.57,0.33,0.18,0.14),1.2:(0.59,0.33,0.19,0.14),1.7:(0.59,0.34,0.21,0.14),
 2.2:(0.58,0.34,0.20,0.14),2.7:(0.57,0.34,0.18,0.14),3.2:(0.57,0.34,0.18,0.14),3.7:(0.57,0.34,0.18,0.14)}
cr={x:(0.54,0.0,0.28,0.27) for x in t}
write({"mediaId":7088,"level":"B","keyWord":"even out","defaultVoice":"female",
 "taps":[
  {"phrase":"to drag a long straightedge","target":"the woman","voice":"female","keys":keys(t,wom)},
  {"phrase":"to hoist a heavy load","target":"the crane","voice":"female","keys":keys(t,cr)},
  {"phrase":"to kneel on the rooftop","target":"the kneeling worker","voice":"female","keys":keys(t,kn)}],
 "stillS":2.2,
 "nouns":[{"word":"a crane","x":0.66,"y":0.05,"voice":"female"},
  {"word":"a hard hat","x":0.23,"y":0.24,"voice":"female"},
  {"word":"a tripod","x":0.85,"y":0.39,"voice":"female"},
  {"word":"concrete","x":0.25,"y":0.80,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","evening","out","the","wet","concrete."],
 "answerVoice":"female",
 "notes":"Key word 'even out' is in the answer. The woman's phrase is 'to drag a long straightedge' rather than 'to even out ...' because the kneeling worker in the background also smooths concrete. The woman's box holds her body and hands, not the whole straightedge. The standing worker (x about 0.42-0.52) is not a target; the woman's box touches him at 1.2. The kneeling worker's gender is not clear, so the default voice is used. The crane box holds the jib at the top edge and the hanging load. 'a hard hat' pill is on the woman's helmet (the workers behind wear small ones too)."})

# ---------- 4852
t=T(19)
man={0.0:(0,0,1.0,0.59),0.5:(0,0,1.0,0.61),1.0:(0,0,0.88,0.70),1.5:(0,0,0.82,0.66),
 2.0:(0,0,1.0,0.41),2.5:(0,0,1.0,0.41),3.0:(0,0,1.0,0.42),3.5:(0,0,1.0,0.42),4.0:(0,0,1.0,0.38),
 4.5:(0.18,0.08,0.70,0.30),5.0:(0.12,0.08,0.80,0.66),5.5:(0.08,0.10,0.84,0.58),6.0:(0.10,0.11,0.76,0.50),
 6.5:(0.25,0.17,0.56,0.42),7.0:(0.25,0.12,0.50,0.50),7.5:(0.31,0.25,0.38,0.27),
 8.0:(0.31,0.24,0.38,0.22),8.5:(0.29,0.24,0.40,0.23),9.0:(0.34,0.28,0.36,0.21)}
board={0.0:(0.33,0.59,0.67,0.41),0.5:(0.36,0.61,0.64,0.39),1.0:(0.49,0.70,0.48,0.25),1.5:(0.47,0.66,0.33,0.14),
 2.0:(0.38,0.41,0.30,0.21),2.5:(0.38,0.41,0.30,0.21),3.0:(0.38,0.42,0.30,0.20),3.5:(0.40,0.42,0.30,0.20),
 4.0:(0.32,0.38,0.30,0.20),4.5:(0.56,0.38,0.18,0.14)}
mach={7.5:(0,0.52,1.0,0.18),8.0:(0,0.46,1.0,0.32),8.5:(0.02,0.47,0.96,0.30),9.0:(0.03,0.49,0.94,0.25)}
write({"mediaId":4852,"level":"B","keyWord":"gear","defaultVoice":"male",
 "taps":[
  {"phrase":"to raise both arms","target":"the man","voice":"male","keys":keys(t,man)},
  {"phrase":"to flash red and green","target":"the circuit board","voice":"male","keys":keys(t,board)},
  {"phrase":"to have large metal gears","target":"the huge machine","voice":"male","keys":keys(t,mach)}],
 "stillS":2.5,
 "nouns":[{"word":"goggles","x":0.50,"y":0.15,"voice":"male"},
  {"word":"tools","x":0.85,"y":0.29,"voice":"male"},
  {"word":"a circuit board","x":0.55,"y":0.50,"voice":"male"},
  {"word":"a vice","x":0.50,"y":0.73,"voice":"male"}],
 "question":"What is the man building?",
 "answer":["He","is","building","a","machine","with","metal","gears."],
 "answerVoice":"male",
 "notes":"Five shots. Key word 'gear' is only visible in the last shot (7.5-9.0), where everything is small, so the noun still is 2.5 (goggles, tools on the pegboard, circuit board, vice) and the key word is in the third phrase and the answer instead. Phrase 3 is a state: no movement of the machine can be read from the frames. The man raises his arms only from 8.0. The board lights up red/green at 3.0-3.5. Where he holds the board in front of his chest (2.0-4.0) the boxes are split horizontally: the man's box is his head and shoulders, his hands beside the board fall outside both boxes. 0.0/0.5 show only his torso and hands (box = upper part of the picture). In the last shot the man stands inside the machine: his box is the middle, the machine's box is the band below him with the big gears (its upper side parts are in no box). The small machine on the trolley (5.0-7.0) is not 'the huge machine': off. Tools hang on both sides of the pegboard; the pill is on the right group. 'a vice' is the British spelling."})

# ---------- 4441
wom={0.0:(0.15,0.35,0.71,0.65),0.5:(0.12,0.33,0.81,0.67),1.0:(0.12,0.31,0.80,0.69),1.5:(0.03,0.27,0.95,0.73),
 2.0:(0.08,0.21,0.92,0.79),2.5:(0.05,0.18,0.95,0.82),3.0:(0.08,0.21,0.88,0.79),3.5:(0.06,0.28,0.90,0.72),
 4.0:(0.33,0.37,0.60,0.63),4.5:(0.32,0.43,0.63,0.57),5.0:(0.33,0.44,0.62,0.56),5.5:(0.34,0.42,0.62,0.58),
 6.0:(0.36,0.46,0.60,0.54),6.5:(0.10,0.40,0.82,0.60),7.0:(0.36,0.40,0.56,0.60),7.5:(0.37,0.41,0.55,0.59),
 8.0:(0.36,0.41,0.50,0.59),8.5:(0.17,0.45,0.70,0.55),9.0:(0.18,0.47,0.66,0.53)}
peak={0.0:(0.52,0.20,0.28,0.15),0.5:(0.52,0.19,0.30,0.14),1.0:(0.55,0.17,0.28,0.14),1.5:(0.57,0.13,0.26,0.14),
 4.0:(0.44,0.23,0.24,0.14),4.5:(0.42,0.29,0.27,0.14),5.0:(0.40,0.30,0.28,0.14),5.5:(0.40,0.28,0.28,0.14),
 6.0:(0.41,0.29,0.29,0.17),6.5:(0.42,0.26,0.28,0.14),7.0:(0.42,0.25,0.28,0.15),7.5:(0.43,0.25,0.28,0.15),
 8.0:(0.42,0.26,0.28,0.14),8.5:(0.42,0.27,0.28,0.15)}
per={4.0:(0.13,0.47,0.19,0.17),4.5:(0.13,0.49,0.19,0.22),5.0:(0.11,0.50,0.21,0.21),5.5:(0.11,0.49,0.22,0.21),
 6.0:(0.14,0.48,0.21,0.24),7.0:(0.16,0.44,0.20,0.20),7.5:(0.17,0.44,0.20,0.21),8.0:(0.15,0.45,0.21,0.17)}
write({"mediaId":4441,"level":"B","keyWord":"breath","defaultVoice":"female",
 "taps":[
  {"phrase":"to keep her eyes shut","target":"the woman","voice":"female","keys":keys(t,wom)},
  {"phrase":"to tower over the landscape","target":"the mountain peak","voice":"female","keys":keys(t,peak)},
  {"phrase":"to wear a white beanie","target":"the person in the white hat","voice":"female","keys":keys(t,per)}],
 "stillS":0.0,
 "nouns":[{"word":"the sky","x":0.30,"y":0.12,"voice":"female"},
  {"word":"a peak","x":0.66,"y":0.28,"voice":"female"},
  {"word":"breath","x":0.22,"y":0.49,"voice":"female"},
  {"word":"a jacket","x":0.52,"y":0.72,"voice":"female"}],
 "question":"What can you see in the air?",
 "answer":["You","can","see","the","woman's","breath."],
 "answerVoice":"female",
 "notes":"The woman's phrase is not 'to breathe out a white cloud' because the people behind her breathe out clouds too at 8.0-8.5; her eyes are shut in almost every frame (the others' are open or not readable). Phrases 1 and 3 are states. The person in the white hat (gender unclear, default voice) stands behind her left shoulder: boxed 4.0-8.0, off at 0.0-3.5 (only a sliver of the head peeks out beside her at 0.0-1.5, inside her box) and at 6.5/8.5/9.0 (behind the breath cloud). From 4.0 the woman's box starts right of that person, so it loses her left shoulder and arm. The peak (Matterhorn) is off at 2.0-3.5 (mostly behind her head) and at 9.0 (fog); elsewhere its box sits above her box and where her hat reaches the peak the box holds mainly the upper part. 'breath' = the white cloud at the left of the still. Answer subject is 'You': answerVoice = default."})
