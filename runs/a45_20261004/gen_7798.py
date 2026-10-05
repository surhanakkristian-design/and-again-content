from gen_7796_7797_7798_7799_lib import write
M=[(0,.53,1,.47),(0,.50,1,.50),(0,.50,1,.50),(0,.50,1,.50),(0,.48,1,.52),(0,.48,1,.52),(0,.48,1,.52),(0,.48,1,.52)]
B=[(.25,.39,.18,.14),(.26,.36,.18,.14),(.27,.36,.18,.14),(.30,.33,.18,.14),(.37,.34,.18,.14),None,None,None]
write(7798,"B","delay","male",
 [("to lounge in a hammock","the man","male",M),
  ("to sip from a mug","the man","male",M),
  ("to flutter off the rake","the bird","male",B)],
 3.7,
 [("a shed",.32,.32,"male"),("string lights",.80,.27,"male"),("a wheelbarrow",.60,.49,"male"),("a pile of leaves",.22,.58,"male")],
 "What is the man doing?","He is lounging in a hammock.","male",
 "Bird is small: perched on the rake 0.2-1.2, flies off 1.7-2.2, gone after. Man box is the whole lower half (he and his legs fill it). Rake hidden later, so not a noun.")
