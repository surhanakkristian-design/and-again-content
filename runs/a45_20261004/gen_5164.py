import json
T=[i*0.5 for i in range(25)]
wo={0.0:(0,.26,.78,.74),0.5:(0,.27,.86,.73),1.0:(0,.15,.80,.85),1.5:(0,.12,.77,.88),2.0:(0,.17,.73,.83),
 2.5:(0,.47,.83,.53),3.0:(0,.25,.73,.75),3.5:(0,.25,.76,.75),4.0:(0,.52,.45,.48),4.5:(0,.47,.33,.53),
 5.0:(0,.45,.25,.55),5.5:(0,.38,.53,.62),6.0:(0,.33,.62,.67),
 10.0:(.34,.82,.60,.18),10.5:(.22,.40,.78,.60),11.0:(.28,.33,.72,.67),11.5:(.18,.33,.82,.67),12.0:(.18,.34,.82,.66)}
cr={8.5:(0,.40,1,.60),9.0:(0,.40,1,.60),9.5:(0,.40,1,.60),10.0:(0,.36,1,.45),
 10.5:(0,.36,.22,.36),11.0:(0,.30,.28,.36),11.5:(0,.32,.18,.34),12.0:(0,.28,.18,.28)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
wk=keys(wo); ck=keys(cr)
c={"mediaId":5164,"level":"B","keyWord":"campaign","defaultVoice":"female",
 "taps":[{"phrase":"to smooth down a poster","target":"the young woman","voice":"female","keys":wk},
         {"phrase":"to wave campaign placards","target":"the crowd","voice":"female","keys":ck},
         {"phrase":"to grin with delight","target":"the young woman","voice":"female","keys":wk}],
 "stillS":7.0,
 "nouns":[{"word":"spotlights","x":.55,"y":.12,"voice":"female"},{"word":"a screen","x":.55,"y":.36,"voice":"female"},
          {"word":"a lectern","x":.22,"y":.56,"voice":"female"},{"word":"an audience","x":.32,"y":.86,"voice":"female"}],
 "question":"What is the woman in red brushing?","answer":["She","is","brushing","a","campaign","poster."],"answerVoice":"female",
 "notes":"Three shots: wall (young woman brushing posters), debate (bald man vs grey-haired woman, no tap target there: their actions are identical), rally (crowd with placards, then the same young woman in the red shirt cheering in close-up). From 10.5 s the woman fills the lower frame, so the crowd box is the strip of placards to her left (her shirt edge at bottom-left falls in no box). 'to grin with delight' also fits her smile at the wall (5.5-6.0 s) - same target, fine. The answer verb is 'brushing' (brush over the poster); the description says she pastes posters."}
json.dump(c,open('content/5164.json','w'),indent=1)
