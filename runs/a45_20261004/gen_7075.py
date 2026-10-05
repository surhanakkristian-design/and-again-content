from gen_7075_7076_7077_7079_w import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.09,0.34,0.67,0.58),(0.08,0.34,0.69,0.59),(0.06,0.33,0.70,0.60),(0.05,0.32,0.72,0.62),(0.04,0.32,0.74,0.64),(0.04,0.31,0.74,0.66),(0.03,0.32,0.75,0.66),(0.04,0.32,0.74,0.66)]
TR=[(0.00,0.12,0.50,0.21),(0.00,0.09,0.30,0.24),(0.00,0.09,0.20,0.23),(0.00,0.08,0.20,0.23),(0.00,0.05,0.20,0.26),(0.00,0.05,0.20,0.25),(0.00,0.08,0.44,0.23),(0.00,0.10,0.40,0.21)]
C=[(0.52,0.17,0.46,0.17),(0.53,0.16,0.45,0.18),(0.53,0.16,0.45,0.17),(0.60,0.14,0.32,0.18),(0.60,0.14,0.32,0.18),(0.61,0.13,0.36,0.18),(0.61,0.13,0.34,0.19),(0.62,0.13,0.36,0.19)]
d={"mediaId":7075,"level":"B","keyWord":"economist","defaultVoice":"female",
"taps":[
 {"phrase":"to jot down notes","target":"the young woman","voice":"female","boxes":W},
 {"phrase":"to hold out an onion","target":"the trader","voice":"male","boxes":TR},
 {"phrase":"to fold her arms","target":"the woman in the dark jacket","voice":"female","boxes":C}],
"stillS":2.2,
"nouns":[{"word":"a hanging scale","x":0.84,"y":0.14,"voice":"female"},
 {"word":"a chalkboard","x":0.86,"y":0.50,"voice":"female"},
 {"word":"a clipboard","x":0.57,"y":0.63,"voice":"female"},
 {"word":"onions","x":0.66,"y":0.83,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","making","notes","on","a","clipboard."],
"answerVoice":"female",
"notes":"Key word 'economist' not used as a noun (would need guessing). Trader and the woman in the dark jacket are cut to their upper part above the young woman's box (boxes split by y). Trader is mostly off the left edge at 1.2-2.7 (cap and arm only)."}
write(d,T)
