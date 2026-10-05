import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def tap(p,tg,v,b): return {"phrase":p,"target":tg,"voice":v,"keys":keys(b)}
def nn(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 7813
dr=[(.27,.24,.69,.74),(.15,.43,.82,.74),(.15,.44,.85,.74),(.14,.40,.87,.74),(.14,.30,.87,.74),(.18,.26,.93,.74),(.15,.24,.86,.78),(.15,.22,.92,.78)]
pk=[(0,.38,.19,.65),(0,.37,.15,.63),(0,.38,.15,.65),(0,.38,.14,.64),(0,.31,.14,.62),(0,.31,.15,.62),(0,.33,.14,.62),(0,.32,.13,.62)]
pu=[(.12,.84,.88,1.0)]*8
save({"mediaId":7813,"level":"B","keyWord":"duo","defaultVoice":"male",
 "taps":[tap("to drum on upturned buckets","the two drummers","male",dr),
         tap("to wear a pink jumper","the woman in pink","female",pk),
         tap("to reflect the cloudy sky","the puddle","male",pu)],
 "stillS":2.7,
 "nouns":[nn("umbrellas",.90,.33,"male"),nn("a fountain",.5,.44,"male"),nn("buckets",.25,.75,"male"),nn("a puddle",.5,.91,"male")],
 "question":"What is the duo doing?",
 "answer":["The","duo","is","drumming","on","blue","buckets."],
 "answerVoice":"male",
 "notes":"The two drummers (a man and a woman) do exactly the same things, so no phrase fits only one of them: they are ONE joint target 'the two drummers' with one box around both. Pink-jumper woman gets a state phrase (everyone in the crowd cheers/claps, no action is hers alone); her box is cut at the drummers' left edge where the man's foot comes close. 'buckets' pill is on the left bucket group (a second, matching group stands on the right). Key word 'duo' not used as a noun slot (no single clear place), it is in the question and answer. Mixed duo, evenId false -> default male."})

# 7997
st=[(.44,.37,.58,.81),(.44,.37,.585,.81),(.42,.38,.565,.81),(.425,.38,.565,.81),(.43,.38,.58,.81),(.425,.38,.59,.81),(.40,.38,.60,.82),(.40,.38,.61,.82)]
mn=[(.22,.42,.44,.71),(.15,.45,.44,.71),(.22,.49,.42,.71),(.22,.49,.425,.71),(.22,.49,.43,.71),(.21,.49,.425,.71),(.20,.49,.40,.72),(.21,.49,.40,.72)]
wd=[(.58,.44,.79,.71),(.585,.45,.87,.71),(.565,.46,.79,.72),(.565,.46,.79,.72),(.58,.45,.79,.72),(.59,.45,.80,.72),(.60,.45,.80,.72),(.61,.45,.80,.72)]
save({"mediaId":7997,"level":"B","keyWord":"star","defaultVoice":"female",
 "taps":[tap("to star in a show","the woman in gold","female",st),
         tap("to kneel on one knee","the man","male",mn),
         tap("to dance in high heels","the woman in black","female",wd)],
 "stillS":3.7,
 "nouns":[nn("curtains",.5,.14,"female"),nn("a spotlight",.5,.25,"female"),nn("a gown",.5,.62,"female"),nn("footlights",.5,.84,"female")],
 "question":"What is the woman in gold doing?",
 "answer":["She","is","starring","in","a","show."],
 "answerVoice":"female",
 "notes":"The star's raised arms (0.2-2.2 s) reach over the two dancers; her box is cut to head+body so it does not overlap the dancers' boxes. The man dances at 0.2-0.7 s and kneels from 1.2 s. 'footlights' pill on the middle one of three."})

# 7748
du=[(.26,.22,.58,.68),(.26,.21,.60,.69),(.22,.28,.53,.76),(.09,.44,.48,.92),(.07,.39,.41,.93),(.07,.39,.48,.94),(.13,.31,.55,.86),(.15,.22,.59,.80)]
gr=[(.66,.44,.93,.80),(.66,.44,.93,.80),(.66,.44,.94,.81),(.68,.44,.95,.825),(.68,.44,.96,.845),(.69,.44,.98,.85),(.70,.44,1.0,.86),(.71,.44,1.0,.87)]
sl=[(.54,.80,.87,.93),(.54,.80,.89,.93),(.54,.81,.89,.95),(.54,.825,.90,.97),(.54,.845,.89,.98),(.54,.85,.92,.99),(.56,.86,.91,1.0),(.60,.87,.92,1.0)]
save({"mediaId":7748,"level":"B","keyWord":"around the clock","defaultVoice":"female",
 "taps":[tap("to paint a dragon sculpture","the woman in dungarees","female",du),
         tap("to yawn over her coffee","the woman in green","female",gr),
         tap("to doze on a cushion","the man on the floor","male",sl)],
 "stillS":2.2,
 "nouns":[nn("a dragon",.62,.21,"female"),nn("paint tins",.46,.84,"female"),nn("a pizza box",.22,.93,"female"),nn("a blanket",.87,.95,"female")],
 "question":"What is the woman in dungarees doing?",
 "answer":["She","is","painting","a","dragon","sculpture."],
 "answerVoice":"female",
 "notes":"Key phrase 'around the clock' cannot be shown as a noun or tapped; not used. Woman in green: head tilted back, mouth open, cup in her hand = yawning (could be read as drinking). A second sleeper (grey hoodie, far left) lies on the floor without a cushion, so 'to doze on a cushion' fits only the man bottom right on the blue cushion; target name 'the man on the floor' - the left sleeper's gender is unclear. The man in black behind the dragon is not a target."})

# 7450
full=(0,0,1,1)
po=[full,full,full,(.05,0,1,1),(.12,0,1,1),(.19,.02,1,1),(.33,.12,1,1),(.34,.20,.95,1)]
bk=[None,None,None,None,(0,.03,.12,.31),(0,.10,.19,.40),(.08,.19,.30,.46),(.11,.21,.32,.48)]
save({"mediaId":7450,"level":"B","keyWord":"potter","defaultVoice":"female",
 "taps":[tap("to shape a tall vase","the potter in front","female",po),
         tap("to reach inside the vase","the potter in front","female",po),
         tap("to work in the background","the person at the back","female",bk)],
 "stillS":3.7,
 "nouns":[nn("a kiln",.40,.24,"female"),nn("a potter",.74,.43,"female"),nn("a vase",.43,.58,"female"),nn("a sponge",.20,.78,"female")],
 "question":"What is the potter in front doing?",
 "answer":["She","is","shaping","a","tall","clay","vase."],
 "answerVoice":"female",
 "notes":"Close-up 0.2-1.2 s: the potter's arms, hands, face and knee and the vase fill the picture, so her box is the whole frame there. The vase and the kiln are not tap targets: the vase cannot be separated from her arms, the kiln overlaps her raised elbow. Person at the back: out of focus / hardly visible until 1.7 s (off), narrow box at 2.2 s because the potter's elbow is next to it; gender unclear -> default voice. 'a potter' pill is on the front potter; a second potter sits at the back with no noun."})
