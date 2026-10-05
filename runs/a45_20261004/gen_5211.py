import json
from gen_5208_5209_5210_5211_lib import build
times=json.load(open("frames/5211/info.json"))["times"]
girl={1.5:(.50,.30,.18,.36),2.0:(.07,.11,.62,.89),2.5:(.30,.13,.52,.87),3.0:(.30,.16,.68,.84),3.5:(.32,.17,.52,.83),
 4.0:(.36,.19,.64,.81),4.5:(.37,.21,.49,.68),5.0:(.34,.26,.56,.52),5.5:(.40,.20,.47,.64),6.0:(.37,.21,.42,.62),
 6.5:(.17,.26,.43,.53),7.0:(.20,.22,.64,.58),7.5:(0,.25,.66,.59),8.0:(.33,.26,.67,.60),8.5:(.21,.24,.79,.76),
 9.0:(.11,.25,.66,.68),9.5:(0,.33,1,.28),10.0:(0,.40,1,.27),10.5:(0,.40,1,.36),11.0:(0,.39,1,.38),11.5:(0,.39,1,.38),12.0:(0,.22,1,.54)}
keys={0.0:(.36,.47,.26,.35),0.5:(.40,.48,.24,.33),1.0:(.48,.49,.20,.35),1.5:(.20,.58,.16,.24)}
build(5211,"B","return","female",[
 ("to haul a suitcase inside","the girl","female",girl),
 ("to flop onto her bed","the girl","female",girl),
 ("to dangle from the lock","the keys","female",keys)],
 7.5,[("a bookcase",.80,.38,"female"),("a sofa",.17,.55,"female"),("a rug",.17,.78,"female"),("a suitcase",.64,.90,"female")],
 "What is the girl pulling behind her?",["She","is","pulling","a","suitcase","covered","in","stickers."],"female",
 "Only one person; keys are the second target (visible 0-1.5 in the lock, then the door opens and they are out of view). At 1.5 the girl is only a thin sliver in the door gap - small box. Suitcase is not a target (it overlaps her boxes in many frames).",times)
