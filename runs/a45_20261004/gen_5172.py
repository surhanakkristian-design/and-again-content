import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
grey={0.0:(0.02,0.0,0.92,0.66),0.5:(0.16,0.02,0.66,0.62),1.0:(0.16,0.02,0.66,0.62),
 4.5:(0.22,0.06,0.68,0.66),5.0:(0.18,0.13,0.68,0.58),6.0:(0.31,0.16,0.44,0.41),6.5:(0.31,0.17,0.45,0.40),
 7.0:(0.63,0.15,0.37,0.57),7.5:(0.66,0.17,0.34,0.55)}
denim={3.5:(0.29,0.16,0.71,0.84),4.0:(0.03,0.12,0.96,0.88)}
white={5.5:(0.08,0.06,0.78,0.76),6.0:(0.04,0.17,0.27,0.30),6.5:(0.05,0.17,0.26,0.30),
 7.0:(0.03,0.22,0.30,0.33),7.5:(0.0,0.22,0.30,0.32),8.0:(0.10,0.0,0.62,0.78)}
c={"mediaId":5172,"level":"B","keyWord":"bang","defaultVoice":"male",
"taps":[{"phrase":"to punch the dough","target":"the man in the grey T-shirt","voice":"male","keys":keys(grey)},
{"phrase":"to bang on a drum","target":"the woman in denim","voice":"female","keys":keys(denim)},
{"phrase":"to pound the spices","target":"the man in the white T-shirt","voice":"male","keys":keys(white)}],
"stillS":6.0,
"nouns":[{"word":"dough","x":0.36,"y":0.53,"voice":"male"},{"word":"a knife","x":0.13,"y":0.66,"voice":"male"},
{"word":"a steak","x":0.66,"y":0.70,"voice":"male"},{"word":"dried chillies","x":0.31,"y":0.89,"voice":"male"}],
"question":"What is the woman in denim doing?",
"answer":["She","is","banging","on","a","drum."],"answerVoice":"female",
"notes":"Fast-cut clip. Close-ups of anonymous hands (meat with mallet 1.5-2.0 s, pestle in mortar 2.5-3.0 s, mallet on dough 8.5-9.0 s) are set off for every target because the owner of the hands cannot be identified. 'to pound the spices' = the man in the white T-shirt working the pestle in the stone mortar 6.0-7.5 s (and swinging the mallet over it at 8.0 s); at 5.5 s he hits the dough with a mallet. The man in the grey T-shirt punches the dough with his fists 0.5-1.0, 4.5-5.0 and 7.0-7.5 s. A second woman (braids, patterned shirt) is not a target; the question names the woman in denim. defaultVoice male (main person = the man in the grey T-shirt). Key word 'bang' is a verb, used in phrase 2 and the answer."}
json.dump(c,open('content/5172.json','w'),indent=1)
