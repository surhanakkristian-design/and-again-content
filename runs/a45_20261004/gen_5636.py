import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
# ---------- 5636
man = [(0.08,0.19,0.33,0.38),(0.06,0.17,0.35,0.42),(0.03,0.16,0.37,0.40),(0.02,0.14,0.38,0.42),(0,0.11,0.40,0.42),(0,0.09,0.39,0.46),(0,0.09,0.37,0.48),(0,0.09,0.37,0.50)]
cust = [(0.41,0.30,0.36,0.46),(0.41,0.29,0.37,0.47),(0.41,0.28,0.36,0.48),(0.41,0.26,0.38,0.50),(0.41,0.24,0.37,0.50),(0.40,0.22,0.39,0.52),(0.39,0.22,0.41,0.56),(0.39,0.22,0.41,0.58)]
serv = [(0.78,0.25,0.22,0.34),(0.79,0.24,0.21,0.35),(0.77,0.23,0.23,0.35),(0.80,0.20,0.20,0.38),(0.79,0.17,0.21,0.38),(0.80,0.15,0.20,0.40),(0.81,0.16,0.19,0.50),(0.81,0.18,0.19,0.44)]
write({"mediaId":5636,"level":"B","keyWord":"be up to you","defaultVoice":"female","taps":[
 {"phrase":"to lean over the counter","target":"the woman in the jumper","voice":"female","keys":K(T8,cust)},
 {"phrase":"to burst out laughing","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to hold a wafer cone","target":"the woman in the apron","voice":"female","keys":K(T8,serv)}],
 "stillS":0.2,
 "nouns":[{"word":"a chandelier","x":0.42,"y":0.08,"voice":"female"},{"word":"a cabinet","x":0.60,"y":0.24,"voice":"female"},{"word":"an apron","x":0.86,"y":0.47,"voice":"female"},{"word":"ice cream","x":0.38,"y":0.76,"voice":"female"}],
 "question":"What is the woman in cream doing?",
 "answer":["She","is","leaning","over","the","ice","cream","counter."],
 "answerVoice":"female",
 "notes":"The customer's skirt and legs run behind/below the server on the right, so her box holds head, torso and the pointing arm only (legs outside). The server's cone is not visible in the last frame (3.7 s), she bends down. The man laughs clearly from about 1.2 s. Key phrase 'be up to you' is not visible, so it is not used. 'in cream' = the cream jumper; the server wears white."})
# ---------- 8028
wom = [(0,0.36,0.30,0.60),(0,0.36,0.30,0.60),(0,0.36,0.29,0.60),(0,0.36,0.29,0.60),(0,0.36,0.29,0.60),(0,0.36,0.29,0.60),(0,0.36,0.30,0.60),(0,0.36,0.30,0.60)]
stk = [(0.30,0.40,0.33,0.30),(0.30,0.40,0.35,0.31),(0.29,0.37,0.38,0.34),(0.29,0.36,0.39,0.36),(0.29,0.35,0.40,0.38),(0.29,0.34,0.42,0.39),(0.30,0.34,0.42,0.40),(0.31,0.34,0.44,0.40)]
chef = [(0.64,0.17,0.36,0.38),(0.66,0.15,0.34,0.40),(0.67,0.14,0.33,0.40),(0.68,0.13,0.32,0.42),(0.69,0.12,0.31,0.43),(0.71,0.11,0.29,0.44),(0.73,0.10,0.27,0.46),(0.76,0.09,0.24,0.48)]
write({"mediaId":8028,"level":"B","keyWord":"total","defaultVoice":"female","taps":[
 {"phrase":"to point at the stack","target":"the chef","voice":"male","keys":K(T8,chef)},
 {"phrase":"to bury her face","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to tower over the counter","target":"the stacks of plates","voice":"female","keys":K(T8,stk)}],
 "stillS":2.2,
 "nouns":[{"word":"a lantern","x":0.42,"y":0.08,"voice":"female"},{"word":"a headband","x":0.80,"y":0.20,"voice":"female"},{"word":"plates","x":0.58,"y":0.55,"voice":"female"},{"word":"chopsticks","x":0.76,"y":0.76,"voice":"female"}],
 "question":"What is the chef doing?",
 "answer":["He","is","pointing","at","the","stack","of","plates."],
 "answerVoice":"male",
 "notes":"The chef's pointing fingertip touches the top of the taller stack, so it falls into the stacks' box; the woman's raised hand touches the left stack, split at x about 0.29. The woman hides her face only in the last two frames (3.2, 3.7 s). Both stacks are one target. The chef stops pointing at 3.2 s. Key word 'total' (verb) cannot be seen without the sound, so 'point at the stack' is used; defaultVoice female by evenId (a man and a woman)."})
# ---------- 7739
cap = [(0.26,0.35,0.28,0.27),(0.30,0.35,0.30,0.27),(0.32,0.36,0.29,0.27),(0.30,0.36,0.27,0.28),(0.30,0.35,0.28,0.28),(0.30,0.35,0.30,0.28),(0.30,0.36,0.30,0.28),(0.32,0.35,0.30,0.29)]
grn = [(0.63,0.24,0.27,0.19),(0.64,0.24,0.26,0.19),(0.66,0.24,0.26,0.19),(0.66,0.24,0.26,0.19),(0.66,0.24,0.27,0.19),(0.67,0.24,0.26,0.19),(0.67,0.24,0.26,0.19),(0.67,0.24,0.26,0.19)]
lad = [(0.05,0.64,0.27,0.23),(0.05,0.63,0.28,0.20),(0.03,0.57,0.27,0.26),(0.02,0.55,0.26,0.26),(0,0.50,0.24,0.25),(0,0.48,0.24,0.25),(0,0.45,0.22,0.30),(0,0.44,0.24,0.30)]
write({"mediaId":7739,"level":"B","keyWord":"aging","defaultVoice":"male","taps":[
 {"phrase":"to roll a cheese wheel","target":"the mouse in the cap","voice":"male","keys":K(T8,cap)},
 {"phrase":"to tap with a hammer","target":"the mouse in green","voice":"male","keys":K(T8,grn)},
 {"phrase":"to climb up the ladder","target":"the mouse on the ladder","voice":"male","keys":K(T8,lad)}],
 "stillS":2.2,
 "nouns":[{"word":"a lantern","x":0.35,"y":0.18,"voice":"male"},{"word":"a window","x":0.16,"y":0.36,"voice":"male"},{"word":"a ladder","x":0.14,"y":0.79,"voice":"male"},{"word":"a bucket","x":0.78,"y":0.90,"voice":"male"}],
 "question":"What is the mouse rolling?",
 "answer":["It","is","rolling","a","heavy","cheese","wheel."],
 "answerVoice":"male",
 "notes":"The mouse in green holds a small hammer against the cheese on the upper shelf; the tapping movement is slight. The third mouse climbs the ladder until about 2.7 s and stands on the shelf with a brush at 3.2-3.7 s (still named 'the mouse on the ladder'). Tails are partly outside the boxes. Key word 'aging' is abstract and not placed as a noun."})
# ---------- 637
T = [i*0.5 for i in range(31)]
#        ft    fb    fl
F = [(.27,.70,.22),(.27,.70,.25),(.30,.72,.30),(.30,.72,.25),(.26,.70,.20),(.27,.70,.18),(.28,.72,.18),(.25,.72,.20),
     (.15,.70,.12),(.24,.67,0),(.24,.78,.15),(.25,.72,.12),(.21,.66,.15),(.21,.72,.18),(.22,.70,.18),(.21,.72,.15),
     (.20,.70,.12),(.21,.72,.10),(.22,.74,.10),(.22,.74,.10),(.20,.72,.08),(.20,.72,.08),(.22,.72,.05),(.15,.72,0),
     (.13,.72,0),(.13,.72,0),(.14,.82,0),(.14,.85,0),(.15,.76,0),(.16,.76,0),(.17,.85,0)]
HOR = [.28,.28,.28,.28,.26,.27,.28,.25,.24,.24,.24,.24,.21,.21,.20,.20,.20,.20,.20,.20,.19,.19,.20,.18,.17,.17,.17,.17,.16,.16,.18]
fruit = [(fl, ft, 1-fl, fb-ft) for ft,fb,fl in F]
pile = [(0, fb, 1, 1-fb) for ft,fb,fl in F]
sky = [(0, 0, 1, min(ft, h)) for (ft,fb,fl),h in zip(F,HOR)]
write({"mediaId":637,"level":"B","keyWord":"pomegranate","defaultVoice":"male","taps":[
 {"phrase":"to open like a flower","target":"the pomegranate in the hands","voice":"male","keys":K(T,fruit)},
 {"phrase":"to lie in a heap","target":"the pomegranates below","voice":"male","keys":K(T,pile)},
 {"phrase":"to stretch over green hills","target":"the sky","voice":"male","keys":K(T,sky)}],
 "stillS":4.0,
 "nouns":[{"word":"the sky","x":0.35,"y":0.06,"voice":"male"},{"word":"a knife","x":0.25,"y":0.25,"voice":"male"},{"word":"a thumb","x":0.80,"y":0.45,"voice":"male"},{"word":"a pomegranate","x":0.48,"y":0.58,"voice":"male"}],
 "question":"What is happening to the pomegranate?",
 "answer":["It","is","opening","like","a","flower."],
 "answerVoice":"male",
 "notes":"Only hands and arms of the person are visible and they overlap the fruit all the time, so hands are no target; the held pomegranate's box includes the hands. The knife is visible too briefly and always on the fruit, so it is not a tap target (only a noun at 4.0 s). Third target is the sky (a state, no action available); the arm crosses the sky box. 'a pomegranate' pill sits on the held fruit although more pomegranates lie below; no other noun is on those. Check 'a thumb' on the right hand at 4.0 s. Pile box = everything below the lower hand; parts of the pile left of the held fruit are in no box."})
