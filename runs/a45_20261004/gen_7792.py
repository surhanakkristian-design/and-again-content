import sys; sys.path.insert(0,'/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_7790_7792_7793_7795_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
rider=[(0.36,0.41,0.54,0.37),(0.42,0.59,0.58,0.41),(0.80,0.62,0.20,0.36),(0.44,0.41,0.46,0.21),
       (0.48,0.35,0.38,0.15),(0.52,0.35,0.38,0.16),(0.50,0.37,0.29,0.17),(0.44,0.40,0.25,0.21)]
cap=[(0.42,0.18,0.40,0.21),(0.39,0.10,0.40,0.23),(0.28,0.19,0.22,0.30),(0.0,0.20,0.28,0.33),None,None,None,None]
write(7792,{"mediaId":7792,"level":"B","keyWord":"cycle","defaultVoice":"male",
 "taps":[{"phrase":"to ride around the steep wall","target":"the rider","voice":"male","keys":K(T,rider)},
         {"phrase":"to wear a protective helmet","target":"the rider","voice":"male","keys":K(T,rider)},
         {"phrase":"to wave a red flag","target":"the man in the flat cap","voice":"male","keys":K(T,cap)}],
 "stillS":2.7,
 "nouns":[{"word":"a big wheel","x":0.50,"y":0.19,"voice":"male"},
          {"word":"smoke","x":0.28,"y":0.40,"voice":"male"},
          {"word":"a motorbike","x":0.74,"y":0.44,"voice":"male"},
          {"word":"a spectator","x":0.50,"y":0.70,"voice":"female"}],
 "question":"What is the rider doing?",
 "answer":["He","is","riding","around","the","steep","wall."],
 "answerVoice":"male",
 "notes":"Key word cycle is abstract, not placed. Spectators all cheer/clap, so no spectator phrase. Flat-cap man only in the first shot (0.2-1.7); at 1.7 only his head top-left and the flag, his arm hidden behind the cheering woman. Rider blurred at 0.7 and 1.2 (bottom right). 'a big wheel' (Ferris wheel) only visible at 2.7, small and glowing."})
