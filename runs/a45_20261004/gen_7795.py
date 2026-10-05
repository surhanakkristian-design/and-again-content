import sys; sys.path.insert(0,'/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_7790_7792_7793_7795_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
w2=[(0.31,0.28,0.36,0.22)]*8
cat2=[(0.69,0.36,0.27,0.14)]*8
w4=[(0.29,0.81,0.33,0.19)]*8
write(7795,{"mediaId":7795,"level":"A","keyWord":"day","defaultVoice":"female",
 "taps":[{"phrase":"to sleep under a blanket","target":"the woman at the bottom","voice":"female","keys":K(T,w4)},
         {"phrase":"to put her feet up","target":"the woman in the second picture","voice":"female","keys":K(T,w2)},
         {"phrase":"to lie on the wall","target":"the cat in the second picture","voice":"female","keys":K(T,cat2)}],
 "stillS":0.2,
 "nouns":[{"word":"a cat","x":0.77,"y":0.15,"voice":"female"},
          {"word":"the sea","x":0.82,"y":0.35,"voice":"female"},
          {"word":"a hat","x":0.40,"y":0.36,"voice":"female"},
          {"word":"a blanket","x":0.50,"y":0.92,"voice":"female"}],
 "question":"What is she doing in the evening?",
 "answer":["She","is","sleeping","under","a","blanket."],
 "answerVoice":"female",
 "notes":"Split screen: the same woman and the same cat appear in all four stacked scenes, so targets are named by scene. 'to put her feet up' = second scene, her feet rest on the wall (literal and idiomatic). Only the cat in the second scene lies down; the others sit. Key word 'day' is abstract (morning to dusk), not placed. 'a cat' pill on the top cat; three more cats are in the picture but no other noun labels them."})
