import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
man={0.0:(.33,0,.72,.29),0.5:(.25,0,.72,.32),1.0:(.22,0,.7,.33),1.5:(.25,0,.65,.31),2.0:(.32,0,.65,.27),2.5:(.38,.02,.64,.25),
 3.0:(.5,.04,.77,.24),3.5:(.44,.07,.72,.27),4.0:(.27,.05,.52,.29),4.5:(.19,0,.52,.3),5.0:(.2,0,.6,.34),5.5:(.18,0,.53,.34),
 6.0:(.2,0,.51,.27),6.5:(.24,0,.5,.24),7.0:(.25,.01,.48,.21),7.5:(.28,.02,.49,.21),8.0:(.29,.04,.5,.24),8.5:(.3,.07,.5,.27),
 9.0:(.3,.12,.5,.31),9.5:(.31,.14,.52,.33),10.0:(.31,.18,.52,.36)}
mow={0.0:(.33,.29,.73,.57),0.5:(.28,.32,.88,.82),1.0:(.22,.33,.95,1),1.5:(.25,.31,.75,.67),2.0:(.33,.27,.67,.51),2.5:(.38,.25,.64,.43),
 3.0:(.39,.24,.74,.4),3.5:(.3,.27,.65,.41),4.0:(.23,.29,.48,.44),4.5:(.19,.3,.53,.52),5.0:(.08,.34,.6,.78),5.5:(.06,.34,.6,.79),
 6.0:(.19,.27,.51,.51),6.5:(.24,.24,.5,.41),7.0:(.27,.21,.47,.37),7.5:(.29,.21,.48,.35),8.0:(.29,.24,.49,.38),8.5:(.29,.27,.49,.41),
 9.0:(.29,.31,.49,.45),9.5:(.3,.33,.5,.47),10.0:(.3,.36,.5,.5)}
spr={0.0:(.73,.08,1,.25),0.5:(.75,.08,1,.24),1.0:(.72,.08,1,.24),1.5:(.72,.07,1,.24),2.0:(.68,.11,1,.26),2.5:(.7,.13,1,.29),
 3.0:(.78,.14,1,.3),3.5:(.73,.14,1,.3),4.0:(.7,.16,1,.32),4.5:(.75,.15,1,.3),5.0:(.79,.13,1,.3),5.5:(.6,.08,1,.3),
 6.0:(.52,.06,1,.27),6.5:(.52,.06,1,.26),7.0:(.5,.06,.97,.27),7.5:(.8,.17,.98,.31),8.0:(.8,.19,.98,.33),8.5:(.8,.21,.98,.35),
 9.0:(.78,.26,.96,.4),9.5:(.78,.28,.96,.42),10.0:(.78,.31,.96,.45)}
c={"mediaId":5093,"level":"B","keyWord":"overgrown","defaultVoice":"male",
 "taps":[
  {"phrase":"to push a lawn mower","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to cut through long grass","target":"the lawn mower","voice":"male","keys":keys(mow)},
  {"phrase":"to spray the mown lawn","target":"the sprinkler","voice":"male","keys":keys(spr)}],
 "stillS":6.0,
 "nouns":[{"word":"a lawn mower","x":0.35,"y":0.38,"voice":"male"},
          {"word":"a hedge","x":0.72,"y":0.05,"voice":"male"},
          {"word":"a sprinkler","x":0.86,"y":0.22,"voice":"male"},
          {"word":"tall grass","x":0.17,"y":0.75,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","mowing","the","overgrown","lawn."],"answerVoice":"male",
 "notes":"Man and mower boxes are split horizontally where the mower body starts (his legs and hands on the handle sit near the line). The sprinkler is not in the description: at 0.0-5.0 only its water jet is visible at the top right (box on the jet), at 5.5-7.0 head + jet, at 7.5-10.0 only a small post far right (head at about x .87-.9) and no visible jet - check it is the sprinkler. The man wipes his forehead at 8.0-8.5 (not used). 'tall grass' pill is on the unmown strip at the left."}
json.dump(c,open('content/5093.json','w'),indent=1)
