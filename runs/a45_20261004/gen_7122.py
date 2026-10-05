import json,sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
horses=K([(0,.43,.75,.565),(0,.43,.87,.555),(0,.43,.98,.565),(.03,.43,1,.55),(.07,.43,1,.555),(.11,.43,1,.6),(.15,.43,1,.6),(.17,.43,1,.6)])
birds=K([(0,.565,.46,.70),(0,.555,.45,.70),(0,.565,.40,.70),(0,.55,.30,.69),(0,.555,.22,.69),None,None,None])
clouds=K([(0,0,1,.42)]*8)
c={"mediaId":7122,"level":"A","keyWord":"flat","defaultVoice":"female",
"taps":[{"phrase":"to run through the water","target":"the horses","voice":"female","keys":horses},
{"phrase":"to fly over the water","target":"the birds","voice":"female","keys":birds},
{"phrase":"to cover the sky","target":"the dark clouds","voice":"female","keys":clouds}],
"stillS":0.2,
"nouns":[{"word":"the sky","x":.5,"y":.15,"voice":"female"},{"word":"horses","x":.35,"y":.50,"voice":"female"},
{"word":"water","x":.40,"y":.72,"voice":"female"},{"word":"grass","x":.75,"y":.88,"voice":"female"}],
"question":"What are the horses doing?","answer":["They","are","running","through","the","water."],"answerVoice":"female",
"notes":"key word 'flat' (noun) not shown as a noun, left out of nouns. Birds fly low just under the horses' legs: horse box cut at the leg line, bird box below it into the water; birds gone from 2.7 s."}
json.dump(c,open('content/7122.json','w'),indent=1)
