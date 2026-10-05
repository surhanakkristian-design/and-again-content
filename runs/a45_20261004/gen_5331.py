import json
T=[i*0.5 for i in range(21)]
J=[(0.25,0.52,0.42,0.37),(0.26,0.51,0.43,0.37),(0.27,0.51,0.41,0.38),(0.26,0.52,0.42,0.36),(0.27,0.52,0.41,0.38),(0.27,0.52,0.40,0.37),
(0.25,0.54,0.40,0.37),(0.26,0.54,0.39,0.37),(0.25,0.54,0.40,0.37),(0.26,0.55,0.41,0.36),(0.28,0.56,0.39,0.35),(0.28,0.56,0.38,0.34),
(0.28,0.55,0.40,0.34),(0.28,0.55,0.40,0.34),(0.29,0.55,0.38,0.34),(0.28,0.55,0.38,0.35),(0.31,0.53,0.31,0.31),(0.30,0.53,0.32,0.30),
(0.27,0.54,0.33,0.30),(0.22,0.54,0.35,0.30),(0.20,0.53,0.30,0.31)]
Wm=[(0.20,0.08,0.74,0.44),(0.25,0.08,0.70,0.43),(0.27,0.10,0.66,0.41),(0.27,0.10,0.66,0.42),(0,0.10,1,0.42),(0.08,0.10,0.88,0.42),
(0.15,0.12,0.80,0.42),(0.15,0.12,0.80,0.42),(0.18,0.12,0.76,0.42),(0.20,0.11,0.74,0.44),(0.18,0.13,0.78,0.43),(0.13,0.11,0.83,0.45),
(0.15,0.09,0.80,0.46),(0.17,0.09,0.78,0.46),(0.17,0.08,0.78,0.47),(0.17,0.07,0.78,0.48),(0.02,0.12,0.97,0.41),(0.07,0.13,0.90,0.40),
(0.13,0.18,0.84,0.36),(0.18,0.18,0.80,0.36),(0.13,0.18,0.84,0.35)]
def ks(L): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
wk,jk=ks(Wm),ks(J)
d=dict(mediaId=5331,level="B",keyWord="fitness",defaultVoice="female",
taps=[dict(phrase="to squeeze an orange",target="the strong woman",voice="female",keys=wk),
dict(phrase="to crush a watermelon",target="the strong woman",voice="female",keys=wk),
dict(phrase="to fill with fresh juice",target="the glass jug",voice="female",keys=jk)],
stillS=9.5,
nouns=[dict(word="a thatched roof",x=0.50,y=0.08,voice="female"),dict(word="a sports top",x=0.62,y=0.45,voice="female"),
dict(word="a jug",x=0.40,y=0.70,voice="female"),dict(word="watermelon",x=0.74,y=0.80,voice="female")],
question="What is the strong woman crushing?",answer=["She","is","crushing","a","watermelon","with","her","bare","hands."],answerVoice="female",
notes="The jug stands in front of the woman's body, so her box ends at the jug's rim and the jug box starts there (her hips and, at t 2.0 and 8.0-8.5, her lower arms/hands are outside her box). Key word 'fitness' is abstract, not used as a noun. 'watermelon' pill on the right half; another half lies at the left edge.")
json.dump(d,open("content/5331.json","w"),indent=1)
