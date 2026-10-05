import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={0.0:(.02,.17,.99,.82),0.5:(.02,.17,.99,.82),1.0:(.02,.17,.99,.81),1.5:(.07,.14,.99,.82),2.0:(.02,.15,.98,.81),
     2.5:(.02,.13,.99,.80),3.0:(.01,.12,.99,.81),3.5:(.20,0,.78,.72),4.0:(.18,0,.72,.62),4.5:(.26,0,.90,.65)}
ch={5.0:(.27,.04,.75,1.0),5.5:(.29,.04,.76,1.0),6.0:(.26,.02,.74,1.0),6.5:(.28,.02,.75,1.0),7.0:(.28,.04,.73,1.0),
    8.5:(.37,0,.55,.21),9.0:(.38,.04,.56,.30)}
men={7.5:(.10,0,1.0,1.0),8.0:(.30,0,.86,1.0),8.5:(.30,.21,.92,1.0),9.0:(.34,.30,.82,1.0)}
c={"mediaId":4904,"level":"B","keyWord":"risky","defaultVoice":"male",
 "taps":[{"phrase":"to balance on a slackline","target":"the young man","voice":"male","keys":keys(man)},
  {"phrase":"to sway against the sky","target":"the stack of chairs","voice":"male","keys":keys(ch)},
  {"phrase":"to form a human tower","target":"the group of men","voice":"male","keys":keys(men)}],
 "stillS":2.5,
 "nouns":[{"word":"a tree trunk","x":.14,"y":.45,"voice":"male"},{"word":"a slackline","x":.22,"y":.635,"voice":"male"},
  {"word":"trainers","x":.50,"y":.72,"voice":"male"},{"word":"a lawn","x":.50,"y":.92,"voice":"male"}],
 "question":"What is the group of men doing?","answer":["The","men","are","forming","a","human","tower."],"answerVoice":"male",
 "notes":"Shot 3.5-4.5 s shows the man's legs on a rusty beam (close-up), boxed as the young man. At 8.5/9.0 a small chair stack sits on top of the human tower: boxed as the stack of chairs, split from the men along the top man's shoulders. Chair stack 'sway' is subtle."}
json.dump(c,open('content/4904.json','w'),indent=1)
