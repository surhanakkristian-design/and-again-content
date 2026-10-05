import json
def K(rows): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in rows]
w=[(0.0,(0,.02,.98,.98)),(0.5,(0,.02,1,.98)),(1.0,(0,.03,1,.97)),(1.5,(0,.03,1,.97)),(2.0,(0,.05,1,.95)),
(2.5,(.16,.21,.77,.79)),(3.0,(.17,.22,.76,.78)),(3.5,(.16,.22,.77,.78)),(4.0,(.17,.22,.76,.78)),(4.5,(.16,.22,.77,.78)),(5.0,(.17,.22,.76,.78)),
(5.5,(.05,.08,.93,.45)),(6.0,(.08,.08,.88,.45)),(6.5,(.05,.06,.93,.45)),(7.0,(.05,.06,.93,.44)),(7.5,(.05,.07,.93,.55)),
(8.0,(.05,.08,.93,.42)),(8.5,(.05,.08,.93,.41)),(9.0,(.05,.10,.93,.43)),(9.5,(.05,.10,.93,.41)),(10.0,(.05,.08,.93,.43))]
cd=[(t,None) for t in (0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0)]+[(5.5,(.74,.53,.22,.14)),(6.0,(.67,.53,.20,.14)),(6.5,(.50,.51,.20,.14)),(7.0,(.51,.50,.20,.14)),(7.5,None),
(8.0,(.48,.50,.20,.14)),(8.5,(.49,.49,.20,.14)),(9.0,(.49,.53,.20,.14)),(9.5,(.49,.51,.20,.14)),(10.0,(.50,.51,.20,.14))]
c={"mediaId":5196,"level":"B","keyWord":"bun","defaultVoice":"female",
"taps":[{"phrase":"to grip a metal pole","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to stifle a yawn","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to flicker in the dark","target":"the candle","voice":"female","keys":K(cd)}],
"stillS":5.0,
"nouns":[{"word":"a bun","x":.53,"y":.29,"voice":"female"},{"word":"glasses","x":.53,"y":.43,"voice":"female"},
{"word":"a bench","x":.12,"y":.67,"voice":"female"},{"word":"a pigeon","x":.88,"y":.87,"voice":"female"}],
"question":"How is the woman wearing her hair?","answer":["She","is","wearing","her","hair","in","a","bun."],"answerVoice":"female",
"notes":"three shots: tram (0-2.0), park bench (2.5-5.0), under a blanket with a tealight candle (5.5-10.0). Candle hidden at 7.5. Night woman boxes stop above the candle (face/hood only) to avoid overlap. Pigeon only at the bottom-right edge in the park shot; bun not visible in the night shot (hood)."}
json.dump(c,open('content/5196.json','w'),indent=1)
