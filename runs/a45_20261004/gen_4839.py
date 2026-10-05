import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
M={0.0:(.44,.21,.56,.75),0.5:(.44,.21,.56,.62),1.0:(.41,.24,.59,.62),1.5:(.36,.11,.40,.38),2.0:(.36,.16,.38,.36),2.5:(.35,.19,.40,.32),
3.0:(.36,.19,.38,.33),3.5:(.36,.19,.40,.32),4.0:(.42,.20,.47,.22),4.5:(.63,.30,.35,.68),5.0:(.33,.20,.45,.24),5.5:(.50,.24,.50,.52),
6.0:(.50,.29,.50,.45),6.5:(.50,.26,.50,.47),7.0:(.50,.26,.50,.48),7.5:(.67,.38,.18,.23),8.0:(.69,.40,.22,.22),8.5:(.71,.40,.20,.21),
9.0:(.69,.37,.21,.24),9.5:(.72,.32,.19,.26),10.0:(.76,.33,.20,.27)}
B={4.0:(0,.42,.72,.56),4.5:(0,.24,.62,.54),5.0:(.28,.44,.42,.50)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
c=dict(mediaId=4839,level="A",keyWord="move",defaultVoice="male",
 taps=[dict(phrase="to push a small car",target="the young man",voice="male",keys=keys(M)),
       dict(phrase="to move a big box",target="the young man",voice="male",keys=keys(M)),
       dict(phrase="to sit on a swing",target="the boy",voice="male",keys=keys(B))],
 stillS=1.0,
 nouns=[dict(word="a house",x=.13,y=.12,voice="male"),dict(word="a tree",x=.88,y=.12,voice="male"),
        dict(word="a car",x=.15,y=.45,voice="male"),
        dict(word="a road",x=.20,y=.86,voice="male")],
 question="What is the young man doing?",
 answer=["He","is","pushing","a","small","car."],answerVoice="male",
 notes="Montage of one young man in a dark T-shirt: car 0-1.0 s, shopping trolley 1.5-3.5 s (seen through the trolley), swing with a boy 4.0-5.0 s, wooden crate 5.5-7.0 s, stone ball with friends 7.5-10.0 s (he is the man in the dark grey T-shirt on the right). At 4.0 and 5.0 s the man stands behind the boy, so the boxes are split horizontally (man = head and shoulders above the boy). 'the boy' is the small child on the swing. 'a big box' = the crate.")
json.dump(c,open('content/4839.json','w'),indent=1)
