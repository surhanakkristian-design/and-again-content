# writes content/5117, 6836, 5540, 5671 (one writer's four videos)
import json
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)})
    return out
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 5117
T = [i * 0.5 for i in range(19)]
man = [(0,0,.58,1),(0,0,.70,1),(0,.05,.72,.95),(0,0,.62,1),(0,0,.56,1),(0,0,.56,1),(0,0,.62,1),(0,.05,.80,.95),(0,0,.70,1),(0,0,.78,1),
       (0,.05,.70,.95),(0,.05,.72,.95),(0,0,.66,1),(0,.16,.58,.84),(0,.26,.44,.74),(0,.34,.62,.66),(.03,.30,.72,.70),(0,.42,.78,.58),(.05,.60,.75,.40)]
shl = [(.60,0,.40,.52),(.72,0,.28,.42),(.74,0,.26,.50),(.64,0,.36,.50),(.58,0,.42,.44),(.58,0,.42,.46),(.64,0,.36,.56),(.82,0,.18,.60),(.72,0,.28,.45),(.80,0,.20,.40),
       (.72,0,.28,.40),(.74,0,.26,.36),(.68,0,.32,.32),(.60,0,.40,.40),(.45,0,.55,.19),(.82,0,.18,.90),(.78,0,.22,.85),(.80,.40,.20,.55),(.82,.50,.18,.50)]
km, ks = keys(T, man), keys(T, shl)
write({"mediaId": 5117, "level": "B", "keyWord": "bookstore", "defaultVoice": "male",
 "taps": [{"phrase": "to flick through a hardback", "target": "the man", "voice": "male", "keys": km},
          {"phrase": "to gasp in amazement", "target": "the man", "voice": "male", "keys": km},
          {"phrase": "to be crammed with books", "target": "the bookshelves", "voice": "male", "keys": ks}],
 "stillS": 1.0,
 "nouns": [{"word": "glasses", "x": 0.37, "y": 0.19, "voice": "male"}, {"word": "bookshelves", "x": 0.78, "y": 0.30, "voice": "male"},
           {"word": "a denim jacket", "x": 0.22, "y": 0.42, "voice": "male"}, {"word": "a hardback", "x": 0.50, "y": 0.54, "voice": "male"}],
 "question": "What is the young man doing?",
 "answer": ["He", "is", "flicking", "through", "a", "hardback", "in", "a", "bookstore."], "answerVoice": "male",
 "notes": "Only one person in focus (blurred customers far behind), so two phrases are on the man; the third target is the bookshelves on the right-hand side (shelves on the left edge are not boxed, the man's box covers that side). The man's box includes the book he holds and the floor stacks under it. 7.0-9.0: the huge book hides part of the right shelves; the shelves box overlaps the book edge at 7.5/8.0. 'bookstore' is the place, used in the answer, not a noun slot."})

# ---------- 6836
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2]
wom = [(.05,.48,.30,.40),(.02,.50,.27,.40),(.13,.63,.26,.37),(.19,.64,.24,.36),(.22,.54,.28,.46),(.25,.54,.29,.46),(.24,.66,.26,.34)]
sofa = [(.35,.49,.34,.32),(.29,.49,.36,.30),(0,.82,.13,.16),(0,.84,.19,.16),(0,.76,.22,.22),(0,.78,.25,.21),(0,.86,.24,.14)]
kw, kso = keys(T, wom), keys(T, sofa)
write({"mediaId": 6836, "level": "B", "keyWord": "apartment building", "defaultVoice": "female",
 "taps": [{"phrase": "to haul up a sofa", "target": "the young woman", "voice": "female", "keys": kw},
          {"phrase": "to dangle from a rope", "target": "the sofa", "voice": "female", "keys": kso},
          {"phrase": "to raise a clenched fist", "target": "the young woman", "voice": "female", "keys": kw}],
 "stillS": 0.2,
 "nouns": [{"word": "an apartment building", "x": 0.50, "y": 0.07, "voice": "female"}, {"word": "a barbecue", "x": 0.66, "y": 0.50, "voice": "female"},
           {"word": "a sofa", "x": 0.50, "y": 0.63, "voice": "female"}, {"word": "a van", "x": 0.86, "y": 0.76, "voice": "female"}],
 "question": "What is the young woman doing?",
 "answer": ["She", "is", "hauling", "a", "sofa", "onto", "her", "balcony."], "answerVoice": "female",
 "notes": "The sofa dangles only at 0.2-0.7; from 1.2 it stands on the balcony behind the railing, half hidden by the woman: its box is the part left of her (small at 1.2, where her left elbow is cut by the split). The fist is raised at 2.2-2.7 (the older women raise open hands, not a fist). Neighbours are too small for tap targets. The key word pill sits on the brick front at the top; the whole picture is the building."})

# ---------- 5540
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
br = [(.50,.12,.50,.60),(.49,.12,.51,.59),(.46,.08,.54,.66),(.52,.11,.48,.66),(.44,.06,.53,.54),(.46,.02,.50,.60),(.44,.08,.50,.51),(.45,.03,.53,.75)]
po = [(.15,.45,.35,.42),(.15,.44,.34,.44),(.14,.50,.32,.50),(.17,.51,.35,.49),(.16,.40,.28,.58),(.20,.44,.26,.56),(.15,.60,.47,.40),(.06,.60,.39,.40)]
kb, kp = keys(T, br), keys(T, po)
write({"mediaId": 5540, "level": "B", "keyWord": "aid", "defaultVoice": "female",
 "taps": [{"phrase": "to scale the climbing wall", "target": "the woman with braids", "voice": "female", "keys": kb},
          {"phrase": "to crouch on the mat", "target": "the woman with the ponytail", "voice": "female", "keys": kp},
          {"phrase": "to grip a large hold", "target": "the woman with braids", "voice": "female", "keys": kb}],
 "stillS": 0.2,
 "nouns": [{"word": "braids", "x": 0.54, "y": 0.27, "voice": "female"}, {"word": "a ponytail", "x": 0.24, "y": 0.58, "voice": "female"},
           {"word": "a mat", "x": 0.68, "y": 0.82, "voice": "female"}, {"word": "a chalk bag", "x": 0.17, "y": 0.91, "voice": "female"}],
 "question": "What is the woman with braids doing?",
 "answer": ["She", "is", "scaling", "a", "steep", "climbing", "wall."], "answerVoice": "female",
 "notes": "In the frames the woman with the ponytail crouches (0.2-1.7), rises and reaches up towards the climber (2.7) but no clear push is visible, so no phrase on helping and the key word 'aid' (abstract) is in no text. The two women overlap in the picture: boxes are split on a vertical line, so the ponytail woman's outstretched hands (0.2-2.7) and at 3.2 the climber's lower foot fall outside their own box. 'a mat' = the big blue mat in the foreground; there are several mats."})

# ---------- 5671
man = [(.20,.28,.34,.49),(.22,.26,.32,.50),(.20,.28,.34,.47),(.22,.30,.32,.45),(.21,.28,.31,.49),(.18,.28,.36,.49),(.20,.29,.32,.46),(.18,.30,.34,.46)]
cyc = [(.56,.33,.27,.44),(.56,.33,.27,.43),(.56,.34,.28,.41),(.56,.34,.27,.40),(.56,.33,.28,.44),(.56,.33,.27,.44),(.55,.34,.28,.41),(.55,.34,.28,.41)]
km, kc = keys(T, man), keys(T, cyc)
write({"mediaId": 5671, "level": "B", "keyWord": "boost", "defaultVoice": "male",
 "taps": [{"phrase": "to pump his fist", "target": "the man", "voice": "male", "keys": km},
          {"phrase": "to pedal up the hill", "target": "the cyclist", "voice": "female", "keys": kc},
          {"phrase": "to run alongside a cyclist", "target": "the man", "voice": "male", "keys": km}],
 "stillS": 3.7,
 "nouns": [{"word": "snowy peaks", "x": 0.22, "y": 0.23, "voice": "male"}, {"word": "a helmet", "x": 0.67, "y": 0.38, "voice": "male"},
           {"word": "a stone wall", "x": 0.86, "y": 0.54, "voice": "male"}, {"word": "fallen leaves", "x": 0.62, "y": 0.86, "voice": "male"}],
 "question": "What is the man doing?",
 "answer": ["He", "is", "giving", "the", "cyclist", "a", "boost."], "answerVoice": "male",
 "notes": "The two women at the roadside both clap, so no phrase fits only one of them; they stand just left of the man and his box overlaps them a little (they are not targets). Clip has a man and a woman as main people: defaultVoice male (odd id). 'boost' = the encouragement he gives by running beside her with his fist up; the slope of the road is gentle in the picture."})
