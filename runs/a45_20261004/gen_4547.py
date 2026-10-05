import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
boy={0.0:(0,.49,.31,.51),0.5:(0,.49,.46,.51),1.0:(0,.44,.50,.56),1.5:(0,.35,.70,.65),2.0:(.02,.16,.86,.84),
 2.5:(.33,.13,.67,.87),3.0:(.33,.15,.67,.85),3.5:(.72,.19,.28,.81),4.0:(.66,.17,.34,.83),4.5:(.40,.03,.60,.97),
 5.0:(.68,0,.32,1.0),5.5:(.58,0,.42,1.0),6.0:(.52,.19,.48,.79),6.5:(.53,.37,.47,.63),
 7.0:(.665,.36,.335,.64),7.5:(.45,.375,.55,.625),8.0:(.665,.34,.335,.66),8.5:(.69,.35,.31,.65),
 9.0:(.645,.36,.355,.64),9.5:(.40,.39,.60,.61),10.0:(.40,.20,.54,.80)}
old={3.5:(.55,.43,.15,.20),4.0:(.50,.41,.16,.16),5.0:(.52,.19,.16,.40),5.5:(.23,.28,.23,.34),
 6.0:(.08,.30,.29,.40),6.5:(0,.34,.34,.40),7.0:(0,.36,.30,.42),7.5:(0,.34,.215,.44),8.0:(0,.35,.24,.42),
 8.5:(0,.35,.23,.42),9.0:(0,.36,.24,.44),9.5:(0,.37,.20,.40),10.0:(0,.39,.28,.42)}
doc={6.5:(.52,.22,.18,.15),7.0:(.50,.25,.165,.29),7.5:(.50,.24,.18,.135),8.0:(.50,.24,.165,.33),
 8.5:(.51,.24,.18,.33),9.0:(.49,.26,.155,.30),9.5:(.50,.26,.18,.13)}
c={"mediaId":4547,"level":"B","keyWord":"waiting room","defaultVoice":"male",
 "taps":[
  {"phrase":"to collect a paper ticket","target":"the boy","voice":"male","keys":keys(boy)},
  {"phrase":"to lean on a walking stick","target":"the old man","voice":"male","keys":keys(old)},
  {"phrase":"to appear in the doorway","target":"the doctor","voice":"female","keys":keys(doc)}],
 "stillS":8.5,
 "nouns":[{"word":"a doctor","x":.62,"y":.34,"voice":"female"},{"word":"a cardigan","x":.35,"y":.55,"voice":"male"},
          {"word":"a backpack","x":.88,"y":.60,"voice":"male"},{"word":"magazines","x":.14,"y":.84,"voice":"male"}],
 "question":"What is the old man doing?",
 "answer":["He","is","sitting","in","the","waiting room."],
 "answerVoice":"male",
 "notes":"The packet says the boy presses a bell; the frames (4.0-5.0 s) show him taking a white paper slip from a ticket dispenser on the counter, so phrase 1 is 'to collect a paper ticket'. The key word 'waiting room' is the whole room, not one place: no noun slot, used in the answer instead ('waiting room.' as one chip). The doctor stands behind the boy from 6.5 s: boxes split vertically at the boy's head (7.0, 8.0, 8.5, 9.0: the boy's box loses his knees) or horizontally at the top of his head (6.5, 7.5, 9.5: the doctor's box is head and chest only). The old man is half hidden behind the mother at 3.5/4.0/5.0 (small boxes; at 4.0 the boy's box loses his reaching arm), not recognisable at 4.5 -> off. 'a cardigan' is the mother's dark red one."}
json.dump(c,open('content/4547.json','w'),indent=1,ensure_ascii=False)
