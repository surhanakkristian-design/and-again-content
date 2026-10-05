import sys; sys.path.insert(0,'/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_7790_7792_7793_7795_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7]
woman=[(0.59,0.37,0.26,0.17),(0.60,0.39,0.26,0.18),(0.61,0.45,0.25,0.17),(0.63,0.48,0.24,0.16),(0.70,0.50,0.21,0.19),(0.70,0.51,0.22,0.19)]
man=[(0.62,0.23,0.22,0.14),(0.65,0.27,0.20,0.12),(0.66,0.31,0.20,0.14),(0.67,0.32,0.21,0.16),(0.70,0.37,0.19,0.13),(0.70,0.39,0.20,0.12)]
skater=[None,None,None,(0.45,0.38,0.18,0.16),(0.06,0.27,0.38,0.47),(0.0,0.16,0.27,0.70)]
write(7793,{"mediaId":7793,"level":"B","keyWord":"date back","defaultVoice":"female",
 "taps":[{"phrase":"to kneel on the glass floor","target":"the woman in red","voice":"female","keys":K(T,woman)},
         {"phrase":"to touch the marble column","target":"the man in beige","voice":"male","keys":K(T,man)},
         {"phrase":"to balance on a skateboard","target":"the man in blue","voice":"male","keys":K(T,skater)}],
 "stillS":1.7,
 "nouns":[{"word":"a pigeon","x":0.71,"y":0.09,"voice":"female"},
          {"word":"a column","x":0.65,"y":0.33,"voice":"female"},
          {"word":"a tram","x":0.13,"y":0.43,"voice":"female"},
          {"word":"a mosaic","x":0.66,"y":0.78,"voice":"female"}],
 "question":"What is the woman in red doing?",
 "answer":["She","is","kneeling","on","the","glass","floor."],
 "answerVoice":"female",
 "notes":"Key word 'date back' is a phrasal verb, not placed. Skater only appears from 1.7 (small, jumping in the background at the column's left), close and big at 2.2-2.7. Man in beige stands behind the kneeling woman: his box is cut at her head line so the boxes do not overlap (his legs are behind her). Mosaic under the glass is faint at 1.7 - check the pill."})
