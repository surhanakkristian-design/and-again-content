import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(.86,.02,.14,.33),0.5:(.86,.02,.14,.33),1.0:(.80,.02,.20,.42),1.5:(0,.02,1.0,.385),
 2.0:(0,0,1.0,.64),2.5:(0,.05,1.0,.81),3.0:(0,.12,1.0,.75),3.5:(.08,.28,.88,.72),4.0:(.05,.47,.85,.53),
 4.5:(.12,.60,.78,.40),5.0:(.12,.62,.74,.38),5.5:(.12,.60,.76,.40)}
clock={0.0:(.16,.18,.70,.58),0.5:(.16,.17,.68,.57),1.0:(.13,.19,.67,.58),1.5:(.04,.405,.66,.38),
 2.0:(0,.64,.25,.36),2.5:(0,.86,.18,.14),3.0:(0,.87,.18,.13)}
woman={7.5:(.34,.42,.31,.47),8.0:(.27,.38,.38,.54),8.5:(.33,.39,.36,.57),9.0:(.33,.40,.36,.56),9.5:(.33,.40,.36,.56),
 10.0:(.31,.40,.36,.57),10.5:(.29,.40,.37,.56),11.0:(.23,.45,.54,.52),11.5:(.16,.40,.68,.60),12.0:(0,.58,.38,.42)}
c={"mediaId":4548,"level":"A","keyWord":"late","defaultVoice":"female",
 "taps":[
  {"phrase":"to drink from a cup","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to stand next to the bed","target":"the alarm clock","voice":"female","keys":keys(clock)},
  {"phrase":"to look at her watch","target":"the woman","voice":"female","keys":keys(woman)}],
 "stillS":9.0,
 "nouns":[{"word":"a roof","x":.50,"y":.06,"voice":"female"},{"word":"a clock","x":.52,"y":.20,"voice":"female"},
          {"word":"people","x":.82,"y":.52,"voice":"female"},{"word":"a woman","x":.50,"y":.66,"voice":"female"}],
 "question":"What is the woman looking at?",
 "answer":["She","is","looking","at","her","watch."],
 "answerVoice":"female",
 "notes":"Three shots (bedroom, kitchen, arcade) with a man and a woman: no single main person, so defaultVoice by evenId (female). Key word 'late' is an adverb, not shown as a thing and not in the answer (it would be a guessed reason). 0.0-1.0 s: the man is only a blurred head of hair behind the clock (small box at the right edge); 1.5 s: his hand lies on the clock, split at the top of the clock face; 2.5/3.0 s: the alarm clock is only a red sliver in the bottom-left corner. 7.0 s: a different, blurred woman with a bag walks by -> the woman is off. 12.0 s: only her navy back and arm at the bottom left. A wall clock in the kitchen and the big arcade clock also appear, but neither stands next to a bed."}
json.dump(c,open('content/4548.json','w'),indent=1,ensure_ascii=False)
