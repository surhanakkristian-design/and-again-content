import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
woman=keys({2.5:(0.04,0.14,0.90,0.72),3.0:(0.0,0.09,1.0,0.83),3.5:(0.0,0.09,0.98,0.80)})
girl=keys({4.0:(0.12,0.2,0.80,0.78),4.5:(0.02,0.27,0.92,0.73),5.0:(0.04,0.24,0.88,0.76)})
singer=keys({5.5:(0.0,0.2,1.0,0.8),6.0:(0.0,0.13,1.0,0.87),6.5:(0.0,0.03,1.0,0.97),7.0:(0.0,0.18,1.0,0.82)})
c=dict(mediaId=4867,level="B",keyWord="thumb",defaultVoice="male",taps=[
 dict(phrase="to hold up a frying pan",target="the woman",voice="female",keys=woman),
 dict(phrase="to give two thumbs up",target="the girl",voice="female",keys=girl),
 dict(phrase="to sing with his eyes closed",target="the singer",voice="male",keys=singer)],
 stillS=5.0,
 nouns=[dict(word="a thumb",x=0.22,y=0.42,voice="male"),dict(word="a blanket",x=0.87,y=0.58,voice="male"),dict(word="a T-shirt",x=0.48,y=0.80,voice="male")],
 question="What is the girl doing?",answer=["She","is","giving","two","thumbs","up."],answerVoice="female",
 notes="Montage of 5 shots; gamer and arena performer not used as targets. 'a thumb' sits on her left-of-frame thumb; the other thumb carries no noun. defaultVoice male (mixed montage, evenId false).")
json.dump(c,open('content/4867.json','w'),indent=1)
