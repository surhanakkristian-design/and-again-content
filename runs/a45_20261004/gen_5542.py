import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [{"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,L)]
WO=[(.08,.36,.64,.83),(.06,.37,.60,.83),(.03,.33,.56,.83),(.06,.35,.57,.83),(.03,.37,.55,.83),(.05,.39,.49,.81),(.09,.38,.44,.83),(.12,.25,.45,.82)]
DO=[(.64,.53,1.0,.83),(.60,.52,1.0,.83),(.56,.55,1.0,.83),(.57,.55,1.0,.83),(.55,.54,1.0,.83),(.50,.53,1.0,.83),(.61,.56,1.0,.82),(.66,.54,.93,.79)]
PO=[(.76,.33,.95,.48),(.76,.32,.96,.47),(.75,.34,.95,.48),(.70,.36,.89,.52),(.71,.36,.90,.52),(.71,.35,.90,.52),(.70,.37,.89,.53),(.68,.37,.89,.53)]
c={"mediaId":5542,"level":"B","keyWord":"alert","defaultVoice":"female",
"taps":[
{"phrase":"to leap up from the sofa","target":"the woman","voice":"female","keys":K(WO)},
{"phrase":"to tug at her sleeve","target":"the dog","voice":"female","keys":K(DO)},
{"phrase":"to boil over on the stove","target":"the pot","voice":"female","keys":K(PO)}],
"stillS":2.2,
"nouns":[{"word":"a border collie","x":.80,"y":.66,"voice":"female"},
{"word":"a pot","x":.80,"y":.45,"voice":"female"},
{"word":"cupboards","x":.80,"y":.26,"voice":"female"},
{"word":"a blanket","x":.25,"y":.86,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["It","is","alerting","the","woman","to","the","boiling","pot."],
"answerVoice":"female",
"notes":"Woman and dog boxes are split where her hand touches the dog's head (0.2-2.2 s). 'to tug at her sleeve': the dog's mouth is on her wrist/sleeve at 0.2-2.2 s; it reads more like nudging her hand, verifier may prefer 'to nudge her hand'. The leap up happens at 2.7-3.7 s. The pot is small; its box includes the steam above it and, from 1.7 s, the water running down the oven door."}
json.dump(c,open("content/5542.json","w"),indent=1,ensure_ascii=False)
