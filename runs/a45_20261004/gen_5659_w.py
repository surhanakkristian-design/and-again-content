from lib_5658_5659_5662_5663 import write
W=[(.10,.29,.65,1),(.08,.28,.65,1),(.08,.28,.645,1),(.08,.28,.655,1),(.06,.26,.655,1),(.06,.26,.665,1),(.02,.27,.655,1),(.02,.26,.655,1)]
M=[(.66,.24,1,.60),(.66,.25,1,.62),(.655,.29,1,.62),(.665,.29,1,.62),(.665,.28,1,.62),(.675,.27,1,.62),(.665,.27,1,.62),(.665,.27,1,.62)]
write(5659,"A","block someone","female",[
 ("to put her phone down","the woman","female",W),
 ("to hold up his phone","the man outside","male",M),
 ("to take a croissant","the woman","female",W)],
 2.2,[("a woman",.35,.55,"female"),("a man",.84,.48,"male"),("a coffee",.78,.64,"female"),("a croissant",.88,.72,"female")],
 "What is the man outside doing?",["He","is","holding","up","his","phone."],"male",
 "Woman (inside, sits at the counter) and man (outside behind the glass). Their boxes are split at x~0.66 because the man's body (y 0.25-0.62) sits right above her hands; her hands with the phone/croissant (x 0.66-0.97, y 0.62-0.80) are therefore outside her box at 0.7-3.7. The croissant grab is at 3.2-3.7 only. A second phone lies on the counter, so no phone noun.")
