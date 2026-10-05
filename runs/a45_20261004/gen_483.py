import json
T=[i*0.5 for i in range(21)]
mk=[(.28,.07,.46,.88),(.28,.08,.40,.88),(.25,.10,.45,.90),(.24,.18,.40,.82),(.20,.24,.40,.76),(.16,.26,.38,.74),(0,0,.88,.62),(.36,.18,.64,.82),(.36,.26,.64,.52),(.18,.24,.70,.50),
(.28,.06,.42,.94),(.33,0,.42,.92),(.27,0,.45,.72),(.12,.34,.60,.34),(.15,0,.33,.44),(.03,0,.66,.55),(.16,.04,.56,.78),(.11,.18,.66,.80),(0,.18,.86,.82),(0,.18,.84,.82),(0,.18,.76,.82)]
man=[None]*10+[(.80,.84,.20,.16),(.78,.66,.22,.30),(.74,.46,.26,.52),(.74,.42,.26,.50),(.66,.52,.34,.48),(.48,.56,.52,.44),(.52,.82,.48,.18)]+[None]*4
def keys(b):
    return [({"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} if k else {"t":t,"off":True}) for t,k in zip(T,b)]
d={"mediaId":483,"level":"A","keyWord":"a monkey","defaultVoice":"male",
"taps":[
 {"phrase":"to climb a big tree","target":"the monkey","voice":"male","keys":keys(mk)},
 {"phrase":"to eat a banana","target":"the monkey","voice":"male","keys":keys(mk)},
 {"phrase":"to wave a hat","target":"the man","voice":"male","keys":keys(man)}],
"stillS":6.5,
"nouns":[{"word":"a monkey","x":.48,"y":.50,"voice":"male"},{"word":"bananas","x":.50,"y":.64,"voice":"male"},{"word":"stairs","x":.80,"y":.25,"voice":"male"},{"word":"a table","x":.50,"y":.77,"voice":"male"}],
"question":"What is the monkey eating?",
"answer":["The","monkey","is","eating","a","banana."],"answerVoice":"male",
"notes":"Only two possible targets (monkey, fruit seller). At 7.0 s only the monkey's tail is in the picture (box on the tail). The man is in frame only 5.0-8.0 s, at 5.0 and 8.0 just partly. 'a hat' left out of the nouns: at 7.5 s he seems to wear one hat and wave another. Still 6.5 s: the monkey holds one banana above the basket of bananas; the table is covered by a cloth, pill on its front edge."}
json.dump(d,open("content/483.json","w"),indent=1,ensure_ascii=False)
