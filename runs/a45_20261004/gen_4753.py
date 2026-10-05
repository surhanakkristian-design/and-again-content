import json
def keys(times, d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True} for t in times]
times=[i*0.5 for i in range(25)]
bm={};rd={};bk={}
for t in times[:12]:
    bm[t]=(0,.07,.47,.90); rd[t]=(.57,.05,.43,.52); bk[t]=(.47,.57,.53,.43)
def s(t,a,b,c): bm[t]=a; rd[t]=b; bk[t]=c
s(6.0,(.05,.08,.50,.88),(.55,.05,.45,.52),(.55,.57,.45,.43))
s(6.5,(.05,.08,.47,.88),(.55,.05,.45,.52),(.52,.57,.48,.43))
s(7.0,(0,.07,.50,.90),(.52,.07,.48,.50),(.50,.57,.50,.43))
s(7.5,(0,.07,.50,.90),(.52,.07,.48,.50),(.50,.57,.50,.43))
s(8.0,(0,.07,.49,.90),(.51,.05,.49,.52),(.49,.57,.51,.43))
s(8.5,(0,.07,.46,.90),(.46,.05,.54,.52),(.46,.57,.54,.43))
s(9.0,(0,.07,.47,.90),(.47,.07,.53,.50),(.47,.57,.53,.43))
s(9.5,(0,.08,.51,.90),(.51,.08,.49,.49),(.51,.57,.49,.43))
s(10.0,(0,.08,.54,.90),(.55,.08,.45,.49),(.54,.58,.46,.42))
s(10.5,(.05,.10,.47,.87),(.52,.08,.48,.49),(.52,.57,.48,.43))
s(11.0,(.08,.18,.38,.80),(.46,.05,.49,.50),(.46,.57,.46,.43))
s(11.5,(.10,.18,.37,.80),(.47,.07,.50,.49),(.47,.57,.51,.43))
s(12.0,(.08,.17,.38,.80),(.46,.07,.48,.50),(.46,.58,.54,.42))
c={"mediaId":4753,"level":"B","keyWord":"forgive","defaultVoice":"male",
"taps":[
{"phrase":"to fold his arms tightly","target":"the man in the blue hoodie","voice":"male","keys":keys(times,bm)},
{"phrase":"to offer a takeaway coffee","target":"the bearded man","voice":"male","keys":keys(times,rd)},
{"phrase":"to have a taped handlebar","target":"the bike","voice":"male","keys":keys(times,bk)}],
"stillS":2.0,
"nouns":[{"word":"a beard","x":.74,"y":.22,"voice":"male"},{"word":"a takeaway cup","x":.60,"y":.35,"voice":"male"},
{"word":"a brick wall","x":.82,"y":.48,"voice":"male"},{"word":"a saddle","x":.63,"y":.59,"voice":"male"}],
"question":"What is the bearded man offering?",
"answer":["He","is","offering","him","a","takeaway","coffee."],
"answerVoice":"male",
"notes":"Key word 'forgive' is a verb that cannot be seen directly, so the question is about the coffee the bearded man hands over (8.5-9.5 s), not about forgiving. Bike phrase is a state ('to have a taped handlebar') because 'lean against the wall' would also fit the bearded man. The three targets are close: boxes are split on vertical lines, so the bike box loses the handlebar end / ribbons on the left and the blue man's hand is cut at 8.5 and 10.0. From 10.5 the men hug and overlap: split on a vertical line at x~0.46-0.52 (blue man left, bearded man right; the blue man's arm with the cup lies inside the bearded man's box at 11.0-12.0)."}
json.dump(c,open("content/4753.json","w"),indent=1,ensure_ascii=False)
