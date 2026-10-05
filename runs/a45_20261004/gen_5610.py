import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
dog=K([(0.01,0.44,0.57,0.45),(0.11,0.46,0.75,0.27),(0.20,0.44,0.60,0.30),(0.33,0.44,0.45,0.31),(0.13,0.43,0.66,0.32),(0.19,0.46,0.62,0.29),(0.20,0.47,0.62,0.29),(0.19,0.47,0.66,0.28)])
wom=K([(0.58,0.26,0.40,0.45),(0.58,0.24,0.40,0.21),(0.62,0.24,0.36,0.20),(0.62,0.24,0.36,0.20),(0.62,0.22,0.34,0.21),(0.55,0.21,0.43,0.25),(0.50,0.20,0.48,0.26),(0.48,0.20,0.50,0.26)])
c=dict(mediaId=5610,level="A",keyWord="be allowed to",defaultVoice="female",
 taps=[dict(phrase="to jump onto the sofa",target="the dog",voice="female",keys=dog),
       dict(phrase="to lie down next to her",target="the dog",voice="female",keys=dog),
       dict(phrase="to pet the dog",target="the woman",voice="female",keys=wom)],
 stillS=3.7,
 nouns=[dict(word="a fireplace",x=0.45,y=0.38,voice="female"),dict(word="a picture",x=0.66,y=0.20,voice="female"),
        dict(word="a dog",x=0.45,y=0.63,voice="female"),dict(word="a sofa",x=0.50,y=0.83,voice="female")],
 question="What is the woman doing?",answer=["She","is","petting","the","dog."],answerVoice="female",
 notes="Dog sits in front of the woman's lap the whole clip: her box is cut to her upper body above the dog. Only two real targets, so the dog has two phrases. She pets the dog only from ~2.7 s.")
json.dump(c,open('content/5610.json','w'),indent=1)
