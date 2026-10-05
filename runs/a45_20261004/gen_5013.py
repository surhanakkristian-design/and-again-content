import json
def K(times, boxes):
    out=[]
    for t in times:
        b=boxes.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T=[i*0.5 for i in range(25)]
old={0.0:(0,0.05,0.6,0.9),0.5:(0,0.03,0.62,0.92),1.0:(0,0.03,0.68,0.92),1.5:(0,0.05,0.7,0.9),2.0:(0,0.04,0.68,0.92),2.5:(0,0.04,0.72,0.92),3.0:(0,0.1,0.72,0.85)}
wom={3.5:(0.55,0.17,0.45,0.82),4.0:(0.36,0.18,0.64,0.81),4.5:(0.25,0.12,0.75,0.87),5.0:(0.28,0.14,0.7,0.85),5.5:(0.3,0.2,0.7,0.79),6.0:(0.27,0.21,0.71,0.78)}
man={6.5:(0.2,0.3,0.44,0.36),7.0:(0.18,0.32,0.44,0.33),7.5:(0.1,0.3,0.46,0.35),8.0:(0.13,0.29,0.42,0.37),8.5:(0.13,0.29,0.4,0.39),9.0:(0.08,0.29,0.44,0.4),9.5:(0.08,0.27,0.44,0.42),10.0:(0.02,0.26,0.5,0.47),10.5:(0,0.26,0.46,0.48),11.0:(0.02,0.26,0.5,0.49),11.5:(0,0.24,0.54,0.5),12.0:(0,0.26,0.54,0.49)}
d={"mediaId":5013,"level":"A","keyWord":"cheap","defaultVoice":"male",
"taps":[
 {"phrase":"to stir a pot","target":"the old man","voice":"male","keys":K(T,old)},
 {"phrase":"to bake cookies","target":"the woman","voice":"female","keys":K(T,wom)},
 {"phrase":"to wear a black sweater","target":"the young man","voice":"male","keys":K(T,man)}],
"stillS":4.0,
"nouns":[{"word":"a woman","x":0.72,"y":0.33,"voice":"female"},{"word":"cookies","x":0.2,"y":0.72,"voice":"male"},{"word":"a kettle","x":0.2,"y":0.46,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","taking","cookies","out","of","the","oven."],
"answerVoice":"female",
"notes":"Three separate shots (old man 0-3.0, woman 3.5-6.0, young man 6.5-12.0) with cross-dissolves at 3.5 and 6.5; faded previous person treated as off. Mixed cast -> defaultVoice male (evenId false). Third phrase is a state: the young man mostly stands and touches the counter; 'black sweater' (turtleneck) separates him from the woman's beige sweater. Price captions overlap boxes, no issue."}
json.dump(d,open("content/5013.json","w"),indent=1)
