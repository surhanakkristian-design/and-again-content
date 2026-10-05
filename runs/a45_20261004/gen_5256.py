import sys; sys.path.insert(0,'.')
from gen_5254 import write
times=[i*0.5 for i in range(21)]
J={0.0:(0.38,0.45,0.21,0.14),0.5:(0.37,0.42,0.24,0.18),1.0:(0.36,0.43,0.25,0.18),1.5:(0.36,0.43,0.26,0.19),
   2.0:(0.36,0.43,0.26,0.21),2.5:(0.35,0.43,0.27,0.21),3.0:(0.35,0.43,0.28,0.23),3.5:(0.35,0.43,0.28,0.23),4.0:(0.35,0.43,0.29,0.23)}
for t in [4.5,5.0,5.5,6.0,6.5,7.0,8.0,8.5,9.0]: J[t]=(0.35,0.43,0.30,0.24)
J[7.5]=(0.33,0.43,0.33,0.24); J[9.5]=(0.39,0.45,0.24,0.18); J[10.0]=(0.44,0.46,0.18,0.14)
M={0.0:(0.51,0.59,0.18,0.14),0.5:(0.50,0.60,0.20,0.18),1.0:(0.51,0.62,0.21,0.20),1.5:(0.51,0.63,0.21,0.20),
   2.0:(0.51,0.66,0.24,0.22),2.5:(0.51,0.66,0.24,0.22),3.0:(0.51,0.67,0.27,0.23),3.5:(0.51,0.67,0.27,0.23),4.0:(0.53,0.67,0.26,0.23)}
for t in [4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]: M[t]=(0.52,0.67,0.27,0.23)
M[9.5]=(0.52,0.64,0.21,0.19); M[10.0]=(0.51,0.61,0.18,0.14)
c={"mediaId":5256,"level":"B","keyWord":"address","defaultVoice":"male","stillS":4.0,
 "nouns":[{"word":"a coat of arms","x":0.44,"y":0.34,"voice":"male"},{"word":"a judge","x":0.50,"y":0.49,"voice":"male"},
          {"word":"a lectern","x":0.50,"y":0.61,"voice":"male"}],
 "question":"What is the judge in red doing?","answer":["He","is","addressing","the","court."],"answerVoice":"male",
 "notes":"One continuous wide shot, small figures. The judge in red stands at the lectern reading from notes; five wigged judges sit behind him (not targets). Standing man = dark-haired man in a suit with his back to the camera at the front table, an empty chair in front of him; he seems to be standing already at 0.0 (the description says he stands up), so 'to stand facing the judge'. The bald man on the right also seems to stand but faces the camera. The 'a coat of arms' pill sits on the carved crest above the judge's chair; only 3 nouns because the wigs/judges in the row are many and close together."}
write(5256,c,times,[("to address the court","the judge in red","male",J),("to read from his notes","the judge in red","male",J),
                    ("to stand facing the judge","the standing man","male",M)])
