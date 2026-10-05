from w_7070_7072_7073_7074_lib import *
man=[(.29,.34,.69,.50),(.36,.36,.63,.51),(.52,.30,.48,.65),(.55,.31,.44,.63),(.55,.22,.43,.65),(.54,.22,.44,.67),(.48,.28,.48,.67),(.34,.29,.52,.66)]
dogs=[(.02,.55,.26,.21),(.02,.55,.34,.27),(.00,.55,.52,.41),(.00,.55,.55,.41),(.00,.48,.55,.49),(.00,.47,.54,.51),(.00,.62,.48,.37),(.07,.57,.27,.41)]
but=[(.10,.40,.18,.14),(.09,.39,.18,.14),(.08,.40,.18,.14),(.07,.39,.18,.14),(.08,.34,.18,.14),(.06,.33,.18,.14),(.06,.40,.18,.14),(.06,.38,.18,.14)]
write(7072,"B","earl","male",[
 ("to pick up a hat box","the young man","male",man),
 ("to sniff at the hat box","the dogs","male",dogs),
 ("to watch from the steps","the butler","male",but)],
 0.2,[("a mansion",.22,.28,"male"),("an earl",.62,.50,"male"),("wolfhounds",.15,.64,"male"),("a hat box",.82,.75,"male")],
 "What is the young man doing?","He is picking up a hat box.","male",
 "the dogs are one group target (only one dog visible at 3.7 s); dog heads overlap the robe at 1.2-2.7 s so the split cuts a little of each; butler is tiny on the steps")
