import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
woman=keys({0.0:(0.45,0.24,0.55,0.34),0.5:(0.40,0.0,0.60,0.58),1.0:(0.28,0.0,0.72,0.75),1.5:(0.25,0.0,0.75,0.68),2.0:(0.20,0.0,0.80,0.80),
 2.5:(0.05,0.11,0.95,0.50),3.0:(0.15,0.13,0.73,0.50),3.5:(0.22,0.10,0.66,0.52),4.0:(0.72,0.86,0.28,0.14),4.5:(0.0,0.10,0.15,0.36),
 5.0:(0.0,0.18,0.22,0.82),5.5:(0.0,0.20,0.17,0.80),6.0:(0.0,0.18,0.30,0.82),8.0:(0.18,0.42,0.62,0.42),8.5:(0.40,0.44,0.26,0.33),
 9.0:(0.36,0.46,0.24,0.30),9.5:(0.40,0.46,0.20,0.27),10.0:(0.37,0.46,0.27,0.20)})
comp=keys({4.0:(0.0,0.22,1.0,0.64),4.5:(0.15,0.26,0.83,0.52),5.0:(0.22,0.30,0.70,0.45),5.5:(0.17,0.33,0.77,0.42),6.0:(0.30,0.33,0.64,0.40)})
c=dict(mediaId=4869,level="A",keyWord="design",defaultVoice="female",taps=[
 dict(phrase="to draw on a tablet",target="the woman",voice="female",keys=woman),
 dict(phrase="to smile at the camera",target="the woman",voice="female",keys=woman),
 dict(phrase="to show a colourful poster",target="the computer",voice="female",keys=comp)],
 stillS=3.0,
 nouns=[dict(word="shelves",x=0.80,y=0.38,voice="female"),dict(word="a woman",x=0.50,y=0.48,voice="female"),
        dict(word="a lamp",x=0.13,y=0.39,voice="female"),dict(word="colour cards",x=0.50,y=0.80,voice="female")],
 question="What is the woman drawing on?",answer=["She","is","drawing","on","a","tablet."],answerVoice="female",
 notes="Only two clear targets (woman, iMac), woman used twice. Sketchbook hands (6.5-7.5 s) not boxed: identity unclear. At 4.5-6.0 woman and computer boxes split side by side; computer box loses a sliver of its left bezel. Key word 'design' is abstract, not a noun slot.")
json.dump(c,open('content/4869.json','w'),indent=1)
