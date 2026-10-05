import json
T=[i*0.5 for i in range(21)]
G={1.5:(0,0,.20,.68),2.0:(0,.14,.36,.72),2.5:(0,.33,.42,.65),3.0:(0,.43,.47,.57),3.5:(.10,.42,.40,.58),4.0:(.10,.39,.40,.60),4.5:(.09,.37,.38,.61),
5.0:(.10,.47,.40,.53),5.5:(.33,.37,.42,.63),6.0:(.26,.30,.57,.70),6.5:(0,.30,1,.70),7.0:(0,.29,.82,.71),7.5:(.22,.33,.52,.67),8.0:(.28,.30,.54,.70),
8.5:(.19,.31,.81,.69),9.0:(.20,.35,.62,.65),9.5:(.19,.33,.81,.67),10.0:(.59,.34,.41,.66)}
B={2.0:(0,0,.24,.14),2.5:(0,.16,.34,.17),3.0:(0,.28,.40,.15),3.5:(0,.27,.42,.15),4.0:(0,.23,.44,.16),4.5:(0,.22,.40,.15),5.0:(0,.26,.36,.21),
5.5:(0,.21,.33,.30),6.0:(0,.17,.18,.48),7.5:(0,.29,.22,.71),8.0:(0,.27,.27,.66),8.5:(0,.28,.19,.68),9.0:(0,.25,.20,.45),9.5:(0,.37,.18,.24),10.0:(0,.18,.28,.44)}
D={0.0:(.57,.04,.30,.24),0.5:(.61,.05,.27,.23),1.0:(.60,.09,.27,.23),1.5:(.60,.28,.29,.23),2.0:(.65,.46,.27,.23),2.5:(.67,.59,.28,.22),3.0:(.68,.62,.30,.20),
3.5:(.73,.60,.27,.22),4.0:(.75,.58,.25,.23),4.5:(.82,.58,.18,.22),7.0:(.82,.61,.18,.33),7.5:(.78,.63,.22,.25),8.0:(.82,.66,.18,.22),9.0:(0,.80,.18,.20),
9.5:(0,.68,.18,.18),10.0:(.08,.63,.50,.24)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=598,level="A",keyWord="rain",defaultVoice="female",
taps=[dict(phrase="to dance in the rain",target="the girl",voice="female",keys=keys(G)),
dict(phrase="to wear a white shirt",target="the boy",voice="male",keys=keys(B)),
dict(phrase="to walk on four legs",target="the dog",voice="female",keys=keys(D))],
stillS=3.5,
nouns=[dict(word="a roof",x=.30,y=.15,voice="female"),dict(word="a tree",x=.80,y=.22,voice="female"),
dict(word="a dog",x=.86,y=.72,voice="female"),dict(word="a boat",x=.50,y=.87,voice="female")],
question="What is the girl doing?",
answer=["She","is","dancing","in","the","rain."],answerVoice="female",
notes="Boy and girl stand pressed together at 2.0-5.5: the boy's box holds only his head/shoulders above the girl's head, the girl's box her body below (his lower shirt falls into or beside her box). Boy: no action fits only him (both laugh, both stand under the roof), so a state phrase. He walks and laughs beside the dancing girl at 7.5-10 but does not dance himself; verifier please check 'to dance in the rain' fits only the girl. Edge slivers: girl at 1.5 is a headless body at the left edge; boy at 6.0 and 9.5 (arm only); dog at 4.5, 7.0, 8.0, 9.0 (ears only). At 7.0/8.0/10.0 the girl's far hand / forearm lies outside her box to keep clear of the dog's box. 'rain' is not a noun slot (it has no single place); 'a boat' is the paper boat in the gutter; several palm trees, the 'a tree' pill is on the big one.")
json.dump(c,open('content/598.json','w'),indent=1)
