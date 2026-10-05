import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
horse=K([(.46,.04,.47,.42),(.45,.05,.52,.43),(.44,.02,.47,.52),(.44,.01,.50,.55),(.43,.0,.53,.59),(.41,.0,.56,.60),(.35,.0,.60,.63),(.32,.0,.62,.63)])
rider=K([(0,0,.45,.32),(0,0,.44,.32),(0,0,.43,.32),(0,0,.43,.32),(0,0,.42,.31),(0,0,.40,.32),(0,0,.34,.33),(0,0,.31,.35)])
c=dict(mediaId=6872,level="B",keyWord="bit",defaultVoice="female",taps=[
 dict(phrase="to bare its big teeth",target="the bay horse",voice="female",keys=horse),
 dict(phrase="to drool from its mouth",target="the bay horse",voice="female",keys=horse),
 dict(phrase="to burst out laughing",target="the rider",voice="female",keys=rider)],
 stillS=2.2,
 nouns=[dict(word="a helmet",x=.33,y=.05,voice="female"),dict(word="a bit",x=.33,y=.33,voice="female"),
        dict(word="teeth",x=.57,y=.42,voice="female"),dict(word="sand",x=.65,y=.88,voice="female")],
 question="What is the horse doing?",
 answer=["It","is","baring","its","big","teeth."],answerVoice="female",
 notes="Rider overlaps the horse's neck: split vertically at the rider's right edge, so the horse box holds the head (teeth, bit, drool) but not the neck/leg in the lower left; the bit ring sits right at the split line. Rider stops laughing and looks up from ~2.7 s.")
json.dump(c,open('content/6872.json','w'),indent=1)
