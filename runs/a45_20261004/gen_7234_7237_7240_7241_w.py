import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(boxes, times):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x1, y1, x2, y2 = [max(0.0, min(1.0, v)) for v in b]
        out.append({"t": t, "x": round(x1, 2), "y": round(y1, 2), "w": round(x2 - x1, 2), "h": round(y2 - y1, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(b, times)} for p, tg, v, b in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(' '), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)

W = {}
# 7234
woman = [(.19,.39,.67,.91),(.22,.40,.73,.88),(.26,.43,.71,.89),(.26,.44,.71,.88),
         (.26,.47,.68,.86),(.29,.49,.68,.85),(.32,.49,.66,.84),(.38,.50,.74,.83)]
houses = [(0,.03,1,.37)]*8
W[7234] = lambda: write(7234,"B","housing","female",
  [("to carry laundry on her hip","the woman","female",woman),
   ("to climb the worn steps","the woman","female",woman),
   ("to cover the steep hillside","the houses","female",houses)],
  0.7,[("housing",.50,.15,"female"),("a satellite dish",.22,.40,"female"),
       ("a laundry basket",.36,.63,"female"),("steps",.50,.92,"female")],
  "What is the woman carrying?","She is carrying a laundry basket on her hip.","female","")
# 7237
balloon = [(.36,.35,.58,.50),(.36,.33,.62,.49)]+[None]*6
fireball = [(.37,.06,.94,.34),(.36,.0,1,.32),(.33,.0,1,.29),(.30,.0,1,.37)]+[None]*4
flame = [(.18,.37,.35,.51),(.19,.40,.36,.54),(.19,.46,.37,.60),(.19,.50,.37,.64),
         (.19,.54,.37,.68),(.20,.56,.38,.70),(.20,.57,.38,.71),(.21,.58,.39,.72)]
W[7237] = lambda: write(7237,"B","hydrogen","male",
  [("to burst into flames","the balloon","male",balloon),
   ("to rise towards the ceiling","the fireball","male",fireball),
   ("to flicker at the tip","the small flame","male",flame)],
  2.7,[("smoke",.55,.22,"male"),("a balloon",.29,.43,"male"),
       ("a gas cylinder",.27,.78,"male"),("a fire extinguisher",.75,.83,"male")],
  "What happens to the balloon?","It bursts into a huge ball of flame.","male",
  "Only the first balloon is a target (off after it bursts); fireball off once only smoke is left (from 2.2 s).")
# 7240
w40 = [(.25,.28,.71,.92),(.32,.27,.71,.93),(.42,.28,.73,.93),(.44,.28,.74,.93),
       (.43,.27,.74,.94),(.44,.26,.76,.95),(.45,.25,.77,.97),(.47,.24,.79,.98)]
statue = [(.01,.32,.24,.71),(.01,.31,.28,.72),(.01,.31,.28,.70),(.01,.31,.29,.71),
          (.0,.30,.27,.72),(.01,.30,.28,.72),(.0,.29,.27,.72),(.02,.29,.29,.72)]
men = [(.72,.40,.96,.68),(.72,.40,.96,.68),(.74,.40,.97,.68),(.75,.40,.98,.68),
       (.75,.40,.97,.68),(.77,.40,.99,.68),(.78,.40,1,.69),(.80,.40,1,.69)]
W[7240] = lambda: write(7240,"B","idol","female",
  [("to press her palms together","the woman","female",w40),
   ("to wear a marigold garland","the statue","female",statue),
   ("to stand beside a bicycle","the two men","male",men)],
  2.2,[("an idol",.15,.45,"female"),("a brass bell",.75,.34,"female"),
       ("an oil lamp",.38,.61,"female"),("a sari",.62,.76,"female")],
  "What is the woman doing?","She is praying in front of the idol.","female",
  "Target 'the two men' is one box over both men (they do the same). Woman/men boxes split where the sari edge meets the left man.")
# 7241
w41 = [(.22,.47,.84,.97),(.19,.46,.86,.97),(.14,.45,.87,1),(.07,.43,.88,1),
       (.05,.43,.89,1),(.02,.42,.90,1),(0,.35,.91,1),(0,.33,.93,1)]
pilot = [(.26,.32,.49,.47),(.30,.32,.49,.46),(.32,.31,.56,.45),(.36,.29,.61,.43),
         (.38,.29,.57,.43),(.39,.28,.56,.42),None,None]
W[7241] = lambda: write(7241,"B","ignore","male",
  [("to ignore the crashing balloon","the woman","female",w41),
   ("to sip an iced drink","the woman","female",w41),
   ("to cling to the basket","the pilot","male",pilot)],
  2.2,[("a hot-air balloon",.72,.15,"male"),("a wicker basket",.30,.48,"male"),
       ("an iced drink",.58,.58,"male"),("pastries",.88,.84,"male")],
  "What is the seated woman doing?","She is ignoring the crashing balloon.","female",
  "Pilot off at 3.2/3.7 s (hidden behind her head). Woman/pilot boxes split by y where his basket meets her head; dog and shouting man skipped as targets because their boxes would overlap hers.")
for m in sys.argv[1:]: W[int(m)]()
