import json
T=[i*0.5 for i in range(21)]
W={0.0:(0.24,0.33,0.52,0.57),0.5:(0.28,0.29,0.72,0.66),1.0:(0.31,0.28,0.54,0.70),1.5:(0.36,0.28,0.64,0.55),
2.0:(0.30,0.29,0.56,0.63),2.5:(0.25,0.31,0.75,0.56),3.0:(0.27,0.35,0.55,0.47),3.5:(0.26,0.33,0.58,0.44),
4.0:(0.0,0.30,0.57,0.52),4.5:(0.28,0.29,0.44,0.50),5.0:(0.31,0.30,0.40,0.52),5.5:(0.04,0.31,0.75,0.46),
6.0:(0.02,0.33,0.78,0.48),6.5:(0.46,0.37,0.54,0.45),7.0:(0.45,0.37,0.45,0.43),7.5:(0.40,0.36,0.40,0.38),
8.0:(0.48,0.37,0.36,0.40),8.5:(0.37,0.40,0.26,0.42),9.0:(0.39,0.39,0.25,0.43),9.5:(0.37,0.38,0.28,0.44),10.0:(0.35,0.39,0.31,0.43)}
C={8.5:(0.0,0.40,0.18,0.24),9.0:(0.0,0.40,0.18,0.20),9.5:(0.0,0.40,0.18,0.22),10.0:(0.0,0.40,0.18,0.20)}
def keys(D):
    return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
c={"mediaId":5270,"level":"A","keyWord":"supermarket","defaultVoice":"female",
"taps":[{"phrase":"to grab cereal boxes","target":"the young woman","voice":"female","keys":keys(W)},
{"phrase":"to fill a big trolley","target":"the young woman","voice":"female","keys":keys(W)},
{"phrase":"to work at the checkout","target":"the cashier","voice":"female","keys":keys(C)}],
"stillS":0.0,
"nouns":[{"word":"lights","x":0.33,"y":0.12,"voice":"female"},{"word":"shelves","x":0.86,"y":0.40,"voice":"female"},
{"word":"a man","x":0.10,"y":0.48,"voice":"female"},{"word":"a trolley","x":0.45,"y":0.75,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","shopping","in","a","supermarket."],"answerVoice":"female",
"notes":"Key word 'supermarket' is the whole place, so it is in the answer, not a noun pill. The cashier is only at the left edge at the checkout 8.5-10.0 (small, partly cut); boxes kept at the minimum size. Other shoppers push trolleys in the background, so no 'to push a trolley' phrase. Still 0.0: 'a man' = the man in black at the left; the grey-haired woman behind is not labelled."}
json.dump(c,open('content/5270.json','w'),indent=1)
