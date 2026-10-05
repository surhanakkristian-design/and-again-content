import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
F=(0.0,0.0,1.0,1.0)
woman={0.0:(0.0,0.08,0.74,0.78),0.5:(0.0,0.09,0.78,0.78),1.0:(0.0,0.09,0.74,0.88),1.5:F,2.0:F,2.5:F,3.0:F,3.5:F,4.0:F,
4.5:(0.0,0.46,0.20,0.42),5.0:(0.0,0.56,0.15,0.40),5.5:(0.0,0.38,0.62,0.62),6.0:F,6.5:F,7.0:(0.0,0.20,0.90,0.80),7.5:(0.0,0.17,1.0,0.83),
8.0:(0.0,0.05,1.0,0.95),8.5:(0.0,0.08,1.0,0.92),9.0:(0.0,0.02,1.0,0.98),9.5:(0.0,0.09,1.0,0.91),10.0:(0.0,0.05,1.0,0.95)}
man={0.0:(0.74,0.44,0.26,0.46),0.5:(0.78,0.46,0.22,0.46),1.0:(0.74,0.54,0.26,0.46),
4.5:(0.36,0.08,0.64,0.92),5.0:(0.30,0.09,0.70,0.91),5.5:(0.66,0.10,0.34,0.90)}
c={"mediaId":290,"level":"A","keyWord":"feeling","defaultVoice":"female",
"taps":[
 {"phrase":"to touch her chest","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to close her eyes","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to wear a grey shirt","target":"the man with long hair","voice":"male","keys":K(man)}],
"stillS":0.0,
"nouns":[{"word":"a flag","x":0.28,"y":0.11,"voice":"female"},{"word":"a woman","x":0.38,"y":0.36,"voice":"female"},{"word":"a glass","x":0.90,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","touching","her","chest."],
"answerVoice":"female",
"notes":"Only one woman; the crowd of men behind her cannot be told apart, so the only second target is the man with long hair in the grey shirt (state phrase: no action that is his alone). He is boxed where his shoulder/hair or whole body shows (0.0-1.0 s, 4.5-5.5 s) and off where only his hand or sleeve reaches into the picture (3.5-4.0 s, 6.0 s on). In the close-ups the woman's body fills the full width, so her box is the whole frame and includes background faces. At 4.5-5.0 s only her maroon sleeve is visible at the left edge. A second small blue flag hangs top right at the still; the pill sits on the big flag top left."}
json.dump(c,open("content/290.json","w"),indent=1)
