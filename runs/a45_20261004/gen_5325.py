import json
T=[i*0.5 for i in range(21)]
W={0.0:(0,.17,.48,.80),0.5:(0,.19,.48,.80),1.0:(.02,.17,.47,.83),1.5:(0,.15,.49,.85),2.0:(0,.19,.50,.81),2.5:(.46,.19,.54,.73),3.0:(.52,.20,.48,.70),
3.5:(.53,.25,.47,.65),4.0:(.56,.19,.44,.58),4.5:(.56,.17,.44,.60),5.0:(.56,.17,.44,.75),5.5:(.58,.19,.42,.75),6.0:(.58,.14,.42,.76),6.5:(.55,.17,.45,.83),
7.0:(.49,.21,.51,.79),7.5:(.48,.17,.52,.83),8.0:(.53,.16,.47,.84),8.5:(.53,.17,.47,.83),9.0:(.63,.22,.37,.78),9.5:(.54,.25,.46,.75),10.0:(.53,.21,.47,.79)}
M={0.0:(.48,.13,.52,.87),0.5:(.48,.15,.52,.85),1.0:(.49,.14,.51,.86),1.5:(.49,.11,.51,.89),2.0:(.50,.16,.50,.84),2.5:(.02,.17,.44,.75),3.0:(0,.15,.52,.78),
3.5:(0,.15,.53,.75),4.0:(0,.14,.56,.66),4.5:(0,.14,.56,.63),5.0:(0,.17,.56,.76),5.5:(0,.15,.58,.72),6.0:(0,.09,.58,.79),6.5:(0,.14,.55,.75),
7.0:(0,.17,.49,.83),7.5:(0,.14,.48,.86),8.0:(0,.11,.53,.89),8.5:(0,.10,.53,.90),9.0:(0,.17,.63,.83),9.5:(0,.21,.54,.79),10.0:(0,.17,.53,.83)}
def keys(d): return [({"t":t,"off":True} if d[t] is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
c={"mediaId":5325,"level":"B","keyWord":"spouse","defaultVoice":"male",
"taps":[{"phrase":"to carry a grocery bag","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to clutch his car keys","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to point at a document","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":4.0,
"nouns":[{"word":"cabinets","x":.45,"y":.14,"voice":"male"},{"word":"a fridge","x":.42,"y":.29,"voice":"male"},
{"word":"documents","x":.55,"y":.79,"voice":"male"},{"word":"a counter","x":.50,"y":.90,"voice":"male"}],
"question":"What are the spouses doing?","answer":["They","are","signing","documents","at","a","counter."],"answerVoice":"male",
"notes":"Only two targets (the man, the woman); both sign, both high-five, so the phrases use what only one does: she carries the paper bag (1.0-2.0 s; at 0.0-0.5 s it hangs between them), he holds the keys (0.0-1.5 s), she points with her pen at his page (4.5 s only - brief, weakest phrase). The man and the woman swap sides at 2.5 s. 'documents' pill sits over the two sheets lying side by side. Key word 'spouse' is in the question, not a noun slot (cannot be placed on one thing). They -> defaultVoice male (mixed couple, odd id)."}
json.dump(c,open('content/5325.json','w'),indent=1)
