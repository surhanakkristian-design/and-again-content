import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(0,.30,1,.70),0.5:(0,.32,1,.68),1.0:(0,.34,1,.66),1.5:(0,.35,1,.65),2.0:(.36,0,.64,1),2.5:(.50,0,.50,1),
3.0:(.72,.55,.28,.25),3.5:(.58,.44,.42,.28),4.0:(.50,.27,.50,.28),4.5:(.24,.26,.76,.74),5.0:(0,.34,1,.66),5.5:(0,.35,1,.65),
6.0:(0,.35,1,.65),6.5:(0,.37,1,.63),7.0:(0,.37,1,.63),7.5:(.38,0,.62,1),8.0:(.30,0,.70,1),8.5:(.30,0,.70,1),
9.0:(.42,0,.58,1),9.5:(.45,0,.55,1),10.0:(.52,0,.48,1)}
D={0.0:(.10,.14,.22,.15),0.5:(.09,.15,.22,.16),1.0:(.09,.18,.22,.15),1.5:(.15,.18,.22,.16),2.0:(.12,.18,.22,.16),2.5:(.17,.17,.22,.17),
3.0:(.20,.13,.22,.16),3.5:(.17,.01,.22,.15),4.5:(.02,.06,.22,.17),5.0:(0,.15,.20,.18),5.5:(0,.18,.18,.16),6.0:(0,.19,.18,.15),
6.5:(0,.20,.18,.16),7.0:(0,.20,.18,.16),7.5:(.02,.21,.22,.16),8.0:(.01,.22,.22,.15),9.0:(.20,.22,.20,.16),9.5:(.26,.24,.18,.16),10.0:(.31,.26,.20,.14)}
c={"mediaId":549,"level":"B","keyWord":"piercing","defaultVoice":"female",
"taps":[
 {"phrase":"to insert a gold hoop","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to lounge on the bed","target":"the dog","voice":"female","keys":keys(D)},
 {"phrase":"to point at her earlobe","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":8.0,
"nouns":[{"word":"a piercing","x":.72,"y":.42,"voice":"female"},{"word":"curls","x":.62,"y":.12,"voice":"female"},{"word":"a light bulb","x":.40,"y":.52,"voice":"female"},{"word":"a jewelry tray","x":.30,"y":.76,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","putting","a","hoop","in","her","ear","piercing."],
"answerVoice":"female",
"notes":"Extreme close-up at a mirror. The woman's box follows the REAL woman (ear, head, hands); her mirror reflection (left, e.g. 3.0-3.5 s and 9.0-10.0 s) is outside the box because the dog sits right next to it in the mirror. Where her hand and head fill the frame and the dog is top left, the woman's box is the lower band (ear + hands) so it does not cover the dog. At 3.0-4.0 s the real woman is only her hand over the tray. The dog is small and blurred, seen in the mirror on the bed (off at 4.0 and 8.5 s). Pointing at the earlobe 0-1.5 s, inserting the hoop 5.0-6.5 s. Spelling 'jewelry' follows the packet (US)."}
json.dump(c,open('content/549.json','w'),indent=1)
