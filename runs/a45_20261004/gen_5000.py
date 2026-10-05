import json
T=[i*0.5 for i in range(25)]
def k(t,b): return dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else dict(t=t,off=True)
M=[(.21,.03,.79,.75),(.21,.03,.79,.72),(.23,.03,.77,.67),(0,0,1,.67),(0,0,.95,.60),(0,0,1,.62),(0,0,.97,.60),(0,0,1,.56),(0,0,.97,.57),(0,0,1,.68),(0,0,1,.58),(0,0,1,.67),
(.06,.02,.89,.57),(.09,0,.85,.58),(0,0,.96,.64),(0,0,.96,.60),(0,0,.96,.57),(.06,0,.94,.58),(.03,0,.90,.74),(.02,.03,.92,.73),(.06,0,.84,.59),(.10,.01,.80,.61),(.02,.04,.90,.59),(.01,.16,.95,.48),(.12,.12,.70,.48)]
H={11.5:(0,.65,1,.35),12.0:(0,.61,1,.39)}
man=[k(t,b) for t,b in zip(T,M)]
taps=[dict(phrase="to cut thin slices",target="the man",voice="male",keys=man),
dict(phrase="to put fish on rice",target="the man",voice="male",keys=man),
dict(phrase="to clap for the chef",target="the hands",voice="male",keys=[k(t,H.get(t)) for t in T])]
c=dict(mediaId=5000,level="A",keyWord="thin",defaultVoice="male",taps=taps,stillS=10.0,
nouns=[dict(word="a man",x=.50,y=.33,voice="male"),dict(word="sushi",x=.70,y=.62,voice="male"),dict(word="a plate",x=.50,y=.76,voice="male")],
question="What is the man cutting?",answer="He is cutting thin slices of fish.".split(),answerVoice="male",
notes="Clapping hands (off-screen person) only at 11.5-12.0 s, both hands in one box below the counter edge; man's box ends above them. 'to put fish on rice' = 4.0-5.5 s (white fish slice on rice).")
json.dump(c,open('content/5000.json','w'),indent=1)
