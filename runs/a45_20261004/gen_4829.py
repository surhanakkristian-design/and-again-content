import json
# t: (blade_left, blade_top, blade_bottom, split_x, hand_top, hand_bottom)
D = {0.0:(.30,.33,.63,.55,.48,1.0),0.5:(.32,.31,.63,.56,.47,1.0),1.0:(.29,.37,.66,.55,.47,1.0),1.5:(.38,.31,.63,.63,.45,.88),
2.0:(.37,.34,.65,.56,.44,.94),2.5:(.33,.38,.68,.55,.48,.98),3.0:(.42,.38,.69,.67,.49,1.0),3.5:(.38,.34,.65,.59,.44,.86),
4.0:(.38,.58,.89,.57,.66,1.0),4.5:(.40,.35,.66,.62,.47,.93),5.0:(.37,.33,.65,.58,.47,1.0),5.5:(.33,.34,.68,.54,.43,.91),6.0:(.41,.32,.63,.61,.41,.86)}
r=lambda v:round(v,2)
sk=[];hk=[]
for t,(bl,bt,bb,sx,ht,hb) in sorted(D.items()):
    x=max(0,bl-.03); y=max(0,bt-.03); sk.append(dict(t=t,x=r(x),y=r(y),w=r(sx-x),h=r(min(1,bb+.03)-y)))
    y2=max(0,ht-.02); hk.append(dict(t=t,x=r(sx),y=r(y2),w=r(1-sx),h=r(min(1,hb+.02)-y2)))
c=dict(mediaId=4829,level="B",keyWord="chip",defaultVoice="male",
 taps=[dict(phrase="to grip a metal scraper",target="the hand",voice="male",keys=hk),
       dict(phrase="to strip old paint off wood",target="the hand",voice="male",keys=hk),
       dict(phrase="to slide under the cracked paint",target="the scraper",voice="male",keys=sk)],
 stillS=3.0,
 nouns=[dict(word="paint",x=.50,y=.15,voice="male"),dict(word="wood",x=.78,y=.39,voice="male"),
        dict(word="a scraper",x=.55,y=.53,voice="male"),dict(word="a hand",x=.84,y=.68,voice="male")],
 question="What is the hand doing?",
 answer=["It","is","stripping","old","paint","off","the","wood."],answerVoice="male",
 notes="Only a hand and a scraper are visible; hand and scraper boxes split along a vertical line at the thumb. Key word 'chip' (paint chips) is not a single placeable thing, so not used as a noun. 'wood' slot = bare patch left of the blade.")
json.dump(c,open('content/4829.json','w'),indent=1)
