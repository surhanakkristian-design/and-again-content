import json
T=[i*0.5 for i in range(25)]
B={
0.0:((0.18,0,0.78,0.50),(0.10,0.50,1,1)),
0.5:((0.17,0,0.78,0.48),(0.12,0.48,1,1)),
1.0:((0.12,0,0.80,0.44),(0.10,0.46,1,1)),
1.5:((0,0,0.82,0.41),(0.10,0.41,1,1)),
2.0:((0,0,0.78,0.50),(0.05,0.50,1,1)),
2.5:((0.20,0,0.95,0.36),(0.10,0.38,1,1)),
3.0:((0.06,0,0.68,0.43),(0.06,0.47,1,1)),
3.5:((0,0,0.66,0.56),(0,0.60,1,1)),
4.0:((0,0,0.55,0.42),(0,0.44,1,1)),
4.5:((0,0,0.48,0.40),(0,0.44,1,1)),
5.0:((0,0,0.48,0.44),(0,0.48,1,1)),
5.5:((0.21,0.08,0.68,0.38),(0.02,0.42,1,1)),
6.0:((0.17,0.03,0.72,0.41),(0,0.44,1,1)),
6.5:((0.22,0.05,0.72,0.44),(0,0.47,1,1)),
7.0:((0.25,0.05,0.72,0.48),(0,0.51,1,1)),
7.5:((0.03,0,0.68,0.33),(0,0.36,1,1)),
8.0:((0,0,0.74,0.28),(0,0.31,1,1)),
8.5:((0,0,0.78,0.33),(0.08,0.36,1,1)),
9.0:((0,0,0.78,0.39),(0.12,0.42,1,1)),
9.5:((0.10,0,0.86,0.43),(0.18,0.47,1,1)),
10.0:((0.14,0,0.86,0.45),(0.20,0.48,1,1)),
10.5:((0.08,0,0.82,0.49),(0.20,0.52,1,1)),
11.0:((0.14,0.02,0.76,0.52),(0.22,0.55,1,1)),
11.5:((0.15,0.04,0.80,0.53),(0.22,0.58,1,1)),
12.0:((0.27,0.04,0.75,0.53),(0.20,0.57,1,1)),
}
def keys(i):
    return [dict(t=t,x=B[t][i][0],y=B[t][i][1],w=round(B[t][i][2]-B[t][i][0],2),h=round(B[t][i][3]-B[t][i][1],2)) for t in T]
c={"mediaId":4269,"level":"A","keyWord":"dry","defaultVoice":"female","taps":[
 {"phrase":"to pour water","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to wear garden gloves","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to get wet","target":"the ground","voice":"female","keys":keys(1)}],
 "stillS":12.0,
 "nouns":[{"word":"a woman","x":0.52,"y":0.20,"voice":"female"},{"word":"a jug","x":0.48,"y":0.47,"voice":"female"},{"word":"a cup","x":0.14,"y":0.60,"voice":"female"},{"word":"a plant","x":0.85,"y":0.60,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","pouring","water","on","the","dry","ground."],"answerVoice":"female",
 "notes":"Two targets only (the woman, the ground = the bed of dry earth); the cup, jug and watering can she holds move with her and lie in her box, their lower parts sometimes in the ground box. Woman and ground boxes are split at the top edge of the bed; at 2.0 s her hand reaches over the bed, the split is below the hand. 'to get wet' is 3 words incl. 'to'. 'a plant': many plants in the yard, the slot is on the big green one at the right edge of the bed; 'a cup' = the copper cup on the wall, next to the watering can."}
json.dump(c,open('content/4269.json','w'),indent=1,ensure_ascii=False)
