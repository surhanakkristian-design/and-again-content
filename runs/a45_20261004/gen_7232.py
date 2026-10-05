import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(bs): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,bs)]
grey=K([(.21,.31,.61,.82),(.31,.31,.72,.88),(.16,.29,.76,.92),(.12,.28,.66,1.0),(.15,.27,.71,1.0),(.07,.23,.86,1.0),(0,.21,.77,1.0),(0,.19,.81,1.0)])
unif=K([(.62,.36,.80,.66),None,None,(.67,.38,.85,.85),(.72,.38,.90,.75),None,(.78,.38,.97,.82),(.82,.38,1.0,.82)])
F="female"
d=dict(mediaId=7232,level="B",keyWord="hostage",defaultVoice=F,
 taps=[dict(phrase="to sob on his shoulder",target="the woman in grey",voice=F,keys=grey),
       dict(phrase="to walk away from the jet",target="the woman in grey",voice=F,keys=grey),
       dict(phrase="to wipe away her tears",target="the woman in uniform",voice=F,keys=unif)],
 stillS=0.2,
 nouns=[dict(word="a floodlight",x=.22,y=.15,voice=F),dict(word="a private jet",x=.72,y=.28,voice=F),
        dict(word="a blanket",x=.32,y=.55,voice=F),dict(word="a bouquet",x=.68,y=.88,voice=F)],
 question="What is the woman in grey doing?",
 answer=["She","is","sobbing","on","a","man's","shoulder."],answerVoice=F,
 notes="Key word 'hostage' is not a visible noun. The hugging man is not a target; the box of the woman in grey includes him where they embrace. The woman in uniform is hidden behind the couple at 0.7, 1.2 and 2.7 s (off) and blurred at 3.2-3.7 s; her boxes are split from the couple's box. 'to walk away from the jet' only fits the first second, before the hug.")
json.dump(d,open("content/7232.json","w"),indent=1)
