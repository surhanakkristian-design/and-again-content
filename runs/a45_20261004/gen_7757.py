import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
M=k([(0.47,0.40,0.98,0.98),(0.48,0.40,0.97,0.98),(0.49,0.40,0.98,0.98),(0.50,0.40,0.97,0.98),(0.48,0.40,0.95,0.98),(0.45,0.40,0.93,0.98),(0.44,0.40,0.89,0.98),(0.44,0.40,0.89,0.98)])
S=k([(0.0,0.01,1.0,0.40)]*8)
d={"mediaId":7757,"level":"B","keyWord":"background","defaultVoice":"male",
 "taps":[{"phrase":"to spray the tomato plants","target":"the man","voice":"male","keys":M},
  {"phrase":"to hold up ripe tomatoes","target":"the man","voice":"male","keys":M},
  {"phrase":"to glide past the garden","target":"the cruise ship","voice":"male","keys":S}],
 "stillS":2.2,
 "nouns":[{"word":"a cruise ship","x":0.30,"y":0.25,"voice":"male"},{"word":"tomatoes","x":0.88,"y":0.65,"voice":"male"},
  {"word":"a deckchair","x":0.44,"y":0.60,"voice":"male"},{"word":"a watering can","x":0.20,"y":0.79,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","spraying","the","tomato","plants","with","a","hose."],"answerVoice":"male",
 "notes":"Only two targets (man, ship): man used twice. Ship box cut at y 0.40 where the man's head overlaps the hull. Key word 'background' is abstract, not placed as a noun. Ship drifts slowly right (glide past)."}
json.dump(d,open('content/7757.json','w'),indent=1)
