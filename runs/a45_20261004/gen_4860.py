import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
W={0.0:(0.62,0,0.38,0.30),0.5:(0,0,1,0.29),1.0:(0,0,1,0.30),1.5:(0,0,1,0.29),2.0:(0,0,1,0.29),2.5:(0.03,0,0.8,0.5),
3.0:(0,0,0.8,0.5),3.5:(0,0,0.8,0.52),4.0:(0,0,0.78,0.5),4.5:(0.05,0,0.95,0.21),5.0:(0,0,1,0.35),5.5:(0,0,1,0.36),
6.0:(0,0,1,0.35),6.5:(0.22,0.02,0.6,0.27),7.0:(0.28,0,0.55,0.38),7.5:(0.3,0,0.55,0.38),8.0:(0.22,0,0.6,0.37),
8.5:(0.22,0,0.62,0.36),9.0:(0.22,0,0.6,0.38)}
TB={0.0:(0.38,0.14,0.24,0.17),0.5:(0.36,0.62,0.24,0.16),1.0:(0.36,0.63,0.27,0.16),1.5:(0.42,0.63,0.25,0.16),
2.0:(0.40,0.63,0.27,0.16),2.5:(0.40,0.58,0.24,0.20)}
K={4.5:(0.22,0.22,0.52,0.36),5.0:(0.22,0.36,0.54,0.37),5.5:(0.2,0.37,0.56,0.38),6.0:(0.18,0.36,0.57,0.40),
6.5:(0.18,0.30,0.58,0.35),7.0:(0.13,0.39,0.72,0.34),7.5:(0.08,0.40,0.80,0.36),8.0:(0.08,0.42,0.84,0.36),
8.5:(0.3,0.45,0.42,0.27),9.0:(0.3,0.47,0.42,0.27)}
def keys(B): return [dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) if t in B else dict(t=t,off=True) for t in T]
taps=[dict(phrase="to stare in disbelief",target="the woman",voice="female",keys=keys(W)),
dict(phrase="to sink to the bottom",target="the tablet",voice="female",keys=keys(TB)),
dict(phrase="to dissolve into a cloud",target="the white block",voice="female",keys=keys(K))]
c=dict(mediaId=4860,level="B",keyWord="bubble",defaultVoice="female",taps=taps,stillS=1.5,
nouns=[dict(word="bubbles",x=0.48,y=0.50,voice="female"),dict(word="a tablet",x=0.54,y=0.72,voice="female"),
dict(word="a spoon",x=0.14,y=0.59,voice="female"),dict(word="a countertop",x=0.5,y=0.90,voice="female")],
question="What is the woman doing?",answer=["She","is","staring","at","the","fizzing","water."],answerVoice="female",
notes="Woman sits behind the glass/tank the whole clip, so her box is cut off above the glass/block (split line). Tablet off 3.0-4.0 (dissolved/hidden by the spoon); at 2.5 the box covers the second tablet sinking and the first at the bottom. Block only from 4.5 s; at 7.0-8.0 box includes the white cloud around it.")
json.dump(c,open('content/4860.json','w'),indent=1)
