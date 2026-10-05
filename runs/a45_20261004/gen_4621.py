import json
times=[i*0.5 for i in range(25)]
W={0.0:(.17,.22,.60,.78),0.5:(.19,.32,.58,.68),1.0:(.23,.38,.58,.62),1.5:(.25,.40,.52,.60),2.0:(.25,.34,.58,.66),2.5:(.19,.30,.60,.70),
3.0:(.05,.49,.70,.51),3.5:(.05,.43,.70,.57),4.0:(0,.40,.59,.60),4.5:(0,.55,.31,.45),
10.0:(0,.24,.65,.76),10.5:(0,.21,.85,.79),11.0:(.05,.23,.90,.77),11.5:(.19,.25,.81,.75),12.0:(.19,.26,.81,.74)}
P={6.5:(.66,.46,.34,.25),7.0:(.40,.47,.60,.22),7.5:(.18,.46,.68,.21),8.0:(.44,.45,.56,.21)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4621,"level":"A","keyWord":"passenger","defaultVoice":"female",
"taps":[
 {"phrase":"to look up at the screens","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to sleep on the floor","target":"the person on the floor","voice":"female","keys":keys(P)},
 {"phrase":"to cover her mouth","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":7.0,
"nouns":[{"word":"a blanket","x":.72,"y":.56,"voice":"female"},{"word":"a suitcase","x":.16,"y":.61,"voice":"female"},
 {"word":"the sky","x":.35,"y":.10,"voice":"female"},{"word":"the floor","x":.60,"y":.85,"voice":"female"}],
"question":"What is the woman looking at?",
"answer":["She","is","looking","up","at","the","screens."],
"answerVoice":"female",
"notes":"Many passengers sleep on the chairs, so no phrase about sleeping on chairs; only one person sleeps on the floor (under a blanket, 6.5-8.0 s). Woman off 5.0-9.5 (at 9.5 only a sleeve at the edge). Key word 'passenger' not used as a noun: many passengers in the picture."}
json.dump(c,open("content/4621.json","w"),indent=1,ensure_ascii=False)
