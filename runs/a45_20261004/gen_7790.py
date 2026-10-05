import sys; sys.path.insert(0,'/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_7790_7792_7793_7795_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.06,0.0,0.92,1.0),(0.19,0.0,0.79,1.0),(0.18,0.02,0.76,0.98),(0.19,0.03,0.78,0.97),
     (0.20,0.04,0.70,0.96),(0.20,0.05,0.74,0.95),(0.20,0.06,0.66,0.94),(0.22,0.07,0.70,0.93)]
woman=[None,(0.07,0.30,0.12,0.46),(0.05,0.30,0.13,0.45),(0.05,0.30,0.14,0.45),
       (0.02,0.19,0.18,0.56),(0.02,0.20,0.18,0.50),(0.03,0.21,0.17,0.55),(0.06,0.27,0.16,0.52)]
write(7790,{"mediaId":7790,"level":"A","keyWord":"creativity","defaultVoice":"male",
 "taps":[{"phrase":"to play the guitar","target":"the young man","voice":"male","keys":K(T,man)},
         {"phrase":"to carry a suitcase","target":"the young man","voice":"male","keys":K(T,man)},
         {"phrase":"to hold some flowers","target":"the woman","voice":"female","keys":K(T,woman)}],
 "stillS":2.2,
 "nouns":[{"word":"the sky","x":0.20,"y":0.05,"voice":"male"},
          {"word":"a pan","x":0.64,"y":0.11,"voice":"male"},
          {"word":"a guitar","x":0.25,"y":0.55,"voice":"male"},
          {"word":"flowers","x":0.88,"y":0.76,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","playing","the","guitar","in","the","street."],
 "answerVoice":"male",
 "notes":"Key word creativity is abstract, not used as a noun. Woman with tulips mostly hidden behind the musician at 0.2 (off); her face is partly inside the man's box and her box is cut at the guitar's left edge where she stands behind it. Suitcase phrase shares the man's keys; clapping not used because several people clap. 'flowers' pill on the tulip bucket bottom right."})
