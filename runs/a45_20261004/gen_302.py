import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
dog={1.0:(.68,.54,.32,.36),1.5:(.64,.41,.36,.32),2.0:(.53,.30,.36,.21),3.0:(.46,.15,.28,.20),3.5:(.51,.19,.42,.20),
4.0:(.51,.18,.42,.19),4.5:(.54,.18,.42,.20),5.0:(.51,.20,.35,.19),5.5:(.51,.21,.41,.19),6.0:(.48,.22,.42,.18),
6.5:(.48,.25,.34,.14),7.0:(.48,.27,.34,.15),7.5:(.26,.63,.36,.29),8.0:(.24,.68,.36,.28),8.5:(.26,.68,.34,.26),
9.0:(.34,.68,.34,.26),9.5:(.42,.61,.38,.27),10.0:(.50,.50,.24,.17)}
man={7.5:(.20,0,.80,.62),8.0:(.33,0,.67,.67),8.5:(.38,0,.62,.67),9.0:(.57,0,.43,.67),9.5:(.21,0,.79,.60),10.0:(.50,.10,.50,.39)}
woman={9.0:(0,.18,.33,.77),9.5:(0,.02,.20,.93),10.0:(0,.05,.42,.80)}
c={"mediaId":302,"level":"A","keyWord":"flour","defaultVoice":"male",
"taps":[
{"phrase":"to lie on the floor","target":"the dog","voice":"male","keys":keys(dog)},
{"phrase":"to touch her nose","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to wear a grey scarf","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":4.0,
"nouns":[{"word":"flour","x":.55,"y":.78,"voice":"male"},{"word":"eggs","x":.27,"y":.24,"voice":"male"},{"word":"a dog","x":.71,"y":.27,"voice":"male"}],
"question":"What is on the man's face?",
"answer":["There","is","flour","on","his","face."],
"answerVoice":"male",
"notes":"Many cuts. The hands in the shots 0-7 s cannot be tied to the man or the woman from the picture (four hands at 3.0 s), so both people are OFF there; the man is boxed 7.5-10 s, the woman only 9.0-10 s (at 9.0 s only her arm and a sliver of face at the left edge; her scarf is seen at 9.5 and 10.0 s). 'to wear a grey scarf' is a state: no action fits only the woman. 'to touch her nose' happens at 9.5 s (the hand on the man's own nose at 7.5 s looks like the woman's). Man boxes are cut to the head/upper body where the dog lies under or between his arms (7.5-10 s). Dog is faint behind the flour cloud at 2.0 s and behind the arm at 6.5 s."}
json.dump(c,open("content/302.json","w"),indent=1,ensure_ascii=False)
