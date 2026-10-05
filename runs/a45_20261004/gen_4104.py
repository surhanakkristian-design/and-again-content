import json
times=[i*0.5 for i in range(26)]
def box(b): return dict(x=round(b[0],2),y=round(b[1],2),w=round(b[2]-b[0],2),h=round(b[3]-b[1],2))
grey={0.0:(0,.40,.36,1),0.5:(0,.40,.46,1),1.0:(0,.48,.50,1),1.5:(0,.44,.50,1),2.0:(0,.42,.52,1),
5.0:(0,.28,.47,1),5.5:(0,.28,.47,1),6.0:(0,.26,.47,1),6.5:(0,.26,.47,1),7.0:(0,.28,.47,1),
10.5:(0,.26,.60,1),11.0:(0,.30,.45,1),11.5:(0,.30,.44,1),12.0:(0,.28,.40,1),12.5:(0,.28,.26,1)}
for t in (7.5,8.0,8.5,9.0,9.5,10.0): grey[t]=(0,0,1,1)
white={0.0:(.36,.24,.97,1),0.5:(.46,.22,1,1),1.0:(.50,.75,.88,1),1.5:(.50,.74,.90,1),2.0:(.52,.66,.92,1),
2.5:(0,.28,.30,1),3.0:(0,.30,.27,1),3.5:(0,.30,.28,1),4.0:(0,.28,.28,1),4.5:(0,.27,.31,1),
5.0:(.47,.13,1,1),5.5:(.47,.13,1,1),6.0:(.47,.10,1,1),6.5:(.47,.10,1,1),7.0:(.47,.13,1,1),
10.5:(.60,.12,1,1),11.0:(.45,.23,1,1),11.5:(.44,.22,1,1),12.0:(.40,.26,1,1),12.5:(.26,.25,1,1)}
dark={1.0:(.33,.05,1,.47),1.5:(.30,.05,1,.44),2.0:(.30,.05,1,.42),2.5:(.30,0,1,1),3.0:(.27,0,1,1),3.5:(.28,0,1,1),4.0:(.28,0,1,1),4.5:(.40,.07,1,1)}
def keys(d): return [dict(t=t,**box(d[t])) if t in d else dict(t=t,off=True) for t in times]
c=dict(mediaId=4104,level="A",keyWord="kiss",defaultVoice="female",
 taps=[dict(phrase="to kiss the grey bird",target="the white bird",voice="female",keys=keys(white)),
       dict(phrase="to turn red in the face",target="the grey bird",voice="female",keys=keys(grey)),
       dict(phrase="to be big and dark",target="the big dark bird",voice="female",keys=keys(dark))],
 stillS=0.0,
 nouns=[dict(word="a grey bird",x=.20,y=.70,voice="female"),dict(word="a white bird",x=.63,y=.80,voice="female"),
        dict(word="trees",x=.55,y=.08,voice="female")],
 question="What is the white bird doing?",
 answer=["She","is","giving","the","grey","bird","a","kiss."],answerVoice="female",
 notes="Animals only, evenId true -> female voice everywhere. The big dark bird gets a state phrase: every action it does (looking down, opening its beak, looking angry) another bird does too. At 1.0-2.0 s the dark bird's box covers only its head (its body lies over the white bird). Birds overlap in most shots: boxes split along a vertical line; at 12.5 s the grey bird's box is narrow (the white head leans over it). Only 3 nouns: nothing else is clear in the still; the kiss itself is not a clear place, so the key word is in the answer.")
json.dump(c,open("content/4104.json","w"),indent=1,ensure_ascii=False)
