import json
T=[i*0.5 for i in range(30)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
man={0.0:(.22,.44,.32,.32),0.5:(.22,.45,.33,.32),1.0:(.24,.44,.31,.32),1.5:(.22,.45,.33,.32),2.0:(.18,.44,.36,.34),2.5:(.16,.44,.39,.36),3.0:(.18,.45,.36,.33),
3.5:(.05,.38,.54,.38),4.0:(0,.33,.44,.46),4.5:(0,.34,.40,.43),5.0:(0,.36,.34,.38),5.5:(0,.36,.34,.38),6.0:(0,.36,.33,.38),6.5:(0,.36,.33,.38),
7.0:(0,.35,.34,.39),7.5:(0,.35,.34,.39),8.0:(0,.35,.33,.39),8.5:(.07,.39,.38,.32),9.0:(.08,.42,.37,.16),9.5:(.23,.47,.20,.15),
10.0:(.22,.51,.20,.14),10.5:(.24,.54,.19,.14),11.0:(.26,.55,.18,.14),11.5:(.28,.56,.18,.14)}
wom={0.0:(.54,.37,.34,.38),0.5:(.55,.38,.35,.40),1.0:(.55,.40,.33,.36),1.5:(.55,.40,.35,.38),2.0:(.54,.37,.34,.39),2.5:(.55,.36,.35,.43),3.0:(.54,.39,.34,.38),
3.5:(.60,.39,.40,.37),4.0:(.52,.34,.48,.50),4.5:(.55,.34,.45,.45),5.0:(.56,.36,.44,.42),5.5:(.56,.36,.44,.42),6.0:(.54,.35,.42,.46),6.5:(.54,.35,.42,.46),
7.0:(.49,.33,.47,.46),7.5:(.49,.33,.47,.46),8.0:(.48,.35,.38,.43),8.5:(.47,.42,.33,.31),9.0:(.46,.45,.20,.14),9.5:(.44,.48,.18,.15),
10.0:(.42,.52,.18,.14),10.5:(.43,.54,.18,.14),11.0:(.44,.55,.18,.14),11.5:(.46,.56,.18,.14)}
hel={10.5:(0,.05,.18,.36),11.0:(0,0,.52,.47),11.5:(.21,.06,.30,.28),12.0:(.29,.12,.23,.20),12.5:(.34,.15,.20,.16),13.0:(.36,.16,.18,.15),13.5:(.38,.16,.18,.15),14.0:(.39,.17,.18,.14),14.5:(.39,.17,.18,.14)}
d={"mediaId":4076,"level":"A","keyWord":"door","defaultVoice":"female",
"taps":[{"phrase":"to wear black shorts","target":"the man","voice":"male","keys":mk(man)},
{"phrase":"to wear white trousers","target":"the woman","voice":"female","keys":mk(wom)},
{"phrase":"to fly up into the sky","target":"the helicopter","voice":"female","keys":mk(hel)}],
"stillS":6.0,
"nouns":[{"word":"the sky","x":.45,"y":.18,"voice":"female"},{"word":"a man","x":.15,"y":.47,"voice":"male"},{"word":"a woman","x":.80,"y":.46,"voice":"female"},{"word":"a town","x":.45,"y":.62,"voice":"female"}],
"question":"What are the man and woman doing?","answer":["They","are","jumping","out","of","a","helicopter."],"answerVoice":"female",
"notes":"The man and the woman do the same things (sit, stand on the bar, jump), so their two phrases are states (clothes): only he wears shorts, only she wears white trousers; a third skydiver in long black trousers shows at the right edge from about 4.5 s and is not a target (the woman's box partly covers that person at 4.5-7.5 s). 0-3 s both are seen from behind inside the cabin (man left, woman right with the blond bun); clothes are not visible there yet. After the jump (9.5-11.5 s) the three are tiny dots; man = left dot, woman = middle dot, boxes off from 12 s. Helicopter is boxed only from 10.5 s when it is seen from outside; off while the camera is inside or only a rotor blade shows. Key word 'door': the open doorway shows only 0-3 s as the opening itself with no clear place for a pill, so it is not a noun and not in the answer; the answer says 'a helicopter', which is seen only after the jump. Packet description says barefoot and camera under the helicopter; frames show shoes and a camera on a skydiver's helmet."}
json.dump(d,open("content/4076.json","w"),indent=1)
