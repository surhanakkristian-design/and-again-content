from gen_7249_7250_7251_7252_lib import build
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman = [(0.6,0.43,0.23,0.46),(0.6,0.43,0.24,0.47),(0.6,0.46,0.24,0.44),(0.58,0.46,0.31,0.44),
         (0.57,0.47,0.33,0.43),(0.53,0.48,0.43,0.42),(0.6,0.52,0.24,0.38),(0.6,0.52,0.25,0.38)]
crowd = [(0.0,0.56,0.58,0.19),(0.0,0.56,0.58,0.19),(0.0,0.56,0.58,0.19),(0.0,0.56,0.56,0.19),
         (0.0,0.56,0.55,0.19),(0.0,0.56,0.51,0.19),(0.0,0.58,0.58,0.19),(0.0,0.58,0.58,0.19)]
build(7249,"B","inspiration","female",
 [("to pull off a canvas cover","the woman with the braid","female",woman),
  ("to raise her arms in triumph","the woman with the braid","female",woman),
  ("to applaud the artist","the crowd","female",crowd)],
 0.2,
 [("a sculpture",0.45,0.38,"female"),("a fountain",0.17,0.76,"female"),("a toolbox",0.61,0.77,"female"),("pigeons",0.2,0.92,"female")],
 "What is the artist doing?","She is raising her arms in triumph.","female",
 "Cover is pulled off during 0.2-1.7; arms in triumph 1.7-2.7, hands to face 3.2-3.7. Crowd only starts clapping visibly from about 1.2. Crowd box stops left of the woman; a few crowd members behind her right side are not boxed.",T)
