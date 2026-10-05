import json
T=[i*0.5 for i in range(19)]
def ks(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
woman={0.0:(.30,.20,.70,.80),0.5:(.30,.13,.70,.87),1.0:(0,.21,1.0,.79),1.5:(.30,.17,.68,.83),2.0:(.18,.12,.82,.88),
2.5:(.25,.10,.75,.90),3.0:(.24,.04,.76,.96),3.5:(.18,.10,.82,.90),4.0:(.02,.10,.98,.90),4.5:(.14,.05,.86,.95),
5.0:(.32,.08,.68,.92),5.5:(.38,.12,.62,.88),6.0:(.76,.34,.22,.30),6.5:(.82,.36,.18,.26),7.0:(.80,.36,.20,.32),
7.5:(.64,.36,.26,.34),8.0:(.44,.37,.32,.38),8.5:(.33,.36,.36,.43),9.0:(.34,.37,.40,.46)}
crowd={6.0:(0,.30,.74,.30),6.5:(0,.30,.80,.30),7.0:(0,.30,.78,.30),7.5:(0,.30,.62,.28),8.0:(0,.32,.42,.30),
8.5:(0,.30,.31,.32),9.0:(0,.32,.32,.26)}
c={"mediaId":5225,"level":"A","keyWord":"finish","defaultVoice":"female",
"taps":[{"phrase":"to drink from a cup","target":"the woman","voice":"female","keys":ks(woman)},
{"phrase":"to look at her watch","target":"the woman","voice":"female","keys":ks(woman)},
{"phrase":"to clap for the runner","target":"the crowd","voice":"female","keys":ks(crowd)}],
"stillS":6.0,
"nouns":[{"word":"the sky","x":.50,"y":.10,"voice":"female"},{"word":"people","x":.22,"y":.37,"voice":"female"},
{"word":"a runner","x":.80,"y":.45,"voice":"female"},{"word":"a cone","x":.79,"y":.61,"voice":"female"}],
"question":"What is the runner doing?",
"answer":["She","is","finishing","the","race."],"answerVoice":"female",
"notes":"Crowd only tapped 6.0-9.0 s (clapping spectators behind the barrier); at 8.5-9.0 s only the left part of the crowd is boxed because the runner stands in front of the middle. Spectators visible in the background at 0-1.5 s are not boxed. Tiny second runners far behind at 6.0-8.5 s."}
json.dump(c,open('content/5225.json','w'),indent=1)
