import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
def K(d): return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
wo={0.0:(.13,.40,.77,.35),0.5:(.17,.27,.64,.54),1.0:(.20,.10,.65,.90),1.5:(.12,.12,.70,.88),2.0:(.62,.23,.32,.44),2.5:(.61,.23,.34,.44),
3.0:(.60,.27,.33,.40),3.5:(.54,.27,.34,.40),4.0:(.34,.23,.35,.42),4.5:(.10,.46,.36,.22),5.0:(0,.37,.19,.36),
7.5:(.62,.44,.18,.16),8.0:(.61,.44,.18,.16),8.5:(.61,.44,.18,.16),9.0:(.60,.45,.18,.15)}
man={2.0:(.06,.51,.38,.25),2.5:(.15,.50,.34,.26),3.0:(0,.50,.56,.25),3.5:(0,.51,.44,.27),4.0:(0,.51,.20,.26)}
c={"mediaId":5197,"level":"B","keyWord":"rebel","defaultVoice":"female",
"taps":[{"phrase":"to climb onto her desk","target":"the woman on the desk","voice":"female","keys":K(wo)},
{"phrase":"to glare at her colleagues","target":"the woman on the desk","voice":"female","keys":K(wo)},
{"phrase":"to rip off his tie","target":"the man at the desk","voice":"male","keys":K(man)}],
"stillS":2.0,
"nouns":[{"word":"a swivel chair","x":.37,"y":.86,"voice":"female"},{"word":"ring binders","x":.66,"y":.71,"voice":"female"},
{"word":"a desk phone","x":.50,"y":.57,"voice":"female"},{"word":"ceiling lights","x":.27,"y":.17,"voice":"female"}],
"question":"Where is the angry woman standing?","answer":["She","is","standing","on","her","desk."],"answerVoice":"female",
"notes":"woman with the bob, glasses and vest: climbs up 0-1.5 (pulls off her lanyard at 1.5), glares from the desk 2.0-4.0, climbs down 4.5, at the left edge 5.0; off 5.5-7.0 (crowd shots); from 7.5 the small bob-haired woman in a vest with folded arms (x~.63-.75) is taken to be her - verifier please confirm. Man at the front desk loosens and rips off his tie 2.5-3.0 and throws it, off from 4.5. 'ceiling lights' = the row of lights on the ceiling."}
json.dump(c,open('content/5197.json','w'),indent=1)
