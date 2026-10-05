from w_7176_7177_7178_7182_lib import write
cand = [(.02,.33,.62,.81),(.02,.24,.56,.84),(.02,.17,.56,.90),(.04,.13,.60,.96),(.08,.12,.57,.99),(.20,.15,.64,.99),(.39,.15,.79,1.0),(.46,.18,.855,1.0)]
dress = [(.24,.19,.42,.33),None,None,None,None,None,(.24,.28,.38,.60),(.19,.26,.45,.60)]
rec = [(.74,.30,.94,.44),(.76,.30,.96,.44),(.76,.31,.96,.45),(.77,.33,.97,.47),(.80,.33,.99,.47),(.82,.34,1.0,.48),(.82,.34,1.0,.48),(.86,.33,1.0,.47)]
write(7178, "B", "go for an interview", "female",
 [("to grab the falling papers", "the woman in the blazer", "female", cand),
  ("to hold a clipboard", "the woman in the dress", "female", dress),
  ("to sit at reception", "the receptionist", "female", rec)],
 3.7,
 [("a clipboard", .37, .40, "female"), ("a blazer", .66, .52, "female"), ("a tie", .13, .57, "female")],
 "What is the woman with glasses holding?", "She is holding a clipboard.", "female",
 "Three women: candidate (cream blazer), woman in navy dress with clipboard (visible only at 0.2 top, behind the candidate's head, and 3.2-3.7; off 0.7-2.7 where she is hidden behind the candidate), receptionist (small, behind the white desk, far right). At 0.2 the dress woman's box is cut at the candidate's head (y .33). At 3.7 receptionist box is .14 wide because the candidate's shoulder is right next to her. 'a tie' = the front man's blue tie.")
