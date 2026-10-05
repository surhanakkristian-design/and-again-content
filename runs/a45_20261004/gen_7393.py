import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
wom=K([(.30,0,.74,.52),(.31,0,.77,.51),(.30,.03,.76,.50),(.30,.07,.78,.49),(.25,.10,.74,.47),(.27,.09,.76,.46),(.27,.08,.73,.45),(.29,.08,.76,.45)])
man=K([(0,.53,.66,1),(0,.52,.66,1),(0,.51,.66,1),(0,.50,.66,1),(0,.48,.66,1),(0,.47,.66,1),(0,.46,.67,1),(0,.46,.66,1)])
c={"mediaId":7393,"level":"A","keyWord":"olive oil","defaultVoice":"female",
"taps":[{"phrase":"to pour olive oil","target":"the woman","voice":"female","keys":wom},
{"phrase":"to hold a round loaf","target":"the man in front","voice":"male","keys":man},
{"phrase":"to lift a big jug","target":"the woman","voice":"female","keys":wom}],
"stillS":0.2,
"nouns":[{"word":"a jug","x":0.62,"y":0.08,"voice":"female"},{"word":"a donkey","x":0.82,"y":0.60,"voice":"female"},
{"word":"bread","x":0.52,"y":0.76,"voice":"female"},{"word":"olives","x":0.84,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","pouring","olive","oil","on","bread."],
"answerVoice":"female",
"notes":"The man stands in front of the woman: boxes split horizontally at the top of his head; the man's box (head, bread, arms) covers the woman's lower skirt and the crate, so the woman is tapped on her jug/head/top. 'loaf' is A2. Key word olive oil not used as a noun pill (thin stream over her body)."}
json.dump(c,open('content/7393.json','w'),indent=1)
