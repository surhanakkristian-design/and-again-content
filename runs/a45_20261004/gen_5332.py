import json
ID=5332
times=json.load(open(f'frames/{ID}/packet.json'))['times']
def keys(d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
chef={0.0:(.21,.06,.64,.52),0.5:(.3,.05,.62,.52),1.0:(.35,.07,.52,.55),1.5:(.38,.1,.42,.5),
      6.5:(.40,.32,.20,.50),7.0:(.42,.38,.15,.47),7.5:(.43,.40,.14,.45)}
grey={5.5:(0,.12,.56,.80),6.0:(0,.17,.56,.78),6.5:(.62,.33,.38,.67),7.0:(.58,.38,.40,.62),7.5:(.58,.37,.41,.63),
      8.0:(.58,.38,.37,.55),8.5:(.62,.40,.37,.52),9.0:(.54,.45,.43,.53)}
wait={4.5:(.20,.14,.52,.56),5.0:(.17,.16,.56,.60)}
c={"mediaId":ID,"level":"B","keyWord":"unity","defaultVoice":"female",
 "taps":[
  {"phrase":"to hand over a plate","target":"the chef","voice":"male","keys":keys(chef)},
  {"phrase":"to pour water into a glass","target":"the grey-haired man","voice":"male","keys":keys(grey)},
  {"phrase":"to serve a cappuccino","target":"the waitress at the bar","voice":"female","keys":keys(wait)}],
 "stillS":6.0,
 "nouns":[{"word":"an exit sign","x":0.58,"y":0.10,"voice":"female"},
          {"word":"a doorway","x":0.62,"y":0.33,"voice":"female"},
          {"word":"a bottle","x":0.42,"y":0.64,"voice":"female"},
          {"word":"a tablecloth","x":0.55,"y":0.86,"voice":"female"}],
 "question":"What is the grey-haired man doing?",
 "answer":["He","is","pouring","water","into","a","glass."],
 "answerVoice":"male",
 "notes":"Clip of many cuts. Chef: kitchen pass 0.0-1.5 (hidden behind the waitress at 2.0, off), then taken as the man in the white chef's jacket in the middle of the group at 6.5-7.5 (same person assumed, not certain); off at 8.0-9.0 where the huddle hides him. Grey-haired man (manager): pouring 5.5-6.0, then on the right of the group 6.5-9.0. Waitress at the bar: only 4.5-5.0; she may also stand in the group but cannot be identified there, so off. Key word 'unity' is abstract, no noun."}
json.dump(c,open(f'content/{ID}.json','w'),indent=1)
