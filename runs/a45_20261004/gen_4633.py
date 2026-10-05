import json
man={0.0:(0,.24,.80,.56),0.5:(0,.25,.86,.55),1.0:(0,.25,.80,.57),1.5:(0,.24,.88,.58),2.0:(0,.24,.86,.58),
2.5:(0,.22,.84,.78),3.0:(.03,.30,.97,.70),3.5:(0,.29,1.0,.71),4.0:(0,.08,.80,.92),4.5:(.10,.05,.72,.95),
5.0:(.10,.12,.70,.88),5.5:(.15,.10,.83,.90),6.0:(0,.08,1.0,.92),6.5:(.05,.08,.90,.92),7.0:(.07,.08,.76,.92),
7.5:(.08,.22,.92,.78),8.0:(.02,.25,.90,.75),8.5:(0,.25,.88,.75),9.0:(0,.22,.88,.78),9.5:(0,.19,.88,.81),10.0:(0,.17,.85,.83)}
bus={3.0:(.42,.08,.58,.22),3.5:(.42,.04,.58,.25),4.0:(.80,.08,.20,.30),4.5:(.82,.10,.18,.24),5.0:(.80,.18,.20,.34)}
times=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4633,"level":"B","keyWord":"desperate","defaultVoice":"male",
"taps":[
 {"phrase":"to check the car battery","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to slump onto the kerb","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to pass the stranded driver","target":"the bus","voice":"male","keys":keys(bus)}],
"stillS":3.0,
"nouns":[{"word":"a bus","x":.72,"y":.22,"voice":"male"},{"word":"a raincoat","x":.62,"y":.55,"voice":"male"},
 {"word":"a battery","x":.36,"y":.78,"voice":"male"},{"word":"a headlight","x":.58,"y":.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["The","desperate","man","is","checking","the","car","battery."],
"answerVoice":"male",
"notes":"Bus is a background target, visible only 3.0-5.0 s (a thin sliver at the right edge at 5.5 s is set off). At 3.0-5.0 the bus is partly behind the man: boxes split along the line between them, so the man's box loses a little hair top / right shoulder there. 'kerb' is British spelling (as in the packet description)."}
json.dump(c,open('content/4633.json','w'),indent=1)
