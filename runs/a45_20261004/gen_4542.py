import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(.18,.25,.58,.75),0.5:(.22,.23,.62,.77),1.0:(.09,.24,.72,.76),1.5:(.10,.25,.68,.75),
 2.0:(.75,.40,.23,.30),2.5:(.81,.40,.19,.30),3.0:(.30,.42,.65,.32),3.5:(.28,.42,.66,.31),
 4.0:(.27,.37,.69,.35),4.5:(.25,.36,.72,.36),5.0:(.25,.36,.72,.37),5.5:(.25,.36,.72,.37),6.0:(.24,.36,.72,.36),
 7.5:(.48,.46,.50,.17),8.0:(.27,.42,.68,.22),8.5:(.47,.26,.45,.39),9.0:(.42,.28,.42,.37)}
screen={2.0:(.48,.22,.26,.32),2.5:(.22,.22,.59,.33),3.0:(.09,.21,.80,.21),3.5:(.07,.20,.84,.22),
 4.0:(.07,.17,.86,.20),4.5:(.07,.16,.88,.20),5.0:(.05,.16,.90,.20),5.5:(.05,.16,.90,.20),6.0:(.05,.16,.90,.20),
 7.5:(.24,.27,.74,.19),8.0:(.24,.27,.72,.15),8.5:(.27,.27,.20,.28),9.0:(.24,.29,.18,.26)}
hand={6.5:(.50,.46,.48,.28),7.0:(.45,.59,.53,.27),7.5:(.62,.63,.30,.14),8.0:(.60,.64,.30,.14),8.5:(.62,.65,.30,.14),9.0:(.60,.65,.30,.14)}
c={"mediaId":4542,"level":"B","keyWord":"agreement","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold up a tablet","target":"the man in white","voice":"male","keys":keys(man)},
  {"phrase":"to display rows of designs","target":"the big screen","voice":"male","keys":keys(screen)},
  {"phrase":"to sketch with a stylus","target":"the hand with the pen","voice":"male","keys":keys(hand)}],
 "stillS":8.0,
 "nouns":[{"word":"a screen","x":.55,"y":.31,"voice":"male"},{"word":"a headdress","x":.66,"y":.44,"voice":"male"},
          {"word":"a handshake","x":.33,"y":.58,"voice":"male"},{"word":"a notebook","x":.25,"y":.91,"voice":"male"}],
 "question":"What is the man in white doing?",
 "answer":["He","is","sealing","an","agreement","with","a","handshake."],
 "answerVoice":"male",
 "notes":"Clip has cuts (corridor, meeting room, tablet close-up, wide room). Man and screen overlap in the picture from 3.0 s on: split horizontally at the top of his headdress, so the screen box covers only the upper part of the screen; at 8.5/9.0 he stands in front of it and the screen box is only its visible left strip. Hand with the pen: clear at 6.5/7.0 (close-up); at 7.5-9.0 it is the small hand of the woman on the right holding the stylus over the tablet, boxes small and split from the man's box. 6.5/7.0: only the man's hands are in the picture -> off. 'sealing an agreement' interprets the handshake (key word); a second, open white pad lies near the dark notebook."}
json.dump(c,open('content/4542.json','w'),indent=1,ensure_ascii=False)
