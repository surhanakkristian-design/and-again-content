import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
yel={0.0:(0,0,0.76,0.52),0.5:(0,0,0.82,0.46),1.0:(0,0,0.84,0.5),1.5:(0.1,0.02,0.77,0.62),2.0:(0,0.1,0.47,0.9)}
tat={2.0:(0.47,0.09,0.32,0.65),2.5:(0.15,0.12,0.7,0.6),3.0:(0.1,0.11,0.78,0.65),3.5:(0.06,0.1,0.88,0.72),4.0:(0.44,0.12,0.56,0.68)}
whe={4.0:(0.2,0.32,0.18,0.36),4.5:(0.29,0.33,0.18,0.37),6.5:(0.1,0.29,0.7,0.68),7.0:(0.1,0.3,0.6,0.67)}
c={"mediaId":5461,"level":"B","keyWord":"ballot","defaultVoice":"male",
"taps":[{"phrase":"to wear a yellow blouse","target":"the woman in yellow","voice":"female","keys":K(yel)},
{"phrase":"to have a tattooed chest","target":"the tattooed man","voice":"male","keys":K(tat)},
{"phrase":"to sit in a wheelchair","target":"the woman in the wheelchair","voice":"female","keys":K(whe)}],
"stillS":6.5,
"nouns":[{"word":"an air conditioner","x":0.22,"y":0.14,"voice":"male"},
{"word":"a ballot paper","x":0.52,"y":0.4,"voice":"male"},
{"word":"a ballot box","x":0.66,"y":0.78,"voice":"male"},
{"word":"a wheelchair","x":0.18,"y":0.84,"voice":"male"}],
"question":"What is the wheelchair user doing?",
"answer":["She","is","dropping","her","ballot","into","the","box."],"answerVoice":"female",
"notes":"All three phrases are states: the only action (posting a paper into the box) is done by everyone. defaultVoice male: mixed group, evenId false. Wheelchair woman hidden behind the queue at 2.5-3.5 and behind the striped-polo man at 5.0-6.0 (only the wheel shows); OFF at 7.5-9.0 (close-up of the box, the hand at 7.5 is not identifiable). The pink-top woman stands behind her at 7.0 inside her box."}
json.dump(c,open('content/5461.json','w'),indent=1)
