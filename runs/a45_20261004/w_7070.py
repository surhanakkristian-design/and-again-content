from w_7070_7072_7073_7074_lib import *
man=[(.33,.36,.63,.60),(.33,.36,.63,.60),(.33,.37,.64,.60),(.33,.37,.64,.60),(.36,.36,.60,.60),(.38,.36,.58,.60),(.43,.36,.55,.62),(.43,.37,.55,.61)]
bar=[(.06,.26,.27,.38),(.06,.26,.27,.38),(.07,.26,.26,.40),(.07,.26,.26,.40),(.09,.25,.27,.37),(.08,.25,.30,.33),(.08,.26,.35,.40),(.08,.26,.34,.38)]
write(7070,"B","drunk","male",[
 ("to sip a glass of whisky","the man","male",man),
 ("to rub his tired eyes","the man","male",man),
 ("to watch him with concern","the barmaid","female",bar)],
 0.2,[("a barmaid",.20,.42,"female"),("shot glasses",.22,.63,"male"),("peanuts",.12,.76,"male"),("a drunk",.68,.58,"male")],
 "What is the man doing?","He is sipping a glass of whisky.","male",
 "eye-rubbing only at 3.7 s; man boxes cut his left hand where it meets the barmaid's box")
