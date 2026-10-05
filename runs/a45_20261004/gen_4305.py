import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
man=K([(0.0,0.05,0.04,0.60,0.74),(0.5,0.05,0.04,0.62,0.74),(1.0,0.07,0.04,0.60,0.76),(1.5,0.07,0.03,0.62,0.77),
(2.0,0.21,0.02,0.76,0.80),(2.5,0.28,0.01,0.72,0.83),(3.0,0.31,0.0,0.69,0.90),(3.5,0.44,0.0,0.56,0.90),
(4.0,0.47,0.01,0.53,0.96),(4.5,0.44,0.06,0.56,0.94),(5.0,0.12,0.28,0.63,0.70),(5.5,0.11,0.31,0.56,0.68),
(6.0,0.31,0.25,0.62,0.69),(6.5,0.26,0.35,0.66,0.65),(7.0,0.14,0.33,0.60,0.67),(7.5,0.15,0.24,0.60,0.76),
(8.0,0.19,0.26,0.56,0.74),(8.5,0.12,0.26,0.73,0.74),(9.0,0.09,0.24,0.62,0.76),(9.5,0.29,0.13,0.55,0.87),
(10.0,0.24,0.26,0.56,0.74),(10.5,0.19,0.26,0.70,0.74),(11.0,0.19,0.25,0.63,0.75),(11.5,0.24,0.28,0.63,0.72),
(12.0,0.26,0.28,0.58,0.68)])
boy=K([(0.0,),(0.5,),(1.0,),(1.5,),(2.0,0,0.48,0.20,0.46),(2.5,0,0.47,0.27,0.47),(3.0,0,0.49,0.30,0.51),
(3.5,0,0.47,0.43,0.53),(4.0,0.03,0.42,0.44,0.58),(4.5,0,0.39,0.43,0.61),(5.0,),(5.5,),(6.0,),(6.5,),(7.0,),(7.5,),(8.0,),(8.5,),(9.0,),
(9.5,0.11,0.52,0.18,0.19),(10.0,0,0.46,0.20,0.31),(10.5,0,0.47,0.18,0.30),(11.0,0,0.48,0.18,0.30),(11.5,0.03,0.49,0.18,0.28),(12.0,0.07,0.46,0.18,0.27)])
d={"mediaId":4305,"level":"A","keyWord":"boy","defaultVoice":"male",
"taps":[{"phrase":"to cook burgers","target":"the man","voice":"male","keys":man},
{"phrase":"to wait for a burger","target":"the boy","voice":"male","keys":boy},
{"phrase":"to catch a ball","target":"the man","voice":"male","keys":man}],
"stillS":2.5,
"nouns":[{"word":"a boy","x":0.13,"y":0.77,"voice":"male"},{"word":"a burger","x":0.52,"y":0.66,"voice":"male"},
{"word":"a cap","x":0.74,"y":0.10,"voice":"male"},{"word":"a woman","x":0.14,"y":0.36,"voice":"female"}],
"question":"What is the boy doing?","answer":["He","is","waiting","for","a","burger."],"answerVoice":"male",
"notes":"Two targets only (man, boy): the guests are a mixed crowd with nothing only one of them does. 'to catch a ball': the ball is seen in the air at 6.5 s and in his hand at 8.0 s, the catch itself falls between frames. The boy in the last shot (9.5-12.0 s) is small in the crowd on the left; I boxed him as the same boy (striped T-shirt), at 9.5 s he stands between the two men and his box is tight. Other men are in the background (red shirt at 4.0 s, blue shirt at 9.5 s): 'the man' = the one in the denim shirt."}
json.dump(d,open("content/4305.json","w"),indent=1,ensure_ascii=False)
