import json
def keys(d, times):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if d.get(t) else dict(t=t, off=True) for t in times]
times=[i*0.5 for i in range(21)]
M={0.0:(0,.30,.63,.70),0.5:(0,.27,.64,.73),1.0:(0,.27,.63,.73),1.5:(0,.25,.69,.75),2.0:(0,.16,.66,.84),2.5:(0,.28,.79,.72),3.0:(0,.34,.88,.66),3.5:(0,.34,.84,.66),
4.0:(0,.31,.86,.69),4.5:(0,.32,.86,.68),5.0:(0,.38,.77,.62),5.5:(0,.40,.77,.60),6.0:(0,.35,.50,.65),6.5:(0,.32,.52,.68),7.0:(0,.31,.52,.69),7.5:(0,.31,.52,.69),
8.0:(0,.31,.52,.69),8.5:(0,.31,.52,.69),9.0:(0,.29,.50,.71),9.5:(0,.32,.52,.68),10.0:(0,.34,.56,.66)}
F={0.0:(.64,.34,.36,.37),0.5:(.65,.33,.35,.37),1.0:(.64,.345,.36,.38),1.5:(.70,.375,.30,.34),2.0:(.66,.45,.34,.27),2.5:(.36,.13,.42,.15),3.0:(.22,.16,.55,.18),3.5:(.26,.16,.70,.18),
4.0:(.27,.17,.67,.14),4.5:(.28,.18,.72,.14),5.0:(.78,.20,.22,.62),5.5:(.78,.21,.22,.60),6.0:(.50,.30,.48,.42),6.5:(.52,.29,.48,.41),7.0:(.52,.32,.48,.41),7.5:(.52,.31,.48,.42),
8.0:(.52,.29,.48,.43),8.5:(.52,.29,.48,.43),9.0:(.50,.275,.50,.55),9.5:(.52,.275,.48,.55),10.0:(.56,.27,.44,.47)}
Wt={0.5:(.80,.19,.20,.14),1.0:(.80,.20,.20,.14),1.5:(.80,.22,.20,.15),2.0:(.80,.22,.20,.23),2.5:(.80,.24,.20,.26),3.0:(.80,.20,.20,.14),
5.0:(.62,.16,.16,.14),5.5:(.60,.16,.17,.14),6.0:(.66,.16,.26,.14),6.5:(.68,.15,.27,.14),7.0:(.68,.15,.30,.17),7.5:(.68,.14,.30,.17),
8.0:(.68,.13,.28,.16),8.5:(.66,.13,.30,.16),9.0:(.68,.13,.28,.14),9.5:(.70,.13,.26,.14),10.0:(.68,.13,.28,.14)}
c={"mediaId":4525,"level":"A","keyWord":"help","defaultVoice":"male",
"taps":[
 {"phrase":"to drink some water","target":"the young man","voice":"male","keys":keys(M,times)},
 {"phrase":"to help the young man","target":"the woman in orange","voice":"female","keys":keys(F,times)},
 {"phrase":"to wear a white shirt","target":"the waiter","voice":"male","keys":keys(Wt,times)}],
"stillS":8.0,
"nouns":[{"word":"a waiter","x":.80,"y":.22,"voice":"male"},{"word":"a glass","x":.80,"y":.63,"voice":"male"},
 {"word":"croissants","x":.62,"y":.73,"voice":"male"},{"word":"a menu","x":.62,"y":.87,"voice":"male"}],
"question":"What is the woman in orange doing?",
"answer":["She","is","helping","the","young","man."],
"answerVoice":"female",
"notes":"Man and woman overlap heavily from 2.0 to 5.5 (she stands behind him and pulls); the boxes are split along a line, so part of her arms/cardigan falls into his box there (2.5-4.5: only her head and shoulders above his back; 5.0-5.5: vertical strip on the right). Waiter is not visible at 0.0 and hidden at 3.5-4.5 (off); at 5.0-5.5 only his head shows. The waiter phrase is a state: he only stands and watches, like the seated guests. He drinks only at 8.5-9.5 while she holds the glass."}
json.dump(c,open('content/4525.json','w'),indent=1,ensure_ascii=False)
