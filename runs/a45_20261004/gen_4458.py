from gen_4457 import write
M={0.0:(0.53,0.04,1.0,0.55),0.5:(0.55,0.04,1.0,0.48),1.0:(0.48,0.05,1.0,0.51),1.5:(0.38,0.08,1.0,0.65),
2.0:(0.22,0.08,1.0,0.82),2.5:(0.15,0.08,1.0,0.86),3.0:(0.10,0.08,1.0,0.95),3.5:(0.17,0.05,1.0,0.95),
4.0:(0.17,0.03,1.0,0.85),4.5:(0.27,0.10,1.0,0.90),5.0:(0.47,0.17,1.0,1.0),5.5:(0.38,0.22,1.0,1.0),
6.0:(0.42,0.20,1.0,1.0),6.5:(0.48,0.14,1.0,1.0),7.0:(0.60,0.08,1.0,1.0),7.5:(0.44,0.10,1.0,1.0),
8.0:(0.50,0.09,1.0,1.0),8.5:(0.40,0.10,1.0,1.0),9.0:(0.36,0.14,1.0,1.0),9.5:(0.30,0.18,1.0,1.0),
10.0:(0.46,0.18,1.0,1.0),10.5:(0.47,0.15,1.0,1.0),11.0:(0.52,0.15,1.0,1.0),11.5:(0.52,0.16,1.0,1.0),12.0:(0.48,0.16,1.0,1.0)}
T={0.0:(0.08,0.56,0.78,0.80),0.5:(0.08,0.49,0.82,0.78),1.0:(0.04,0.52,0.78,0.82),1.5:(0.06,0.66,0.66,1.0)}
C={6.5:(0.15,0.63,0.42,0.80),7.0:(0.08,0.64,0.42,0.83),7.5:(0.05,0.64,0.40,0.83),8.0:(0.05,0.65,0.40,0.84),
8.5:(0.05,0.64,0.39,0.84),9.0:(0.02,0.66,0.35,0.84),9.5:(0.02,0.66,0.29,0.84),10.0:(0.06,0.66,0.40,0.85),
10.5:(0.06,0.66,0.40,0.85),11.0:(0.06,0.66,0.40,0.86),11.5:(0.06,0.66,0.40,0.86),12.0:(0.03,0.68,0.38,0.88)}
c={"mediaId":4458,"level":"B","keyWord":"disaster","defaultVoice":"male",
 "taps":[
  {"phrase":"to wave a tea towel","target":"the man","voice":"male","k":"M"},
  {"phrase":"to pop up burnt","target":"the toast","voice":"male","k":"T"},
  {"phrase":"to roast in the oven","target":"the chicken","voice":"male","k":"C"}],
 "stillS":3.0,
 "nouns":[{"word":"a cupboard","x":0.16,"y":0.22,"voice":"male"},
          {"word":"a spatula","x":0.26,"y":0.64,"voice":"male"},
          {"word":"an apron","x":0.68,"y":0.52,"voice":"male"},
          {"word":"a frying pan","x":0.45,"y":0.80,"voice":"male"}],
 "question":"What is the man waving?",
 "answer":["He","is","waving","a","towel","at","the","smoke."],
 "answerVoice":"male",
 "notes":"Clip has cuts/pans: toast only 0-1.5 s (toaster in the foreground), chicken only from 6.5 s (dark in the open oven, dim through smoke; at 6.0 s the oven is open but the bird is not yet readable, so off). Man's box is cut at the toast's top edge at 0-1.5 s and at 9.0 s on the left, where the raised towel reaches over the oven (half of the towel outside his box). The key word 'disaster' is not a visible thing, so it is not in the answer; the question asks about the towel he waves at the smoke (8.5-9.5 s). A second towel hangs on the oven door, so no towel noun. The bird could be a chicken or small turkey."}
write(4458,c,{"M":M,"T":T,"C":C})
