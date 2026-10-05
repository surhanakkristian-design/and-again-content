import json
times=[i*0.5 for i in range(21)]
H={4.5:.9,7.0:.95,7.5:.95,9.5:.92,10.0:.92}
keys=[dict(t=t,x=0.0,y=0.0,w=1.0,h=H.get(t,.85)) for t in times]
tg="the woman"
c=dict(mediaId=5073,level="A",keyWord="medicine",defaultVoice="female",
 taps=[dict(phrase=p,target=tg,voice="female",keys=keys) for p in ["to take her medicine","to stick out her tongue","to drink some water"]],
 stillS=2.0,
 nouns=[dict(word="medicine",x=.31,y=.56,voice="female"),dict(word="a spoon",x=.68,y=.47,voice="female"),
        dict(word="a glass",x=.87,y=.81,voice="female"),dict(word="pills",x=.33,y=.86,voice="female")],
 question="What is the woman doing?",answer=["She","is","taking","her","medicine."],answerVoice="female",
 notes="Only one person, close-up filling the frame, so all three phrases target the woman with a near full-frame box. 'medicine' pill sits on the brown bottle in her hand at 2.0 s.")
json.dump(c,open('content/5073.json','w'),indent=1)
