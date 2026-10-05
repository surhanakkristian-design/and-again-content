import json, sys
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst):
    out=[]
    for t,b in zip(T,lst):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def tap(p,tg,v,b): return {"phrase":p,"target":tg,"voice":v,"keys":K(b)}
def N(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
C={}
# 5561
wom=[(0,.16,.93,.84),(0,.08,.97,.92),(0,.10,.86,.90),(0,.08,.88,.92),(0,.05,.65,.95),(0,.10,.62,.88),(0,.14,.62,.86),(0,.20,.73,.80)]
man=[None,None,None,None,(.82,.22,.18,.58),(.78,.15,.22,.65),(.74,.20,.26,.70),(.74,.23,.26,.65)]
C[5561]=dict(mediaId=5561,level="A",keyWord="appropriate",defaultVoice="female",
 taps=[tap("to tie her boot","the woman","female",wom),tap("to bend over the boots","the woman","female",wom),tap("to kneel on the floor","the man","male",man)],
 stillS=3.7,nouns=[N("a woman",.25,.45,"female"),N("a man",.88,.50,"male"),N("a window",.78,.17,"female"),N("boots",.85,.88,"female")],
 question="What is the woman doing?",answer=["She","is","tying","her","boot."],answerVoice="female",
 notes="Shop assistant only shows as an arm/knee sliver at the right edge 0.2-1.7, set off there. Woman box at 0.2/0.7 reaches the right edge region of loose boots on the floor. Customers in the back are small and not used.")
# 5562
navy=[(.04,.31,.27,.19),(.04,.31,.27,.19),(.04,.31,.27,.19),(.04,.31,.27,.19),(.03,.31,.27,.18),(.04,.30,.19,.30),(.01,.29,.20,.33),(.01,.29,.20,.35)]
cream=[(.17,.50,.40,.47),(.17,.50,.40,.47),(.16,.50,.40,.50),(.17,.50,.40,.50),(.19,.49,.38,.51),(.24,.41,.37,.59),(.22,.34,.36,.66),(.22,.31,.36,.69)]
blue=[(.59,.33,.27,.29),(.59,.33,.27,.29),(.59,.33,.27,.29),(.59,.33,.29,.29),(.60,.33,.27,.29),(.62,.33,.25,.29),(.62,.33,.26,.30),(.62,.32,.27,.31)]
C[5562]=dict(mediaId=5562,level="B",keyWord="approval",defaultVoice="female",
 taps=[tap("to hold a presentation clicker","the woman in navy","female",navy),tap("to applaud with raised arms","the man in blue","male",blue),tap("to rise from her chair","the woman in cream","female",cream)],
 stillS=1.2,nouns=[N("ferns",.48,.28,"female"),N("skyscrapers",.86,.40,"female"),N("a notebook",.56,.72,"female"),N("an office chair",.16,.82,"female")],
 question="What is the woman in cream doing?",answer=["She","is","rising","from","her","chair."],answerVoice="female",
 notes="Woman in navy stands behind the woman in cream: her box is cut at the cream woman's head (y .50 for 0.2-2.2), so her lower blazer/skirt is outside the box. Woman in cream also claps (as does the man in white, not used); she rises from 2.7. The clicker is small in her right hand.")
# 5563
m=[(0,.65,1,.35),(0,.60,1,.40),(0,.66,.66,.34),(0,.68,.66,.32),(0,.68,.66,.32),(0,.68,.66,.32),(0,.70,.66,.30),(0,.70,1,.30)]
w=[(.35,.27,.32,.31),(.34,.26,.33,.32),(.35,.25,.32,.33),(.35,.24,.31,.27),(.35,.23,.31,.25),(.35,.24,.32,.24),(.34,.23,.32,.25),(.34,.22,.32,.26)]
cat=[(0,.43,.30,.22),(0,.42,.30,.18),(0,.43,.31,.22),(0,.51,.42,.17),(0,.48,.58,.19),(0,.48,.68,.19),(0,.48,.68,.20),(0,.48,.77,.21)]
C[5563]=dict(mediaId=5563,level="B",keyWord="approve",defaultVoice="female",
 taps=[tap("to stamp a document","the man","male",m),tap("to clasp her hands together","the woman","female",w),tap("to stretch across the desk","the cat","female",cat)],
 stillS=1.2,nouns=[N("a brass lantern",.43,.10,"female"),N("a tabby cat",.14,.54,"female"),N("a document",.70,.73,"female"),N("a glass of tea",.94,.65,"female")],
 question="What is the cat doing?",answer=["It","is","stretching","across","the","desk."],answerVoice="female",
 notes="POV shot: 'the man' is only his arms on the desk; the raised stamp hand at 0.7 (x .75-1.0, y .41-.60) is outside his box because a single box would overlap the woman; at 3.7 the stamp hand top is cut. Cat box cut at the woman's waist line 1.7-3.7 (the raised tail at x .02-.12 above it not covered). Cat stretches from 1.7 on; sits at 0.2-1.2.")
# 5564
wo=[(.16,.39,.43,.58),(.16,.38,.44,.59),(.16,.35,.43,.63),(.17,.34,.42,.64),(.20,.36,.41,.64),(.10,.38,.51,.62),(.10,.40,.51,.60),(.11,.42,.50,.58)]
wk=[(.60,.59,.38,.23),(.60,.59,.39,.22),(.60,.58,.39,.25),(.60,.59,.39,.22),(.61,.61,.38,.26),(.62,.63,.37,.26),(.62,.64,.37,.26),(.62,.66,.37,.26)]
sk=[(.07,.03,.33,.16),(.07,.04,.33,.15),(.07,.05,.33,.15),(.08,.06,.32,.16),(.09,.09,.32,.16),(.09,.11,.33,.16),(.10,.13,.32,.16),(.10,.15,.32,.16)]
C[5564]=dict(mediaId=5564,level="B",keyWord="architecture",defaultVoice="female",
 taps=[tap("to hold up a blueprint","the woman","female",wo),tap("to use a spirit level","the worker","male",wk),tap("to let in the sunlight","the skylight","female",sk)],
 stillS=0.7,nouns=[N("a skylight",.24,.12,"female"),N("trees",.14,.40,"female"),N("a blueprint",.50,.52,"female"),N("a spirit level",.86,.79,"female")],
 question="What is the woman holding up?",answer=["She","is","holding","up","a","blueprint."],answerVoice="female",
 notes="The drawing is a white sheet with a pencil drawing of an arch, called 'a blueprint' (plan) - verifier may prefer 'a drawing'. Woman and worker boxes split at x ~.60 (the drawing's right edge / the worker's foot are close).")
for i in (sys.argv[1:] or C):
    json.dump(C[int(i)],open(f'content/{i}.json','w'),indent=1)
