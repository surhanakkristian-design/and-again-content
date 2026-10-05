import json
from gen_5208_5209_5210_5211_lib import build
times=json.load(open("frames/5208/info.json"))["times"]
man={0.0:(.27,.06,.73,.94),0.5:(.08,.06,.92,.94),1.0:(0,.26,1,.32),1.5:(0,.15,1,.51),2.0:(0,.08,1,.52),
 2.5:(0,.04,1,.54),3.0:(0,.06,1,.54),3.5:(.17,.13,.60,.52),4.0:(.10,.10,.84,.31),4.5:(.20,.10,.80,.28),
 5.0:(.03,.09,.94,.54),5.5:(.03,.07,.97,.56),6.0:(.04,.18,.92,.46),6.5:(.08,.16,.92,.47),7.0:(.02,.13,.96,.50),
 7.5:(.02,.10,.98,.52),8.0:(0,.06,1,.60),8.5:(0,.05,1,.62),9.0:(0,.05,1,.63)}
pan={1.0:(.46,.58,.54,.30),1.5:(.06,.66,.94,.30),2.0:(.03,.60,.97,.30),2.5:(0,.58,1,.32),3.0:(0,.60,1,.35)}
waiter={4.0:(0,.41,.50,.17),4.5:(0,.38,.78,.25)}
build(5208,"B","cuisine","male",[
 ("to gaze at his meal","the man","male",man),
 ("to land on a plastic table","the pan","male",pan),
 ("to lift a tagine lid","the waiter","male",waiter)],
 8.5,[("the skyline",.22,.22,"male"),("a candle",.84,.31,"male"),("a suit",.18,.50,"male"),("a steak",.50,.70,"male")],
 "What is the man doing?",["He","is","gazing","at","his","meal."],"male",
 "Three scenes. Waiter seen only 3.5-4.5 (at 3.5 a man in a dark suit sets the tagine down at the right edge (box OFF, may be a different person); at 4.0-4.5 the white-sleeved arm from the left lifts the lid - boxed on that arm, man box cut above it; could be two waiters). A different hand lifts a silver cloche at 6.0 - phrase says tagine lid so only the 3.5-4.5 waiter fits. Pan target only while on the street table (1.0-3.0).",times)
