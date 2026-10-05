import json
times=[i*0.5 for i in range(24)]
lampc={0.0:.35,0.5:.35,1.0:.35,1.5:.37,2.0:.38,2.5:.39,3.0:.40,3.5:.41,4.0:.43,4.5:.44,9.5:.46,10.0:.46,10.5:.47,11.0:.46,11.5:.46}
lampclose={5.0:0.0,5.5:0.0,6.0:.04,6.5:.09,7.0:.13,7.5:.17,8.0:.19,8.5:.21,9.0:.21}
man=[];car=[];lamp=[]
for t in times:
    if t<=4.5:
        man.append({"t":t,"x":0.50,"y":0.20,"w":0.50,"h":0.80})
        car.append({"t":t,"x":0.0,"y":0.34,"w":0.50,"h":0.66})
        lamp.append({"t":t,"x":round(lampc[t]-.10,2),"y":0.04,"w":0.20,"h":0.15})
    elif t<=9.0:
        man.append({"t":t,"off":True})
        car.append({"t":t,"x":0.0,"y":0.20,"w":1.0,"h":0.80})
        lamp.append({"t":t,"x":lampclose[t],"y":0.0,"w":0.20,"h":0.14})
    else:
        man.append({"t":t,"x":0.60,"y":0.20,"w":0.40,"h":0.80})
        car.append({"t":t,"x":0.0,"y":0.45,"w":0.60,"h":0.55})
        lamp.append({"t":t,"x":round(lampc[t]-.10,2),"y":0.04,"w":0.20,"h":0.15})
d={"mediaId":4163,"level":"A","keyWord":"talk","defaultVoice":"male",
"taps":[
 {"phrase":"to talk to the camera","target":"the man","voice":"male","keys":man},
 {"phrase":"to be bright yellow","target":"the car","voice":"male","keys":car},
 {"phrase":"to shine in the dark","target":"the lamp","voice":"male","keys":lamp}],
"stillS":2.0,
"nouns":[{"word":"a man","x":0.74,"y":0.46,"voice":"male"},
 {"word":"a car","x":0.24,"y":0.56,"voice":"male"},
 {"word":"a lamp","x":0.38,"y":0.14,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","talking","to","the","camera."],
"answerVoice":"male",
"notes":"Cut to a car close-up 5.0-9.0 s (man off; the lamp is only a blurred glow at the top edge there, boxed anyway). Man and car overlap: split at x 0.50 (first shot) / 0.60 (last shot). In the last shot the man's stretched arm lies on the car roof (x 0.13-0.6, y 0.36-0.44): the car box starts below it at y 0.45 and the man box holds only his body, so the arm is in neither box. The car has no action, so its phrase is a state. Only 3 nouns: the stool is not an A-level word."}
json.dump(d,open("content/4163.json","w"),indent=1,ensure_ascii=False)
