from w_7421_7422_7425_7427_lib import build
W=[[.21,.31,.53,.47],[.21,.30,.53,.48],[.19,.31,.55,.47],[.21,.30,.57,.48],[.20,.27,.56,.53],[.20,.27,.59,.53],[.19,.28,.62,.52],[.19,.28,.62,.52]]
T=[[.22,.78,.46,.18],[.22,.78,.50,.19],[.21,.78,.52,.20],[.21,.78,.55,.21],[.21,.80,.55,.20],[.22,.80,.55,.20],[.21,.80,.56,.20],[.21,.80,.58,.20]]
D=[[.75,.58,.22,.14],[.75,.58,.22,.14],[.75,.59,.22,.14],[.79,.59,.20,.14],[.78,.58,.21,.14],[.80,.58,.20,.14],[.82,.58,.18,.14],[.82,.57,.18,.14]]
build(7422,'B','perry','female',
 [("to tug at the wooden tap","the woman in the apron","female",W),
  ("to overflow with froth","the wooden tub","female",T),
  ("to lie on the cobbled floor","the dog","female",D)],
 0.7,
 [("an orchard",.37,.29,"female"),("a barrel",.12,.38,"female"),("perry",.40,.65,"female"),("pears",.86,.93,"female")],
 "What is happening to the wooden tub?","It is overflowing with frothy perry.","female",
 "Woman and tub overlap (her legs stand behind the tub): split horizontally at y~.78-.80, so her boots are partly in the tub box zone and cut. Dog box is to the right of her elbow/apron. Friends at the door (two women, one man) cheer as a group: not used as a target.")
