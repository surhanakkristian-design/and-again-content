from gen_7998_8002_8003_8005_lib import write
WO = [(0.36,0.26,0.44,0.67),(0.30,0.26,0.49,0.68),(0.31,0.26,0.49,0.68),(0.37,0.25,0.44,0.69),
      (0.20,0.25,0.61,0.68),(0.16,0.24,0.58,0.76),(0.22,0.24,0.52,0.76),(0.22,0.28,0.52,0.72)]
CA = [(0.81,0.58,0.18,0.19),(0.81,0.58,0.18,0.19),(0.81,0.58,0.18,0.19),(0.82,0.58,0.18,0.19),
      (0.82,0.58,0.18,0.19),(0.78,0.58,0.20,0.19),(0.78,0.58,0.20,0.19),(0.79,0.58,0.20,0.19)]
write(8003, {"level":"B","keyWord":"stay","defaultVoice":"female",
 "taps":[
  {"phrase":"to fold a striped towel","target":"the woman","voice":"female","boxes":WO},
  {"phrase":"to lean on the railing","target":"the woman","voice":"female","boxes":WO},
  {"phrase":"to sit in the doorway","target":"the cat","voice":"female","boxes":CA}],
 "stillS":2.2,
 "nouns":[{"word":"a lighthouse","x":0.40,"y":0.10,"voice":"female"},
          {"word":"a cat","x":0.88,"y":0.68,"voice":"female"},
          {"word":"herbs","x":0.42,"y":0.84,"voice":"female"},
          {"word":"rubber boots","x":0.90,"y":0.89,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","folding","a","striped","towel."],
 "answerVoice":"female",
 "notes":"Only two targets (woman, cat); the woman has two phrases: folding (0.2-2.2) and leaning on the railing (2.7-3.7). The towel flies wide at 0.2 and is not fully inside her box. Cat box padded to the minimum size; it sits half hidden behind the red door frame. Rubber boots are cut by the right edge; the pill is clamped inward."})
