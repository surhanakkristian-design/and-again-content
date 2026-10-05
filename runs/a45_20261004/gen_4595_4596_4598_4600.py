import json
def T(n): return [round(i*0.5,1) for i in range(n)]
def keys(times, spec):
    # spec: list of (t_from, t_to, box or None)
    out=[]
    for t in times:
        b='x'
        for a,z,bx in spec:
            if a-1e-6<=t<=z+1e-6: b=bx
        assert b!='x', t
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def save(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json','w'), indent=1, ensure_ascii=False)

# 4595
t=T(21)
man=keys(t,[(0,10,(0.0,0.10,1.0,0.90))])
save({"mediaId":4595,"level":"B","keyWord":"cry","defaultVoice":"male",
 "taps":[{"phrase":"to cry his eyes out","target":"the man","voice":"male","keys":man},
         {"phrase":"to wipe away his tears","target":"the man","voice":"male","keys":man},
         {"phrase":"to clutch a tissue box","target":"the man","voice":"male","keys":man}],
 "stillS":8.5,
 "nouns":[{"word":"a ceiling fan","x":0.40,"y":0.21,"voice":"male"},
          {"word":"tissues","x":0.11,"y":0.59,"voice":"male"},
          {"word":"a hoodie","x":0.72,"y":0.58,"voice":"male"},
          {"word":"a tissue box","x":0.35,"y":0.70,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","crying","and","clutching","a","tissue","box."],
 "answerVoice":"male",
 "notes":"Only one target (the man), so all three phrases use him; his box is almost the whole picture because his arm and the hand with the box reach the left and bottom edges. The ceiling fan is small and dim in the background. Wiping happens only at 3.0-4.5 s, clutching the box against his chest from 8.0 s."})

# 4596
woman=keys(t,[(0,10,(0.0,0.0,1.0,1.0))])
save({"mediaId":4596,"level":"A","keyWord":"nose","defaultVoice":"female",
 "taps":[{"phrase":"to blow her nose","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to cry on the sofa","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to hold a white tissue","target":"the woman","voice":"female","keys":woman}],
 "stillS":7.5,
 "nouns":[{"word":"hair","x":0.48,"y":0.10,"voice":"female"},
          {"word":"a nose","x":0.50,"y":0.37,"voice":"female"},
          {"word":"a sweater","x":0.50,"y":0.57,"voice":"female"},
          {"word":"a blanket","x":0.50,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","blowing","her","nose."],
 "answerVoice":"female",
 "notes":"Only one target; she fills the whole picture, so the box is the full frame. The sofa is only a dark shape behind her. Nose-blowing is at 4.0-7.0 s."})

# 4598
t=T(25)
w=keys(t,[(0,0,(0.0,0.13,0.57,0.87)),(0.5,0.5,(0.0,0.13,0.47,0.87)),(1.0,1.0,(0.0,0.16,0.60,0.84)),
          (1.5,1.5,(0.0,0.16,0.65,0.84)),(2.0,2.5,(0.0,0.15,0.50,0.85)),(3.0,3.0,(0.0,0.16,0.55,0.84)),
          (3.5,3.5,(0.05,0.10,0.90,0.75)),(4.0,4.0,(0.0,0.04,1.0,0.76)),(4.5,5.5,(0.0,0.04,1.0,0.70)),
          (6.0,6.5,(0.0,0.03,1.0,0.77)),(7.0,7.0,(0.0,0.07,0.78,0.62)),(7.5,12.0,(0.0,0.06,1.0,0.70))])
b=keys(t,[(0,0,(0.58,0.0,0.42,0.62)),(0.5,0.5,(0.50,0.0,0.50,0.65)),(1.0,1.0,(0.61,0.0,0.39,0.72)),
          (1.5,1.5,(0.80,0.05,0.20,0.70)),(2.0,2.5,(0.82,0.18,0.18,0.42)),(3.0,3.0,(0.82,0.20,0.18,0.52)),
          (3.5,12.0,None)])
save({"mediaId":4598,"level":"B","keyWord":"huge","defaultVoice":"female",
 "taps":[{"phrase":"to serve an espresso","target":"the barista","voice":"male","keys":b},
         {"phrase":"to clutch a huge mug","target":"the woman","voice":"female","keys":w},
         {"phrase":"to gasp in amazement","target":"the woman","voice":"female","keys":w}],
 "stillS":12.0,
 "nouns":[{"word":"shelves","x":0.75,"y":0.10,"voice":"female"},
          {"word":"glasses","x":0.50,"y":0.23,"voice":"female"},
          {"word":"a mug","x":0.50,"y":0.55,"voice":"female"},
          {"word":"a counter","x":0.50,"y":0.85,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","clutching","a","huge","mug."],
 "answerVoice":"female",
 "notes":"The barista is in the picture only in the first shot (0-3.0 s; from 2.0 s only his arm and apron at the right edge); the hands that pass the mugs at 3.5 and 7.0 s come from the camera side and are not boxed. At 1.0 s the woman's fingertips reach under the barista's hand, so her box is cut at x 0.60. The woman's box includes the mug she holds. A woman stands in the background at 0-1.0 s (staff, back turned), so 'the woman' could be questioned there."})

# 4600
m=keys(t,[(0,2.0,(0.0,0.0,1.0,0.72)),(2.5,2.5,(0.05,0.0,0.93,0.64)),(3.0,4.5,(0.08,0.0,0.79,0.64)),
          (5.0,5.0,(0.0,0.0,0.87,0.70)),(5.5,5.5,(0.07,0.0,0.80,0.55)),(6.0,6.0,(0.0,0.0,0.87,0.45)),
          (6.5,6.5,(0.10,0.0,0.78,0.60)),(7.0,7.5,(0.0,0.0,1.0,0.42)),(8.0,8.5,(0.0,0.0,1.0,0.40)),
          (9.0,9.5,(0.03,0.0,0.97,0.50)),(10.0,10.0,(0.03,0.0,0.65,0.50)),(10.5,10.5,(0.0,0.0,0.64,0.50)),
          (11.0,11.0,(0.0,0.17,0.36,0.47)),(11.5,11.5,(0.0,0.17,0.32,0.45)),(12.0,12.0,(0.0,0.20,0.27,0.30))])
wo=keys(t,[(0,2.5,None),(3.0,4.5,(0.87,0.05,0.13,0.55)),(5.0,5.5,(0.87,0.0,0.13,0.55)),
           (6.0,6.0,(0.87,0.0,0.13,0.45)),(6.5,6.5,(0.88,0.0,0.12,0.36)),(7.0,9.5,None),
           (10.0,10.0,(0.69,0.07,0.31,0.43)),(10.5,10.5,(0.65,0.04,0.35,0.46)),
           (11.0,11.0,(0.40,0.03,0.60,0.60)),(11.5,11.5,(0.42,0.05,0.58,0.58)),(12.0,12.0,(0.36,0.07,0.64,0.57))])
mt="the man in the waistcoat"
save({"mediaId":4600,"level":"B","keyWord":"exchange","defaultVoice":"male",
 "taps":[{"phrase":"to count the banknotes","target":mt,"voice":"male","keys":m},
         {"phrase":"to fan out the banknotes","target":mt,"voice":"male","keys":m},
         {"phrase":"to gasp in amazement","target":"the woman","voice":"female","keys":wo}],
 "stillS":10.0,
 "nouns":[{"word":"a beanie","x":0.80,"y":0.17,"voice":"male"},
          {"word":"a waistcoat","x":0.30,"y":0.28,"voice":"male"},
          {"word":"a coin","x":0.42,"y":0.56,"voice":"male"},
          {"word":"banknotes","x":0.62,"y":0.78,"voice":"male"}],
 "question":"What is the woman staring at?",
 "answer":["She","is","staring","at","a","fan","of","banknotes."],
 "answerVoice":"female",
 "notes":"Bystander men stand behind, so the main man is 'the man in the waistcoat'. The woman is only a narrow strip at the right edge at 3.0-6.5 s (box narrower than 0.18 so it does not overlap the man); she is fully visible from 10.0 s. At 6.5 s the man's fingertips on the fan pass under her strip and are cut from his box. From 11.0 s the man is only a sleeve and waistcoat at the left edge. The key word 'exchange' is not in the texts: the exchange itself is not clearly shown as an action of one target."})
