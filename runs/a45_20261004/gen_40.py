import json
T=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
F=(0,0,1,1)
wom={0.0:(0,0,1,0.15),0.5:(0,0,1,0.15),1.0:(0,0,1,0.20),1.5:(0,0,1,0.41),2.0:(0,0,0.62,0.75),2.5:(0,0,1,0.37),3.0:(0,0,1,0.39),3.5:(0,0,1,0.30),4.0:(0,0,1,0.28),
     4.5:(0,0,1,0.29),5.0:(0,0,1,0.28),5.5:(0,0,1,0.32),6.0:(0,0,1,0.41),6.5:(0,0,1,0.45),7.0:(0,0,1,0.46),7.5:(0,0,1,0.46),8.0:(0,0,1,0.46),8.5:(0,0,1,0.48),
     9.0:(0,0,1,0.57),9.5:(0,0,1,0.60),10.0:(0,0,1,0.58),10.5:(0,0,1,0.72),11.0:(0,0,1,0.85),11.5:(0,0,1,0.87),12.0:F,12.5:F,13.0:F,13.5:F,14.0:F,14.5:F,15.0:F}
cards={0.0:(0.30,0.42,0.42,0.27),0.5:(0.31,0.40,0.41,0.26),1.0:(0.30,0.38,0.42,0.26),1.5:(0.29,0.41,0.41,0.24),2.0:(0.62,0.36,0.38,0.38),2.5:(0,0.37,1,0.38),3.0:(0,0.39,1,0.38),
       3.5:(0,0.35,1,0.40),4.0:(0,0.32,1,0.42),4.5:(0,0.34,1,0.42),5.0:(0,0.35,1,0.42),5.5:(0,0.36,1,0.41),6.0:(0,0.41,1,0.34),6.5:(0,0.45,1,0.30),7.0:(0,0.46,1,0.29),
       7.5:(0,0.46,1,0.31),8.0:(0,0.46,1,0.34),8.5:(0,0.48,1,0.37),9.0:(0,0.57,1,0.41),9.5:(0,0.60,1,0.40),10.0:(0,0.58,1,0.42),10.5:(0,0.74,1,0.26),11.0:(0,0.86,1,0.14),11.5:(0,0.88,1,0.12)}
c={"mediaId":40,"level":"A","keyWord":"answer","defaultVoice":"female",
 "taps":[{"phrase":"to pick one card","target":"the woman","voice":"female","keys":keys(wom)},
         {"phrase":"to lie on the table","target":"the cards","voice":"female","keys":keys(cards)},
         {"phrase":"to hold up a card","target":"the woman","voice":"female","keys":keys(wom)}],
 "stillS":11.5,
 "nouns":[{"word":"hair","x":0.20,"y":0.20,"voice":"female"},{"word":"a sweater","x":0.80,"y":0.30,"voice":"female"},
          {"word":"a card","x":0.45,"y":0.44,"voice":"female"},{"word":"a table","x":0.60,"y":0.78,"voice":"female"}],
 "question":"What is the woman holding up?",
 "answer":["She","is","holding","up","a","card."],"answerVoice":"female",
 "notes":"Only two targets: the woman (first only her sweater and hands, face from 12.5 s) and the cards on the table. Her hands touch the cards, so the picture is split along a horizontal line (vertical at 2.0 s); the card she slides out counts as the woman's once she lifts it (10.5 s on). Cards are out of the picture from 12.0 s. The key word 'answer' is not a visible noun; it is only meant by the card text 'You have to wait'. The burned-in caption 'Ask a question' is on the first frames."}
json.dump(c,open('content/40.json','w'),indent=1,ensure_ascii=False)
