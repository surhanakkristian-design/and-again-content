import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
W={0.0:(0,.34,.50,.50),0.5:(.25,.29,.38,.59),1.0:(.27,.37,.18,.14),1.5:(.21,.26,.28,.38)}
M={2.0:(.32,.86,.60,.14),2.5:(.08,.27,.92,.73),3.0:(.05,.27,.95,.73),5.5:(.28,.34,.55,.38),6.0:(.30,.38,.50,.42),
7.5:(.30,.45,.28,.31),8.0:(.29,.45,.27,.31),8.5:(.32,.47,.30,.33),9.0:(.35,.49,.27,.34),9.5:(.30,.47,.30,.36),10.0:(.14,.50,.42,.50)}
B={3.5:(.39,.33,.40,.40),4.0:(.30,.31,.27,.53),4.5:(.22,.32,.30,.58),5.0:(.23,.29,.33,.67)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
c=dict(mediaId=4840,level="A",keyWord="hide",defaultVoice="female",
 taps=[dict(phrase="to hide behind a curtain",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to sit under a desk",target="the man in the blue shirt",voice="male",keys=keys(M)),
       dict(phrase="to hide behind a tree",target="the boy",voice="male",keys=keys(B))],
 stillS=6.0,
 nouns=[dict(word="a window",x=.52,y=.25,voice="female"),dict(word="a door",x=.12,y=.42,voice="female"),
        dict(word="a man",x=.55,y=.46,voice="male"),dict(word="a box",x=.55,y=.68,voice="female")],
 question="What is the boy doing?",
 answer=["He","is","hiding","behind","a","tree."],answerVoice="male",
 notes="The packet description does not match the frames well: real shots = a woman in a dark top runs and hides behind grey curtains (0-1.5 s), a man in a blue shirt sits under an office desk (2.0-3.0 s), a boy in a red T-shirt hides behind a tree trunk (3.5-5.0 s), the same man in the blue shirt sits in a cardboard box in a hallway and closes it (5.5-6.5 s; at 6.5 s he is inside the closed box -> off), a blurred pan (7.0 s), then a group of friends with the man in the blue T-shirt in the front centre jump up, throw confetti (7.5-10.0 s). 'the woman' is only the curtain woman; the women in the final group are not boxed. At 2.0 s only his blue shirt shows under the desk edge. defaultVoice by evenId (several people, no single main person).")
json.dump(c,open('content/4840.json','w'),indent=1)
