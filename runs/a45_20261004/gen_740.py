import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, **dict(zip("xywh", d[t]))) if t in d else dict(t=t, off=True) for t in T]
man={0:(.14,.20,.86,.80),.5:(.14,.20,.86,.80),1.5:(.14,.24,.86,.76),2:(.13,.26,.68,.74),
3:(0,.64,.80,.36),3.5:(.02,.56,.82,.44),4:(.20,.86,.52,.14),
4.5:(0,.13,1,.87),5:(0,.12,1,.88),5.5:(0,.08,1,.92),6:(0,.04,1,.96),6.5:(0,.04,1,.96),7:(0,.02,1,.98),7.5:(0,.04,1,.96),
8:(0,.28,1,.72),8.5:(0,.24,.47,.76),9:(0,.25,.51,.75),9.5:(0,.23,.48,.77),10:(0,.24,.49,.76)}
wom={1:(0,.24,1,.76),2:(.82,0,.18,.44),2.5:(.26,.30,.25,.31),3:(.33,.30,.24,.30),3.5:(.46,.28,.24,.26),4:(.44,.27,.24,.26),
8.5:(.48,.38,.42,.62),9:(.52,.33,.48,.67),9.5:(.49,.29,.51,.71),10:(.50,.31,.50,.69)}
c={"mediaId":740,"level":"B","keyWord":"stopwatch","defaultVoice":"male",
"taps":[
{"phrase":"to sprint down the track","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to time the sprinter","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stare at the dial","target":"the man","voice":"male","keys":keys(man)}],
"stillS":0.0,
"nouns":[{"word":"a stopwatch","x":.48,"y":.50,"voice":"male"},{"word":"a thumb","x":.62,"y":.30,"voice":"male"},
{"word":"a cord","x":.44,"y":.88,"voice":"male"},{"word":"a sleeve","x":.84,"y":.76,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","timing","the","sprinter","with","a","stopwatch."],
"answerVoice":"male",
"notes":"Two targets (man, woman); the stopwatch is always in the man's hand so it is not a separate target. In the POV shots (0-2.0, 3.0-4.0) only the man's hand/arm with the stopwatch is visible: boxed as 'the man'; 2.5 s shows only the cord, man off. At 4.5-8.0 a tiny blurred pink figure behind the man is ignored (woman off). 8.5-10.0: the two stand together, split along a vertical line; his arm (8.5) and her hands (10.0) cross it. At 10.0 the woman also looks at the stopwatch, laughing - 'to stare at the dial' is the man's long stare at 4.5-7.0."}
json.dump(c,open("content/740.json","w"),indent=1)
