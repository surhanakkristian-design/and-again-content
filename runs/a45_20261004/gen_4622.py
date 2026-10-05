import json
times=[i*0.5 for i in range(21)]
W={0.0:(.07,.40,.85,.60),0.5:(.07,.42,.90,.58),1.0:(.03,.43,.92,.57),1.5:(.05,.43,.93,.57),2.0:(.05,.42,.90,.58),2.5:(.05,.39,.93,.61),
3.0:(.09,.39,.87,.61),3.5:(.12,.40,.86,.60),4.0:(.09,.40,.89,.60),4.5:(.12,.42,.88,.58),
5.0:(.19,.39,.76,.52),5.5:(.17,.37,.78,.54),6.0:(.10,.39,.85,.38),6.5:(.09,.41,.91,.36),7.0:(.09,.44,.91,.43),
7.5:(.02,.50,.98,.38),8.0:(.02,.46,.98,.25),8.5:(.02,.46,.98,.25),9.0:(.02,.49,.98,.24),9.5:(.02,.50,.98,.42),10.0:(.02,.50,.98,.30)}
P={0.0:(.74,.24,.26,.16),0.5:(.74,.25,.26,.17),1.0:(.74,.26,.26,.17),1.5:(.74,.26,.26,.17),2.0:(.74,.25,.26,.17),2.5:(.74,.24,.26,.15),
3.0:(.72,.24,.28,.15),3.5:(.74,.24,.26,.16),4.0:(.72,.23,.28,.17),4.5:(.72,.24,.28,.18),
5.0:(0,.25,.95,.14),5.5:(0,.23,.95,.14),6.0:(0,.22,.95,.17),6.5:(0,.23,.95,.18),7.0:(0,.26,.95,.18),
7.5:(.18,.24,.82,.22),8.0:(.15,.19,.85,.26),8.5:(.15,.19,.85,.26),9.0:(.15,.19,.85,.26),9.5:(.15,.19,.85,.26),10.0:(.15,.19,.85,.26)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4622,"level":"B","keyWord":"sigh","defaultVoice":"female",
"taps":[
 {"phrase":"to sigh at the ceiling","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to glance at her watch","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to stand on the tarmac","target":"the plane","voice":"female","keys":keys(P)}],
"stillS":6.0,
"nouns":[{"word":"a suitcase","x":.70,"y":.80,"voice":"female"},{"word":"a plane","x":.35,"y":.33,"voice":"female"},
 {"word":"a neck pillow","x":.24,"y":.46,"voice":"female"},{"word":"a paper cup","x":.54,"y":.56,"voice":"female"}],
"question":"What is the woman glancing at?",
"answer":["She","is","glancing","at","her","watch."],
"answerVoice":"female",
"notes":"Only two real targets (woman, plane outside); the sleeping men in the back were not used because the woman sleeps too later. Plane box is cut at the top of the woman's head where they meet (2.5-6.5 s) so the boxes do not overlap. The plane icon on the gate sign is not in the plane box. Plane phrase is a state. Pillow and cup pills are close (0.10 in y)."}
json.dump(c,open("content/4622.json","w"),indent=1,ensure_ascii=False)
