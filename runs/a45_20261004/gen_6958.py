from gen_6957_6958_6959_6960_lib import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
case=[(0.12,0.25,0.38,0.19),(0.13,0.25,0.44,0.19),(0.17,0.25,0.38,0.19),(0.22,0.25,0.39,0.19),(0.29,0.25,0.41,0.20),(0.36,0.25,0.43,0.20),(0.43,0.24,0.45,0.23),(0.51,0.24,0.49,0.23)]
water=[(0.12,0.66,0.88,0.34),(0.12,0.66,0.88,0.34),(0.10,0.64,0.90,0.36),(0.12,0.64,0.88,0.36),(0.14,0.62,0.86,0.38),(0.22,0.64,0.78,0.36),(0.30,0.66,0.70,0.34),(0.36,0.66,0.64,0.34)]
bag=[None,None,None,None,(0.0,0.41,0.18,0.18),(0.0,0.42,0.20,0.19),(0.05,0.42,0.20,0.19),(0.11,0.42,0.21,0.18)]
write(6958,"B","coffee shop","female",[
 ("to display fresh croissants","the glass case","female",case),
 ("to flood the tiled floor","the water","female",water),
 ("to stand on the windowsill","the bag of coffee","female",bag)],
 1.2,[("a pendant lamp",0.40,0.09,"female"),("an espresso machine",0.78,0.30,"female"),("croissants",0.33,0.33,"female"),("floodwater",0.30,0.90,"female")],
 "What is happening in the coffee shop?","Water is flooding the empty coffee shop.","female",
 "no people; camera pans left; bag of coffee only visible from 2.2 s; two copper lamps at 1.2 s, pill on the left one; water box = inside floor only",T)
