import json
T=[i*0.5 for i in range(17)]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
M=[(0,0.17,0.93,0.82),(0,0.17,0.95,0.80),(0,0.18,0.93,0.82),(0,0.17,0.95,0.82),(0,0.18,0.95,0.80),(0,0.17,0.97,0.80),
   (0,0.17,0.95,0.82),(0,0.17,0.97,0.82),(0,0.18,0.95,0.80),(0,0.17,0.97,0.80),(0,0.17,0.95,0.82),(0,0.17,1.0,0.82),
   (0,0.18,1.0,0.80),(0,0.18,1.0,0.80),(0,0.15,1.0,0.84),(0,0.16,1.0,0.84),(0,0.17,1.0,0.86)]
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
k=keys(M)
d=dict(mediaId=1,level="A",keyWord="break",defaultVoice="male",
 taps=[dict(phrase="to laugh at his phone",target="the man",voice="male",keys=k),
       dict(phrase="to touch his head",target="the man",voice="male",keys=k),
       dict(phrase="to open his mouth wide",target="the man",voice="male",keys=k)],
 stillS=0.5,
 nouns=[dict(word="a curtain",x=0.25,y=0.08,voice="male"),
        dict(word="a phone",x=0.68,y=0.40,voice="male"),
        dict(word="a sweater",x=0.25,y=0.58,voice="male"),
        dict(word="books",x=0.60,y=0.80,voice="male")],
 question="What is the man doing?",
 answer=["He","is","laughing","at","his","phone."],answerVoice="male",
 notes="Only one living target (the man), so all three phrases use him with the same keys. He laughs at the phone until about 3 s, touches his head 5.5-6.5 s, mouth wide open at 7.5 s. The answer describes the first half of the clip only. Key word 'break' is not a visible noun, so it is not placed. 'books' = the two open books stacked on the desk.")
json.dump(d,open("content/1.json","w"),indent=1)
