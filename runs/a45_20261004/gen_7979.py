from gen_7977_7978_7979_7980_lib import *
gw = keys([(.07,.50,.75,.50),(.02,.51,.70,.49),(.02,.50,.44,.48),None,(0,.50,.25,.33),(0,.50,.28,.29),(0,.51,.28,.26),(.03,.52,.30,.25)])
cw = keys([None,None,None,(0,.35,.66,.65),(.26,.38,.53,.62),(.38,.40,.50,.60),(.46,.43,.37,.57),(.48,.45,.32,.55)])
mc = keys([None,None,None,None,None,None,(.84,.35,.16,.63),(.80,.38,.20,.53)])
write(7979, {"mediaId": 7979, "level": "B", "keyWord": "set back", "defaultVoice": "female",
 "taps": [
  {"phrase": "to lean against the tarpaulin", "target": "the woman in the rain jacket", "voice": "female", "keys": gw},
  {"phrase": "to giggle behind her glove", "target": "the woman in white", "voice": "female", "keys": cw},
  {"phrase": "to lift his helmet overhead", "target": "the man in white", "voice": "male", "keys": mc}],
 "stillS": 3.2,
 "nouns": [{"word": "a storm cloud", "x": .30, "y": .20, "voice": "female"}, {"word": "a pavilion", "x": .62, "y": .40, "voice": "female"},
           {"word": "a helmet", "x": .76, "y": .72, "voice": "female"}, {"word": "a boundary rope", "x": .44, "y": .92, "voice": "female"}],
 "question": "What is the woman in white doing?",
 "answer": ["She", "is", "giggling", "behind", "her", "glove."],
 "answerVoice": "female",
 "notes": "Several ground staff pull the cover, so only the blonde woman in the navy rain jacket is a target: she leans back into the cover with her whole body while the men bend forward (weakest phrase, check). She is hidden behind the cricketer at 1.7 (off). The female cricketer is only a glove + helmet at the bottom left at 1.2 (off). The male cricketer appears only at 3.2-3.7 at the right edge (shoe/arm at 2.2/2.7 marked off); at 3.7 his box and hers are split at x 0.80. Still 3.2: the man at the right also holds a helmet above his head; the 'a helmet' pill sits on the woman's helmet. Key word 'set back' is not a noun."})
