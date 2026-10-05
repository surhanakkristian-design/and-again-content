import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.11,0.38,0.79,0.30),(0.10,0.37,0.83,0.31),(0.10,0.38,0.84,0.31),(0.09,0.36,0.89,0.33),
   (0.07,0.37,0.88,0.33),(0.06,0.37,0.92,0.33),(0.04,0.37,0.94,0.33),(0.02,0.37,0.97,0.33)]
L=[(0.43,0.12,0.22,0.21),(0.43,0.12,0.24,0.21),(0.43,0.12,0.23,0.21),(0.43,0.12,0.24,0.21),
   (0.43,0.11,0.24,0.21),(0.43,0.11,0.24,0.21),(0.42,0.10,0.25,0.21),(0.42,0.10,0.25,0.21)]
k=lambda B:[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
c=dict(mediaId=5549,level="B",keyWord="ambitious",defaultVoice="male",
 taps=[dict(phrase="to put his feet up",target="the man",voice="male",keys=k(M)),
       dict(phrase="to loosen his tie",target="the man",voice="male",keys=k(M)),
       dict(phrase="to hang from the ceiling",target="the amber lamp",voice="male",keys=k(L))],
 stillS=3.2,
 nouns=[dict(word="skyscrapers",x=0.40,y=0.34,voice="male"),dict(word="a painting",x=0.88,y=0.30,voice="male"),
        dict(word="a globe",x=0.33,y=0.46,voice="male"),dict(word="takeaway cups",x=0.22,y=0.89,voice="male")],
 question="What is the man doing?",answer=["He","is","resting","his","feet","on","the","desk."],answerVoice="male",
 notes="Only one person; 2 phrases on the man, 1 on the hanging amber lamp (a brass desk lamp also stands on the desk but does not hang). 'to loosen his tie' = tugging the tie at 0.2-0.7 s. Man box covers his outstretched legs to the shoes on the desk. Key word 'ambitious' is an adjective, no noun slot.")
json.dump(c,open('content/5549.json','w'),indent=1)
