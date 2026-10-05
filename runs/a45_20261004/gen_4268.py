import json
T=[i*0.5 for i in range(24)]
# per time: dog, man, tv as (x0,y0,x1,y1) or None
B={
0.0:((0.31,0.20,0.83,0.80),(0,0.46,0.31,0.61),None),
0.5:((0.34,0.24,0.84,0.82),(0,0.47,0.34,0.62),None),
1.0:((0.38,0.25,0.90,0.85),(0,0.50,0.38,0.65),None),
1.5:((0.44,0.23,0.97,0.84),(0,0.49,0.44,0.63),None),
2.0:((0.48,0.22,1.0,0.80),(0,0.47,0.48,0.61),None),
2.5:((0.56,0.21,1.0,0.80),(0,0.47,0.56,0.61),None),
3.0:((0.60,0.22,1.0,0.80),(0,0.45,0.60,0.60),None),
3.5:((0.58,0.60,1.0,0.76),(0.22,0.45,1.0,0.60),None),
4.0:((0.80,0.63,1.0,0.83),(0.47,0.45,1.0,0.62),(0,0.11,0.18,0.39)),
4.5:(None,(0.74,0.46,1.0,0.64),(0,0.10,0.39,0.42)),
5.0:(None,None,(0,0.11,0.58,0.44)),
5.5:(None,None,(0,0.11,0.67,0.45)),
6.0:(None,None,(0,0.11,0.62,0.44)),
6.5:(None,(0.68,0.47,1.0,0.65),(0,0.10,0.33,0.42)),
7.0:((0.66,0.62,1.0,0.85),(0.31,0.46,1.0,0.62),None),
7.5:((0.62,0.20,1.0,0.80),(0,0.44,0.62,0.60),None),
8.0:((0.46,0.19,1.0,0.78),(0,0.45,0.46,0.59),None),
8.5:((0.40,0.18,0.92,0.76),(0,0.44,0.40,0.59),None),
9.0:((0.38,0.18,0.92,0.76),(0,0.44,0.38,0.58),None),
9.5:((0.38,0.17,0.90,0.75),(0,0.44,0.38,0.58),None),
10.0:((0.38,0.16,0.90,0.75),(0,0.38,0.38,0.57),None),
10.5:((0.38,0.16,0.90,0.75),(0,0.38,0.38,0.57),None),
11.0:((0.30,0.17,0.71,0.76),(0.71,0.19,1.0,0.47),None),
11.5:((0.17,0.17,0.71,0.76),(0.71,0.19,1.0,0.50),None),
}
def keys(i):
    out=[]
    for t in T:
        b=B[t][i]
        out.append({"t":t,"off":True} if b is None else dict(t=t,x=b[0],y=b[1],w=round(b[2]-b[0],2),h=round(b[3]-b[1],2)))
    return out
c={"mediaId":4268,"level":"A","keyWord":"fan","defaultVoice":"male","taps":[
 {"phrase":"to sit with a ball","target":"the dog","voice":"male","keys":keys(0)},
 {"phrase":"to lie on the sofa","target":"the man","voice":"male","keys":keys(1)},
 {"phrase":"to show a football match","target":"the TV","voice":"male","keys":keys(2)}],
 "stillS":6.0,
 "nouns":[{"word":"a TV","x":0.28,"y":0.27,"voice":"male"},{"word":"flowers","x":0.14,"y":0.62,"voice":"male"},{"word":"cups","x":0.60,"y":0.74,"voice":"male"},{"word":"a table","x":0.45,"y":0.88,"voice":"male"}],
 "question":"What is the dog watching?",
 "answer":["It","is","watching","a","football","match."],"answerVoice":"male",
 "notes":"The man lies behind the dog and overlaps it: up to 10.5 s his box is his legs left of the dog (his half-hidden head right of the dog falls inside the dog box); at 11.0 and 11.5 his head is clearly visible, so his box is head + shoulders on the right and the dog box is cut at x 0.71. The dog's far-left paws lie outside its box. 3.5, 4.0 and 7.0 are blurred pan frames with only legs / paws visible. Key word 'fan' (the dog as a football fan) is not a placeable noun, so it is not among the nouns. Nouns on the 6.0 s still (TV, flowers, two cups, table)."}
json.dump(c,open('content/4268.json','w'),indent=1,ensure_ascii=False)
