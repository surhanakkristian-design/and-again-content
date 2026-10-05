from gen_7878_7879_7881_7882_lib import write
A = [(.00,.39,.57,.61),(.05,.43,.55,.57),(.02,.43,.56,.57),(.04,.43,.56,.57),(.20,.43,.40,.57),(.22,.43,.38,.57),(.22,.43,.38,.57),(.22,.43,.36,.57)]
W = [None,None,None,None,(.00,.44,.20,.56),(.00,.41,.22,.59),(.00,.41,.22,.59),(.00,.40,.22,.60)]
M = [None,None,None,None,None,(.77,.15,.23,.27),(.80,.38,.20,.51),(.58,.34,.42,.40)]
write(7882, "B", "intersection", "female",
 [("to point straight up", "the arm in the blue sleeve", "female", A),
  ("to wear a lilac top", "the woman", "female", W),
  ("to lean into the frame", "the man", "male", M)],
 0.2,
 [("vapour trails", .30, .13, "female"), ("an intersection", .50, .28, "female"), ("a church spire", .61, .58, "female"), ("a picnic blanket", .76, .86, "female")],
 "What are the people pointing at?", "They are pointing at two vapour trails.", "female",
 "Everyone points at the X, so the phrases separate them: the viewer's arm points straight up, the woman (lilac top) and the man (leans in from the right, white shirt) point diagonally. From 2.2 the woman's raised arm crosses the blue arm: her box is the left strip x 0-.20/.22 (head + lilac top; most of her raised arm lies in the blue-arm box), the blue-arm box is x .20/.22-.58/.60 (hand + most of the sleeve). At 3.7 the man's box starts at .58, the blue-arm box ends there. 'to wear a lilac top' is a state: no action fits only her. 'an intersection' pill sits on the crossing point, 'vapour trails' on the upper-left trail away from it.")
