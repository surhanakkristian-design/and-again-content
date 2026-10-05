import json
T=[i*0.5 for i in range(21)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
man={0.0:(0.40,0.14,0.22,0.18),0.5:(0.45,0.10,0.40,0.62),1.0:(0.18,0.02,0.82,0.96),1.5:(0.20,0.12,0.80,0.88),2.0:(0.32,0.24,0.68,0.76),
2.5:(0.30,0.20,0.70,0.80),3.0:(0.38,0.28,0.62,0.72),3.5:(0.42,0.10,0.58,0.90),4.0:(0.50,0.25,0.50,0.75),4.5:(0.45,0.24,0.55,0.76),
5.0:(0.40,0.21,0.60,0.79),5.5:(0.21,0.22,0.79,0.78),6.0:(0.25,0.20,0.75,0.80),6.5:(0.26,0.26,0.60,0.36),7.0:(0.18,0.39,0.50,0.33),
7.5:(0.18,0.41,0.56,0.33),8.0:(0.26,0.24,0.52,0.74),8.5:(0.42,0.13,0.42,0.82),9.0:(0.38,0.16,0.36,0.70),9.5:(0.32,0.14,0.42,0.72),10.0:(0.29,0.12,0.40,0.62)}
w={1.5:(0.0,0.12,0.20,0.42),3.5:(0.0,0.02,0.36,0.50),4.0:(0.0,0.05,0.48,0.58),4.5:(0.0,0.06,0.43,0.60),5.0:(0.0,0.0,0.38,0.50),5.5:(0.0,0.0,0.20,0.44),6.0:(0.0,0.0,0.24,0.33)}
c=dict(mediaId=623,level="A",keyWord="rude",defaultVoice="male",taps=[
 dict(phrase="to look at his phone",target="the young man",voice="male",keys=keys(man)),
 dict(phrase="to put a cup down",target="the waitress",voice="female",keys=keys(w)),
 dict(phrase="to put his feet up",target="the young man",voice="male",keys=keys(man))],
 stillS=2.5,nouns=[dict(word="a phone",x=0.70,y=0.54,voice="male"),dict(word="sunglasses",x=0.78,y=0.27,voice="male"),dict(word="a boot",x=0.60,y=0.83,voice="male"),dict(word="a fork",x=0.12,y=0.78,voice="male")],
 question="What is the young man doing?",answer=["He","is","looking","at","his","phone."],answerVoice="male",
 notes="Many cuts. Waitress = dark-haired woman in grey T-shirt (1.5, 3.5-6.0); a different blonde woman carries a tray from 6.5 (not a target). At 0.5 a woman in grey seen from behind may be the waitress - left off. Croissant avoided as a noun: a second croissant on the tray at the back. At 5.5/6.0 the waitress box is cut at her upper arm to stay clear of the man's reaching hand.")
json.dump(c,open('content/623.json','w'),indent=1)
