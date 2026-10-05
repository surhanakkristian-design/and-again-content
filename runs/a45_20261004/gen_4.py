import json
times=[i*0.5 for i in range(19)]
ptop={0.0:.69,0.5:.69,1.0:.70,1.5:.70,2.0:.71,2.5:.72,3.0:.72,3.5:.73,4.0:.75,4.5:.78,5.0:.80}
wk=[];pk=[]
for t in times:
    if t in ptop:
        y=ptop[t]
        wk.append({"t":t,"x":0.0,"y":0.03,"w":1.0,"h":round(y-0.03,2)})
        pk.append({"t":t,"x":0.82,"y":y,"w":0.18,"h":round(min(0.27,1-y),2)})
    else:
        wk.append({"t":t,"x":0.0,"y":0.02,"w":1.0,"h":0.96})
        pk.append({"t":t,"off":True})
c={"mediaId":4,"level":"A","keyWord":"course","defaultVoice":"female",
"taps":[
 {"phrase":"to drink cold coffee","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to type on a laptop","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to grow in a pot","target":"the plant","voice":"female","keys":pk}],
"stillS":0.0,
"nouns":[{"word":"a laptop","x":0.28,"y":0.75,"voice":"female"},{"word":"a glass","x":0.76,"y":0.70,"voice":"female"},
 {"word":"a plant","x":0.90,"y":0.84,"voice":"female"},{"word":"a table","x":0.40,"y":0.93,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","drinking","coffee","at","the","table."],
"answerVoice":"female",
"notes":"Key word 'course' is not visible (laptop screen never shown), so it is not used. Only one person; two phrases share her. The plant is small at the right edge and is hidden behind the glass from 5.5 s (off). Woman box is cut at the top of the plant box while the plant is visible. 'a glass' and 'a plant' pills are close (x), separated in y."}
json.dump(c,open('content/4.json','w'),indent=1)
