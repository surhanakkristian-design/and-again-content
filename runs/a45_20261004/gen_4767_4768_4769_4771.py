import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OFF = None
def keys(times, boxes):
    out = []
    for t in times:
        b = boxes.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c): json.dump(c, open(f'{HERE}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 4767
t = T(19)
g = {0.0:(0,.15,.62,.85),0.5:(0,.16,.62,.84),1.0:(0,.16,.6,.84),1.5:(0,.16,.62,.84),2.0:(0,.15,.6,.85),2.5:(0,.16,.68,.84),
     3.0:(0,.15,.66,.85),3.5:(.03,.18,.6,.82),4.0:(.02,.19,.62,.81),4.5:(.05,.12,.66,.88),5.0:(0,.1,.63,.9),5.5:(0,.06,.74,.94),
     6.0:(0,.03,.7,.85),6.5:(0,.04,.62,.84),7.0:(0,.06,.46,.9),7.5:(0,.19,.7,.81),8.0:(0,.21,.84,.79),8.5:(0,.23,.86,.77),9.0:(0,.24,.84,.76)}
k = keys(t, g)
save({"mediaId": 4767, "level": "A", "keyWord": "gardener", "defaultVoice": "female",
 "taps": [{"phrase": "to cut a bush", "target": "the gardener", "voice": "female", "keys": k},
          {"phrase": "to water the flowers", "target": "the gardener", "voice": "female", "keys": k},
          {"phrase": "to wear a blue apron", "target": "the gardener", "voice": "female", "keys": k}],
 "stillS": 6.0,
 "nouns": [{"word": "a gardener", "x": 0.17, "y": 0.30, "voice": "female"},
           {"word": "a watering can", "x": 0.36, "y": 0.48, "voice": "female"},
           {"word": "flowers", "x": 0.62, "y": 0.78, "voice": "female"},
           {"word": "trees", "x": 0.62, "y": 0.08, "voice": "female"}],
 "question": "What is the gardener doing?",
 "answer": ["She", "is", "watering", "the", "flowers."], "answerVoice": "female",
 "notes": "Only one real target (the gardener); the people in the background are tiny. All three phrases use her. The answer names the second action (watering); she also cuts bushes earlier."})

# ---------- 4768
t = T(19)
pw = {0.0:(.1,.15,.9,.85),0.5:(0,.05,1,.95),1.0:(0,.05,1,.95),1.5:(0,.05,1,.95),
      6.5:(.76,.25,.24,.5),7.0:(.64,.29,.3,.3),7.5:(.6,.3,.18,.24),8.0:(.6,.3,.18,.2),8.5:(.6,.3,.18,.2),9.0:(.6,.31,.18,.2)}
cm = {2.0:(0,.03,.93,.97),2.5:(.03,.05,.97,.95),3.0:(.05,.1,.92,.9),
      7.0:(.02,.29,.3,.3),7.5:(.18,.28,.2,.24),8.0:(.22,.28,.18,.2),8.5:(.23,.28,.18,.2),9.0:(.23,.31,.18,.2)}
lw = {5.0:(0,.1,1,.9),5.5:(0,.12,1,.88),6.0:(0,.15,1,.85),
      6.5:(.3,.26,.4,.42),7.0:(.36,.31,.26,.2),7.5:(.4,.31,.19,.2),8.0:(.41,.3,.18,.2),8.5:(.42,.3,.17,.2),9.0:(.41,.31,.18,.2)}
save({"mediaId": 4768, "level": "A", "keyWord": "card", "defaultVoice": "female",
 "taps": [{"phrase": "to hold a present", "target": "the woman with the present", "voice": "female", "keys": keys(t, pw)},
          {"phrase": "to hold two cards", "target": "the man with the cards", "voice": "male", "keys": keys(t, cm)},
          {"phrase": "to look up and laugh", "target": "the laughing woman", "voice": "female", "keys": keys(t, lw)}],
 "stillS": 3.0,
 "nouns": [{"word": "cards", "x": 0.60, "y": 0.58, "voice": "female"},
           {"word": "a man", "x": 0.35, "y": 0.44, "voice": "male"},
           {"word": "a box", "x": 0.72, "y": 0.92, "voice": "female"},
           {"word": "a window", "x": 0.80, "y": 0.24, "voice": "female"}],
 "question": "What is the man in brown holding?",
 "answer": ["He", "is", "holding", "two", "red", "cards."], "answerVoice": "male",
 "notes": "Clip of cuts. The man in glasses (3.5-4.5 s) is not a target. In the group shots (6.5-9.0 s) the three targets are small and sit close together; boxes there are tight and identity rests on clothes/position (striped sweater + present, brown T-shirt, woman in the middle). Card man is cut off at 6.5 s (off). 'a man' and 'cards' are both on the same large figure (chest vs hands)."})

# ---------- 4769
t = T(21)
w = {0.0:(0,.38,.52,.62),0.5:(0,.4,.5,.6),1.0:(0,.42,.6,.58),1.5:(0,.42,.5,.58),2.0:(0,.42,.56,.58),2.5:(0,.42,.58,.58),
     3.0:(0,.42,.54,.58),3.5:(0,.42,.62,.58),4.0:(0,.43,.62,.57),4.5:(0,.43,.62,.57),5.0:(0,.43,.62,.57),5.5:(0,.43,.66,.57),
     6.0:(0,.43,.72,.57),6.5:(0,.43,.7,.57),7.0:(0,.43,.54,.57),7.5:(0,.44,.52,.56),8.0:(0,.45,.52,.55),8.5:(0,.45,.52,.55),
     9.0:(0,.45,.52,.55),9.5:(0,.45,.54,.55),10.0:(0,.44,.56,.56)}
k = keys(t, w)
save({"mediaId": 4769, "level": "A", "keyWord": "fence", "defaultVoice": "female",
 "taps": [{"phrase": "to cover her mouth", "target": "the woman", "voice": "female", "keys": k},
          {"phrase": "to wear a blue cap", "target": "the woman", "voice": "female", "keys": k},
          {"phrase": "to look over the fence", "target": "the woman", "voice": "female", "keys": k}],
 "stillS": 4.5,
 "nouns": [{"word": "a fence", "x": 0.72, "y": 0.71, "voice": "female"},
           {"word": "the sky", "x": 0.50, "y": 0.15, "voice": "female"},
           {"word": "a cap", "x": 0.30, "y": 0.49, "voice": "female"},
           {"word": "rocks", "x": 0.68, "y": 0.40, "voice": "female"}],
 "question": "Where is the woman standing?",
 "answer": ["She", "is", "standing", "next to", "a", "fence."], "answerVoice": "female",
 "notes": "Only one target (the woman); all three phrases use her, one is a state (cap). 'rocks' = the canyon walls. 'next to' is one chip."})

# ---------- 4771
t = T(25)
wo = {0.0:(.07,.13,.86,.87),0.5:(.08,.13,.9,.87),1.0:(.1,.18,.9,.82),1.5:(0,.16,1,.84),
      2.5:(.4,.3,.6,.7),3.0:(.28,.29,.72,.71),3.5:(.4,.28,.6,.72),4.0:(.4,.25,.6,.75),4.5:(.8,.36,.2,.64),
      5.0:(.1,.35,.8,.65),5.5:(.1,.37,.85,.63),6.0:(0,.35,1,.65),6.5:(0,.35,1,.65),7.0:(0,.37,1,.63),7.5:(0,.37,1,.63),
      8.0:(.1,.42,.86,.58),8.5:(.16,.47,.82,.53),9.0:(.16,.45,.78,.55),9.5:(.08,.48,.88,.52),
      10.0:(.05,.47,.76,.53),10.5:(.22,.46,.78,.54),11.0:(.2,.42,.8,.58),11.5:(.08,.36,.92,.64),12.0:(.03,.3,.97,.7)}
sh = {2.5:(.04,.46,.22,.2),3.5:(.2,.44,.2,.16),4.0:(.15,.47,.24,.23),4.5:(.19,.47,.26,.23)}
pa = {8.0:(0,.28,1,.14),8.5:(0,.29,1,.18),9.0:(0,.28,1,.17),9.5:(0,.3,1,.18),
      10.0:(.15,.31,.8,.16),10.5:(0,.3,1,.16),11.0:(0,.3,1,.12),11.5:(0,.22,1,.14)}
save({"mediaId": 4771, "level": "A", "keyWord": "palace", "defaultVoice": "female",
 "taps": [{"phrase": "to open a gate", "target": "the woman", "voice": "female", "keys": keys(t, wo)},
          {"phrase": "to have white wool", "target": "the big sheep", "voice": "female", "keys": keys(t, sh)},
          {"phrase": "to stand behind a gold gate", "target": "the palace", "voice": "female", "keys": keys(t, pa)}],
 "stillS": 10.0,
 "nouns": [{"word": "a palace", "x": 0.60, "y": 0.40, "voice": "female"},
           {"word": "a gate", "x": 0.13, "y": 0.28, "voice": "female"},
           {"word": "the sky", "x": 0.55, "y": 0.14, "voice": "female"},
           {"word": "a coat", "x": 0.50, "y": 0.80, "voice": "female"}],
 "question": "What is the woman opening?",
 "answer": ["She", "is", "opening", "the", "gate", "of", "a", "palace."], "answerVoice": "female",
 "notes": "Sheep and palace phrases are states (no unique action). Small sheep in the far background also have white wool; the box is on the big sheep in front only. At 3.5 s the sheep's head is behind her hands: boxes split at x = 0.40. From 11.0 s her head covers most of the palace: palace box is the strip above her hair; at 12.0 s palace set off (almost hidden)."})
