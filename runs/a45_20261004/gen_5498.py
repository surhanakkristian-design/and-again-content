import json
B={0.0:(0.32,0.39,0.48,0.38),0.5:(0.32,0.39,0.48,0.38),1.0:(0.34,0.41,0.44,0.35),1.5:(0.07,0.38,0.80,0.42),2.0:(0.06,0.39,0.84,0.43),
 2.5:(0.04,0.39,0.90,0.44),3.0:(0.29,0.40,0.50,0.36),3.5:(0.10,0.40,0.80,0.41),4.0:(0.12,0.39,0.77,0.41),4.5:(0.08,0.38,0.86,0.43),
 5.0:(0.05,0.39,0.87,0.43),5.5:(0.28,0.39,0.64,0.41),6.0:(0.05,0.39,0.88,0.43),6.5:(0.03,0.38,0.94,0.45),7.0:(0.0,0.38,0.97,0.45),
 7.5:(0.0,0.38,0.99,0.45),8.0:(0.31,0.43,0.41,0.33),8.5:(0.26,0.42,0.52,0.37),9.0:(0.0,0.45,0.93,0.37),9.5:(0.16,0.41,0.66,0.41),
 10.0:(0.20,0.42,0.54,0.41),10.5:(0.20,0.42,0.55,0.41),11.0:(0.19,0.43,0.55,0.40),11.5:(0.20,0.43,0.55,0.40),12.0:(0.19,0.43,0.54,0.40)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in sorted(B.items())]
c={"mediaId":5498,"level":"A","keyWord":"window","defaultVoice":"female",
 "taps":[{"phrase":"to open the window","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to wear a warm jumper","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to look very happy","target":"the woman","voice":"female","keys":keys}],
 "stillS":10.0,
 "nouns":[{"word":"a window","x":0.50,"y":0.09,"voice":"female"},{"word":"a mountain","x":0.35,"y":0.39,"voice":"female"},
  {"word":"a woman","x":0.52,"y":0.52,"voice":"female"},{"word":"snow","x":0.20,"y":0.66,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","opening","the","window."],"answerVoice":"female",
 "notes":"Only one person; windows/landscapes are static and surround her, so all three phrases target the woman. 'a window' pill sits on the top of the white window frame. 'jumper' is British English (US: sweater)."}
json.dump(c,open('content/5498.json','w'),indent=1)
