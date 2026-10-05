import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if t in d else dict(t=t, off=True) for t in T]
worm={0.0:(.41,.47,.20,.17),0.5:(.38,.42,.23,.22),1.0:(.28,.39,.34,.27),1.5:(.16,.39,.49,.27),2.0:(.09,.38,.62,.28),2.5:(.03,.38,.76,.29),
3.0:(.02,.42,.89,.26),3.5:(.04,.38,.96,.31),4.0:(.08,.38,.92,.24),4.5:(.13,.39,.87,.25),5.0:(.21,.41,.79,.26),5.5:(.28,.42,.72,.25),
6.0:(.30,.42,.70,.22),6.5:(.34,.42,.66,.22),7.0:(.36,.42,.64,.22),7.5:(.38,.43,.62,.21),8.0:(.41,.42,.59,.19),8.5:(.42,.36,.28,.25),
9.0:(.41,.43,.19,.16),9.5:(.44,.47,.18,.14)}
snail={0.0:(.61,.25,.36,.20),0.5:(.61,.25,.36,.20),1.0:(.62,.26,.38,.18),1.5:(.65,.26,.35,.18),2.0:(.72,.25,.28,.17),2.5:(.79,.26,.21,.17),3.0:(.82,.27,.18,.15)}
c=dict(mediaId=885,level="A",keyWord="worm",defaultVoice="male",taps=[
 dict(phrase="to come out of the ground",target="the worm",voice="male",keys=keys(worm)),
 dict(phrase="to have a brown shell",target="the snail",voice="male",keys=keys(snail)),
 dict(phrase="to move over a stone",target="the worm",voice="male",keys=keys(worm))],
 stillS=2.0,
 nouns=[dict(word="leaves",x=.30,y=.12,voice="male"),dict(word="a snail",x=.84,y=.36,voice="male"),
        dict(word="a worm",x=.38,y=.47,voice="male"),dict(word="the ground",x=.50,y=.80,voice="male")],
 question="What is the worm doing?",
 answer=["It","is","coming","out","of","the","ground."],answerVoice="male",
 notes="Only two living targets (worm, snail); the worm has two phrases. The snail does not visibly act, so its phrase is a state. The worm moves over the grey stone at about 3.5-5.5 s. Snail leaves the frame after 3.0 s; at 2.5-3.0 s worm and snail boxes are split tightly (snail box at 3.0 s is narrow at the right edge). The worm also goes back into the ground at the end (8.0-9.5 s); the question/answer describes the first, longer action.")
json.dump(c,open('content/885.json','w'),indent=1,ensure_ascii=False)
