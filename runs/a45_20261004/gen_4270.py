import json
T=[i*0.5 for i in range(25)]
# driver, duck
B={
0.0:((0.40,0.40,1,1),None),
0.5:((0.38,0.40,1,1),None),
1.0:((0.52,0.50,1,1),None),
1.5:((0.46,0.37,1,1),None),
2.0:((0.43,0.38,1,1),None),
2.5:((0.50,0.40,1,1),None),
3.0:((0.48,0.52,1,1),None),
3.5:((0.45,0.50,1,1),None),
4.0:((0.48,0.50,1,1),None),
4.5:((0.25,0.43,1,1),None),
5.0:((0.52,0.40,1,1),None),
5.5:((0.40,0.43,1,1),None),
6.0:((0.57,0.51,1,1),None),
6.5:((0.52,0.51,1,1),(0.42,0.36,0.60,0.50)),
7.0:((0.48,0.38,1,1),(0.30,0.37,0.48,0.51)),
7.5:((0.48,0.58,1,1),(0.38,0.40,0.66,0.57)),
8.0:((0.66,0.52,1,1),(0.32,0.45,0.66,0.67)),
8.5:((0.54,0.50,1,1),(0.23,0.42,0.54,0.66)),
9.0:((0.58,0.50,1,1),(0.30,0.39,0.58,0.58)),
9.5:((0.48,0.54,1,1),(0.32,0.38,0.60,0.54)),
10.0:((0.43,0.52,1,1),(0.33,0.36,0.59,0.52)),
10.5:((0.43,0.51,1,1),(0.36,0.36,0.60,0.51)),
11.0:((0.40,0.50,1,1),(0.40,0.36,0.64,0.50)),
11.5:((0.40,0.50,1,1),(0.44,0.35,0.66,0.49)),
12.0:((0.38,0.50,1,1),(0.52,0.35,0.72,0.49)),
}
def keys(i):
    out=[]
    for t in T:
        b=B[t][i]
        out.append({"t":t,"off":True} if b is None else dict(t=t,x=b[0],y=b[1],w=round(b[2]-b[0],2),h=round(b[3]-b[1],2)))
    return out
c={"mediaId":4270,"level":"B","keyWord":"slow","defaultVoice":"female","taps":[
 {"phrase":"to grip the steering wheel","target":"the driver","voice":"female","keys":keys(0)},
 {"phrase":"to slow down the kart","target":"the driver","voice":"female","keys":keys(0)},
 {"phrase":"to waddle across the track","target":"the duck","voice":"female","keys":keys(1)}],
 "stillS":10.0,
 "nouns":[{"word":"a banner","x":0.88,"y":0.31,"voice":"female"},{"word":"a duck","x":0.46,"y":0.44,"voice":"female"},{"word":"a steering wheel","x":0.74,"y":0.57,"voice":"female"},{"word":"a tyre","x":0.22,"y":0.74,"voice":"female"}],
 "question":"What is the driver doing?",
 "answer":["The","driver","is","slowing","down","for","a","duck."],"answerVoice":"female",
 "notes":"The driver is seen from behind (braided hair, an earring, striped suit); gender not identifiable, so defaultVoice follows evenId=true -> female and the texts say 'the driver'. Driver box = legs, hands on the wheel and head; from 9.5 s the duck stands right above the steering wheel, so the boxes are split horizontally there and the driver's head (right edge, above the split) is left out. Duck: a far dark dot at 6.0 s (off), keyed from 6.5 s (still tiny at 6.5 and 7.0). 'to slow down the kart' can only be seen in motion (the track stops rushing past once the duck appears)."}
json.dump(c,open('content/4270.json','w'),indent=1,ensure_ascii=False)
