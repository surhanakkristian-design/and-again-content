import json
T=[i*0.5 for i in range(17)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(.34,.37,.42,.49),0.5:(.35,.33,.41,.53),1.0:(.31,.35,.42,.525),1.5:(.31,.36,.41,.51),
 2.0:(.28,.22,.43,.64),2.5:(.31,.18,.41,.69),3.0:(.18,.22,.52,.59),3.5:(.24,.18,.47,.64),
 4.0:(.09,.27,.90,.44),4.5:(.04,.34,.95,.42),5.0:(.09,.31,.88,.55),5.5:(.09,.27,.83,.53),
 6.0:(.17,.27,.64,.58),6.5:(.24,.32,.51,.54),7.0:(.18,.30,.44,.52),7.5:(.26,.28,.37,.46),8.0:(.21,.31,.42,.45)}
rope={0.0:(.52,.86,.22,.14),0.5:(.52,.86,.22,.14),1.0:(.50,.875,.22,.125),1.5:(.44,.87,.22,.13),
 2.0:(.47,.86,.22,.14),2.5:(.44,.87,.22,.13),3.0:(.40,.81,.22,.19),3.5:(.40,.82,.22,.18),
 4.0:(.33,.71,.32,.29),4.5:(.25,.76,.27,.24),5.0:(.16,.86,.26,.14),5.5:(.12,.80,.22,.20),
 6.0:(.12,.85,.22,.15),6.5:(.14,.86,.22,.14),7.0:(.12,.82,.22,.18),7.5:(.13,.74,.24,.26),8.0:(.12,.76,.24,.24)}
blue={0.0:(.235,.80,.105,.15),0.5:(.225,.82,.125,.15),1.0:(.205,.85,.105,.15),1.5:(.195,.84,.115,.16),
 2.0:(.19,.86,.19,.14),2.5:(.18,.87,.19,.13),3.0:(.145,.86,.19,.14)}
c={"mediaId":4545,"level":"A","keyWord":"strength","defaultVoice":"female",
 "taps":[
  {"phrase":"to climb a high rock","target":"the woman","voice":"female","keys":keys(woman)},
  {"phrase":"to hang down the rock","target":"the rope","voice":"female","keys":keys(rope)},
  {"phrase":"to wear a blue T-shirt","target":"the man in blue","voice":"male","keys":keys(blue)}],
 "stillS":0.0,
 "nouns":[{"word":"the sky","x":.20,"y":.15,"voice":"female"},{"word":"a rock","x":.72,"y":.25,"voice":"female"},
          {"word":"a woman","x":.46,"y":.60,"voice":"female"},{"word":"men","x":.22,"y":.90,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","climbing","a","high","rock."],
 "answerVoice":"female",
 "notes":"Key word 'strength' is abstract: not a noun slot and not in the answer. The rope hangs from her harness, so its box is only the free part below her feet (split under her shoes; at 5.5 s her lower legs are cut off at y .80 to leave room for the rope). The two men are tiny and only visible 0.0-3.0 s; the man in blue has no action of his own, so a state phrase; his box is kept narrow (0.0-1.5 s) between the man in black and the woman's box. Smaller rocks also lie on the left; the 'a rock' pill sits on the big one."}
json.dump(c,open('content/4545.json','w'),indent=1,ensure_ascii=False)
