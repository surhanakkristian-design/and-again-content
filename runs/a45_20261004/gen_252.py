import json
T=[i*0.5 for i in range(21)]
N=None
woman=[(0.52,0.48,0.48,0.40),(0.57,0.47,0.43,0.35),(0.57,0.46,0.43,0.54),(0.51,0.47,0.49,0.53),(0.40,0.48,0.42,0.52),(0.21,0.56,0.33,0.44),(0.10,0.53,0.38,0.47),(0.03,0.51,0.44,0.49),(0,0.26,0.47,0.74),(0,0.28,0.47,0.72),(0,0.37,0.47,0.63),(0,0.36,0.48,0.64),(0,0.38,0.46,0.62),(0,0.39,0.47,0.61),(0,0.42,0.40,0.58),(0,0.42,0.45,0.58),(0,0.33,0.36,0.67),(0,0.43,0.45,0.57),(0,0.42,0.45,0.58),(0,0.44,0.45,0.56),(0,0.47,0.42,0.53)]
man=[N,N,N,N,N,(0.56,0.52,0.44,0.30),(0.50,0.50,0.50,0.34),(0.48,0.27,0.52,0.73),(0.48,0.20,0.52,0.80),(0.48,0.26,0.52,0.74),(0.48,0.32,0.52,0.68),(0.49,0.34,0.51,0.66),(0.47,0.36,0.53,0.64),(0.48,0.38,0.52,0.62),(0.48,0.39,0.52,0.61),(0.50,0.40,0.50,0.60),(0.50,0.39,0.50,0.61),(0.50,0.42,0.50,0.58),(0.50,0.47,0.50,0.53),(0.52,0.46,0.48,0.54),(0.55,0.44,0.45,0.56)]
bird=[N]*9+[(0.76,0.01,0.22,0.15),(0.68,0.11,0.22,0.15),(0.65,0.15,0.22,0.15),(0.63,0.18,0.22,0.15),(0.62,0.20,0.22,0.15),(0.63,0.21,0.22,0.15),(0.62,0.22,0.22,0.15),(0.60,0.22,0.22,0.15),(0.63,0.21,0.24,0.16),N,N,N]
def keys(b): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,b)]
c={"mediaId":252,"level":"A","keyWord":"dust","defaultVoice":"female",
"taps":[{"phrase":"to blow on a suitcase","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to hold up one finger","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to sit high up","target":"the bird","voice":"female","keys":keys(bird)}],
"stillS":7.5,
"nouns":[{"word":"dust","x":0.35,"y":0.22,"voice":"female"},{"word":"a man","x":0.84,"y":0.68,"voice":"male"},{"word":"a woman","x":0.16,"y":0.80,"voice":"female"},{"word":"a suitcase","x":0.70,"y":0.87,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","blowing","dust","off","a","suitcase."],"answerVoice":"male",
"notes":"0-2 s show only a hand drawing a line in the dust; the bare arm with the raised finger belongs to the woman (seen from 4.0 s), so her box follows that arm from the start; the man's coated hand enters at 2.5. The thing he holds is a small old case: 'suitcase' follows the description, could be read as a box. The bird on the beam is small, visible 4.5-8.5 s (partly behind the dust cloud at 7.0-7.5). The woman's raised finger is clear 2.0-6.5 s; afterwards she waves an open hand. defaultVoice female: mixed pair, evenId true."}
json.dump(c,open('content/252.json','w'),indent=1)
