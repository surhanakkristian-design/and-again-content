from gen_7758_7759_7760_7762_lib import write
dog = [(0.54,0.36,0.30,0.29),(0.56,0.36,0.36,0.29),(0.57,0.34,0.41,0.31),(0.60,0.34,0.34,0.31),
       (0.60,0.38,0.34,0.30),(0.58,0.42,0.38,0.26),(0.60,0.35,0.36,0.32),(0.60,0.33,0.38,0.34)]
cat = [(0.28,0.41,0.20,0.17),(0.27,0.41,0.20,0.17),(0.32,0.43,0.20,0.17),(0.32,0.43,0.19,0.17),
       (0.32,0.43,0.20,0.17),(0.32,0.43,0.20,0.17),(0.31,0.41,0.20,0.19),(0.30,0.40,0.20,0.20)]
rab = [(0.0,0.43,0.19,0.19),(0.03,0.43,0.19,0.18),(0.0,0.43,0.18,0.20),(0.03,0.43,0.19,0.18),
       (0.0,0.43,0.18,0.18),(0.0,0.43,0.18,0.18),(0.0,0.43,0.18,0.18),(0.0,0.43,0.18,0.18)]
write(7762, "B", "bias", "female",
 [("to sniff the sausages", "the dog", "female", dog),
  ("to raise both paws", "the cat", "female", cat),
  ("to wear a striped apron", "the rabbit", "female", rab)],
 3.2,
 [("a tent", 0.45, 0.12, "female"), ("a strawberry cake", 0.27, 0.56, "female"),
  ("a tart", 0.12, 0.64, "female"), ("a blue rosette", 0.66, 0.68, "female")],
 "What is the dog doing?", "It is sniffing the sausages.", "female",
 "cat raises its paws only at 0.2-0.7; rabbit phrase is a state (it does no distinct action); key word bias is abstract, not a noun slot")
