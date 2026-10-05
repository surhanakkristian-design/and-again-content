import json
times=[i/2 for i in range(19)]
B=lambda x,y,w,h:dict(x=x,y=y,w=w,h=h)
man={0.0:B(0,0.22,0.10,0.62),0.5:B(0,0.20,0.11,0.65),1.0:B(0,0.24,0.16,0.60),1.5:B(0,0.25,0.17,0.60),2.0:B(0,0.24,0.17,0.62),2.5:B(0,0.0,0.17,0.85),
3.0:B(0,0,0.40,1),3.5:B(0,0,0.48,1),4.0:B(0,0.03,0.61,0.97),4.5:B(0,0.02,0.69,0.98),5.0:B(0,0.03,0.67,0.97),5.5:B(0,0.03,0.73,0.97),
6.0:B(0,0.03,0.71,0.97),6.5:B(0,0.03,0.75,0.97),7.0:B(0,0.03,0.65,0.97),7.5:B(0,0.03,0.54,0.97),8.0:B(0,0.03,0.51,0.97),8.5:B(0,0.0,0.51,1),9.0:B(0,0.03,0.47,0.97)}
wom={0.0:B(0.10,0.03,0.63,0.97),0.5:B(0.11,0.03,0.64,0.97),1.0:B(0.17,0.03,0.56,0.97),1.5:B(0.18,0.03,0.58,0.97),2.0:B(0.18,0.02,0.55,0.98),2.5:B(0.18,0.03,0.60,0.97),
3.0:B(0.41,0.05,0.59,0.95),3.5:B(0.49,0.05,0.51,0.95),4.0:B(0.62,0.05,0.38,0.95),4.5:B(0.70,0.05,0.30,0.95),5.0:B(0.68,0.07,0.32,0.93),5.5:B(0.74,0.07,0.26,0.93),
6.0:B(0.72,0.05,0.28,0.95),6.5:B(0.76,0.05,0.24,0.95),7.0:B(0.66,0.07,0.34,0.93),7.5:B(0.55,0.07,0.45,0.93),8.0:B(0.52,0.07,0.47,0.93),8.5:B(0.52,0.07,0.47,0.93),9.0:B(0.48,0.15,0.52,0.85)}
girl={0.0:B(0.74,0.15,0.26,0.85),0.5:B(0.76,0.15,0.24,0.85),1.0:B(0.74,0.15,0.26,0.85),1.5:B(0.77,0.15,0.23,0.85),2.0:B(0.74,0.15,0.26,0.85),2.5:B(0.79,0.15,0.21,0.85)}
def keys(d): return [dict(t=t,**d[t]) if t in d else {"t":t,"off":True} for t in times]
c={"mediaId":4950,"level":"B","keyWord":"hip","defaultVoice":"female",
"taps":[
{"phrase":"to grin at the camera","target":"the woman in red","voice":"female","keys":keys(wom)},
{"phrase":"to keep a straight face","target":"the young man","voice":"male","keys":keys(man)},
{"phrase":"to wear a black sports top","target":"the girl in black","voice":"female","keys":keys(girl)}],
"stillS":8.5,
"nouns":[{"word":"a ceiling light","x":0.55,"y":0.07,"voice":"female"},
{"word":"a crop top","x":0.72,"y":0.47,"voice":"female"},
{"word":"a hip","x":0.86,"y":0.70,"voice":"female"},
{"word":"a ruffled skirt","x":0.62,"y":0.86,"voice":"female"}],
"question":"What is the young man doing?",
"answer":["He","is","resting","his","hands","on","his","hips."],
"answerVoice":"male",
"notes":"Everyone holds hands on hips, so no phrase uses that pose. 0-2.5: the young man is only a grey-shirt sliver at the left edge (head out of frame) - narrow box; the woman's left elbow is cut off by it. The girl in black (bob hair) is visible only 0-2.5 behind the woman's right arm; split at x ~0.74, her box contains the woman's right elbow. From 3.0 man/woman boxes split vertically (her arm crosses into his box). 'to keep a straight face': true until ~8.0, at 8.5-9.0 he laughs. 'to grin at the camera': she smiles throughout but looks at the man around 4-7. Noun 'a hip' sits on her left hip under her hand."}
json.dump(c,open('content/4950.json','w'),indent=1)
