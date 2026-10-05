import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
woman=K([(0.50,0.24,0.50,0.52),(0.52,0.28,0.48,0.52),(0.50,0.26,0.45,0.55),(0.52,0.20,0.48,0.59),
         (0.51,0.28,0.36,0.55),(0.51,0.14,0.49,0.63),(0.50,0.30,0.38,0.56),(0.52,0.25,0.35,0.62)])
green=K([(0.11,0.60,0.39,0.24),(0.10,0.60,0.40,0.24),(0.08,0.61,0.42,0.24),(0.07,0.61,0.43,0.24),
         (0.04,0.61,0.46,0.25),(0.02,0.61,0.48,0.25),(0.0,0.62,0.49,0.26),(0.0,0.62,0.50,0.26)])
navy=K([(0.20,0.46,0.30,0.14),(0.19,0.46,0.31,0.14),(0.17,0.47,0.33,0.14),(0.16,0.47,0.34,0.14),
        (0.13,0.47,0.37,0.14),(0.11,0.47,0.39,0.14),(0.10,0.48,0.39,0.14),(0.09,0.48,0.41,0.14)])
c=dict(mediaId=8037,level="B",keyWord="waking",defaultVoice="female",
 taps=[dict(phrase="to leap into the air",target="the woman in lilac",voice="female",keys=woman),
       dict(phrase="to sleep face down",target="the man in green",voice="male",keys=green),
       dict(phrase="to sleep open-mouthed",target="the man in navy",voice="male",keys=navy)],
 stillS=3.7,
 nouns=[dict(word="the sky",x=0.30,y=0.12,voice="female"),
        dict(word="lamps",x=0.13,y=0.45,voice="female"),
        dict(word="a mop",x=0.86,y=0.55,voice="female"),
        dict(word="a jacket",x=0.62,y=0.84,voice="female")],
 question="What is the woman in lilac doing?",
 answer=["She","is","leaping","into","the","air."],
 answerVoice="female",
 notes="Key word 'waking' not a visible noun, not placed. The woman in lilac jumps at 0.2-2.7 and stands with hands on cheeks at 3.2-3.7 (end of the jump). Her box starts at x 0.50-0.52 to stay clear of the two sleeping men, so her outstretched left arm is cut at 0.2, 0.7, 1.7, 2.7. The man in green sleeps face down on his arm/book; the man in navy lies on his cheek with his mouth open (box at the 0.14 minimum height, split from the man in green at y 0.60-0.62). The woman with brown hair sleeping above the man in navy is not a target and partly sits in his box. The cleaner with the mop is mostly hidden behind the jumping woman and not used as a target. 'lamps' = the group of green reading lamps on the left.")
json.dump(c,open('content/8037.json','w'),indent=1)
