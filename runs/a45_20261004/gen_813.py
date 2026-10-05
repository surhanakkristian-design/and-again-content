import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
B={0.0:(0,.15,.95,.87),0.5:(0,.13,1,.87),1.0:(0,.13,.98,.97),1.5:(.17,.13,1,.97),2.0:(.22,.16,1,.87),2.5:(.22,.18,1,.88),
3.0:(.18,.18,1,.97),3.5:(.18,.16,1,.98),4.0:(.18,.15,1,.88),4.5:(.08,.17,1,.90),5.0:(.15,.22,.98,.97),5.5:(0,.22,.92,.98),
6.0:(0,.24,.95,.87),6.5:(.03,.28,.92,.88),7.0:(.04,.15,1,.63),7.5:(0,.13,.96,.62),8.0:(0,.12,.90,.71),8.5:(0,.12,.88,.72),
9.0:(.02,.15,.88,.84),9.5:(0,.08,1,.86),10.0:(0,.07,.98,.76)}
k=keys(B)
c={"mediaId":813,"level":"A","keyWord":"turkey","defaultVoice":"male",
"taps":[{"phrase":"to show its big tail","target":"the big turkey","voice":"male","keys":k},
{"phrase":"to open its beak","target":"the big turkey","voice":"male","keys":k},
{"phrase":"to stand on the hay","target":"the big turkey","voice":"male","keys":k}],
"stillS":10.0,
"nouns":[{"word":"a turkey","x":.55,"y":.40,"voice":"male"},{"word":"a tail","x":.18,"y":.27,"voice":"male"},
{"word":"a fence","x":.85,"y":.52,"voice":"male"},{"word":"hay","x":.50,"y":.85,"voice":"male"}],
"question":"What is the turkey doing?","answer":["It","is","standing","on","the","hay."],"answerVoice":"male",
"notes":"Only the big turkey is a clear target (background birds are small, blurred and change between shots), so all three phrases use it. 'to open its beak' is visible at 2.5-3.0 s only; 'beak' may be slightly above A. Nouns 'a turkey' (chest) and 'a tail' (fan feathers, left) are on the same bird but at clearly different places."}
json.dump(c,open('content/813.json','w'),indent=1)
