import json,sys
VID=5367
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),2.0:(0,0,1,1),
   2.5:(0,0.09,1,0.91),3.0:(0,0.09,1,0.91),3.5:(0,0.09,1,0.91),4.0:(0,0,1,1),
   4.5:(0.07,0.15,0.88,0.58),5.0:(0,0.19,1,0.5),5.5:(0,0.17,1,0.52),6.0:(0,0.18,1,0.52),6.5:(0,0.15,1,0.55),
   7.0:(0.05,0.29,0.43,0.42),7.5:(0.39,0.36,0.36,0.32),8.0:(0.31,0.33,0.3,0.32),8.5:(0.3,0.35,0.3,0.27),9.0:(0.24,0.33,0.26,0.32)}
C={2.5:(0,0,1,0.09),3.0:(0,0,1,0.09),3.5:(0,0,1,0.09),
   4.5:(0,0.02,1,0.13),5.0:(0,0.02,1,0.17),5.5:(0,0.02,1,0.15),6.0:(0,0.02,1,0.16),6.5:(0,0.02,1,0.13),
   7.0:(0.5,0.2,0.5,0.12),7.5:(0,0.22,1,0.14),8.0:(0,0.24,1,0.09),8.5:(0,0.25,1,0.1),9.0:(0,0.26,1,0.07)}
c={"mediaId":VID,"level":"B","keyWord":"stuff","defaultVoice":"female",
 "taps":[
  {"phrase":"to gulp down her water","target":"the woman with braids","voice":"female","keys":K(W)},
  {"phrase":"to wear a tie-dye T-shirt","target":"the woman with braids","voice":"female","keys":K(W)},
  {"phrase":"to cheer from the stands","target":"the crowd","voice":"female","keys":K(C)}],
 "stillS":5.5,
 "nouns":[{"word":"spectators","x":0.22,"y":0.12,"voice":"female"},
          {"word":"a T-shirt","x":0.84,"y":0.46,"voice":"female"},
          {"word":"a plastic cup","x":0.14,"y":0.77,"voice":"female"},
          {"word":"a cheeseburger","x":0.38,"y":0.92,"voice":"female"}],
 "question":"What is the woman with braids doing?",
 "answer":["She","is","stuffing","a","burger","into","her","mouth."],
 "answerVoice":"female",
 "notes":"Close-ups 0.0-4.0 (drinking from a plastic cup), then her at the table 4.5-6.5, then wide shot of the row of competitors 7.0-9.0 with a blonde woman in front of her. Men in the far background also hold cups at 8.0-8.5 (tiny), so 'gulp down her water' is clearly hers only at 0-4.0. Crowd is blurred behind her at 2.5-3.5 (thin top strip), off at 0-2.0 and 4.0; its box is a strip above the competitors' heads, thin at 8.0-9.0. Blonde woman and other competitors also stuff burgers, so no burger phrase; it is the answer instead. Several cups and burgers in the still: pills on one cup and the front burger."}
json.dump(c,open(f'content/{VID}.json','w'),indent=1)
