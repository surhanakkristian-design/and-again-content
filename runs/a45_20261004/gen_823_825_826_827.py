import json
def K(times, rows):
    out=[]
    for t,r in zip(times,rows):
        if r is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 823
t=T(11)
screen=[(0.08,0.31,0.92,0.38),(0.08,0.31,0.92,0.38),(0.05,0.30,0.95,0.40),(0.03,0.30,0.97,0.40),(0.0,0.28,1.0,0.42),
 (0.0,0.27,0.78,0.42),(0.0,0.27,0.68,0.46),(0.0,0.25,0.58,0.48),(0.0,0.23,0.56,0.48),(0.0,0.21,0.58,0.49),(0.0,0.19,0.58,0.52)]
hand=[None]*5+[(0.78,0.42,0.22,0.20),(0.68,0.38,0.32,0.22),(0.58,0.36,0.42,0.22),(0.56,0.33,0.44,0.22),(0.58,0.33,0.42,0.22),(0.58,0.32,0.42,0.22)]
person=[(0.0,0.71,1.0,0.29),(0.0,0.71,1.0,0.29),(0.0,0.80,1.0,0.20),(0.0,0.80,1.0,0.20),(0.0,0.76,0.22,0.20)]+[None]*6
save({"mediaId":823,"level":"A","keyWord":"screen","defaultVoice":"male",
 "taps":[
  {"phrase":"to point at the screen","target":"the hand on the right","voice":"male","keys":K(t,hand)},
  {"phrase":"to show colourful charts","target":"the screen","voice":"male","keys":K(t,screen)},
  {"phrase":"to use a keyboard","target":"the person at the desk","voice":"male","keys":K(t,person)}],
 "stillS":0.0,
 "nouns":[{"word":"a screen","x":0.45,"y":0.45,"voice":"male"},{"word":"a keyboard","x":0.35,"y":0.80,"voice":"male"},
          {"word":"a mouse","x":0.80,"y":0.85,"voice":"male"},{"word":"a plant","x":0.15,"y":0.24,"voice":"male"}],
 "question":"What is the hand pointing at?",
 "answer":["The","hand","is","pointing","at","the","screen."],"answerVoice":"male",
 "notes":"Pointing hand enters from the right at 2.5 s and lies over the screen: screen box is cut at the fingertip. 'the person at the desk' = foreground person seen from behind (shoulder, left hand on keyboard, right hand on mouse), visible only 0-2.0 s; the hand rests on the keyboard, real typing is not clear, so 'to use a keyboard'. Its box is the strip below the monitor (head at the left edge is left out to avoid the screen box). Several plants in the room: the pill is on the big one at the left."})

# 825
t=T(20)
dog=[(0.62,0.32,0.38,0.60),(0.63,0.35,0.37,0.60),(0.63,0.38,0.37,0.60),(0.63,0.42,0.37,0.58),(0.63,0.45,0.37,0.55),(0.63,0.48,0.37,0.52),
 (0.63,0.50,0.37,0.50),(0.63,0.53,0.37,0.47),(0.63,0.55,0.37,0.45),(0.63,0.57,0.37,0.43),(0.63,0.59,0.37,0.41),(0.63,0.61,0.37,0.39),
 (0.63,0.63,0.37,0.37),(0.64,0.65,0.36,0.35),(0.65,0.67,0.35,0.33),(0.66,0.68,0.34,0.32),(0.56,0.70,0.44,0.30),(0.50,0.72,0.50,0.28),
 (0.40,0.72,0.60,0.28),(0.36,0.70,0.64,0.30)]
hand=[(0.0,0.70,0.60,0.24),(0.0,0.71,0.61,0.25),(0.0,0.75,0.61,0.25),(0.0,0.79,0.61,0.21),(0.05,0.84,0.56,0.16),(0.10,0.86,0.52,0.14),
 (0.25,0.86,0.37,0.14),None,None,None,None,None,(0.20,0.86,0.42,0.14),(0.0,0.78,0.63,0.22),(0.0,0.67,0.63,0.33),
 (0.0,0.59,0.65,0.36),(0.0,0.53,0.66,0.17),(0.0,0.53,0.64,0.19),(0.0,0.53,0.62,0.19),(0.0,0.53,0.60,0.17)]
cl=[(0,0,1,0.20),(0,0,1,0.22),(0,0,1,0.25),(0,0,1,0.27),(0,0,1,0.30),(0,0,1,0.32),(0,0.02,1,0.34),(0,0.05,1,0.34),(0,0.05,1,0.38),
 (0,0.05,1,0.40),(0,0.05,1,0.44),(0,0.05,1,0.46),(0,0,1,0.52),(0,0,1,0.53),(0,0,1,0.56),(0,0,1,0.57),(0,0,1,0.52),(0,0,1,0.52),(0,0,1,0.52),(0,0,1,0.52)]
save({"mediaId":825,"level":"A","keyWord":"view","defaultVoice":"male",
 "taps":[
  {"phrase":"to lick a hand","target":"the dog","voice":"male","keys":K(t,dog)},
  {"phrase":"to hold a dog lead","target":"the hand","voice":"male","keys":K(t,hand)},
  {"phrase":"to float in the sky","target":"the clouds","voice":"male","keys":K(t,cl)}],
 "stillS":0.0,
 "nouns":[{"word":"mountains","x":0.40,"y":0.24,"voice":"male"},{"word":"a dog","x":0.82,"y":0.55,"voice":"male"},
          {"word":"a shoe","x":0.22,"y":0.73,"voice":"male"},{"word":"grass","x":0.25,"y":0.45,"voice":"male"}],
 "question":"What is the dog looking at?",
 "answer":["The","dog","is","looking","at","the","mountains."],"answerVoice":"male",
 "notes":"Key word 'view' is abstract, so it is not a noun slot. The dog licks the hand only at 9.0-9.5 s. Hand (with forearm) leaves the frame 3.5-5.5 s. At 8.0-9.5 s dog and hand touch: boxes split along a horizontal line, the hanging lead loop is left out. Clouds box covers the sky band (mountain tops inside it at the start). 'lead' is British; 'leash' would be the US word. 'to float in the sky' is 6 words with 'to' (5 without)."})

# 826
t=T(10)
desk=[(0.17,0.38,0.24,0.30),(0.17,0.39,0.24,0.30),(0.16,0.39,0.24,0.30),(0.17,0.39,0.24,0.30),(0.17,0.39,0.24,0.30),
 (0.19,0.39,0.24,0.30),(0.19,0.39,0.24,0.30),(0.19,0.39,0.24,0.30),(0.19,0.39,0.24,0.30),(0.17,0.39,0.24,0.30)]
cam=[(0.43,0.34,0.30,0.38),(0.43,0.35,0.31,0.38),(0.43,0.36,0.30,0.38),(0.43,0.35,0.31,0.38),(0.47,0.35,0.22,0.34),
 (0.50,0.36,0.18,0.16),None,(0.50,0.36,0.18,0.16),(0.53,0.36,0.18,0.16),(0.52,0.36,0.18,0.16)]
boom=[(0.82,0.33,0.18,0.33),(0.82,0.33,0.18,0.33),(0.82,0.34,0.18,0.32),(0.81,0.33,0.19,0.34),(0.78,0.32,0.22,0.35),
 (0.82,0.33,0.18,0.36),(0.80,0.33,0.20,0.37),(0.80,0.33,0.20,0.37),(0.80,0.32,0.20,0.38),(0.80,0.32,0.20,0.38)]
save({"mediaId":826,"level":"B","keyWord":"film","defaultVoice":"male",
 "taps":[
  {"phrase":"to film the scene","target":"the cameraman","voice":"male","keys":K(t,cam)},
  {"phrase":"to raise a boom microphone","target":"the man with the microphone","voice":"male","keys":K(t,boom)},
  {"phrase":"to act for the camera","target":"the man at the desk","voice":"male","keys":K(t,desk)}],
 "stillS":0.0,
 "nouns":[{"word":"a studio light","x":0.72,"y":0.16,"voice":"male"},{"word":"a camera","x":0.50,"y":0.45,"voice":"male"},
          {"word":"a desk","x":0.20,"y":0.56,"voice":"male"},{"word":"cables","x":0.50,"y":0.88,"voice":"male"}],
 "question":"What is the cameraman doing?",
 "answer":["He","is","filming","an","actor","at","a","desk."],"answerVoice":"male",
 "notes":"The cameraman sits on the dolly behind the camera; from 2.5 s the standing man in black (tablet, not a target) walks in front of him: small box on the camera/head where still visible, off at 3.0 s. The cameraman's and boom operator's boxes overlap the standing man, who is no target. 'to act for the camera' is an inference from the set (he is the one lit and filmed); background office workers sit at other desks. A second light stands at the left edge; the pill is on the big round one."})

# 827
t=T(20)
save({"mediaId":827,"level":"A","keyWord":"animal","defaultVoice":"male",
 "taps":[
  {"phrase":"to sit on a branch","target":"the owl","voice":"male","keys":K(t,[(0.05,0.03,0.22,0.18)]*20)},
  {"phrase":"to eat from a tree","target":"the giraffe","voice":"male","keys":K(t,[(0.58,0.12,0.38,0.38)]*20)},
  {"phrase":"to sit near a pig","target":"the dog","voice":"male","keys":K(t,[(0.03,0.53,0.24,0.24)]*20)}],
 "stillS":5.0,
 "nouns":[{"word":"a cow","x":0.33,"y":0.42,"voice":"male"},{"word":"a giraffe","x":0.78,"y":0.34,"voice":"male"},
          {"word":"a dog","x":0.18,"y":0.63,"voice":"male"},{"word":"an elephant","x":0.88,"y":0.72,"voice":"male"}],
 "question":"Which animal is sitting on a branch?",
 "answer":["The","owl","is","sitting","on","a","branch."],"answerVoice":"male",
 "notes":"Still illustration, only the colour changes; German labels are printed in the picture until about 4 s (still at 5.0 s has none). Giraffe box overlaps zebra and hippo, which are no targets. The goat also eats (from a bush), so the giraffe phrase says tree. Key word 'animal' is in the question, not a noun slot."})
