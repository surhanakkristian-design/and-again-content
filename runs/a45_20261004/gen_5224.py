import json
T=[i*0.5 for i in range(19)]
def ks(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
behind={t:(.08,.59,.84,.41) for t in [5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]}
king={0.0:(0,.22,1.0,.78),0.5:(0,.22,1.0,.78),1.0:(0,.20,.62,.80),1.5:(.38,.22,.62,.78),2.0:(.22,.32,.34,.30),2.5:(.22,.32,.38,.30),
3.0:(.22,.33,.36,.29),3.5:(.22,.33,.24,.18),4.0:(.23,.34,.32,.28),4.5:(.23,.34,.32,.28),5.0:(.24,.26,.32,.34),**behind}
servant={1.0:(.64,.13,.36,.87),1.5:(0,.12,.36,.88)}
crowd={t:(0,.40,1.0,.18) for t in behind}
c={"mediaId":5224,"level":"A","keyWord":"royal","defaultVoice":"male",
"taps":[{"phrase":"to wear a gold crown","target":"the king","voice":"male","keys":ks(king)},
{"phrase":"to carry a tray of food","target":"the servant","voice":"male","keys":ks(servant)},
{"phrase":"to bow to the king","target":"the crowd","voice":"male","keys":ks(crowd)}],
"stillS":0.0,
"nouns":[{"word":"candles","x":.65,"y":.11,"voice":"male"},{"word":"a crown","x":.42,"y":.27,"voice":"male"},
{"word":"a guard","x":.85,"y":.42,"voice":"male"},{"word":"a chair","x":.14,"y":.77,"voice":"male"}],
"question":"What is the crowd doing?",
"answer":["They","are","bowing","to","the","king."],"answerVoice":"male",
"notes":"Servant with the tray is visible only 1.0-1.5 s (short window). Crowd bows from 6.5 s; at 5.5-6.0 s it still stands. King seen from behind at 5.5-9.0 s; crowd box cut at y 0.58 above his crown. 'a chair' labels the carved throne (A level)."}
json.dump(c,open('content/5224.json','w'),indent=1)
