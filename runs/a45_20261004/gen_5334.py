import json
ID=5334
times=json.load(open(f'frames/{ID}/packet.json'))['times']
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
man={0.0:(0,.07,1,.93),0.5:(0,.09,1,.91),1.0:(0,.04,1,.96),1.5:(0,.27,.31,.73),2.0:(0,.29,.19,.60),2.5:(0,.38,.18,.34),
     3.0:(0,.40,.18,.42),3.5:(0,.36,.25,.56),4.0:(0,.35,.44,.63),4.5:(.16,.37,.55,.62),5.0:(.39,.38,.57,.62),5.5:(.59,.38,.41,.62)}
fl={6.5:(0,.06,1,.27),7.0:(0,.07,1,.28),7.5:(0,.07,1,.28),8.0:(0,.06,1,.25),8.5:(0,.06,1,.23),9.0:(0,.06,1,.24)}
c={"mediaId":ID,"level":"B","keyWord":"respect","defaultVoice":"male",
 "taps":[
  {"phrase":"to carry rolled-up banners","target":"the bearded man","voice":"male","keys":keys(man)},
  {"phrase":"to have a bushy white beard","target":"the bearded man","voice":"male","keys":keys(man)},
  {"phrase":"to light up the stadium","target":"the floodlights","voice":"male","keys":keys(fl)}],
 "stillS":4.0,
 "nouns":[{"word":"a beard","x":0.15,"y":0.46,"voice":"male"},
          {"word":"a denim jacket","x":0.18,"y":0.68,"voice":"male"},
          {"word":"a hoodie","x":0.68,"y":0.60,"voice":"male"},
          {"word":"a wristwatch","x":0.80,"y":0.79,"voice":"male"}],
 "question":"What is the bearded man carrying?",
 "answer":["He","is","carrying","rolled-up","banners."],
 "answerVoice":"male",
 "notes":"Almost everyone holds a hand on the chest, so no phrase uses that. The rolled-up things under his arm (red/yellow with lettering) are read as rolled-up banners - check the word. The man in the navy hoodie with glasses also has a short white goatee; 'bushy white beard' is meant to fit only the big bald man. Bearded man only at the left edge at 2.0-3.0 (sleeve/shoulder), off from 6.0 (the denim sleeve at the right edge at 6.0 is the blonde woman). Floodlights only in the wide shots 6.5-9.0. 'rolled-up' is one chip."}
json.dump(c,open(f'content/{ID}.json','w'),indent=1)
