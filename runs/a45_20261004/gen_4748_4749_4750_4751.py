import json
def B(t,x,y,w,h): return {"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)}
def OFF(t): return {"t":t,"off":True}
def times(n): return [i*0.5 for i in range(n)]
def keys(ts, d):
    return [B(t,*d[t]) if d.get(t) else OFF(t) for t in ts]
def save(o): json.dump(o, open("content/%d.json"%o["mediaId"],"w"), indent=1, ensure_ascii=False)

# ---------- 4748
ts = times(19)
sky = keys(ts,{t:(0,0,1,0.27) for t in ts})
wing = keys(ts,{t:(0.10,0.27,0.90,0.33) for t in ts})
clouds = keys(ts,{t:(0,0.60,1,0.40) for t in ts})
save({"mediaId":4748,"level":"A","keyWord":"cloud","defaultVoice":"female",
 "taps":[
  {"phrase":"to hide the ground below","target":"the clouds","voice":"female","keys":clouds},
  {"phrase":"to belong to a plane","target":"the wing","voice":"female","keys":wing},
  {"phrase":"to stay clear and blue","target":"the sky","voice":"female","keys":sky}],
 "stillS":7.5,
 "nouns":[{"word":"clouds","x":0.40,"y":0.78,"voice":"female"},
          {"word":"a wing","x":0.62,"y":0.45,"voice":"female"},
          {"word":"the sky","x":0.50,"y":0.13,"voice":"female"}],
 "question":"What is hiding the ground?",
 "answer":["White","clouds","are","hiding","the","ground."],
 "answerVoice":"female",
 "notes":"No person or animal: targets are things (clouds, wing, sky), two phrases are states. Boxes are three fixed bands: sky above the wing tip, wing band, clouds below it; the clouds between the wing and the horizon on the left (y 0.43-0.60) fall inside the wing band. In the first seconds the cloud band also holds the ground seen through the gaps. Only 3 nouns (nothing else clearly visible)."})

# ---------- 4749
ts = times(21)
para = keys(ts,{2.0:(0.36,0.41,0.40,0.43),2.5:(0.38,0.45,0.35,0.36),3.0:(0.35,0.45,0.36,0.36)})
bask = keys(ts,{3.5:(0.47,0.34,0.53,0.58),4.0:(0.48,0.33,0.52,0.58),4.5:(0.48,0.33,0.52,0.58),5.0:(0.49,0.33,0.51,0.57)})
sky_ = keys(ts,{7.0:(0,0.86,1,0.14),7.5:(0,0,1,1),8.0:(0,0,1,0.90),8.5:(0,0.09,1,0.73),
                9.0:(0.09,0.20,0.84,0.55),9.5:(0.17,0.26,0.65,0.43),10.0:(0.24,0.29,0.51,0.34)})
save({"mediaId":4749,"level":"B","keyWord":"formation","defaultVoice":"male",
 "taps":[
  {"phrase":"to link hands in formation","target":"the skydivers","voice":"male","keys":sky_},
  {"phrase":"to steer a rainbow paraglider","target":"the woman under the rainbow wing","voice":"female","keys":para},
  {"phrase":"to lean on a wicker basket","target":"the woman in the basket","voice":"female","keys":bask}],
 "stillS":4.0,
 "nouns":[{"word":"a hot-air balloon","x":0.68,"y":0.10,"voice":"male"},
          {"word":"the sun","x":0.22,"y":0.47,"voice":"male"},
          {"word":"fields","x":0.25,"y":0.72,"voice":"male"},
          {"word":"a wicker basket","x":0.68,"y":0.90,"voice":"male"}],
 "question":"What are the skydivers doing?",
 "answer":["They","are","linking","hands","in","formation."],
 "answerVoice":"male",
 "notes":"Montage of 5 shots (tandem pair 0-1.5, paraglider 2-3, balloon 3.5-5, hang-glider 5.5-6.5, skydivers 7-10); each target has a box only in its own shot. At 7.0 only the skydivers' legs show at the bottom edge. The key word 'formation' is in a phrase and the answer, not among the nouns: the still is the balloon shot, where the nouns sit well apart (in the ring shot everything would label the same place). Mixed group, odd id -> default voice male. The tandem pair (shot 1) hangs under a white canopy, not a rainbow paraglider."})

# ---------- 4750
ts = times(25)
W = {0.0:(0.15,0.06,0.77,0.52),0.5:(0.07,0.06,0.84,0.52),1.0:(0.08,0.06,0.68,0.69),1.5:(0.21,0.12,0.55,0.70),
     2.0:(0.24,0.08,0.76,0.50),2.5:(0.27,0.08,0.69,0.49),3.0:(0.23,0.10,0.50,0.62),3.5:(0.15,0.11,0.58,0.61),
     4.0:(0.25,0.18,0.46,0.50),4.5:(0.28,0.17,0.43,0.49),5.0:(0.32,0.16,0.38,0.46),5.5:(0.36,0.16,0.51,0.32),
     6.0:(0.32,0.18,0.36,0.42),6.5:(0.36,0.19,0.44,0.38),7.0:(0.40,0.21,0.41,0.31),7.5:(0.38,0.21,0.36,0.28),
     8.0:(0.39,0.21,0.35,0.26),8.5:(0.31,0.21,0.39,0.24),9.0:(0.40,0.22,0.29,0.23),9.5:(0.40,0.21,0.33,0.24),
     10.0:(0.37,0.22,0.30,0.22),10.5:(0.37,0.22,0.30,0.22),11.0:(0.31,0.22,0.38,0.23),11.5:(0.37,0.22,0.30,0.22),
     12.0:(0.37,0.22,0.30,0.22)}
K = {0.0:(0.76,0.58,0.24,0.27),0.5:(0.76,0.58,0.24,0.27),1.0:(0.77,0.58,0.23,0.27),1.5:(0.77,0.57,0.23,0.27),
     2.0:(0.74,0.58,0.26,0.26),2.5:(0.74,0.58,0.26,0.27),3.0:(0.74,0.54,0.26,0.26),3.5:(0.73,0.52,0.27,0.26),
     4.0:(0.72,0.49,0.28,0.27),4.5:(0.72,0.48,0.28,0.26),5.0:(0.71,0.50,0.29,0.20),5.5:(0.70,0.49,0.30,0.20),
     6.0:(0.69,0.46,0.31,0.20),6.5:(0.81,0.44,0.19,0.18),7.0:(0.82,0.44,0.18,0.16),7.5:(0.76,0.42,0.20,0.14),
     8.0:(0.75,0.40,0.18,0.14)}
wk = keys(ts,W); bk = keys(ts,K)
save({"mediaId":4750,"level":"A","keyWord":"clothes","defaultVoice":"female",
 "taps":[
  {"phrase":"to fold a T-shirt","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to reach into the basket","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to be full of clothes","target":"the basket","voice":"female","keys":bk}],
 "stillS":4.0,
 "nouns":[{"word":"a woman","x":0.50,"y":0.40,"voice":"female"},
          {"word":"a basket","x":0.86,"y":0.62,"voice":"female"},
          {"word":"clothes","x":0.48,"y":0.72,"voice":"female"},
          {"word":"a bed","x":0.50,"y":0.88,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","folding","clothes","on","the","bed."],
 "answerVoice":"female",
 "notes":"Only two targets (woman, basket); the basket phrase is a state. Where her arm or the shirt she holds reaches over the basket (0.0, 0.5, 2.0, 2.5, 5.5) the woman's box stops just above the basket rim and loses her lower body; at 1.0, 3.5 and 5.0 it stops at the basket's left edge instead and loses an elbow / the reaching hand. The basket is hidden behind the piles from 8.5 (off); at 7.5-8.0 only its top shows. Doubt: 'clothes' could also label the washing inside the basket; the pill is on the folded pile, the basket pill on the wicker. By the end the bed is also 'full of clothes', but the bed is not a target."})

# ---------- 4751
ts = times(21)
G = {0.0:(0.07,0.10,0.93,0.90),0.5:(0.09,0.09,0.91,0.91),1.0:(0.11,0.04,0.89,0.96),1.5:(0.11,0.06,0.89,0.94),
     2.0:(0.12,0.09,0.88,0.91),2.5:(0.12,0.09,0.88,0.91),3.0:(0.08,0.17,0.89,0.83),3.5:(0.10,0.21,0.84,0.79),
     4.0:(0.08,0.24,0.68,0.76),4.5:(0.06,0.21,0.66,0.79),5.0:(0.02,0.21,0.59,0.79),5.5:(0.05,0.21,0.56,0.79),
     6.0:(0.25,0.21,0.69,0.79),6.5:(0.21,0.24,0.58,0.76),7.0:(0.19,0.25,0.60,0.75),7.5:(0.21,0.22,0.58,0.78),
     8.0:(0.20,0.24,0.45,0.76),8.5:(0.05,0.39,0.54,0.61),9.0:(0.06,0.47,0.46,0.53),9.5:(0.09,0.48,0.49,0.52),
     10.0:(0.06,0.49,0.47,0.51)}
T = {4.0:(0.77,0.28,0.23,0.30),4.5:(0.73,0.30,0.27,0.26),5.0:(0.62,0.30,0.38,0.24),5.5:(0.62,0.31,0.20,0.21),
     6.0:(0,0.24,0.24,0.33),6.5:(0,0.24,0.20,0.30),7.0:(0,0.25,0.18,0.29),7.5:(0,0.22,0.20,0.30),
     8.0:(0,0.17,0.19,0.38),8.5:(0,0.16,0.22,0.22),9.0:(0,0.32,0.56,0.14),9.5:(0,0.33,0.56,0.14),
     10.0:(0,0.34,0.44,0.14)}
D = {6.5:(0.80,0.46,0.18,0.14),7.0:(0.80,0.50,0.18,0.14),7.5:(0.80,0.54,0.20,0.19),8.0:(0.66,0.68,0.34,0.24),
     8.5:(0.60,0.72,0.40,0.28),9.0:(0.54,0.66,0.25,0.32),9.5:(0.62,0.59,0.24,0.23),10.0:(0.66,0.56,0.24,0.20)}
save({"mediaId":4751,"level":"A","keyWord":"guide","defaultVoice":"female",
 "taps":[
  {"phrase":"to hold a yellow umbrella","target":"the guide","voice":"female","keys":keys(ts,G)},
  {"phrase":"to run on rails","target":"the tram","voice":"female","keys":keys(ts,T)},
  {"phrase":"to walk on four legs","target":"the dog","voice":"female","keys":keys(ts,D)}],
 "stillS":9.5,
 "nouns":[{"word":"an umbrella","x":0.30,"y":0.23,"voice":"female"},
          {"word":"a tram","x":0.30,"y":0.42,"voice":"female"},
          {"word":"a dog","x":0.74,"y":0.70,"voice":"female"},
          {"word":"a guide","x":0.33,"y":0.82,"voice":"female"}],
 "question":"What is the guide holding?",
 "answer":["She","is","holding","a","yellow","umbrella."],
 "answerVoice":"female",
 "notes":"The guide's box holds her body and, where no other target is in the way, the umbrella too (0-8.0); from 8.5 the tram lies between her and the canopy, so the box is her body only and the canopy belongs to no box. The tram is half hidden behind the umbrella and the walkers; its box is the visible part (4.0-10.0). 'to run on rails': the rails themselves are hardly visible. The dog is tiny at 6.5-7.0 (right edge) and a speck at 6.0 (off). The visitors behind the guide are not a target."})
