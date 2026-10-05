import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def write(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 125
W={2.5:(0,0,0.78,0.62),3.0:(0,0,0.78,0.82),3.5:(0,0,0.81,0.85),8.5:(0,0,0.66,0.85),9.0:(0,0,0.70,1.0),9.5:(0,0,0.71,1.0),10.0:(0,0.02,0.71,0.98)}
M={4.0:(0,0,0.58,0.76),4.5:(0,0,0.62,0.70),5.0:(0,0,0.62,0.76),5.5:(0,0,0.58,0.48)}
C={2.5:(0.80,0.08,0.20,0.16),3.0:(0.79,0.21,0.21,0.17),3.5:(0.82,0.22,0.18,0.18),4.0:(0.60,0.23,0.40,0.18),4.5:(0.64,0.22,0.36,0.18),5.0:(0.64,0.17,0.36,0.18),5.5:(0.60,0,0.40,0.20),
   8.5:(0.68,0.17,0.32,0.20),9.0:(0.72,0.30,0.28,0.20),9.5:(0.73,0.30,0.27,0.17),10.0:(0.73,0.31,0.27,0.21)}
write({"mediaId":125,"level":"A","keyWord":"butter","defaultVoice":"female",
 "taps":[
  {"phrase":"to eat bread with butter","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to touch the butter","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to sit by the window","target":"the cat","voice":"female","keys":keys(C)}],
 "stillS":5.0,
 "nouns":[{"word":"a man","x":0.24,"y":0.18,"voice":"male"},{"word":"a cat","x":0.84,"y":0.29,"voice":"female"},
          {"word":"butter","x":0.52,"y":0.69,"voice":"female"},{"word":"bread","x":0.42,"y":0.93,"voice":"female"}],
 "question":"What is the woman eating?",
 "answer":["She","is","eating","bread","with","butter."],"answerVoice":"female",
 "notes":"Hands-only shots (0-2.0, 6.0-8.0) are off for both people: the owner of the hands is not identifiable. 'to touch the butter': the man presses it with a finger at 4.0-5.5; the hands cutting/spreading butter use a knife. Cat lies/sits on the windowsill; at 4.0-5.5 it lies rather than sits."})

# ---------- 126
M={3.5:(0,0,0.45,1.0),4.0:(0,0,0.51,1.0),4.5:(0,0,0.50,1.0),5.0:(0,0,0.50,1.0),5.5:(0,0,0.50,1.0),6.0:(0,0,0.50,1.0),6.5:(0,0,0.50,1.0),
   7.0:(0,0,0.49,1.0),7.5:(0,0,0.49,1.0),8.0:(0,0.02,0.52,0.98),8.5:(0,0,0.60,1.0),9.0:(0,0,0.58,1.0),9.5:(0,0,0.80,1.0),10.0:(0,0,0.80,1.0)}
C={3.5:(0.46,0.17,0.20,0.16),4.0:(0.52,0.17,0.19,0.15),4.5:(0.51,0.17,0.19,0.15),5.0:(0.51,0.19,0.19,0.15),5.5:(0.51,0.20,0.19,0.15),
   6.0:(0.51,0.22,0.19,0.15),6.5:(0.51,0.25,0.19,0.15),7.0:(0.50,0.28,0.19,0.15),7.5:(0.50,0.31,0.19,0.15),8.0:(0.53,0.32,0.18,0.14),
   8.5:(0.61,0.24,0.18,0.14),9.0:(0.59,0.29,0.18,0.14)}
W={3.5:(0.67,0.03,0.33,0.97),4.0:(0.72,0.05,0.28,0.95),4.5:(0.71,0.03,0.29,0.97),5.0:(0.71,0.05,0.29,0.95),5.5:(0.71,0.05,0.29,0.95),
   6.0:(0.71,0.08,0.29,0.92),6.5:(0.71,0.10,0.29,0.90),7.0:(0.70,0.20,0.30,0.80),7.5:(0.70,0.20,0.30,0.80),8.0:(0.72,0.28,0.28,0.72),
   8.5:(0.80,0.15,0.20,0.85),9.0:(0.78,0.24,0.22,0.76),9.5:(0.81,0.28,0.19,0.72),10.0:(0.81,0.24,0.19,0.76)}
write({"mediaId":126,"level":"A","keyWord":"button","defaultVoice":"female",
 "taps":[
  {"phrase":"to wear a blue shirt","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to fix the man's shirt","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to lie on the shelf","target":"the cat","voice":"female","keys":keys(C)}],
 "stillS":2.5,
 "nouns":[{"word":"a button","x":0.52,"y":0.47,"voice":"female"},{"word":"a window","x":0.65,"y":0.14,"voice":"female"},
          {"word":"a finger","x":0.28,"y":0.36,"voice":"female"},{"word":"a jar","x":0.40,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","fixing","the","man's","shirt."],"answerVoice":"female",
 "notes":"Man phrase is a state: his only action (buttoning his shirt) is also done by the woman at 8.5-9.0. The cat on the shelf sits between the two people, so the boxes are split in columns: the woman's box is the right column with her face, her left arm falls outside. Cat counted as hidden at 9.5-10.0. 0-3.0 shows only hands: all off. 'a jar' may be slightly above A level; 'a finger' slot is on the index finger (the thumb below is the other finger)."})

# ---------- 127
K={0.0:(0.35,0,0.36,1.0),0.5:(0.13,0,0.78,1.0),1.0:(0.18,0.09,0.72,0.91)}
W={};M={}
for t,(k,w,m) in {6.0:((0.17,0,0.63,0.45),(0,0.46,0.58,0.54),(0.59,0.46,0.29,0.54)),
 6.5:((0.17,0,0.63,0.44),(0,0.45,0.58,0.55),(0.59,0.46,0.29,0.54)),
 7.0:((0.17,0,0.63,0.44),(0,0.45,0.54,0.55),(0.55,0.47,0.33,0.53)),
 7.5:((0.17,0,0.63,0.44),(0,0.45,0.49,0.55),(0.50,0.47,0.40,0.53)),
 8.0:((0.17,0,0.63,0.44),(0,0.45,0.47,0.55),(0.49,0.47,0.40,0.53)),
 8.5:((0.17,0,0.63,0.46),(0,0.47,0.44,0.53),(0.45,0.51,0.45,0.49)),
 9.0:((0.17,0,0.63,0.46),(0,0.47,0.45,0.53),(0.47,0.50,0.42,0.50)),
 9.5:((0.17,0,0.63,0.44),(0,0.45,0.49,0.55),(0.50,0.49,0.40,0.51)),
 10.0:((0.17,0,0.63,0.43),(0,0.44,0.49,0.56),(0.50,0.44,0.40,0.56))}.items():
    K[t]=k;W[t]=w;M[t]=m
write({"mediaId":127,"level":"B","keyWord":"cactus","defaultVoice":"female",
 "taps":[
  {"phrase":"to point at the spines","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to wear a khaki shirt","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to tower over the couple","target":"the tall cactus","voice":"female","keys":keys(K)}],
 "stillS":7.5,
 "nouns":[{"word":"a cactus","x":0.48,"y":0.27,"voice":"female"},{"word":"spines","x":0.82,"y":0.62,"voice":"female"},
          {"word":"a sun hat","x":0.28,"y":0.53,"voice":"female"},{"word":"the sky","x":0.20,"y":0.10,"voice":"female"}],
 "question":"What is the woman pointing at?",
 "answer":["She","is","pointing","at","the","spiny","cactus."],"answerVoice":"female",
 "notes":"Man phrase is a state: his gestures (raised palms 8.5-10) are shared with the woman at 9.5-10. 'the tall cactus' = the branched saguaro in the middle; boxed only above the couple's heads in 6.0-10, and in 0-1.0 where the same-looking saguaro fills the frame (couple not in that shot - doubt). The spiny cactus at the right edge is also a cactus: 'a cactus' pill sits on the saguaro, 'spines' on the right one. The man also wears a hat ('a sun hat' slot is on the woman's). Small birds at 4.0-5.5 not used."})

# ---------- 128
W={0.0:(0.02,0.36,0.26,0.28),0.5:(0.08,0.33,0.21,0.32),1.0:(0.27,0.29,0.25,0.17),1.5:(0.27,0.25,0.33,0.24),
   2.0:(0.17,0.08,0.66,0.41),2.5:(0.17,0.08,0.66,0.41),3.0:(0.15,0.08,0.68,0.42),3.5:(0.13,0.05,0.74,0.55),4.0:(0.05,0.04,0.83,0.48),
   4.5:(0,0,0.68,0.30),5.0:(0,0,0.72,0.27),5.5:(0.05,0,0.75,0.23),6.0:(0.12,0,0.88,0.17),6.5:(0.25,0,0.75,0.16),7.0:(0.10,0,0.90,0.26),
   7.5:(0.05,0,0.95,0.27),8.0:(0.02,0,0.98,0.42),8.5:(0.45,0.05,0.32,0.48),9.0:(0.34,0.19,0.34,0.37),9.5:(0.38,0.20,0.35,0.33),10.0:(0.40,0.23,0.32,0.29)}
K={0.0:(0.29,0.42,0.56,0.36),0.5:(0.30,0.41,0.55,0.37),1.0:(0.20,0.47,0.58,0.38),1.5:(0.18,0.50,0.55,0.38),
   2.0:(0.05,0.50,0.90,0.50),2.5:(0.05,0.50,0.90,0.50),3.0:(0.05,0.51,0.90,0.49),3.5:(0.05,0.61,0.90,0.39),4.0:(0.03,0.53,0.92,0.47),
   4.5:(0,0.31,0.92,0.55),5.0:(0,0.28,0.95,0.68),5.5:(0,0.24,1.0,0.76),6.0:(0,0.18,0.92,0.78),6.5:(0,0.17,1.0,0.80),7.0:(0,0.27,1.0,0.73),
   7.5:(0,0.28,1.0,0.72),8.0:(0,0.43,0.93,0.57),8.5:(0,0.54,0.84,0.39),9.0:(0.08,0.57,0.66,0.27),9.5:(0.15,0.54,0.60,0.27),10.0:(0.18,0.53,0.56,0.22)}
D={9.0:(0.55,0.86,0.30,0.14),9.5:(0.53,0.82,0.40,0.18),10.0:(0.50,0.76,0.42,0.24)}
write({"mediaId":128,"level":"A","keyWord":"cake","defaultVoice":"female",
 "taps":[
  {"phrase":"to blow out the candles","target":"the woman with the crown","voice":"female","keys":keys(W)},
  {"phrase":"to look up at the table","target":"the dog","voice":"female","keys":keys(D)},
  {"phrase":"to have berries on top","target":"the cake","voice":"female","keys":keys(K)}],
 "stillS":10.0,
 "nouns":[{"word":"a cake","x":0.40,"y":0.63,"voice":"female"},{"word":"a dog","x":0.70,"y":0.90,"voice":"female"},
          {"word":"a balloon","x":0.14,"y":0.06,"voice":"female"},{"word":"a crown","x":0.60,"y":0.27,"voice":"female"}],
 "question":"What is the dog looking at?",
 "answer":["The","dog","is","looking","at","the","cake."],"answerVoice":"female",
 "notes":"Cake phrase is a state (a thing). Dog only in 9.0-10.0; at 9.0 just the top of its head. Woman with the crown in the dark opening shots (0-1.5) is small and hard to tell from the second woman - check boxes there. Question is about the dog because two women are shown and a clear subject name would exceed 7 words; the dog looks up at the table where the cake stands."})
