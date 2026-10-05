import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
cat=[(0.12,0.28,0.62,0.47),(0.14,0.27,0.63,0.46),(0.12,0.27,0.52,0.45),(0.16,0.17,0.50,0.45),
     (0.10,0.15,0.66,0.58),(0.09,0.06,0.66,0.75),(0.08,0.16,0.76,0.58),(0.17,0.15,0.67,0.73)]
V="female"
c={"mediaId":7478,"level":"B","keyWord":"kitty","defaultVoice":V,
 "taps":[{"phrase":"to lounge on the windowsill","target":"the kitty","voice":V,"keys":K(cat)},
         {"phrase":"to dangle a front paw","target":"the kitty","voice":V,"keys":K(cat)},
         {"phrase":"to stroll along the windowsill","target":"the kitty","voice":V,"keys":K(cat)}],
 "stillS":0.2,
 "nouns":[{"word":"a kitty","x":0.30,"y":0.42,"voice":V},{"word":"a windowsill","x":0.24,"y":0.63,"voice":V},
          {"word":"a wicker basket","x":0.72,"y":0.68,"voice":V},{"word":"a ball of wool","x":0.58,"y":0.86,"voice":V}],
 "question":"What is the kitty doing?",
 "answer":["The","kitty","is","strolling","along","the","windowsill."],"answerVoice":V,
 "notes":"Only one animal/person in the clip, so all three phrases target the cat. Lounging with a front paw dangling over the sill edge 0.2-0.7; gets up 1.2, strolls along the sill 1.7-3.2, sits upright 3.7. Question 'doing' covers the middle (strolling) part; at the very start it is lying."}
json.dump(c,open('content/7478.json','w'),indent=1)
