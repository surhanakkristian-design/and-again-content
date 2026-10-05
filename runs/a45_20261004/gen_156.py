import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,.10,1,.90),0.5:(0,.10,1,.90),1.0:(0,.08,1,.92),1.5:(0,.07,1,.93),2.0:(0,.07,1,.93),2.5:(0,.12,1,.88),3.0:(0,.10,1,.90),
3.5:(0,.07,1,.93),4.0:(0,.10,1,.90),4.5:(.12,.15,.88,.85),5.0:(0,.05,1,.95),5.5:(0,.08,1,.92),6.0:(0,.05,1,.95),6.5:(0,.05,1,.95),
7.0:(0,.05,1,.95),7.5:(0,.05,1,.95),8.0:(0,.06,1,.94),8.5:(0,.06,1,.94),9.0:(0,.04,1,.96),9.5:(0,.04,1,.96),10.0:(0,.03,1,.97)}
k=keys(man)
c={"mediaId":156,"level":"A","keyWord":"chest","defaultVoice":"male",
"taps":[
 {"phrase":"to wipe his face","target":"the man","voice":"male","keys":k},
 {"phrase":"to get a gold medal","target":"the man","voice":"male","keys":k},
 {"phrase":"to touch his chest","target":"the man","voice":"male","keys":k}],
"stillS":7.0,
"nouns":[{"word":"a chest","x":.50,"y":.65,"voice":"male"},{"word":"a medal","x":.47,"y":.92,"voice":"male"},
 {"word":"flags","x":.80,"y":.50,"voice":"male"},{"word":"hair","x":.50,"y":.19,"voice":"male"}],
"question":"What is the man touching?",
"answer":["He","is","touching","his","chest."],
"answerVoice":"male",
"notes":"Only one usable target: the runner fills the frame in every shot; the medal and the flags lie inside / behind him (boxes would overlap) and the clapping people are tiny blurred figures at the edge. So all three phrases share the man. At 4.5 the left strip (person in a yellow vest putting the medal on) is left out of his box. 'a chest' pill sits on the ribbon over his chest."}
json.dump(c,open("content/156.json","w"),indent=1)
