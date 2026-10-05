import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
T=[i*0.5 for i in range(25)]
young={0.0:(0.36,0.02,0.52,0.98),0.5:(0.22,0.15,0.78,0.85),1.0:(0.0,0.26,0.94,0.50),1.5:(0.03,0.35,0.97,0.42),2.0:(0.07,0.33,0.93,0.46),2.5:(0.0,0.33,1.0,0.47),3.0:(0.0,0.33,1.0,0.47),3.5:(0.0,0.33,1.0,0.52)}
woman={4.0:(0.27,0.33,0.46,0.32),4.5:(0.24,0.24,0.50,0.42),5.0:(0.26,0.22,0.50,0.43),5.5:(0.26,0.22,0.50,0.43),6.0:(0.22,0.24,0.68,0.42),6.5:(0.22,0.24,0.52,0.46),7.0:(0.26,0.24,0.58,0.42),7.5:(0.24,0.24,0.76,0.44)}
robe={8.0:(0.08,0.31,0.82,0.60),8.5:(0.06,0.31,0.88,0.36),9.0:(0.02,0.33,0.96,0.42),9.5:(0.02,0.33,0.96,0.46),10.0:(0.0,0.32,1.0,0.56),10.5:(0.0,0.32,1.0,0.58),11.0:(0.0,0.33,1.0,0.60),11.5:(0.0,0.34,1.0,0.64),12.0:(0.0,0.34,1.0,0.66)}
keys=lambda d:[k(t,d.get(t)) for t in T]
c={"mediaId":4385,"level":"A","keyWord":"cost","defaultVoice":"male",
"taps":[
{"phrase":"to lie on his side","target":"the young man","voice":"male","keys":keys(young)},
{"phrase":"to sit in bed","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to lie on a big bed","target":"the man in the red robe","voice":"male","keys":keys(robe)}],
"stillS":5.0,
"nouns":[{"word":"a woman","x":0.56,"y":0.52,"voice":"female"},{"word":"a pillow","x":0.13,"y":0.47,"voice":"male"},{"word":"a window","x":0.90,"y":0.34,"voice":"male"},{"word":"a blanket","x":0.52,"y":0.85,"voice":"male"}],
"question":"How much does the big bed cost?",
"answer":["The","big","bed","costs","twenty","thousand","euros."],
"answerVoice":"male",
"notes":"Three shots, one person each (young man 0-3.5, woman 4.0-7.5, man in robe 8.0-12.0). Question uses the key word and is answered from the caption '€20,000' burnt into the picture over the four-poster bed (number written as words in the chips). Fallback if a caption-based question is not wanted: 'What is the woman doing?' -> 'She is sitting in bed.' Phrase 1: the young man lands on his back and rolls onto his side from 2.0; the robe man stays on his back. Phrase 3: the young man lies on a bare mattress on the floor, not a bed; the woman sits. 'a blanket' = the patchwork quilt. defaultVoice male: mixed group, evenId false."}
json.dump(c,open("content/4385.json","w"),indent=1,ensure_ascii=False)
