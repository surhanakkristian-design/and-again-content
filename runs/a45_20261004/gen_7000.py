from gen_6997_6998_6999_7000_lib import build
cr=[(.21,.50,.45,.23),(.21,.50,.47,.23),(.19,.51,.47,.24),(.19,.51,.49,.24),(.17,.50,.51,.24),(.21,.50,.52,.23),(.18,.51,.56,.23),(.23,.47,.56,.26)]
moon=[(.18,0,.19,.15),(.17,0,.19,.14),(.17,0,.19,.14),(.16,0,.19,.14),(.16,0,.19,.14),(.16,0,.19,.14),(.16,0,.19,.14),(.16,0,.19,.14)]
moths=[(.70,.06,.29,.40)]*7+[(.70,.06,.29,.39)]
build(7000,"A","cricket","female",[
 ("to open its wings","the cricket","female",cr),
 ("to shine in the night sky","the moon","female",moon),
 ("to fly around the lamp","the moths","female",moths)],
 0.2,[("the moon",.28,.07,"female"),("a lamp",.89,.24,"female"),("chairs",.20,.46,"female"),("a cricket",.42,.62,"female")],
 "What is the cricket doing?","It is opening its wings.","female",
 "Cricket box leaves out the thin antenna tips (they reach into the moth area). The moths are small and several (group target, box around the lamp shade area). Moon small and at the top edge, partly cut from 2.7. Wings flutter at 0.2-1.2 and spread wide at 3.7.")
