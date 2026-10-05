import json
times=[i*0.5 for i in range(21)]
def keys(b): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t in times]
W=(0,.10,.95,.53); P=(0,.77,.67,.16)
c={"mediaId":608,"level":"B","keyWord":"relief","defaultVoice":"female",
"taps":[{"phrase":"to grip the steering wheel","target":"the driver","voice":"female","keys":keys(W)},
{"phrase":"to laugh with relief","target":"the driver","voice":"female","keys":keys(W)},
{"phrase":"to rest on the windscreen","target":"the wiper","voice":"female","keys":keys(P)}],
"stillS":6.0,
"nouns":[{"word":"a steering wheel","x":.62,"y":.45,"voice":"female"},{"word":"a dashboard","x":.50,"y":.68,"voice":"female"},{"word":"a windscreen wiper","x":.33,"y":.85,"voice":"female"},{"word":"a sweatshirt","x":.21,"y":.43,"voice":"female"}],
"question":"What is the driver gripping?","answer":["She","is","gripping","the","steering","wheel."],"answerVoice":"female",
"notes":"One fixed shot through the windscreen; the driver hardly moves, so her box is the same at every time (it holds the wheel too, which is in front of her). Only one person: two phrases share her; the third target is the windscreen wiper at the bottom (a thing, a state). 'to laugh with relief' is true only from about 9.0 s; she grips the wheel until 7.5 s. A passenger's hand shows at the right edge (x > 0.95) and is left outside the box. The key word 'relief' is abstract, so it is in a phrase, not in the nouns."}
json.dump(c,open('content/608.json','w'),indent=1,ensure_ascii=False)
