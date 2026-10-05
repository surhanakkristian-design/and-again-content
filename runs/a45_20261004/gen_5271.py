import json
T=[round(i*0.5,1) for i in range(21)]
# per time: woman (x0,x1,top), man in blue (x0,x1,top), man in hat (x0,x1,top); bottom always 1.0
D={0.0:((0.19,0.66,0.44),(0.86,1.0,0.47),None),0.5:((0.22,0.66,0.45),(0.84,1.0,0.47),None),
1.0:((0.21,0.65,0.47),(0.82,1.0,0.42),None),1.5:((0.15,0.58,0.47),(0.62,1.0,0.40),None),
2.0:((0.03,0.44,0.48),(0.44,0.96,0.36),None),2.5:((0.0,0.37,0.47),(0.37,0.90,0.36),None),
3.0:((0.0,0.34,0.55),(0.34,0.83,0.37),None),3.5:((0.0,0.32,0.43),(0.32,0.80,0.37),None),
4.0:((0.0,0.33,0.44),(0.33,0.79,0.38),(0.82,1.0,0.46)),4.5:((0.02,0.32,0.44),(0.32,0.74,0.39),(0.74,1.0,0.36)),
5.0:((0.0,0.32,0.45),(0.32,0.70,0.40),(0.70,1.0,0.35)),5.5:((0.0,0.32,0.45),(0.32,0.67,0.39),(0.67,1.0,0.35)),
6.0:((0.0,0.32,0.42),(0.32,0.67,0.40),(0.67,1.0,0.36)),6.5:((0.0,0.33,0.45),(0.33,0.68,0.42),(0.68,1.0,0.37)),
7.0:((0.0,0.32,0.46),(0.32,0.67,0.44),(0.67,1.0,0.40)),7.5:((0.0,0.32,0.47),(0.32,0.68,0.45),(0.68,1.0,0.41)),
8.0:((0.0,0.31,0.48),(0.31,0.68,0.46),(0.68,1.0,0.41)),8.5:((0.0,0.32,0.48),(0.32,0.69,0.46),(0.69,1.0,0.41)),
9.0:((0.0,0.31,0.48),(0.31,0.67,0.47),(0.67,1.0,0.41)),9.5:((0.0,0.31,0.52),(0.31,0.70,0.46),(0.70,1.0,0.41)),
10.0:((0.0,0.32,0.52),(0.32,0.69,0.45),(0.69,1.0,0.41))}
def keys(i):
    out=[]
    for t in T:
        b=D[t][i]
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,x1,top=b; out.append({"t":t,"x":x0,"y":top,"w":round(x1-x0,2),"h":round(1.0-top,2)})
    return out
c={"mediaId":5271,"level":"A","keyWord":"cry","defaultVoice":"male",
"taps":[{"phrase":"to shout through her hands","target":"the woman","voice":"female","keys":keys(0)},
{"phrase":"to wear a blue T-shirt","target":"the man in blue","voice":"male","keys":keys(1)},
{"phrase":"to wear a big hat","target":"the man in the hat","voice":"male","keys":keys(2)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"male"},{"word":"rocks","x":0.45,"y":0.33,"voice":"male"},
{"word":"a hat","x":0.79,"y":0.45,"voice":"male"},{"word":"a woman","x":0.18,"y":0.62,"voice":"female"}],
"question":"What are the three people doing?","answer":["They","are","shouting","with","open","arms."],"answerVoice":"male",
"notes":"All three shout at 6.0-9.0, so the men get state phrases (blue T-shirt / big hat) - only the woman cups her hands round her mouth (0.0-2.0). Bodies overlap from 5.0 (arms across each other): boxes split along the body lines. Man in blue is only an arm/side at the right edge 0.0-1.0. Man in the hat: off until 4.0 (only an arm at the edge), at 4.0 his hat is cut off. Key word 'cry' (noun) is not a visible thing, not used in the texts. Mixed group -> defaultVoice male (evenId false)."}
json.dump(c,open('content/5271.json','w'),indent=1)
