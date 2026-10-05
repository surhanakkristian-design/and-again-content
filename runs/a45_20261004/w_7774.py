from w_7772_7774_7775_7776_lib import build
W = [(0.00,0.27,0.50,0.43),(0.00,0.26,0.50,0.44),(0.00,0.25,0.50,0.45),(0.00,0.25,0.50,0.45),
     (0.00,0.23,0.50,0.47),(0.00,0.22,0.50,0.48),(0.00,0.23,0.49,0.48),(0.00,0.23,0.49,0.48)]
G = [(0.51,0.33,0.31,0.42),(0.51,0.33,0.32,0.42),(0.51,0.32,0.32,0.43),(0.51,0.32,0.32,0.43),
     (0.51,0.29,0.35,0.46),(0.51,0.28,0.38,0.48),(0.50,0.29,0.37,0.47),(0.50,0.29,0.39,0.49)]
build(7774, "A", "cent", "female",
  [("to empty a jar of coins", "the woman", "female", W),
   ("to wear a green apron", "the goat", "female", G),
   ("to smile at the goat", "the woman", "female", W)],
  2.2,
  [("a lamp", 0.65, 0.15, "female"), ("a goat", 0.67, 0.46, "female"),
   ("a cup", 0.45, 0.70, "female"), ("cents", 0.30, 0.80, "female")],
  "What is the woman doing?", "She is emptying a jar of coins.", "female",
  "Only two targets (woman, goat); woman used twice. Goat phrase is a state (apron) because its only action (holding the spatula) needs a B word. Woman smiles at the goat from about 2.2 s. Coin pile labelled 'cents' for the key word (copper coins).")
