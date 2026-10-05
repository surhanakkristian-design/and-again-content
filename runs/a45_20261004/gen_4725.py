import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.5:(.55,0,.45,.63),1.0:(.43,0,.57,.82),3.5:(.66,.20,.34,.65),4.0:(.63,.16,.37,.56),4.5:(.66,.18,.34,.56),
     5.0:(.72,.13,.28,.85),5.5:(.38,.06,.62,.94),6.0:(0,0,.60,.97),7.5:(0,.09,.20,.28),8.0:(0,.18,.28,.17)}
woman={0.0:(0,0,.33,.52),1.5:(.78,.05,.22,.65),2.0:(.58,.03,.42,.57),2.5:(.62,.10,.38,.48),3.0:(.63,.17,.37,.50),
     3.5:(.48,.27,.18,.22),4.0:(.45,.23,.18,.19),4.5:(.49,.25,.17,.20),5.0:(.11,.26,.58,.64),5.5:(0,.24,.38,.76),
     6.5:(.33,.26,.33,.22),7.0:(0,.30,.12,.34),7.5:(0,.37,.24,.27),8.0:(.12,.35,.18,.15),8.5:(.06,.32,.22,.20),
     9.0:(.06,.34,.22,.20),9.5:(.07,.34,.22,.20),10.0:(0,.31,.20,.20)}
boy={0.5:(.25,.31,.28,.22),1.0:(.05,.50,.37,.27),1.5:(.17,.40,.45,.33),2.0:(.10,.32,.48,.30),2.5:(.08,.31,.54,.31),
     3.0:(.13,.32,.48,.42),3.5:(.32,.49,.34,.31),4.0:(.28,.42,.35,.28),4.5:(.31,.45,.35,.27)}
c={"mediaId":4725,"level":"A","keyWord":"pizza","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold the dough up","target":"the man in blue","voice":"male","keys":keys(man)},
  {"phrase":"to throw some flour","target":"the woman","voice":"female","keys":keys(woman)},
  {"phrase":"to wear no shirt","target":"the little boy","voice":"male","keys":keys(boy)}],
 "stillS":5.0,
 "nouns":[{"word":"a woman","x":.28,"y":.38,"voice":"female"},{"word":"a pizza","x":.50,"y":.54,"voice":"male"},
          {"word":"an oven","x":.68,"y":.70,"voice":"male"},{"word":"a table","x":.30,"y":.88,"voice":"male"}],
 "question":"What is the woman carrying?",
 "answer":["She","is","carrying","a","pizza."],
 "answerVoice":"female",
 "notes":"Many cuts and many people. The man in blue = the man in the blue T-shirt (holds the dough up at 1.0 s); at night he is boxed only at 7.5 and 8.0 s (top left, leaning in) - later his identity is unclear, so off. The woman = dark-haired woman in the white top (sprinkles flour at 2.0-3.0 s); a second dark-haired woman sits on the right at night and is not boxed. The little boy = the shirtless boy in the kitchen only; the child at the night table wears a shirt and is not boxed. 'to wear no shirt' is a state: his dough-pressing is not unique (the man and the grandmother also work dough). The man also carries a pizza, so the question names the woman. Still 5.0 s: a second pizza is cut by the right edge; 'a table' = the worktop in the foreground."}
json.dump(c,open('content/4725.json','w'),indent=1,ensure_ascii=False)
