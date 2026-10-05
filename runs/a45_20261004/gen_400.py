import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
G={0.0:(0.20,0.23,0.62,0.65),0.5:(0.36,0.20,0.58,0.50),1.0:(0.15,0.21,0.85,0.57),1.5:(0,0.23,0.96,0.53),
   2.0:(0.03,0.20,0.97,0.43),2.5:(0.12,0.24,0.80,0.40),3.0:(0.25,0.27,0.60,0.37),3.5:(0.37,0.21,0.42,0.37),
   4.0:(0.28,0.17,0.63,0.41),7.0:(0.70,0.10,0.30,0.52),8.5:(0.50,0.27,0.20,0.47),9.0:(0.49,0.28,0.24,0.58),
   9.5:(0.53,0.24,0.28,0.62),10.0:(0.56,0.26,0.26,0.54)}
K={5.5:(0.17,0.28,0.58,0.48),6.0:(0.74,0.40,0.26,0.28)}
F={6.0:(0,0.14,1,0.19),6.5:(0,0.11,1,0.21),7.0:(0,0.15,0.69,0.22),7.5:(0,0.22,1,0.21),8.0:(0,0.20,1,0.22),
   8.5:(0,0.26,0.30,0.22),9.0:(0,0.28,0.29,0.24),9.5:(0,0.24,0.28,0.29),10.0:(0,0.25,0.33,0.24)}
c={"mediaId":400,"level":"A","keyWord":"ice hockey","defaultVoice":"female",
 "taps":[
  {"phrase":"to skate around a cone","target":"the girl with number 9","voice":"female","keys":keys(G)},
  {"phrase":"to wear a white helmet","target":"the goalie","voice":"female","keys":keys(K)},
  {"phrase":"to shout behind the glass","target":"the fans","voice":"female","keys":keys(F)}],
 "stillS":6.5,
 "nouns":[{"word":"fans","x":0.50,"y":0.21,"voice":"female"},{"word":"a goal","x":0.60,"y":0.38,"voice":"female"},
          {"word":"a puck","x":0.70,"y":0.59,"voice":"female"},{"word":"ice","x":0.40,"y":0.80,"voice":"female"}],
 "question":"What are the girls doing?",
 "answer":["They","are","playing","ice hockey."],
 "answerVoice":"female",
 "notes":"Hard clip, many cuts. The girl with number 9 (long braid) is clear at 0.0-4.0 and 8.5-10.0 (the right one of the two hugging players). 4.5-5.0 and 7.5-8.0 show the teammate with number 19 -> off. 7.0 (player with the stick up behind the goal): taken as number 9 because of the blond hair on her back, but it could be the teammate - please check. The goalie is only at 5.5-6.0; 'to wear a white helmet' is a state (at 6.0 the head is cut off by the picture edge). The fans = the shouting people behind the glass from 6.0; the quiet people on the bench at 2.5-4.0 and the dim figures at 5.5 are not boxed. At 7.5-8.0 the fans box runs the full width behind the teammate (not a target); at 7.0 and 8.5-10.0 only the fans LEFT of the players are boxed, the fans on the right are cut off by the girl's box. The key word is not a visible thing, so it is in the answer only ('ice hockey.' one chip). The puck at 6.5 is small (in the goal, x 0.70 y 0.59). Question in the plural because two girls of the team are shown."}
json.dump(c,open('content/400.json','w'),indent=1)
