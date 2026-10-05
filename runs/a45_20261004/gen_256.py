import json
T=[i*0.5 for i in range(21)]
def mk(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(0,.17,.50,1),0.5:(0,.17,.53,1),1.0:(0,0,.83,1),1.5:(0,0,.81,1),2.0:(0,0,1,1),2.5:(0,0,1,1),3.0:(0,.02,.77,1),
   4.5:(0,.09,.46,1),5.0:(0,.11,.42,1),5.5:(0,.10,.48,1),6.0:(0,.13,.48,1),6.5:(0,.15,.49,1),7.0:(0,.15,.47,1),7.5:(0,.16,.48,1),
   8.0:(0,.14,.59,1),8.5:(0,.21,.52,1),9.0:(0,.20,.46,1),9.5:(0,.22,.44,1),10.0:(0,.24,.43,1)}
C={0.0:(.51,.17,.70,.38),0.5:(.54,.15,.73,.37),1.0:(.84,.08,1,.46),1.5:(.82,.08,1,.42),3.0:(.78,.13,.98,.47),
   5.0:(.55,.11,.74,.44),5.5:(.49,.10,.67,.36),6.0:(.49,.09,.67,.31),6.5:(.52,.09,.71,.31),7.0:(.52,.12,.70,.34),7.5:(.53,.08,.72,.22),
   8.0:(.60,.12,.78,.33),8.5:(.53,.13,.71,.36),9.0:(.47,.14,.67,.42),9.5:(.47,.16,.66,.42),10.0:(.44,.16,.62,.37)}
M={0.0:(.71,.15,1,1),0.5:(.74,.14,1,1),3.5:(.09,.06,1,1),4.0:(.03,.02,1,1),4.5:(.47,.10,1,1),5.0:(.75,.10,1,1),5.5:(.68,.08,1,1),
   6.0:(.68,.15,1,1),6.5:(.72,.14,1,1),7.0:(.71,.16,1,1),7.5:(.66,.23,1,1),8.0:(.75,.34,1,1),8.5:(.72,.18,1,1),9.0:(.68,.20,1,1),9.5:(.67,.20,1,1),10.0:(.63,.21,1,1)}
c={"mediaId":256,"level":"A","keyWord":"eating","defaultVoice":"female",
"taps":[
 {"phrase":"to smell the hot soup","target":"the young woman","voice":"female","keys":mk(W)},
 {"phrase":"to have a dark beard","target":"the man","voice":"male","keys":mk(M)},
 {"phrase":"to cook in the street","target":"the cook","voice":"female","keys":mk(C)}],
"stillS":10.0,
"nouns":[{"word":"a sign","x":0.26,"y":0.16,"voice":"female"},{"word":"a beard","x":0.73,"y":0.40,"voice":"female"},{"word":"bowls","x":0.50,"y":0.76,"voice":"female"},{"word":"jeans","x":0.14,"y":0.88,"voice":"female"}],
"question":"What are the man and woman eating?",
"answer":["They","are","eating","hot","soup","with","noodles."],
"answerVoice":"female",
"notes":"Many cuts. Both guests eat noodles, drink from bowls, rub their bellies and give thumbs up, so the unique phrases are: the young woman smells her soup (0.5, bowl at her nose, eyes closed) and the man's beard (state). The cook (older woman in an apron at the stall behind them) stands between/behind the two heads: her box takes the gap, so the man's box starts right of her and loses his near shoulder/hand in the two-shots. Cook set off where she is hidden or only a blur (2.0, 2.5, 3.5-4.5). Young woman off at 3.5/4.0 (only a sleeve at the edge). stillS 10.0: the two empty bowls stand together ('bowls')."}
json.dump(c,open('content/256.json','w'),indent=1,ensure_ascii=False)
