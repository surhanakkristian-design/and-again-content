import json
T=[i*0.5 for i in range(25)]
w={0.0:(0.18,0.37,0.82,0.63),0.5:(0.18,0.36,0.82,0.64),1.0:(0.17,0.34,0.72,0.66),1.5:(0.2,0.37,0.8,0.63),2.0:(0.17,0.37,0.83,0.63),2.5:(0.2,0.35,0.8,0.65),
3.0:(0.37,0.3,0.63,0.7),3.5:(0.3,0.32,0.7,0.68),4.0:(0.27,0.33,0.71,0.67),4.5:(0.25,0.34,0.75,0.66),5.0:(0.17,0.33,0.83,0.67),5.5:(0,0.33,1,0.67),
6.0:(0.03,0.33,0.97,0.67),6.5:(0.03,0.33,0.97,0.67),7.0:(0.1,0.33,0.9,0.67),7.5:(0.05,0.33,0.95,0.67),8.0:(0,0.32,1,0.68),8.5:(0.08,0.32,0.92,0.68),
9.0:(0.0,0.3,0.65,0.7),9.5:(0,0.29,0.7,0.71),10.0:(0,0.28,0.68,0.72),10.5:(0,0.27,0.7,0.73),11.0:(0,0.26,0.71,0.74),11.5:(0,0.25,0.73,0.75),12.0:(0,0.23,0.73,0.77)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4681,"level":"A","keyWord":"lamp","defaultVoice":"female",
"taps":[
 {"phrase":"to ride a camel","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to touch a blue lamp","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":keys(w)}],
"stillS":7.0,
"nouns":[{"word":"a lamp","x":0.26,"y":0.45,"voice":"female"},{"word":"a hand","x":0.25,"y":0.63,"voice":"female"},{"word":"a scarf","x":0.74,"y":0.61,"voice":"female"},{"word":"a shirt","x":0.52,"y":0.82,"voice":"female"}],
"question":"What is the woman touching?",
"answer":["She","is","touching","a","big","blue","lamp."],
"answerVoice":"female",
"notes":"Only the woman is a real tap target (three shots: camel 0-2.5, bazaar 3.0-8.5, boat 9.0-12.0; 9.0 is a cross-fade). The camel itself is hardly visible (head at the left edge at 0.0-0.5), she sits on the saddle. 'a lamp' pill is on the big blue lamp; many small lamps hang behind, no other noun names them. In the lamp shots her box includes the raised hand and so overlaps the lower part of the blue lamp."}
json.dump(c,open("content/4681.json","w"),indent=1)
