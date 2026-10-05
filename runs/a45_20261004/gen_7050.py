import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst):
    out=[]
    for t,b in zip(T,lst):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman=K([(0.22,0.33,0.66,0.40),(0.19,0.42,0.68,0.38),(0.19,0.55,0.68,0.30),(0.13,0.51,0.83,0.34),
         (0.14,0.43,0.76,0.41),(0.13,0.37,0.68,0.49),(0.17,0.31,0.64,0.57),(0.22,0.31,0.60,0.56)])
jog=K([(0.0,0.52,0.19,0.16),(0.0,0.52,0.18,0.16),(0.0,0.55,0.18,0.16),None,None,None,None,None])
c={"mediaId":7050,"level":"A","keyWord":"do sport","defaultVoice":"female",
 "taps":[{"phrase":"to fall on the sand","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to jump for the ball","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to run by the sea","target":"the man running","voice":"male","keys":jog}],
 "stillS":2.2,
 "nouns":[{"word":"the sky","x":0.30,"y":0.15,"voice":"female"},{"word":"a net","x":0.80,"y":0.32,"voice":"female"},
          {"word":"a woman","x":0.38,"y":0.62,"voice":"female"},{"word":"sand","x":0.50,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","doing","sport","on","the","beach."],"answerVoice":"female",
 "notes":"Jogger is small and only visible 0.2-1.2 s at the far left edge. Ball flight not used (seagulls also fly)."}
json.dump(c,open('content/7050.json','w'),indent=1)
