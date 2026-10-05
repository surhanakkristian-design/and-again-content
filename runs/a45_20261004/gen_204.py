import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
B={0.0:(.10,0,.70,.93),0.5:(.11,.02,.71,.90),1.0:(.12,0,.66,.97),1.5:(.12,.02,.63,.95),2.0:(.16,0,.57,.88),2.5:(.15,0,.62,.88),3.0:(.20,0,.67,.95),3.5:(.11,0,.70,.95),
4.0:(.09,0,.62,.95),4.5:(.09,0,.74,.97),5.0:(.09,0,.66,1),5.5:(.11,0,.73,1),6.0:(.11,0,.64,.97),6.5:(.13,0,.73,.97),7.0:(.09,.03,.69,.95),7.5:(.08,.03,.74,.95),
8.0:(.08,.03,.60,.87),8.5:(.10,.03,.63,.89),9.0:(.13,.08,.68,.90),9.5:(.15,.08,.70,.90),10.0:(.19,.13,.64,.87)}
N={0.0:(0,.08,.10,.76),0.5:(0,.10,.11,.74),1.0:(0,.15,.12,.75),1.5:(0,.18,.12,.74),2.0:(0,.07,.16,.70),2.5:(0,.07,.15,.70),3.0:(0,.08,.20,.84),3.5:(0,.07,.11,.85),
4.0:(0,.12,.09,.68),4.5:(0,.18,.09,.62),5.0:(0,.15,.09,.50),5.5:(0,.15,.11,.72),6.0:(0,.12,.11,.64),6.5:(0,.18,.13,.55),7.0:(0,.24,.09,.58),7.5:None,
8.0:None,8.5:None,9.0:(0,.28,.12,.50),9.5:(0,.27,.14,.53),10.0:(0,.25,.17,.45)}
c={"mediaId":204,"level":"B","keyWord":"crutch","defaultVoice":"male",
"taps":[tap("to walk on crutches","the boy","male",B),tap("to clutch a clipboard","the nurse","female",N),tap("to raise a clenched fist","the boy","male",B)],
"stillS":3.0,
"nouns":[noun("a nurse",.13,.42,"female"),noun("a crutch",.71,.60,"male"),noun("a medical boot",.45,.80,"male"),noun("a door handle",.86,.34,"male")],
"question":"What is the boy doing?","answer":["He","is","walking","on","two","crutches."],"answerVoice":"male",
"notes":"The nurse is only a strip at the left edge (0-0.2 wide), a sliver at 7.0 and gone at 7.5-8.5; her box is split from the boy's along her edge, so the boy's left crutch tip is sometimes cut. She holds the clipboard to 6.5 and claps with it at 9.5-10. The fist is raised only at 9.5-10. 'a crutch' sits on the boy's left crutch (right in the picture); the other crutch has no noun. Both boots are the same kind; the pill is between/on them."}
json.dump(c,open('content/204.json','w'),indent=1)
