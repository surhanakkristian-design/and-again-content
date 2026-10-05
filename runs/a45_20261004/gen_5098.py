import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
tops={0.0:.32,0.5:.32,1.0:.33,1.5:.35,2.0:.35,2.5:.33,3.0:.36,3.5:.37,4.0:.42}
man={t:(0,y,0.70,1-y) for t,y in tops.items()}
man.update({4.5:(0,0.44,0.70,0.56),5.0:(0,0.50,0.70,0.50),5.5:(0,0.54,0.70,0.46),6.0:(0,0.57,0.78,0.43),6.5:(0,0.57,0.80,0.43),
 7.0:(0,0.59,0.78,0.41),7.5:(0,0.60,0.80,0.40),8.0:(0.05,0.60,0.60,0.40),8.5:(0.05,0.60,0.65,0.40),9.0:(0.05,0.60,0.60,0.40),
 9.5:(0.10,0.61,0.60,0.39),10.0:(0.12,0.60,0.60,0.40),10.5:(0.07,0.59,0.62,0.41),11.0:(0.05,0.59,0.62,0.41),11.5:(0.05,0.59,0.65,0.41),12.0:(0.05,0.59,0.62,0.41)})
flag={6.0:(0,0,0.18,0.36),6.5:(0,0,0.67,0.41),7.0:(0,0,0.82,0.48),7.5:(0,0,1,0.50),8.0:(0,0,1,0.50),8.5:(0,0,1,0.49),9.0:(0,0,1,0.49),
 9.5:(0,0,1,0.49),10.0:(0,0,1,0.49),10.5:(0,0,1,0.49),11.0:(0,0,1,0.51),11.5:(0,0,1,0.52),12.0:(0,0,1,0.51)}
c={"mediaId":5098,"level":"A","keyWord":"national","defaultVoice":"male",
"taps":[
 {"phrase":"to film himself","target":"the red-haired man","voice":"male","keys":K(man)},
 {"phrase":"to wear a long scarf","target":"the red-haired man","voice":"male","keys":K(man)},
 {"phrase":"to cover the sky","target":"the flag","voice":"male","keys":K(flag)}],
"stillS":9.0,
"nouns":[{"word":"a flag","x":0.50,"y":0.22,"voice":"male"},
 {"word":"lights","x":0.40,"y":0.43,"voice":"male"},
 {"word":"people","x":0.82,"y":0.80,"voice":"male"}],
"question":"What is the red-haired man looking at?",
"answer":["He","is","looking","at","the","national","flag."],"answerVoice":"male",
"notes":"Selfie clip: his arm reaches to the camera at the bottom left ('to film himself'). Drumming not used: the dark-haired man next to him (0-5.5) also beats a drum. 'to wear a long scarf': crowd members hold scarves up over their heads, they do not wear them; only he wears one round his neck. Flag visible from 6.0 (only a corner at top left at 6.0), covers the top half of the frame from 7.5; man box below it, no overlap. Noun 'a scarf' left out: the crowd holds many scarves up at the still. The red-haired man is boxed generously 0-4.0 (x 0-0.70), which also touches the dark-haired drummer's left arm."}
json.dump(c,open('content/5098.json','w'),indent=1)
