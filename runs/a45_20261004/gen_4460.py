from gen_4457 import write
R={ # t: woman, person, fire
0.0:((0.18,0.06,0.70,0.50),(0.71,0.10,0.97,0.45),(0.18,0.51,0.82,0.82)),
0.5:((0.18,0.06,0.70,0.50),(0.71,0.10,0.97,0.45),(0.18,0.51,0.82,0.82)),
1.0:((0.17,0.08,0.66,0.52),(0.67,0.12,0.93,0.46),(0.15,0.53,0.82,0.84)),
1.5:((0.18,0.08,0.66,0.52),(0.67,0.12,0.92,0.46),(0.15,0.53,0.82,0.84)),
2.0:((0.17,0.10,0.65,0.52),(0.66,0.12,0.92,0.46),(0.15,0.53,0.82,0.82)),
2.5:((0.17,0.11,0.65,0.52),(0.66,0.12,0.92,0.46),(0.15,0.53,0.82,0.82)),
3.0:((0.17,0.11,0.64,0.54),(0.65,0.14,0.90,0.49),(0.12,0.55,0.85,0.85)),
3.5:((0.15,0.10,0.64,0.50),(0.65,0.15,0.92,0.50),(0.12,0.51,0.88,0.85)),
4.0:((0.15,0.12,0.63,0.50),(0.64,0.17,0.90,0.50),(0.12,0.51,0.88,0.82)),
4.5:((0.17,0.12,0.64,0.54),(0.65,0.19,0.92,0.54),(0.12,0.55,0.88,0.82)),
5.0:((0.17,0.13,0.63,0.55),(0.64,0.19,0.90,0.55),(0.12,0.56,0.88,0.85)),
5.5:((0.17,0.12,0.63,0.55),(0.64,0.19,0.90,0.55),(0.12,0.56,0.88,0.85)),
6.0:((0.17,0.12,0.62,0.55),(0.63,0.19,0.88,0.52),(0.12,0.56,0.88,0.85)),
6.5:((0.14,0.09,0.82,0.55),None,(0.12,0.56,0.88,0.85)),
7.0:((0.20,0.12,0.63,0.56),(0.64,0.23,0.86,0.56),(0.12,0.57,0.85,0.92)),
7.5:((0.22,0.19,0.64,0.56),(0.65,0.26,0.86,0.56),(0.12,0.57,0.85,0.95)),
8.0:((0.20,0.25,0.62,0.59),(0.63,0.30,0.84,0.59),(0.10,0.60,0.88,0.97)),
8.5:((0.20,0.27,0.62,0.59),(0.63,0.32,0.84,0.59),(0.10,0.60,0.88,0.97)),
9.0:((0.20,0.27,0.62,0.60),(0.63,0.32,0.84,0.60),(0.10,0.61,0.88,0.98)),
9.5:((0.20,0.27,0.62,0.60),(0.63,0.32,0.84,0.60),(0.10,0.61,0.88,0.98)),
10.0:((0.22,0.22,0.63,0.58),(0.64,0.28,0.85,0.58),(0.10,0.59,0.90,0.97)),
}
Y1={4.5:0.44,5.0:0.45,5.5:0.45,6.0:0.44,7.0:0.45,7.5:0.44,8.0:0.49,8.5:0.49,9.0:0.51,9.5:0.49,10.0:0.47}
for t,y in Y1.items(): R[t]=(R[t][0],R[t][1][:3]+(y,),R[t][2])
W={t:v[0] for t,v in R.items()}; P={t:v[1] for t,v in R.items() if v[1]}; F={t:v[2] for t,v in R.items()}
c={"mediaId":4460,"level":"B","keyWord":"palm","defaultVoice":"female",
 "taps":[
  {"phrase":"to warm her palms","target":"the woman in front","voice":"female","k":"W"},
  {"phrase":"to huddle in a blanket","target":"the person in the blanket","voice":"female","k":"P"},
  {"phrase":"to light up the stones","target":"the fire","voice":"female","k":"F"}],
 "stillS":8.0,
 "nouns":[{"word":"sparks","x":0.45,"y":0.13,"voice":"female"},
          {"word":"a palm","x":0.29,"y":0.53,"voice":"female"},
          {"word":"flames","x":0.47,"y":0.70,"voice":"female"},
          {"word":"stones","x":0.55,"y":0.93,"voice":"female"}],
 "question":"What is the woman in front doing?",
 "answer":["She","is","warming","her","palms","by","the","fire."],
 "answerVoice":"female",
 "notes":"Three targets that overlap in the picture, boxes split along straight lines: the fire's box is the lower part (sticks, flame base, stone ring) below the woman's hands, so flames rising in front of her body fall in the woman's box; the person in the blanket sits right behind her and gets the strip right of her head, which cuts the woman's right arm out of her box in most frames; from 4.5 s that strip ends above her right hand, so her right palm lies in no box. The person in the blanket is dim from 5.0 s and almost fully hidden at 6.5 s (off there); gender not certain, default voice. 'a palm': two palms are held up apart, the slot is on the left one and no other noun is on the right one. She warms her palms only from about 6.5 s; before that she feeds the fire."}
write(4460,c,{"W":W,"P":P,"F":F})
