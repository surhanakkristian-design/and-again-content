import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x1,x2,y1,y2=b; out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
woman=K([(.06,.58,.37,.95),(.08,.56,.36,.95),(.06,.53,.32,.96),(.10,.53,.28,.91),(.10,.51,.29,.92),(.11,.50,.30,.92),(.10,.49,.31,.93),(.11,.51,.32,.93)])
bell=K([(.50,.88,.13,.37),(.56,.89,.14,.44),(.53,.88,.22,.50),(.53,.88,.26,.505),(.52,.81,.35,.62),(.51,.82,.44,.71),(.51,.82,.50,.74),(.52,.82,.53,.76)])
man=K([(.77,.99,.49,.72),(.78,.99,.49,.72),(.78,.99,.50,.73),(.79,.99,.51,.73),(.81,.99,.52,.74),(.82,1.0,.54,.75),(.82,1.0,.54,.76),(.82,1.0,.54,.76)])
c={"mediaId":6901,"level":"B","keyWord":"bring down","defaultVoice":"female",
"taps":[{"phrase":"to lower a heavy bronze bell","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to sink onto a wooden cradle","target":"the bell","voice":"female","keys":bell},
{"phrase":"to raise both hands","target":"the man in black","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a church tower","x":0.47,"y":0.17,"voice":"female"},{"word":"a bell","x":0.70,"y":0.28,"voice":"female"},
{"word":"a braid","x":0.22,"y":0.46,"voice":"female"},{"word":"sandbags","x":0.66,"y":0.70,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","lowering","a","heavy","bronze","bell."],
"answerVoice":"female",
"notes":"From 2.2 s the man in black stands right behind the bell rim, so the bell and man boxes are split at x 0.81-0.82 (bell box clips its right rim slightly). The man raises his hands 0.2-1.7 s, then holds them to his head and walks. Woman's raised hand touches the bell at 0.2-1.7 s; boxes split there."}
json.dump(c,open('content/6901.json','w'),indent=1)
