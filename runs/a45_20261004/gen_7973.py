import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
suit=[(.06,.35,.30,.32),(.10,.35,.28,.33),None,None,(.47,.33,.155,.40),(.47,.32,.16,.43),(.46,.33,.175,.44),(.475,.33,.15,.46)]
wom=[(.40,.34,.29,.39),(.39,.31,.28,.44),(.22,.29,.39,.45),(.21,.29,.33,.45),(.12,.26,.345,.52),(.12,.26,.345,.53),(.15,.28,.30,.55),(.17,.28,.30,.55)]
yng=[(.69,.40,.18,.32),(.68,.39,.19,.34),(.62,.38,.26,.34),(.64,.36,.26,.36),(.63,.32,.28,.45),(.635,.28,.27,.51),(.64,.29,.26,.52),(.63,.29,.29,.53)]
def k(L): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,L)]
c={"mediaId":7973,"level":"B","keyWord":"school year","defaultVoice":"female",
"taps":[{"phrase":"to swing the door open","target":"the man in the suit","voice":"male","keys":k(suit)},
{"phrase":"to clutch her books","target":"the young woman","voice":"female","keys":k(wom)},
{"phrase":"to grip his backpack straps","target":"the young man","voice":"male","keys":k(yng)}],
"stillS":3.7,
"nouns":[{"word":"the sky","x":.82,"y":.12,"voice":"female"},{"word":"a lantern","x":.64,"y":.30,"voice":"female"},
{"word":"books","x":.33,"y":.43,"voice":"female"},{"word":"autumn leaves","x":.35,"y":.92,"voice":"female"}],
"question":"What is the young woman holding?","answer":["She","is","clutching","a","pile","of","books."],
"answerVoice":"female","notes":"Man in the suit is 'off' at 1.2 and 1.7 s: he is almost fully hidden behind the woman (only legs/shoulder peek out). He swings the door open at 0.2-0.7 s only. 'school year' not a visible noun."}
json.dump(c,open("content/7973.json","w"),indent=1)
