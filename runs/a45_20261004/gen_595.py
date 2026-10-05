import json
B=[(0,.33,1,.45),(0,.16,1,.55),(0,.18,1,.63),(.23,.10,.60,.70),(.20,.09,.57,.68),(.20,.10,.58,.70),(.15,.11,.60,.80),(.06,.34,.86,.54),(.01,.26,.82,.46),(.04,.26,.83,.45),(0,.23,.83,.58),(.01,.20,.79,.62),(.03,.19,.77,.53),(.06,.23,.79,.51),(.09,.16,.90,.53),(.03,.33,.69,.31),(.35,.39,.40,.32),(.47,.31,.53,.38),(.33,.25,.45,.39),(.26,.24,.46,.38),(.27,.21,.40,.45)]
keys=[dict(t=i*0.5,x=b[0],y=b[1],w=b[2],h=b[3]) for i,b in enumerate(B)]
c=dict(mediaId=595,level="A",keyWord="rabbit",defaultVoice="male",
taps=[dict(phrase=p,target="the rabbit",voice="male",keys=keys) for p in ["to eat green leaves","to wash its face","to jump over the grass"]],
stillS=2.5,
nouns=[dict(word="the sky",x=.30,y=.08,voice="male"),dict(word="a rabbit",x=.47,y=.52,voice="male"),
dict(word="grass",x=.82,y=.40,voice="male"),dict(word="leaves",x=.70,y=.85,voice="male")],
question="What is the rabbit eating?",
answer=["It","is","eating","green","leaves."],answerVoice="male",
notes="Only one usable target: the rabbit (the birds in the sky are tiny specks, sometimes two or three, not tappable). 'grass' pill sits on the tall grass tuft at the right; 'leaves' on the clover patch. The rabbit jumps at 0-1.0 and 7.0-8.5, eats at 3.5-5.5, washes its face at 6.0-6.5.")
json.dump(c,open('content/595.json','w'),indent=1)
