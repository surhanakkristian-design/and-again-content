import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0.08,0.36,0.88,0.64),0.5:(0.04,0.37,0.96,0.63),1.0:(0.0,0.40,1.0,0.60),1.5:(0.0,0.41,1.0,0.59),
 2.0:(0.0,0.42,1.0,0.58),2.5:(0.0,0.44,1.0,0.56),3.0:(0.0,0.45,1.0,0.55),3.5:(0.0,0.45,1.0,0.55),
 4.0:(0.0,0.12,0.52,0.88),4.5:(0.0,0.10,0.56,0.90),5.0:(0.0,0.13,0.63,0.87),5.5:(0.0,0.15,0.67,0.85),
 6.0:(0.0,0.13,0.69,0.87),6.5:(0.0,0.10,0.74,0.90),7.0:(0.0,0.03,0.52,0.97),7.5:(0.0,0.0,0.72,1.0),
 8.0:(0.04,0.36,0.88,0.64),8.5:(0.07,0.37,0.86,0.63),9.0:(0.07,0.39,0.82,0.61),9.5:(0.07,0.37,0.83,0.63),
 10.0:(0.04,0.36,0.93,0.64),10.5:(0.12,0.38,0.88,0.62),11.0:(0.08,0.40,0.92,0.60),11.5:(0.07,0.39,0.88,0.61),12.0:(0.07,0.40,0.93,0.60)}
seller={4.0:(0.78,0.15,0.22,0.20),4.5:(0.74,0.13,0.26,0.21),5.0:(0.74,0.10,0.26,0.20),5.5:(0.78,0.09,0.22,0.20),6.0:(0.82,0.09,0.18,0.19)}
mon={}
for t in T:
    if t<4.0: mon[t]=(0.0,0.0,1.0,round(man[t][1],2))
c={"mediaId":4973,"level":"B","keyWord":"a monument","defaultVoice":"male",
 "taps":[
  {"phrase":"to lean over the spices","target":"the young man","voice":"male","keys":K(man)},
  {"phrase":"to watch over his stall","target":"the spice seller","voice":"male","keys":K(seller)},
  {"phrase":"to rise above the gardens","target":"the monument","voice":"male","keys":K(mon)}],
 "stillS":3.0,
 "nouns":[{"word":"a monument","x":0.50,"y":0.18,"voice":"male"},{"word":"the sky","x":0.15,"y":0.07,"voice":"male"},
  {"word":"cypress trees","x":0.86,"y":0.56,"voice":"male"},{"word":"a pool","x":0.16,"y":0.85,"voice":"male"}],
 "question":"What is the young traveller doing?",
 "answer":["He","is","posing","in","front","of","a","monument."],"answerVoice":"male",
 "notes":"Three shots (monument 0-3.5, spice market 4-7.5, colour festival 8-12). Question answered from shot 1; in shots 2-3 he leans over spices / celebrates. Monument box is split at the man's head line. Seller only visible 4.0-6.0 (top right)."}
json.dump(c,open('content/4973.json','w'),indent=1)
