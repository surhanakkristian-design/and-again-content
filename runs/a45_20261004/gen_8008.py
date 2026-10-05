import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(d): return [ (dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if d.get(t) else dict(t=t,off=True)) for t in T]
wom=keys({0.2:(0.10,0.33,0.34,0.38),0.7:(0.07,0.41,0.36,0.30),1.2:(0.0,0.43,0.38,0.31),1.7:(0.02,0.42,0.36,0.33),2.2:(0.02,0.41,0.37,0.35),2.7:(0.02,0.45,0.44,0.30),3.2:(0.0,0.44,0.34,0.33),3.7:(0.0,0.44,0.34,0.33)})
man=keys({0.2:(0.47,0.53,0.46,0.25),0.7:(0.44,0.55,0.56,0.21),1.2:(0.47,0.56,0.50,0.24),1.7:(0.40,0.55,0.60,0.20),2.2:(0.55,0.50,0.39,0.27),2.7:(0.59,0.45,0.41,0.33),3.2:(0.61,0.44,0.39,0.35),3.7:(0.62,0.43,0.38,0.36)})
spr=keys({0.2:(0.22,0.72,0.20,0.16),0.7:(0.22,0.74,0.20,0.16),1.2:(0.22,0.76,0.20,0.15),1.7:(0.21,0.78,0.20,0.14),2.2:(0.17,0.80,0.20,0.14),2.7:(0.17,0.82,0.20,0.14),3.2:(0.15,0.84,0.20,0.14),3.7:(0.16,0.84,0.20,0.14)})
c=dict(mediaId=8008,level="B",keyWord="suddenly",defaultVoice="female",taps=[
 dict(phrase="to throw up her hands",target="the woman",voice="female",keys=wom),
 dict(phrase="to clutch a baguette",target="the man",voice="male",keys=man),
 dict(phrase="to shoot water into the air",target="the sprinkler",voice="female",keys=spr)],
 stillS=3.7,
 nouns=[dict(word="a baguette",x=0.78,y=0.66,voice="female"),dict(word="a straw hat",x=0.19,y=0.85,voice="female"),
        dict(word="a picnic blanket",x=0.68,y=0.88,voice="female"),dict(word="trees",x=0.35,y=0.20,voice="female")],
 question="What is the man holding?",answer=["He","is","clutching","a","baguette."],answerVoice="male",
 notes="Sprinkler box = sprinkler head + bottom of the water jet (head is small). Woman throws up her hands 0.2-2.2, then crouches laughing. Key word 'suddenly' is an adverb, not used in the answer (placement ambiguity).")
json.dump(c,open('content/8008.json','w'),indent=1)
