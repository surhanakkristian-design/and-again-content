import json
T=[i*0.5 for i in range(17)]
w={0.0:(.25,.44,.62,.35),0.5:(.25,.29,.62,.45),1.0:(.17,.29,.69,.55),1.5:(.17,.31,.69,.55),2.0:(.14,.34,.73,.45),2.5:(.16,.36,.71,.43),3.0:(.11,.37,.74,.53),3.5:(.14,.38,.73,.54),4.0:(.15,.41,.70,.40),4.5:(.17,.43,.70,.40),5.0:(.14,.45,.73,.48),5.5:(.19,.36,.70,.54),6.0:(.18,.38,.73,.43),6.5:(.22,.42,.71,.41),7.0:(.20,.46,.73,.51),7.5:(.17,.37,.76,.62),8.0:(.21,.27,.74,.64)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":4010,"level":"A","keyWord":"climb","defaultVoice":"female",
"taps":[
 {"phrase":"to climb a rock wall","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to reach up high","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to wear a white top","target":"the woman","voice":"female","keys":keys(w)}],
"stillS":2.0,
"nouns":[{"word":"a woman","x":.38,"y":.60,"voice":"female"},{"word":"a rock","x":.72,"y":.20,"voice":"female"},{"word":"trees","x":.18,"y":.85,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","climbing","a","rock","wall."],
"answerVoice":"female",
"notes":"Only one possible target (the woman), so all three phrases use her; the third is a state. 'a rock' labels the cliff face. Only 3 nouns: rope and clips are thin and not A-level words."}
json.dump(c,open("content/4010.json","w"),indent=1)
