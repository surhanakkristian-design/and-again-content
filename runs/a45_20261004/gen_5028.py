import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
man={0.0:(0,.19,.66,.81),0.5:(0,.16,.78,.84),1.0:(0,.35,.44,.40),1.5:(0,.13,.76,.87),2.0:(0,.62,.18,.32),
 2.5:(0,.13,.62,.87),3.0:(0,.07,.57,.93),3.5:(0,.10,.53,.90),4.0:(0,.14,.58,.86),4.5:(0,.25,.26,.66),
 9.0:(.74,.19,.26,.38),9.5:(.74,.19,.26,.38),10.0:(.75,.19,.25,.38),10.5:(.81,.19,.19,.38),
 11.0:(.67,.21,.33,.37),11.5:(.64,.21,.36,.37),12.0:(.63,.23,.37,.35)}
judge={9.0:(0,.29,.66,.71),9.5:(0,.29,.68,.71),10.0:(0,.29,.72,.71),10.5:(0,.32,.80,.68),
 11.0:(0,.33,.66,.67),11.5:(0,.33,.63,.67),12.0:(0,.33,.62,.67)}
book={5.0:(0,.31,1,.56),5.5:(0,.33,1,.54),6.0:(0,.37,1,.48),6.5:(0,.37,1,.48),7.0:(0,.37,1,.49),
 7.5:(0,.37,1,.49),8.0:(0,.37,1,.49),8.5:(0,.38,1,.48)}
c={"mediaId":5028,"level":"A","keyWord":"difficult","defaultVoice":"male",
"taps":[
 {"phrase":"to carry heavy books","target":"the young man","voice":"male","keys":K(man)},
 {"phrase":"to hold a wooden hammer","target":"the judge","voice":"female","keys":K(judge)},
 {"phrase":"to lie open on the pile","target":"the open book","voice":"male","keys":K(book)}],
"stillS":12.0,
"nouns":[{"word":"books","x":.47,"y":.30,"voice":"male"},{"word":"glasses","x":.86,"y":.33,"voice":"male"},
 {"word":"a judge","x":.12,"y":.72,"voice":"female"},{"word":"a hammer","x":.76,"y":.76,"voice":"male"}],
"question":"What is the young man carrying?",
"answer":["He","is","carrying","heavy","books."],"answerVoice":"male",
"notes":"Gavel called 'a wooden hammer' / 'a hammer' to keep A level. Close-up 5.0-8.5 shows a hand on the open book whose owner is unclear, so the young man is OFF there. At 1.0/2.0/4.5 only his hands/arm (with books) show at the left edge. Judge is a woman (voice female); judge box excludes the gavel tip where it would overlap the man's box."}
json.dump(c,open('content/5028.json','w'),indent=1)
