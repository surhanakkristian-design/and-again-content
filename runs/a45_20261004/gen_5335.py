import json
ID=5335
times=json.load(open(f'frames/{ID}/packet.json'))['times']
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
w={0.0:(.09,.33,.70,.67),0.5:(.01,.37,.82,.63),1.0:(.04,.11,.83,.89),1.5:(.07,.11,.93,.89),2.0:(.20,.03,.63,.97),
   2.5:(.24,.16,.56,.84),3.0:(.28,.30,.46,.70),3.5:(.32,.41,.36,.59),4.0:(.37,.46,.30,.44),4.5:(.38,.53,.27,.33),
   5.0:(.43,.62,.20,.26),5.5:(.42,.68,.20,.18)}
f={5.5:(.18,0,.55,.14),6.0:(.17,0,.50,.14),6.5:(.17,.02,.48,.14),7.0:(.18,.04,.48,.15),7.5:(.18,.06,.46,.14),
   8.0:(.20,.11,.45,.14),8.5:(.20,.14,.80,.16),9.0:(.22,.17,.78,.15),9.5:(.22,.20,.78,.14),10.0:(.24,.21,.76,.14)}
c={"mediaId":ID,"level":"B","keyWord":"enthusiastic","defaultVoice":"female",
 "taps":[
  {"phrase":"to leap out of her seat","target":"the woman in the denim jacket","voice":"female","keys":keys(w)},
  {"phrase":"to clap above her head","target":"the woman in the denim jacket","voice":"female","keys":keys(w)},
  {"phrase":"to shine over the stadium","target":"the floodlights","voice":"female","keys":keys(f)}],
 "stillS":2.0,
 "nouns":[{"word":"a denim jacket","x":0.38,"y":0.56,"voice":"female"},
          {"word":"jeans","x":0.52,"y":0.86,"voice":"female"},
          {"word":"spectators","x":0.86,"y":0.62,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","clapping","above","her","head."],
 "answerVoice":"female",
 "notes":"Woman in the denim jacket is tracked while the shot widens; from 5.0 she is small in the crowd and from 6.0 she cannot be picked out, so off. Floodlights from 5.5 (at 5.0 only a sliver at the top edge, off); from 8.5 a second floodlight at the right edge is included in the box. Others in the crowd clap too but at chest height, not above the head. Still 2.0: 'spectators' on the seated fans to the right of her."}
json.dump(c,open(f'content/{ID}.json','w'),indent=1)
