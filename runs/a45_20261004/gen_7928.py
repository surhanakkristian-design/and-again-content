import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
wom=[(.17,.37,.50,.58),(.18,.37,.50,.58),(.16,.36,.55,.59),(.14,.35,.61,.60),(.14,.36,.54,.59),(.14,.36,.52,.59),(.12,.35,.52,.60)]
def K(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
k=K(wom)
c=dict(mediaId=7928,level="B",keyWord="overtime",defaultVoice="female",
 taps=[dict(phrase="to work overtime at her desk",target="the woman",voice="female",keys=k),
       dict(phrase="to scribble some notes",target="the woman",voice="female",keys=k),
       dict(phrase="to rub her temple",target="the woman",voice="female",keys=k)],
 stillS=0.7,
 nouns=[dict(word="an exit sign",x=.82,y=.27,voice="female"),dict(word="a takeaway box",x=.81,y=.56,voice="female"),
        dict(word="a mug",x=.83,y=.67,voice="female"),dict(word="a jacket",x=.12,y=.62,voice="female")],
 question="What is the woman doing?",answer=["She","is","working","overtime","at","her","desk."],answerVoice="female",
 notes="All three phrases use the woman: the cleaner and the security guard are tiny, far in the background and overlap each other by the exit, so they are not used as targets. She rubs her temple only at the end (3.2 s). 'a jacket' = the jacket hanging on her chair.")
json.dump(c,open('content/7928.json','w'),indent=1)
