from gen_7026_7027_7028_7029_lib import write
D = [(.44,.30,.36,.52),(.44,.30,.36,.52),(.41,.30,.40,.52),(.39,.30,.43,.52),(.38,.28,.45,.54),(.38,.28,.45,.54),(.38,.28,.49,.54),(.34,.31,.47,.66)]
G = [(.80,.33,.20,.67),(.80,.33,.20,.67),(.81,.34,.19,.66),(.82,.33,.18,.67),(.83,.32,.17,.68),(.83,.31,.17,.69),(.87,.31,.13,.69),(.81,.31,.19,.69)]
write(7026, "B", "defendant", "male",
 [("to grip the brass rail", "the young man", "male", D),
  ("to bow his head slowly", "the young man", "male", D),
  ("to stand guard beside him", "the guard", "male", G)],
 2.2,
 [("a defendant", .64, .58, "male"), ("a guard", .88, .45, "male"), ("a wig", .24, .49, "male"), ("a public gallery", .22, .18, "male")],
 "What is the defendant doing?", "He is gripping the brass rail.", "male",
 "Bow is only at the end (3.2-3.7). Guard box narrow at 3.2 where he is at the edge.")
