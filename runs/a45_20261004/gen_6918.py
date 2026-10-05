from gen_6916_6917_6918_6919_lib import write
woman=[(.03,.23,.47,.75),(.02,.23,.47,.75),(.02,.23,.48,.75),(.02,.23,.49,.75),(.0,.21,.45,.77),(.0,.22,.30,.70),(.0,.52,.18,.22),(.0,.52,.18,.22)]
man=[(.57,.20,.43,.80),(.58,.19,.42,.81),(.58,.20,.42,.80),(.58,.19,.42,.81),(.56,.19,.44,.81),(.46,.17,.46,.83),(.30,.11,.52,.89),(.19,.11,.55,.89)]
write(6918,"B","call in","female",[
 ("to beckon with one finger","the woman","female",woman),
 ("to hold a stack of papers","the woman","female",woman),
 ("to step through the doorway","the man in the banana suit","male",man)],
 2.2,[("sunglasses",.15,.25,"female"),("a coat stand",.39,.47,"female"),("a banana suit",.80,.52,"female"),("papers",.25,.65,"female")],
 "What is the woman doing?","She is beckoning to the next person.","female",
 "Key word 'call in' not used in the answer: 'She is calling in the next person' also allows 'calling the next person in' (two chip orders). 'Beckon' is visible at 0.2-0.7 (raised finger); 'next person' is inferred from the queue of waiting mascots and her gesture. At 3.2-3.7 only her hand and papers show at the left edge. The banana man is walking towards the camera past her; the description says into the office.")
