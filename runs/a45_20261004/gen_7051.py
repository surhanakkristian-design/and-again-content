import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
man=K([(0.30,0.0,0.40,0.43),(0.31,0.0,0.39,0.45),(0.32,0.0,0.38,0.53),(0.33,0.0,0.35,0.65),
       (0.32,0.10,0.37,0.62),(0.33,0.14,0.36,0.63),(0.33,0.16,0.35,0.62),(0.34,0.16,0.35,0.62)])
sofa=K([(0.03,0.13,0.27,0.22),(0.03,0.16,0.28,0.20),(0.03,0.26,0.29,0.22),(0.03,0.36,0.30,0.21),
        (0.03,0.43,0.29,0.21),(0.03,0.46,0.30,0.21),(0.03,0.48,0.30,0.21),(0.03,0.48,0.30,0.21)])
wom=K([(0.70,0.05,0.18,0.29),(0.70,0.08,0.18,0.29),(0.70,0.19,0.18,0.27),(0.70,0.29,0.18,0.27),
       (0.70,0.37,0.18,0.26),(0.70,0.39,0.18,0.27),(0.70,0.40,0.18,0.27),(0.70,0.41,0.18,0.27)])
c={"mediaId":7051,"level":"A","keyWord":"do the cleaning","defaultVoice":"male",
 "taps":[{"phrase":"to hold a black bag","target":"the man","voice":"male","keys":man},
         {"phrase":"to sleep on the sofa","target":"the people on the sofa","voice":"male","keys":sofa},
         {"phrase":"to stand by the door","target":"the woman","voice":"female","keys":wom}],
 "stillS":3.7,
 "nouns":[{"word":"a T-shirt","x":0.48,"y":0.38,"voice":"male"},{"word":"a bag","x":0.62,"y":0.60,"voice":"male"},
          {"word":"a sofa","x":0.16,"y":0.64,"voice":"male"},{"word":"the floor","x":0.50,"y":0.92,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","doing","the","cleaning."],"answerVoice":"male",
 "notes":"Sofa target is a pair of sleepers (group). Woman in the doorway is small; box padded to minimum size. Two lampshades hang, so no lamp noun."}
json.dump(c,open('content/7051.json','w'),indent=1)
