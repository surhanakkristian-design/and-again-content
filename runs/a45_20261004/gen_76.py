import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def write(mid,level,kw,dv,taps,still,nouns,q,a,av,notes):
    json.dump({"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
      "taps":[{"phrase":p,"target":t,"voice":v,"keys":keys(k)} for p,t,v,k in taps],
      "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
      "question":q,"answer":a,"answerVoice":av,"notes":notes},open(f"content/{mid}.json","w"),indent=1)
woman={0.0:(0,0,1,.82),0.5:(0,0,1,.82),1.0:(0,0,1,.84),1.5:(0,0,1,.65),2.0:(0,.03,.60,.84),2.5:(0,.11,.55,.76),
 3.0:(0,.10,.56,.84),3.5:(0,0,.80,.80),4.0:(0,0,.55,.78),4.5:(0,0,.51,.82),5.0:(0,0,1,.95),5.5:(0,0,1,.95),
 6.0:(0,.06,.57,.66),6.5:(0,.07,.58,.65),8.5:(0,.12,.50,.62),9.0:(0,.15,.54,.76),9.5:(0,.13,.52,.77),10.0:(0,.10,.54,.67)}
man={2.0:(.61,.07,.39,.50),2.5:(.56,.12,.44,.46),3.0:(.57,.10,.43,.56),3.5:(.81,0,.19,.52),4.0:(.56,.34,.44,.29),
 4.5:(.53,.24,.47,.56),6.0:(.58,.09,.42,.58),6.5:(.60,.09,.40,.57),8.0:(.02,.18,.76,.52),8.5:(.52,.14,.48,.48),
 9.0:(.56,.13,.44,.62),9.5:(.55,.10,.45,.63),10.0:(.57,.10,.43,.54)}
write(76,"A","battery","female",
 [("to hold a flashlight","the woman","female",woman),
  ("to wear a grey hat","the man","male",man),
  ("to put in new batteries","the woman","female",woman)],
 10.0,[("batteries",.53,.77,"female"),("a cup",.80,.66,"female"),("a hat",.82,.20,"female"),("a woman",.22,.35,"female")],
 "What is the woman holding?",["She","is","holding","a","flashlight."],"female",
 "Close-ups 0-1.5 s and 5-5.5 s show only the woman's body and hands (rust shirt): boxed as the woman. At 4.0-4.5 s the right hand with the two batteries has a dark sleeve = the man. 7.0-7.5 s nobody (ceiling), 8.0 s only the man. Man's phrase is a state (his actions are not his alone). 'flashlight' is US English.")
