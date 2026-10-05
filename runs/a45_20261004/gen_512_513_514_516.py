import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, x2, y2 = b
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(x2 - x, 2), "h": round(y2 - y, 2)})
    return out
def write(vid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{vid}/info.json'))['times']
    c = {"mediaId": vid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, d)} for p, tg, v, d in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans, "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{vid}.json', 'w'), ensure_ascii=False, indent=1)

# ---------- 512 (boxes as x1,y1,x2,y2)
W = {0.5:(0,0,.60,.34), 1.0:(0,0,.54,.38), 1.5:(.06,0,.40,.60), 2.0:(.08,.15,.40,.60), 2.5:(0,0,.48,.50), 3.0:(0,0,.55,.50),
     3.5:(0,0,.57,.74), 4.0:(.10,0,.50,.22), 4.5:(.03,0,.49,.23), 5.0:(.05,0,.48,.34), 5.5:(.14,0,.50,.46), 6.0:(.12,.02,.48,.44),
     6.5:(.10,.03,.46,.44), 7.0:(.10,.06,.46,.55), 7.5:(.56,.08,1,1), 8.0:(.55,.05,1,1), 8.5:(.57,.05,1,1), 9.0:(.54,.08,1,1),
     9.5:(.58,.08,1,1), 10.0:(.62,.10,1,1)}
M = {0.5:(.61,0,1,.14), 1.0:(.56,0,1,.36), 1.5:(.56,0,.95,.57), 2.0:(.55,.13,.92,.57), 2.5:(.49,0,1,.12), 3.0:(.56,0,1,.19),
     3.5:(.58,0,1,.40), 4.0:(.56,0,.92,.14), 4.5:(.56,0,1,.15), 5.0:(.53,0,1,.36), 5.5:(.53,0,.86,.46), 6.0:(.52,.04,.86,.44),
     6.5:(.53,.06,.87,.46), 7.0:(.54,.08,.87,.58), 7.5:(.36,.38,.55,.68), 8.0:(.35,.38,.54,.67), 8.5:(.36,.38,.56,.68),
     9.0:(.35,.38,.53,.73), 9.5:(.35,.38,.56,.73), 10.0:(.36,.38,.57,.63)}
D = {5.5:(.86,.28,1,.46), 6.0:(.87,.36,1,.53), 6.5:(.87,.40,1,.56), 7.0:(.87,.52,1,.68), 8.5:(.37,.79,.56,.95),
     9.0:(.32,.77,.53,.99), 9.5:(.33,.78,.57,.99), 10.0:(.36,.64,.61,1)}
write(512, "A", "outfit", "female",
  [("to look in the mirror", "the woman", "female", W), ("to wear a green T-shirt", "the man", "male", M),
   ("to pick up a shoe", "the dog", "female", D)],
  6.5, [("a jacket", .50, .47, "female"), ("trousers", .50, .78, "female"), ("shoes", .16, .66, "female"), ("a hat", .84, .71, "female")],
  "What is the woman doing?", ["She", "is", "looking", "at", "her", "outfit", "in", "the", "mirror."], "female",
  "Mirror shot 7.5-10.0: the woman is in the picture twice (real, from behind on the right, and her reflection on the left) with the man's reflection between them, so one box cannot hold both; her box is the REAL woman on the right, the reflection is not boxed. The man in the mirror shot = his reflection. Bed shots: both lean over the bed and their arms cross; boxes are split and cut the woman's right forearm at 2.5-3.5. At 0.0 only hands (whose is unclear) -> both off. At 4.0/4.5 a hand at the right edge (owner unclear) is in no box. Man gets a state phrase: everything he does (leaning on the bed, looking, smiling) the woman does too; his thumbs up shows only at 9.0-9.5. Dog: at the bed edge 5.5-7.0, in the mirror 8.5-10.0 where it takes a white shoe in its mouth (9.5-10.0); small and partly hidden. Key word 'outfit' is the whole set, so it is in the answer, not a noun.")

# ---------- 513
WO = {4.5:(.52,.24,1,.97), 5.0:(.58,.21,1,1), 5.5:(0,.38,.22,.95), 7.0:(.79,.44,1,1), 7.5:(0,.40,.41,.92), 8.0:(0,.43,.26,.79),
      8.5:(.05,.48,.34,.77), 9.0:(.22,.60,.42,.74)}
P = {4.5:(.22,.57,.52,.77), 5.0:(.24,.58,.58,.80), 7.0:(.31,.62,.66,.84), 7.5:(.42,.62,.73,.82), 8.0:(.33,.62,.67,.84), 8.5:(.35,.64,.61,.80)}
H = {4.5:(0,0,.51,.56), 5.0:(0,0,.57,.57), 7.5:(.42,.28,.83,.61), 8.0:(.27,.30,1,.61), 8.5:(.35,.37,1,.63), 9.0:(.26,.47,.86,.60),
     9.5:(.30,.60,.74,.82), 10.0:(.31,.64,.67,.82)}
write(513, "A", "outside", "male",
  [("to walk on the mat", "the woman in the orange dress", "female", WO), ("to stand under the table", "the pot", "male", P),
   ("to have a grey roof", "the house", "male", H)],
  8.5, [("the sky", .40, .15, "male"), ("a house", .72, .46, "male"), ("a pot", .48, .72, "male"), ("grass", .50, .93, "male")],
  "Where are the people eating?", ["They", "are", "eating", "outside", "the", "house."], "male",
  "Many cuts and about seven people whose clothes repeat (two red T-shirts, several white shirts) and change between shots, and the two men both carry the table, so only one person is a target: the woman in the orange wrap dress (walks barefoot over the mat at 4.5-5.5; at 7.0 she is the bending figure at the right edge, 7.5-9.0 she sits front left). The other two targets are things with state phrases. The house: boxed only where it is seen from outside (4.5, 5.0, 7.5-10.0); off in the first shots filmed from inside the doorway. Its boxes are cut where the woman or the pot is in front (7.5 left half of the house, 9.0 only the upper part). Pot: 'to stand under the table' fits 7.0-8.5; at 4.5-5.0 it is being carried, boxed anyway (same pot); the mat also lies under the table - verifier may want to check that. Woman off at 9.5/10.0 (a dot). No single main person -> defaultVoice by evenId false = male.")

# ---------- 514
W4 = {0.0:(.75,0,1,.27), 0.5:(.80,0,1,.30), 1.0:(.82,0,1,.20), 1.5:(.66,0,1,.25), 2.0:(.56,0,1,.30), 2.5:(.58,0,1,.28), 3.0:(.76,0,1,.28),
      3.5:(.72,0,1,.47), 4.0:(.55,.10,1,.80), 4.5:(.60,.06,1,.50), 5.0:(.63,.05,1,.60), 5.5:(.80,0,1,.40), 6.0:(.82,0,1,.13),
      6.5:(.68,0,1,.32), 7.0:(.58,.03,1,.36), 7.5:(.69,.05,1,.50), 8.0:(.80,.10,1,.47), 8.5:(.78,.11,1,.50), 9.0:(.72,.10,1,.60),
      9.5:(.68,.13,1,.62), 10.0:(.65,.10,1,.62)}
M4 = {0.0:(.58,.08,.75,.48), 0.5:(.58,.08,.80,.50), 1.0:(.60,.08,.82,.48), 1.5:(.62,.25,.90,.47), 2.0:(.60,.30,.88,.52), 2.5:(.60,.28,.90,.44),
      3.0:(.60,.10,.76,.50), 3.5:(.58,.22,.72,.47), 5.5:(.66,.12,.80,.40), 6.0:(.70,.13,1,.50), 6.5:(.60,.32,.86,.48), 7.0:(.58,.36,.80,.50),
      7.5:(.57,.20,.69,.50), 8.0:(.58,.16,.80,.52), 8.5:(.56,.15,.78,.52), 9.0:(.48,.16,.72,.50), 9.5:(.43,.16,.68,.50), 10.0:(.40,.18,.65,.53)}
B4 = {0.0:(.56,.57,1,.76), 0.5:(.56,.56,1,.76), 1.0:(.66,.48,1,.62), 1.5:(.28,.50,.72,.70), 2.0:(.08,.56,.44,.72), 2.5:(.06,.55,.36,.71),
      3.5:(.14,.52,.46,.70), 4.0:(.14,.46,.48,.62), 4.5:(.14,.45,.48,.61), 5.0:(.12,.43,.50,.60), 5.5:(.14,.42,.50,.58), 6.0:(.05,.46,.42,.66),
      6.5:(.05,.49,.40,.68), 7.0:(.05,.50,.34,.66), 7.5:(.07,.52,.46,.72), 8.0:(.20,.52,.72,.73), 8.5:(.24,.52,.78,.76), 9.0:(.17,.52,.72,.74),
      9.5:(.20,.50,.68,.73), 10.0:(.14,.53,.65,.75)}
write(514, "A", "oven", "female",
  [("to cover her hair", "the woman", "female", W4), ("to have a beard", "the man", "male", M4),
   ("to bake in the oven", "the bread", "female", B4)],
  8.5, [("a window", .40, .10, "female"), ("an oven", .20, .45, "female"), ("bread", .52, .62, "female"), ("a glove", .80, .76, "female")],
  "What are they doing?", ["They", "are", "taking", "bread", "out", "of", "the", "oven."], "female",
  "The man and the woman crouch cheek to cheek the whole clip and their heads overlap in almost every frame; the boxes are split along the line between the two faces, are mostly head-sized and lose parts (shoulders, arms, the oven gloves, whose owner is often unclear). Because both do the same things (watch the oven, smile, reach in) and the hands cannot be told apart, both get state phrases that fit only one of them (her head cloth, his beard). Man off at 4.0-5.0 (hidden behind her, only a bit of beard). Bread = the same loaf throughout: raw dough on the tray at 0.0-2.5, inside the lit oven 3.5-7.5, taken out 8.0-10.0; off at 3.0 (hidden by the door). 'a glove' = the oven glove; 'an oven' pill sits on the control panel / front. Couple, no single main person -> defaultVoice by evenId true = female.")

# ---------- 516
MAN = {0.0:(0,.08,.72,1), 0.5:(0,.06,.62,1), 1.0:(0,0,.52,1), 1.5:(0,.28,.25,.90), 2.0:(0,.28,.18,.80), 2.5:(0,.36,.15,.80),
       3.0:(0,.04,1,1), 3.5:(.08,.20,1,1), 4.0:(.28,.20,1,.97), 4.5:(.35,.18,1,.95), 5.0:(.28,.15,.78,1), 5.5:(.27,.13,.73,1),
       6.0:(.25,.13,.73,.93), 6.5:(.25,.13,.73,.93), 7.0:(.25,.13,.73,.93)}
SINK = {0.0:(.72,.58,1,.80), 0.5:(.63,.55,1,.80), 1.0:(.53,.60,1,.92), 1.5:(.26,.60,.97,.94), 2.0:(.19,.50,1,.84), 2.5:(.16,.45,1,.88),
        5.0:(.79,.36,1,.52), 5.5:(.74,.36,1,.52), 6.0:(.74,.36,1,.52), 6.5:(.74,.36,1,.52), 7.0:(.74,.36,1,.52)}
write(516, "B", "overflow", "male",
  [("to turn off the tap", "the man", "male", MAN), ("to stand in a puddle", "the man", "male", MAN),
   ("to overflow with soapy water", "the sink", "male", SINK)],
  6.0, [("a towel", .58, .33, "male"), ("a tap", .87, .42, "male"), ("a washing machine", .85, .72, "male"), ("a puddle", .30, .92, "male")],
  "What is wrong with the sink?", ["The", "sink", "is", "overflowing", "onto", "the", "floor."], "male",
  "Cartoon, one person: two phrases for the man (turns off the tap at 4.0-4.5, stands in the puddle 4.5-7.0), one for the sink (overflows at 2.5, water runs down the cupboard at 4.0). Sink boxes at 0.0-1.0 hold only the part right of the man's arm; sink off at 3.0-3.5 (close-up of the man) and at 4.0-4.5 (hidden behind his arms); from 5.0 the sink is small at the right edge and the box takes the tap with it. The puddle and the towel were not used as targets because they overlap the man. The key word is a verb: it is in phrase 3 and in the answer.")
