import json
B={0.0:(.10,.23,.89,.77),0.5:(.03,.15,.97,.85),1.0:(0,.12,1.0,.88),1.5:(0,.15,1.0,.85),2.0:(0,.10,1.0,.90),
2.5:(0,.03,1.0,.97),3.0:(.02,0,.70,.88),3.5:(.03,.10,.62,.80),4.0:(0,.10,.67,.68),4.5:(.08,.09,.60,.61),
5.0:(.20,.16,.43,.48),5.5:(.28,.47,.38,.35),6.0:(.30,.46,.34,.35),6.5:(.31,.46,.34,.35),7.0:(.30,.47,.32,.35),
7.5:(.32,.47,.35,.35),8.0:(.31,.46,.34,.35),8.5:(.29,.43,.34,.34),9.0:(.30,.42,.34,.38)}
T=[i*0.5 for i in range(19)]
K=[{"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} for t in T]
c={"mediaId":4886,"level":"B","keyWord":"steep","defaultVoice":"male",
"taps":[{"phrase":"to climb a steep slope","target":"the hiker","voice":"male","keys":K},
{"phrase":"to lean on trekking poles","target":"the hiker","voice":"male","keys":K},
{"phrase":"to carry a bulky rucksack","target":"the hiker","voice":"male","keys":K}],
"stillS":7.0,
"nouns":[{"word":"peaks","x":0.5,"y":0.11,"voice":"male"},{"word":"a valley","x":0.25,"y":0.34,"voice":"male"},
{"word":"a hiker","x":0.45,"y":0.56,"voice":"male"},{"word":"a trail","x":0.65,"y":0.8,"voice":"male"}],
"question":"What is the hiker doing?","answer":["He","is","climbing","a","steep","slope."],"answerVoice":"male",
"notes":"Only one person in the clip, so all three phrases share the hiker. 'a hiker' pill is on the man; other nouns are landscape."}
json.dump(c,open('content/4886.json','w'),indent=1)
