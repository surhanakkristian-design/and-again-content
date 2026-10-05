import json
B={0.0:(0,0,1,0.55),0.5:(0,0,1,0.55),1.0:(0,0,1,0.55),1.5:(0,0,1,0.55),2.0:(0,0.16,0.95,0.6),2.5:(0,0.16,0.95,0.52),
3.0:(0,0.16,1.0,0.57),3.5:(0,0.09,1,0.63),4.0:(0,0.04,0.95,0.66),4.5:(0.08,0.02,0.92,0.62),5.0:(0.1,0.24,0.85,0.76),
5.5:(0.15,0.15,0.85,0.85),6.0:(0.1,0.03,0.9,0.97),6.5:(0.1,0.03,0.9,0.97),7.0:(0.40,0.37,0.28,0.2),7.5:(0.40,0.37,0.28,0.2),
8.0:(0.40,0.37,0.26,0.19),8.5:(0.35,0.17,0.32,0.35),9.0:(0.35,0.06,0.36,0.47)}
keys=[dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in B.items()]
taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in ["to do a big puzzle","to wear big glasses","to raise her arms"]]
c=dict(mediaId=4859,level="A",keyWord="piece",defaultVoice="female",taps=taps,stillS=2.5,
nouns=[dict(word="a window",x=0.45,y=0.07,voice="female"),dict(word="books",x=0.86,y=0.34,voice="female"),
dict(word="glasses",x=0.56,y=0.42,voice="female"),dict(word="pieces",x=0.62,y=0.86,voice="female")],
question="What is the woman doing?",answer=["She","is","doing","a","big","puzzle."],answerVoice="female",
notes="Only one person, so all three taps share the woman. 'to raise her arms' happens only at 8.5-9.0 s. Key word 'piece' shown as plural 'pieces' (many loose pieces on the table).")
json.dump(c,open('content/4859.json','w'),indent=1)
