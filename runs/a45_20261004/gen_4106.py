import json
times=[i*0.5 for i in range(19)]
def box(b): return dict(x=round(b[0],2),y=round(b[1],2),w=round(b[2]-b[0],2),h=round(b[3]-b[1],2))
dog={0.0:(.42,.47,.80,.70),0.5:(.38,.47,.80,.68),1.0:(.42,.47,.80,.70),1.5:(.40,.43,.82,.70),2.0:(.35,.22,.82,.72),2.5:(.40,.38,.82,.73),
3.0:(.38,.41,.82,.74),3.5:(.36,.46,.82,.74),4.0:(.36,.47,.82,.73),4.5:(.36,.45,.82,.73),5.0:(.38,.46,.82,.74),5.5:(.38,.47,.82,.73),
6.0:(.40,.47,.86,.73),6.5:(.40,.46,.88,.73),7.0:(.45,.44,.93,.73),7.5:(.50,.48,1,.70),8.0:(.53,.41,1,.72),8.5:(.53,.40,.90,.68),9.0:(.45,.47,.92,.74)}
man={0.0:(0,.10,1,.47),0.5:(0,.10,1,.47),1.0:(0,.10,1,.47),1.5:(0,.08,1,.43),2.0:(0,.02,.35,.65),2.5:(0,0,1,.38),
3.0:(0,.02,1,.41),3.5:(0,.02,1,.46),4.0:(0,.02,1,.47),4.5:(0,.02,1,.45),5.0:(0,.02,1,.46),5.5:(0,.02,1,.47),
6.0:(0,.04,1,.47),6.5:(0,.05,1,.46),7.0:(0,.08,1,.44),7.5:(0,.10,1,.48),8.0:(0,.12,.53,.72),8.5:(0,.15,.53,.72),9.0:(0,.18,1,.47)}
def keys(d): return [dict(t=t,**box(d[t])) if t in d else dict(t=t,off=True) for t in times]
c=dict(mediaId=4106,level="A",keyWord="hungry",defaultVoice="male",
 taps=[dict(phrase="to hold a fork",target="the man",voice="male",keys=keys(man)),
       dict(phrase="to eat his pasta",target="the dog",voice="male",keys=keys(dog)),
       dict(phrase="to laugh at the dog",target="the man",voice="male",keys=keys(man))],
 stillS=4.5,
 nouns=[dict(word="a man",x=.52,y=.28,voice="male"),dict(word="a dog",x=.58,y=.52,voice="male"),
        dict(word="pasta",x=.50,y=.80,voice="male"),dict(word="a table",x=.50,y=.94,voice="male")],
 question="What is the dog doing?",
 answer=["The","hungry","dog","is","eating","his","pasta."],answerVoice="male",
 notes="The dog sits in front of the man, so the man's box is the part above the dog (head, shoulders, raised arm) and the dog's box the part below; at 2.0 s the dog stretches up over the man's face, the man's box is his raised arm on the left; at 8.0-8.5 s the split is vertical. 'pasta' slot is on the plate (pasta is also on the fork). 'his' in the phrase and answer = the man's pasta.")
json.dump(c,open("content/4106.json","w"),indent=1,ensure_ascii=False)
