import json
T=[i*0.5 for i in range(19)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
sun={t:(0.23,0.0,0.22,0.12) for t in T if t<=3.5}
church={}
cy={2.5:(0.27,0.40),3.0:(0.26,0.45),3.5:(0.26,0.45),4.0:(0.21,0.42),4.5:(0.20,0.40),5.0:(0.19,0.40),5.5:(0.16,0.39),
    6.0:(0.14,0.37),6.5:(0.14,0.37),7.0:(0.18,0.41),7.5:(0.20,0.42),8.0:(0.21,0.42),8.5:(0.22,0.42),9.0:(0.22,0.43)}
for t,(a,b) in cy.items(): church[t]=(0.28,a,0.42,round(b-a,2))
people={}
for t in T:
    if t<=1.5: people[t]=(0.0,0.12,1.0,0.83)
    elif t==2.0: people[t]=(0.0,0.15,1.0,0.65)
    elif t==2.5: people[t]=(0.0,0.40,1.0,0.35)
    else:
        top=cy[t][1]; bot={3.0:0.88,3.5:0.9,4.0:0.9,4.5:0.92,5.0:0.98}.get(t,1.0)
        people[t]=(0.0,top,1.0,round(bot-top,2))
def keys(d): return [k(t,d.get(t)) for t in T]
c={"mediaId":4896,"level":"A","keyWord":"shadow","defaultVoice":"female",
 "taps":[
  {"phrase":"to run across the square","target":"the people","voice":"female","keys":keys(people)},
  {"phrase":"to shine in the sky","target":"the sun","voice":"female","keys":keys(sun)},
  {"phrase":"to have a big dome","target":"the church","voice":"female","keys":keys(church)}],
 "stillS":5.0,
 "nouns":[{"word":"the sky","x":0.5,"y":0.1,"voice":"female"},
          {"word":"a church","x":0.5,"y":0.33,"voice":"female"},
          {"word":"people","x":0.5,"y":0.55,"voice":"female"},
          {"word":"a shadow","x":0.42,"y":0.83,"voice":"female"}],
 "question":"What are the people doing?",
 "answer":["They","are","running","across","the","square."],
 "answerVoice":"female",
 "notes":"Crowd clip: 'the people' box is the whole crowd (very large). Sun visible only 0-3.5 s (glare at top). Church hidden behind the running man at 2.0 s -> off. 'a shadow' = the long shadow of the woman in red/yellow at bottom; many shadows exist, check. 'dome' maybe A2+."}
json.dump(c,open("content/4896.json","w"),indent=1)
