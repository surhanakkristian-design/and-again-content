import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2],2),"h":round(v[3],2)})
    return out
def B(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
def W(c): json.dump(c,open(f"content/{c['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 7040
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:B(.43,.19,.82,.52),0.7:B(.43,.19,.82,.60),1.2:B(.43,.19,.82,.60),1.7:B(.43,.19,.82,.60),
     2.2:B(.42,.20,.82,.61),2.7:B(.42,.20,.82,.61),3.2:B(.42,.20,.80,.61),3.7:B(.40,.21,.82,.62)}
man={0.2:B(.15,.13,.43,.58),0.7:B(.15,.13,.43,.58),1.2:B(.15,.13,.43,.58),1.7:B(.15,.13,.43,.58),
     2.2:B(.15,.12,.42,.58),2.7:B(.15,.12,.42,.58),3.2:B(.15,.13,.42,.58),3.7:B(.13,.13,.40,.58)}
dc={0.2:(.50,.59),0.7:(.51,.71),1.2:(.55,.76),1.7:(.57,.78),2.2:(.57,.79),2.7:(.57,.80),3.2:(.57,.80),3.7:(.57,.80)}
die={t:B(round(max(x-.10,.43),2),round(y-.07,2),round(x+.10,2),round(y+.07,2)) for t,(x,y) in dc.items()}
W({"mediaId":7040,"level":"B","keyWord":"die","defaultVoice":"female",
 "taps":[
  {"phrase":"to roll across the board","target":"the white die","voice":"female","keys":K(T,die)},
  {"phrase":"to clutch his head","target":"the man in black","voice":"male","keys":K(T,man)},
  {"phrase":"to toss a die","target":"the curly-haired woman","voice":"female","keys":K(T,wom)}],
 "stillS":2.7,
 "nouns":[{"word":"a die","x":.57,"y":.80,"voice":"female"},{"word":"popcorn","x":.16,"y":.65,"voice":"female"},
          {"word":"a board game","x":.66,"y":.67,"voice":"female"},{"word":"necklaces","x":.57,"y":.43,"voice":"female"}],
 "question":"What is rolling across the board?",
 "answer":["A","white","die","is","rolling","across","the","board."],
 "answerVoice":"female",
 "notes":"A second small die lies still at about (0.17,0.81); the target is the big rolling die, the 'a die' pill sits on it. 'to toss a die': the woman's throw is only visible as the open hand with the die in the air at 0.2 s; afterwards she holds her chest. Woman/man boxes split at x~0.42 (her hair overlaps his arm). The man in grey behind her is not a target."})

# ---------- 5517
wom={0.2:B(.03,.22,.50,.83),0.7:B(.02,.23,.52,.84),1.2:B(.01,.26,.53,.85),1.7:B(.02,.26,.47,.85),
     2.2:B(.0,.25,.41,.85),2.7:B(.02,.22,.56,.87),3.2:B(.30,.24,.54,.96),3.7:B(.24,.28,.52,.98)}
man={0.2:B(.50,.29,.81,.86),0.7:B(.52,.29,.85,.87),1.2:B(.53,.30,.88,.88),1.7:B(.47,.31,1.0,.90),
     2.2:B(.41,.20,1.0,.87),2.7:B(.56,.16,.88,.92),3.2:B(.54,.20,.88,.98),3.7:B(.52,.24,.86,1.0)}
fis={0.2:B(.81,.34,.99,.57),0.7:B(.85,.34,1.0,.57),1.2:B(.88,.40,1.0,.60)}
W({"mediaId":5517,"level":"B","keyWord":"accept","defaultVoice":"male",
 "taps":[
  {"phrase":"to accept a marriage proposal","target":"the woman","voice":"female","keys":K(T,wom)},
  {"phrase":"to hold a ring box","target":"the man in white","voice":"male","keys":K(T,man)},
  {"phrase":"to carry a fishing rod","target":"the man by the sea","voice":"male","keys":K(T,fis)}],
 "stillS":0.2,
 "nouns":[{"word":"a ring box","x":.52,"y":.53,"voice":"male"},{"word":"a picnic basket","x":.38,"y":.67,"voice":"male"},
          {"word":"a blanket","x":.55,"y":.81,"voice":"male"},{"word":"footprints","x":.50,"y":.92,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","accepting","his","marriage","proposal."],
 "answerVoice":"female",
 "notes":"The fisherman is only in the picture until about 1.2 s (half out of frame at 1.2), small box at the right edge. Couple boxes split at the joined hands; in the hug (3.2, 3.7) they overlap in the picture and are split left/right. 'a ring box' pill is small-target: it sits on the box in his hand, next to his arm."})

# ---------- 4125
T=[i*0.5 for i in range(31)]
man={0.0:B(.36,.54,.68,.83),0.5:B(.40,.60,.62,.84),1.0:B(.36,.63,.70,.89),1.5:B(.38,.74,.58,.90),
     4.0:B(.0,.59,.20,.81),4.5:B(.0,.58,.23,.81),5.0:B(.0,.59,.29,.82),5.5:B(.0,.61,.19,.83),6.0:B(.0,.65,.18,.81),
     7.0:B(.0,.63,.15,.85),7.5:B(.04,.62,.29,.90),8.0:B(.05,.63,.30,.92),8.5:B(.05,.63,.30,.92),9.0:B(.0,.64,.27,.94),9.5:B(.0,.64,.12,.92)}
fl={6.0:B(.30,.18,.98,.86),6.5:B(.08,.18,1.0,.88),7.0:B(.15,.20,1.0,.90),7.5:B(.29,.20,1.0,.90),8.0:B(.30,.22,.98,.91),
    8.5:B(.30,.22,.98,.91),9.0:B(.27,.22,.96,.92),9.5:B(.12,.20,1.0,.92),10.0:B(.02,.15,.98,.88),10.5:B(.0,.10,1.0,.90)}
el={12.0:B(.18,.24,.94,.90),12.5:B(.14,.22,1.0,.90),13.0:B(.09,.10,.99,.90),13.5:B(.06,.09,.92,.90),
    14.0:B(.05,.10,.90,.91),14.5:B(.06,.11,.89,.92),15.0:B(.0,.20,1.0,.98)}
W({"mediaId":4125,"level":"B","keyWord":"stage","defaultVoice":"male",
 "taps":[
  {"phrase":"to tug at a sheet","target":"the man in the suit","voice":"male","keys":K(T,man)},
  {"phrase":"to burst into petals","target":"the flower elephant","voice":"male","keys":K(T,fl)},
  {"phrase":"to raise its trunk","target":"the grey elephant","voice":"male","keys":K(T,el)}],
 "stillS":8.0,
 "nouns":[{"word":"a spotlight","x":.50,"y":.10,"voice":"male"},{"word":"an elephant","x":.55,"y":.45,"voice":"male"},
          {"word":"a suit","x":.19,"y":.75,"voice":"male"},{"word":"a stage","x":.78,"y":.90,"voice":"male"}],
 "question":"What is the grey elephant doing?",
 "answer":["It","is","raising","its","trunk","on","the","stage."],
 "answerVoice":"male",
 "notes":"Two elephants in sequence, never together: the flower sculpture (6.0-10.5 s, box kept through the burst at 10.0/10.5, off while only falling petals are seen) and the real grey elephant (from 12.0 s, faint behind petals at 12.0). Flower elephant is off while it is under the silk sheet. Man: only his legs show under the sheet at 0.5/1.5; off 2.0-3.5 and 6.5 (out of frame / a sliver). Where the man stands in front of the flower elephant's ear (7.0-9.5) the elephant box is cut at the man's box. 'a stage' pill sits on the sandy stage floor; 'an elephant' labels the flower elephant at the still."})

# ---------- 347
T=[i*0.5 for i in range(19)]
sp={0.0:(.54,.28,.17),0.5:(.54,.29,.17),1.0:(.56,.30,.17),1.5:(.56,.30,.10),2.0:(.52,.28,.14),2.5:(.53,.29,.14),
    3.0:(.58,.40,.17),3.5:(.58,.40,.15),4.0:(.52,.29,.15),4.5:(.50,.35,.19),6.5:(.48,.26,.08),7.0:(.49,.40,.12),
    7.5:(.49,.38,.11),8.0:(.49,.28,.09),8.5:(.50,.31,.12),9.0:(.52,.42,.21)}
wom={t:B(.0,v[1],v[0],1.0) for t,v in sp.items()}
man={t:B(v[0],v[2],1.0,1.0) for t,v in sp.items()}
wom[5.0]=B(.0,.46,.45,1.0); man[5.0]=B(.48,.22,1.0,1.0)
wom[5.5]=B(.0,.37,.32,1.0); man[5.5]=B(.62,.19,1.0,1.0)
wom[6.0]=B(.0,.31,.46,1.0); man[6.0]=B(.50,.15,1.0,1.0)
wk=K(T,wom)
W({"mediaId":347,"level":"B","keyWord":"gossip","defaultVoice":"male",
 "taps":[
  {"phrase":"to whisper some gossip","target":"the young woman","voice":"female","keys":wk},
  {"phrase":"to gasp behind his hands","target":"the young man","voice":"male","keys":K(T,man)},
  {"phrase":"to wear round glasses","target":"the young woman","voice":"female","keys":wk}],
 "stillS":0.0,
 "nouns":[{"word":"an awning","x":.35,"y":.10,"voice":"male"},{"word":"curly hair","x":.72,"y":.28,"voice":"male"},
          {"word":"a braid","x":.22,"y":.60,"voice":"male"},{"word":"a table","x":.60,"y":.80,"voice":"male"}],
 "question":"What is the woman with glasses doing?",
 "answer":["She","is","whispering","some","gossip","into","his","ear."],
 "answerVoice":"female",
 "notes":"Only two usable targets: the old couple at the other table is sharp for about one second (5.5 s) only, so the young woman carries two phrases, one of them a state (round glasses). Both friends sip coffee and both glance, so those actions were not used. At 9.0 s both laugh behind a hand: 'to gasp behind his hands' refers to 1.5-3.0 s (both hands, shocked) - verifier please judge. Boxes split along the line between the two heads."})
