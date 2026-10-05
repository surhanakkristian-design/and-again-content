import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if t in d else dict(t=t, off=True) for t in T]
woman={4.0:(.78,.57,.22,.43),4.5:(.50,.55,.50,.45),5.0:(.45,.66,.38,.34),5.5:(.34,.69,.35,.31),6.0:(.26,.57,.34,.43),6.5:(.24,.60,.33,.40),
7.0:(.14,.73,.39,.27),7.5:(.12,.74,.40,.26),8.0:(.12,.65,.40,.35),8.5:(.12,.66,.40,.34),9.0:(.12,.66,.38,.34),9.5:(.12,.66,.38,.34),10.0:(.12,.66,.40,.34)}
man={5.0:(.84,.60,.16,.40),5.5:(.70,.65,.30,.35),6.0:(.61,.55,.32,.45),6.5:(.58,.56,.30,.44),7.0:(.54,.69,.29,.31),7.5:(.53,.71,.29,.29),
8.0:(.52,.61,.27,.39),8.5:(.53,.63,.30,.37),9.0:(.50,.63,.35,.37),9.5:(.50,.63,.48,.37),10.0:(.52,.63,.38,.37)}
pc={5.0:(.88,.455),5.5:(.77,.44),6.0:(.69,.425),6.5:(.66,.41),7.0:(.655,.40),7.5:(.66,.39),8.0:(.66,.375),8.5:(.665,.365),9.0:(.67,.36),9.5:(.675,.35),10.0:(.68,.33)}
plane={t:(round(min(x-.09,.82),2),round(y-.07,2),.18,.14) for t,(x,y) in pc.items()}
c=dict(mediaId=884,level="A",keyWord="world",defaultVoice="female",taps=[
 dict(phrase="to point at the city",target="the woman",voice="female",keys=keys(woman)),
 dict(phrase="to open his arms wide",target="the man",voice="male",keys=keys(man)),
 dict(phrase="to fly high in the sky",target="the plane",voice="female",keys=keys(plane))],
 stillS=8.0,
 nouns=[dict(word="the sky",x=.30,y=.15,voice="female"),dict(word="a plane",x=.66,y=.37,voice="female"),
        dict(word="a man",x=.66,y=.74,voice="male"),dict(word="a woman",x=.36,y=.86,voice="female")],
 question="What are the two people doing?",
 answer=["They","are","looking","at","the","city."],answerVoice="female",
 notes="Key word 'world' is not a visible noun, so it is not used. Plane: a tiny light speck crosses the sky at 1.0-3.0 s (not identifiable) - keys off there; a bird flies low at the right edge in the last frame (10.0 s) only, phrase says 'high in the sky' to keep it on the plane. Man opens both arms at 9.0-10.0 s (then one arm goes around the woman); the woman raises only one arm to point (4.5-6.0 s). Couple stand close: boxes split along the line between them; at 9.0 s the man's left hand reaches into the woman's box.")
json.dump(c,open('content/884.json','w'),indent=1,ensure_ascii=False)
