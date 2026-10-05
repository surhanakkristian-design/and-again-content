import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
drv=K([(0.11,0.52,0.95,1.0),(0.12,0.52,0.95,1.0),(0.10,0.52,0.96,1.0),(0.10,0.51,0.96,1.0),(0.09,0.51,0.96,1.0),(0.09,0.51,0.98,1.0),(0.09,0.52,0.96,1.0),(0.08,0.52,0.98,1.0)])
bride=K([(0.53,0.28,0.86,0.50),(0.52,0.28,0.85,0.50),(0.49,0.26,0.85,0.50),(0.49,0.26,0.85,0.50),(0.49,0.25,0.85,0.50),(0.49,0.24,0.85,0.50),(0.50,0.26,0.87,0.50),(0.49,0.26,0.87,0.50)])
pink=K([(0.12,0.27,0.52,0.50),None,None,None,(0.13,0.27,0.48,0.50),(0.09,0.27,0.48,0.50),(0.11,0.27,0.49,0.50),(0.09,0.27,0.48,0.50)])
c=dict(mediaId=6868,level="B",keyWord="berlin",defaultVoice="female",
 taps=[dict(phrase="to grip the steering wheel",target="the chauffeur",voice="female",keys=drv),
       dict(phrase="to wear a lace wedding dress",target="the bride",voice="female",keys=bride),
       dict(phrase="to wear a pale pink dress",target="the woman in pink",voice="female",keys=pink)],
 stillS=2.7,
 nouns=[dict(word="feathers",x=0.25,y=0.24,voice="female"),dict(word="a pillow",x=0.56,y=0.34,voice="female"),
        dict(word="a peaked cap",x=0.27,y=0.60,voice="female"),dict(word="a steering wheel",x=0.78,y=0.80,voice="female")],
 question="What are the two passengers doing?",answer=["They","are","having","a","pillow","fight."],answerVoice="female",
 notes="Key word 'berlin' (a type of car) is not a labelable noun here, not among the nouns. Both women in the back swing pillows, so their phrases are states (dress) - no action fits only one of them. The woman in pink is hidden behind the feather-covered glass at 0.7-1.7 (off); at 2.2-3.7 she is visible but blurred through the feathers. Back-seat boxes end at y 0.50, the chauffeur box starts at 0.51-0.52.")
json.dump(c,open('content/6868.json','w'),indent=1)
