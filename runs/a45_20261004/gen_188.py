import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
N=None

P={0.0:(.35,.43,.30,.25),0.5:(.08,.24,.80,.60),1.0:(.08,.25,.82,.68),1.5:N,2.0:N,2.5:N,3.0:N,3.5:N,4.0:N,4.5:(0,.15,1,.85),5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:N,6.5:N,
7.0:(.75,.24,.25,.72),7.5:(.66,.36,.34,.60),8.0:(.71,.40,.29,.42),8.5:(.40,.54,.18,.14),9.0:(.42,.55,.18,.14)}
J={0.0:N,0.5:N,1.0:N,1.5:(.20,.27,.62,.34),2.0:N,2.5:N,3.0:(.84,0,.16,.30),3.5:(.82,0,.18,.48),4.0:(.25,.15,.50,.27),4.5:N,5.0:N,5.5:N,6.0:(0,0,1,.47),6.5:(0,0,1,.39),
7.0:(.28,.13,.44,.34),7.5:(.28,.12,.44,.20),8.0:(.28,.13,.44,.20),8.5:(.40,.40,.18,.14),9.0:(.40,.41,.18,.14)}
B={0.0:N,0.5:N,1.0:N,1.5:(.15,.61,.68,.14),2.0:(0,.38,1,.41),2.5:(0,.36,1,.32),3.0:(.05,.10,.79,.85),3.5:(.08,.12,.74,.82),4.0:(0,.42,1,.30),4.5:N,5.0:N,5.5:N,6.0:(0,.47,1,.48),6.5:(0,.39,1,.56),
7.0:(0,.47,.74,.32),7.5:(.12,.32,.53,.46),8.0:(.27,.33,.43,.35),8.5:N,9.0:N}
c={"mediaId":188,"level":"B","keyWord":"constitution","defaultVoice":"male",
"taps":[tap("to lean across the table","the man in the suit","male",P),tap("to wear a powdered wig","the judge","male",J),tap("to bear two wax seals","the book","male",B)],
"stillS":4.0,
"nouns":[noun("a wig",.50,.20,"male"),noun("a constitution",.50,.56,"male"),noun("marble",.50,.88,"male")],
"question":"What is the politician reading?","answer":["He","is","reading","a","page","of","the","constitution."],"answerVoice":"male",
"notes":"Animated clip with many cuts. Key word constitution = the huge sealed book; the noun pill 'a constitution' sits on the open book (weak spot: it is only identifiable as a constitution from the story). The wigged official's gender is unclear, called 'the judge', voice = default (male). The judge phrase is a state (wig) because the judge's actions are mostly shown as gloved hands only (2.0, 2.5: judge off, only hands). 'to lean across the table' is seen at 7.0-8.0 only; the man in the suit at 0.0 sits among other suited men (box on the one in the middle who speaks). 8.5/9.0: tiny figures in a wide shot, minimum-size boxes; the young aide next to them has no box. Question subject 'the politician' = the man in the suit (reads the page at 7.0-8.0)."}
json.dump(c,open('content/188.json','w'),indent=1)
