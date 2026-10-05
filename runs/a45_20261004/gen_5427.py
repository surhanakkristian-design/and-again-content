import json
T=[i*0.5 for i in range(19)]
O=None
E=[(.00,.00,1.0,.82),(.00,.00,1.0,.76),(.00,.00,1.0,.86)]+[O]*16
P=[O,O,O,O,(.00,.06,1.0,.94),(.00,.06,1.0,.94),O,O,O,O,(.86,.14,.14,.62),(.79,.26,.21,.52),(.69,.33,.23,.45),(.74,.32,.16,.44),(.73,.35,.14,.42),O,(.70,.31,.20,.50),(.71,.33,.12,.16),(.70,.35,.15,.25)]
B=[O,O,O,(.28,.03,.46,.71),O,O,(.00,.10,1.0,.90),(.00,.04,.97,.96),O,O,(.66,.08,.20,.47),(.61,.20,.18,.38),(.62,.22,.16,.10),(.60,.27,.14,.30),(.58,.25,.15,.30),(.60,.32,.16,.26),O,(.58,.28,.13,.12),O]
def keys(L): return [dict(t=t,off=True) if k is None else dict(t=t,x=k[0],y=k[1],w=k[2],h=k[3]) for t,k in zip(T,L)]
c=dict(mediaId=5427,level="B",keyWord="seal",defaultVoice="male",
taps=[dict(phrase="to hold up a sealed envelope",target="the woman with the envelope",voice="female",keys=keys(E)),
dict(phrase="to clutch a gold trophy",target="the woman with a ponytail",voice="female",keys=keys(P)),
dict(phrase="to wear a dark green hoodie",target="the boy in the green hoodie",voice="male",keys=keys(B))],
stillS=1.0,
nouns=[dict(word="curly hair",x=.85,y=.33,voice="male"),dict(word="a wax seal",x=.50,y=.52,voice="male"),
dict(word="an envelope",x=.27,y=.61,voice="male"),dict(word="a denim shirt",x=.14,y=.78,voice="male")],
question="What is the ponytailed woman holding?",answer=["She","is","clutching","a","gold","trophy."],answerVoice="female",
notes="Many cuts: 0-1.0 envelope close-up (curly-haired woman), 1.5 blurry group (boy in green hoodie centre; the woman at the right edge may be the ponytail woman but no trophy, left off), 2.0-2.5 ponytail woman with the trophy, 3.0-3.5 boy close-up, 4.0-4.5 legs only (all off), 5.0-9.0 group on the stage. Envelope woman boxed only in her close-up: in the group shots several women have curly hair and she cannot be identified with certainty (likely the leftmost woman in the light shirt). In the group the boy stands partly behind the ponytail woman: boxes split (6.0 boy box = only his head above her). Boy hidden at 8.0 and 9.0; ponytail woman hidden at 7.5 (hug). Boy: no action fits only him (the ponytail woman also clenches a fist, others clasp hands), so a state phrase. Trophy: gold figure on a blue column.")
json.dump(c,open('content/5427.json','w'),indent=1)
