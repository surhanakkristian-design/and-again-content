import json
T=[i*0.5 for i in range(21)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
W={0.0:(0.26,0.10,0.70,0.55),0.5:(0.22,0.08,0.72,0.62),1.0:(0.20,0.09,0.70,0.78),1.5:(0.0,0.12,1.0,0.76),2.0:(0.13,0.11,0.83,0.66),
2.5:(0.18,0.13,0.76,0.64),3.0:(0.04,0.16,0.82,0.82),3.5:(0.18,0.18,0.74,0.80),4.0:(0.31,0.23,0.60,0.60),4.5:(0.43,0.25,0.50,0.48),
5.0:(0.20,0.26,0.60,0.74),5.5:(0.0,0.23,0.60,0.75),6.0:(0.0,0.26,0.74,0.74),6.5:(0.0,0.21,0.82,0.79),7.0:(0.02,0.13,0.80,0.87),
7.5:(0.06,0.26,0.78,0.74),8.0:(0.13,0.36,0.70,0.64),8.5:(0.08,0.28,0.76,0.72),9.0:(0.10,0.25,0.74,0.75),9.5:(0.10,0.25,0.74,0.75),10.0:(0.08,0.24,0.76,0.76)}
k=keys(W)
c=dict(mediaId=628,level="A",keyWord="sadness",defaultVoice="female",taps=[
 dict(phrase="to put books in a box",target="the woman",voice="female",keys=k),
 dict(phrase="to hold a book",target="the woman",voice="female",keys=k),
 dict(phrase="to cry on the floor",target="the woman",voice="female",keys=k)],
 stillS=8.0,nouns=[dict(word="a pencil",x=0.36,y=0.42,voice="female"),dict(word="glasses",x=0.50,y=0.56,voice="female"),dict(word="books",x=0.85,y=0.85,voice="female"),dict(word="boxes",x=0.10,y=0.65,voice="female")],
 question="What is the woman doing?",answer=["She","is","crying","on","the","floor."],answerVoice="female",
 notes="Only one possible target (the woman), used for all three phrases. Key word 'sadness' is abstract, not used as a noun. Nouns at 8.0: 'books' = the pile bottom right (she also hugs a single book, not labelled); 'boxes' = the stack at the left edge (more boxes behind her); 'a pencil' is the pencil in her hair bun.")
json.dump(c,open('content/628.json','w'),indent=1)
