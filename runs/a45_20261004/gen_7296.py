import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,boxes)]
wy=[0.06,0.06,0.07,0.10,0.21,0.21,0.21,0.21]; ww=[0.71,0.72,0.71,0.72,0.75,0.77,0.72,0.75]
woman=K([(0.0,y,w,round(1-y,2)) for y,w in zip(wy,ww)])
man=K([(0.76,0.40,0.22,0.23),(0.78,0.38,0.22,0.25),(0.78,0.38,0.21,0.26),(0.78,0.37,0.22,0.25),
       (0.79,0.34,0.21,0.26),(0.80,0.34,0.20,0.26),(0.81,0.34,0.19,0.28),(0.82,0.33,0.18,0.28)])
c=dict(mediaId=7296,level="B",keyWord="liquor",defaultVoice="female",
 taps=[dict(phrase="to pour the clear liquor",target="the woman",voice="female",keys=woman),
       dict(phrase="to sniff the foamy liquor",target="the woman",voice="female",keys=woman),
       dict(phrase="to work behind the still",target="the man",voice="male",keys=man)],
 stillS=0.7,
 nouns=[dict(word="a still",x=0.50,y=0.47,voice="female"),
        dict(word="a jug",x=0.53,y=0.67,voice="female"),
        dict(word="liquor",x=0.52,y=0.82,voice="female"),
        dict(word="an apron",x=0.18,y=0.92,voice="female")],
 question="What is the woman pouring?",
 answer=["She","is","pouring","clear","liquor","into","a","gourd."],
 answerVoice="female",
 notes="She pours 0.2-1.7 s and sniffs the cup 2.7-3.7 s. 'liquor' pill on the foamy cup gourd; 'a gourd' left out as a noun since two gourds are visible. The man in the background is small and partly behind the copper coil.")
json.dump(c,open('content/7296.json','w'),indent=1)
