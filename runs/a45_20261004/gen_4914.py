import json
T=[round(i*0.5,1) for i in range(21)]
G={0.0:(.27,.28,.5,.42),0.5:(.08,.19,.9,.77),3.5:(0,.4,.32,.54),4.0:(0,.41,.29,.4),4.5:(.13,.38,.32,.34),
5.5:(.7,.39,.3,.32),7.0:(.54,.36,.32,.5),8.0:(0,.13,1,.87),8.5:(.02,.07,.98,.93),9.0:(0,.38,.72,.62),
9.5:(.1,.57,.25,.26),10.0:(.6,.46,.4,.53)}
R={2.0:(.42,.25,.48,.75),2.5:(.17,.24,.73,.76),3.0:(.12,.22,.78,.78)}
L={7.0:(.18,.4,.35,.6),7.5:(.2,.3,.68,.7)}
def keys(b):
    return [dict(t=t,x=b[t][0],y=b[t][1],w=b[t][2],h=b[t][3]) if t in b else dict(t=t,off=True) for t in T]
c=dict(mediaId=4914,level="A",keyWord="guitar",defaultVoice="male",
taps=[dict(phrase="to play the guitar",target="the young man",voice="male",keys=keys(G)),
      dict(phrase="to run down the street",target="the runner",voice="male",keys=keys(R)),
      dict(phrase="to dance and laugh",target="the little girl",voice="female",keys=keys(L))],
stillS=0.0,
nouns=[dict(word="buildings",x=.25,y=.08,voice="male"),dict(word="trees",x=.1,y=.28,voice="male"),
       dict(word="a guitar",x=.45,y=.45,voice="male"),dict(word="a bench",x=.15,y=.56,voice="male")],
question="What is the young man doing?",
answer=["He","is","playing","the","guitar."],answerVoice="male",
notes="At 6.5 a second person with a guitar appears at the right edge (x .8-1, y .45-.6), probably a generation artefact: the young man's box there is off to avoid a wrong target. At 7.0 the girl stands in front of the young man: split at x .53/.54. 7.5 shows him only on a phone screen: off. The runner (man, bib 13) is visible 2.0-3.0 only; at 1.0-1.5 a different, small woman runner with a bib passes at the right edge in the background (left off, not a target) - she also runs, check whether that matters.")
json.dump(c,open('content/4914.json','w'),indent=1)
