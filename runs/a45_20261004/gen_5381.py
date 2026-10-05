import json
T=[i*0.5 for i in range(21)]
HM={0.0:(.04,.21,.72,.79),0.5:(.14,.13,.80,.87),1.0:(.17,.14,.83,.86),1.5:(.14,.10,.82,.90),2.0:(0,.13,.80,.87)}
CW={2.5:(0,.21,.52,.52),3.0:(0,.15,.50,.62),3.5:(0,.20,.52,.56),4.0:(0,.20,.50,.52)}
OW={4.5:(.16,.31,.37,.50),5.0:(.13,.34,.38,.48),5.5:(.09,.34,.38,.48),6.0:(.13,.32,.37,.48),6.5:(.26,.31,.40,.50),7.0:(.74,.31,.26,.30)}
def keys(B):
    return [{"t":t,"off":True} if t not in B else {"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} for t in T]
c={"mediaId":5381,"level":"A","keyWord":"conversation","defaultVoice":"male",
"taps":[{"phrase":"to talk on the phone","target":"the man in the hoodie","voice":"male","keys":keys(HM)},
{"phrase":"to laugh out loud","target":"the woman with curly hair","voice":"female","keys":keys(CW)},
{"phrase":"to have grey hair","target":"the old woman","voice":"female","keys":keys(OW)}],
"stillS":5.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"male"},{"word":"trees","x":0.82,"y":0.27,"voice":"male"},
{"word":"a fence","x":0.60,"y":0.60,"voice":"male"},{"word":"flowers","x":0.20,"y":0.82,"voice":"male"}],
"question":"What are the two women doing?",
"answer":["They","are","talking","in","a","cafe."],"answerVoice":"female",
"notes":"Four scenes: man in hoodie on the phone 0-2 s, two women in a cafe 2.5-4 s, old woman and man at the fence 4.5-7 s (she is at the right edge at 7.0 s), family dinner 7.5-10 s. 'to laugh out loud' is unique within the cafe shot (her friend looks surprised), but the family at dinner also laughs later - verifier please check. 'to have grey hair' is a state: in the fence shot both people talk, lean and gesture, so no action fits only her; she is the only grey-haired person in the clip. defaultVoice male: mixed group, evenId false. answerVoice female: subject = the two women."}
json.dump(c,open('content/5381.json','w'),indent=1)
