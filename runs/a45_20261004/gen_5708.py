import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
W=K([(0.03,0.43,0.74,0.39),(0.11,0.45,0.58,0.37),(0.10,0.48,0.58,0.34),(0.09,0.40,0.55,0.42),(0.09,0.21,0.49,0.61),(0.06,0.20,0.59,0.65),(0.08,0.22,0.59,0.76),(0.10,0.23,0.60,0.77)])
H=K([(0.63,0.23,0.26,0.20),(0.67,0.23,0.24,0.21),(0.69,0.24,0.23,0.23),(0.66,0.24,0.25,0.21),(0.66,0.24,0.25,0.31),(0.67,0.26,0.24,0.30),(0.68,0.28,0.22,0.24),(0.71,0.29,0.19,0.18)])
c=dict(mediaId=5708,level="B",keyWord="care",defaultVoice="female",
 taps=[dict(phrase="to spread her coat wide",target="the young woman",voice="female",keys=W),
       dict(phrase="to clutch a wet dog",target="the young woman",voice="female",keys=W),
       dict(phrase="to stand behind a trolley",target="the man in the hood",voice="male",keys=H)],
 stillS=0.7,
 nouns=[dict(word="a street lamp",x=0.16,y=0.17,voice="female"),dict(word="a shopping trolley",x=0.86,y=0.60,voice="female"),
        dict(word="a dog",x=0.56,y=0.68,voice="female"),dict(word="tarmac",x=0.45,y=0.90,voice="female")],
 question="What is the young woman doing?",answer=["She","is","hugging","the","wet","dog","to","her","chest."],answerVoice="female",
 notes="Dog not used as a tap target (it only stands/gets carried). Hooded man is partly hidden behind the trolleys; his box covers head and upper body only, cut above the woman's box. Hugging happens from 2.2 s on.")
json.dump(c,open('content/5708.json','w'),indent=1)
