import json
T=[i*0.5 for i in range(19)]
S={0.0:(.18,.13,.60,.76),0.5:(.22,.06,.55,.65),1.0:(.26,.14,.55,.86),2.0:(0,.23,1,.77),2.5:(.30,.27,.42,.56),
   3.0:(.28,.34,.40,.48),3.5:(.04,.38,.94,.58),4.0:(0,.37,.85,.63),4.5:(.44,0,.56,.56),6.5:(0,.45,.75,.55),
   7.0:(0,.50,1,.30),7.5:(0,.17,1,.78),8.0:(.26,0,.55,1),8.5:(.33,.25,.36,.63),9.0:(.29,.36,.32,.50)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4929,level="A",keyWord="grade",defaultVoice="male",
 taps=[dict(phrase="to run to class",target="the student",voice="male",keys=keys(S)),
       dict(phrase="to write in a notebook",target="the student",voice="male",keys=keys(S)),
       dict(phrase="to get a good grade",target="the student",voice="male",keys=keys(S))],
 stillS=7.5,
 nouns=[dict(word="a hoodie",x=.50,y=.48,voice="male"),dict(word="a grade",x=.42,y=.64,voice="male"),
        dict(word="a desk",x=.50,y=.92,voice="male")],
 question="Where is the student running?",
 answer=["He","is","running","to","class."],answerVoice="male",
 notes="All three phrases use the student (the lecturer at 2.5 s is tiny; classmates at 8.0-9.0 s also raise their fists, so no fist phrase). Student off at 1.5 s (frisbee shot) and 5.0-6.0 s (highlighter, coffee, books close-ups). 4.5 s and 6.5-7.0 s show only his hands (boxes on hands/arm; 7.0 s box is the band with both hands and the paper between them). Writing is only in the 4.5 s close-up. 'a grade' pill sits on the red A+ on the paper at 7.5 s. Frames differ from the description (no A mark close-up at the end; the A+ paper is shown at 7.0-7.5 s).")
json.dump(c,open('content/4929.json','w'),indent=1,ensure_ascii=False)
