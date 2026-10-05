import json
O=None
def mk(K,i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
# man, bottle
K={0.0:((.02,.05,.74,.95),O),0.5:((.22,.02,.78,.98),O),
1.0:((.10,.18,.71,.82),(.82,.62,.18,.30)),1.5:((.08,.02,.75,.98),(.84,.46,.16,.27)),
2.0:((0,0,1,1),O),2.5:((0,0,1,1),O),
3.0:((.03,0,.83,1),(.87,.65,.13,.22)),3.5:((.03,.08,.84,.92),(.88,.65,.12,.23)),
4.0:((0,.06,.86,.94),(.87,.54,.13,.23)),4.5:((.06,.04,.86,.96),(.93,.54,.07,.23)),
5.0:((.05,.08,.84,.92),(.90,.58,.10,.30))}
d={"mediaId":760,"level":"B","keyWord":"swell","defaultVoice":"male",
"taps":[{"phrase":"to pull off a sock","target":"the man","voice":"male","keys":mk(K,0)},
{"phrase":"to poke a swollen ankle","target":"the man","voice":"male","keys":mk(K,0)},
{"phrase":"to contain drinking water","target":"the bottle","voice":"male","keys":mk(K,1)}],
"stillS":3.0,
"nouns":[{"word":"an ankle","x":.34,"y":.82,"voice":"male"},{"word":"an ice pack","x":.80,"y":.86,"voice":"male"},
{"word":"a tank top","x":.50,"y":.46,"voice":"male"},{"word":"trees","x":.75,"y":.13,"voice":"male"}],
"question":"What is happening to his ankle?",
"answer":["His","ankle","is","swelling","up."],
"answerVoice":"male",
"notes":"Only real targets: the man, the water bottle, the ice pack. Ice pack not used as tap target (in his hands / on his ankle at 4.5-5.0 s, under the bottle before). The bottle stands at the right edge next to the man's elbow/hand, so its box is narrower than 0.18 (0.07 wide at 4.5 s where his hand with the ice pack is right beside it). 2.0-2.5 s close-up of his legs and feet: whole picture = the man. Bottle phrase is a state (nothing else acts). 'an ankle' = the cartoon balloon lump above the foot. Trees are blurred background."}
json.dump(d,open("content/760.json","w"),indent=1,ensure_ascii=False)
