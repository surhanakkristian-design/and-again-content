import json
T=[i*0.5 for i in range(21)]
O=None
wom=[(0,0,.80,.98),(0,0,.78,.98),(0,0,.80,1),(0,0,.81,1),(0,0,.48,1),(0,0,.50,1),(0,0,.48,1),(0,0,.46,1),(0,0,.53,1),(0,0,.78,1),(0,0,.81,1),(0,0,1,1),(0,0,.92,1),(0,0,.95,1),(0,.08,1,.92),(0,.10,.82,.90),(0,0,.47,1),(0,.02,.45,.98),(0,.08,.49,.92),(0,.12,.57,.88),(0,.13,.54,.87)]
man=[(.82,.14,.18,.44),(.82,.14,.18,.50),(.82,.17,.18,.50),(.82,.17,.18,.47),(.50,0,.50,.70),(.52,0,.48,.67),(.50,0,.50,.67),(.48,0,.52,.67),(.55,0,.45,.72),(.80,.12,.20,.75),(.82,.32,.18,.48),O,O,O,O,(.82,.44,.18,.56),(.49,0,.51,.84),(.47,0,.53,.87),(.51,.08,.49,.90),(.59,.08,.41,.90),(.56,.07,.44,.83)]
def k(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
kw=k(wom)
d=dict(mediaId=480,level="A",keyWord="mineral water",defaultVoice="female",
 taps=[dict(phrase="to open the bottle",target="the woman",voice="female",keys=kw),
       dict(phrase="to drink the water",target="the woman",voice="female",keys=kw),
       dict(phrase="to wear a blue T-shirt",target="the man",voice="male",keys=k(man))],
 stillS=9.0,
 nouns=[dict(word="mineral water",x=.60,y=.78,voice="female"),dict(word="a bottle",x=.38,y=.65,voice="female"),
        dict(word="a table",x=.55,y=.94,voice="female"),dict(word="a man",x=.75,y=.35,voice="male")],
 question="What is the woman pouring?",
 answer=["She","is","pouring","mineral","water","into","a","glass."],answerVoice="female",
 notes="Only two tappable targets (woman, man), so two phrases use the woman. Close-ups: 0-5 s show mostly the woman's hands/shirt and only the man's blue T-shirt at the right; 5.5-7.0 s the man is just a sliver at the edge (off). Where her hand with the glass reaches in front of him (2.0-4.0, 8.0-9.0 s) the boxes are split vertically between the two bodies, so her fingers fall partly into his box. 'to wear a blue T-shirt' is a state: the man does nothing that the woman does not also do. Only the woman is seen drinking.")
json.dump(d,open("content/480.json","w"),indent=1)
