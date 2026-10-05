import json
T=[i*0.5 for i in range(19)]
F={0.0:[.30,.10,.70,.78],0.5:[.30,.10,.70,.78],1.0:[.29,.11,.71,.80],1.5:[.29,.11,.71,.80],2.0:[.30,.11,.70,.79],2.5:[.30,.11,.70,.79],
3.0:[.28,.12,.72,.82],3.5:[.24,.17,.76,.80],4.0:[.31,.18,.69,.69],4.5:[.37,.17,.63,.70],5.0:[.45,.18,.55,.77],5.5:[.39,.17,.61,.78],
6.0:[.32,.22,.68,.68],6.5:[0,.12,1.0,.80],7.0:[.22,.20,.78,.80],7.5:[0,.02,1.0,.98],8.0:[.08,0,.92,1.0],8.5:[0,.10,1.0,.90],9.0:[0,.13,1.0,.87]}
S={0.0:[0,.20,.29,.21],0.5:[0,.20,.29,.21],1.0:[0,.24,.28,.19],1.5:[0,.24,.28,.19],2.0:[0,.22,.29,.21],2.5:[0,.22,.29,.21],
3.0:[0,.27,.27,.17],3.5:[0,.26,.23,.17],4.0:[0,.23,.30,.21],4.5:[.02,.22,.33,.22],5.0:[0,.25,.35,.22],5.5:[.07,.25,.29,.22],6.0:[0,.26,.30,.21]}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4575,"level":"A","keyWord":"cold","defaultVoice":"female",
"taps":[
{"phrase":"to cough into her hand","target":"the woman in front","voice":"female","keys":keys(F)},
{"phrase":"to take the water bottle","target":"the woman in front","voice":"female","keys":keys(F)},
{"phrase":"to ask for silence","target":"the woman in the white shirt","voice":"female","keys":keys(S)}],
"stillS":4.0,
"nouns":[{"word":"a chair","x":.16,"y":.52,"voice":"female"},{"word":"a bottle","x":.10,"y":.79,"voice":"female"},
{"word":"a book","x":.38,"y":.87,"voice":"female"}],
"question":"What is the woman in front doing?",
"answer":["She","is","coughing","into","her","hand."],
"answerVoice":"female",
"notes":"The woman in the white shirt puts a finger to her lips only at about 4.5-5.5 s ('to ask for silence' may be a little above level A; fallback 'to wear a white shirt'). She is hidden from 6.5 s. The front woman's box starts right of the white-shirt woman, so her left sleeve is partly outside it in 0-6 s. She grips the bottle only at 7.5-8.5 s. Other chairs stand in the background; the pill is on the big one in front."}
json.dump(c,open("content/4575.json","w"),indent=1)
