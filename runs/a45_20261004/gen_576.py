import json
exec(open("gen_575.py").read().split("# ---------- 575")[0])
t=T(11)
w={0.0:(.30,.17,.56,.48),0.5:(.28,.18,.58,.47),1.0:(.31,.18,.56,.48),1.5:(0,0,1,1),2.0:(0,0,1,1),2.5:(0,0,1,1),
 3.0:(0,.25,1,.75),3.5:(0,.35,1,.65),4.5:(0,.05,1,.95),5.0:(0,.07,1,.93)}
k=K(t,w)
j={"mediaId":576,"level":"A","keyWord":"pray","defaultVoice":"female",
 "taps":[{"phrase":"to pray at her desk","target":"the woman","voice":"female","keys":k},
  {"phrase":"to press her hands together","target":"the woman","voice":"female","keys":k},
  {"phrase":"to look up and cry","target":"the woman","voice":"female","keys":k}],
 "stillS":0.0,
 "nouns":[{"word":"a woman","x":.52,"y":.40,"voice":"female"},{"word":"a laptop","x":.20,"y":.62,"voice":"female"},
  {"word":"books","x":.65,"y":.83,"voice":"female"},{"word":"a lamp","x":.82,"y":.27,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","praying","at","her","desk."],
 "answerVoice":"female",
 "notes":"Only one possible target, used for all three phrases. 1.5-2.5 s are close-ups (hands / face) that fill the frame: full-frame box. 4.0 s is a blurred pan over the desk without her: off. 'to look up and cry': she looks up at 3.0-3.5 s, a tear is visible at 2.5 s. 'books': a second smaller pile lies behind at the right edge; the pill sits on the big pile in front."}
json.dump(j,open("content/576.json","w"),indent=1)
