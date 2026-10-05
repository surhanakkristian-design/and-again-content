from gen_7328_7329_7332_7334_lib import write
man=[(0.22,0.50,0.18,0.26)]*8
pink=[(0.74,0.49,0.18,0.21),(0.75,0.49,0.18,0.21),(0.76,0.48,0.18,0.22),(0.77,0.48,0.18,0.22),(0.76,0.47,0.18,0.22),(0.77,0.47,0.18,0.22),(0.76,0.46,0.18,0.22),(0.77,0.45,0.18,0.23)]
dog=[(0.67,0.70,0.18,0.16),(0.70,0.70,0.18,0.18),(0.69,0.71,0.21,0.20),(0.76,0.72,0.21,0.20),(0.80,0.74,0.20,0.24),(0.80,0.79,0.20,0.19),None,None]
write(7328,"A","mall","female",[
 ("to run next to the sheep","the dog","female",dog),
 ("to walk with a stick","the man with the stick","male",man),
 ("to run in a pink top","the woman in pink","female",pink)],
 0.2,[("sheep",0.45,0.62,"female"),("a dog",0.76,0.78,"female"),("a lamp",0.13,0.41,"female"),("trees",0.78,0.15,"female")],
 "What is the dog doing?","The dog is running next to the sheep.","female",
 "Key word 'mall' (the promenade/avenue) not used as a noun: for A learners 'mall' = shopping centre, would mislead. Dog leaves frame at 3.2 s. Man in yellow also runs, so pink-top phrase is specific.")
