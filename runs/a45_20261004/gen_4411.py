import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
wom={0.0:(.10,.04,.74,.97),0.5:(.08,0,1,1),1.0:(.19,.19,.97,1),1.5:(0,.19,.75,1),2.0:(0,.17,.98,.95),2.5:(0,.12,.58,.95),
 3.0:(0,.03,.49,.97),3.5:(0,0,.55,.97),4.0:(0,0,.46,1),4.5:(0,0,.50,1),5.0:(0,0,.52,1),5.5:(0,0,.62,1),6.0:(0,0,.50,1),
 6.5:(0,.34,1,1),7.0:(0,.42,1,1),7.5:(0,.44,1,1),8.0:(0,.51,1,1),8.5:(0,0,.50,1),9.0:(0,0,.50,.97)}
man={1.0:(0,.16,.18,.31),1.5:(.08,.04,.46,.18),2.0:(.19,.01,.67,.16),2.5:(.59,0,.92,.66),3.0:(.50,.07,1,.83),3.5:(.56,.07,1,.82),
 4.0:(.47,0,1,.58),4.5:(.51,0,1,.58),5.0:(.53,0,1,.75),5.5:(.63,0,1,.75),6.0:(.51,0,1,.60),6.5:(.40,0,1,.33),7.0:(.36,0,1,.41),
 7.5:(.36,0,1,.43),8.0:(.30,0,1,.50),8.5:(.51,0,1,.50),9.0:(.51,.02,1,.80)}
c={"mediaId":4411,"level":"B","keyWord":"treatment","defaultVoice":"female",
 "taps":[
  {"phrase":"to roll down her sock","target":"the woman","voice":"female","keys":K(wom)},
  {"phrase":"to treat a painful blister","target":"the woman","voice":"female","keys":K(wom)},
  {"phrase":"to hand over a plaster","target":"the man","voice":"male","keys":K(man)}],
 "stillS":4.0,
 "nouns":[{"word":"a blister","x":.38,"y":.60,"voice":"female"},{"word":"a sock","x":.62,"y":.71,"voice":"female"},
          {"word":"a boot","x":.72,"y":.88,"voice":"female"},{"word":"a sun hat","x":.78,"y":.12,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","treating","a","blister","on","her","heel."],
 "answerVoice":"female",
 "notes":"Only two targets (woman, man), so two phrases share the woman. The two overlap heavily in the close-ups: boxes are split along the line between her leg/hands and his body - vertical split at 2.5-6 s and 8.5-9 s, horizontal split at 6.5-8 s (her hands and ankle below, his body above), so parts of her upper leg (6.5-8 s) and of his left arm lie outside their boxes. Man off at 0-0.5 s (only a sleeve at the edge at 0.5 s); at 1-2 s only his hat/head behind her. 'painful' is read from her face and the raw blister. Key word 'treatment' appears as the verb 'to treat / treating'. Nouns at 4.0 s: blister and sock pills are close (0.11 apart in y)."}
json.dump(c,open('content/4411.json','w'),indent=1,ensure_ascii=False)
