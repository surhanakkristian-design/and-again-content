import json
T=[i*0.5 for i in range(25)]
P=[(0,0.26,0.57,0.66),(0,0.28,0.52,0.50),(0,0.29,0.52,0.71),(0,0.49,0.37,0.36),(0,0.09,0.64,0.91),(0,0.25,0.77,0.75),
(0.29,0.31,0.44,0.66),(0.27,0.32,0.42,0.60),(0.29,0.31,0.43,0.61),(0.08,0.31,0.61,0.61),(0.27,0.31,0.44,0.61),(0.09,0.32,0.61,0.61),
(0.27,0.31,0.43,0.62),(0,0.31,1,0.63),(0,0.33,1,0.60),(0.02,0.33,0.98,0.61),(0.02,0.33,0.98,0.59),(0.02,0.34,0.98,0.59),
(0.02,0.33,0.98,0.61),(0.01,0.33,0.99,0.61)]+[(0,0.33,1,0.61)]*5
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,P)]
tap=lambda p:dict(phrase=p,target="the policeman",voice="male",keys=keys)
c=dict(mediaId=5347,level="A",keyWord="stop",defaultVoice="male",
taps=[tap("to stop the traffic"),tap("to raise his hand"),tap("to hold out his arms")],
stillS=8.0,
nouns=[dict(word="the sky",x=0.50,y=0.08,voice="male"),dict(word="a bus",x=0.50,y=0.28,voice="male"),
dict(word="a policeman",x=0.52,y=0.56,voice="male"),dict(word="a road",x=0.80,y=0.82,voice="male")],
question="What is the policeman doing?",answer=["He","is","stopping","the","traffic."],answerVoice="male",
notes="All three phrases on the policeman: the bus is always directly behind him with his arms across it, so it cannot get a box that does not overlap his; scooters change from shot to shot. 0.0-1.5 s is a POV shot: only his white-gloved raised hand/arm is visible, boxed as the policeman. Raised palm 2.5-6.0 s, arms held out 6.5-12.0 s. Key word stop (noun) is not a visible thing, so no noun for it.")
json.dump(c,open('content/5347.json','w'),indent=1)
