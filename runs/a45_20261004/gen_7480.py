import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=[(0.58,0.33,0.38,0.52),(0.52,0.33,0.43,0.52),(0.47,0.33,0.48,0.52),(0.45,0.33,0.49,0.52),
     (0.42,0.33,0.52,0.52),(0.41,0.35,0.52,0.50),(0.43,0.34,0.44,0.50),(0.44,0.34,0.42,0.50)]
door=[(0.30,0.16,0.28,0.66),(0.20,0.16,0.32,0.66),(0.10,0.16,0.37,0.66),(0.07,0.15,0.38,0.67),
      (0.09,0.15,0.33,0.66),(0.08,0.15,0.33,0.67),(0.08,0.17,0.35,0.66),(0.08,0.17,0.36,0.66)]
V="male"
c={"mediaId":7480,"level":"B","keyWord":"put away","defaultVoice":V,
 "taps":[{"phrase":"to heave the door shut","target":"the man at the door","voice":V,"keys":K(man)},
         {"phrase":"to brace his legs","target":"the man at the door","voice":V,"keys":K(man)},
         {"phrase":"to swing shut","target":"the vault door","voice":V,"keys":K(door)}],
 "stillS":0.2,
 "nouns":[{"word":"a ceiling light","x":0.68,"y":0.10,"voice":V},{"word":"a vault door","x":0.42,"y":0.26,"voice":V},
          {"word":"a diamond","x":0.14,"y":0.48,"voice":V},{"word":"a trolley","x":0.86,"y":0.58,"voice":V}],
 "question":"What is the man heaving shut?",
 "answer":["He","is","heaving","the","vault","door","shut."],"answerVoice":V,
 "notes":"Two guards stand behind the man (x ~.55-.70, y .37-.60) at 0.2-2.2, then hidden behind him; they lie inside his box but do nothing matching the phrases. Man/door boxes split at his hands on the wheel. Diamond on the shelf visible only 0.2-1.2 (gone behind the door later), still = 0.2. Key word 'put away' not used as a phrase (nothing is placed; the door is shut)."}
json.dump(c,open('content/7480.json','w'),indent=1)
