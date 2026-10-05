from lib_5304_5306_5307_5308 import write
A = {0.0:(0,0,.75,1),0.5:(0,.22,1,.76),1.0:(0,.27,.9,.73),1.5:(0,.25,.9,.75),2.0:(0,.26,.86,.7)}
B = {3.5:(.6,.4,.4,.5),4.0:(.22,.33,.44,.56),4.5:(.38,.36,.4,.45)}
G = {5.0:(.6,.42,.4,.38),5.5:(.48,.42,.5,.4),6.0:(.4,.48,.36,.52),6.5:(.48,.5,.32,.5),7.0:(.5,.65,.33,.35),7.5:(.6,.57,.35,.43),
 8.0:(.57,.58,.42,.42),8.5:(.57,.58,.4,.42),9.0:(.55,.58,.38,.42),9.5:(.57,.6,.4,.4),10.0:(.52,.54,.4,.46),10.5:(.53,.53,.42,.47),
 11.0:(.52,.52,.37,.48),11.5:(.52,.52,.35,.48),12.0:(.5,.5,.28,.46)}
write(5306,"A","comfortable","male",[
 ("to sit in a brown armchair","the man in the denim shirt","male",A),
 ("to sit on the woman's lap","the little boy","male",B),
 ("to raise his fist","the man in the grey T-shirt","male",G)],
 4.5,[("photos",.6,.12,"male"),("a man",.3,.42,"male"),("a boy",.52,.52,"male"),("a pillow",.9,.42,"male")],
 "What is the little boy doing?","He is sitting on the woman's lap.","male",
 "Three shots: armchair man (denim shirt) 0-2 s, couple + boy on the patterned sofa 2.5-4.5 s, crowd on the grey sectional 5-12 s. The denim-shirt man is off after the cut (the sofa man wears a dark T-shirt). Boy runs in at 3.5, climbs on at 4.0 and sits on the woman's lap at 4.5 (lap only clearly at 4.5). Grey T-shirt man jumps on at 5.0 and raises his fist 7.5-9.5; tracked to the end.")
