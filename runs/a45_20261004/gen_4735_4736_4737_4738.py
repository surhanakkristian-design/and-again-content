import json
def keys(d, n):
    out=[]
    for i in range(n):
        t=i*0.5
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)

# ---- 4735
w={0.0:(.50,.20,.50,.80),0.5:(.42,.18,.58,.82),1.0:(.48,.18,.52,.82),1.5:(.48,.17,.52,.83),2.0:(.38,.14,.62,.86),
   2.5:(.52,.33,.28,.57),4.5:(.48,.31,.20,.32),5.0:(.76,.31,.20,.34),5.5:(0,.28,.24,.72),6.0:(0,.44,.22,.54),
   6.5:(0,.18,.50,.82),7.0:(0,.21,.78,.79),7.5:(0,.22,.94,.78),8.0:(.10,.23,.80,.77),8.5:(0,.25,.86,.75),9.0:(.05,.29,.71,.71)}
m={0.0:(0,0,.14,1),0.5:(0,0,.20,1),1.0:(0,0,.16,1),1.5:(0,0,.14,1),2.5:(.24,.22,.28,.58),3.0:(.15,.33,.70,.60),
   4.5:(.20,.26,.18,.40),5.0:(.48,.27,.19,.38)}
s={0.0:(.14,.15,.36,.75),0.5:(.20,.10,.22,.68),1.0:(.16,.15,.32,.73),1.5:(.14,.09,.34,.64),2.0:(0,.08,.36,.70),
   4.5:(.38,.30,.10,.24),5.0:(.67,.31,.09,.22)}
save({"mediaId":4735,"level":"B","keyWord":"punch","defaultVoice":"female",
 "taps":[
  {"phrase":"to wipe her forehead","target":"the woman","voice":"female","keys":keys(w,19)},
  {"phrase":"to grab her from behind","target":"the man","voice":"male","keys":keys(m,19)},
  {"phrase":"to absorb every punch","target":"the black shield","voice":"female","keys":keys(s,19)}],
 "stillS":1.5,
 "nouns":[{"word":"a shield","x":.32,"y":.20,"voice":"female"},{"word":"a glove","x":.28,"y":.42,"voice":"female"},
          {"word":"a braid","x":.84,"y":.38,"voice":"female"},{"word":"mud","x":.40,"y":.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","throwing","punches","at","a","shield."],
 "answerVoice":"female",
 "notes":"Many cuts. The woman = the soldier with the braids who punches the shield and stands close to camera at the end (wipes her forehead with her arm 8.0-9.0 s). The man = her partner who holds the shield (0.0-1.5, 4.5, 5.0 s) and grabs her from behind at 2.5 s. 0.0-1.5 s: man, shield and woman overlap, boxes split by vertical lines (the woman's punching arm lies in the shield box). 2.5 s: split at x .52, the man's head is half in his box. 3.0 s: only the man boxed (his face is visible, the woman is hidden on his back); 3.5 s (legs in the air) and 4.0 s (a woman sitting on the mat, another standing: not sure which is she) both off. 5.5 s: the figure at the right edge is not boxed (identity unclear). 4.5/5.0 s: small boxes, the shield only .10 wide between the two. Background pairs do the same drill but are tiny; phrases chosen to be unique to the main pair. Key word 'punch' is not a placeable thing; it is in a phrase and the answer."})

# ---- 4736
w={0.0:(.02,.28,.56,.72),0.5:(0,.28,.58,.72),1.0:(0,.28,.63,.72),1.5:(0,.29,.66,.71),2.0:(0,.26,.72,.74),2.5:(0,.19,.52,.81),
   3.0:(0,.20,.35,.80),3.5:(0,.23,.24,.77),4.0:(0,.23,.25,.77),4.5:(0,.28,.19,.72),5.0:(0,.42,.18,.58),
   6.5:(0,.18,.25,.82),7.0:(0,.27,.57,.73),7.5:(0,.29,.62,.71),8.0:(0,.29,.53,.71),8.5:(0,.29,.60,.71),
   9.0:(.12,.28,.56,.72),9.5:(.07,.24,.62,.76),10.0:(.14,.25,.60,.75)}
s={0.0:(.58,.20,.42,.68),0.5:(.58,.15,.42,.68),1.0:(.63,.17,.37,.78),1.5:(.66,.16,.34,.80),2.0:(.72,.13,.28,.71),
   2.5:(.74,.29,.26,.65),3.0:(.65,.33,.35,.65),3.5:(.74,.33,.26,.60),4.0:(.86,.38,.14,.20),4.5:(.84,.39,.16,.19),
   5.0:(.79,.36,.21,.34),5.5:(.72,.41,.28,.42),6.0:(.80,.13,.20,.71),6.5:(.77,.16,.23,.74),7.0:(.59,.22,.37,.72),
   7.5:(.63,.24,.35,.70),8.0:(.53,.21,.43,.64),8.5:(.60,.21,.40,.66),9.0:(.82,.28,.18,.70),9.5:(.82,.28,.18,.72)}
g={5.5:(.35,.55,.37,.18),6.0:(.38,.50,.42,.23),6.5:(.44,.46,.33,.27)}
save({"mediaId":4736,"level":"B","keyWord":"army","defaultVoice":"female",
 "taps":[
  {"phrase":"to punch a padded shield","target":"the woman in front","voice":"female","keys":keys(w,21)},
  {"phrase":"to absorb the blows","target":"the black shield","voice":"female","keys":keys(s,21)},
  {"phrase":"to land on the mats","target":"the woman on the ground","voice":"female","keys":keys(g,21)}],
 "stillS":2.0,
 "nouns":[{"word":"a shield","x":.85,"y":.42,"voice":"female"},{"word":"a glove","x":.66,"y":.57,"voice":"female"},
          {"word":"mats","x":.60,"y":.71,"voice":"female"},{"word":"the sky","x":.35,"y":.12,"voice":"female"}],
 "question":"What is the woman in front doing?",
 "answer":["She","is","punching","a","padded","shield."],
 "answerVoice":"female",
 "notes":"The woman in front = the soldier with the bun and long braid close to camera. The black shield = the one held at the right edge by a partner who is almost out of frame (not a target). The woman on the ground = the soldier thrown onto the mats in the background; boxed only at 5.5-6.5 s where she lies / sits on the mats. Before that she is one of two grappling soldiers who cannot be told apart, and the crouching woman at 7.0-7.5 s may or may not be her: all off. 5.0 s: only the front woman's glove at the left edge. 6.0 s: front woman out of frame. 10.0 s: shield out of frame. Key word 'army' is not a placeable noun (the scene shows it as a whole) and is not used in the texts. Background soldiers wrestle rather than punch shields."})

# ---- 4737
w={0.0:(0,0,.28,1),0.5:(0,0,.30,1),1.0:(0,0,.32,1),1.5:(0,0,.35,1),2.0:(0,0,.35,1),2.5:(0,0,.40,1),3.0:(0,0,.64,.48),
   3.5:(.08,.08,.78,.70),4.0:(.05,.07,.80,.80),4.5:(.05,.07,.80,.80),5.0:(0,.02,.78,.93),5.5:(0,.02,.80,.93),
   6.0:(0,.01,.78,.86),6.5:(0,.01,.80,.86),7.0:(.42,.02,.30,.50),7.5:(.50,0,.32,.44),8.0:(.50,0,.33,.44),
   8.5:(.53,.02,.31,.45),9.0:(.52,.06,.31,.46),9.5:(.56,.12,.30,.44),10.0:(.55,.17,.29,.42),10.5:(.57,.21,.28,.41),
   11.0:(.54,.24,.28,.43),11.5:(.57,.26,.28,.41),12.0:(.59,.26,.31,.42)}
gl={0.0:(.28,.43,.46,.44),0.5:(.30,.40,.50,.46),1.0:(.32,.37,.46,.47),1.5:(.35,.38,.47,.47),2.0:(.35,.36,.49,.49),
    2.5:(.40,.42,.50,.50),3.0:(.36,.49,.50,.50)}
tp={0.0:(.50,0,.50,.20),0.5:(.48,0,.30,.17),1.0:(.50,0,.50,.20),1.5:(.52,0,.48,.22),2.0:(.55,0,.45,.21),
    2.5:(.60,0,.40,.26),3.0:(.66,0,.34,.44)}
save({"mediaId":4737,"level":"B","keyWord":"jug","defaultVoice":"female",
 "taps":[
  {"phrase":"to tip a metal jug","target":"the woman","voice":"female","keys":keys(w,25)},
  {"phrase":"to overflow with water","target":"the glass","voice":"female","keys":keys(gl,25)},
  {"phrase":"to drip slowly","target":"the tap above the glass","voice":"female","keys":keys(tp,25)}],
 "stillS":5.5,
 "nouns":[{"word":"a jug","x":.22,"y":.42,"voice":"female"},{"word":"a bucket","x":.70,"y":.86,"voice":"female"},
          {"word":"a tap","x":.86,"y":.46,"voice":"female"},{"word":"a palm tree","x":.87,"y":.08,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","pouring","water","from","a","jug."],
 "answerVoice":"female",
 "notes":"The woman = the main woman in every shot (0.0-3.0 s only her left part: her hand around the glass lies in the glass box; at 3.0 s her box is the top part with her face). The glass brims over at 2.5-3.0 s. The tap above the glass = the brass tap of the first shot, running until 2.0 s and dripping at 2.5-3.0 s; the taps on the post at 3.5-6.5 s are a different-looking fitting and are NOT boxed (verifier: decide whether they should be). The grey vessel is called a jug by the packet (key word): at 3.5-4.5 s it has a spout like a watering can, at 5.0-6.5 s it looks like a pail; still 5.5 s chosen so that the black bucket is unmistakable and 'a jug' is the grey vessel in her hands. Two taps stand close together at 5.5 s, the slot is on the right one. The friends on the loungers are not targets (both men raise an arm, nothing unique)."})

# ---- 4738
w={0.0:(0,.06,.95,.90),0.5:(0,.11,1,.89),1.0:(.05,.26,.78,.66),1.5:(.18,.18,.70,.80),2.0:(0,.02,1,.82),2.5:(.08,.17,.92,.70),
   3.0:(0,.35,.75,.63),3.5:(0,.27,.78,.60),4.0:(.12,.08,.88,.92),4.5:(.05,0,.95,.76),5.0:(.14,0,.78,.82),5.5:(.40,.14,.60,.86),
   6.5:(.03,.11,.84,.76),7.0:(0,.21,.87,.79),7.5:(0,.11,.87,.89),8.0:(0,.03,.97,.94),8.5:(0,.02,1,.98),9.0:(0,.06,1,.94),
   9.5:(0,.09,1,.91),10.0:(0,.08,1,.92),10.5:(0,.10,1,.90),11.0:(0,.38,.97,.62),11.5:(0,.33,1,.67),12.0:(0,.27,1,.73)}
k=keys(w,25)
save({"mediaId":4738,"level":"A","keyWord":"everywhere","defaultVoice":"female",
 "taps":[
  {"phrase":"to look under the bed","target":"the woman","voice":"female","keys":k},
  {"phrase":"to hold two shoes","target":"the woman","voice":"female","keys":k},
  {"phrase":"to find her passport","target":"the woman","voice":"female","keys":k}],
 "stillS":8.5,
 "nouns":[{"word":"a passport","x":.56,"y":.54,"voice":"female"},{"word":"a bed","x":.89,"y":.44,"voice":"female"},
          {"word":"a curtain","x":.25,"y":.14,"voice":"female"},{"word":"clothes","x":.84,"y":.63,"voice":"female"}],
 "question":"Where are the clothes?",
 "answer":["The","clothes","are","everywhere."],
 "answerVoice":"female",
 "notes":"Only one possible target (the woman), so all three phrases use her. 6.0 s is the empty room: off. She looks under the mattress / bed frame at 2.5-3.5 and 6.5-7.0 s, holds two boots at 4.0 s, picks the passport up at 8.0 s. Key word 'everywhere' is an adverb: it is the last word of the answer. Still 8.5 s: 'clothes' slot on the pile at the right, more clothes lie at the left edge; the window frame behind her head is not a noun."})
