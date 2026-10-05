import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(0.0,0.12,0.66,0.47),0.5:(0.0,0.12,0.66,0.47),1.0:(0.0,0.27,1.0,0.73),1.5:(0.0,0.25,0.36,0.75),4.0:(0.0,0.10,0.33,0.55),
 6.0:(0.08,0.0,0.40,0.21),6.5:(0.07,0.14,0.30,0.44),7.0:(0.07,0.16,0.26,0.42),7.5:(0.08,0.16,0.26,0.42),
 8.0:(0.27,0.28,0.23,0.35),8.5:(0.29,0.28,0.23,0.33),9.0:(0.28,0.29,0.22,0.33),9.5:(0.28,0.29,0.22,0.31),10.0:(0.27,0.29,0.22,0.31)}
woman={0.0:(0.05,0.60,0.72,0.40),0.5:(0.0,0.60,0.78,0.40),2.0:(0.0,0.27,1.0,0.73),2.5:(0.0,0.27,1.0,0.73),
 6.5:(0.58,0.30,0.32,0.38),7.0:(0.53,0.32,0.37,0.34),7.5:(0.55,0.31,0.37,0.35),
 8.0:(0.50,0.31,0.19,0.32),8.5:(0.52,0.31,0.19,0.30),9.0:(0.50,0.32,0.19,0.30),9.5:(0.50,0.32,0.19,0.28),10.0:(0.49,0.31,0.19,0.29)}
ball={3.0:(0.0,0.23,1.0,0.77),3.5:(0.13,0.44,0.87,0.56),6.0:(0.0,0.22,1.0,0.78),6.5:(0.0,0.69,1.0,0.31),7.0:(0.0,0.67,1.0,0.33),7.5:(0.0,0.67,1.0,0.33),
 8.0:(0.03,0.64,0.94,0.36),8.5:(0.08,0.62,0.84,0.38),9.0:(0.08,0.63,0.82,0.37),9.5:(0.08,0.61,0.80,0.39),10.0:(0.08,0.61,0.78,0.39)}
c={"mediaId":4615,"level":"A","keyWord":"colorful","defaultVoice":"male",
"taps":[
 {"phrase":"to blow up a balloon","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to hang up a paper chain","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to lie on the floor","target":"the balloons","voice":"male","keys":keys(ball)}],
"stillS":8.0,
"nouns":[{"word":"a ladder","x":0.22,"y":0.53,"voice":"male"},{"word":"a sofa","x":0.80,"y":0.58,"voice":"male"},
 {"word":"balloons","x":0.50,"y":0.82,"voice":"male"},{"word":"lights","x":0.76,"y":0.40,"voice":"male"}],
"question":"What is on the floor?",
"answer":["There","are","colorful","balloons","on","the","floor."],
"answerVoice":"male",
"notes":"Clip has many cuts. The man is boxed by his hands/arm (patterned sleeve) at 1.0, 1.5, 4.0 and by his legs on the ladder at 6.0. 'the balloons' = the loose balloons (sofa at 3.0-3.5, floor from 6.0); the single balloon the woman blows up / holds is left inside her box (balloons off at 0.0-2.5). defaultVoice male: man + woman, odd id."}
json.dump(c,open('content/4615.json','w'),indent=1)
