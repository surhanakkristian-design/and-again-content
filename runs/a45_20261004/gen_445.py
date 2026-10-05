import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
woman={t:(0,0,.9,1) for t in T if t<=3.5}
woman.update({4.0:(.38,.07,.56,.21),4.5:(.38,.07,.56,.21),5.0:(.38,.07,.56,.21),
5.5:(.4,.5,.68,.78),6.0:(.38,.5,.67,.78),6.5:(.33,.55,.66,.82),7.0:(.34,.59,.65,.85),7.5:(.36,.62,.65,.86),
8.0:(.36,.65,.64,.85),8.5:(.36,.67,.63,.87),9.0:(.36,.7,.62,.88),9.5:(.4,.71,.6,.88),10.0:(.4,.72,.6,.88)})
line={4.0:(0,.21,1,1),4.5:(0,.21,1,1),5.0:(0,.21,1,1),
5.5:(.4,.05,.6,.5),6.0:(.4,.07,.6,.5),6.5:(.4,.08,.6,.55),7.0:(.4,.12,.6,.59),7.5:(.4,.15,.6,.62),
8.0:(.4,.18,.6,.65),8.5:(.4,.2,.6,.67),9.0:(.4,.23,.6,.7),9.5:(.4,.25,.6,.71),10.0:(.4,.26,.6,.72)}
c={"mediaId":445,"level":"A","keyWord":"line","defaultVoice":"female",
"taps":[
{"phrase":"to walk in green boots","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear a blue cap","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to be long and white","target":"the white line","voice":"female","keys":keys(line)}],
"stillS":8.0,
"nouns":[{"word":"a line","x":.5,"y":.38,"voice":"female"},{"word":"a woman","x":.52,"y":.76,"voice":"female"},
{"word":"grass","x":.22,"y":.55,"voice":"female"},{"word":"a hill","x":.5,"y":.06,"voice":"female"}],
"question":"What is the woman standing on?",
"answer":["She","is","standing","on","a","white","line."],
"answerVoice":"female",
"notes":"Only two targets: the woman and the line. A second person (green jacket) is only an arm at the right edge in the close-up (0-3.5 s) and a tiny blur at 4-5 s, so not used. The marking machine is never seen whole (only its handle), so no phrase about it. Line box is OFF in the close-up 0-3.5 s: the strip of paint is seen only between the woman's legs, inside her box. At 4-5 s the woman is the left one of two tiny blurred figures at the top; her box there is small and stops at x 0.56 before the green figure. In the drone shot (5.5 s on) the woman stands on the line: line box = the part above her head, her box around her. A second, short white line crosses at the bottom of the drone shot and is not boxed (the phrase 'long' means the one running up the field). Her boots are clear in the close-up; in the drone shot she mostly stands, slowly stepping."}
json.dump(c,open("content/445.json","w"),indent=1,ensure_ascii=False)
