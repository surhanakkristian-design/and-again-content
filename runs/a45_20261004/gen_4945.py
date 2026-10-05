import json
T=[i*0.5 for i in range(19)]
W=[(0,0.18,1.0,0.82),(0,0.14,1.0,0.86),(0,0.08,1.0,0.92),(0,0.18,0.92,0.82),(0,0.18,0.97,0.82),(0,0.24,0.97,0.76),(0.02,0.23,0.95,0.77),None,None,
(0.05,0.22,0.95,0.78),(0,0.20,1.0,0.80),(0,0.18,1.0,0.82),(0,0.24,1.0,0.76),(0,0.27,1.0,0.73),(0,0.28,1.0,0.72),(0,0.28,1.0,0.72),
(0,0.30,0.62,0.70),(0,0.28,0.57,0.72),(0,0.37,0.63,0.63)]
M=[None]*7+[(0.02,0.18,0.98,0.74),(0,0.18,1.0,0.74)]+[None]*7+[(0.63,0.49,0.23,0.27),(0.60,0.48,0.37,0.28),(0.82,0.48,0.18,0.24)]
def ks(L): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,L)]
taps=[{"phrase":"to sing into a microphone","target":"the woman","voice":"female","keys":ks(W)},
{"phrase":"to put on headphones","target":"the woman","voice":"female","keys":ks(W)},
{"phrase":"to clap his hands","target":"the man","voice":"male","keys":ks(M)}]
c={"mediaId":4945,"level":"A","keyWord":"sing","defaultVoice":"female","taps":taps,"stillS":3.0,
"nouns":[{"word":"lights","x":0.12,"y":0.23,"voice":"female"},{"word":"a microphone","x":0.80,"y":0.24,"voice":"female"},{"word":"headphones","x":0.29,"y":0.35,"voice":"female"},{"word":"a T-shirt","x":0.40,"y":0.74,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","singing","into","a","microphone."],"answerVoice":"female",
"notes":"Man is clapping only small behind the glass at 8.0-9.0 s; at 3.5-4.0 s he is at the desk (big). Man set off at 4.5 s (blurred far background, overlaps her arm) and 5.0-7.5 s (not clearly visible). 'to put on headphones' = 0.0-1.0 s."}
json.dump(c,open('content/4945.json','w'),indent=1)
