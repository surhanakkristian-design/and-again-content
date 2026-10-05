from gen_7297 import K, write, T
truck=[(0.18,0.42,0.17,0.19),(0.18,0.42,0.18,0.19),(0.17,0.42,0.18,0.19),(0.15,0.42,0.17,0.19),
       (0.11,0.42,0.20,0.19),(0.06,0.42,0.20,0.19),(0.01,0.43,0.17,0.23),(0.00,0.43,0.14,0.23)]
hay=[(0.35,0.28,0.56,0.30),(0.36,0.28,0.57,0.30),(0.35,0.28,0.59,0.31),(0.32,0.27,0.60,0.32),
     (0.31,0.27,0.62,0.33),(0.26,0.26,0.63,0.34),(0.18,0.23,0.65,0.36),(0.14,0.20,0.68,0.38)]
shrine=[(0.12,0.62,0.20,0.21),(0.12,0.62,0.20,0.21),(0.11,0.62,0.20,0.21),(0.09,0.62,0.19,0.21),
        (0.03,0.62,0.20,0.21),(0.00,0.62,0.18,0.21),None,None]
write({"mediaId":7300,"level":"B","keyWord":"load","defaultVoice":"female",
 "taps":[{"phrase":"to teeter on the edge","target":"the truck","voice":"female","keys":K(T,truck)},
         {"phrase":"to lean out over the valley","target":"the hay bales","voice":"female","keys":K(T,hay)},
         {"phrase":"to stand among the wildflowers","target":"the shrine","voice":"female","keys":K(T,shrine)}],
 "stillS":0.7,
 "nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"female"},
          {"word":"a load","x":0.63,"y":0.38,"voice":"female"},
          {"word":"a truck","x":0.27,"y":0.52,"voice":"female"},
          {"word":"a shrine","x":0.21,"y":0.73,"voice":"female"}],
 "question":"What is the truck doing?",
 "answer":["It","is","teetering","on","the","edge","of","the","road."],
 "answerVoice":"female",
 "notes":"Truck and its hay load overlap: truck box = cab + front wheel only, hay box = the bale stack (bed and rear wheel partly inside it). Phrase 3 is a state (shrine), no other action target; shrine leaves the frame after 2.7. A tiny goat on the rocks top-left (0.2-1.2) is not used. 'teeter' is the camera-implied tilt; truck does not visibly move."})
