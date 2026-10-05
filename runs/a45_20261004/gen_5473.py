import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
M={0.0:(0.08,0.09,0.92,0.76),0.5:(0.04,0.09,0.96,0.76),1.0:(0.05,0.08,0.95,0.77),1.5:(0.08,0.08,0.92,0.80),
 2.0:(0.08,0.07,0.92,0.78),2.5:(0.04,0.08,0.96,0.76),3.0:(0.05,0.10,0.95,0.72),3.5:(0.02,0.08,0.97,0.74),
 4.0:(0.06,0.08,0.93,0.72),4.5:(0.20,0.07,0.78,0.75),5.0:(0.10,0.11,0.88,0.85),5.5:(0.06,0.10,0.94,0.80),
 6.0:(0.0,0.09,1.0,0.76),6.5:(0.02,0.07,0.98,0.73),7.0:(0.05,0.07,0.95,0.73),7.5:(0.06,0.06,0.94,0.72),
 8.0:(0.10,0.10,0.88,0.66),8.5:(0.05,0.06,0.93,0.66),9.0:(0.12,0.10,0.86,0.66)}
O={4.5:(0.0,0.64,0.20,0.20),7.5:(0.0,0.85,0.18,0.15),8.0:(0.0,0.77,0.62,0.17),8.5:(0.0,0.72,0.50,0.17),9.0:(0.0,0.76,0.58,0.20)}
c={"mediaId":5473,"level":"B","keyWord":"wealthy","defaultVoice":"male",
"taps":[{"phrase":"to pull out a bank card","target":"the man with a moustache","voice":"male","keys":keys(M)},
{"phrase":"to empty his coin purse","target":"the man with a moustache","voice":"male","keys":keys(M)},
{"phrase":"to reach across the table","target":"the other man","voice":"male","keys":keys(O)}],
"stillS":7.5,
"nouns":[{"word":"a parasol","x":0.40,"y":0.10,"voice":"male"},{"word":"apples","x":0.12,"y":0.44,"voice":"male"},
{"word":"a wallet","x":0.83,"y":0.56,"voice":"male"},{"word":"coins","x":0.55,"y":0.82,"voice":"male"}],
"question":"What is falling onto the table?","answer":["Coins","are","falling","onto","the","table."],"answerVoice":"male",
"notes":"Frames differ from the description: at 5.0-7.0 he opens a clasp coin purse and coins pour out onto the wooden table (no empty-wallet reveal). The other man is only an arm/hand from the left (4.5 takes a banknote, 7.5-9.0 reaches over the coins; his head edge at top-left 8.5-9.0 is left out). Hands overlap at 8.0-9.0: split horizontally (main man above ~0.72-0.77, other hand below). 'wealthy' is an adjective, not placed. Bank card phrase only true at 1.0-2.0."}
json.dump(c,open('content/5473.json','w'),indent=1)
