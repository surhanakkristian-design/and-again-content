import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
hands={0.0:(0,.19,1,.45),0.5:(0,.21,1,.5),1.0:(0,.25,1,.42),1.5:(0,.15,1,.52),2.0:(0,0,1,.63)}
hoop={6.0:(0,.14,1,.86),6.5:(0,.14,1,.86),7.0:(0,.14,1,.86)}
women={7.5:(0,.25,1,.37),8.0:(0,.2,1,.38),8.5:(0,.2,1,.4),9.0:(0,.08,1,.92),9.5:(0,.1,1,.9),10.0:(0,.2,1,.8)}
c={"mediaId":4845,"level":"A","keyWord":"cloth","defaultVoice":"male",
"taps":[
 {"phrase":"to sew on a button","target":"the hands on the blue shirt","voice":"male","keys":keys(hands)},
 {"phrase":"to hold the white cloth","target":"the round frame","voice":"male","keys":keys(hoop)},
 {"phrase":"to lift a big blanket","target":"the women","voice":"female","keys":keys(women)}],
"stillS":4.5,
"nouns":[{"word":"a sewing machine","x":0.45,"y":0.13,"voice":"male"},
 {"word":"a hand","x":0.82,"y":0.48,"voice":"male"},
 {"word":"cloth","x":0.40,"y":0.80,"voice":"male"}],
"question":"What are the women lifting?",
"answer":["They","are","lifting","a","big","blanket."],
"answerVoice":"female",
"notes":"Five shots, different people; no single main person, evenId false -> defaultVoice male. Hands in shot 1 (0-2 s) are of unclear gender -> male default. 'blanket' for the patchwork quilt (A level). Round frame = embroidery hoop (A wording), holds white cloth only at 6-7 s. Women keyed 7.5-10 s (at the table first, then lifting). Still 4.5 s: only 3 nouns, the needle is too close to the hand pill."}
json.dump(c,open('content/4845.json','w'),indent=1)
