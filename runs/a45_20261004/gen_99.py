import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
R={0.0:(.18,.42,.82,.58),0.5:(.55,0,.45,1),1.0:(.22,.08,.78,.92),1.5:(.28,.08,.72,.92),2.0:(.20,0,.80,1),2.5:(.80,0,.20,.80),3.0:(.78,.60,.22,.40),3.5:None,
4.0:(.80,.55,.20,.15),4.5:(.63,.30,.37,.32),5.0:(.66,.60,.34,.20),5.5:None,6.0:(.44,.10,.56,.90),6.5:(.38,.14,.62,.86),7.0:(.31,.18,.69,.82),7.5:(.36,.20,.64,.80),
8.0:(.40,.20,.60,.80),8.5:(.44,.20,.56,.80),9.0:(.42,.20,.58,.80),9.5:(.06,.20,.94,.49),10.0:(.22,.20,.78,.49)}
F={0.0:None,0.5:None,1.0:None,1.5:None,2.0:None,2.5:(0,.34,.30,.16),3.0:(0,.08,.44,.56),3.5:(0,.10,.45,.56),4.0:(0,.14,.47,.56),4.5:(0,.18,.50,.52),5.0:(0,.20,.45,.60),5.5:(0,.28,.32,.50),
6.0:None,6.5:None,7.0:None,7.5:None,8.0:None,8.5:None,9.0:None,9.5:None,10.0:None}
C={0.0:None,0.5:None,1.0:None,1.5:None,2.0:None,2.5:(0,.70,.24,.22),3.0:(.03,.68,.36,.22),3.5:(.25,.76,.30,.20),4.0:(.34,.73,.30,.20),4.5:(.36,.75,.27,.20),5.0:(.35,.84,.28,.16),5.5:(.28,.84,.30,.16),
6.0:(.12,.76,.31,.22),6.5:(.05,.76,.32,.22),7.0:(0,.74,.30,.26),7.5:(0,.76,.35,.24),8.0:(.07,.69,.32,.21),8.5:(.08,.70,.35,.22),9.0:(.08,.72,.33,.20),9.5:(.17,.70,.30,.24),10.0:(.08,.70,.38,.22)}
c={"mediaId":99,"level":"A","keyWord":"book","defaultVoice":"female",
"taps":[tap("to read a green book","the red-haired woman","female",R),tap("to hold a big cup","the woman with short hair","female",F),tap("to sleep on the blanket","the cat","female",C)],
"stillS":8.0,
"nouns":[noun("a window",.14,.25,"female"),noun("a book",.62,.54,"female"),noun("a cat",.22,.81,"female"),noun("a blanket",.66,.88,"female")],
"question":"What is the red-haired woman doing?","answer":["She","is","reading","a","green","book."],"answerVoice":"female",
"notes":"Many cuts and close-ups. Red-haired woman: only her hands/arms at 0.0, 3.0, 4.0-5.0 (cream sweater sleeve), off at 3.5 and 5.5 (a sliver at the edge). The friend is only a hand with the cup at 2.5. The cat is dark and partly hidden by the book/blanket at 2.5-5.5 (weak there), clear from 6.0. Cat box and woman box are split next to each other from 6.0, the woman's left elbow/hand is cut a little at 6.5-9.0. Still 8.0: she hugs the book, the book pill sits on the book on her chest; no noun for the woman."}
json.dump(c,open('content/99.json','w'),indent=1)
