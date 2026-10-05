import json
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T19=[i*0.5 for i in range(19)]
T29=[i*0.5 for i in range(29)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 5358
W=[(.21,.05,.79,.58)]*4+[(.21,.05,.79,.59),(.21,.05,.79,.59),(.21,.06,.79,.61),(.23,.07,.66,.56),(.24,.09,.60,.49),(.27,.11,.61,.51),(.29,.31,.43,.38),(.30,.34,.40,.58),(.28,.72,.42,.14),(.28,.70,.42,.14),(.38,.15,.30,.80),(.38,.19,.30,.77),(.38,.24,.30,.63),(.38,.24,.30,.63),(.38,.24,.30,.72)]
L=[(0,.22,.21,.20)]*7+[(0,.23,.23,.20),(0,.23,.24,.20),(.03,.27,.24,.17),(.04,.28,.25,.18),(.06,.29,.24,.17)]+[None]*7
kw=K(T19,W); kl=K(T19,L)
save({"mediaId":5358,"level":"B","keyWord":"peek","defaultVoice":"female",
 "taps":[
  {"phrase":"to peek through a gap","target":"the woman in the cardigan","voice":"female","keys":kw},
  {"phrase":"to stack heavy books","target":"the woman in the cardigan","voice":"female","keys":kw},
  {"phrase":"to lean on her hand","target":"the woman on the left","voice":"female","keys":kl}],
 "stillS":2.0,
 "nouns":[{"word":"bookshelves","x":.50,"y":.07,"voice":"female"},{"word":"glasses","x":.50,"y":.30,"voice":"female"},
          {"word":"a cardigan","x":.50,"y":.44,"voice":"female"},{"word":"a textbook","x":.55,"y":.63,"voice":"female"}],
 "question":"What is the hidden woman doing?",
 "answer":["She","is","peeking","through","a","gap","between","the","books."],
 "answerVoice":"female",
 "notes":"Main woman's box is cut at the left (x>=0.21..0.30) while the woman on the left is visible, so her left elbow is outside the box at 0-5 s. At 6.0-6.5 s only her feet under the table are visible (boxed); from 7.0 s the box spans face in the gap down to the feet. Woman on the left is small and hidden from 6.0 s. A blonde student on the right also sits in the background."})

# 7
M=[(0,.16,1,.84),(0,.16,1,.84),(0,.17,1,.83),(0,.16,1,.84),(0,.15,1,.85),(0,.15,1,.85),(0,.16,1,.84),(0,.16,1,.84),(0,.20,1,.80),(0,.07,1,.93),(0,0,1,1),(0,.07,1,.93)]+[(0,0,1,1)]*7+[(0,.27,1,.73),(0,.23,.90,.77),(0,.18,1,.82),(0,.21,1,.79),(0,.17,1,.83),(0,.10,1,.90),(0,.08,1,.92),(0,.02,1,.98),(0,.13,1,.87),(0,.10,1,.90)]
km=K(T29,M)
save({"mediaId":7,"level":"B","keyWord":"graduation","defaultVoice":"male",
 "taps":[
  {"phrase":"to raise his diploma","target":"the man","voice":"male","keys":km},
  {"phrase":"to grin at the camera","target":"the man","voice":"male","keys":km},
  {"phrase":"to hug another graduate","target":"the man","voice":"male","keys":km}],
 "stillS":4.5,
 "nouns":[{"word":"a diploma","x":.76,"y":.24,"voice":"male"},{"word":"a stadium","x":.24,"y":.28,"voice":"male"},
          {"word":"a graduation cap","x":.36,"y":.43,"voice":"male"},{"word":"a sash","x":.26,"y":.87,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","raising","his","diploma","at","his","graduation."],
 "answerVoice":"male",
 "notes":"Only one clear target (the graduate in front); the other graduates are small and blurred, so all three phrases are his. The hug (12-14 s) shows the other graduate only as a shoulder/cap. Key word 'graduation' is abstract, so the noun is 'a graduation cap'; 'a stadium' sits on the stands in the background."})

# 4360
G=[(.08,.15,.86,.85),(.10,.19,.88,.81),(.05,.20,.90,.80),(0,.20,.93,.80),(0,.18,.92,.82),(0,.16,.94,.84),(0,.21,1,.79),(0,.22,1,.78),(0,.21,1,.79),(0,.20,1,.80),(0,.20,1,.80),(.10,.28,.80,.66),(.10,.27,.82,.67),(.10,.28,.83,.70),(.08,.28,.86,.72),(.04,.28,.88,.72),(.02,.27,.92,.73),(0,.26,.96,.74),(0,.26,.96,.74)]
kg=K(T19,G)
save({"mediaId":4360,"level":"B","keyWord":"purse","defaultVoice":"female",
 "taps":[
  {"phrase":"to peer into a bag","target":"the woman","voice":"female","keys":kg},
  {"phrase":"to carry several shopping bags","target":"the woman","voice":"female","keys":kg},
  {"phrase":"to show off her purse","target":"the woman","voice":"female","keys":kg}],
 "stillS":8.0,
 "nouns":[{"word":"paper bags","x":.22,"y":.43,"voice":"female"},{"word":"a purse","x":.66,"y":.48,"voice":"female"},
          {"word":"a holdall","x":.70,"y":.72,"voice":"female"},{"word":"an escalator","x":.45,"y":.93,"voice":"female"}],
 "question":"What is the woman showing off?",
 "answer":["She","is","showing","off","her","purse","on","an","escalator."],
 "answerVoice":"female",
 "notes":"One target only (passers-by in the mall are tiny and all just walk). Box includes the bags she carries. 'purse' = the brown patterned handbag (US sense); 'a holdall' = the big black bag (British word; 'a duffel bag' would be the US one). 'paper bags' pill sits on the white/brown paper bags at her right arm; a cloth tote hangs below them."})

# 5379
Tl=[(0,.26,.52,.74),(0,.26,.51,.74),(0,.27,.50,.73),(0,.26,.52,.74),(0,.27,.52,.73),(.15,0,.85,.70),(0,0,1,.68),(.15,0,.85,.72),(.38,.03,.62,.56),(0,0,1,.72),(0,.08,1,.92),(0,.08,1,.92),(0,.26,.47,.74),(0,.26,.25,.31),(0,.27,.43,.73),(0,.27,.42,.73),(0,.28,.42,.72),(0,.28,.42,.72),(0,.30,.42,.70)]
Y=[(.52,.11,.46,.89),(.51,.11,.47,.89),(.50,.11,.46,.89),(.52,.11,.46,.89),(.52,.11,.44,.89)]+[None]*7+[(.47,.11,.53,.89),(.25,.09,.75,.91),(.43,.11,.57,.89),(.42,.08,.58,.92),(.42,.08,.58,.92),(.42,.10,.58,.90),(.42,.14,.58,.86)]
kt=K(T19,Tl); ky=K(T19,Y)
save({"mediaId":5379,"level":"B","keyWord":"alter","defaultVoice":"male",
 "taps":[
  {"phrase":"to take a customer's measurements","target":"the tailor","voice":"male","keys":kt},
  {"phrase":"to mark fabric with chalk","target":"the tailor","voice":"male","keys":kt},
  {"phrase":"to slip on a jacket","target":"the man in the jacket","voice":"male","keys":ky}],
 "stillS":0.0,
 "nouns":[{"word":"a ceiling fan","x":.28,"y":.08,"voice":"male"},{"word":"fabric","x":.85,"y":.13,"voice":"male"},
          {"word":"a jacket","x":.70,"y":.55,"voice":"male"},{"word":"a tape measure","x":.30,"y":.78,"voice":"male"}],
 "question":"What is the tailor doing?",
 "answer":["He","is","altering","a","jacket","for","a","customer."],
 "answerVoice":"male",
 "notes":"2.5-5.5 s are close-ups: only the tailor's hands/arms are visible (boxed as the tailor; at 5.0-5.5 s the box also covers the sewing machine, which is not a target). The young man is off in those shots. At 6.5 s the young man fills most of the frame and the tailor is a small box top-left. The tailor's reaching arm crosses into the young man's box at 0-2 s (split at the young man's back)."})
