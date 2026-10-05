import json
def K(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(times,boxes): 
    assert len(times)==len(boxes),(len(times),len(boxes))
    return [K(t,b) for t,b in zip(times,boxes)]
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4178
t=T(24)
hen=[(0,.15,.75,.60),(0,.17,.74,.58),(0,.20,.79,.58),(0,.23,.56,.50),(0,.18,.62,.50),(0,.20,.66,.56),(0,.15,.90,.72),(0,.06,.92,.76),None,
 (.27,.24,.65,.47),(.24,.27,.65,.43),(.19,.24,.70,.50),(.10,.26,.80,.38),(.03,.18,.86,.44),(0,.13,.95,.46),(0,.13,.95,.46),(0,.10,.95,.49),
 (.03,.10,.83,.46),(.08,.14,.75,.38),(.08,.14,.75,.38),(.08,.14,.75,.38),(.08,.14,.75,.38),(.08,.14,.75,.38),(.08,.14,.75,.38)]
mouse=[None]*12+[(.17,.66,.46,.22),(.25,.62,.38,.16),(.28,.59,.32,.20),(.28,.59,.32,.20),(.29,.59,.30,.16),(.33,.56,.26,.14),
 (.36,.52,.24,.14),None,(.36,.52,.24,.14),(.36,.52,.24,.14),(.36,.52,.24,.14),(.36,.52,.24,.14)]
candle=[None]*9+[(.05,.52,.20,.20),(.04,.50,.19,.18),(0,.48,.18,.22),None,None,None,None,None,(.87,.47,.13,.20)]+[(.84,.40,.16,.22)]*6
save({"mediaId":4178,"level":"B","keyWord":"generous","defaultVoice":"female",
 "taps":[
  {"phrase":"to peer into the burrow","target":"the hen","voice":"female","keys":keys(t,hen)},
  {"phrase":"to stand beneath the hen","target":"the grey mouse","voice":"female","keys":keys(t,mouse)},
  {"phrase":"to glow in the darkness","target":"the candle","voice":"female","keys":keys(t,candle)}],
 "stillS":10.5,
 "nouns":[{"word":"a hen","x":.50,"y":.30,"voice":"female"},{"word":"a candle","x":.88,"y":.50,"voice":"female"},{"word":"corn","x":.52,"y":.78,"voice":"female"}],
 "question":"What is the hen doing?",
 "answer":["She","is","sharing","her","corn","with","the","mice."],
 "answerVoice":"female",
 "notes":"Key word 'generous' is an adjective, not a visible noun; the answer shows it through 'sharing her corn'. Grey mouse is small and dim from 9.0 s on and hidden behind the hen's head at 9.5 s (off). The pink mice at the bottom also stand lower than the hen, but only the grey one stands directly beneath her at the mouth of the hole. Candle is off at 6.0-8.0 s (out of frame)."})

# ---------- 4179
t=T(25)
save({"mediaId":4179,"level":"A","keyWord":"birthday","defaultVoice":"female",
 "taps":[
  {"phrase":"to blow out the candles","target":"the woman","voice":"female","keys":keys(t,[(.02,.10,.96,.38)]*25)},
  {"phrase":"to hang on the wall","target":"the banner","voice":"female","keys":keys(t,[(0,0,1,.10)]*25)},
  {"phrase":"to have three candles","target":"the cake","voice":"female","keys":keys(t,[(0,.48,1,.46)]*25)}],
 "stillS":12.0,
 "nouns":[{"word":"sunglasses","x":.50,"y":.29,"voice":"female"},{"word":"a shirt","x":.28,"y":.45,"voice":"female"},
          {"word":"candles","x":.50,"y":.61,"voice":"female"},{"word":"a cake","x":.50,"y":.80,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","blowing","out","her","birthday","candles."],
 "answerVoice":"female",
 "notes":"Static shot, so the three boxes are constant bands: banner 0-0.10, woman 0.10-0.48, cake with candles 0.48-0.94. The tiara tip reaches into the banner band. At 0.0 s the banner is half hidden by hands and the tiara. 'to have three candles' is a state (the cake does nothing). She blows the candles out between 5.5 and 8.0 s."})

# ---------- 4180
t=T(24)
W=[(.58,.15,.32,.56),(.60,.16,.36,.56),(.60,.16,.32,.56),(.62,.16,.34,.57),(.60,.16,.33,.56),(.60,.16,.24,.56),(.57,.16,.35,.56),(.66,.15,.34,.58),(.66,.15,.34,.62),
   (.60,.15,.40,.44),(.62,.16,.38,.42),(.62,.16,.38,.43),(.62,.16,.38,.43),(.62,.16,.38,.42),(.62,.16,.38,.42),(.62,.16,.38,.42),(.62,.13,.38,.45),(.60,.12,.40,.46),
   (.55,.12,.45,.50),(.55,.13,.45,.49),(.50,.12,.50,.50),(.50,.12,.50,.50),(.50,.11,.50,.51),(.50,.10,.50,.52)]
A=[(.22,.51,.36,.32),(.20,.50,.40,.33),(.18,.52,.42,.32),(.20,.52,.42,.35),(.16,.50,.44,.33),(.20,.50,.40,.34),(.20,.55,.37,.30),(.18,.56,.48,.31),(.26,.58,.40,.35),
   (.30,.59,.50,.36),(.38,.58,.42,.40),(.39,.59,.42,.41),(.40,.59,.47,.41),(.40,.58,.44,.42),(.40,.58,.42,.42),(.40,.58,.42,.42),(.42,.58,.42,.42),(.42,.58,.42,.42),
   (.18,.70,.60,.30),(.18,.69,.60,.31),(.10,.66,.60,.34),(.10,.66,.60,.34),(.05,.66,.60,.34),(.10,.66,.58,.34)]
M=[None]*5+[(.84,.17,.16,.42),(.39,.20,.18,.35),(.22,.18,.33,.38),(.08,.15,.36,.43),(.05,.13,.40,.46),(0,.12,.38,.63),(.03,.11,.36,.65),(.03,.10,.37,.63),
   (.04,.10,.36,.64),(.04,.11,.36,.60),(.04,.12,.36,.59),(.08,.12,.34,.58),(.06,.12,.36,.59),(.04,.14,.38,.55),(.04,.14,.38,.54),(.04,.14,.36,.50),(.04,.14,.36,.50),
   (.04,.15,.34,.49),(.04,.15,.34,.48)]
save({"mediaId":4180,"level":"B","keyWord":"mistake","defaultVoice":"female",
 "taps":[
  {"phrase":"to grip a red leash","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to cradle a puppy","target":"the man","voice":"male","keys":keys(t,M)},
  {"phrase":"to crawl along the pavement","target":"the alligator","voice":"female","keys":keys(t,A)}],
 "stillS":6.5,
 "nouns":[{"word":"a woman","x":.82,"y":.40,"voice":"female"},{"word":"a puppy","x":.27,"y":.36,"voice":"female"},{"word":"a leash","x":.69,"y":.57,"voice":"female"},{"word":"an alligator","x":.55,"y":.87,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","walking","an","alligator","on","a","leash."],
 "answerVoice":"female",
 "notes":"Key word 'mistake' (verb: she mistakes the alligator for her dog) is only clear with the sound, so the answer stays with what the picture shows. The woman and the alligator overlap in the picture: up to 4.0 s the boxes are split by a vertical line (woman right, alligator left), from 4.5 s by a horizontal line (woman's upper body above, alligator below), so her lower legs fall outside her box there. The man's box includes the puppy he carries. The 'a leash' pill sits on the leash in front of the woman's legs, 'a woman' on her shirt 0.17 higher."})

# ---------- 4181
t=T(25)
W=[(.15,.06,.75,.45),(.20,.03,.76,.46),(.20,.02,.72,.45),(.20,.01,.78,.45),(.20,0,.78,.46),(.20,0,.72,.46),(.15,0,.78,.45),(.17,0,.76,.45),(.15,0,.80,.41),
   (.18,.03,.76,.34),(.23,.04,.63,.33),(.27,.06,.58,.32),(.28,.06,.50,.32),(.28,.06,.44,.34),(.28,.06,.42,.36),(.27,.05,.43,.38),(.27,.05,.48,.36),(.20,.05,.56,.39),
   (.17,.04,.60,.40),(.08,.02,.80,.38),(.05,.02,.90,.35),(.05,.02,.95,.31),(0,.02,.47,.75),(0,.02,.50,.80),(0,.05,.50,.72)]
C=[(.02,.51,.94,.42),(.08,.49,.92,.46),(.08,.47,.92,.48),(.08,.46,.92,.50),(.05,.46,.95,.46),(.03,.46,.97,.46),(0,.45,.97,.49),(.08,.45,.90,.50),(0,.41,.97,.53),
   (.04,.37,.92,.48),(.04,.37,.90,.44),(.10,.38,.88,.44),(.03,.38,.88,.46),(.05,.40,.87,.45),(.08,.42,.90,.48),(.05,.43,.92,.49),(.02,.41,.92,.49),(0,.44,.90,.49),
   (0,.44,.92,.48),(.02,.40,.90,.48),(.03,.37,.92,.47),(.10,.33,.90,.48),(.47,.30,.53,.60),(.50,.37,.50,.61),(.50,.38,.50,.50)]
save({"mediaId":4181,"level":"A","keyWord":"offer","defaultVoice":"female",
 "taps":[
  {"phrase":"to ride a red scooter","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to reach for the cake","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to stand on a white plate","target":"the cake","voice":"female","keys":keys(t,C)}],
 "stillS":8.0,
 "nouns":[{"word":"a woman","x":.48,"y":.18,"voice":"female"},{"word":"candles","x":.50,"y":.50,"voice":"female"},
          {"word":"a cake","x":.50,"y":.64,"voice":"female"},{"word":"a plate","x":.50,"y":.84,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","reaching","for","the","cake."],
 "answerVoice":"female",
 "notes":"Only two targets (woman on her scooter, cake on its plate); the hands that hold the plate and set the candles belong to nobody visible. The cake phrase is a state. The cake is in front of the woman, so the boxes are split along the top of the candles / cake (horizontal line up to 10.5 s, vertical line from 11.0 s when she is beside it); her hands on the handlebar or plate fall into the cake box in some frames. She reaches for the cake from 8.5 s. Key word 'offer' (the cake is held out to her) is not in the answer because the person offering is not shown."})
