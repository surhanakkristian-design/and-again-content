from gen_6916_6917_6918_6919_lib import write
man=[(.27,.30,.53,.62),(.29,.30,.52,.62),(.28,.35,.44,.63),(.29,.31,.48,.67),(.29,.32,.68,.58),(.29,.32,.66,.58),(.29,.32,.66,.60),(.29,.32,.66,.60)]
fire=[(.09,.53,.18,.18)]*8
write(6916,"A","cab","male",[
 ("to lean out of the train","the man","male",man),
 ("to hold a metal handle","the man","male",man),
 ("to burn very brightly","the fire","male",fire)],
 0.2,[("a cab",.40,.15,"male"),("a cap",.66,.34,"male"),("a fire",.17,.62,"male"),("smoke",.83,.20,"male")],
 "What is the man doing?","He is leaning out of the train.","male",
 "One person only; fire in the firebox is the second target. 'a cab' pill sits on the cab roof (the cab is the whole room). A second crew member is faintly visible deep in the background at 0.2-1.7 (tiny, dark); the main man is unmistakable. At 1.2-1.7 he bends in to the lever, so 'lean out' is only true at 0.2 and 2.2-3.7.")
