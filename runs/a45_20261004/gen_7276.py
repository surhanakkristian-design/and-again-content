from gen_7275_7276_7277_7278_lib import *
def b(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
diver=[b(0,.17,.63,.67),b(0,.16,.64,.67),b(0,.14,.64,.68),b(0,.12,.65,.68),b(0,.08,.62,.69),b(0,.08,.56,.73),b(0,.08,.55,.79),b(0,.07,.56,.84)]
fish=[b(.64,.51,.84,.65),b(.65,.51,.85,.65),b(.65,.51,.85,.65),b(.66,.53,.86,.67),b(.63,.57,.83,.71),b(.62,.64,.82,.79),b(.58,.71,.78,.85),b(.62,.72,.82,.86)]
tape=[b(0,.70,1,.92),b(0,.70,1,.93),b(0,.75,1,.95),b(.1,.76,1,.97),b(.12,.81,1,1),b(.14,.84,.82,1),b(.15,.86,.55,1),None]
write(7276,"B","kill off","female",
 [("to reach towards the bleached coral","the diver","female",diver),
  ("to swim among the coral branches","the orange fish","female",fish),
  ("to stretch across the reef","the measuring tape","female",tape)],
 1.2,
 [("a diver",0.28,0.46,"female"),("bubbles",0.28,0.09,"female"),("coral",0.82,0.70,"female"),("a measuring tape",0.45,0.86,"female")],
 "What is the diver doing?","She is reaching towards the bleached coral.","female",
 "Fish is tiny and right next to the diver's glove: diver box ends just left of the fish. Tape only a sliver at 3.7 -> off.")
