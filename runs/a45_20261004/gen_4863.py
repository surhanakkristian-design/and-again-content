import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
w={0.0:(0.10,0.36,0.90,0.64),0.5:(0.10,0.33,0.90,0.67),1.0:(0.32,0.36,0.38,0.64),1.5:(0.50,0.86,0.50,0.14),
2.0:(0.36,0.55,0.64,0.45),2.5:(0.48,0.46,0.52,0.36),3.0:(0.46,0.0,0.54,0.74),3.5:(0.44,0.0,0.56,0.76),
4.0:(0.52,0.02,0.48,0.74),4.5:(0.48,0.03,0.52,0.72),5.0:(0.62,0.23,0.38,0.64),5.5:(0.38,0.38,0.62,0.55),
6.0:(0.42,0.45,0.58,0.55),6.5:(0.40,0.43,0.57,0.57),7.0:(0.21,0.61,0.55,0.39),7.5:(0.28,0.71,0.42,0.29),
8.0:(0.30,0.75,0.39,0.25),8.5:(0.32,0.75,0.37,0.25),9.0:(0.32,0.78,0.35,0.22)}
k=keys(w)
c={"mediaId":4863,"level":"A","keyWord":"plan","defaultVoice":"female",
"taps":[
 {"phrase":"to put up a note","target":"the woman","voice":"female","keys":k},
 {"phrase":"to write in a notebook","target":"the woman","voice":"female","keys":k},
 {"phrase":"to look up and smile","target":"the woman","voice":"female","keys":k}],
"stillS":3.0,
"nouns":[{"word":"a calendar","x":0.45,"y":0.14,"voice":"female"},
 {"word":"a note","x":0.63,"y":0.30,"voice":"female"},
 {"word":"a pen","x":0.60,"y":0.57,"voice":"female"},
 {"word":"a notebook","x":0.42,"y":0.74,"voice":"female"}],
"question":"What is the woman writing in?",
"answer":["She","is","writing","in","a","notebook."],
"answerVoice":"female",
"notes":"Only one person (the woman), so all three phrases share her; 0-2.5 s she is only hands/arms, 3-4.5 s face at the top-right edge plus hands. Key word 'plan' is abstract, not used as a noun pill; the wall calendar is 'a calendar'. Still 3.0 s: the calendar is blurred in the background but clearly a big wall calendar."}
json.dump(c,open('content/4863.json','w'),indent=1)
