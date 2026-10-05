import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,b)]
woman=[(.42,.40,.32,.50),(.42,.38,.36,.50),(.41,.38,.39,.50),(.41,.38,.38,.50),(.42,.37,.37,.47),(.43,.38,.37,.45),(.44,.38,.36,.44),(.44,.38,.36,.42)]
cows=[(.12,.24,.30,.47),(.13,.24,.29,.52),(.12,.24,.29,.51),(.11,.24,.30,.52),(.11,.23,.31,.52),(.10,.24,.33,.52),(.07,.24,.37,.54),(.08,.24,.36,.52)]
farmer=[(.45,.23,.18,.16),(.46,.23,.18,.15),(.48,.22,.18,.15),(.49,.22,.18,.15),(.50,.22,.18,.15),(.52,.22,.18,.15),(.55,.22,.18,.15),(.57,.22,.18,.15)]
c={"mediaId":7015,"level":"B","keyWord":"dairy","defaultVoice":"female",
"taps":[
 {"phrase":"to carry two pails of milk","target":"the young woman","voice":"female","keys":K(woman)},
 {"phrase":"to walk in single file","target":"the cows","voice":"female","keys":K(cows)},
 {"phrase":"to stand by the shed door","target":"the farmer","voice":"male","keys":K(farmer)}],
"stillS":1.7,
"nouns":[{"word":"a farmer","x":0.60,"y":0.33,"voice":"male"},{"word":"a shed","x":0.80,"y":0.13,"voice":"female"},
 {"word":"milk churns","x":0.79,"y":0.45,"voice":"female"},{"word":"straw","x":0.86,"y":0.75,"voice":"female"}],
"question":"What is the young woman carrying?",
"answer":["She","is","carrying","two","pails","of","milk."],
"answerVoice":"female",
"notes":"Key word 'dairy' is not a visible countable noun, so not placed. Cows box covers the whole line; split from the woman at about x .42-.44 (her left bucket is slightly cut early on). Milk spills only in the first second, so the phrase uses carrying."}
json.dump(c,open('content/7015.json','w'),indent=1)
