import json
T=[i*0.5 for i in range(21)]
def mk(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,0.92,1),1.5:(0,0,1,1),2.0:(0,0,0.82,1),2.5:(0,0,0.9,0.98),
 3.0:(0,0,0.95,1),3.5:(0,0.03,1,0.97),4.0:(0,0.38,1,0.62),4.5:(0,0.18,1,0.82),5.0:(0,0.37,1,0.63),5.5:(0,0.26,0.5,0.66),
 6.0:(0,0,1,0.66),6.5:(0,0,1,0.62),7.0:(0,0,1,0.44),7.5:(0,0,1,0.39),8.0:(0,0,1,0.26),8.5:(0,0,1,0.27),9.0:(0,0,1,0.40),
 9.5:(0,0,1,0.58),10.0:(0,0,1,0.61)}
sell={4.0:(0.62,0,0.38,0.19),4.5:(0.6,0,0.4,0.17),5.0:(0.45,0.05,0.55,0.31),5.5:(0.5,0.03,0.45,0.32)}
coins={7.0:(0.05,0.44,0.95,0.47),7.5:(0.05,0.39,0.95,0.47),8.0:(0.03,0.27,0.97,0.49),8.5:(0.18,0.27,0.82,0.38),
 9.0:(0.34,0.40,0.66,0.26),9.5:(0.2,0.58,0.8,0.32),10.0:(0.15,0.61,0.85,0.29)}
c={"mediaId":5474,"level":"A","keyWord":"coin","defaultVoice":"male",
 "taps":[{"phrase":"to open his wallet","target":"the man","voice":"male","keys":mk(man)},
  {"phrase":"to sell fruit","target":"the stallholder","voice":"male","keys":mk(sell)},
  {"phrase":"to fall onto the table","target":"the coins","voice":"male","keys":mk(coins)}],
 "stillS":10.0,
 "nouns":[{"word":"a jacket","x":0.75,"y":0.28,"voice":"male"},{"word":"a purse","x":0.32,"y":0.48,"voice":"male"},
  {"word":"coins","x":0.55,"y":0.74,"voice":"male"},{"word":"a table","x":0.5,"y":0.93,"voice":"male"}],
 "question":"What is falling onto the table?",
 "answer":["Coins","are","falling","onto","the","table."],"answerVoice":"male",
 "notes":"Frames show banknotes at the market, not a card (description says card); phrases avoid it. Coins OFF at 6.0-6.5 (inside the purse held by the man, would overlap his box). At 8.5-9.0 the man's pointing finger touches the coins: boxes split horizontally, fingertip falls in the coins box. Stallholder only blurry at 4.0."}
json.dump(c,open('content/5474.json','w'),indent=1)
