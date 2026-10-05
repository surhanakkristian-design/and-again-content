import json
OFF=None
# t: (woman, man, bird)
K={
0.0:((0,0,.70,.55),OFF,OFF),
0.5:((0,0,1,.62),OFF,OFF),
1.0:((0,0,1,.73),(.82,.74,.18,.26),OFF),
1.5:((0,0,1,.71),(.78,.72,.22,.28),OFF),
2.0:((0,0,.69,.82),(.70,.62,.30,.36),OFF),
2.5:((0,0,.50,.83),(.62,.38,.38,.40),OFF),
3.0:((0,0,.36,.85),(.65,.33,.35,.50),OFF),
3.5:((0,0,.40,.72),(.41,.08,.59,.48),OFF),
4.0:((0,0,.48,.60),(.50,.18,.50,.28),OFF),
4.5:((0,0,.55,.60),(.56,.27,.44,.24),OFF),
5.0:((0,0,.49,.62),(.50,.30,.50,.24),OFF),
5.5:((0,0,.56,.62),(.57,.30,.43,.24),OFF),
6.0:((0,0,.54,.60),(.55,.28,.45,.26),OFF),
6.5:((0,0,.55,.60),(.62,.28,.38,.28),OFF),
7.0:((0,0,.64,.62),(.66,.29,.34,.30),OFF),
7.5:((0,0,.39,.78),(.40,.05,.60,.19),OFF),
8.0:((0,0,.41,.80),(.42,0,.58,.22),OFF),
8.5:((0,0,.49,.82),(.50,0,.50,.24),OFF),
9.0:((0,.08,.40,.92),(.41,.04,.35,.32),(.77,.03,.23,.16)),
9.5:((0,.14,.42,.86),(.43,.08,.33,.30),(.77,.08,.23,.15)),
10.0:((0,.16,.49,.84),(.50,.10,.30,.32),(.81,.10,.19,.15)),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":750,"level":"A","keyWord":"string","defaultVoice":"female",
"taps":[
 {"phrase":"to tie the string","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to lift the box","target":"the man","voice":"male","keys":keys(1)},
 {"phrase":"to sit by the window","target":"the bird","voice":"female","keys":keys(2)}],
"stillS":10.0,
"nouns":[{"word":"a bird","x":.88,"y":.21,"voice":"female"},
 {"word":"string","x":.58,"y":.31,"voice":"female"},
 {"word":"a woman","x":.25,"y":.41,"voice":"female"},
 {"word":"a box","x":.58,"y":.56,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","tying","a","box","with","string."],
"answerVoice":"female",
"notes":"'the man' = the customer; only his hands and arm are in the picture (chin at the top right at 2.0 s, not boxed), boxes are on his hands / arm. He lifts the box by the string at 7.5-8.5 s; from 8.5 s the woman also holds the box from below. The bird is in the window only at 9.0-10.0 s; the man's arm passes under it, so his box covers the fist and the near part of the arm only. Hands of the two meet on the box at 4.0-7.0 s: boxes split on a vertical line. 'string' as a mass noun (label and answer)."}
json.dump(d,open("content/750.json","w"),indent=1,ensure_ascii=False)
