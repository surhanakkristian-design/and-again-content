import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
chef=[(0.12,0.34,0.38,0.64),(0.12,0.34,0.38,0.64),(0.10,0.35,0.40,0.63),(0.10,0.35,0.33,0.63),(0.06,0.34,0.34,0.64),(0.0,0.33,0.30,0.65),(0.0,0.34,0.18,0.62)]
fish=[(0.50,0.55,0.40,0.20),(0.50,0.55,0.40,0.20),(0.50,0.55,0.42,0.20),(0.43,0.56,0.47,0.19),(0.40,0.56,0.50,0.19),(0.30,0.57,0.60,0.19),(0.18,0.57,0.52,0.20)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7314,"level":"A","keyWord":"main course","defaultVoice":"male",
"taps":[{"phrase":"to cut the fish","target":"the chef","voice":"male","keys":k(chef)},
{"phrase":"to hold a big knife","target":"the chef","voice":"male","keys":k(chef)},
{"phrase":"to lie on a board","target":"the fish","voice":"male","keys":k(fish)}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":0.5,"y":0.10,"voice":"male"},{"word":"candles","x":0.52,"y":0.50,"voice":"male"},
{"word":"a main course","x":0.55,"y":0.65,"voice":"male"},{"word":"a board","x":0.80,"y":0.77,"voice":"male"}],
"question":"What is the chef doing?","answer":["He","is","cutting","the","fish."],"answerVoice":"male",
"notes":"Chef and fish boxes split at the cleaver/apron line; fish tail behind chef's arm falls in chef box. Second chef and hand at bottom right also hold the board, so no board-holding phrase."}
json.dump(c,open('content/7314.json','w'),indent=1)
