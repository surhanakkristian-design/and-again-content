import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
red={0.0:(.34,.31,.66,.69),0.5:(.33,.31,.67,.69),1.0:(.05,.23,.95,.77),1.5:(.20,.30,.80,.70),2.0:(.24,.27,.76,.73),
 2.5:(.33,.30,.67,.70),3.5:(.25,.36,.37,.50),4.0:(.15,.32,.40,.52),5.0:(.12,.11,.60,.74),6.0:(.43,.09,.19,.30)}
mnt={0.0:(0,.08,.86,.22),0.5:(0,.08,.86,.22),1.0:(0,.07,.88,.15),1.5:(0,.08,.90,.21),2.0:(0,.08,1,.19),2.5:(0,.08,1,.18),3.0:(0,.07,.98,.24)}
row={6.5:(.10,.20,.32,.34),7.0:(.15,.23,.29,.31),7.5:(.02,.23,.40,.31),8.0:(.02,.23,.41,.30),8.5:(.22,.23,.22,.28),
 9.0:(.19,.20,.33,.33),9.5:(.19,.25,.30,.28),10.0:(.17,.25,.27,.28)}
c={"mediaId":5032,"level":"A","keyWord":"ahead","defaultVoice":"female",
"taps":[
 {"phrase":"to read a map","target":"the woman in red","voice":"female","keys":K(red)},
 {"phrase":"to rise above the trees","target":"the snowy mountains","voice":"female","keys":K(mnt)},
 {"phrase":"to raise her fist","target":"the woman at the front of the boat","voice":"female","keys":K(row)}],
"stillS":0.0,
"nouns":[{"word":"mountains","x":.30,"y":.17,"voice":"female"},{"word":"a cap","x":.58,"y":.32,"voice":"female"},
 {"word":"a jacket","x":.70,"y":.55,"voice":"female"},{"word":"a map","x":.76,"y":.73,"voice":"female"}],
"question":"What is the woman in red doing?",
"answer":["She","is","reading","a","map."],"answerVoice":"female",
"notes":"Three shots: trail 0-3.0, stream 3.5-6.0, rowing boat 6.5-10.0. Woman in red OFF at 3.0 (only a map corner), 4.5 (only a shoe) and 5.5 (hidden behind the blonde hiker); 6.0 box on the red top behind the blonde - check it is her. Snowy mountains only in the trail shot (rowing shot has other, mostly snowless mountains -> OFF). 'a cap' is the grey cap of the man behind her at 0.0, pill sits close to her hair."}
json.dump(c,open('content/5032.json','w'),indent=1)
