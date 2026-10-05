from gen_7288_7290_7291_7292_lib import write
man=[(.57,.29,.43,.23),(.61,.14,.39,.36),(.64,0,.36,.30)]
cat=[(.46,.56,.32,.17),(.48,.56,.34,.17),(.50,.57,.35,.17)]
baker=[(.37,.73,.23,.27),(.35,.73,.30,.27),(.31,.74,.32,.26)]
write(7288,"B","let down","male",
 [("to let down a wicker basket","the young man","male",man),
  ("to ride down in a basket","the ginger cat","male",cat),
  ("to hold up a baguette","the baker","male",baker)],
 0.2,[("a wicker basket",.62,.76,"male"),("a balcony",.82,.55,"male"),("bunting",.22,.40,"male"),("a crowd",.15,.64,"male")],
 "What is the young man doing?","He is letting down a wicker basket.","male",
 "Short clip (3 frames). Cat box sits inside the basket; baker box starts below the basket bottom edge region to avoid overlap, so the baker's head and loaf top are partly outside it.")
