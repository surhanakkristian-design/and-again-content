import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/'
def K(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
def tap(p,t,v,k): return {"phrase":p,"target":t,"voice":v,"keys":k}
def write(d):
    json.dump(d,open(R+f"{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 6846
woman=K([(0.2,.08,.12,.57,.88),(0.7,.08,.12,.57,.88),(1.2,.06,.12,.59,.88),(1.7,.08,.12,.57,.88),(2.2,.04,.10,.61,.90)])
man=K([(0.2,.66,.34,.33,.16),(0.7,.66,.34,.33,.16),(1.2,.66,.35,.33,.16),(1.7,.66,.33,.33,.17),(2.2,.66,.31,.33,.18)])
write({"mediaId":6846,"level":"B","keyWord":"attorney","defaultVoice":"female",
 "taps":[tap("to hold out a contract","the woman","female",woman),
         tap("to wear a trouser suit","the woman","female",woman),
         tap("to stir on the sofa","the man","male",man)],
 "stillS":0.2,
 "nouns":[{"word":"an attorney","x":.45,"y":.32,"voice":"female"},
          {"word":"a curtain","x":.21,"y":.20,"voice":"female"},
          {"word":"a contract","x":.40,"y":.62,"voice":"female"},
          {"word":"banknotes","x":.72,"y":.90,"voice":"female"}],
 "question":"What is the attorney doing?",
 "answer":["The","attorney","is","offering","a","thick","contract."],
 "answerVoice":"female",
 "notes":"Curtain not used as a target: its box would overlap the woman's (she fills the frame). Woman box cut at x 0.65 so it does not overlap the man on the sofa; the right edge of the contract (coloured tabs) lies outside her box. The man is small and partly hidden behind a briefcase; he lies at first, sits up at 1.7-2.2."})

# 6847
mag=K([(0.2,.00,.00,.92,.62),(0.7,.00,.00,.98,.39),(1.2,.00,.00,.78,.44),(1.7,.00,.00,.74,.44),(2.2,.00,.00,.70,.45),(2.7,.00,.00,.68,.45),(3.2,.00,.00,.68,.46),(3.7,.00,.00,.68,.47)])
wom=K([(0.2,None,0,0,0),(0.7,.68,.40,.32,.56),(1.2,.40,.46,.31,.49),(1.7,.23,.47,.35,.48),(2.2,.29,.48,.27,.44),(2.7,.31,.48,.27,.42),(3.2,.29,.49,.25,.46),(3.7,.31,.49,.25,.46)])
drv=K([(0.2,None,0,0,0),(0.7,None,0,0,0),(1.2,None,0,0,0),(1.7,.80,.48,.20,.15),(2.2,.80,.48,.19,.15),(2.7,.80,.48,.19,.15),(3.2,.79,.48,.20,.15),(3.7,.79,.49,.20,.15)])
write({"mediaId":6847,"level":"B","keyWord":"attraction","defaultVoice":"male",
 "taps":[tap("to hang from rusty chains","the magnet","male",mag),
         tap("to have long silver hair","the woman","female",wom),
         tap("to sit in the cab","the driver","male",drv)],
 "stillS":2.2,
 "nouns":[{"word":"a magnet","x":.25,"y":.25,"voice":"male"},
          {"word":"a digger","x":.82,"y":.42,"voice":"male"},
          {"word":"scrap metal","x":.12,"y":.63,"voice":"male"},
          {"word":"mud","x":.55,"y":.92,"voice":"male"}],
 "question":"What is the huge magnet doing?",
 "answer":["The","magnet","is","attracting","two","metal","sheets."],
 "answerVoice":"male",
 "notes":"The woman and man do the same actions (hold sheets, laugh, lean back), so the woman is picked out by a state (silver hair). The driver is small in the digger cab (from 1.7); his box overlaps the man, who is not a target. At 0.2 only an edge of a person shows at the right: off. defaultVoice male: mixed pair, evenId false."})

# 6848
wm=K([(0.2,.40,.46,.41,.54),(0.7,.33,.43,.54,.57),(1.2,.23,.41,.77,.59),(1.7,.26,.41,.74,.59),(2.2,.25,.40,.68,.60),(2.7,.23,.40,.74,.60),(3.2,.21,.40,.76,.60),(3.7,.19,.40,.79,.60)])
lg=K([(0.2,.17,.40,.23,.45),(0.7,.14,.39,.19,.55),(1.2,.10,.37,.13,.58),(1.7,.03,.32,.23,.64),(2.2,.05,.38,.20,.60),(2.7,.03,.37,.20,.61),(3.2,.02,.37,.19,.63),(3.7,.01,.37,.18,.63)])
write({"mediaId":6848,"level":"B","keyWord":"authority","defaultVoice":"female",
 "taps":[tap("to shout through a megaphone","the woman","female",wm),
         tap("to wear a navy uniform","the woman","female",wm),
         tap("to carry a red flag","the shirtless lifeguard","male",lg)],
 "stillS":2.2,
 "nouns":[{"word":"an umbrella","x":.26,"y":.27,"voice":"female"},
          {"word":"a flag","x":.17,"y":.44,"voice":"female"},
          {"word":"a megaphone","x":.40,"y":.66,"voice":"female"},
          {"word":"a lifeguard tower","x":.77,"y":.36,"voice":"female"}],
 "question":"What is the woman in uniform doing?",
 "answer":["She","is","shouting","through","a","megaphone."],
 "answerVoice":"female",
 "notes":"The woman fills most of the frame, so the lifeguard box is split from hers by a vertical line (at 0.2 split at x 0.40 so his head stays in his box; lifeguard box narrow, the megaphone's left tip at 0.2 falls outside her box). The blowing umbrella was not used as a target: from 3.2 it is behind the woman's head and the police officer. Police officers also wear uniforms, but light blue shirts, not a navy one; the lifeguard in the red cap is a second lifeguard, hence 'shirtless'."})

# 6850
mn=K([(0.2,.25,.35,.52,.40),(0.7,.25,.35,.52,.40),(1.2,.23,.36,.54,.40),(1.7,.21,.35,.58,.42),(2.2,.19,.31,.61,.44),(2.7,.17,.29,.66,.45),(3.2,.17,.28,.67,.48),(3.7,.17,.27,.69,.48)])
cp=K([(0.2,0,.16,.95,.19),(0.7,0,.16,.95,.19),(1.2,0,.17,.95,.19),(1.7,0,.16,.95,.19),(2.2,0,.14,.95,.17),(2.7,0,.14,.95,.15),(3.2,0,.14,.95,.14),(3.7,0,.14,.95,.13)])
write({"mediaId":6850,"level":"B","keyWord":"bachelor","defaultVoice":"male",
 "taps":[tap("to tuck into his cake","the man","male",mn),
         tap("to wave at the camera","the man","male",mn),
         tap("to dance close together","the couples","male",cp)],
 "stillS":0.2,
 "nouns":[{"word":"a bachelor","x":.45,"y":.52,"voice":"male"},
          {"word":"fairy lights","x":.15,"y":.12,"voice":"male"},
          {"word":"a handbag","x":.86,"y":.56,"voice":"male"},
          {"word":"a slice of cake","x":.63,"y":.79,"voice":"male"}],
 "question":"What is the bachelor doing?",
 "answer":["He","is","tucking","into","a","slice","of","cake."],
 "answerVoice":"male",
 "notes":"Couples box = the dance floor band above the man's head (split horizontally at his head top); dancers left/right of him below that line fall outside. The wave is short (about 2.5-3.2 s). Voice of the couples phrase = defaultVoice male."})
