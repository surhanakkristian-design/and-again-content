import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x0, y0, x1, y1 = b
        out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def write(mid, kw, dv, taps, still, nouns, q, ans, av, notes):
    c = {"mediaId": mid, "level": "B", "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(b)} for p, tg, v, b in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"{HERE}/content/{mid}.json", "w"), indent=1, ensure_ascii=False)

def v7220():
    gk = [(.01,.40,.90,.67),(.01,.44,.91,.69),(.0,.45,.90,.70),(.0,.46,.94,.71),(.0,.40,.98,.71),(.0,.39,1.0,.72),(.0,.39,1.0,.74),(.0,.37,1.0,.74)]
    fire = [(.07,.22,.27,.37)]*8
    crowd = [(.28,.16,1.0,.37),(.28,.16,1.0,.37),(.28,.11,1.0,.36),(.28,.11,1.0,.36),(.28,.09,1.0,.36),(.28,.12,1.0,.36),(.28,.17,1.0,.36),(.28,.17,1.0,.36)]
    write(7220, "hold off", "male",
      [("to sprawl across the ice", "the goalkeeper", "male", gk),
       ("to cheer on the players", "the crowd", "male", crowd),
       ("to blaze in a metal barrel", "the fire", "male", fire)],
      2.7, [("pine trees", .50, .06, "male"), ("a barrel", .20, .30, "male"), ("a net", .12, .55, "male"), ("a puck", .44, .70, "male")],
      "What is the goalkeeper doing?", "He is sprawling across the ice.", "male",
      "crowd box starts at x .28 so it does not overlap the fire box; standing players in front of the crowd on the right fall inside the crowd box at 0.2-0.7 s; key word hold off is shown by the goalkeeper keeping the attackers away")

def v7222():
    gir = [(.54,.0,1.0,.41),(.53,.0,1.0,.45),(.50,.0,1.0,.45),(.50,.0,1.0,.45),(.50,.0,1.0,.42),(.50,.0,1.0,.39),(.55,.0,1.0,.37),(.58,.0,1.0,.38)]
    wom = [(.0,.41,.75,1.0),(.0,.45,.76,1.0),(.0,.45,.75,1.0),(.0,.45,.73,1.0),(.0,.42,.66,1.0),(.0,.39,.63,1.0),(.0,.42,.40,1.0),(.0,.48,.30,1.0)]
    write(7222, "hold out", "female",
      [("to hold out a leafy branch", "the woman in yellow", "female", wom),
       ("to lean towards the giraffe", "the woman in yellow", "female", wom),
       ("to stick out its tongue", "the giraffe", "female", gir)],
      2.2, [("the sky", .20, .15, "female"), ("a guide", .43, .60, "male"), ("a railing", .82, .70, "female"), ("a potted plant", .55, .88, "female")],
      "What is the woman in yellow doing?", "She is holding out a leafy branch.", "female",
      "woman and giraffe boxes split horizontally where her hand meets the tongue (tongue tip / her head top slightly cut at 0.7-1.7 s); guide not used as target because her arm crosses him; second giraffe in background so no giraffe noun")

def v7223():
    wom = [(.19,.28,.75,.77),(.19,.27,.76,.77),(.19,.24,.76,.79),(.19,.22,.81,.81),(.18,.21,.77,.84),(.17,.22,.78,.87),(.16,.25,.78,.90),(.16,.26,.79,.90)]
    arch = [(.0,.04,1.0,.28),(.0,.05,1.0,.27),(.0,.07,1.0,.24),(.0,.07,1.0,.22),(.0,.07,1.0,.21),(.0,.08,1.0,.22),(.0,.11,1.0,.25),(.0,.12,1.0,.26)]
    write(7223, "hold up", "female",
      [("to hold up a metal beam", "the superhero", "female", wom),
       ("to rise from a deep squat", "the superhero", "female", wom),
       ("to span the cobbled lane", "the metal arch", "female", arch)],
      2.7, [("a metal beam", .50, .21, "female"), ("a costume", .50, .48, "female"), ("bunting", .20, .91, "female"), ("a paper lantern", .84, .88, "female")],
      "What is the superhero doing?", "She is holding up a metal beam.", "female",
      "arch box ends where the superhero's hands start; the held beam lies in front of the arch and falls into the arch box; arch partly hidden by the beam later in the clip")

def v7224():
    man = [(.22,.39,.77,.72),(.21,.37,.79,.73),(.18,.37,.80,.75),(.19,.36,.83,.77),(.20,.35,.82,.78),(.15,.33,.88,.78),(.14,.33,.88,.80),(.14,.34,.88,.80)]
    bowl = [(.46,.25,.66,.39),(.47,.23,.67,.37),(.47,.22,.67,.37),(.48,.22,.68,.36),(.49,.21,.69,.35),(.51,.19,.71,.33),(.52,.19,.72,.33),(.53,.19,.73,.34)]
    swim = [(.66,.19,.86,.36),(.67,.17,.86,.34),(.67,.18,.86,.35),(.68,.17,.87,.34),(.70,.15,.88,.34),(.71,.13,.90,.32),(.72,.15,.92,.33),(.73,.15,.93,.34)]
    write(7224, "hold your breath", "male",
      [("to pinch his nose shut", "the man in front", "male", man),
       ("to hover above his head", "the bowl of apples", "male", bowl),
       ("to dangle both legs underwater", "the swimmer", "male", swim)],
      2.2, [("candles", .30, .46, "male"), ("a bow tie", .50, .59, "male"), ("a tablecloth", .17, .74, "male"), ("apples", .58, .31, "male")],
      "What is the man in front doing?", "He is pinching his nose shut.", "male",
      "swimmer in red trunks sits at the top edge of the pool, gender not certain; bowl box split from the man's hair at its stand")

for f in sys.argv[1:]: globals()['v' + f]()
