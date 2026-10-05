from gen_4962_4963_4964_4965 import write
b={0.0:(0,0.12,0.60,0.88),0.5:(0,0.12,0.60,0.88),1.0:(0,0.17,0.66,0.83),1.5:(0,0.17,0.74,0.83),2.0:(0,0.19,0.77,0.81),
 2.5:(0,0.35,0.87,0.65),3.0:(0,0.25,0.90,0.75),3.5:(0.08,0.16,0.70,0.84),4.0:(0,0.12,0.80,0.88),4.5:(0,0.14,0.84,0.86),
 5.0:(0,0.16,0.87,0.84),5.5:(0,0.26,0.84,0.74),6.0:(0,0.27,0.87,0.73),6.5:(0.03,0.16,0.80,0.84),7.0:(0.06,0.09,0.52,0.91),
 7.5:(0,0.11,0.60,0.89),8.0:(0,0.11,0.55,0.89),8.5:(0,0.13,0.64,0.87),9.0:(0,0.15,0.68,0.85)}
write(4965,"A","bathroom","male",
 [("to brush his teeth","the boy","male",b),("to wash his hands","the boy","male",b),("to dry his face","the boy","male",b)],
 0.0,[("a window",0.18,0.12,"male"),("a toothbrush",0.38,0.31,"male"),("a tap",0.88,0.70,"male"),("a sink",0.55,0.85,"male")],
 "What is the boy brushing?",["He","is","brushing","his","teeth."],"male",
 "only one person: all three phrases on the boy; key word bathroom is the whole room, not placed as a noun")
