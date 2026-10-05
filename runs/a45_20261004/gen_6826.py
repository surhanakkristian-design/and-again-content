from gen_6821_6823_6825_6826_lib import write
man   = [(0.0,0.50,0.37,0.24),(0.0,0.50,0.37,0.24),(0.0,0.50,0.40,0.26),(0.0,0.49,0.44,0.28),(0.0,0.46,0.47,0.31),(0.0,0.43,0.52,0.38),(0.0,0.40,0.58,0.46),(0.0,0.37,0.66,0.56)]
hat   = [(0.45,0.73,0.24,0.17),(0.51,0.72,0.21,0.19),(0.60,0.72,0.24,0.14),(0.64,0.77,0.30,0.14),(0.72,0.80,0.28,0.15),(0.82,0.84,0.18,0.15),None,None]
woman = [(0.74,0.43,0.24,0.16),(0.76,0.43,0.22,0.16),(0.80,0.43,0.20,0.16),(0.79,0.42,0.21,0.16),(0.80,0.40,0.20,0.16),None,None,None]
write(6826,"B","air","male",[
 ("to lounge on a bench","the man","male",man),
 ("to roll across the floor","the straw hat","male",hat),
 ("to lean over the wall","the woman","female",woman)],
 0.7,[("curtains",0.30,0.30,"male"),("a wind chime",0.72,0.22,"male"),("a straw hat",0.62,0.81,"male"),("a cat",0.13,0.87,"male")],
 "What is the man doing?","He is lounging on a blue cushion.","male",
 "Camera pushes in on the man; the hat leaves the frame after 2.7 s and the woman after 2.2 s (only a sliver of her at the right edge at 2.7 s, set off). The woman is small and far away, boxes at the 0.18 x 0.14 minimum or more. 'curtains' = the two white curtains billowing out of the doorway. Key word 'air' is not a placeable noun.")
