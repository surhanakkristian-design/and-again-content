import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.13,0.38,0.77,0.40),(0.13,0.38,0.79,0.45),(0.12,0.38,0.85,0.50),(0.10,0.37,0.90,0.54),(0.08,0.30,0.92,0.70),(0.07,0.29,0.93,0.71),(0.03,0.30,0.97,0.70),(0.03,0.29,0.97,0.71)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,man)]
taps=[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to go to sleep","to drop a book","to lie in a hammock"]]
c={"mediaId":7187,"level":"A","keyWord":"go to sleep","defaultVoice":"male","taps":taps,"stillS":0.2,
"nouns":[{"word":"trees","x":0.50,"y":0.12,"voice":"male"},{"word":"a man","x":0.24,"y":0.46,"voice":"male"},
{"word":"a book","x":0.61,"y":0.77,"voice":"male"},{"word":"a rope","x":0.66,"y":0.93,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","going","to","sleep","in","a","hammock."],"answerVoice":"male",
"notes":"Only one target (the man); the book is visible only at 0.2 while falling, so all three phrases use the man. Box includes the hammock he lies in. Still 0.2: book in the air under his hand."}
json.dump(c,open('content/7187.json','w'),indent=1)
