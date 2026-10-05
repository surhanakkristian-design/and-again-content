import json
G={0.0:(.24,.28,.53,.39),0.5:(.34,.32,.39,.40),1.0:(.34,.31,.34,.41),1.5:(.35,.28,.32,.39),2.0:(.35,.30,.32,.34),2.5:(.33,.30,.36,.32),
3.0:(.39,.34,.45,.30),3.5:(.29,.29,.52,.34),4.0:(.24,.30,.57,.32),4.5:(.18,.31,.69,.31),5.0:(.11,.25,.60,.28),5.5:(.03,.24,.72,.32),
6.0:(0,.22,.73,.35),6.5:(.42,.34,.22,.20),7.0:(.44,.34,.23,.21),7.5:(.41,.36,.37,.24),8.0:(.11,.30,.52,.23),8.5:(.22,.31,.50,.28),
9.0:(.18,.32,.67,.34),9.5:(.32,.30,.57,.49),10.0:(.24,.19,.65,.78),10.5:(.19,.18,.81,.78),11.0:(.10,.20,.78,.80),11.5:(.12,.19,.70,.81),12.0:(.17,.19,.68,.81)}
T=[i/2 for i in range(25)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4349,level="A",keyWord="guard",defaultVoice="male",taps=[
 dict(phrase="to run into the sea",target="the guard",voice="male",keys=keys(G)),
 dict(phrase="to ride a wave",target="the guard",voice="male",keys=keys(G)),
 dict(phrase="to hold a yellow board",target="the guard",voice="male",keys=keys(G))],
 stillS=12.0,nouns=[dict(word="a cap",x=.44,y=.26,voice="male"),dict(word="flags",x=.86,y=.36,voice="male"),
 dict(word="a guard",x=.42,y=.58,voice="male"),dict(word="a board",x=.85,y=.72,voice="male")],
 question="What is the guard holding?",answer=["He","is","holding","a","yellow","board."],answerVoice="male",
 notes="Only one real target (the guard), so all three phrases share it. A second man stands small in the background at 11.0-12.0 s; the guard's box stops before him. 'flags' = the two tall yellow banners; 'a cap' and 'a guard' are on the same person but far apart (head / chest).")
json.dump(c,open('content/4349.json','w'),indent=1,ensure_ascii=False)
