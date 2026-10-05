import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
T=[i*0.5 for i in range(21)]
young={0.0:(0.0,0.24,0.70,0.76),0.5:(0.22,0.25,0.56,0.60),1.0:(0.19,0.27,0.81,0.38),1.5:(0.17,0.45,0.83,0.28),2.0:(0.12,0.45,0.88,0.30)}
woman={2.5:(0.27,0.35,0.48,0.25),3.0:(0.27,0.35,0.48,0.24),3.5:(0.27,0.35,0.48,0.24),4.0:(0.23,0.31,0.42,0.27),4.5:(0.21,0.26,0.37,0.30),5.0:(0.17,0.24,0.31,0.33)}
robe={5.5:(0.22,0.34,0.59,0.33),6.0:(0.27,0.34,0.48,0.32),6.5:(0.36,0.33,0.24,0.32),7.0:(0.33,0.33,0.28,0.31),7.5:(0.30,0.33,0.34,0.31),8.0:(0.19,0.34,0.46,0.28),8.5:(0.17,0.34,0.66,0.33),9.0:(0.05,0.38,0.93,0.30),9.5:(0.07,0.47,0.82,0.22),10.0:(0.09,0.47,0.76,0.20)}
keys=lambda d:[k(t,d.get(t)) for t in T]
c={"mediaId":4387,"level":"A","keyWord":"compare","defaultVoice":"male",
"taps":[
{"phrase":"to wear a hat","target":"the young man","voice":"male","keys":keys(young)},
{"phrase":"to make her bed","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to open the curtains","target":"the man in the robe","voice":"male","keys":keys(robe)}],
"stillS":4.5,
"nouns":[{"word":"a woman","x":0.37,"y":0.43,"voice":"female"},{"word":"a pillow","x":0.55,"y":0.53,"voice":"male"},{"word":"a bed","x":0.50,"y":0.70,"voice":"male"},{"word":"the floor","x":0.50,"y":0.93,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","making","her","bed."],
"answerVoice":"female",
"notes":"Three shots, one person each (young man 0-2.0, woman 2.5-5.0, man in robe 5.5-10.0). defaultVoice male: mixed group, evenId false. Phrase 1 is a state: the young man's only action (throwing himself onto the bed) is also done by the man in the robe at 8.5-9.0. Key word 'compare' is not visible as an action, so it is not used. 'a bed' = the white futon on the floor; 'the floor' pill sits on the mats below the futon. The man in the robe is a dark silhouette against the window at 5.5-6.5."}
json.dump(c,open("content/4387.json","w"),indent=1,ensure_ascii=False)
