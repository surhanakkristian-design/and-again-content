import json
def B(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d): return [B(t,d[t]) for t in sorted(d)]
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)
def mk(lst): return {i*0.5:b for i,b in enumerate(lst)}
N=None
# ---------- 4345
w=mk([N,(.19,.25,.4,.67),(.07,.31,.78,.69),(0,.09,1,.91),(0,.12,.8,.88),(0,.08,.85,.92),(.2,.12,.68,.88),(.15,.12,.85,.88),
(.15,.17,.85,.83),(.1,.2,.8,.8),(.02,.17,.72,.83),(.02,.2,.72,.8),(0,.05,.95,.95),(.07,.14,.75,.86),(.22,.3,.52,.7),
(.25,.27,.38,.52),(.27,.22,.3,.42),(.3,.21,.27,.4),(.33,.25,.26,.43)])
tg="the woman in the bright jacket"
save({"mediaId":4345,"level":"A","keyWord":"joy","defaultVoice":"female",
"taps":[{"phrase":"to come into the house","target":tg,"voice":"female","keys":keys(w)},
{"phrase":"to carry the presents","target":tg,"voice":"female","keys":keys(w)},
{"phrase":"to hold a phone","target":tg,"voice":"female","keys":keys(w)}],
"stillS":8.0,
"nouns":[{"word":"a cake","x":.28,"y":.62,"voice":"female"},{"word":"balloons","x":.58,"y":.06,"voice":"female"},
{"word":"a table","x":.3,"y":.76,"voice":"female"},{"word":"a chair","x":.84,"y":.76,"voice":"female"}],
"question":"What is the woman carrying?","answer":["She","is","carrying","the","birthday","presents."],"answerVoice":"female",
"notes":"One target for all three phrases: the boy and the girl do the same things (run to her, hug her, scream, dance) and the party guests share their clothes colours, so no phrase fits only one child. 0.0 s: closed door, woman not visible -> off. 3.5-6.0 s: selfie close-up, her box also holds parts of the children's faces. Key word 'joy' is abstract -> not a noun slot. 'a table' sits under the cake (pill 0.14 lower); 'presents' left out as a noun because they lie around the cake."})
# ---------- 4347
w=mk([(.4,.33,.6,.67),(.36,.33,.64,.67),(.38,.36,.62,.64),(.55,.35,.45,.65),(.48,.38,.52,.62),(.6,.39,.4,.61),(.56,.42,.44,.58),
(0,.5,.47,.5),(0,.51,.48,.49),(0,.51,.48,.49),(0,.53,.47,.47),(0,.53,.47,.47),(0,.52,.47,.48),(0,.52,.47,.48),
(.2,.34,.54,.58),(.27,.36,.42,.38),(.36,.39,.31,.28),(.38,.41,.33,.24),(.38,.35,.31,.25),(.41,.34,.3,.25),
(.33,.34,.37,.2),(.3,.3,.52,.24),(.2,.31,.68,.3),(.3,.29,.54,.32),(.02,.27,.7,.34)])
k=mk([N]*7+[(.36,.37,.5,.13),(.28,.38,.62,.13),(.38,.38,.6,.13),(.36,.4,.64,.13),(.3,.4,.7,.13),(.38,.39,.62,.13),(.3,.39,.68,.13)]+[N]*11)
b=mk([(0,.3,.4,.2),(0,.29,.36,.2),(.03,.32,.35,.18)]+[N]*22)
save({"mediaId":4347,"level":"B","keyWord":"ferry","defaultVoice":"female",
"taps":[{"phrase":"to crouch in the tall grass","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to hop across the plain","target":"the kangaroos","voice":"female","keys":keys(k)},
{"phrase":"to span the harbour","target":"the bridge","voice":"female","keys":keys(b)}],
"stillS":4.5,
"nouns":[{"word":"kangaroos","x":.7,"y":.48,"voice":"female"},{"word":"a visor","x":.2,"y":.57,"voice":"female"},
{"word":"grass","x":.65,"y":.8,"voice":"female"},{"word":"the sky","x":.5,"y":.15,"voice":"female"}],
"question":"What is the woman filming?","answer":["She","is","filming","kangaroos","hopping","across","the","plain."],"answerVoice":"female",
"notes":"Key word 'ferry' is a verb and the boat itself is hardly visible (roof and rail only), so it is in no text. Boxes: on the boat the bridge runs behind the woman's head, so the bridge box is only the part left of her (split along her visor) and her outstretched arm sticks a little out of her box at the bottom left. In the grass shot the kangaroos pass right above her head: split along the horizon, so the top of her hair (about 0.05) lies above her box. The bridge is visible only 0.0-1.0 s. Two men sit behind her on the boat at 0.0-0.5 s (right edge), not targets."})
# ---------- 4349
g=mk([(.18,.28,.6,.38),(.34,.32,.4,.4),(.33,.31,.36,.54),(.34,.28,.33,.5),(.34,.3,.33,.33),(.33,.29,.37,.32),(.38,.34,.45,.3),
(.28,.29,.5,.34),(.23,.3,.55,.32),(.17,.31,.71,.31),(.1,.26,.6,.3),(.07,.24,.68,.34),(0,.21,.74,.36),(.42,.34,.22,.19),
(.42,.34,.26,.21),(.41,.36,.37,.24),(.11,.29,.52,.24),(.22,.3,.5,.28),(.17,.32,.68,.34),(.31,.3,.59,.5),(.21,.19,.67,.75),
(.18,.17,.82,.77),(.09,.2,.91,.8),(.11,.19,.89,.81),(.16,.19,.84,.81)])
tg="the man in the red cap"
save({"mediaId":4349,"level":"A","keyWord":"guard","defaultVoice":"male",
"taps":[{"phrase":"to run into the sea","target":tg,"voice":"male","keys":keys(g)},
{"phrase":"to ride a wave","target":tg,"voice":"male","keys":keys(g)},
{"phrase":"to hold a yellow board","target":tg,"voice":"male","keys":keys(g)}],
"stillS":10.0,
"nouns":[{"word":"a guard","x":.42,"y":.52,"voice":"male"},{"word":"a board","x":.72,"y":.38,"voice":"male"},
{"word":"the sea","x":.15,"y":.44,"voice":"male"},{"word":"sand","x":.82,"y":.7,"voice":"male"}],
"question":"What is the guard doing?","answer":["He","is","riding","a","wave","on","his","board."],"answerVoice":"male",
"notes":"One target for all three phrases: the only other people are two small men far back on the beach at 11.0-12.0 s (right edge); at 11.5-12.0 s they stand inside the guard's box. The guard's box always includes his board. 6.5 s is a dissolve (a faint ghost of the previous shot above him). Question is about the whole clip; he rides the wave from 3.0 to 9.0 s."})
# ---------- 4351
w=mk([(.17,.3,.83,.7),(.11,.31,.8,.69),(.23,.3,.67,.7),(.07,.31,.9,.69),(.17,.3,.63,.7),(.45,.17,.55,.52),(.42,.2,.58,.6),
(.44,.22,.56,.58),(.45,.21,.55,.44),(.45,.21,.55,.44),(.46,.2,.54,.57),(.47,.2,.53,.57),(.47,.18,.53,.46),(.47,.18,.53,.46),
(.47,.18,.53,.6),N,N,N,(0,.58,.38,.42),(0,.39,.58,.61),(0,.35,1,.65),(0,.36,1,.64),(0,.37,1,.63),(0,.38,1,.62),(0,.38,1,.62)])
m=mk([N]*5+[(0,.63,.42,.22),(0,.67,.41,.22),(.02,.67,.41,.22),(0,.61,.43,.24),(0,.61,.44,.24),(0,.67,.44,.24),(0,.67,.45,.23),
(0,.62,.44,.23),(0,.62,.44,.24),(0,.67,.42,.23)]+[N]*10)
save({"mediaId":4351,"level":"B","keyWord":"marble","defaultVoice":"female",
"taps":[{"phrase":"to lean over the balustrade","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to spread her arms wide","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to play string instruments","target":"the musicians","voice":"female","keys":keys(m)}],
"stillS":4.0,
"nouns":[{"word":"marble","x":.82,"y":.68,"voice":"female"},{"word":"musicians","x":.2,"y":.73,"voice":"female"},
{"word":"a chandelier","x":.55,"y":.19,"voice":"female"},{"word":"a trench coat","x":.75,"y":.42,"voice":"female"}],
"question":"What is the woman leaning on?","answer":["She","is","leaning","on","a","marble","balustrade."],"answerVoice":"female",
"notes":"Two targets only: the fountains (palace shot) stand right behind the woman's head and the cable cars (7.5-9.5 s) are tiny and partly behind her, so a clean third box was not possible. 7.5-8.5 s: only a sliver of her hair/coat at the bottom left edge -> off. 7.0 s is a dissolve into the mountain shot. 'marble' slot is on the polished top of the balustrade in front of her; the statue and columns are marble too, so no other noun names them. Several chandeliers hang in the hall; the slot is on the big near one."})
