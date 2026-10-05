import json
T=[i*0.5 for i in range(19)]
denim={0:(.09,.17,.81,.83),.5:(.07,.17,.86,.83),1:(.17,.16,.73,.84),1.5:(.66,.36,.34,.2),2:(.62,.37,.38,.17),2.5:(.64,.37,.36,.2),
3:(.72,.42,.28,.18),3.5:(.71,.41,.29,.17),4.5:(.82,.56,.18,.16),7:(.7,0,.3,.66),7.5:(.33,0,.62,.45),8:(.37,0,.63,.3),8.5:(.34,.03,.66,.3),9:(.34,.1,.66,.3)}
hood={1.5:(.1,.25,.55,.7),2:(.08,.25,.54,.63),2.5:(.08,.26,.56,.62),3:(.12,.22,.59,.7),3.5:(.14,.11,.56,.8),4:(.11,.11,.63,.78),
7:(0,.05,.33,.52),7.5:(0,.06,.32,.46),8:(.04,.09,.32,.3),8.5:(.03,.12,.3,.17),9:(.08,.17,.24,.14)}
beard={4.5:(0,.14,.82,.84),5:(0,.15,1,.85),5.5:(0,.16,1,.84),6:(0,.17,1,.83),6.5:(0,.17,1,.83)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
d={"mediaId":4313,"level":"B","keyWord":"pub","defaultVoice":"male",
"taps":[{"phrase":"to hold out the microphone","target":"the man in the denim shirt","voice":"male","keys":keys(denim)},
{"phrase":"to point at herself in surprise","target":"the woman in the hoodie","voice":"female","keys":keys(hood)},
{"phrase":"to touch his chest dramatically","target":"the man in the yellow jacket","voice":"male","keys":keys(beard)}],
"stillS":2.0,
"nouns":[{"word":"a microphone","x":.76,"y":.45,"voice":"male"},{"word":"a hoodie","x":.3,"y":.58,"voice":"male"},
{"word":"fairy lights","x":.45,"y":.17,"voice":"male"},{"word":"a beer mug","x":.8,"y":.63,"voice":"male"}],
"question":"What is the elderly woman doing?","answer":["She","is","singing","in","a","crowded","pub."],"answerVoice":"female",
"notes":"Key word 'pub' is the whole place, so it is not a noun pill; it is in the answer. Everybody who gets the microphone sings, so 'to sing' is not a tap phrase. The man in the denim shirt: whole figure at 0-1.0 and 7.0-9.0, only his hand with the microphone at 1.5-4.5 (box = the hand). The woman in the hoodie points at herself at 2.0-2.5; from 7.0 she stands clapping in the crowd on the left (small at 8.5-9.0, partly behind his arm); at 8.0-9.0 his box ends above the elderly woman's hair. The man in the yellow jacket: only 4.5-6.5 boxed (hand on chest 5.5-6.5); his sleeve at the left edge from 7.0 is off. The elderly woman (7.0-9.0) is not a tap target, she is the subject of the question."}
json.dump(d,open("content/4313.json","w"),indent=1)
