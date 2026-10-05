from gen_5340_5342_5343_5344_lib import K, write
N=None
T=[i*0.5 for i in range(19)]
def track(d): return K([(t,)+d[t] if t in d else (t,N) for t in T])
sc=track({5.0:(0.25,0.36,0.75,0.22)})
fl=track({3.5:(0.28,0.38,0.50,0.28),4.0:(0.26,0.38,0.50,0.30),4.5:(0.27,0.38,0.53,0.30)})
qu=track({6.0:(0.05,0.66,0.95,0.34),6.5:(0.12,0.61,0.88,0.39),7.0:(0.04,0.59,0.96,0.41),7.5:(0.08,0.48,0.90,0.50),
 8.0:(0.09,0.39,0.80,0.53),8.5:(0.11,0.40,0.81,0.51),9.0:(0.13,0.41,0.80,0.52)})
write(5344,{"mediaId":5344,"level":"B","keyWord":"quilt","defaultVoice":"female",
 "taps":[
  {"phrase":"to snip a loose thread","target":"the scissors","voice":"female","keys":sc},
  {"phrase":"to decorate the white linen","target":"the embroidered flower","voice":"female","keys":fl},
  {"phrase":"to be held up proudly","target":"the patchwork quilt","voice":"female","keys":qu}],
 "stillS":8.0,
 "nouns":[{"word":"a patchwork quilt","x":0.50,"y":0.62,"voice":"female"},{"word":"spools","x":0.40,"y":0.15,"voice":"female"},
  {"word":"a window","x":0.88,"y":0.12,"voice":"female"},{"word":"a rug","x":0.25,"y":0.95,"voice":"female"}],
 "question":"What are the women showing?",
 "answer":["They","are","showing","a","patchwork","quilt."],
 "answerVoice":"female",
 "notes":"Montage of close-ups with hands only, then a group of ~10 young women, so all three targets are things. The scissors (description says pocket knife; frames show scissors) are visible only at 5.0. The flower is visible 3.5-4.5. Many people in the group shot, none used as target."})
