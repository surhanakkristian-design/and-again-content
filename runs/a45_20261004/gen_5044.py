import json
T=[i/2 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
hp={0.0:(0.0,0.13,1.0,1.0),0.5:(0.0,0.12,1.0,1.0),1.0:(0.0,0.11,1.0,1.0),1.5:(0.0,0.09,1.0,1.0),2.0:(0.0,0.07,1.0,1.0)}
br={2.5:(0.02,0.2,0.83,0.84),3.0:(0.0,0.2,0.82,0.84),3.5:(0.02,0.19,0.84,0.84),4.0:(0.0,0.17,0.86,0.84),4.5:(0.0,0.16,0.9,0.85)}
dm={5.0:(0.0,0.17,0.76,1.0),5.5:(0.0,0.17,0.74,1.0),6.0:(0.0,0.16,0.73,1.0),6.5:(0.0,0.15,0.74,1.0),7.0:(0.0,0.14,0.73,1.0),7.5:(0.0,0.15,0.76,1.0)}
c={"mediaId":5044,"level":"A","keyWord":"hear","defaultVoice":"female",
"taps":[
 {"phrase":"to listen to music","target":"the man with headphones","voice":"male","keys":keys(hp)},
 {"phrase":"to talk in a cafe","target":"the woman with braids","voice":"female","keys":keys(br)},
 {"phrase":"to listen at the door","target":"the man in the blue shirt","voice":"male","keys":keys(dm)}],
"stillS":3.5,
"nouns":[{"word":"a lamp","x":0.40,"y":0.16,"voice":"female"},{"word":"a glass","x":0.15,"y":0.70,"voice":"female"},
 {"word":"a cup","x":0.62,"y":0.81,"voice":"female"},{"word":"a table","x":0.30,"y":0.92,"voice":"female"}],
"question":"What is the man with headphones doing?",
"answer":["He","is","listening","to","music."],"answerVoice":"male",
"notes":"Montage of 4 shots: headphones man 0.0-2.0, cafe 2.5-4.5, man at the office door 5.0-7.5, festival crowd 8.0-10.0 (no target there: many people cover their ears, no single one fits). Braids woman: mouth open mid-sentence, her friend at the right edge is cut off and not boxed. defaultVoice female (montage, no single main person, evenId true). Key word 'hear' is a verb, not placed."}
json.dump(c,open('content/5044.json','w'),indent=1)
