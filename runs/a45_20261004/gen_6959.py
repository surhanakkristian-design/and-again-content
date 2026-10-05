from gen_6957_6958_6959_6960_lib import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.15,0.32,0.83,0.55),(0.08,0.29,0.74,0.71),(0.03,0.32,0.79,0.68),(0.06,0.25,0.81,0.75),(0.06,0.30,0.63,0.70),(0.06,0.26,0.88,0.60),(0.0,0.27,0.72,0.73),(0.0,0.26,0.77,0.74)]
boot=[None,None,None,None,(0.70,0.78,0.18,0.15),(0.62,0.86,0.33,0.14),(0.73,0.85,0.25,0.14),(0.78,0.84,0.21,0.15)]
write(6959,"A","collect","male",[
 ("to carry a lot of things","the man","male",man),
 ("to put on a hat","the man","male",man),
 ("to fall into the water","the black boot","male",boot)],
 3.7,[("trees",0.70,0.18,"male"),("a hat",0.60,0.32,"male"),("a tent",0.10,0.38,"male"),("a kettle",0.38,0.79,"male")],
 "What is the man carrying?","He is carrying a lot of things.","male",
 "friends in background too small/far for a target; man and boot boxes split where the falling boot is next to him (2.2-3.7), so the man's box loses some edge (hat brim / feet)",T)
