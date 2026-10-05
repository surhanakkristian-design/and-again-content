import json
T=[i*0.5 for i in range(25)]
W={0.0:(.48,0,.5,.88),0.5:(.5,0,.5,.88),1.0:(.4,0,.6,.88),1.5:(.4,0,.6,.88),2.0:(.36,.04,.64,.83),2.5:(.3,.08,.7,.76),
3.0:(.25,.15,.75,.77),3.5:(.24,.13,.76,.7),4.0:(.2,.08,.8,.66),4.5:(.3,0,.7,.76),5.0:(.45,0,.55,.72),5.5:(.4,0,.6,.72),
6.0:(.25,0,.75,.65),6.5:(.2,0,.8,.63),7.0:(.28,.02,.72,.65),7.5:(.38,.02,.62,.64),8.0:(.46,.02,.54,.72),8.5:(.6,0,.4,.73),
9.0:(.5,.05,.5,.83),9.5:(.6,.1,.4,.79),10.0:(.6,.1,.4,.67),10.5:(.62,.1,.38,.65),11.0:(.63,.1,.37,.77),11.5:(.64,.1,.36,.77),12.0:(.52,.1,.46,.66)}
V={0.0:(0,.28,.47,.45),0.5:(0,.3,.49,.7),1.0:(0,.32,.39,.68),1.5:(0,.33,.39,.67),2.0:(0,.3,.35,.7),2.5:(0,.3,.29,.7),
3.0:(0,.28,.24,.45),3.5:(0,.25,.23,.35),4.0:(0,.17,.19,.35),4.5:(0,.17,.29,.25),5.0:(0,.17,.44,.2),5.5:(0,.16,.39,.2),
6.0:(0,.12,.24,.17),6.5:(0,.12,.19,.16),7.0:(0,.16,.27,.18),7.5:(0,.17,.37,.18),8.0:(0,.15,.45,.3),8.5:(0,.2,.59,.35),
9.0:(0,.22,.49,.5),9.5:(0,.22,.59,.78),10.0:(0,.25,.59,.75),10.5:(0,.27,.61,.73),11.0:(0,.3,.62,.7),11.5:(0,.3,.63,.7),12.0:(0,.3,.51,.7)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c=dict(mediaId=4786,level="B",keyWord="sparkle",defaultVoice="female",taps=[
 dict(phrase="to trace a glowing spiral",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to crouch at the water's edge",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to break on the shore",target="the waves",voice="female",keys=keys(V))],
 stillS=9.0,nouns=[dict(word="a woman",x=.84,y=.32,voice="female"),dict(word="waves",x=.2,y=.42,voice="female"),
 dict(word="a spiral",x=.35,y=.8,voice="female"),dict(word="sand",x=.75,y=.93,voice="female")],
 question="What is the woman doing?",answer="She is tracing a spiral in the sand.".split(),answerVoice="female",
 notes="Only the woman and the glowing waves are clear targets; the woman carries two phrases. Waves box kept left of the woman (split) and small in 4.0-7.5 where the waves are only a band at the top-left behind her.")
json.dump(c,open('content/4786.json','w'),indent=1)
