import json
T=[round(i*0.5,1) for i in range(21)]
H={0.0:(.66,.2,.34,.8),0.5:(.48,.19,.52,.81),1.0:(.5,.22,.5,.78),1.5:(.6,.21,.4,.18),2.0:(.63,.24,.37,.76),
2.5:(.58,.27,.2,.72),3.0:(.54,.29,.21,.62),3.5:(.59,.3,.19,.56),4.0:(.6,.31,.2,.54),4.5:(.48,0,.35,.78),
5.0:(.71,.25,.29,.75),5.5:(.66,.22,.34,.78),6.5:(.66,.31,.34,.69),7.5:(.54,.31,.23,.55),8.0:(.56,.38,.2,.4),
8.5:(.56,.43,.21,.32),9.0:(.58,.35,.18,.41),9.5:(.56,.22,.23,.47),10.0:(.57,.23,.23,.43)}
D={1.5:(.43,.39,.5,.61),2.0:(.3,.34,.32,.66),2.5:(.33,.35,.25,.64),3.0:(.34,.36,.2,.58),3.5:(.41,.37,.18,.52),
4.0:(.42,.37,.18,.51),4.5:(.2,0,.28,.6),5.0:(.42,.33,.29,.67),5.5:(.48,.4,.18,.47),6.5:(.33,.37,.33,.62),
7.5:(.36,.37,.18,.46),8.0:(.38,.41,.18,.35),8.5:(.38,.45,.18,.3),9.0:(.4,.37,.18,.39),9.5:(.38,.27,.18,.41),10.0:(.39,.28,.18,.33)}
P={7.0:(0,.45,.62,.23)}
def keys(b):
    return [dict(t=t,x=b[t][0],y=b[t][1],w=b[t][2],h=b[t][3]) if t in b else dict(t=t,off=True) for t in T]
c=dict(mediaId=4915,level="A",keyWord="shoulder",defaultVoice="male",
taps=[dict(phrase="to wear a grey hoodie",target="the man in the hoodie",voice="male",keys=keys(H)),
      dict(phrase="to wear a colourful dress",target="the girl in the dress",voice="female",keys=keys(D)),
      dict(phrase="to put down a phone",target="the hand",voice="male",keys=keys(P))],
stillS=8.0,
nouns=[dict(word="the sky",x=.5,y=.15,voice="male"),dict(word="a hoodie",x=.68,y=.47,voice="male"),
       dict(word="a dress",x=.5,y=.57,voice="female"),dict(word="tiles",x=.5,y=.85,voice="male")],
question="What are the five friends doing?",
answer=["They","are","jumping","into","the","air."],answerVoice="male",
notes="All group actions (arms over shoulders, walking, jumping) are shared by all five, so phrases 1-2 are clothing states; phrase 3 is the hand placing a phone on the wall at 7.0 only (one frame). Key word 'shoulder' left out of the nouns: there are ten shoulders, no single clear place. 1.5: the hoodie man is behind the girl, box on his head only. 4.5 is a legs-only shot (dress hem and grey trousers). 6.0 back view: both off. Answer does not reuse phrase/noun words (the jump is the clearest shared action).")
json.dump(c,open('content/4915.json','w'),indent=1)
