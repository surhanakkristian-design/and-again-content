from w_7070_7072_7073_7074_lib import *
woman=[(.50,.25,.42,.42),(.55,.25,.43,.42),(.54,.28,.40,.40),(.55,.26,.40,.40),(.60,.17,.36,.45),(.64,.18,.35,.45),(.73,.18,.27,.45),(.80,.15,.20,.30)]
dog=[(.33,.80,.34,.17),(.30,.80,.38,.18),(.30,.82,.35,.16),(.30,.82,.36,.16),(.36,.80,.36,.17),(.40,.81,.35,.17),(.45,.81,.33,.17),(.40,.84,.32,.16)]
write(7074,"B","eats","female",[
 ("to carry a steaming paella","the woman","female",woman),
 ("to adjust her straw hat","the woman","female",woman),
 ("to lie under the table","the dog","female",dog)],
 2.2,[("a straw hat",.78,.26,"female"),("paella",.48,.60,"female"),("a loaf",.42,.75,"female"),("a dog",.53,.88,"female")],
 "What is the woman doing?","She is carrying a steaming paella.","female",
 "woman carries the pan only 0.2-1.7 s, then sets it down; she is only half in frame at 3.7 s; dog lies in shadow under the table")
