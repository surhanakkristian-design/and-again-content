import json
def K(times, d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
def B(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:B(.24,.37,.47,.68),0.7:B(.24,.37,.47,.68),1.2:B(.24,.37,.47,.68),1.7:B(.24,.36,.48,.68),
     2.2:B(.20,.35,.48,.67),2.7:B(.20,.35,.50,.67),3.2:B(.18,.35,.50,.68),3.7:B(.17,.35,.51,.68)}
mid={0.2:B(.47,.38,.66,.60),0.7:B(.47,.38,.67,.60),1.2:B(.47,.38,.67,.60),1.7:B(.48,.37,.75,.62),
     2.2:B(.48,.37,.75,.62),2.7:B(.50,.36,.80,.62),3.2:B(.50,.37,.82,.62),3.7:B(.51,.37,.84,.62)}
fg={0.2:B(.73,.44,1.0,1.0),0.7:B(.72,.43,1.0,1.0),1.2:B(.73,.45,1.0,1.0),1.7:B(.77,.45,1.0,1.0),
    2.2:B(.69,.68,1.0,1.0),2.7:B(.69,.68,1.0,1.0),3.2:B(.70,.67,1.0,1.0),3.7:B(.70,.67,1.0,1.0)}
c={"mediaId":7045,"level":"B","keyWord":"diplomat","defaultVoice":"female",
 "taps":[
  {"phrase":"to hand over a document","target":"the woman in grey","voice":"female","keys":K(T,wom)},
  {"phrase":"to hold a paper cup","target":"the man next to her","voice":"male","keys":K(T,mid)},
  {"phrase":"to pick up the document","target":"the man in the foreground","voice":"male","keys":K(T,fg)}],
 "stillS":0.2,
 "nouns":[{"word":"a wall lamp","x":.62,"y":.32,"voice":"female"},{"word":"a diplomat","x":.38,"y":.53,"voice":"female"},
          {"word":"paper cups","x":.40,"y":.74,"voice":"female"},{"word":"a stack of papers","x":.42,"y":.87,"voice":"female"}],
 "question":"What is the woman in grey doing?",
 "answer":["She","is","handing","over","a","handwritten","document."],
 "answerVoice":"female",
 "notes":"Woman / man-next-to-her boxes split at x ~0.47-0.50 (her right shoulder and his left arm touch), so her reaching hand at 0.2-1.7 is partly cut. The man next to her holds the paper cup from about 1.2 s (before that he gestures with an empty hand). Foreground man: only his back/head and hands are visible; from 2.2 s only his arm and hands holding the page. 'a diplomat' pill sits on the woman in grey (she is the key-word person). 'paper cups' = the standing and the knocked-over cup together."}
json.dump(c,open("content/7045.json","w"),indent=1,ensure_ascii=False)
