import json
T=[i*0.5 for i in range(21)]
# (man_top, split_x, woman_top); man x=0..split, woman split..1, both to the bottom
S=[(0.31,0.65,0.39),(0.31,0.67,0.39),(0.35,0.61,0.38),(0.31,0.60,0.38),(0.30,0.56,0.38),(0.30,0.55,0.38),(0.32,0.57,0.38),
   (0.31,0.65,0.38),(0.31,0.66,0.38),(0.31,0.68,0.38),(0.35,0.66,0.39),(0.31,0.68,0.40),(0.31,0.66,0.40),(0.32,0.66,0.41),
   (0.31,0.63,0.41),(0.31,0.68,0.41),(0.31,0.70,0.40),(0.31,0.70,0.39),(0.37,0.61,0.40),(0.31,0.63,0.40),(0.28,0.65,0.38)]
M=[dict(t=t,x=0.0,y=a,w=s,h=round(1-a,2)) for t,(a,s,b) in zip(T,S)]
W=[dict(t=t,x=s,y=b,w=round(1-s,2),h=round(1-b,2)) for t,(a,s,b) in zip(T,S)]
c=dict(mediaId=5036,level="A",keyWord="learn",defaultVoice="male",taps=[
 dict(phrase="to learn to juggle",target="the man",voice="male",keys=M),
 dict(phrase="to clap her hands",target="the woman",voice="female",keys=W),
 dict(phrase="to wear a blue jacket",target="the woman",voice="female",keys=W)],
 stillS=9.0,nouns=[dict(word="the sky",x=0.35,y=0.10,voice="male"),dict(word="buildings",x=0.22,y=0.32,voice="male"),
 dict(word="a man",x=0.30,y=0.80,voice="male"),dict(word="a woman",x=0.82,y=0.85,voice="female")],
 question="What is the man doing?",answer=["He","is","learning","to","juggle."],answerVoice="male",
 notes="Two people side by side; boxes split along a vertical line between them. At 3.5-8.5 the man's hand with a ball reaches in front of the woman and is cut off by the split. She claps at 9.0-10.0 only. Woman also juggles/throws balls, so no ball action is used for her. Hand on head at 1.0 (fumble).")
json.dump(c,open('content/5036.json','w'),indent=1)
