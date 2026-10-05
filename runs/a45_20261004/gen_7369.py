import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
Wm={0.2:(.27,.57,.42,.25),0.7:(.26,.57,.54,.25),1.2:(.26,.6,.6,.25),1.7:(.13,.5,.2,.25),2.2:(.15,.535,.32,.24),2.7:(.18,.545,.36,.25),3.2:(.25,.565,.33,.24),3.7:(.28,.575,.4,.25)}
N={0.2:(.27,.24,.41,.32),0.7:(.27,.24,.37,.32),1.2:(.25,.435,.5,.15),1.7:(.33,.38,.62,.2),2.2:(.33,.3,.46,.235),2.7:(.33,.28,.46,.265),3.2:(.3,.28,.45,.285),3.7:(.29,.24,.41,.335)}
F={0.2:(.69,.28,.25,.14),0.7:(.65,.28,.25,.14),1.2:(.6,.29,.24,.14),2.2:(.8,.3,.2,.14),2.7:(.8,.29,.2,.14),3.2:(.76,.29,.22,.14),3.7:(.71,.29,.23,.14)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=7369,level="B",keyWord="move around",defaultVoice="female",
 taps=[dict(phrase="to paddle around a whale",target="the woman",voice="female",keys=keys(Wm)),
       dict(phrase="to blow a misty spout",target="the near whale",voice="female",keys=keys(N)),
       dict(phrase="to raise its tail",target="the far whale",voice="female",keys=keys(F))],
 stillS=0.7,
 nouns=[dict(word="a paddle board",x=.6,y=.76,voice="female"),dict(word="a whale",x=.52,y=.5,voice="female"),
        dict(word="a boat",x=.65,y=.18,voice="female"),dict(word="mountains",x=.3,y=.05,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","moving","around","the","big","whale."],answerVoice="female",
 notes="Two whales: 'a whale' pill is on the big near one; no noun is on the far one. Near-whale box includes the spout but stops left of the far whale's box, so the last tenth of its body (tail end) is outside at most times; at 1.2 s the box is the body only. Far whale is under water at 1.7 s (off); at 2.2 s only its back shows. Answer uses the key word 'moving around'; 'paddling around' would be the more specific verb.")
json.dump(c,open('content/7369.json','w'),indent=1,ensure_ascii=False)
