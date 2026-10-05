import json
T=[i*0.5 for i in range(21)]
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def woman(t):
    if t<=1.5: return (0.0,0.0,1.0,0.66)
    if t<=5.5: return (0.0,0.0,1.0,0.48)
    if t==6.0: return (0.0,0.0,1.0,0.60)
    if t<=9.5: return (0.0,0.0,1.0,0.64)
    return (0.12,0.03,0.85,0.62)
G={2.0:(0.36,0.50,0.64,0.38),2.5:(0.31,0.50,0.69,0.38),3.0:(0.23,0.50,0.77,0.38),3.5:(0.15,0.50,0.85,0.38),
   4.0:(0.02,0.49,0.92,0.39),4.5:(0.0,0.49,0.82,0.39),5.0:(0.0,0.49,0.68,0.39),5.5:(0.0,0.49,0.57,0.40)}
W=keys(woman); g=keys(lambda t:G.get(t))
c={"mediaId":5177,"level":"A","keyWord":"a teapot","defaultVoice":"female",
"taps":[
 {"phrase":"to pour tea into a cup","target":"the woman","voice":"female","keys":W},
 {"phrase":"to have red braids","target":"the woman","voice":"female","keys":W},
 {"phrase":"to stand in a row","target":"the glasses","voice":"female","keys":g}],
"stillS":0.5,
"nouns":[{"word":"a teapot","x":0.16,"y":0.52,"voice":"female"},
 {"word":"a cup","x":0.47,"y":0.76,"voice":"female"},
 {"word":"a woman","x":0.62,"y":0.30,"voice":"female"},
 {"word":"a table","x":0.78,"y":0.90,"voice":"female"}],
"question":"What is she pouring into the cup?",
"answer":["She","is","pouring","tea","into","the","cup."],
"answerVoice":"female",
"notes":"Woman box stops above the glasses (split line y~0.49) in 2.0-5.5; at 6.0 only one glass is left (no row), later edge slivers -> off from 6.0. Two phrases share the woman (only person)."}
json.dump(c,open('content/5177.json','w'),indent=1)
