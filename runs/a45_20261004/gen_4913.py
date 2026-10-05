import json
T=[round(i*0.5,1) for i in range(21)]
D={0.0:(0,.2,.5,.8),0.5:(0,.21,.52,.79),1.0:(0,.2,.5,.8),1.5:(0,.2,.52,.8),2.0:(0,.22,.46,.78),2.5:(0,.22,.49,.78),
4.5:(0,0,.47,1),5.0:(0,.08,.49,.92),5.5:(0,.15,.47,.85),
6.0:(.02,.1,.78,.27),6.5:(.15,.21,.72,.28),7.0:(.25,.2,.55,.17),7.5:(.24,.2,.55,.15),8.0:(.3,.21,.4,.14),
8.5:(.36,.22,.3,.14),9.0:(.35,.23,.33,.14),9.5:(.1,.3,.6,.32),10.0:(.22,.33,.4,.27)}
J={0.0:(.51,.2,.49,.8),0.5:(.53,.21,.47,.79),1.0:(.55,.22,.45,.78),1.5:(.53,.2,.47,.8),2.0:(.5,.22,.5,.78),2.5:(.51,.22,.49,.78),
4.5:(.48,0,.52,1),5.0:(.5,.08,.5,.92),5.5:(.48,.15,.52,.85),
6.0:(.2,.38,.72,.62),6.5:(.25,.5,.5,.5),7.0:(.15,.38,.55,.62),7.5:(.12,.36,.6,.62),8.0:(.2,.36,.55,.62),
8.5:(.27,.37,.5,.6),9.0:(.27,.38,.5,.6),9.5:(.3,.63,.45,.33),10.0:(.22,.61,.36,.2)}
def keys(b):
    return [dict(t=t,x=b[t][0],y=b[t][1],w=b[t][2],h=b[t][3]) if t in b else dict(t=t,off=True) for t in T]
kd,kj=keys(D),keys(J)
c=dict(mediaId=4913,level="B",keyWord="bracelet",defaultVoice="female",
taps=[dict(phrase="to give her friend a piggyback",target="the woman in jeans",voice="female",keys=kj),
      dict(phrase="to ride on her friend's back",target="the woman in the dress",voice="female",keys=kd),
      dict(phrase="to have a blonde ponytail",target="the woman in the dress",voice="female",keys=kd)],
stillS=5.5,
nouns=[dict(word="the sky",x=.35,y=.06,voice="female"),dict(word="bracelets",x=.48,y=.43,voice="female"),
       dict(word="a crop top",x=.8,y=.72,voice="female"),dict(word="a summer dress",x=.18,y=.84,voice="female")],
question="What is the woman in jeans doing?",
answer=["She","is","giving","her","friend","a","piggyback."],answerVoice="female",
notes="3.0-4.0 are hand close-ups (bracelet being fastened) where the owner of each hand is unclear: off for both. During the piggyback (6.0-10.0) the two women overlap, so the rider's box is her head/shoulders above the split line and the carrier's box everything below; the rider's hanging legs fall in the carrier's box. Close-ups 4.5-5.5 split at the middle between the two raised arms. 'bracelets' = the two bracelets side by side.")
json.dump(c,open('content/4913.json','w'),indent=1)
