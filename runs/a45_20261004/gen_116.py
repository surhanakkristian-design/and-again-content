# writes content/116.json, 117.json, 120.json, 123.json (one writer's four videos)
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c): json.dump(c, open(f'{HERE}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 116
t = T(19)
man = {0.0:(.05,.10,.90,.90),0.5:(.12,.10,.88,.90),1.0:(.03,.08,.85,.92),1.5:(0,0,1,.55),2.0:(0,0,1,.52),2.5:(.15,.12,.85,.88),
 3.0:(.12,.06,.88,.94),3.5:(0,0,1,.45),4.0:(0,0,1,.55),4.5:(.10,.13,.90,.87),5.0:(0,.13,.88,.87),5.5:(.20,.18,.39,.80),
 6.0:(0,.05,.72,.62),6.5:(0,.03,.82,.61),7.0:(0,.05,.82,.59),7.5:(.05,.12,.92,.88),8.0:(.18,.18,.82,.82),8.5:(0,0,1,.58),9.0:(0,0,1,.60)}
pot = {5.5:(.60,.44,.34,.20),6.0:(.40,.68,.52,.27),6.5:(.50,.65,.42,.20),7.0:(.50,.65,.42,.20)}
save({"mediaId":116,"level":"A","keyWord":"breaking","defaultVoice":"male","taps":[
 {"phrase":"to hold a hammer","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to laugh happily","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to fall on the floor","target":"the pot","voice":"male","keys":keys(t,pot)}],
 "stillS":0.0,
 "nouns":[{"word":"a hammer","x":.22,"y":.27,"voice":"male"},{"word":"a man","x":.58,"y":.40,"voice":"male"},
          {"word":"a tile","x":.48,"y":.75,"voice":"male"},{"word":"a window","x":.65,"y":.07,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","breaking","tiles","with","a","hammer."],"answerVoice":"male",
 "notes":"Only one person; two phrases share the man, third target is the clay pot (visible 5.5-7.0 only: tips off the bench, lands on the floor). Close-ups 1.5/2.0/3.5/4.0/8.5/9.0 show only the man's hands/legs/torso: box = that part. 5.5-7.0 man box cut so it does not overlap the pot (5.5 right part of head, 6.0-7.0 his boots are outside). Cartoon character named 'a man'."})

# ---------- 117
t = T(21)
woman = {0.0:(.48,.10,.52,.65),0.5:(.48,.10,.52,.72),1.0:(.49,.07,.51,.73),1.5:(.37,0,.63,.62),2.0:(.39,0,.61,.62),2.5:(.55,0,.45,.58),3.0:(.52,0,.48,.68),
 9.5:(.12,.18,.25,.52),10.0:(.10,.20,.31,.42)}
man = {0.0:(.05,.13,.42,.44),0.5:(.08,.13,.39,.44),1.0:(.03,.12,.45,.52),1.5:(0,0,.36,.60),2.0:(0,0,.38,.50),2.5:(.03,0,.44,.50),3.0:(.02,0,.47,.52),
 3.5:(0,0,1,.92),4.0:(0,0,1,.55),4.5:(0,0,1,.55),5.0:(0,0,1,.72),5.5:(0,0,1,.72),6.0:(0,0,1,.62),6.5:(0,0,1,.62),7.0:(0,0,1,.66),7.5:(0,0,1,.68),
 8.0:(0,0,1,.60),8.5:(.15,0,.85,.78),9.0:(.05,0,.95,.82),9.5:(.38,.12,.62,.78),10.0:(.42,.13,.58,.68)}
cat = {0.0:(.74,0,.26,.09),0.5:(.76,0,.24,.09),1.0:(.74,0,.26,.06),9.5:(.79,0,.21,.12),10.0:(.77,0,.21,.13)}
save({"mediaId":117,"level":"B","keyWord":"mosaic","defaultVoice":"male","taps":[
 {"phrase":"to wrap plates in cloth","target":"the woman","voice":"female","keys":keys(t,woman)},
 {"phrase":"to display the finished mosaic","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to perch on a shelf","target":"the cat","voice":"male","keys":keys(t,cat)}],
 "stillS":10.0,
 "nouns":[{"word":"a mosaic","x":.62,"y":.60,"voice":"male"},{"word":"a cat","x":.84,"y":.08,"voice":"male"},
          {"word":"a mallet","x":.16,"y":.74,"voice":"male"},{"word":"a headscarf","x":.30,"y":.26,"voice":"male"}],
 "question":"What is the man displaying?","answer":["He","is","displaying","the","finished","mosaic."],"answerVoice":"male",
 "notes":"Cat sits on the top shelf directly above the woman's head at 0.0-1.0: its box is thinner than the minimum so it does not overlap hers. 3.5-9.0 only the man's gloved hands / torso are in the picture (woman off; a figure at the top edge of 9.0 is not keyed). 9.5/10.0: the cat sits right beside the man's head, so the man box starts below the cat box (his hair / forehead are outside) and the cat box is thinner than the minimum; his raised glove overlaps the woman, split by a vertical line. Woman's head is out of frame 1.5-3.0 (she swings the mallet): box = her torso and arm. 'a headscarf' pill is small-target, on the woman's head at 10.0."})

# ---------- 120
man = {0.0:(0,0,.52,.80),0.5:(0,0,.55,.75),1.0:(0,0,.58,.62),1.5:(0,0,1,.58),2.0:(0,.29,1,.33),2.5:(0,.36,1,.26),3.0:(0,.33,1,.44),3.5:(.57,0,.43,.62),
 4.5:(.40,0,.52,.22),5.0:(0,.05,.71,.48),5.5:(0,.30,1,.17),6.0:(0,.37,1,.20)}
woman = {0.0:(.55,.25,.45,.32),0.5:(.57,.20,.43,.32),1.0:(.60,.10,.40,.44),2.0:(.66,0,.34,.28),2.5:(.38,.12,.20,.23),3.0:(.36,.08,.22,.24),3.5:(.26,0,.30,.40),
 4.0:(.50,0,.50,.35),5.0:(.72,0,.28,.42),5.5:(.38,0,.62,.29),6.0:(.32,0,.68,.36),6.5:(0,.05,1,.75),7.0:(0,.12,1,.72),7.5:(0,.12,1,.76),8.0:(0,.10,1,.76),
 8.5:(0,.10,1,.88),9.0:(0,.15,1,.85),9.5:(0,.15,1,.85),10.0:(0,.14,1,.84)}
save({"mediaId":120,"level":"A","keyWord":"burger","defaultVoice":"female","taps":[
 {"phrase":"to cook the meat","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to eat a big burger","target":"the woman","voice":"female","keys":keys(t,woman)},
 {"phrase":"to sit at the table","target":"the woman","voice":"female","keys":keys(t,woman)}],
 "stillS":6.0,
 "nouns":[{"word":"a woman","x":.65,"y":.20,"voice":"female"},{"word":"a hand","x":.40,"y":.46,"voice":"female"},{"word":"a burger","x":.50,"y":.70,"voice":"female"}],
 "question":"What is the woman eating?","answer":["She","is","eating","a","big","burger."],"answerVoice":"female",
 "notes":"1.5-6.0 the man is only hands/arms in the foreground with the woman behind them: the man box is the hand area, the woman box the part of her that shows (2.0-3.0 small; 4.5 she is hidden -> off; 4.0 only the man's fingertips on the bottle -> man off). She only eats from 6.5 on. A rooster walks in the background 9.0-10.0 (not used)."})

# ---------- 123
woman = {0.0:(0,.30,.36,.70),0.5:(0,.22,.58,.78),1.0:(0,.15,.60,.85),1.5:(0,.12,.65,.88),2.0:(0,.05,.64,.95),2.5:(0,0,.52,1),3.0:(0,0,.47,1),3.5:(0,0,.46,1),
 4.0:(0,0,.41,1),4.5:(0,.20,.47,.80),5.0:(0,.30,.40,.70),5.5:(0,.39,.46,.61),6.0:(0,.37,.62,.63),6.5:(0,.39,.62,.61),7.0:(0,.47,.62,.53),7.5:(0,.45,.64,.55),
 8.0:(0,.35,.75,.65),8.5:(0,.36,.73,.64),9.0:(0,.28,.47,.72),9.5:(0,0,.18,1),10.0:(0,0,.22,1)}
man = {5.5:(0,0,.18,.38),6.0:(0,0,.18,.36),6.5:(0,0,.18,.38),7.0:(0,0,.19,.46),7.5:(.09,0,.18,.44),8.0:(.07,0,.18,.34),8.5:(.11,0,.18,.35),9.0:(.11,0,.22,.27),
 9.5:(.19,0,.24,.24),10.0:(.23,0,.30,.36)}
bird = {3.5:(.48,.28,.32,.24),4.0:(.42,.17,.46,.40)}
save({"mediaId":123,"level":"A","keyWord":"bush","defaultVoice":"female","taps":[
 {"phrase":"to pick some berries","target":"the woman","voice":"female","keys":keys(t,woman)},
 {"phrase":"to stand behind the woman","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to fly out of the bush","target":"the bird","voice":"female","keys":keys(t,bird)}],
 "stillS":2.0,
 "nouns":[{"word":"a hand","x":.48,"y":.20,"voice":"female"},{"word":"a bowl","x":.12,"y":.60,"voice":"female"},{"word":"a bush","x":.65,"y":.75,"voice":"female"}],
 "question":"What is the woman picking?","answer":["She","is","picking","berries","from","a","bush."],"answerVoice":"female",
 "notes":"The bird is clearly in the picture only at 3.5 and 4.0 (black, in the leaves; small at 3.5). A dark animal sits on the path in the background from 4.5 on; not certain it is the bird, so not keyed. Man and woman stand close at the left edge 5.5-10.0: the man's box is his head/chest only, the woman's box is her arm, bowl and dress (7.0-9.0 her face at the edge is outside her box; 9.5/10.0 her box is the left strip with face and body, her raised hand is outside). The man phrase is a position, no action fits only him."})
