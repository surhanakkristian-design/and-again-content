from gen_5156_5157_5158_5161_lib import build
T = [i*0.5 for i in range(25)]
man = {0.0:(0.15,0.4,0.6,0.6),0.5:(0.17,0.39,0.6,0.61),1.0:(0.2,0.42,0.5,0.58),1.5:(0.17,0.42,0.53,0.58),
 2.0:(0.14,0.43,0.58,0.57),2.5:(0.17,0.42,0.55,0.58),3.0:(0.2,0.43,0.56,0.57),
 3.5:(0.08,0.46,0.6,0.54),4.0:(0.04,0.44,0.58,0.56),4.5:(0.04,0.44,0.58,0.56),5.0:(0.02,0.46,0.58,0.54),
 5.5:(0.03,0.45,0.57,0.55),6.0:(0.03,0.44,0.57,0.56),6.5:(0.05,0.05,0.95,0.58),7.0:(0,0.05,1.0,0.62),
 7.5:(0,0.05,1.0,0.63),8.0:(0,0,1.0,0.69),8.5:(0,0,1.0,0.69),9.0:(0,0.03,1.0,0.67),9.5:(0,0.03,1.0,0.67),
 10.0:(0,0.02,1.0,0.7),10.5:(0,0.02,1.0,0.7),11.0:(0,0.02,1.0,0.69),11.5:(0,0.02,1.0,0.69),12.0:(0,0.04,1.0,0.71)}
pig = {0.0:(0.75,0.55,0.25,0.35),0.5:(0.77,0.55,0.23,0.35),1.0:(0.7,0.58,0.3,0.32),1.5:(0.7,0.55,0.3,0.32),
 2.0:(0.72,0.55,0.28,0.2),2.5:(0.72,0.57,0.28,0.16),3.0:(0,0.53,0.2,0.15)}
build(5161,"B","cathedral","male",[
 ("to lean on a railing","the young man","male",man),
 ("to scatter across the square","the pigeons","male",pig),
 ("to taste a fried dumpling","the young man","male",man)],
 2.0,[("a cathedral",0.47,0.25,"male"),("pigeons",0.12,0.6,"male"),("a backpack",0.22,0.75,"male"),("cobblestones",0.82,0.86,"male")],
 "What is the young man eating?",["He","is","eating","fried","dumplings."],"male",
 "Pigeons are on both sides of him in 0-3 s; their box covers the bigger flock beside him and is cut where his outstretched arm crosses it. Man box at 0-3 s excludes the tip of his outstretched arm. In the restaurant shot the plate (bottom) is outside his box.",T)
