import json
OFF=None
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    assert len(times)==len(boxes)
    return out
def write(mid, level, kw, dv, times, taps, still, nouns, q, a, av, notes):
    d={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":t,"voice":v,"keys":keys(times,b)} for p,t,v,b in taps],
       "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":a.split(" "),"answerVoice":av,"notes":notes}
    json.dump(d,open(f"content/{mid}.json","w"),indent=1,ensure_ascii=False)

# 517
T=[i*0.5 for i in range(13)]
car=[(.06,.48,.68,.23),(.08,.48,.71,.25),(0,.44,.46,.24),(.03,.44,.47,.23),(.03,.44,.47,.22),(0,.44,.49,.22),(0,.43,.56,.27),(.11,.46,.87,.28),(.32,.42,.68,.38),(.25,.41,.75,.40),(.22,.42,.78,.50),(.20,.41,.80,.52),(.18,.40,.82,.43)]
van=[(.12,.21,.70,.27),(.09,.22,.72,.26),(.46,.28,.48,.47),(.50,.30,.50,.47),(.50,.30,.50,.37),(.49,.29,.51,.38),(.56,.30,.44,.36),(.20,.32,.50,.14),(.06,.36,.26,.20),(.03,.38,.22,.18),(.02,.40,.20,.16),(.01,.40,.19,.15),(0,.40,.18,.14)]
write(517,"B","overtake","male",T,[
 ("to overtake a camper van","the red car","male",car),
 ("to swing in front","the red car","male",car),
 ("to fall behind the convertible","the camper van","male",van)],
 0.0,[("a camper van",.47,.34,"male"),("a convertible",.42,.60,"male"),("sand dunes",.60,.07,"male"),("a highway",.62,.86,"male")],
 "What is the red car doing?","It is overtaking a camper van.","male",
 "Car and van overlap in the picture from 1.0 to 4.0 s: boxes split along a vertical line, so part of the van's left body (1.0-3.0 s) and the car's left wing (4.0-5.5 s) lie outside their box. Two phrases share the red car (driver not used as a target: he sits inside the car box).")

# 8027
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.27,.26,.50,.54),(.35,.26,.40,.54),(.34,.23,.44,.58),(.33,.27,.45,.52),(.32,.29,.44,.50),(.32,.29,.42,.50),(.35,.30,.37,.48),(.36,.29,.37,.49)]
wom=[(.78,.30,.19,.42),(.77,.30,.20,.42),(.79,.33,.19,.39),(.79,.37,.19,.36),(.77,.38,.19,.32),(.75,.39,.19,.31),(.73,.38,.19,.30),(.74,.36,.19,.35)]
write(8027,"B","tons","male",T,[
 ("to ride a kick scooter","the man","male",man),
 ("to throw his arms up","the man","male",man),
 ("to giggle behind her hands","the woman","female",wom)],
 0.2,[("a straw hat",.44,.31,"male"),("a ceiling light",.64,.16,"male"),("a kick scooter",.50,.74,"male"),("plastic balls",.22,.87,"male")],
 "What is the man doing?","He is riding a scooter through tons of balls.","male",
 "Only two possible targets (man, woman), so the man has two phrases. The woman covers her mouth with both hands at 0.2-0.7 s only. The scooter pill sits on the deck, where loose balls lie close by.")

# 7756
bear=[(.27,.42,.31,.40),(.27,.42,.30,.40),(.25,.42,.30,.41),(.27,.42,.29,.42),(.18,.41,.36,.43),(.17,.40,.35,.46),(.17,.40,.36,.46),(.19,.40,.40,.46)]
rac=[(.58,.70,.40,.21),(.57,.69,.41,.22),(.56,.70,.42,.23),(.56,.70,.42,.23),(.55,.68,.40,.25),(.53,.65,.32,.27),(.55,.57,.34,.33),(.60,.57,.33,.34)]
carb=[(.30,.24,.70,.18),(.30,.24,.70,.18),(.28,.24,.72,.18),(.28,.24,.72,.18),(.28,.23,.72,.18),(.28,.23,.72,.17),(.28,.23,.72,.17),(.30,.23,.70,.17)]
write(7756,"B","automotive","female",T,[
 ("to fit a front wheel","the bear","female",bear),
 ("to clutch a spanner","the raccoon","female",rac),
 ("to rest on a lift","the red car","female",carb)],
 3.2,[("a bear",.33,.60,"female"),("a raccoon",.70,.75,"female"),("tyres",.38,.30,"female"),("a sports car",.75,.39,"female")],
 "What is the bear doing?","It is fitting a wheel onto a sports car.","female",
 "The car box holds the body only (above the bear's head): the front wheel is in the bear's hands and would overlap the bear box. 'to rest on a lift' is a state, chosen to get three different targets. Key word 'automotive' is an adjective and is not used.")

# 733
T=[i*0.5 for i in range(19)]
w=[(0,.26,.33,.24),(0,.35,.37,.27),(.04,.17,.61,.68),(0,.16,.73,.69),OFF,OFF,OFF,(0,.45,.33,.17),OFF,(0,.30,.20,.53),(.15,.32,.29,.53),(.22,.33,.27,.54),(.23,.33,.26,.54),(.23,.33,.26,.54),(.22,.33,.24,.55),(.17,.32,.28,.57),(.16,.34,.29,.57),(.16,.35,.29,.59),(.15,.35,.30,.61)]
m=[(.66,.22,.34,.30),(.63,.29,.37,.33),(.80,.86,.20,.14),(.80,.86,.20,.14),(.30,.15,.70,.62),(.29,.12,.71,.65),(.29,.13,.71,.64),(.70,.38,.30,.24),(.82,.38,.18,.30),(.80,.30,.20,.50),(.50,.33,.44,.52),(.49,.33,.37,.55),(.49,.33,.38,.54),(.49,.33,.38,.54),(.46,.33,.42,.56),(.45,.33,.44,.57),(.45,.34,.46,.58),(.45,.35,.48,.59),(.45,.35,.49,.62)]
b=[(0,0,.45,.25),(0,0,.45,.28),OFF,OFF,OFF,OFF,OFF,(.05,.08,.42,.36),(.07,.10,.39,.30),(.21,.15,.26,.27),(.09,.18,.37,.14),(.04,.25,.18,.30),(.05,.25,.18,.30),(.05,.25,.18,.30),(.04,.25,.18,.30),(.08,.18,.38,.14),(.07,.14,.39,.20),(.08,.08,.38,.27),(.06,.06,.40,.29)]
write(733,"B","state","male",T,[
 ("to hold up a brass stamp","the woman in the teal sash","female",w),
 ("to frown at the document","the grey-haired man","male",m),
 ("to display a white circle","the teal banner","male",b)],
 8.5,[("a chandelier",.50,.06,"male"),("a circle",.28,.28,"male"),("a triangle",.72,.30,"male"),("a marble floor",.50,.94,"male")],
 "What are the two leaders doing?","They are shaking hands in front of their banners.","male",
 "Clip with cuts. 0.0-0.5 s and 3.5 s show only the leaders' hands/arms with the stamps: boxed as the woman (brass stamp, left) and the man (dark stamp, right); 1.0-1.5 s the man's hand at the bottom right. Woman off at 4.0 s (only her arm at the left edge, next to a delegate woman). From 5.0 s the teal banner is partly behind the woman: its box is only the visible strip above her head (5.0, 7.5-9.0 s) or left of her (5.5-7.0 s); the circle is hidden or half hidden 5.0-7.5 s. Both leaders press a stamp and shake hands, so the phrases use what only one does (she lifts the brass stamp at 1.5 s, he frowns at 2.0-2.5 s). The model answer describes the handshake (5.5-6.5 s); key word 'state' is not visible and not used.")
