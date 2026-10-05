import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t]))) for t in T]
# (woman_right_edge, bald x0,x1,y0,y1, blue x0,x1,y0,y1)
R={0.0:(0.70,0.70,0.86,0.35,0.57,0.86,1.0,0.27,0.56),0.5:(0.71,0.71,0.89,0.36,0.56,0.89,1.0,0.27,0.50),
 1.0:(0.70,0.70,0.86,0.36,0.56,0.86,1.0,0.29,0.53),1.5:(0.71,0.71,0.86,0.36,0.56,0.86,1.0,0.29,0.51),
 2.0:(0.68,0.68,0.82,0.36,0.59,0.82,1.0,0.28,0.56),2.5:(0.66,0.66,0.76,0.36,0.56,0.76,1.0,0.28,0.56),
 3.0:(0.62,0.62,0.78,0.35,0.59,0.78,1.0,0.28,0.56),3.5:(0.63,0.63,0.78,0.38,0.59,0.78,1.0,0.31,0.57),
 4.0:(0.62,0.62,0.79,0.35,0.57,0.79,1.0,0.28,0.53),4.5:(0.62,0.62,0.79,0.35,0.59,0.79,1.0,0.28,0.53),
 5.0:(0.56,0.56,0.70,0.37,0.59,0.70,0.87,0.30,0.57),5.5:(0.58,0.58,0.68,0.39,0.59,0.68,0.84,0.32,0.57),
 6.0:(0.56,0.56,0.66,0.37,0.59,0.66,0.81,0.31,0.55),6.5:(0.62,0.62,0.70,0.39,0.59,0.70,0.83,0.33,0.57),
 7.0:(0.62,0.62,0.73,0.39,0.61,0.73,0.88,0.32,0.57),7.5:(0.62,0.62,0.74,0.38,0.59,0.74,0.89,0.31,0.56),
 8.0:(0.63,0.63,0.76,0.38,0.59,0.76,0.89,0.31,0.56),8.5:(0.74,0.74,0.87,0.35,0.61,0.87,1.0,0.28,0.51),
 9.0:(0.75,0.75,0.90,0.35,0.61,0.90,1.0,0.29,0.57),9.5:(0.73,0.73,0.90,0.39,0.61,0.90,1.0,0.31,0.56),
 10.0:(0.68,0.68,0.88,0.39,0.63,0.88,1.0,0.33,0.59),10.5:(0.72,0.72,0.86,0.42,0.63,0.86,1.0,0.36,0.61),
 11.0:(0.70,0.70,0.87,0.44,0.69,0.87,1.0,0.39,0.63),11.5:(0.74,0.74,0.88,0.46,0.68,0.88,1.0,0.41,0.66),
 12.0:(0.66,0.66,0.88,0.49,0.77,0.88,1.0,0.44,0.72)}
WO,BA,BL={},{},{}
for t,(we,a0,a1,ay0,ay1,b0,b1,by0,by1) in R.items():
    top=0.20 if t==12.0 else 0.0
    bot=0.88 if t>=9.5 else 0.78
    WO[t]=(0.0,top,round(we,2),round(bot-top,2))
    BA[t]=(a0,ay0,round(a1-a0,2),round(ay1-ay0,2))
    BL[t]=(b0,by0,round(b1-b0,2),round(by1-by0,2))
c={"mediaId":5174,"level":"B","keyWord":"cheerful","defaultVoice":"female",
"taps":[{"phrase":"to lift the jug high","target":"the young woman","voice":"female","keys":keys(WO)},
{"phrase":"to applaud the young woman","target":"the man in the dark shirt","voice":"male","keys":keys(BA)},
{"phrase":"to have a white beard","target":"the man in the blue shirt","voice":"male","keys":keys(BL)}],
"stillS":12.0,
"nouns":[{"word":"a jug","x":0.24,"y":0.50,"voice":"female"},{"word":"a patterned dress","x":0.30,"y":0.72,"voice":"female"},
{"word":"rice","x":0.22,"y":0.92,"voice":"female"},{"word":"salad","x":0.74,"y":0.93,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","pouring","orange","juice","into","a","glass."],"answerVoice":"female",
"notes":"One continuous shot. The young woman lifts the jug above her head 9.5-11.0 s. The bald man in the dark shirt claps (applauds) 10.5-12.0 s; the man in the blue shirt does not clap (checked on a zoom), so phrase 2 fits only him. Phrase 3 is a state: the man in the blue shirt is the only one with a white beard (the bald man is clean-shaven). The two men sit close together behind the woman's hair, so the boxes are split at the line between them and are narrow (0.10-0.20 wide) in some frames; the blue-shirt man is cut by the right edge before 5 s. An anonymous hand holding the glass (owner off screen) and a second woman in a red top (background 5-8 s) are not targets; the question says 'the young woman' because of her. Key word 'cheerful' is an adjective and is not placed."}
json.dump(c,open('content/5174.json','w'),indent=1)
