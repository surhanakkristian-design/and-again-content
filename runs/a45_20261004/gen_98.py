import json
W={0.0:(.12,.08,.83,.58),0.5:(.12,.08,.83,.58),1.0:(.12,.10,.83,.56),1.5:(.15,.10,.80,.54),2.0:(.15,.13,.68,.44),2.5:(.17,.13,.68,.45),
3.0:(0,0,1,.78),3.5:(0,0,1,.77),4.0:None,4.5:None,5.0:(.35,0,.65,.53),5.5:(.05,0,.95,.70),6.0:(0,0,1,.63),6.5:(.20,.05,.80,.50),
7.0:(.25,.08,.70,.39),7.5:(.25,.10,.70,.39),8.0:(.28,.12,.62,.36),8.5:(.25,.13,.65,.41),9.0:(.20,.19,.65,.41)}
B={0.0:(0,.66,1,.34),0.5:(0,.66,1,.34),1.0:(0,.66,1,.34),1.5:(0,.64,1,.36),2.0:(0,.57,1,.43),2.5:(0,.58,1,.42),
3.0:(0,.78,1,.22),3.5:(0,.77,1,.23),4.0:(0,.20,1,.77),4.5:(0,.22,1,.70),5.0:(0,.53,1,.45),5.5:(0,.70,1,.28),6.0:(0,.63,1,.31),6.5:(.05,.55,.45,.40),
7.0:(.20,.47,.52,.34),7.5:(.22,.49,.52,.34),8.0:(.23,.48,.50,.30),8.5:(.10,.54,.42,.37),9.0:(0,.60,.95,.28)}
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
c={"mediaId":98,"level":"B","keyWord":"hammock","defaultVoice":"female",
"taps":[{"phrase":"to gasp in astonishment","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to clutch a book tightly","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have a burgundy cover","target":"the book","voice":"female","keys":keys(B)}],
"stillS":8.0,
"nouns":[{"word":"a hammock","x":.14,"y":.70,"voice":"female"},{"word":"a dome","x":.86,"y":.17,"voice":"female"},
{"word":"a braid","x":.72,"y":.52,"voice":"female"},{"word":"flowers","x":.25,"y":.12,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","reading","a","book","in","a","hammock."],"answerVoice":"female",
"notes":"Woman and book overlap in the picture: the woman's box is her head/upper body above the book, the book's box is below the split line; her body beside/below the book (6.5-8.5 s) is in neither box. 4.0-4.5 s: close-up of the book with only her hand, woman set off. The book phrase is a state (the book does nothing only it does). Hammock pill sits on the netting at the lower left edge, which is narrow."}
json.dump(c,open('content/98.json','w'),indent=1)
