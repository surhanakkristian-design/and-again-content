from gen_6831_6832_6833_6834_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.0,0.25,0.41,1.0),(0.0,0.25,0.40,1.0),(0.0,0.24,0.35,1.0),(0.0,0.22,0.34,1.0),
     (0.0,0.21,0.33,1.0),(0.0,0.21,0.32,1.0),(0.0,0.20,0.32,1.0),(0.0,0.19,0.32,1.0)]
woman=[(0.41,0.41,0.60,0.62),(0.40,0.41,0.58,0.62),(0.35,0.41,0.55,0.70),(0.34,0.40,0.73,0.66),
       (0.33,0.40,0.73,0.58),(0.32,0.40,0.52,0.56),(0.32,0.40,0.74,0.62),(0.32,0.40,0.75,0.62)]
build(6833,"B","analyst","male",[
 ("to draw a curved line","the man","male",man),
 ("to clutch some printouts","the man","male",man),
 ("to point at the curve","the woman in beige","female",woman)],
 3.2,[("glasses",0.33,0.32,"male"),("a sticky note",0.82,0.45,"male"),("a laptop",0.48,0.79,"male"),("a takeaway cup",0.33,0.88,"male")],
 "What is the man drawing?","He is drawing a curved line.","male",
 "Key word 'analyst' not placed as a noun (his job is not visible as such). The man's drawing arm crosses in front of the two women, so his box is cut at the women's line (his outstretched arm and the right part of his head fall outside); the woman in beige is half hidden behind his arm until 1.2 and her box also covers the woman in navy behind her. She points her pen at the curve from 1.7 on. Printouts in his hands (2.2-3.7) lie partly inside her box.",T)
