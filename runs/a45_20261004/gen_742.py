import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, **dict(zip("xywh", d[t]))) if t in d else dict(t=t, off=True) for t in T]
wom={0:(.72,0,.28,.80),.5:(.78,.46,.22,.42),1:(.69,.34,.31,.22),1.5:(.54,.18,.46,.50),2:(.68,.10,.32,.62),2.5:(.58,.21,.42,.45),
3:(.52,0,.48,.78),3.5:(.46,0,.54,.68),4:(.12,0,.88,.66),4.5:(0,.02,.79,.56),5:(0,.02,.66,.72),5.5:(.02,.07,.49,.66),
6:(0,.11,.44,.52),6.5:(0,.12,.43,.62),7:(0,.13,.47,.60),7.5:(0,.12,.47,.63),8:(0,.14,.46,.56),8.5:(0,.14,.46,.54),
9:(0,.16,.46,.60),9.5:(0,.14,.45,.60),10:(0,0,.45,.64)}
man={4.5:(.80,0,.20,.76),5:(.67,0,.33,.74),5.5:(.63,0,.37,.86),6:(.61,.04,.39,.72),6.5:(.59,.07,.41,.70),7:(.65,.07,.35,.70),
7.5:(.61,.07,.39,.72),8:(.60,.07,.40,.68),8.5:(.60,.07,.40,.66),9:(.60,.07,.40,.72),9.5:(.60,.07,.40,.70),10:(.60,0,.40,.72)}
cat={5.5:(.52,.37,.10,.24),6:(.45,.34,.15,.20),6.5:(.44,.33,.14,.22),7:(.48,.31,.16,.21),7.5:(.48,.32,.12,.22),8:(.47,.32,.12,.20),
8.5:(.47,.32,.12,.20),9:(.47,.35,.12,.20),9.5:(.46,.35,.13,.20),10:(.46,.34,.13,.20)}
c={"mediaId":742,"level":"A","keyWord":"stove","defaultVoice":"female",
"taps":[
{"phrase":"to hold a wooden spoon","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to hold a kettle","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to sit under the window","target":"the cat","voice":"female","keys":keys(cat)}],
"stillS":8.5,
"nouns":[{"word":"a stove","x":.45,"y":.87,"voice":"female"},{"word":"a kettle","x":.78,"y":.73,"voice":"female"},
{"word":"a cat","x":.53,"y":.42,"voice":"female"},{"word":"a window","x":.52,"y":.20,"voice":"female"}],
"question":"What are they doing?",
"answer":["They","are","cooking","on","the","stove."],
"answerVoice":"female",
"notes":"0.0-3.0: only a hand/arm at the knobs; the rolled terracotta sleeve and the face at 0.0 are the woman's (the packet description says the man), so these frames are boxed as the woman - please check. The woman holds the spoon from 6.5 s; the man holds the kettle only at 5.5-6.5 s (carries it in, sets it down). The cat sits between the two people, so its box is narrower than 0.18 (0.10-0.16 wide) to avoid overlap. 4.5 s: the man's arm reaches across under the woman; boxes split at x 0.79. 10.0 s: man's raised elbow crosses x 0.60 slightly."}
json.dump(c,open("content/742.json","w"),indent=1)
