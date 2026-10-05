import json,sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
woman=[(0.515,0.18,0.21,0.16),(0.515,0.18,0.21,0.17),(0.53,0.19,0.20,0.18),(0.56,0.19,0.19,0.19),(0.57,0.21,0.19,0.19),(0.57,0.22,0.18,0.19),(0.57,0.24,0.18,0.19),(0.57,0.26,0.18,0.19)]
piano=[(0.17,0.17,0.345,0.25),(0.17,0.17,0.345,0.25),(0.17,0.17,0.36,0.25),(0.17,0.17,0.37,0.25),(0.17,0.17,0.38,0.25),(0.17,0.17,0.38,0.25),(0.17,0.18,0.38,0.24),(0.17,0.18,0.38,0.24)]
man=[(0.60,0.51,0.18,0.14),(0.61,0.51,0.18,0.14),(0.61,0.52,0.18,0.14),(0.62,0.53,0.18,0.14),(0.62,0.54,0.18,0.14),(0.62,0.55,0.18,0.14),(0.62,0.57,0.18,0.14),(0.62,0.58,0.18,0.14)]
c=dict(mediaId=7129,level="A",keyWord="floor",defaultVoice="female",taps=[
 dict(phrase="to stand next to the piano",target="the woman",voice="female",keys=keys(woman)),
 dict(phrase="to hang in the air",target="the piano",voice="female",keys=keys(piano)),
 dict(phrase="to iron some clothes",target="the man",voice="male",keys=keys(man))],
 stillS=2.2,
 nouns=[dict(word="the sky",x=0.22,y=0.06,voice="female"),dict(word="a piano",x=0.33,y=0.29,voice="female"),dict(word="a building",x=0.50,y=0.80,voice="female")],
 question="Where is the piano?",answer=["The","piano","is","hanging","in","the","air."],answerVoice="female",
 notes="Key word 'floor' (storey) is not used as a noun pill: every level is a floor, no single clear place. 'the woman' = woman on the balcony; other small women are visible in lower flats (yoga, one at y 0.7) but none stands next to the piano. 'the man' ironing is the only one ironing. Woman's outstretched hand touches the piano's right edge at 0.2-0.7: boxes split at x 0.515. Piano moves very slightly; slow camera pull-back.")
json.dump(c,open('content/7129.json','w'),indent=1)
