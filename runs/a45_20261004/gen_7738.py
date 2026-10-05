from gen_7502_7529_7738_7740_lib import write
wo={0.2:(0.20,0.55,0.19,0.33),0.7:(0.20,0.55,0.21,0.36),1.2:(0.22,0.57,0.22,0.34),1.7:(0.23,0.57,0.25,0.37),
    2.2:(0.21,0.57,0.24,0.39),2.7:(0.20,0.55,0.27,0.42),3.2:(0.17,0.56,0.32,0.44),3.7:(0.19,0.55,0.30,0.45)}
man={0.2:(0.40,0.55,0.18,0.31),0.7:(0.42,0.55,0.18,0.33),1.2:(0.45,0.55,0.17,0.33),1.7:(0.49,0.54,0.16,0.37),
     2.2:(0.46,0.53,0.17,0.38),2.7:(0.48,0.52,0.16,0.40),3.2:(0.50,0.53,0.23,0.39),3.7:(0.50,0.51,0.24,0.49)}
mam={0.2:(0.58,0.46,0.36,0.23),0.7:(0.61,0.43,0.38,0.26),1.2:(0.63,0.44,0.35,0.25),1.7:(0.66,0.46,0.34,0.23),
     2.2:(0.65,0.47,0.35,0.22),2.7:(0.66,0.47,0.34,0.22),3.2:(0.74,0.46,0.26,0.24),3.7:(0.75,0.46,0.25,0.22)}
write(7738,"A","age","female",[
 ("to pull a sledge","the woman","female",wo),
 ("to have a dark beard","the man","male",man),
 ("to walk by the river","the mammoth","female",mam)],
 2.2,[("the sky",0.55,0.15,"female"),("a mammoth",0.80,0.56,"female"),("a sledge",0.15,0.76,"female"),("snow",0.70,0.86,"female")],
 "What is the woman doing?","She is pulling a sledge.","female",
 "Key word 'age' (Ice Age) is not a visible noun, so it is not used. The woman's right hand reaches back to the sledge; the man's hands are free, so 'pull a sledge' fits only her. The man's phrase is a state (beard): his only own action is smiling, but she smiles a little too at the end. Woman and man overlap; boxes split along the line between them. 'mammoth' is not an everyday A word but the only true name for the animal. defaultVoice female (mixed pair, evenId true).")
