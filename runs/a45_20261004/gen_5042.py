import json
T=[i/2 for i in range(9)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={0.0:(0.19,0.22,0.94,1.0),0.5:(0.18,0.17,0.94,1.0),1.0:(0.2,0.32,0.96,1.0),3.0:(0.12,0.34,0.42,0.77),3.5:(0.15,0.33,0.42,0.76),4.0:(0.06,0.36,0.41,0.76)}
blonde={1.5:(0.26,0.18,0.76,1.0),3.0:(0.56,0.36,0.74,0.65),3.5:(0.57,0.36,0.75,0.65),4.0:(0.56,0.37,0.74,0.65)}
curly={2.0:(0.33,0.22,1.0,1.0),2.5:(0.26,0.31,0.96,1.0),3.0:(0.74,0.35,0.92,0.61),3.5:(0.75,0.35,0.93,0.62),4.0:(0.74,0.38,0.92,0.62)}
c={"mediaId":5042,"level":"B","keyWord":"painful","defaultVoice":"male",
"taps":[
 {"phrase":"to hold the door open","target":"the man in grey","voice":"male","keys":keys(man)},
 {"phrase":"to wear a navy crop top","target":"the blonde woman","voice":"female","keys":keys(blonde)},
 {"phrase":"to sink onto a bench","target":"the curly-haired woman","voice":"female","keys":keys(curly)}],
"stillS":4.0,
"nouns":[{"word":"trees","x":0.55,"y":0.10,"voice":"male"},{"word":"an apartment block","x":0.22,"y":0.27,"voice":"male"},
 {"word":"a bench","x":0.90,"y":0.66,"voice":"male"},{"word":"the pavement","x":0.40,"y":0.85,"voice":"male"}],
"question":"What is the man in grey doing?",
"answer":["He","is","holding","the","door","open."],"answerVoice":"male",
"notes":"Cuts: door shot 0.0-1.5, bench shot 2.0-2.5, group shot 3.0-4.0. The curly-haired woman in the group shot is assumed to be the dark-haired woman in black behind the man in the maroon vest (small, partly hidden) - check. The blonde woman wears a navy crop top in both her shots; the man in grey leads the group at the left. Key word 'painful' is an adjective, not placed as a noun."}
json.dump(c,open('content/5042.json','w'),indent=1)
