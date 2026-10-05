import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(.07,.20,.90,.80),0.5:(.07,.22,.93,.78),1.0:(.07,.25,.90,.75),1.5:(.07,.26,.93,.74),2.0:(.06,.25,.90,.75),2.5:(.06,.24,.93,.76),3.0:(.07,.24,.90,.76),3.5:(.07,.24,.93,.76),4.0:(.08,.22,.87,.78),4.5:(.15,.21,.68,.79),
5.0:(.14,.62,.70,.38),5.5:(.13,.58,.72,.42),6.0:(.13,.64,.72,.36),6.5:(.25,.65,.50,.35),7.0:(.25,.65,.50,.35),7.5:(.25,.65,.50,.35),8.0:(.25,.61,.50,.39),8.5:(.22,.59,.60,.41),9.0:(.12,.42,.82,.58),9.5:(.12,.41,.76,.59),10.0:(.12,.39,.76,.61)}
balloon={5.0:(.30,.39,.37,.22),5.5:(.24,.29,.47,.28),6.0:(.25,.35,.45,.28),6.5:(.18,.30,.59,.34),7.0:(.12,.24,.68,.40),7.5:(.08,.19,.77,.45),8.0:(.05,.10,.84,.50),8.5:(.07,.08,.85,.50),9.0:(.10,0,.80,.41),9.5:(.12,0,.76,.40),10.0:(.14,0,.74,.38)}
kw=keys(woman)
c={"mediaId":455,"level":"B","keyWord":"lungs","defaultVoice":"female",
"taps":[
 {"phrase":"to take deep breaths","target":"the woman","voice":"female","keys":kw},
 {"phrase":"to inflate a red balloon","target":"the woman","voice":"female","keys":kw},
 {"phrase":"to swell to a huge size","target":"the balloon","voice":"female","keys":keys(balloon)}],
"stillS":10.0,
"nouns":[{"word":"a balloon","x":.50,"y":.17,"voice":"female"},{"word":"a T-shirt","x":.50,"y":.66,"voice":"female"},{"word":"leggings","x":.50,"y":.90,"voice":"female"},{"word":"a lawn","x":.20,"y":.78,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","inflating","a","huge","red","balloon."],
"answerVoice":"female",
"notes":"Key word 'lungs' is not visible, so it is in no noun slot or answer. The balloon covers the woman from 5.0 on: boxes are split with a horizontal line, the balloon keeps its whole area and the woman's box is her body below it (her face above the balloon at 5.0-6.0 and her raised arms at 9.0-10.0 are outside her box). At 4.5 the balloon is a tiny red dot inside her hands in front of her face: set off there. Tiny blurred passers-by and a dog in the background at 1.0-3.5 are ignored."}
json.dump(c,open("content/455.json","w"),indent=1)
