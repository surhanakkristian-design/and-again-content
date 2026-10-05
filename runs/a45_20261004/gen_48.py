import json
OFF=None
def keys(T,B):
    out=[]
    for t,a in zip(T,B):
        if a is None: out.append(dict(t=t,off=True))
        else: out.append(dict(t=t,x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2)))
    assert len(T)==len(B),(len(T),len(B))
    return out
def T(n): return [i*0.5 for i in range(n)]

# ---------- 48
t=T(31)
man=[(0,.52,1,1),(0,.46,.95,1)]+[OFF]*5+[(.28,.34,1,1),(.68,.79,1,1),(.3,.58,1,1),(.3,.78,.62,1),(.3,.6,.62,.9),(.05,.68,.4,.93)]+[OFF]*8+[(.15,.84,.45,1)]+[OFF]*9
bed=[OFF]*12+[(.15,.40,.55,.62),(.12,.44,.68,.70),(.6,.45,1,.78),OFF,OFF,(0,.45,.58,.86),(0,.52,.53,1),(0,.58,.48,1)]+[OFF]*11
sea=[OFF]*20+[(.15,.42,.65,.56),(.08,.44,.85,.57),(.15,.44,.85,.56),(.08,.45,.9,.6),(0,.45,1,.65),(0,.46,1,.68),(0,.45,1,.73),(0,.45,1,.71),(0,.42,1,.69),(0,.41,1,.68),(0,.42,1,.72)]
d=dict(mediaId=48,level="A",keyWord="arrive",defaultVoice="male",
 taps=[dict(phrase="to open the door",target="the man",voice="male",keys=keys(t,man)),
       dict(phrase="to have white sheets",target="the bed",voice="male",keys=keys(t,bed)),
       dict(phrase="to have small white waves",target="the sea",voice="male",keys=keys(t,sea))],
 stillS=15.0,
 nouns=[dict(word="the sky",x=0.50,y=0.20,voice="male"),
        dict(word="the sea",x=0.50,y=0.52,voice="male"),
        dict(word="sand",x=0.50,y=0.67,voice="male"),
        dict(word="trees",x=0.45,y=0.82,voice="male")],
 question="What is the man doing?",
 answer=["He","is","opening","the","door."],answerVoice="male",
 notes="POV clip with cuts. The man is seen only in parts: legs/arms 0-0.5 s, face 3.5 s, hand/arm at the door 4.0-6.0 s, hand 10.5 s; his box follows these parts. The bed and the sea are things, so their phrases are states. The sea is boxed from 10.0 s (through the balcony door); earlier tiny glimpses through the far window are left off. The bed is off at 8.0 s and 10.0 s (only a sliver). The answer describes 4.5-6.0 s. Key word 'arrive' is a verb, not placed.")
json.dump(d,open("content/48.json","w"),indent=1)

# ---------- 49
t=T(21)
full=(0,.05,1,1)
woman=[full]*6+[(0,.08,1,1),(0,.02,1,1),(0,0,1,1),(0,.2,.48,.8)]+[OFF]*5+[(0,.22,.57,1),(.08,.2,.76,1),(.17,.22,.78,1),(.17,.25,.80,1),(.12,.2,.66,1),(.18,.2,.66,1)]
target=[OFF]*9+[(.48,.14,.66,.30),(.41,.40,.59,.54),(.41,.40,.59,.54),(.32,.36,.75,.76),(.15,.27,1,1),(.15,.28,1,1),(.57,.28,1,1),(.76,.28,1,.9),(.78,.28,1,.88),(.80,.3,1,.93),(.66,.28,1,.95),(.66,.3,1,1)]
man=[OFF]*16+[(0,.27,.08,.95),(0,.25,.17,.80),(0,.27,.17,1),(0,.27,.12,.62),(0,.26,.17,.44)]
d=dict(mediaId=49,level="B",keyWord="arrow",defaultVoice="female",
 taps=[dict(phrase="to retrieve her arrow",target="the woman",voice="female",keys=keys(t,woman)),
       dict(phrase="to rest on a wooden stand",target="the target",voice="female",keys=keys(t,target)),
       dict(phrase="to stand behind the archer",target="the man",voice="male",keys=keys(t,man))],
 stillS=6.5,
 nouns=[dict(word="the sky",x=0.65,y=0.10,voice="female"),
        dict(word="an arrow",x=0.28,y=0.30,voice="female"),
        dict(word="a target",x=0.65,y=0.68,voice="female"),
        dict(word="grass",x=0.55,y=0.92,voice="female")],
 question="What has the arrow hit?",
 answer=["The","arrow","has","hit","the","middle","of","the","target."],answerVoice="female",
 notes="The arrow itself is not a tap target (it always overlaps the woman or the target). Woman and target overlap at 8.0-10.0 s (she reaches in front of it): split by a vertical line, the target keeps the strip to the right of her. The man is at the left edge 8.0-10.0 s; at 8.0 s his box is only 0.08 wide and at 10.0 s the woman's box starts at x 0.18, so her raised hand (x 0.08-0.18) lies in no box (his box holds only his face) - weak spot. Question in present perfect because the hit is the visible result (6.5 s).")
json.dump(d,open("content/49.json","w"),indent=1)

# ---------- 50
t=T(21)
hh=[.40]*6+[.43,.43,.38,.38,.36,.36,.32,.32,.43,.43,.38,.38,.36,.36,.30]
hand=[(.18,0,1,h) for h in hh]
jar=[(.17,.44,.84,.86)]*21
d=dict(mediaId=50,level="A",keyWord="jar",defaultVoice="female",
 taps=[dict(phrase="to hold the bag",target="the hand",voice="female",keys=keys(t,hand)),
       dict(phrase="to wear a black glove",target="the hand",voice="female",keys=keys(t,hand)),
       dict(phrase="to fill up with cream",target="the jar",voice="female",keys=keys(t,jar))],
 stillS=8.5,
 nouns=[dict(word="a glove",x=0.80,y=0.12,voice="female"),
        dict(word="a bag",x=0.52,y=0.27,voice="female"),
        dict(word="a jar",x=0.50,y=0.62,voice="female"),
        dict(word="a table",x=0.50,y=0.92,voice="female")],
 question="What is the hand doing?",
 answer=["It","is","filling","a","jar","with","cream."],answerVoice="female",
 notes="Only two separable targets: the gloved hand (with the top of the bag it holds) and the front jar; the bag cannot be boxed apart from the hand, so the hand has two phrases (one is a state). 'the jar' = the clear jar in front; the blurred jars at the back are already full and are not boxed. The front jar is swapped for an empty one at 3.0 s and 7.0 s but stays in the same place. No person shown, default voice by evenId.")
json.dump(d,open("content/50.json","w"),indent=1)

# ---------- 51
t=T(21)
hand=[OFF,OFF,OFF,(.27,.15,1,.95),(0,.27,1,1),(.1,.27,1,.95),(.12,.27,1,1),(.33,.07,1,.8),(.38,0,1,1),(.27,.23,1,1),(.26,.24,1,1),(.08,.25,1,1),(.3,.22,1,1),(.36,.21,1,1),(.24,.25,1,1),(.17,.32,1,1),(.1,.31,1,1),(.08,.23,1,.85),(.15,.34,1,1),(.08,.25,1,1),(.06,.29,1,.9)]
mug=[(.05,0,.43,.16),(.02,0,.38,.16),(0,.03,.35,.26),(0,.03,.27,.26),(0,0,.3,.14),(0,0,.25,.14),(0,.03,.3,.26),(.04,.06,.33,.33),(.05,.02,.38,.28),(.05,.02,.45,.23),(.05,.04,.44,.24),(.05,.03,.45,.25),(.05,.02,.45,.22),(.05,.02,.45,.21),(.07,.04,.47,.25),(.07,.03,.47,.29),(.05,0,.45,.24),(.05,0,.45,.23),(.05,.01,.47,.28),(.05,.01,.45,.25),(.03,0,.45,.24)]
d=dict(mediaId=51,level="B",keyWord="squeeze",defaultVoice="male",
 taps=[dict(phrase="to squeeze the slime",target="the hand",voice="male",keys=keys(t,hand)),
       dict(phrase="to grab a handful",target="the hand",voice="male",keys=keys(t,hand)),
       dict(phrase="to stand in the background",target="the mug",voice="male",keys=keys(t,mug))],
 stillS=6.0,
 nouns=[dict(word="a mug",x=0.25,y=0.12,voice="male"),
        dict(word="a thumb",x=0.42,y=0.30,voice="male"),
        dict(word="a wrist",x=0.75,y=0.72,voice="male"),
        dict(word="beads",x=0.25,y=0.86,voice="male")],
 question="What is the hand doing?",
 answer=["It","is","squeezing","a","handful","of","beads."],answerVoice="male",
 notes="The slime is not a tap target: the hand lies on / in it the whole time, so the two cannot be boxed apart. Targets are the hand (two phrases) and the dim mug in the background (a state; it is dark but recognisable, weak spot). The hand box follows hand + forearm and includes the slime it holds. Hand enters at 1.5 s. Only a hand is shown, default voice by evenId. 'beads' sits on the bead-filled slime ring on the table.")
json.dump(d,open("content/51.json","w"),indent=1)
