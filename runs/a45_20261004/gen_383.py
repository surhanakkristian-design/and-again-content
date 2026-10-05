import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
def T(n,step=0.5,start=0.0): return [round(start+i*step,2) for i in range(n)]
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 383
t=T(21)
W=[(0,0,0.5,0.65),(0.03,0,0.50,0.72),(0,0.24,0.62,0.76),(0,0.46,0.67,0.54),(0,0.43,0.62,0.57),
   (0,0.05,0.46,0.42),(0.05,0,0.67,0.72),(0,0.10,0.72,0.90),(0,0.12,0.72,0.88),(0,0.16,0.74,0.33),
   (0.57,0.06,0.35,0.64),(0.60,0.06,0.33,0.60),(0.57,0.37,0.23,0.34),(0.53,0.57,0.20,0.22),
   (0.23,0.29,0.28,0.48),(0.15,0.27,0.35,0.50),(0.17,0.27,0.35,0.39),(0.17,0.27,0.35,0.39),
   (0.09,0.45,0.43,0.29),(0.09,0.45,0.44,0.29),(0.09,0.45,0.45,0.29)]
M=[(0.5,0,0.5,0.45),(0.55,0,0.45,0.52),(0.62,0.36,0.38,0.64),(0.67,0.56,0.33,0.44),(0.62,0.56,0.38,0.44),
   (0.46,0.47,0.54,0.53),(0.72,0,0.28,0.36),(0.72,0.30,0.28,0.70),(0.72,0.33,0.28,0.67),OFF,
   (0.0,0.22,0.57,0.72),(0.12,0.25,0.48,0.67),(0.27,0.50,0.30,0.39),(0.33,0.66,0.20,0.24),
   (0.51,0.33,0.30,0.44),(0.50,0.28,0.36,0.49),(0.52,0.27,0.34,0.39),(0.52,0.27,0.34,0.39),
   (0.52,0.45,0.28,0.30),(0.53,0.45,0.27,0.30),(0.54,0.45,0.26,0.30)]
B=[OFF]*18+[(0.72,0.02,0.28,0.34),(0.55,0.02,0.36,0.35),(0.34,0.02,0.37,0.34)]
save({"mediaId":383,"level":"A","keyWord":"hiking","defaultVoice":"male",
 "taps":[
  {"phrase":"to carry a blue backpack","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to drink from a bottle","target":"the man","voice":"male","keys":keys(t,M)},
  {"phrase":"to fly over the mountains","target":"the birds","voice":"male","keys":keys(t,B)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.08,"voice":"male"},{"word":"mountains","x":0.45,"y":0.25,"voice":"male"},
          {"word":"a woman","x":0.40,"y":0.45,"voice":"female"},{"word":"grass","x":0.80,"y":0.79,"voice":"male"}],
 "question":"What are the two people doing?",
 "answer":["They","are","hiking","in","the","mountains."],"answerVoice":"male",
 "notes":"Man drinks only at t=10.0 (bottle in his hand from 7.5). Birds only 9.0-10.0. 2.5 s is a fist-bump close-up (sleeves only), 3.0 s legs only, 4.5 s only the woman's arm. Lying frames 9.0-10.0: the man's legs fall in the woman's box (bodies overlap diagonally). defaultVoice male: mixed pair, evenId false."})

# ---------- 13
t=T(19)
W=[(0.25,0.07,0.53,0.73),(0.08,0.07,0.84,0.73),(0,0,1,0.57),(0,0,1,0.53),(0,0,1,0.50),(0,0,1,0.60),
   (0.10,0,0.90,0.50),(0.10,0,0.90,0.56),(0.05,0,0.93,0.47),(0.22,0,0.60,0.60),(0.07,0.07,0.69,0.78),
   (0.03,0,0.97,1.0),(0,0,1,1),(0,0,1,1),(0.40,0,0.60,0.62),(0.08,0,0.92,1),(0,0,1,1),
   (0.17,0.15,0.63,0.85),(0.25,0.18,0.52,0.82)]
k=keys(t,W)
save({"mediaId":13,"level":"A","keyWord":"napkin","defaultVoice":"female",
 "taps":[
  {"phrase":"to fold a napkin","target":"the woman","voice":"female","keys":k},
  {"phrase":"to wipe her mouth","target":"the woman","voice":"female","keys":k},
  {"phrase":"to sit on a chair","target":"the woman","voice":"female","keys":k}],
 "stillS":8.5,
 "nouns":[{"word":"a woman","x":0.50,"y":0.34,"voice":"female"},{"word":"a napkin","x":0.47,"y":0.80,"voice":"female"},
          {"word":"a chair","x":0.82,"y":0.66,"voice":"female"},{"word":"a table","x":0.14,"y":0.92,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","folding","a","napkin."],"answerVoice":"female",
 "notes":"Only one possible target (the woman), used for all three phrases. 7.0 s shows only her arm. 'wipe' is A2/B1 but the natural verb."})

# ---------- 6949
t=[0.2,0.7,1.2,1.7,2.2,2.7]
W=[(0,0,0.64,0.48),(0,0,0.64,0.50),(0.09,0.13,0.65,0.76),(0.09,0.22,0.59,0.70),(0.09,0.25,0.57,0.62),(0.12,0.21,0.54,0.66)]
M=[OFF,OFF,(0.74,0.42,0.26,0.58),(0.68,0.50,0.32,0.50),(0.66,0.44,0.34,0.56),(0.66,0.56,0.34,0.44)]
kw=keys(t,W)
save({"mediaId":6949,"level":"A","keyWord":"chocolate","defaultVoice":"female",
 "taps":[
  {"phrase":"to pour hot chocolate","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to wear a gold dress","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to drink from a cup","target":"the man in the hat","voice":"male","keys":keys(t,M)}],
 "stillS":0.7,
 "nouns":[{"word":"chocolate","x":0.55,"y":0.33,"voice":"female"},{"word":"a cup","x":0.55,"y":0.60,"voice":"female"},
          {"word":"a hand","x":0.32,"y":0.73,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","pouring","hot","chocolate","into","a","cup."],"answerVoice":"female",
 "notes":"0.2/0.7 s: close-up, woman = ladle + lower body. Man in the hat = foreground right figure with a cup at his mouth (1.2-2.7). 'chocolate' slot is on the pouring stream, 'a cup' on the glass (which also holds chocolate). Second woman phrase is a state (gold dress)."})

# ---------- 330
t=T(19)
G=[(0,0,0.36,0.65),(0,0.05,0.58,0.83),(0,0.12,0.58,0.78),(0,0.18,0.60,0.72),(0,0.23,0.58,0.54),
   (0,0.24,0.57,0.76),(0,0.20,0.66,0.80),(0,0.18,0.64,0.82),(0,0.18,0.64,0.82),(0,0.17,0.62,0.83),
   (0.28,0.20,0.72,0.80),(0.07,0.27,0.76,0.73),(0.19,0.27,0.56,0.73),(0.25,0.35,0.44,0.60),
   (0.29,0.38,0.21,0.54),(0.25,0.34,0.19,0.54),(0.24,0.33,0.20,0.46),OFF,OFF]
M=[OFF,(0.62,0.42,0.18,0.14),(0.61,0.40,0.18,0.14),(0.62,0.37,0.20,0.17),(0.59,0.35,0.22,0.24),
   (0.59,0.15,0.41,0.58),(0.66,0.17,0.34,0.66),(0.64,0.17,0.36,0.65),(0.64,0.16,0.36,0.56),(0.62,0.16,0.38,0.56),
   (0,0.10,0.28,0.58),OFF,OFF,OFF,
   (0.50,0.34,0.20,0.48),(0.44,0.30,0.27,0.56),(0.44,0.29,0.30,0.48),OFF,OFF]
kg=keys(t,G)
save({"mediaId":330,"level":"A","keyWord":"gate","defaultVoice":"female",
 "taps":[
  {"phrase":"to run to the gate","target":"the girl","voice":"female","keys":kg},
  {"phrase":"to show her ticket","target":"the girl","voice":"female","keys":kg},
  {"phrase":"to hold the door open","target":"the man","voice":"male","keys":keys(t,M)}],
 "stillS":2.0,
 "nouns":[{"word":"a window","x":0.45,"y":0.12,"voice":"female"},{"word":"a gate","x":0.66,"y":0.30,"voice":"female"},
          {"word":"a girl","x":0.38,"y":0.40,"voice":"female"},{"word":"a suitcase","x":0.14,"y":0.62,"voice":"female"}],
 "question":"Where is the girl running?",
 "answer":["She","is","running","to","the","gate."],"answerVoice":"female",
 "notes":"The white card she holds up is a boarding pass, called 'ticket' for level A. Man is tiny in 0.5-2.0 (min-size box; a second small dark figure stands beside him at 0.5-1.0). Man hidden behind the girl 5.5-6.5 -> off. Door closed 8.5-9.0 -> both off. 'a gate' slot sits on the door frame with the green sign; the man stands inside it."})
