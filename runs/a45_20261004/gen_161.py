import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman={0.5:(.14,.22,.44,.34),1.0:(.03,.17,.57,.44),1.5:(0,.10,.37,.50),2.0:(0,.02,.24,.52),2.5:(0,0,.25,.56),3.0:(0,.05,.27,.50),
8.5:(0,.10,.09,.30),9.0:(0,.24,.11,.28)}
man={1.5:(.37,.10,.55,.26),2.0:(.24,.02,.57,.31),2.5:(.25,0,.58,.32),3.0:(.27,0,.54,.33),3.5:(0,0,.56,.50),4.0:(0,0,.58,.50),
4.5:(0,0,.60,.51),5.0:(0,0,.61,.51),5.5:(0,0,.53,.55),6.0:(0,0,.50,.56),6.5:(0,0,.52,.54),7.0:(0,0,.56,.42),7.5:(0,0,.70,.67),
8.0:(0,0,.68,.70),8.5:(.09,0,.71,.95),9.0:(.11,0,.72,.95),9.5:(0,0,.95,.57),10.0:(0,0,.92,.57)}
dog={2.0:(.82,.10,.18,.18),2.5:(.83,.08,.17,.20),3.0:(.82,.08,.18,.20),3.5:(.70,.22,.30,.21),4.0:(.72,.21,.28,.22),4.5:(.72,.21,.28,.22),
5.0:(.73,.21,.27,.22),9.5:(.41,.58,.26,.15),10.0:(.43,.57,.27,.17)}
c={"mediaId":161,"level":"B","keyWord":"chicken drumstick","defaultVoice":"male",
"taps":[
 {"phrase":"to bite into a drumstick","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to pull out the roasting tray","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to peek over the counter","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":8.5,
"nouns":[{"word":"a drumstick","x":.55,"y":.29,"voice":"male"},{"word":"herbs","x":.84,"y":.45,"voice":"male"},
 {"word":"limes","x":.88,"y":.67,"voice":"male"},{"word":"a plate","x":.62,"y":.80,"voice":"male"}],
"question":"What is the man biting into?",
"answer":["He","is","biting","into","a","chicken","drumstick."],
"answerVoice":"male",
"notes":"Woman is clearly visible only 0.5-3.0 (pulling the tray out of the oven, seen from inside the oven); at 8.5-9.0 only a sliver of her face at the left edge (narrow box). The hand opening the oven at 0.0 is not attributable -> all off. Man off at 1.0 (blurred behind the woman). Dog: boxes where its face is visible (2.0-5.0, 9.5-10.0); at 8.0-9.0 only a dark shape of its back, set off. At 9.5-10.0 the dog peeks over the counter next to the man's waist, so the man's box covers only his upper body (y < .57). The man bites at 8.5-9.0."}
json.dump(c,open("content/161.json","w"),indent=1)
