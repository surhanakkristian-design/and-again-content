import json
T=[i*0.5 for i in range(21)]
# t: (girl top y, boy top y, stars bottom)
D={0.0:(0.47,0.47,0.46),0.5:(0.48,0.50,0.47),1.0:(0.51,0.54,0.50),1.5:(0.52,0.55,0.51),2.0:(0.53,0.56,0.52),2.5:(0.55,0.58,0.54),
3.0:(0.59,0.61,0.58),3.5:(0.62,0.63,0.61),4.0:(0.63,0.65,0.62),4.5:(0.65,0.67,0.64),5.0:(0.69,0.69,0.68),5.5:(0.70,0.70,0.69),
6.0:(0.69,0.69,0.68),6.5:(0.69,0.69,0.68),7.0:(0.69,0.69,0.68),7.5:(0.67,0.67,0.66),8.0:(0.65,0.64,0.63),8.5:(0.64,0.63,0.62),
9.0:(0.63,0.62,0.61),9.5:(0.62,0.61,0.60),10.0:(0.60,0.59,0.58)}
G=[{"t":t,"x":0,"y":D[t][0],"w":0.52,"h":round(1-D[t][0],2)} for t in T]
B=[{"t":t,"x":0.52,"y":D[t][1],"w":0.48,"h":round(1-D[t][1],2)} for t in T]
S=[{"t":t,"x":0,"y":0,"w":1.0,"h":D[t][2]} for t in T]
c={"mediaId":719,"level":"A","keyWord":"space","defaultVoice":"male",
"taps":[
{"phrase":"to wear a purple sweater","target":"the girl","voice":"female","keys":G},
{"phrase":"to wear a grey sweater","target":"the boy","voice":"male","keys":B},
{"phrase":"to shine in the dark","target":"the stars","voice":"male","keys":S}],
"stillS":2.0,
"nouns":[{"word":"stars","x":0.50,"y":0.34,"voice":"male"},{"word":"a girl","x":0.27,"y":0.74,"voice":"female"},{"word":"a boy","x":0.72,"y":0.76,"voice":"male"}],
"question":"What are they looking at?",
"answer":["They","are","looking","at","the","stars."],"answerVoice":"male",
"notes":"Girl and boy do exactly the same thing all clip (lean back, look up), so their phrases are states (sweater colour); the boy's sweater is dark grey and looks almost black in the dark frames 4.0-7.5. Stars = the whole projected dome; at 0.0 the dome is still lit brown with only a few faint stars. Key word 'space' not used as a noun because it would label the same place as 'stars'. Only 3 nouns: nothing else is clearly visible. Boxes of girl and boy split at x 0.52; her hand reaches across that line at 8.0-10.0."}
json.dump(c,open("content/719.json","w"),indent=1)
