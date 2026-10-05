import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
L={0.0:(.12,.14,.88,.86),0.5:(.12,.10,.88,.90),1.0:(.35,.17,.65,.83),1.5:(.38,.17,.62,.83),2.0:(.44,.17,.56,.83),
   2.5:(.24,.11,.76,.89),3.0:(.18,.08,.82,.92),3.5:(.08,0,.92,1),4.0:(0,0,.81,1),4.5:(0,0,.81,1),5.0:(0,0,.81,1),
   5.5:(0,0,.81,1),6.0:(0,.14,.81,.86),6.5:(0,.26,.79,.74),7.0:(0,.25,.77,.75),7.5:(0,.21,1,.79),8.0:(.05,.22,.74,.78),
   8.5:(.06,.22,.73,.78),9.0:(.06,.24,.69,.76),9.5:(.22,.26,.78,.74),10.0:(.39,.30,.61,.70)}
R={0.0:(0,.17,.11,.75),0.5:(0,.16,.11,.74),1.0:(0,.17,.34,.60),1.5:(0,.18,.37,.74),2.0:(0,.17,.43,.80),
   2.5:(0,.13,.23,.80),3.0:(0,.36,.17,.34),9.5:(0,.30,.21,.65),10.0:(0,.27,.38,.73)}
C={4.0:(.82,.05,.18,.18),4.5:(.82,.05,.18,.18),5.0:(.82,.07,.18,.18),5.5:(.82,.10,.18,.18),6.0:(.82,.20,.18,.18),
   6.5:(.80,.27,.20,.18),7.0:(.78,.33,.22,.16),8.0:(.80,.37,.20,.17),8.5:(.80,.37,.20,.17),9.0:(.77,.40,.23,.15)}
c={"mediaId":357,"level":"A","keyWord":"hairbrush","defaultVoice":"female",
 "taps":[{"phrase":"to brush her long hair","target":"the woman with long hair","voice":"female","keys":keys(L)},
  {"phrase":"to clap her hands","target":"the woman with red hair","voice":"female","keys":keys(R)},
  {"phrase":"to sit by the flowers","target":"the cat","voice":"female","keys":keys(C)}],
 "stillS":9.5,
 "nouns":[{"word":"a curtain","x":.45,"y":.10,"voice":"female"},{"word":"a window","x":.84,"y":.24,"voice":"female"},
  {"word":"flowers","x":.84,"y":.42,"voice":"female"},{"word":"a hairbrush","x":.60,"y":.60,"voice":"female"}],
 "question":"What is the woman holding?","answer":["She","is","holding","a","hairbrush."],"answerVoice":"female",
 "notes":"The cat is small and soft in the background on the windowsill next to the tulips (4.0-9.0; off where only a sliver shows at 7.5 and 9.5). The red-haired woman is at the left edge: narrow boxes at 0.0-0.5 and 3.0, off at 3.5 and 7.5-9.0 (only fingertips or a sleeve). Where the two women touch, the boxes are split on a vertical line, so the long-haired woman's brush hand is partly outside at 1.0-2.0. Question does not name which woman: only one woman holds anything."}
json.dump(c,open('content/357.json','w'),indent=1)
