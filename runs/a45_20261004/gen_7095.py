import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
blue=K([(0.52,0.28,0.48,0.47),(0.60,0.25,0.40,0.51),(0.46,0.27,0.52,0.53),(0.36,0.31,0.62,0.44),(0.0,0.36,0.53,0.40),None])
red=K([(0.0,0.28,0.46,0.47),(0.0,0.26,0.34,0.50),(0.0,0.25,0.28,0.56),None,None,None])
dog=K([None,None,(0.28,0.29,0.17,0.14),(0.19,0.28,0.17,0.15),None,(0.14,0.32,0.20,0.15)])
c={"mediaId":7095,"level":"B","keyWord":"face off","defaultVoice":"female",
"taps":[{"phrase":"to skate off with the puck","target":"the player in blue","voice":"female","keys":blue},
{"phrase":"to wear a red jersey","target":"the player in red","voice":"female","keys":red},
{"phrase":"to sit among the spectators","target":"the dog","voice":"female","keys":dog}],
"stillS":2.7,
"nouns":[{"word":"a lantern","x":0.33,"y":0.28,"voice":"female"},{"word":"a dog","x":0.24,"y":0.41,"voice":"female"},
{"word":"a drum","x":0.66,"y":0.40,"voice":"female"},{"word":"a snow bank","x":0.50,"y":0.55,"voice":"female"}],
"question":"What is the player in blue doing?","answer":["She","is","skating","off","with","the","puck."],"answerVoice":"female",
"notes":"Face-off 0.2-0.7 s, the player in blue takes the puck at 1.2 s and skates off; 2.7 s shows only the crowd. Red player phrase is a state (no action fits only her: both crouch). Dog appears from 1.2 s, small, behind the snow bank; at 1.2/1.7 its box is narrowed to stay clear of the players; at 2.2 s the dog is half hidden behind the blue helmet, so it is off there. Key word 'face off' is a phrasal verb, not placed."}
json.dump(c,open('content/7095.json','w'),indent=1)
