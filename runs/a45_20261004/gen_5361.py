import json
times=[i*0.5 for i in range(19)]
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,.04,1,.96),1.5:(.64,0,.36,.42),2.0:(0,0,.24,.54),2.5:(.29,.02,.63,.87),
3.0:(.23,.05,.64,.93),3.5:(.24,.02,.62,.78),4.0:(.27,.12,.62,.75),4.5:(.28,.02,.66,.81),5.0:(.21,.02,.67,.93),
5.5:(.17,.03,.74,.90),6.0:(0,.04,1,.96),6.5:(.14,.19,.22,.27),7.0:(.15,.19,.19,.29),7.5:(.14,.21,.20,.28),
8.0:(.03,.24,.27,.27),8.5:(.10,.19,.23,.52),9.0:(0,.11,.37,.62)}
T={6.5:(.37,.02,.56,.96),7.0:(.35,.03,.53,.95),7.5:(.35,.07,.54,.92),8.0:(.31,.17,.55,.81),8.5:(.34,.17,.64,.80),9.0:(.38,.10,.62,.88)}
def keys(D):
    return [{"t":t,**dict(zip("xywh",D[t]))} if t in D else {"t":t,"off":True} for t in times]
c={"mediaId":5361,"level":"A","keyWord":"easy","defaultVoice":"female",
 "taps":[
  {"phrase":"to pull up the handle","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to carry six suitcases","target":"the trolley","voice":"female","keys":keys(T)},
  {"phrase":"to push a trolley","target":"the woman","voice":"female","keys":keys(W)}],
 "stillS":4.0,
 "nouns":[{"word":"a door","x":0.13,"y":0.25,"voice":"female"},
          {"word":"a big suitcase","x":0.55,"y":0.62,"voice":"female"},
          {"word":"a small suitcase","x":0.16,"y":0.75,"voice":"female"},
          {"word":"shoes","x":0.84,"y":0.84,"voice":"female"}],
 "question":"What is the woman pushing?",
 "answer":["She","is","pushing","a","trolley."],
 "answerVoice":"female",
 "notes":"Key word 'easy' is an adjective, not placed as a noun. At 1.5/2.0 only her legs are visible. In the airport shot she is mostly hidden behind the suitcase stack; her box covers her visible head/body, the trolley box the stack + trolley right of her (split line between them). At 6.0 the metal bars are suitcase handles, so the trolley is off."}
json.dump(c,open('content/5361.json','w'),indent=1)
