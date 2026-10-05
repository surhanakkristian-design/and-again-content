import json
T=[i*0.5 for i in range(25)]
def k(t,b): return dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else dict(t=t,off=True)
M={0.0:(.03,.38,.80,.62),0.5:(.02,.39,.84,.61),1.0:(.01,.40,.88,.60),1.5:(.02,.41,.86,.59),2.0:(0,.41,.80,.59),
6.5:(.34,0,.66,.62),7.0:(.40,.18,.60,.74),7.5:(.40,.13,.60,.80),8.0:(.40,.08,.60,.84),8.5:(.39,.06,.61,.86),9.0:(.38,.07,.62,.86),
9.5:(.32,.09,.68,.83),10.0:(.23,.09,.77,.83),10.5:(.30,.09,.70,.83),11.0:(.34,.09,.66,.83),11.5:(.39,.12,.61,.80),12.0:(.39,.10,.61,.82)}
L={6.5:(.12,0,.21,.15),7.0:(.12,0,.27,.36),7.5:(.11,0,.28,.36),8.0:(.10,0,.29,.40),8.5:(.10,0,.28,.40),9.0:(.09,0,.28,.40),
9.5:(.08,0,.23,.40),10.0:(.04,0,.18,.40),10.5:(.08,0,.21,.40),11.0:(.06,0,.27,.44),11.5:(.06,0,.32,.44),12.0:(.05,0,.33,.42)}
G={t:(0,0,1,1) for t in [2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]}
taps=[dict(phrase="to form a long tunnel",target="the gates",voice="female",keys=[k(t,G.get(t)) for t in T]),
dict(phrase="to slurp his ramen noodles",target="the man",voice="male",keys=[k(t,M.get(t)) for t in T]),
dict(phrase="to hang above the stall",target="the lanterns",voice="female",keys=[k(t,L.get(t)) for t in T])]
c=dict(mediaId=4998,level="B",keyWord="tunnel",defaultVoice="male",taps=taps,stillS=12.0,
nouns=[dict(word="lanterns",x=.20,y=.20,voice="male"),dict(word="a jacket",x=.75,y=.55,voice="male"),dict(word="chopsticks",x=.20,y=.63,voice="male"),dict(word="a bowl",x=.40,y=.88,voice="male")],
question="What is the man eating?",answer="He is eating ramen with chopsticks.".split(),answerVoice="male",
notes="Gates fill the whole frame 2.5-6.0 s (no person there), box = full frame. Lanterns and man overlap at the top left in the ramen shot: split vertically, so the man's box leaves out his chopstick hand under the lanterns. Key word 'tunnel' only in phrase 1 (the gates form the tunnel); still frame is the ramen shot.")
json.dump(c,open('content/4998.json','w'),indent=1)
