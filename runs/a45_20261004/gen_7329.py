from gen_7328_7329_7332_7334_lib import write
# splits between woman (left) and steward
woman=[(0.45,0.31,0.54,0.26),None,(0.16,0.33,0.34,0.42),(0.17,0.32,0.33,0.44),(0.21,0.33,0.31,0.44),(0.22,0.33,0.30,0.44),(0.20,0.32,0.30,0.45),(0.17,0.30,0.33,0.48)]
player=[(0.44,0.57,0.40,0.42),(0.47,0.33,0.38,0.65),(0.50,0.33,0.20,0.65),(0.50,0.32,0.20,0.66),(0.52,0.32,0.21,0.63),(0.52,0.32,0.21,0.63),(0.50,0.32,0.20,0.66),(0.50,0.29,0.20,0.69)]
steward=[(0.09,0.44,0.30,0.40),(0.00,0.44,0.32,0.40),(0.00,0.44,0.16,0.40),(0.00,0.44,0.17,0.40),(0.00,0.44,0.21,0.40),(0.00,0.44,0.22,0.40),(0.00,0.44,0.20,0.40),(0.00,0.44,0.17,0.40)]
write(7329,"B","mama","female",[
 ("to lean over the barrier","the woman","female",woman),
 ("to grin at the woman","the player","male",player),
 ("to applaud the couple","the steward","male",steward)],
 2.7,[("a steward",0.14,0.60,"female"),("a poncho",0.37,0.48,"female"),("a photographer",0.72,0.57,"female"),("floodlights",0.78,0.13,"female")],
 "What is the woman doing?","She is leaning over the barrier.","female",
 "Key word 'mama' not placed as a noun: nothing in the picture shows she is his mother. Woman and player overlap: split along the line between them; woman hidden behind the player at 0.7 s (off). Player's face hidden at 0.2/0.7 s (grin visible from 1.2 s). Fans in the stands also clap, but only the steward faces the couple. Steward box cut where the woman's boot reaches him.")
