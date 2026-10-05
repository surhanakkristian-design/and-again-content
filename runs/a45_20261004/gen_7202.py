import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(d): return [dict(t=t,x=round(d[t][0],2),y=round(d[t][1],2),w=round(d[t][2]-d[t][0],2),h=round(d[t][3]-d[t][1],2)) for t in T]
man={0.2:(.37,.18,.79,.92),0.7:(.32,.22,.79,.94),1.2:(.30,.27,.79,.97),1.7:(.30,.23,.79,.97),2.2:(.34,.19,.79,.97),2.7:(.31,.19,.78,.97),3.2:(.27,.18,.78,.99),3.7:(.25,.17,.77,.99)}
old={0.2:(.80,.33,.99,.62),0.7:(.80,.33,.99,.62),1.2:(.80,.33,1.0,.62),1.7:(.80,.32,1.0,.61),2.2:(.80,.32,1.0,.64),2.7:(.79,.33,1.0,.66),3.2:(.79,.34,1.0,.67),3.7:(.78,.34,1.0,.69)}
cows={0.2:(.0,.38,.36,.72),0.7:(.0,.38,.31,.74),1.2:(.0,.38,.29,.74),1.7:(.0,.38,.29,.74),2.2:(.0,.37,.33,.76),2.7:(.0,.38,.30,.76),3.2:(.0,.38,.26,.76),3.7:(.0,.38,.24,.76)}
c=dict(mediaId=7202,level="A",keyWord="hand",defaultVoice="male",
 taps=[dict(phrase="to throw hay on the ground",target="the young man",voice="male",keys=k(man)),
       dict(phrase="to hold a cup",target="the old man",voice="male",keys=k(old)),
       dict(phrase="to look over the fence",target="the cows",voice="male",keys=k(cows))],
 stillS=2.2,
 nouns=[dict(word="a barn",x=.82,y=.20,voice="male"),dict(word="cows",x=.15,y=.46,voice="male"),
        dict(word="a hand",x=.67,y=.56,voice="male"),dict(word="a fence",x=.22,y=.70,voice="male")],
 question="What is the old man holding?",answer=["He","is","holding","a","cup."],answerVoice="male",
 notes="Young man's box is cut at x .79 so it does not touch the old man's box; his raised hand with the hay at 0.2 s reaches .85. 'a hand' pill is on the young man's gloved right hand. Thrown hay is a bale of straw; 'hay' kept for level A.")
json.dump(c,open('content/7202.json','w'),indent=1)
