import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
woman=K([(.63,.56,.19,.35),(.72,.55,.21,.37),(.73,.55,.21,.37),(.75,.55,.24,.37),(.78,.54,.21,.38),(.79,.54,.21,.38)])
ele=K([(0,.35,.63,.29),(0,.33,.54,.44),(0,.33,.52,.45),(0,.33,.60,.40),(0,.33,.55,.44),(0,.32,.56,.45)])
men=K([(.74,.42,.19,.14),(.75,.41,.20,.14),(.76,.41,.20,.14),(.77,.41,.22,.14),(.78,.40,.21,.14),(.80,.40,.20,.14)])
c={"mediaId":6990,"level":"A","keyWord":"copy","defaultVoice":"female",
"taps":[
 {"phrase":"to laugh out loud","target":"the woman","voice":"female","keys":woman},
 {"phrase":"to reach out its trunk","target":"the big elephant","voice":"female","keys":ele},
 {"phrase":"to hold their heads","target":"the two men","voice":"male","keys":men}],
"stillS":1.2,
"nouns":[{"word":"birds","x":0.55,"y":0.31,"voice":"female"},
 {"word":"an elephant","x":0.20,"y":0.42,"voice":"female"},
 {"word":"a copy","x":0.20,"y":0.70,"voice":"female"},
 {"word":"a woman","x":0.84,"y":0.70,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","laughing","out","loud."],
"answerVoice":"female",
"notes":"Two men (rangers) are small in the background, box at minimum size; their box and the woman's box split horizontally around y 0.55 (top of her hair / their legs slightly cut). At 0.2 the big elephant's trunk tip is cut at x 0.63 to stay off the woman's box. The big elephant box also covers the head of the model elephant below it (unavoidable). 'laugh out loud': she laughs with an open mouth visibly; no sound needed."}
json.dump(c,open('content/6990.json','w'),indent=1)
