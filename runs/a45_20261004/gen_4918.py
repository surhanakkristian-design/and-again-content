import json
T=[i*0.5 for i in range(19)]
M={1.0:(.16,.22,.6,.78),1.5:(.08,.07,.92,.93),2.0:(.3,0,.7,.5),2.5:(.22,0,.78,.77),3.0:(.42,0,.58,.87),3.5:(.08,0,.92,.9),
   4.0:(.05,.19,.9,.81),4.5:(.41,.07,.52,.93),6.0:(.28,.3,.5,.4),6.5:(0,0,.76,.57),
   7.5:(.47,.12,.53,.88),8.0:(.3,.09,.7,.91),8.5:(.2,.08,.8,.92),9.0:(.22,.1,.78,.9)}
W={0.0:(.1,.04,.88,.94),0.5:(.03,.08,.97,.92),2.0:(0,0,.3,.47),4.0:(.22,.05,.18,.14),4.5:(.2,.12,.2,.14),
   5.0:(.05,.12,.95,.88),5.5:(0,.1,1,.9),7.5:(0,.2,.47,.8),8.0:(0,.22,.3,.75),8.5:(0,.27,.2,.7),9.0:(0,.4,.2,.6)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4918,level="B",keyWord="stairs",defaultVoice="male",
 taps=[dict(phrase="to rush up the stairs",target="the young man",voice="male",keys=keys(M)),
       dict(phrase="to struggle with heavy bags",target="the elderly woman",voice="female",keys=keys(W)),
       dict(phrase="to give a thumbs-up",target="the young man",voice="male",keys=keys(M))],
 stillS=4.0,
 nouns=[dict(word="stairs",x=.62,y=.78,voice="male"),dict(word="a hoodie",x=.47,y=.22,voice="male"),
        dict(word="jeans",x=.5,y=.52,voice="male"),dict(word="a paper bag",x=.78,y=.38,voice="male")],
 question="What is the young man carrying?",
 answer=["He","is","carrying","paper","bags","up","the","stairs."],answerVoice="male",
 notes="Frames differ from the packet description (order of shots; trolley only 6.0-7.0 s, so not used as a target). At 4.0 s the woman is a small figure beside the man's head: her box is 0.18 x 0.14 and the man's box starts below his head (y 0.19); at 4.5 s the man's box starts right of her (x 0.41). 2.0 s is a close-up of hands only: split at x 0.30 (cardigan sleeve left = woman, hoodie sleeves right = man). 7.0 s: only a sliver of the man's hand, set off. Two paper bags at 4.0 s (one under each arm); the pill is on the right one.")
json.dump(c,open('content/4918.json','w'),indent=1,ensure_ascii=False)
