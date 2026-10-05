import json
T=[i*0.5 for i in range(21)]
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
mug=keys(lambda t:(0.0,0.36,1.0,0.64) if t<=1.5 else None)
pan=keys(lambda t:(0.0,0.12,1.0,0.82) if 2.0<=t<=3.0 else None)
def tw(t):
    if t<7.5: return None
    if t==7.5: return (0.08,0.06,0.90,0.94)
    return (0.0,0.05,0.98,0.95)
tower=keys(tw)
c={"mediaId":5176,"level":"A","keyWord":"a mug","defaultVoice":"female",
"taps":[
 {"phrase":"to fill with coffee","target":"the white mug","voice":"female","keys":mug},
 {"phrase":"to hold pancake batter","target":"the frying pan","voice":"female","keys":pan},
 {"phrase":"to stand in a tower","target":"the glasses","voice":"female","keys":tower}],
"stillS":0.5,
"nouns":[{"word":"a mug","x":0.50,"y":0.80,"voice":"female"},
 {"word":"coffee","x":0.64,"y":0.36,"voice":"female"},
 {"word":"a tap","x":0.45,"y":0.21,"voice":"female"}],
"question":"What is going into the mug?",
"answer":["Black","coffee","is","going","into","the","mug."],
"answerVoice":"female",
"notes":"Montage of 5 unrelated pour shots (coffee 0-1.5, batter 2-3, cocktail 3.5-5, syrup 5.5-7, champagne tower 7.5-10); targets are objects. 'a tap' = blurred kitchen faucet behind the mug."}
json.dump(c,open('content/5176.json','w'),indent=1)
