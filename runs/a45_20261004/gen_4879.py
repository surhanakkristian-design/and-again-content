import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
woman={0.0:(0,.30,.85,.70),0.5:(.10,.30,.74,.70),1.0:(.18,.30,.58,.70),1.5:(.25,.25,.58,.75),2.0:(0,.15,1,.85),
 2.5:(.05,.27,.95,.73),3.0:(.05,.20,.95,.80),3.5:(.05,.15,.92,.85),4.0:(.08,.07,.86,.93),4.5:(.12,.50,.80,.50),
 5.0:(.05,.63,.80,.37),5.5:(.08,.42,.88,.58),6.0:(.05,.36,.92,.64),6.5:(.05,.32,.90,.68),
 7.0:(.32,.50,.36,.44),7.5:(.33,.49,.36,.45),8.0:(.34,.46,.32,.48),8.5:(.32,.47,.32,.47),9.0:(.30,.51,.34,.47)}
log={4.5:(0,.13,1,.37),5.0:(0,.27,1,.36),5.5:(0,0,1,.42),6.0:(0,.04,1,.32),6.5:(0,.02,1,.30)}
car={7.0:(0,.10,1,.40),7.5:(0,.09,1,.40),8.0:(.02,.09,.98,.37),8.5:(.02,.10,.98,.37),9.0:(.02,.12,.98,.39)}
c={"mediaId":4879,"level":"B","keyWord":"competition","defaultVoice":"female",
"taps":[
 {"phrase":"to hoist a massive boulder","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to lie across her shoulders","target":"the log","voice":"female","keys":keys(log)},
 {"phrase":"to rest on her raised hands","target":"the car","voice":"female","keys":keys(car)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.80,"y":0.06,"voice":"female"},
 {"word":"a car","x":0.45,"y":0.25,"voice":"female"},
 {"word":"a weightlifter","x":0.48,"y":0.60,"voice":"female"},
 {"word":"a mat","x":0.50,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","lifting","heavy","objects","in","a","competition."],
"answerVoice":"female",
"notes":"Woman (the only athlete) keyed throughout; log 4.5-6.5 s and car 7.0-9.0 s split from her box along the line of her hands/shoulders, so her box excludes raised arms while the object is held. Log lies across her shoulders at 4.5-5.0 s, then is pressed overhead 5.5-6.5 s. Boulder hoist 2.0-4.0 s. Key word 'competition' not a visible noun, used in the answer."}
json.dump(c,open('content/4879.json','w'),indent=1)
