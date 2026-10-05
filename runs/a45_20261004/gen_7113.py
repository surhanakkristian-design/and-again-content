import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
wom=K([(.12,.33,.58,.48),(.12,.31,.62,.49),(.08,.29,.64,.52),(.08,.25,.66,.55),(.04,.17,.70,.53),(.04,.13,.73,.60),(.02,.09,.76,.62),(.01,.02,.80,.66)])
clock=K([(.35,.18,.18,.14),(.38,.16,.18,.14),(.35,.15,.18,.14),(.35,.08,.18,.14),(.35,.03,.18,.14),(.35,0,.18,.13),None,None])
d=dict(mediaId=7113,level="A",keyWord="fill in a form",defaultVoice="female",
taps=[dict(phrase="to fill in a form",target="the young woman",voice="female",keys=wom),
 dict(phrase="to wear a yellow jacket",target="the young woman",voice="female",keys=wom),
 dict(phrase="to show the time",target="the clock",voice="female",keys=clock)],
stillS=0.2,
nouns=[dict(word="a clock",x=.45,y=.27,voice="female"),dict(word="a jacket",x=.25,y=.58,voice="female"),
 dict(word="a form",x=.55,y=.82,voice="female"),dict(word="a machine",x=.88,y=.50,voice="female")],
question="What is the woman in yellow doing?",answer=["She","is","filling","in","a","form."],answerVoice="female",
notes="Only the woman in the yellow jacket is a clear unique target; people in the queue hold parcels (several), so two phrases share her. Clock leaves the top edge by 3.2 (off at 3.2 and 3.7). 'a machine' = the self-service machine on the right.")
json.dump(d,open("content/7113.json","w"),indent=1)
