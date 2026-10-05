import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
rope=[(0.74,0.21,0.20,0.20),(0.74,0.22,0.19,0.20),(0.76,0.24,0.20,0.23),(0.76,0.21,0.20,0.24),
      (0.77,0.19,0.20,0.23),(0.77,0.19,0.20,0.22),(0.78,0.21,0.20,0.22),(0.82,0.21,0.18,0.22)]
torch=[(0.70,0.45,0.24,0.26),(0.70,0.46,0.25,0.26),(0.70,0.48,0.26,0.23),(0.72,0.47,0.26,0.25),
       (0.73,0.45,0.27,0.27),(0.73,0.45,0.27,0.27),(0.76,0.45,0.24,0.29),(0.78,0.45,0.22,0.29)]
jar=[(0.41,0.31,0.18,0.21),(0.41,0.32,0.18,0.23),(0.40,0.34,0.19,0.23),(0.40,0.37,0.20,0.23),
     (0.39,0.36,0.22,0.25),(0.38,0.36,0.22,0.26),(0.39,0.38,0.23,0.26),(0.38,0.36,0.22,0.28)]
V="male"
c={"mediaId":7481,"level":"B","keyWord":"put back","defaultVoice":V,
 "taps":[{"phrase":"to cling to a rope","target":"the monkey on the rope","voice":V,"keys":K(rope)},
         {"phrase":"to hold a lit torch","target":"the monkey on the crate","voice":V,"keys":K(torch)},
         {"phrase":"to dangle in a sling","target":"the clay jar","voice":V,"keys":K(jar)}],
 "stillS":2.7,
 "nouns":[{"word":"a skylight","x":0.50,"y":0.16,"voice":V},{"word":"a clay jar","x":0.50,"y":0.48,"voice":V},
          {"word":"a stepladder","x":0.12,"y":0.64,"voice":V},{"word":"a pedestal","x":0.50,"y":0.74,"voice":V}],
 "question":"Where are the monkeys putting the jar?",
 "answer":["They","are","putting","it","back","on","the","pedestal."],"answerVoice":V,
 "notes":"Two aproned monkeys with white gloves guide the jar down 0.2-3.2; it stands on the pedestal at 3.2-3.7 but is still in the rope sling (dangle is true mostly 0.2-2.7). Rope monkey climbs/hangs on the rope at the right edge throughout; it clings to the rope with hands and feet. Torch monkey on the crate also holds a board. A close-up monkey in the foreground 0.2-2.2 and one sitting in the water are not used. 'the monkeys' in the question = the two on the pedestal."}
json.dump(c,open('content/7481.json','w'),indent=1)
