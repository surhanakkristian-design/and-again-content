from gen_7917_7919_7920_7921_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.00,.35,.63,.65),(.00,.35,.63,.65),(.00,.36,.63,.64),(.00,.36,.63,.64),(.00,.35,.64,.65),(.00,.30,.63,.70),(.00,.35,.60,.65),(.00,.35,.59,.65)]
card=[(.76,.44,.24,.56),(.76,.44,.24,.56),(.77,.44,.23,.56),(.77,.44,.23,.56),(.77,.46,.23,.54),(.77,.44,.23,.56),(.60,.44,.40,.56),(.59,.45,.41,.55)]
build(7920,"B","obsession","male",T,[
 ("to straighten a framed picture","the man in red","male",man),
 ("to frown in concentration","the man in red","male",man),
 ("to tap the man's shoulder","the woman in the cardigan","female",card)],
 0.2,[("a spirit level",.14,.40,"male"),("a globe",.19,.73,"male"),("a cabinet",.20,.88,"male"),("a window",.84,.30,"male")],
 "What is the man in red doing?","He is straightening a framed picture.","male",
 "Two phrases share the man in red (the dancers behind overlap the cardigan woman too much for a clean third box). The cardigan woman taps his shoulder only at 3.2-3.7; before that she just holds a drink at the right edge. 'to frown in concentration': he squints with a serious face. Cardigan box widens at 3.2-3.7 to her hand on his shoulder (split at x ~.60).")
