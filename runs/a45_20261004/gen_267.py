# writes content for 267, 268, 269, 270
import json
def keys(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def tap(p,t,v,d,times): return {"phrase":p,"target":t,"voice":v,"keys":keys(d,times)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
def save(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)

# ---------- 267
t=T(21)
M={0.0:(0,0,.90,.47),0.5:(0,0,.95,.52),1.0:(0,0,.90,.58),1.5:(0,0,.75,.48),2.0:(0,0,.95,.44),2.5:(0,0,.52,.72),3.0:(0,0,.48,.76),3.5:(0,0,.55,.78),
4.0:(0,0,.55,.36),4.5:(0,0,.50,.37),5.0:(0,.02,.36,.60),5.5:(0,.04,.37,.58),6.0:(0,0,.40,.50),6.5:(0,0,.41,.50),7.0:(0,.03,.52,.36),7.5:(0,.03,.47,.36),
8.0:(0,.03,.45,.37),8.5:(0,.03,.40,.57),9.0:(0,.08,.40,.72),9.5:(0,.18,.47,.68),10.0:(0,.18,.46,.62)}
R={0.0:(.25,.47,.50,.43),0.5:(.27,.52,.58,.38),1.0:(.22,.58,.55,.38),1.5:(.22,.48,.55,.50),2.0:(.12,.44,.48,.42),
4.0:(0,.36,.44,.32),4.5:(.24,.37,.42,.35),5.0:(.36,.46,.42,.42),5.5:(.37,.45,.55,.42),6.0:(.40,.27,.45,.43),6.5:(.41,.24,.52,.46),7.0:(.30,.39,.60,.42),7.5:(.33,.39,.60,.42),
8.0:(.33,.40,.62,.31),8.5:(.40,.33,.56,.45),9.0:(.45,.56,.53,.40),9.5:(.47,.52,.53,.45),10.0:(.48,.58,.50,.36)}
C={5.5:(.37,0,.20,.16),6.0:(.40,0,.22,.26),7.5:(.47,0,.20,.20),8.0:(.46,0,.20,.18),8.5:(.40,0,.27,.33),9.0:(.40,.10,.32,.45),9.5:(.47,.16,.30,.36),10.0:(.46,.17,.32,.40)}
save({"mediaId":267,"level":"A","keyWord":"engineer","defaultVoice":"male",
"taps":[tap("to build a robot","the man in black","male",M,t),tap("to pick up a cube","the robot","male",R,t),tap("to clap his hands","the man in the white coat","male",C,t)],
"stillS":4.5,
"nouns":[noun("an engineer",.25,.18,"male"),noun("a robot",.48,.52,"male"),noun("a laptop",.78,.66,"male"),noun("a box",.24,.74,"male")],
"question":"What is the engineer doing?","answer":["He","is","building","a","small","robot."],"answerVoice":"male",
"notes":"Hands of the man in black overlap the robot in 0.0-2.0, 4.0-4.5 and 7.0-8.0: boxes are split, part of his hands falls into the robot box. The man in the white coat (dark hair, glasses) claps only from 8.5; his box is on only where his face is visible (5.5, 6.0, 7.5-10.0), headless white coats earlier are off. At 8.5 the raised fist of the man in black lies inside the colleague's box. A second white coat is at the right edge at 9.0-9.5 (only an arm/hand). 'a box' = the clear plastic tray. 'an engineer' pill sits on the face of the man in black."})

# ---------- 268
W={0.0:(0,0,.47,.83),0.5:(0,0,.50,.83),1.0:(0,0,.57,.92),1.5:(0,0,.57,.92),2.0:(0,0,.56,.80),2.5:(0,0,.57,.55),3.0:(0,0,.57,.62),3.5:(0,0,.60,.70),
4.0:(0,0,.33,.60),4.5:(0,0,.30,.60),5.0:(0,0,.25,.70),5.5:(0,0,.20,.52),6.0:(0,0,.18,.40),6.5:(0,0,.18,.38),7.0:(0,0,.18,.52),7.5:(0,0,.26,.48),
8.0:(0,0,.47,.54),8.5:(0,0,.30,.52),9.0:(0,0,.40,.60),9.5:(0,.08,.40,.55),10.0:(0,.13,.36,.50)}
K={0.0:(.60,.35,.30,.17),0.5:(.62,.34,.34,.17),1.0:(.60,.33,.40,.20),1.5:(.60,.31,.38,.20),2.0:(.60,.24,.38,.18),2.5:(.62,.18,.38,.24),3.0:(.60,.17,.40,.20),3.5:(.62,.08,.38,.22),
4.0:(.58,0,.42,.18),8.0:(.55,0,.40,.17),8.5:(.78,.12,.22,.26),9.0:(.62,.27,.38,.30),9.5:(.58,.27,.42,.30),10.0:(.40,.26,.60,.33)}
save({"mediaId":268,"level":"A","keyWord":"envelope","defaultVoice":"female",
"taps":[tap("to kiss the envelope","the woman in red","female",W,t),tap("to hold a candle","the woman in red","female",W,t),tap("to sleep behind the lamp","the cat","female",K,t)],
"stillS":1.5,
"nouns":[noun("a lamp",.74,.24,"female"),noun("a cat",.78,.42,"female"),noun("a candle",.15,.67,"female"),noun("an envelope",.52,.78,"female")],
"question":"What is the woman in red kissing?","answer":["She","is","kissing","the","envelope."],"answerVoice":"female",
"notes":"The kiss is short (about 8.5-9.0 s), her mouth is at the top edge of the envelope. She holds the candle holder at 0.0-1.5 and the candle itself at 4.0-5.0. From 4.0 to 7.5 only her left hand / sleeve is in the picture (small box at the left edge). The blonde woman in green (right edge, mostly hands) is no target and has no box; the hand with the stamp at 6.0-6.5 is hers. The cat sleeps behind the lamp stem, off at 4.5-7.5 (close-ups)."})

# ---------- 269
W={0.0:(.48,.17,.52,.55),0.5:(.50,.17,.50,.57),1.0:(.52,.17,.48,.56),1.5:(.48,.17,.52,.56),2.0:(.46,.17,.54,.55),2.5:(.40,.10,.60,.58),3.0:(.30,0,.70,.72),3.5:(.28,0,.70,.70),
4.0:(.28,.02,.72,.60),4.5:(.36,.08,.64,.59),5.0:(.40,.17,.60,.55),5.5:(.40,.17,.60,.57),6.0:(.38,.17,.62,.57),6.5:(.35,.17,.65,.57),7.0:(.36,.17,.64,.56),7.5:(.49,.18,.51,.59),
8.0:(.36,.17,.64,.55),8.5:(.36,.17,.64,.55),9.0:(.36,.17,.62,.56),9.5:(.36,.17,.62,.55),10.0:(.34,.17,.62,.55)}
Cy={0.0:(.24,.22,.24,.30),0.5:(.22,.22,.27,.33),1.0:(.06,.20,.34,.38),1.5:(0,.20,.26,.38),5.0:(0,.28,.22,.36),5.5:(0,.20,.38,.46),6.0:(.14,.20,.24,.36),6.5:(.12,.20,.22,.36),7.0:(.17,.22,.19,.40),7.5:(.28,.22,.21,.38)}
H={0.0:(.40,.72,.60,.20),0.5:(.43,.74,.57,.20),1.0:(.40,.73,.60,.20),1.5:(.38,.73,.62,.20),2.0:(.36,.72,.64,.20),2.5:(.30,.68,.70,.20),3.0:(.20,.72,.72,.20),3.5:(.18,.70,.74,.20),
4.0:(.20,.62,.72,.22),4.5:(.28,.67,.72,.20),5.0:(.36,.72,.64,.26),5.5:(.40,.74,.60,.24),6.0:(.40,.74,.60,.20),6.5:(.42,.74,.58,.20),7.0:(.40,.73,.60,.22),7.5:(.36,.77,.64,.20),
8.0:(.28,.72,.70,.21),8.5:(.28,.72,.70,.21),9.0:(.24,.73,.70,.22),9.5:(.24,.72,.70,.22),10.0:(.20,.72,.72,.23)}
save({"mediaId":269,"level":"B","keyWord":"envy","defaultVoice":"female",
"taps":[tap("to gaze through the window","the woman on the bus","female",W,t),tap("to pedal past the bus","the cyclist","female",Cy,t),tap("to rest across her lap","the rusty handlebar","female",H,t)],
"stillS":6.0,
"nouns":[noun("a cyclist",.24,.31,"female"),noun("curly hair",.72,.25,"female"),noun("a sleeveless top",.74,.53,"female"),noun("a handlebar",.62,.84,"female")],
"question":"What is the curly-haired woman doing?","answer":["She","is","gazing","at","the","cyclist","with envy."],"answerVoice":"female",
"notes":"'with envy.' is one chip so the word order is fixed. The cyclist (woman in a pink top, outside, hazy behind the glass) is visible at 0.0-1.5 and 5.0-7.5; at 5.0 only the front wheel. The woman's box ends at the handlebar (her knees and the hand on the brake lever fall into the handlebar box). At 6.0-7.0 her palm on the glass touches the cyclist's box: split along the hand edge. Other passengers in the background are no targets."})

# ---------- 270
t=T(31)
G={0.0:(0,.08,.76,.92),0.5:(0,.08,.62,.92),1.0:(0,.08,.60,.92),1.5:(0,0,.51,1.0),2.0:(0,0,.41,1.0),2.5:(.76,0,.24,.55),3.0:(.72,.05,.28,.58),3.5:(.72,.05,.28,.58),
4.0:(.75,.05,.25,.50),4.5:(.67,.05,.33,.50),5.0:(.61,.15,.39,.40),5.5:(.67,0,.33,.50),6.0:(.70,0,.30,.42),6.5:(.57,0,.43,.52),7.0:(.72,0,.28,.42),7.5:(.75,0,.25,.42),
10.5:(0,.05,1.0,.87),11.0:(0,.05,1.0,.92),11.5:(0,.07,1.0,.88),12.0:(0,.05,1.0,.86),12.5:(0,.60,1.0,.40),13.0:(0,.63,1.0,.37),13.5:(0,.65,1.0,.35),14.0:(0,.66,1.0,.34),14.5:(0,.66,1.0,.34),15.0:(0,.66,1.0,.34)}
E={2.5:(.46,.24,.30,.26),3.0:(.46,.32,.26,.24),3.5:(.44,.32,.28,.24),4.0:(.48,.30,.27,.25),4.5:(.39,.32,.28,.24),5.0:(.34,.33,.27,.24),5.5:(.17,.12,.50,.42),6.0:(.25,.09,.45,.43),
6.5:(.07,.20,.50,.45),7.0:(.27,.13,.45,.42),7.5:(.30,.12,.45,.43),8.0:(0,.25,1.0,.50),8.5:(0,.24,1.0,.52),9.0:(0,.24,1.0,.53),9.5:(0,.24,1.0,.53),10.0:(0,.22,1.0,.57),
12.5:(.22,.27,.68,.33),13.0:(.14,.27,.70,.36),13.5:(.17,.28,.69,.37),14.0:(.12,.31,.70,.35),14.5:(.09,.31,.70,.35),15.0:(.07,.32,.68,.34)}
B={0.0:(.76,.20,.24,.28),0.5:(.62,.29,.26,.30),1.0:(.60,.31,.32,.32),1.5:(.51,.22,.42,.42),2.0:(.41,.13,.52,.55),2.5:(.08,0,.56,.18),3.0:(.08,0,.56,.17),3.5:(.07,0,.57,.16),
4.0:(.08,0,.58,.16),4.5:(.09,0,.57,.15),5.0:(.11,0,.56,.14),8.0:(0,0,.62,.18),8.5:(.05,0,.60,.17),9.0:(0,0,.62,.16),9.5:(0,0,.62,.16),10.0:(0,0,.62,.14)}
save({"mediaId":270,"level":"A","keyWord":"eraser","defaultVoice":"female",
"taps":[tap("to smile at the camera","the girl","female",G,t),tap("to look like a mountain","the eraser","female",E,t),tap("to show a red sun","the box","female",B,t)],
"stillS":4.5,
"nouns":[noun("a box",.38,.07,"female"),noun("a hand",.78,.22,"female"),noun("an eraser",.52,.44,"female"),noun("paper",.45,.80,"female")],
"question":"What does the eraser look like?","answer":["The","eraser","looks","like","a","little","mountain."],"answerVoice":"female",
"notes":"Present simple on purpose (a state: what it looks like). In the close-ups (2.5-7.5, 12.5-15.0) only the girl's hand is visible: her box is the part of the hand beside / below the eraser, the fingertips on the eraser fall into the eraser box. The eraser is a blue block until 7.5 and the mountain shape from 8.0. The box: in her hand at 0.0-2.0, lying behind the paper at 2.5-5.0, blurred in the background at 8.0-10.0 (weak there, at 10.0 only a strip at the top edge). 'to show a red sun' = the picture printed on the box. Eraser not visible at 0.0-2.0 (inside the box) and 10.5-12.0."})
