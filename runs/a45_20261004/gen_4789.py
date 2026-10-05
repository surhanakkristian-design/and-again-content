import json
T=[i*0.5 for i in range(19)]
W={0.0:(.12,.3,.54,.4),0.5:(.14,.3,.52,.41),1.0:(.1,.33,.56,.38),1.5:(.14,.32,.5,.38),2.0:(.14,.28,.5,.42),
2.5:(.3,.46,.42,.21),3.0:(.29,.44,.41,.23),3.5:(.3,.47,.4,.2),4.0:(.27,.44,.41,.22),4.5:(.29,.44,.4,.22),
5.0:(.3,.44,.4,.22),5.5:(.29,.45,.4,.21),6.0:(.3,.44,.41,.2),6.5:(.08,.23,.87,.5),7.0:(.02,.31,.8,.45),
7.5:(.17,.4,.67,.33),8.0:(.2,.46,.58,.27),8.5:(.19,.49,.59,.24),9.0:(.2,.5,.54,.22)}
M={0.0:(.67,.18,.33,.52),0.5:(.67,.18,.33,.45),1.0:(.67,.22,.33,.48),1.5:(.68,.23,.32,.47),
2.5:(.48,.35,.28,.11),3.5:(.42,.35,.3,.12),4.0:(.69,.36,.15,.29),4.5:(.7,.35,.29,.3)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4789,level="B",keyWord="authority",defaultVoice="female",taps=[
 dict(phrase="to stamp an official document",target="the woman in green",voice="female",keys=keys(W)),
 dict(phrase="to sign a document",target="the woman in green",voice="female",keys=keys(W)),
 dict(phrase="to hold out an open folder",target="the man in the dark suit",voice="male",keys=keys(M))],
 stillS=8.5,nouns=[dict(word="a map",x=.5,y=.2,voice="female"),dict(word="a businesswoman",x=.5,y=.62,voice="female"),
 dict(word="a ring binder",x=.15,y=.74,voice="female"),dict(word="a desk",x=.6,y=.87,voice="female")],
 question="What is the woman in green doing?",answer="She is stamping an official document.".split(),answerVoice="female",
 notes="Busy office with several staff walking through. The dark-suited man is boxed where he is visible (0-1.5 s beside her, 2.5-4.5 s at the map / with a folder); at 2.5 and 3.5 s he stands right behind her head, so his box is only the strip above her head. Off at 6.5 s (mostly hidden behind her). 'Sign a document' (pen, 3.0 and 5.0 s) is only done by her.")
json.dump(c,open('content/4789.json','w'),indent=1)
