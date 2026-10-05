import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else {"t":t,"off":True} for t,b in zip(T,lst)]
woman=K([(.12,.26,.82,.74),(.20,.29,.63,.71),(.27,.33,.50,.67),(.30,.35,.43,.65),(.32,.35,.37,.60),(.32,.35,.38,.55),(.33,.35,.36,.55),(.32,.35,.37,.53)])
abbey=K([(0,0,1,.26),(0,0,1,.29),(0,0,1,.33),(0,.01,1,.34),(0,.04,1,.31),(0,.06,1,.29),(0,.08,1,.27),(0,.08,1,.27)])
c={"mediaId":6814,"level":"B","keyWord":"abbey","defaultVoice":"female",
"taps":[
 {"phrase":"to ride along a causeway","target":"the young woman","voice":"female","keys":woman},
 {"phrase":"to hold her hat on","target":"the young woman","voice":"female","keys":woman},
 {"phrase":"to stand on a rocky island","target":"the abbey","voice":"female","keys":abbey}],
"stillS":2.7,
"nouns":[{"word":"an abbey","x":0.62,"y":0.27,"voice":"female"},{"word":"a straw hat","x":0.51,"y":0.42,"voice":"female"},
 {"word":"a raincoat","x":0.52,"y":0.53,"voice":"female"},{"word":"a bicycle","x":0.50,"y":0.80,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","riding","a","bicycle","along","a","causeway."],
"answerVoice":"female",
"notes":"Only one person, so two phrases share the woman. Abbey box is cut off at the top of the woman's box (her hat overlaps the abbey's lower walls). Abbey phrase is a state (no action fits the building). Gulls are small and scattered, not used."}
json.dump(c,open('content/6814.json','w'),indent=1)
