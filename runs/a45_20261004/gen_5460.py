import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
grey={0.0:(0,0.17,1,0.83),0.5:(0,0.18,1,0.82),1.0:(0,0.15,0.98,0.85),1.5:(0.12,0,0.88,1),2.0:(0,0.22,0.68,0.78),
 2.5:(0.1,0.43,0.82,0.57),3.0:(0.4,0.48,0.6,0.52),5.0:(0.52,0.44,0.28,0.26),5.5:(0.82,0.52,0.18,0.48)}
brown={4.5:(0,0.2,0.26,0.44),5.5:(0.24,0.27,0.5,0.71),8.0:(0.48,0.34,0.27,0.18),8.5:(0.64,0.4,0.22,0.14)}
green={6.0:(0,0,1,1),6.5:(0,0.32,0.95,0.68),7.0:(0,0.84,0.5,0.16),7.5:(0,0.76,0.2,0.24),8.0:(0,0.64,0.36,0.32),
 8.5:(0,0.63,0.44,0.32),9.0:(0,0.58,0.42,0.38)}
c={"mediaId":5460,"level":"B","keyWord":"sickness","defaultVoice":"female",
"taps":[{"phrase":"to hurry to a rubbish bin","target":"the man in grey","voice":"male","keys":K(grey)},
{"phrase":"to wear a brown crop top","target":"the woman in the brown top","voice":"female","keys":K(brown)},
{"phrase":"to turn green in the face","target":"the green-faced man","voice":"male","keys":K(green)}],
"stillS":5.0,
"nouns":[{"word":"clouds","x":0.62,"y":0.06,"voice":"female"},
{"word":"flags","x":0.4,"y":0.15,"voice":"female"},
{"word":"a metal fence","x":0.16,"y":0.45,"voice":"female"},
{"word":"a rubbish bin","x":0.75,"y":0.82,"voice":"female"}],
"question":"What are the people doing?",
"answer":["They","are","bending","over","the","bins."],"answerVoice":"female",
"notes":"Crowded clip with many cuts; nearly everyone covers their mouth and bends over bins, so uniqueness is weak. defaultVoice female: mixed group, evenId true. Man in grey: 0.0-3.0, then probably the grey-shirted man bent into the bin behind the woman at 5.0 and the man at the right edge at 5.5 (identity likely, not certain). Woman in brown top: 4.5 (left, behind the woman in the navy top), 5.5, and probably the bent dark-haired woman at 8.0/8.5 (identity uncertain). Phrase is a state: covering the mouth is shared by many people and the two-hand version does not fit in 6 words; the other women wear navy, white or lilac tops. Green-faced man: close-up 6.0-6.5, then bottom-left 7.0-9.0 (blue T-shirt, green tint). A second, small bin stands partly hidden behind the woman at 5.0 (x 0.42, y 0.40)."}
json.dump(c,open('content/5460.json','w'),indent=1)
