import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [{"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,L)]
WO=[(.08,.12,.52,.90),(.05,.12,.52,.88),(.06,.13,.54,.90),(.06,.13,.55,.92),(.06,.13,.55,.92),(.06,.14,.57,.92),(.04,.13,.57,.95),(.04,.15,.61,.95)]
FR=[(.52,.05,.94,.33),(.52,.04,.94,.33),(.54,.04,.94,.32),(.55,.04,.95,.33),(.55,.05,.94,.33),(.57,.05,.96,.34),(.57,.06,.94,.36),(.62,.08,.96,.37)]
SM=[(.55,.70,1.0,.98),(.55,.70,1.0,.98),(.57,.73,1.0,.99),(.59,.76,1.0,1.0),(.64,.79,1.0,1.0),(.64,.82,1.0,1.0),(.78,.86,.98,1.0),(.80,.86,1.0,1.0)]
c={"mediaId":5543,"level":"A","keyWord":"alive","defaultVoice":"female",
"taps":[
{"phrase":"to laugh with joy","target":"the woman","voice":"female","keys":K(WO)},
{"phrase":"to shine in the sun","target":"the frame","voice":"female","keys":K(FR)},
{"phrase":"to make white smoke","target":"the smoker","voice":"female","keys":K(SM)}],
"stillS":1.2,
"nouns":[{"word":"bees","x":.58,"y":.05,"voice":"female"},
{"word":"a hive","x":.60,"y":.74,"voice":"female"},
{"word":"smoke","x":.90,"y":.83,"voice":"female"},
{"word":"grass","x":.36,"y":.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","lifting","a","frame","of","bees."],
"answerVoice":"female",
"notes":"The woman's box leaves out her raised arms and the frame (split at the frame's lower-left corner), so the frame can be its own target. The smoker's box includes the white smoke; from 3.2 s only its top is visible at the bottom right corner, the smoke mostly gone. The front hive is not a target (it overlaps the woman's and smoker's boxes). Key word 'alive' is an adjective that is hard to fit naturally ('a frame of live bees' would change the word); left out of the answer. 'smoke' pill is on the smoke cloud next to the smoker."}
json.dump(c,open("content/5543.json","w"),indent=1,ensure_ascii=False)
