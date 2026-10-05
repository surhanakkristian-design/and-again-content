import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
dog=K([(0,0.29,0.45,0.64),(0,0.31,0.49,0.62),(0,0.32,0.44,0.62),(0,0.31,0.44,0.63),(0,0.29,0.49,0.65),(0,0.29,0.50,0.65),(0,0.29,0.49,0.65),(0,0.29,0.50,0.65)])
man=K([(0.46,0.19,0.54,0.79),(0.50,0.20,0.50,0.78),(0.45,0.21,0.55,0.77),(0.46,0.21,0.54,0.77),(0.50,0.18,0.50,0.80),(0.51,0.18,0.49,0.80),(0.50,0.18,0.50,0.80),(0.51,0.17,0.49,0.81)])
c=dict(mediaId=7867,level="B",keyWord="help",defaultVoice="male",
taps=[dict(phrase="to examine a screwdriver",target="the man",voice="male",keys=man),
dict(phrase="to carry a wooden stool",target="the man",voice="male",keys=man),
dict(phrase="to wear a green apron",target="the dog",voice="male",keys=dog)],
stillS=3.2,
nouns=[dict(word="a brass lamp",x=0.66,y=0.09,voice="male"),dict(word="a screwdriver",x=0.56,y=0.38,voice="male"),
dict(word="screws",x=0.61,y=0.605,voice="male"),dict(word="an apron",x=0.12,y=0.76,voice="male")],
question="What is the man doing?",answer="He is examining a small screwdriver.".split(),answerVoice="male",
notes="Only two targets (man, dog); two man phrases. Dog paw and man hand touch at 0.2/1.2, boxes split at x~0.45. Dog phrase is a state (apron) because no dog action fits only the dog (both lean on the counter).")
json.dump(c,open('content/7867.json','w'),indent=1)
