import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else dict(t=t,off=True) for t,b in zip(T,boxes)]
woman=K([(0.0,0.19,0.80,0.72),(0.0,0.30,0.80,0.62),(0.0,0.28,0.79,0.58),(0.02,0.27,0.74,0.65),
         (0.05,0.16,0.86,0.77),(0.0,0.16,1.0,0.78),(0.0,0.0,1.0,1.0),(0.0,0.02,1.0,0.98)])
c=dict(mediaId=8011,level="A",keyWord="survive",defaultVoice="female",
 taps=[dict(phrase="to climb up the mountain",target="the woman",voice="female",keys=woman),
       dict(phrase="to hold two ice axes",target="the woman",voice="female",keys=woman),
       dict(phrase="to wear a red jacket",target="the woman",voice="female",keys=woman)],
 stillS=2.2,
 nouns=[dict(word="the sky",x=0.45,y=0.07,voice="female"),
        dict(word="a woman",x=0.30,y=0.45,voice="female"),
        dict(word="a rock",x=0.78,y=0.57,voice="female"),
        dict(word="snow",x=0.72,y=0.85,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","climbing","up","the","mountain."],answerVoice="female",
 notes="Only one person in the clip, so all three phrases target the woman. Key word 'survive' is a verb, not placeable as a noun.")
json.dump(c,open('content/8011.json','w'),indent=1)
