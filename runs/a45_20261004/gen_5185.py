import json
T=[i*0.5 for i in range(21)]
OM={0.0:(.03,.37,.52,.63),0.5:(.02,.37,.56,.63),1.0:(.03,.36,.52,.64),1.5:(.03,.37,.49,.63),2.0:(.03,.37,.45,.63),
 2.5:(.05,.37,.45,.63),3.0:(.03,.35,.44,.65),3.5:(.07,.35,.45,.65),4.0:(.08,.34,.42,.66),4.5:(.07,.34,.43,.66),
 5.0:(.03,.34,.44,.66),5.5:(.03,.34,.44,.66),6.0:(.02,.34,.46,.66),6.5:(0,.32,.40,.68),7.0:(0,.31,.38,.69),
 7.5:(0,.31,.42,.69),8.0:(0,.30,.45,.70),8.5:(0,.30,.48,.70),9.0:(0,.29,.52,.71),9.5:(0,.29,.52,.71),10.0:(0,.27,.53,.73)}
YP={0.0:(.55,.29,.35,.71),0.5:(.58,.30,.38,.70),1.0:(.55,.29,.45,.71),1.5:(.52,.34,.44,.66),2.0:(.48,.32,.45,.68),
 2.5:(.50,.33,.40,.67),3.0:(.47,.32,.38,.68),3.5:(.52,.33,.38,.67),4.0:(.50,.31,.34,.69),4.5:(.50,.31,.34,.69),
 5.0:(.47,.31,.35,.69),5.5:(.47,.31,.35,.69),6.0:(.48,.31,.45,.69),6.5:(.40,.27,.40,.73),7.0:(.38,.26,.44,.74),
 7.5:(.42,.26,.47,.74),8.0:(.45,.26,.53,.74),8.5:(.48,.25,.52,.75),9.0:(.52,.25,.48,.75),9.5:(.52,.24,.48,.76),10.0:(.53,.22,.47,.78)}
def keys(d):
    out=[]
    for t in T:
        x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
ok=keys(OM); yk=keys(YP)
c={"mediaId":5185,"level":"B","keyWord":"kindness","defaultVoice":"male",
 "taps":[{"phrase":"to clutch a paper bag","target":"the old man","voice":"male","keys":ok},
         {"phrase":"to hold a yellow umbrella","target":"the young person","voice":"male","keys":yk},
         {"phrase":"to hug the old man","target":"the young person","voice":"male","keys":yk}],
 "stillS":10.0,
 "nouns":[{"word":"an umbrella","x":.40,"y":.12,"voice":"male"},{"word":"baguettes","x":.37,"y":.64,"voice":"male"},
          {"word":"a paper bag","x":.35,"y":.86,"voice":"male"},{"word":"a raincoat","x":.80,"y":.62,"voice":"male"}],
 "question":"What is the old man holding?","answer":["He","is","clutching","a","bag","of","baguettes."],"answerVoice":"male",
 "notes":"The young person's gender is ambiguous (description says 'young person'), so the target is 'the young person' with the default (male) voice; verifier may prefer 'the young woman' + female. The two overlap all clip long (the young person stands behind and puts an arm across the old man); boxes split along a vertical line between their heads, the umbrella canopy is left out of both boxes. At 9.0-10.0 the young person's hand also touches the bag, but the old man is the one clutching it."}
json.dump(c,open('content/5185.json','w'),indent=1)
