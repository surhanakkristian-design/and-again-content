from gen_7998_8002_8003_8005_lib import write
W = [(0.15,0.09,0.64,0.82),(0.14,0.08,0.70,0.87),(0.12,0.07,0.72,0.93),(0.20,0.04,0.69,0.96),
     (0.22,0.02,0.72,0.98),(0.20,0.03,0.78,0.97),(0.17,0.06,0.81,0.94),(0.17,0.06,0.83,0.94)]
write(7998, {"level":"B","keyWord":"state of mind","defaultVoice":"female",
 "taps":[
  {"phrase":"to balance on one leg","target":"the woman","voice":"female","boxes":W},
  {"phrase":"to raise her arms overhead","target":"the woman","voice":"female","boxes":W},
  {"phrase":"to press her palms together","target":"the woman","voice":"female","boxes":W}],
 "stillS":0.2,
 "nouns":[{"word":"the sky","x":0.50,"y":0.06,"voice":"female"},
          {"word":"tower blocks","x":0.16,"y":0.30,"voice":"female"},
          {"word":"a lorry","x":0.75,"y":0.46,"voice":"female"},
          {"word":"a yoga mat","x":0.74,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","balancing","on","one","leg","above","the","traffic."],
 "answerVoice":"female",
 "notes":"Only one clear target (the woman); all three phrases use her. The jammed cars/lorries surround her on both sides, so no separate vehicle target. Camera pushes in; the mat leaves the frame after 1.7. Key word (state of mind) is not a visible noun."})
