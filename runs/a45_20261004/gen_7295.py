import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else dict(t=t,off=True) for t,b in zip(T,boxes)]
man=K([(0.20,0.34,0.36,0.26),(0.20,0.33,0.36,0.27),(0.19,0.31,0.36,0.30),(0.13,0.32,0.41,0.30),
       (0.0,0.29,0.47,0.32),(0.08,0.19,0.43,0.42),(0.07,0.28,0.48,0.33),(0.07,0.30,0.48,0.32)])
ly=[0.60,0.60,0.61,0.62,0.61,0.61,0.61,0.62]
link=K([(0.36,y,0.27,0.15) for y in ly])
wave=K([(0.18,0.19,0.82,0.15),(0.18,0.17,0.82,0.16),(0.10,0.12,0.90,0.19),(0.10,0.16,0.90,0.16),None,None,None,None])
c=dict(mediaId=7295,level="B",keyWord="link",defaultVoice="male",
 taps=[dict(phrase="to swing a heavy sledgehammer",target="the man with the hammer",voice="male",keys=man),
       dict(phrase="to connect the rusty links",target="the steel link",voice="male",keys=link),
       dict(phrase="to crash behind the ship",target="the huge wave",voice="male",keys=wave)],
 stillS=0.7,
 nouns=[dict(word="the northern lights",x=0.30,y=0.09,voice="male"),
        dict(word="a wave",x=0.55,y=0.26,voice="male"),
        dict(word="a torch",x=0.77,y=0.50,voice="male"),
        dict(word="a link",x=0.49,y=0.66,voice="male")],
 question="What is the man hammering?",
 answer=["He","is","hammering","the","steel","link."],
 answerVoice="male",
 notes="Man box split from the link box along y~0.60-0.62 (his legs are behind the chain, so legs are cut). Wave counted visible 0.2-1.7 s; from 2.2 s only mist, so off. 'a chain' left out so 'a link' cannot be confused with the rusty chain links.")
json.dump(c,open('content/7295.json','w'),indent=1)
