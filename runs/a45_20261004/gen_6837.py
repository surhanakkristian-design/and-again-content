import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,off=True) if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
woman=K([(.71,.08,.29,.84),(.69,.08,.31,.84),(.66,.12,.34,.80),(.63,.18,.37,.76),(.60,.24,.40,.66),(.59,.27,.41,.62),(.53,.30,.42,.68),(.55,.34,.40,.62)])
man=K([(.36,.00,.34,.52),(.32,.00,.36,.62),(.31,.08,.34,.56),(.32,.09,.31,.50),(.34,.15,.26,.47),(.32,.16,.27,.50),(.32,.18,.20,.50),(.32,.19,.22,.47)])
bald=K([(.13,.23,.22,.29),None,(.12,.28,.19,.27),(.12,.29,.19,.26),(.12,.31,.22,.24),(.13,.31,.19,.24),(.12,.35,.20,.26),(.13,.36,.19,.25)])
c=dict(mediaId=6837,level="A",keyWord="apply",defaultVoice="female",
 taps=[dict(phrase="to put out a fire",target="the woman in yellow",voice="female",keys=woman),
       dict(phrase="to hold up a plate",target="the man in green",voice="male",keys=man),
       dict(phrase="to hold a salad bowl",target="the bald man",voice="male",keys=bald)],
 stillS=2.7,
 nouns=[dict(word="a plate",x=.51,y=.17,voice="female"),dict(word="a party hat",x=.76,y=.29,voice="female"),
        dict(word="a plant",x=.13,y=.42,voice="female"),dict(word="a barbecue",x=.20,y=.84,voice="female")],
 question="What is the woman in yellow doing?",
 answer=["She","is","putting","out","a","fire."],answerVoice="female",
 notes="Woman's box leaves out her far-left foot/hose where the man in green overlaps. Bald man hidden by spray at 0.7 s (off). Key word 'apply' (verb) not placeable.")
json.dump(c,open("content/6837.json","w"),indent=1)
