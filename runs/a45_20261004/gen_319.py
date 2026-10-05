import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
F={0.0:(.12,.38,.56,.31),0.5:(.13,.39,.56,.31),1.0:(.13,.39,.55,.32),1.5:(.14,.40,.55,.32),2.0:(.12,.39,.55,.30),
2.5:(.11,.38,.54,.30),3.0:(.09,.39,.59,.30),3.5:(.08,.39,.60,.30),4.0:(.06,.39,.60,.30),4.5:(.06,.39,.60,.30),
5.0:(.05,.39,.60,.30),5.5:(.04,.40,.57,.29),6.0:(.03,.40,.56,.30),6.5:(.01,.40,.56,.30),7.0:(0,.32,.60,.46),
7.5:(.38,.07,.62,.53),8.0:(.34,.33,.58,.24),8.5:(.50,.44,.34,.19),9.0:(.40,.44,.34,.19),9.5:(.36,.44,.36,.19),10.0:(.33,.44,.34,.18)}
S={1.5:(.60,.76,.40,.24),2.0:(.68,.70,.32,.25),2.5:(.66,.69,.34,.31),3.0:(.62,.76,.38,.24),3.5:(.62,.76,.38,.24),
4.0:(.67,.70,.33,.26),4.5:(.64,.70,.36,.24),5.0:(.62,.80,.38,.20),5.5:(.60,.82,.40,.18),6.0:(.60,.71,.40,.29),
6.5:(.60,.71,.40,.29),7.0:(.48,.82,.52,.18),7.5:(.38,.80,.62,.20),8.0:(.15,.70,.85,.30),8.5:(0,.70,1.0,.30),
9.0:(0,.76,1.0,.24),9.5:(0,.78,1.0,.22),10.0:(0,.80,1.0,.20)}
c={"mediaId":319,"level":"A","keyWord":"frog","defaultVoice":"male",
"taps":[
{"phrase":"to sit on a stone","target":"the frog","voice":"male","keys":keys(F)},
{"phrase":"to jump onto a leaf","target":"the frog","voice":"male","keys":keys(F)},
{"phrase":"to swim in the water","target":"the fish","voice":"male","keys":keys(S)}],
"stillS":4.5,
"nouns":[{"word":"a frog","x":.30,"y":.50,"voice":"male"},{"word":"a stone","x":.28,"y":.78,"voice":"male"},
{"word":"a fish","x":.78,"y":.77,"voice":"male"}],
"question":"What is the frog doing?",
"answer":["It","is","sitting","on","a","stone."],
"answerVoice":"male",
"notes":"Only two kinds of target: the frog (two phrases) and the fish. 'the fish' = the group of orange/white koi under the water; one box around all fish visible at each time, kept clear of the frog box. Fish OFF at 0-1.0 s (only a pale blur). At 4.5 s one orange fish is clear; a second pale fish is faint at the bottom right edge. The small blue dragonfly (0-4.0 s) is not used. The frog jumps at 7.0-8.0 s and lands on a lily pad ('a leaf' for level A)."}
json.dump(c,open("content/319.json","w"),indent=1,ensure_ascii=False)
