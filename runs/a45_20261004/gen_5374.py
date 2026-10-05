from lib_5372_5373_5374_5375 import keys, write, times
T = times(5374)
man = {0.0:(.18,.35,.58,.49),0.5:(.20,.38,.62,.52),1.0:(.18,.38,.65,.52),1.5:(.30,.42,.85,.56),2.0:(.22,.42,.84,.56),
 2.5:(.25,.40,.86,.56),3.0:(.15,.41,.75,.56),3.5:(.14,.41,.92,.56),4.0:(.03,.39,.92,.57),4.5:(0,.41,.96,.56),
 5.0:(0,.41,.98,.56),5.5:(0,.38,.98,.57),6.0:(0,.38,.84,.56),6.5:(0,.44,.88,.56),7.0:(0,.45,.86,.58),
 7.5:(0,.465,.80,.58),8.0:(0,.40,.86,.58),8.5:(.08,.40,.70,.62),9.0:(.24,.39,.73,.63),9.5:(.28,.38,.77,.63),10.0:(.33,.39,.80,.68)}
dol = {6.5:(.46,.30,.72,.44),7.0:(.45,.30,.75,.45),7.5:(.46,.30,.76,.465),
 8.5:(.70,.36,.95,.50),9.0:(.74,.36,.96,.52),9.5:(.78,.36,.98,.50),10.0:(.80,.36,.98,.50)}
km = keys(T, man)
write(5374, {"mediaId":5374,"level":"B","keyWord":"shallow","defaultVoice":"male",
 "taps":[{"phrase":"to swim front crawl","target":"the man","voice":"male","keys":km},
         {"phrase":"to wear red swimming trunks","target":"the man","voice":"male","keys":km},
         {"phrase":"to leap from the waves","target":"the dolphin","voice":"male","keys":keys(T,dol)}],
 "stillS":7.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},{"word":"a dolphin","x":0.60,"y":0.41,"voice":"male"},
          {"word":"swimming trunks","x":0.33,"y":0.50,"voice":"male"},{"word":"the sea","x":0.50,"y":0.80,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","swimming","through","shallow","water."],"answerVoice":"male",
 "notes":"One swimmer, low camera at water level. Man is small at 0.0-1.0 (far away). Dolphin leaps 6.5-7.5 just above the man's head: dolphin box ends where the man's box starts (horizontal split). 8.5-10.0 only the dolphin's fin is visible far right (small boxes padded to minimum size, split from the man's hands). Dolphin off 0-6.0 and 8.0. Sandbank and boats too small/thin for pills on the still."})
