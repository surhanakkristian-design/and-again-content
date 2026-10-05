from lib_5658_5659_5662_5663 import write
M=[(0,.13,.82,1),(0,.14,.85,1),(0,.17,.81,1),(.11,.20,.83,1),(.24,.19,.83,1),(.23,.21,.79,1),(.27,.22,.74,1),(.31,.22,.74,1)]
F=[(.83,.25,1,1),(.86,.25,1,1),(.82,.25,1,1),(.84,.28,1,1),(.84,.26,1,1),(.80,.27,1,1),(.75,.27,1,1),(.75,.27,1,1)]
write(5662,"B","bloody","male",[
 ("to throw up his hands","the man","male",M),
 ("to hold the blender lid","the woman","female",F),
 ("to wipe his sticky face","the man","male",M)],
 3.2,[("spice jars",.20,.17,"male"),("a blender",.19,.55,"male"),("tomato sauce",.68,.44,"male"),("a chopping board",.20,.80,"male")],
 "What is the man covered in?",["He","is","covered","in","tomato","sauce."],"male",
 "Man (front, sauce on face/arm) and woman (behind his right side) overlap: boxes split at x~0.74-0.86 per frame, so the man's raised right hand at 0.2-0.7 is partly in no box. 'to throw up his hands' fits 0.2-1.7, 'to wipe his sticky face' 1.7-3.2 (he wipes with his forearm at 2.7). The woman holds the clear lid in every frame (at 0.2 only its edge). Noun 'tomato sauce' sits on his sauce-covered arm/shoulder.")
