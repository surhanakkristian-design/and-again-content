import json
girl={0.0:(.10,.20,.90,.80),0.5:(.03,.15,.97,.85),1.0:(.22,.18,.78,.82),1.5:(.22,.18,.78,.82),2.0:(.38,.17,.62,.83),
2.5:(.48,.17,.52,.83),3.0:(.47,.17,.53,.83),3.5:(.22,.08,.66,.55),4.0:(0,.08,1.0,.88),4.5:(0,.15,.80,.85),5.0:(0,.17,.82,.83),
6.0:(0,.60,.18,.18),6.5:(0,.33,.26,.34),7.0:(0,.53,1.0,.47),7.5:(0,.52,1.0,.48),8.0:(0,.38,.66,.62),8.5:(0,.76,.82,.24),9.0:(.03,.52,.90,.48)}
lh={5.5:(.50,.17,.32,.30),6.0:(.55,.16,.33,.29),6.5:(.60,.19,.35,.27),7.0:(.64,.22,.36,.31),7.5:(.67,.23,.33,.29),
8.0:(.67,.24,.33,.26),8.5:(.48,.24,.40,.28),9.0:(.42,.24,.36,.28)}
times=[i*0.5 for i in range(19)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4635,"level":"B","keyWord":"destination","defaultVoice":"female",
"taps":[
 {"phrase":"to circle her destination","target":"the girl","voice":"female","keys":keys(girl)},
 {"phrase":"to gaze at the sea","target":"the girl","voice":"female","keys":keys(girl)},
 {"phrase":"to tower over the cliff","target":"the lighthouse","voice":"female","keys":keys(lh)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":.40,"y":.12,"voice":"female"},{"word":"a lighthouse","x":.60,"y":.36,"voice":"female"},
 {"word":"a cliff","x":.33,"y":.50,"voice":"female"},{"word":"a backpack","x":.43,"y":.90,"voice":"female"}],
"question":"What is the girl circling?",
"answer":["She","is","circling","her","destination","on","a","photo."],
"answerVoice":"female",
"notes":"Girl box = her face/body or, in the clifftop shots, only her arms and hands (6.0: just fingertips at the left edge). 3.5-4.0 s: she is seen only as a reflection in the train window (box on the reflection). 'the lighthouse' = the real tower (5.5-9.0 s); the tiny lighthouse inside the photo is not boxed. 7.0-8.0 s: her hands are in front of the tower, boxes split between them. Photo is not in the still (9.0 s), so it is not a noun."}
json.dump(c,open('content/4635.json','w'),indent=1)
