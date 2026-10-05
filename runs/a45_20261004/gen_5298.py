import json
T=[i*0.5 for i in range(23)]
M={0.0:(0,.09,.86,.91),0.5:(0,.10,.90,.90),1.0:(0,.10,.89,.90),1.5:(0,.12,.86,.88),2.0:(0,.11,.85,.89),2.5:(0,.11,.86,.89),
3.0:(0,.12,.86,.88),3.5:(0,.12,.86,.88),4.0:(0,.13,.78,.87),4.5:(0,.12,.92,.88),5.0:(0,.14,1.0,.86),5.5:(0,.13,1.0,.87),
6.0:(0,.11,.92,.89),6.5:(0,.11,.84,.89),7.0:(0,.12,.75,.88),7.5:(0,.12,.82,.88),8.0:(.02,.12,.94,.88),8.5:(0,.12,.95,.88),
9.0:(0,.13,.78,.87),9.5:(0,.14,.90,.86),10.0:(0,.12,.97,.88),10.5:(0,.12,.90,.88),11.0:(0,.11,.88,.89)}
def keys(b):
    return [{"t":t,"off":True} if b.get(t) is None else dict(zip("txywh",(t,)+b[t])) for t in T]
mk=keys(M)
c={"mediaId":5298,"level":"B","keyWord":"blazer","defaultVoice":"female",
"taps":[{"phrase":"to sniff a paper strip","target":"the woman","voice":"female","keys":mk},
{"phrase":"to reach for another bottle","target":"the woman","voice":"female","keys":mk},
{"phrase":"to gasp in surprise","target":"the woman","voice":"female","keys":mk}],
"stillS":2.0,
"nouns":[{"word":"a ponytail","x":0.22,"y":0.20,"voice":"female"},{"word":"a white top","x":0.48,"y":0.47,"voice":"female"},
{"word":"a blazer","x":0.15,"y":0.68,"voice":"female"},{"word":"perfume bottles","x":0.62,"y":0.86,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","trying","out","perfumes","in","a","shop."],"answerVoice":"female",
"notes":"One clear person; shoppers/assistant in the background are small and blurred, so all three phrases use the woman (she fills most of the frame; box runs to the bottom behind the bottles). 'to sniff a paper strip' 0.5-1.0 and 6.0; 'to reach for another bottle' 2.0-2.5, 5.0, 8.0, 10.0; 'to gasp in surprise' 9.0 (wide eyes, open mouth, visual only). Key word 'blazer' placed as a noun; nouns ponytail/white top/blazer are different parts of the same large figure, well apart."}
json.dump(c,open('content/5298.json','w'),indent=1)
