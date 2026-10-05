import sys; sys.path.insert(0,'.')
from gen_5254 import write
times=[i*0.5 for i in range(19)]
W={0.0:(0,0.25,0.92,0.75),0.5:(0,0.24,1.0,0.76),1.0:(0,0.23,1.0,0.77),1.5:(0,0.23,0.88,0.77),2.0:(0.02,0.24,0.78,0.76),
   2.5:(0,0.26,1.0,0.74),3.0:(0,0.27,0.76,0.73),3.5:(0,0.27,0.95,0.73),4.0:(0,0.27,0.96,0.73),4.5:(0,0.26,0.90,0.74),
   5.0:(0,0.27,0.85,0.73),5.5:(0,0.29,0.92,0.71),6.0:(0,0.30,0.86,0.70),6.5:(0.02,0.32,0.80,0.68),7.0:(0,0.33,0.75,0.67),
   7.5:(0,0.35,0.80,0.65),8.0:(0,0.36,0.90,0.64),8.5:(0,0.37,0.84,0.63),9.0:(0,0.39,0.74,0.61)}
L={}
for t,(x,y,w,h) in W.items():
    top={0.0:0.10,0.5:0.09,1.0:0.10,1.5:0.10,2.0:0.09,2.5:0.09,3.0:0.10,3.5:0.11,4.0:0.10,4.5:0.09,5.0:0.10,5.5:0.10,
         6.0:0.11,6.5:0.11,7.0:0.12,7.5:0.11,8.0:0.12,8.5:0.13,9.0:0.14}[t]
    L[t]=(0.0,top,1.0,round(y-top,2))
c={"mediaId":5258,"level":"A","keyWord":"bar","defaultVoice":"female","stillS":2.0,
 "nouns":[{"word":"lights","x":0.35,"y":0.20,"voice":"female"},{"word":"a woman","x":0.18,"y":0.70,"voice":"female"},
          {"word":"a bar","x":0.82,"y":0.68,"voice":"female"},{"word":"a glass","x":0.79,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","making","drinks","at","the","bar."],"answerVoice":"female",
 "notes":"Everyone along the counter shakes a shaker, so no shaker phrase is unique; the woman gets 'to laugh out loud' (the men behind only smile, though one grins at 1.5 - check) and the state 'to have long curly hair'. Lights box = band above the woman's hair (y from the top bulbs down to her hair line), full width; men's heads and palms at the right edge fall partly into it. 'a bar' pill sits on the counter with the glasses."}
write(5258,c,times,[("to laugh out loud","the woman","female",W),("to have long curly hair","the woman","female",W),
                    ("to hang over the bar","the lights","female",L)])
