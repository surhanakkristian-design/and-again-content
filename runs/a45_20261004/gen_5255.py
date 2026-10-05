import sys; sys.path.insert(0,'.')
from gen_5254 import write
times=[i*0.5 for i in range(19)]
J={0.0:(0.0,0.25,0.92,0.36),0.5:(0.02,0.25,0.90,0.36),1.0:(0.0,0.27,0.88,0.34),1.5:(0.02,0.27,0.88,0.34),
   2.0:(0.0,0.26,0.88,0.36),2.5:(0.0,0.26,0.88,0.36),3.0:(0.0,0.28,0.92,0.35),
   3.5:(0.0,0.67,1.0,0.30),4.0:(0.0,0.66,1.0,0.29),4.5:(0.0,0.66,1.0,0.30),5.0:(0.0,0.67,1.0,0.29),5.5:(0.0,0.62,1.0,0.35),6.0:(0.0,0.62,1.0,0.33),
   6.5:(0.0,0.35,1.0,0.38),7.0:(0.0,0.28,0.58,0.35),7.5:(0.0,0.29,0.58,0.34),8.0:(0.02,0.35,0.28,0.15),8.5:(0.07,0.36,0.27,0.14),9.0:(0.05,0.38,0.27,0.14)}
M={0.0:(0.15,0.61,0.74,0.33),0.5:(0.15,0.61,0.72,0.33),1.0:(0.13,0.62,0.74,0.32),1.5:(0.13,0.62,0.74,0.32),
   2.0:(0.13,0.62,0.74,0.32),2.5:(0.13,0.62,0.74,0.32),3.0:(0.12,0.63,0.74,0.32),
   3.5:(0.18,0.31,0.62,0.36),4.0:(0.20,0.31,0.58,0.35),4.5:(0.20,0.31,0.60,0.35),5.0:(0.15,0.31,0.65,0.36),5.5:(0.20,0.32,0.50,0.30),6.0:(0.25,0.32,0.50,0.30),
   8.0:(0.48,0.44,0.18,0.16),8.5:(0.48,0.44,0.18,0.16),9.0:(0.48,0.45,0.19,0.17)}
c={"mediaId":5255,"level":"B","keyWord":"guilty","defaultVoice":"female","stillS":2.0,
 "nouns":[{"word":"a coat of arms","x":0.50,"y":0.26,"voice":"female"},{"word":"a judge","x":0.50,"y":0.37,"voice":"female"},
          {"word":"a gavel","x":0.10,"y":0.53,"voice":"female"},{"word":"a microphone","x":0.86,"y":0.48,"voice":"female"}],
 "question":"What is the young man doing?","answer":["He","is","staring","up","at","the","judge."],"answerVoice":"male",
 "notes":"Key word 'guilty' is not shown (only heard/implied), so it is not used. Judge: 0-3.0 at the bench; 3.5-6.0 only her red sleeve, hand and gavel in the foreground (box = bottom strip under the man's chin; at 5.5 the raised gavel head above y 0.62 is outside her box to keep it apart from the man's box); 6.5 only her hand and gavel; 7.0-9.0 small at left. Young man: 0-3.0 back of his head at bottom, 3.5-6.0 close-up face, off 6.5-7.5, 8.0-9.0 small seated figure in the wide shot (assumed the same man). The judge noun at 2.0 sits on her face/hair."}
write(5255,c,times,[("to bang the gavel","the judge","female",J),("to study a document","the judge","female",J),
                    ("to stare up in shock","the young man","male",M)])
