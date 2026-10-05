import json
T=[i*0.5 for i in range(21)]
def mk(d):
    ks=[]
    for t in T:
        b=d.get(t)
        if b: ks.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
        else: ks.append({"t":t,"off":True})
    return ks
M={0.0:(0,.17,.78,1),0.5:(0,.17,.72,1),1.0:(0,.13,.76,1),1.5:(0,.18,.44,1),9.0:(0,.38,.33,.60),9.5:(0,.37,.40,.59),10.0:(0,.34,.40,.55)}
R={2.5:(.10,.30,1,1),3.0:(.08,.33,1,1),3.5:(0,.37,1,1),4.0:(0,.35,1,1),4.5:(.12,.27,1,1),8.0:(.48,.41,1,1),8.5:(.30,.44,.92,1),
   9.0:(.34,.47,.70,1),9.5:(.40,.46,.60,1),10.0:(.40,.43,.60,1)}
Y={5.0:(.24,.30,1,1),5.5:(.08,.28,1,1),6.0:(.16,.29,1,1),9.0:(.70,.42,1,1),9.5:(.60,.41,1,1),10.0:(.60,.39,1,1)}
c={"mediaId":5100,"level":"B","keyWord":"stick","defaultVoice":"female",
 "taps":[
  {"phrase":"to attach a green flag","target":"the man in green","voice":"male","keys":mk(M)},
  {"phrase":"to wear a red jumper","target":"the woman in red","voice":"female","keys":mk(R)},
  {"phrase":"to stick a print onto Asia","target":"the man in yellow","voice":"male","keys":mk(Y)}],
 "stillS":10.0,
 "nouns":[{"word":"fairy lights","x":0.55,"y":0.16,"voice":"female"},{"word":"a map","x":0.30,"y":0.27,"voice":"female"},
          {"word":"a T-shirt","x":0.88,"y":0.80,"voice":"female"},{"word":"a camera","x":0.60,"y":0.93,"voice":"female"}],
 "question":"What is the man in yellow doing?",
 "answer":["He","is","sticking","a","print","onto","Asia."],
 "answerVoice":"male",
 "notes":"'to wear a red jumper' is a state: her actions (pointing, pressing a flag on) are shared with others (the woman in white also points at 8.0). Man in yellow only a sliver at the right edge at 8.5 -> off. 9.0-10.0 the woman in red and the man in yellow stand close: split at x 0.60-0.70, so the lower right part of her red jumper lies in his box. 'a print' = the instant photo (B-level word). The yellow flag + print land on northern Asia/Russia area of the map."}
json.dump(c,open('content/5100.json','w'),indent=1)
