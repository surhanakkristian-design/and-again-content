import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,off=True) if bb is None else dict(t=t,x=bb[0],y=bb[1],w=round(bb[2]-bb[0],2),h=round(bb[3]-bb[1],2)) for t,bb in zip(T,b)]
dancer=K([(0.0,.26,.99,1.0),(.04,.24,.51,1.0),(.06,.23,.47,1.0),(.08,.24,.47,1.0),(.08,.25,.45,1.0),(0.0,.25,.58,1.0),(0.0,.28,.55,1.0),(0.0,.28,.56,1.0)])
trump=K([None,(.78,.36,1.0,.86),(.64,.38,.89,.99),(.60,.37,.84,.99),(.56,.37,.82,.88),(.59,.37,.81,.88),(.56,.38,.80,.88),(.57,.38,.79,.90)])
pian=K([None,None,(.89,.44,1.0,.90),(.84,.46,1.0,.92),(.82,.45,1.0,.90),(.81,.46,1.0,.91),(.80,.47,1.0,.92),(.79,.47,1.0,.94)])
c={"mediaId":7819,"level":"B","keyWord":"era","defaultVoice":"female",
"taps":[{"phrase":"to fling her arms wide","target":"the woman in silver","voice":"female","keys":dancer},
{"phrase":"to play the trumpet","target":"the man","voice":"male","keys":trump},
{"phrase":"to glance over her shoulder","target":"the woman at the piano","voice":"female","keys":pian}],
"stillS":1.2,
"nouns":[{"word":"an arched window","x":0.50,"y":0.23,"voice":"female"},{"word":"a trumpet","x":0.76,"y":0.44,"voice":"female"},
{"word":"a vintage car","x":0.55,"y":0.62,"voice":"female"},{"word":"a flapper dress","x":0.28,"y":0.76,"voice":"female"}],
"question":"What is the woman in silver doing?","answer":["She","is","flinging","her","arms","wide."],"answerVoice":"female",
"notes":"Arms flung wide only at 3.2-3.7 s (high kick at 0.2 s). Trumpeter set off at 0.2 s: only a blurred sliver at the right edge behind the dancer's kicking leg. Pianist enters at 1.2 s and glances over her shoulder at 1.7-2.7 s; she sits at the right edge so her box is narrow at 1.2 s. Dancer box at 2.7-3.7 s cut at x~0.56-0.58 so her outstretched arm does not overlap the trumpeter. 'a flapper dress' and 'a vintage car' are B-level labels; key word 'era' is abstract, not placed."}
json.dump(c,open('content/7819.json','w'),indent=1)
