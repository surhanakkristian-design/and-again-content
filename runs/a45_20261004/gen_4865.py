import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
p={0.0:(0.27,0.32,0.54,0.58),0.5:(0.27,0.31,0.54,0.60),1.0:(0.23,0.31,0.57,0.60),1.5:(0.19,0.22,0.81,0.68),
2.0:(0.19,0.21,0.81,0.59),2.5:(0.19,0.21,0.81,0.59),3.0:(0.19,0.21,0.81,0.59),3.5:(0.21,0.21,0.79,0.59),
7.5:(0.02,0.32,0.98,0.68),8.0:(0.05,0.31,0.90,0.69),8.5:(0.08,0.31,0.90,0.69),9.0:(0.14,0.32,0.74,0.68),
9.5:(0.16,0.31,0.84,0.69),10.0:(0.14,0.29,0.86,0.71)}
cy={4.0:(0.07,0.39,0.72,0.43)}
tr={5.0:(0.28,0.64,0.36,0.36),5.5:(0.26,0.64,0.34,0.36),6.0:(0.33,0.63,0.32,0.37),6.5:(0.33,0.64,0.30,0.36),7.0:(0.33,0.68,0.31,0.32)}
c={"mediaId":4865,"level":"B","keyWord":"lens","defaultVoice":"male",
"taps":[
 {"phrase":"to crouch beside a rosebush","target":"the photographer","voice":"male","keys":keys(p)},
 {"phrase":"to ride a racing bike","target":"the cyclist","voice":"male","keys":keys(cy)},
 {"phrase":"to support the camera","target":"the tripod","voice":"male","keys":keys(tr)}],
"stillS":2.0,
"nouns":[{"word":"a clock tower","x":0.60,"y":0.12,"voice":"male"},
 {"word":"a lens","x":0.38,"y":0.48,"voice":"male"},
 {"word":"a rose","x":0.25,"y":0.58,"voice":"male"},
 {"word":"a sneaker","x":0.82,"y":0.73,"voice":"male"}],
"question":"What is the photographer photographing up close?",
"answer":["He","is","photographing","a","delicate","pink","rose."],
"answerVoice":"male",
"notes":"Cyclist is visible in one frame only (4.0 s, blurred street shot); tripod only 5.0-7.0 s. Photographer keyed in the park, rose garden and red-carpet shots; at 7.5-10 s the crowd behind him is not tapped. Rose is pale pink."}
json.dump(c,open('content/4865.json','w'),indent=1)
