from gen_5575_5576_5578_5579_lib import *
F=[(0.06,0.27,0.46,0.91,(0.33,0.88),(0.25,0.83),(0.31,0.86)),
   (0.07,0.26,0.45,0.93,(0.33,0.89),(0.24,0.84),(0.30,0.88)),
   (0.03,0.27,0.46,0.94,(0.32,0.92),(0.23,0.86),(0.30,0.90)),
   (0.03,0.26,0.46,0.94,(0.32,0.92),(0.23,0.86),(0.29,0.90)),
   (0.00,0.25,0.47,0.98,(0.30,0.96),(0.21,0.90),(0.28,0.94)),
   (0.00,0.23,0.52,1.00,(0.30,0.96),(0.20,0.92),(0.27,0.96)),
   (0.00,0.21,0.61,1.00,(0.29,1.00),(0.21,0.95),(0.26,1.00)),
   (0.00,0.20,0.60,1.00,(0.28,1.00),(0.19,0.96),(0.25,1.00))]
wom=B([(a,w[0],b,w[1]) for a,b,c,d,w,h,m in F])
hor=B([(b,h[0],c,h[1]) for a,b,c,d,w,h,m in F])
man=B([(c,m[0],d,m[1]) for a,b,c,d,w,h,m in F])
write(5575,{"mediaId":5575,"level":"A","keyWord":"ask for permission","defaultVoice":"female",
 "taps":[{"phrase":"to hold the horse","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to touch the horse's head","target":"the man","voice":"male","keys":man},
         {"phrase":"to stand between them","target":"the horse","voice":"female","keys":hor}],
 "stillS":1.2,
 "nouns":[{"word":"a horse","x":0.37,"y":0.56,"voice":"female"},{"word":"a lamp","x":0.73,"y":0.30,"voice":"female"},
          {"word":"flowers","x":0.58,"y":0.39,"voice":"female"},{"word":"boots","x":0.17,"y":0.82,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","touching","the","horse's","head."],"answerVoice":"male",
 "notes":"Key word 'ask for permission' is a phrase, not shown as a noun; the clip only shows him reaching to the horse while looking at her. The man's hand on the horse's head lies in the horse box (split between horse and man boxes at the hand). The horse's body behind the woman is split at her right edge."})
