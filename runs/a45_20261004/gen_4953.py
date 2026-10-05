import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
w={}
for t in T:
    if t<=6.0: w[t]=(0.0,0.03,0.80,0.95)
    elif t<10: w[t]=(0.0,0.05,0.82,0.58)
    else: w[t]=(0.0,0.0,0.75,0.39)
w[3.0]=(0.0,0.20,0.60,0.95)
s={}
for t in T:
    if 6.5<=t<10: s[t]=(0.44,0.59,0.63,0.73)
s[10.0]=(0.43,0.40,0.63,0.56)
wk=K(w); sk=K(s)
c={"mediaId":4953,"level":"B","keyWord":"hope","defaultVoice":"female",
"taps":[
 {"phrase":"to water a flowerpot","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to clasp her hands nervously","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to push through the soil","target":"the sprout","voice":"female","keys":sk}],
"stillS":8.5,
"nouns":[{"word":"a braid","x":0.25,"y":0.40,"voice":"female"},
 {"word":"a sprout","x":0.53,"y":0.64,"voice":"female"},
 {"word":"a flowerpot","x":0.55,"y":0.78,"voice":"female"},
 {"word":"a windowsill","x":0.72,"y":0.91,"voice":"female"}],
"question":"What is growing in the flowerpot?",
"answer":["A","tiny","sprout","is","growing","in","the","flowerpot."],
"answerVoice":"female",
"notes":"Woman changes from pyjamas to an orange sweater at 3.0 s (same person). Sprout first clearly visible at 6.5 s (tiny); woman box cut off above the sprout box from 6.5 s. Key word hope is a verb, not placed as a noun."}
json.dump(c,open("content/4953.json","w"),indent=1)
