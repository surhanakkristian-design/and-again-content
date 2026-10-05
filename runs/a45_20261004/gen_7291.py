from gen_7288_7290_7291_7292_lib import write
man=[(.38,.28,.55,.53),(.41,.25,.53,.57),(.37,.25,.60,.59),(.48,.22,.45,.64),(.40,.17,.58,.69),(.45,.14,.45,.78),(.36,.16,.51,.84),(.33,.20,.57,.80)]
nav=[(.07,.31,.31,.28),(.08,.31,.32,.29),(.04,.32,.33,.30),(.08,.31,.36,.31),(.12,.33,.28,.29),(.16,.48,.29,.24),(.06,.60,.30,.22),(.03,.68,.30,.17)]
M="male"
write(7291,"B","lick",M,
 [("to grit his teeth","the man in grey",M,man),
  ("to celebrate with raised fists","the man in grey",M,man),
  ("to crawl through the mud","the man in navy",M,nav)],
 0.2,[("a canvas tent",.20,.15,M),("spectators",.82,.27,M),("a thick rope",.82,.49,M),("mud",.22,.80,M)],
 "What is the man in grey doing?","He is celebrating with raised fists.",M,
 "Key word 'lick' (= beat) is not shown as a noun and not used. Crowd not used as a target because it sits behind the main man. Boxes of the man in grey are cut at the navy man (from 2.2 s his raised left arm partly falls outside). 'to grit his teeth' = 0.2-1.7 s strain face; check the navy man does not look the same. 3.2 s: another man in a dark navy polo runs in on the left; only the navy target crawls.")
