import json
T=[i*0.5 for i in range(19)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
W=[(0,0.05,0.72,0.95),(0,0.05,0.74,0.95),(0,0.07,0.70,0.93),(0,0.10,0.64,0.90),(0,0.05,0.80,0.95),(0,0.03,0.80,0.97),
   (0,0.07,0.80,0.93),(0.05,0.12,0.82,0.88),(0.10,0.18,0.74,0.82),(0,0.22,0.70,0.78),(0.03,0.17,0.76,0.83),(0,0.24,0.88,0.76),
   (0,0.08,0.58,0.92),(0,0,0.68,1),None,None,(0.25,0.30,0.37,0.70),(0.05,0.32,0.75,0.68),(0.07,0.35,0.81,0.65)]
D=[None]*12+[(0.60,0,0.40,1),(0.70,0,0.30,1),(0.02,0.02,0.96,0.96),(0.02,0.02,0.96,0.96),(0.63,0,0.37,1),(0.81,0,0.19,1),(0.89,0,0.11,1)]
w=K(W); d=K(D)
c=dict(mediaId=5008,level="B",keyWord="unlock",defaultVoice="female",
 taps=[dict(phrase="to unlock a brass letterbox",target="the woman",voice="female",keys=w),
       dict(phrase="to sort through old keys",target="the woman",voice="female",keys=w),
       dict(phrase="to swing wide open",target="the wooden door",voice="female",keys=d)],
 stillS=9.0,
 nouns=[dict(word="the sky",x=0.55,y=0.10,voice="female"),dict(word="ivy",x=0.17,y=0.35,voice="female"),
        dict(word="a lanyard",x=0.55,y=0.62,voice="female"),dict(word="flowerpots",x=0.15,y=0.73,voice="female")],
 question="What is the woman doing?",answer=["She","is","unlocking","a","brass","letterbox."],answerVoice="female",
 notes="Wooden door target: at 8.0-9.0 only the right door wing is boxed; at 9.0 it is a thin sliver at the right edge. Woman marked off at 7.0 (absent) and 7.5 (only a face in the door gap). Letterbox only at 0-1.5 s; the woman pushes the doors open but the phrase is about the door.")
json.dump(c,open('content/5008.json','w'),indent=1)
