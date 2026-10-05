import json
G=[(0.0,.28,.21,.47,.74),(0.5,.26,.21,.49,.74),(1.0,.24,.22,.50,.73),(1.5,.26,.22,.47,.73),(2.0,.02,0,.96,1),(2.5,.02,0,.96,1),
(3.0,.13,.23,.80,.77),(3.5,.16,.25,.78,.75),(4.0,.14,.24,.79,.76),(4.5,.15,.21,.80,.79),(5.0,.04,.18,.96,.82),(5.5,.07,.17,.93,.83),
(6.0,.04,.15,.96,.85),(6.5,.07,.14,.93,.86),(7.0,.34,.11,.66,.89),(7.5,.27,.06,.73,.94),(8.0,.41,.13,.59,.87),(8.5,.44,.19,.56,.81),
(9.0,.28,.18,.72,.82),(9.5,.28,.17,.72,.83),(10.0,.30,.19,.70,.81)]
F={0.0:(.76,.26,.22,.64),0.5:(.76,.27,.23,.63),1.0:(.74,.27,.25,.63),1.5:(.73,.27,.26,.63)}
def k(t,v):
    if v is None: return {"t":t,"off":True}
    x,y,w,h=v; return {"t":t,"x":x,"y":y,"w":w,"h":h}
gk=[k(t,(x,y,w,h)) for t,x,y,w,h in G]
fk=[k(t,F.get(t)) for t,*_ in G]
c={"mediaId":4800,"level":"B","keyWord":"groom","defaultVoice":"male",
"taps":[{"phrase":"to adjust his bow tie","target":"the groom","voice":"male","keys":gk},
{"phrase":"to grin over his shoulder","target":"the man behind him","voice":"male","keys":fk},
{"phrase":"to step into the garden","target":"the groom","voice":"male","keys":gk}],
"stillS":8.0,
"nouns":[{"word":"a groom","x":.68,"y":.30,"voice":"male"},{"word":"a hedge","x":.40,"y":.47,"voice":"male"},
{"word":"a guest","x":.20,"y":.57,"voice":"male"},{"word":"a rose","x":.62,"y":.63,"voice":"male"}],
"question":"What is the groom adjusting?","answer":["He","is","adjusting","his","bow","tie."],"answerVoice":"male",
"notes":"0-1.5 s is a mirror shot: the groom box is on his reflection (centre); the dark back in the left foreground is the real groom and is left untapped. The man behind him appears only 0-1.5 s (off later). 2.0-2.5 s close-up of the groom's chest while someone's hands pin the rose (whole frame boxed as the groom). 'a groom' noun is on his head, 'a rose' on his lapel (same figure but separate places)."}
json.dump(c,open('content/4800.json','w'),indent=1)
