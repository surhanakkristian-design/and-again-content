import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
B={0.0:(0,0.19,0.72,1),0.5:(0,0.19,0.74,1),1.0:(0,0.19,0.73,1),1.5:(0,0.19,0.69,1),2.0:(0,0.19,0.62,1),2.5:(0,0.22,0.53,1),
 3.0:(0,0.27,0.47,1),3.5:(0,0.30,0.60,1),4.0:(0,0.29,0.50,1),4.5:(0,0.34,0.46,1),5.0:(0,0.41,0.44,1),5.5:(0.10,0.46,0.50,1),
 6.0:(0.18,0.48,0.53,1),6.5:(0.25,0.50,0.58,1),7.0:(0.30,0.52,0.53,0.93),7.5:(0.32,0.55,0.51,0.86),8.0:(0.33,0.53,0.51,0.82),
 8.5:(0.33,0.55,0.51,0.80),9.0:(0.32,0.57,0.50,0.78)}
G={0.0:(0.74,0.04,1,1),0.5:(0.76,0.04,1,1),1.0:(0.75,0.04,1,1),1.5:(0.71,0.04,1,1),2.0:(0.63,0.08,1,1),2.5:(0.54,0.14,1,1),
 3.0:(0.48,0.18,1,1),3.5:(0.61,0.18,1,1),4.0:(0.51,0.19,1,1),4.5:(0.47,0.25,1,1),5.0:(0.45,0.34,1,1),5.5:(0.51,0.40,0.98,1),
 6.0:(0.54,0.45,0.93,1),6.5:(0.59,0.47,0.86,0.99),7.0:(0.54,0.50,0.75,0.93),7.5:(0.52,0.53,0.71,0.86),8.0:(0.52,0.53,0.70,0.82),
 8.5:(0.52,0.55,0.70,0.80),9.0:(0.51,0.56,0.69,0.78)}
c={"mediaId":4781,"level":"A","keyWord":"marry","defaultVoice":"male",
"taps":[
 {"phrase":"to give him a ring","target":"the bride","voice":"female","keys":keys(B)},
 {"phrase":"to cry with joy","target":"the bride","voice":"female","keys":keys(B)},
 {"phrase":"to smile at his bride","target":"the groom","voice":"male","keys":keys(G)}],
"stillS":6.0,
"nouns":[{"word":"a tree","x":0.50,"y":0.10,"voice":"male"},
 {"word":"a groom","x":0.72,"y":0.60,"voice":"male"},
 {"word":"a bride","x":0.37,"y":0.72,"voice":"female"}],
"question":"What are the man and woman doing?",
"answer":["They","are","getting","married","in","a","garden."],
"answerVoice":"male",
"notes":"Bride slides the ring onto the groom's finger 0-2 s (she slides it onto his finger). Groom's arm reaches into the bride's box 0-2 s (split at the groom's body). From 7.0 s the couple is small in a cheering crowd; boxes kept at min size 0.18 wide, the groom box at 8-9 s also covers guests next to him. Other women in white dresses among the guests at 8-9 s. Couple answer 'They' -> defaultVoice (evenId false = male)."}
json.dump(c,open("content/4781.json","w"),indent=1)
