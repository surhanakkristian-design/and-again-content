import json
T=[i*0.5 for i in range(21)]
N=None
woman=[N,(0,0.14,0.57,0.58),(0,0.14,0.57,0.58),(0,0.15,0.55,0.58),N,N,N,N,N,N,(0.44,0.29,0.46,0.71),(0.43,0.53,0.57,0.47),(0.49,0.45,0.51,0.55),(0,0.36,0.66,0.64),(0,0.34,0.43,0.60),(0.02,0.30,0.46,0.34),(0.02,0.23,0.48,0.33),(0.06,0.26,0.44,0.30),(0.17,0.29,0.30,0.39),(0.19,0.24,0.26,0.36),(0.17,0.30,0.32,0.28)]
man=[N,(0.58,0.18,0.42,0.54),(0.58,0.16,0.42,0.56),(0.56,0.16,0.44,0.56),N,N,N,N,N,N,(0.09,0,0.34,1.0),(0.09,0.23,0.33,0.77),(0.05,0.49,0.42,0.51),(0.70,0.29,0.30,0.71),(0.65,0.27,0.35,0.73),(0.50,0.22,0.50,0.43),(0.52,0.14,0.48,0.59),(0.51,0.18,0.49,0.52),(0.48,0.21,0.46,0.48),(0.46,0.21,0.50,0.39),(0.50,0.26,0.45,0.33)]
cat=[N]*19+[(0,0.61,0.62,0.20),(0,0.60,0.80,0.21)]
def keys(b): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,b)]
c={"mediaId":253,"level":"A","keyWord":"dusting","defaultVoice":"male",
"taps":[{"phrase":"to clean above the door","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to wear a grey scarf","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to walk on a shelf","target":"the cat","voice":"male","keys":keys(cat)}],
"stillS":10.0,
"nouns":[{"word":"a cat","x":0.35,"y":0.71,"voice":"male"},{"word":"books","x":0.88,"y":0.71,"voice":"male"},{"word":"a shelf","x":0.50,"y":0.57,"voice":"male"},{"word":"a lamp","x":0.82,"y":0.07,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","cleaning","above","the","door."],"answerVoice":"male",
"notes":"Many cuts. 0.0 and 2.0-4.5 s are close-ups of hands with a cloth whose owner cannot be told: both people off there. The woman's phrase is a state (grey headscarf): every action she does (cleaning, thumbs up, laughing) the man does too. The man cleans above the door only at 5.0-5.5 s; at 5.5 his raised arm crosses above the woman, so his box holds head and body but not the hand with the cloth. At 7.5 his pointing hand lies inside the woman's box (split on a vertical line). The cat is on the shelf only at 9.5-10.0 s. defaultVoice male: mixed couple, evenId false."}
json.dump(c,open('content/253.json','w'),indent=1)
