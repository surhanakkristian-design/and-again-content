import json
T=[i*0.5 for i in range(21)]
def kb(t,a):
    if a is None: return dict(t=t,off=True)
    return dict(t=t,x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
def keys(b): return [kb(t,a) for t,a in zip(T,b)]
def run(mid,d):
    json.dump(d,open("content/%d.json"%mid,"w"),indent=1)
if __name__=="__main__":
    W=[(0,.18,.32,1),(0,.18,.24,1),(0,.2,.27,1),(0,.23,.30,1),(0,.18,.27,1),(0,.2,.26,1),(0,.2,.3,1),(0,.22,.3,1),(0,.18,.32,1),
       (0,.2,.26,1),(0,.22,.3,1),(0,.22,.3,1),(0,.15,.28,1),(0,.17,.26,1),(0,.18,.26,1),(0,.18,.26,1),(0,.16,.24,1),(0,.16,.23,1),
       (0,.2,.28,1),(0,.2,.28,1),(0,.18,.28,1)]
    M=[(.72,.18,1,1),(.82,.2,1,.9),(.78,.25,1,1),(.68,.22,1,1),(.72,.17,1,1),(.8,.2,1,1),(.8,.18,1,1),(.76,.2,1,1),(.72,.16,1,1),
       (.73,.2,1,1),(.72,.2,1,1),(.72,.22,1,1),(.7,.16,1,1),(.76,.2,1,1),(.76,.2,1,1),(.76,.2,1,1),(.78,.2,1,1),(.76,.2,1,1),
       (.72,.18,1,1),(.7,.2,1,1),(.68,.18,1,1)]
    S=[None]*12+[(.28,.19,.46,.33)]*9
    d=dict(mediaId=306,level="A",keyWord="flying",defaultVoice="female",
     taps=[dict(phrase="to have long braids",target="the woman",voice="female",keys=keys(W)),
           dict(phrase="to have a short beard",target="the man",voice="male",keys=keys(M)),
           dict(phrase="to shine over the clouds",target="the sun",voice="female",keys=keys(S))],
     stillS=9.0,
     nouns=[dict(word="the sun",x=0.37,y=0.26,voice="female"),
            dict(word="clouds",x=0.50,y=0.62,voice="female"),
            dict(word="a woman",x=0.15,y=0.45,voice="female"),
            dict(word="a man",x=0.85,y=0.50,voice="male")],
     question="What are they flying over?",
     answer=["They","are","flying","over","the","clouds."],answerVoice="female",
     notes="Both people do the same things (look out, smile, open their mouths), and it is unclear whose hand points and whose holds the phone, so the two person phrases are states that fit only one of them (braids / beard). Third target is the sun, visible from 6.0 s; its box is split from the woman's box at x=0.28. Hands in the middle of the window are left out of both person boxes. Key word 'flying' is not a visible noun; it is used in question and answer. defaultVoice: mixed couple, evenId true -> female.")
    run(306,d)
