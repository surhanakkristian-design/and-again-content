import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
split=[.50,.50,.50,.52,.50,.50,.50,.50]
wtop=[(.03,.29),(.03,.30),(.03,.31),(.03,.32),(.01,.35),(.01,.36),(0,.37),(0,.37)]
wom=K([(x,y,round(s-x,2),round(.99-y,2)) for (x,y),s in zip(wtop,split)])
film=K([(.50,.39,.24,.38),(.50,.37,.25,.37),(.50,.34,.24,.39),(.52,.33,.26,.38),(.50,.30,.29,.41),(.50,.29,.29,.43),(.50,.30,.30,.44),(.50,.31,.30,.43)])
meter=K([(.82,.42,.18,.15)]*8)
d=dict(mediaId=7114,level="B",keyWord="film",defaultVoice="female",
taps=[dict(phrase="to raise a metal frame",target="the woman in yellow",voice="female",keys=wom),
 dict(phrase="to shimmer with rainbow colours",target="the soap film",voice="female",keys=film),
 dict(phrase="to measure the wind speed",target="the wind meter",voice="female",keys=meter)],
stillS=0.7,
nouns=[dict(word="skyscrapers",x=.30,y=.31,voice="female"),dict(word="a water tower",x=.76,y=.36,voice="female"),
 dict(word="a soap film",x=.62,y=.50,voice="female"),dict(word="a trough",x=.65,y=.85,voice="female")],
question="What is the woman in yellow doing?",answer=["She","is","raising","a","large","metal","frame."],answerVoice="female",
notes="Woman and soap film overlap (her hands hold the frame): boxes split at x=0.50 (0.52 at 1.7), so her hands are partly in the film box. People behind the film (blonde woman, young man) both reach up, so neither is a target. Wind meter is held at the right edge; it slides almost out of frame at 3.2-3.7 (only a sliver + hand).")
json.dump(d,open("content/7114.json","w"),indent=1)
