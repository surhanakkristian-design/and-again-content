import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(d): return [ (dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if d.get(t) else dict(t=t,off=True)) for t in T]
man=keys({0.2:(0.0,0.16,0.20,0.84),0.7:(0.0,0.15,0.13,0.85),1.2:(0.0,0.14,0.15,0.86),1.7:(0.0,0.14,0.15,0.86),2.2:(0.0,0.13,0.13,0.87),2.7:(0.0,0.13,0.12,0.87),3.2:(0.0,0.13,0.13,0.87),3.7:(0.0,0.13,0.13,0.87)})
wom=keys({0.2:(0.21,0.25,0.50,0.32),0.7:(0.14,0.25,0.60,0.32),1.2:(0.16,0.24,0.58,0.33),1.7:(0.16,0.24,0.58,0.33),2.2:(0.14,0.23,0.60,0.34),2.7:(0.13,0.23,0.62,0.35),3.2:(0.14,0.22,0.62,0.36),3.7:(0.14,0.23,0.64,0.36)})
ted=keys({0.2:(0.40,0.57,0.48,0.14),0.7:(0.40,0.57,0.50,0.14),1.2:(0.41,0.57,0.50,0.14),1.7:(0.41,0.57,0.52,0.14),2.2:(0.41,0.57,0.53,0.14),2.7:(0.42,0.58,0.55,0.14),3.2:(0.43,0.58,0.56,0.15),3.7:(0.44,0.59,0.56,0.15)})
c=dict(mediaId=8009,level="B",keyWord="surgery",defaultVoice="female",taps=[
 dict(phrase="to operate on a teddy bear",target="the woman",voice="female",keys=wom),
 dict(phrase="to hold out a metal dish",target="the man",voice="male",keys=man),
 dict(phrase="to lie on the operating table",target="the teddy bear",voice="female",keys=ted)],
 stillS=2.2,
 nouns=[dict(word="an operating lamp",x=0.55,y=0.07,voice="female"),dict(word="tiles",x=0.75,y=0.32,voice="female"),
        dict(word="a teddy bear",x=0.74,y=0.64,voice="female"),dict(word="a tray",x=0.33,y=0.73,voice="female")],
 question="What is the woman doing?",answer=["She","is","operating","on","a","teddy","bear."],answerVoice="female",
 notes="Woman box = upper body above the table only (her hands touch the teddy; split along the teddy's top edge). Man's box excludes his outstretched hands/dish where they cross in front of the woman (2.7-3.7). Key word 'surgery' is abstract, not placed as a noun.")
json.dump(c,open('content/8009.json','w'),indent=1)
