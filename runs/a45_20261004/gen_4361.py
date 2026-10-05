import json
OFF=None
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    assert len(times)==len(boxes)
    return out
def T(n): return [i*0.5 for i in range(n)]
def tap(p,tg,v,k): return {"phrase":p,"target":tg,"voice":v,"keys":k}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
D={}
# 4361
w=[(0,.27,1,.73)]*6+[(.15,.18,.85,.82),(0,.1,.97,.9),(0,.14,1,.86),(.05,.22,.95,.78),(0,.23,.92,.77),(.06,.19,.94,.81),(0,.21,.97,.79),(0,.17,1,.83),(0,.15,1,.85),(0,.15,1,.85),(0,.14,1,.86),(0,.14,1,.86),(0,.17,1,.83),(0,.17,1,.83),(0,.17,1,.83)]
k=keys(T(21),w)
D[4361]={"mediaId":4361,"level":"B","keyWord":"shop","defaultVoice":"female",
 "taps":[tap("to show off her purchases","the woman","female",k),tap("to stroll past shop windows","the woman","female",k),tap("to ride up the escalator","the woman","female",k)],
 "stillS":2.0,
 "nouns":[noun("a skyscraper",.78,.10,"female"),noun("a traffic light",.67,.24,"female"),noun("a paper bag",.80,.52,"female"),noun("a dress",.50,.78,"female")],
 "question":"What is the woman doing?",
 "answer":["She","is","shopping","and","showing","off","her","purchases."],
 "answerVoice":"female",
 "notes":"Only one possible target (the woman), used for all three phrases; her box includes the bags she carries. Two paper bags at the still (left and right); the slot is on the right one."}
# 54
w=[(0,.52,.31,.25),(0,.5,.55,.24),(0,0,.5,1),(0,.1,.6,.9),(0,.1,.56,.9),(0,.1,.5,.9),(0,.1,.52,.9),(0,.1,.6,.9),(0,.1,.56,.9),(0,.1,.52,.9),(0,.1,.5,.9),(.03,.1,.65,.9),(0,.1,.9,.9),(.03,.12,.97,.88),(.03,.12,.97,.88),(.15,.14,.83,.86),(.22,.17,.76,.83)]
a=[(.32,0,.68,.92),(.15,0,.85,.49),(.5,.08,.48,.88),(.6,.15,.4,.8),(.56,.18,.44,.65),(.5,.18,.5,.67),(.52,.3,.48,.62),(.6,.18,.4,.7),(.56,.18,.44,.7),(.52,.18,.48,.67),(.5,.2,.5,.72),(.68,.18,.32,.74)]+[OFF]*5
kw=keys(T(17),w); ka=keys(T(17),a)
D[54]={"mediaId":54,"level":"B","keyWord":"atm","defaultVoice":"female",
 "taps":[tap("to enter her PIN code","the woman","female",kw),tap("to dispense the cash","the ATM","female",ka),tap("to count the banknotes","the woman","female",kw)],
 "stillS":2.5,
 "nouns":[noun("a lamp",.72,.13,"female"),noun("an ATM",.75,.33,"female"),noun("banknotes",.72,.70,"female"),noun("a coat",.20,.78,"female")],
 "question":"What is the woman doing?",
 "answer":["She","is","withdrawing","cash","from","an","ATM."],
 "answerVoice":"female",
 "notes":"0.0-0.5 s show only her hand with the card (woman box = hand) on a close-up of the ATM; her hands touch the machine, boxes split along a vertical line. ATM off after the move to the flower cart (6.0 s). 'an ATM' kept in capitals."}
# 540
ref=[(0,.07,.5,.93),(0,.17,.6,.83),OFF,OFF,OFF,(.32,.34,.2,.19),(.32,.34,.2,.2),(.32,.34,.2,.19),(.36,.33,.2,.19)]+[OFF]*12
st=[OFF,(.75,.33,.25,.67),(.24,.31,.6,.62),(.22,.19,.6,.74),(.3,.1,.6,.66),(.57,.15,.41,.57),(.7,.2,.3,.6),(.76,.24,.24,.52),(.77,.24,.23,.41),(.73,.27,.27,.36),(.74,.29,.26,.45),(.79,.29,.21,.45),(.66,.28,.34,.36),(.61,.33,.22,.35),(.71,.3,.29,.55),(.57,.34,.28,.53),(.52,.35,.25,.42)]+[OFF]*4
gk=[OFF]*9+[(.42,.32,.2,.18),(.4,.31,.21,.21),(.41,.31,.2,.21),(.4,.3,.22,.2),(.43,.36,.18,.15),(.45,.45,.26,.15),(.38,.48,.19,.14)]+[OFF]*5
D[540]={"mediaId":540,"level":"B","keyWord":"penalty","defaultVoice":"female",
 "taps":[tap("to award a penalty","the referee","male",keys(T(21),ref)),tap("to take a penalty kick","the striker","female",keys(T(21),st)),tap("to dive for the ball","the goalkeeper","female",keys(T(21),gk))],
 "stillS":5.0,
 "nouns":[noun("palm trees",.60,.26,"female"),noun("a goal",.28,.345,"female"),noun("a goalkeeper",.52,.43,"female"),noun("a ball",.45,.57,"female")],
 "question":"What is the striker doing?",
 "answer":["She","is","taking","a","penalty","kick."],
 "answerVoice":"female",
 "notes":"Striker = the orange player who places the ball and shoots (number 7 from behind); off from 8.5 s, lost in the celebrating crowd. Goalkeeper only boxed 4.5-7.5 s (small, far away); at 6.5 s she is half hidden behind the striker. Referee small in the background 2.5-4.0 s. Other players in orange/green are not targets."}
# 105
w=[(0,.25,.65,.75),(0,.24,.9,.76),(0,.38,1,.52),(0,.38,1,.55),(0,.57,1,.43),(0,0,.45,1),(0,0,.47,1),(0,0,.47,1),(0,0,.45,1),(0,0,1,1),(0,0,1,1),(0,.22,1,.78),OFF,OFF,OFF,OFF,(0,.17,.9,.83),(0,.17,.53,.83),(0,.15,.5,.85)]
m=[OFF]*5+[(.5,.17,.5,.52),(.5,.15,.5,.58),(.5,.15,.5,.6),(.48,.17,.52,.52)]+[OFF]*6+[(0,.07,1,.93),OFF,(.53,.12,.47,.88),(.5,.15,.5,.85)]
kw=keys(T(19),w)
D[105]={"mediaId":105,"level":"B","keyWord":"bow","defaultVoice":"female",
 "taps":[tap("to draw the bowstring","the woman","female",kw),tap("to hand over an arrow","the man","male",keys(T(19),m)),tap("to aim at the target","the woman","female",kw)],
 "stillS":0.5,
 "nouns":[noun("a bow",.64,.20,"female"),noun("an arrow",.60,.47,"female"),noun("a braid",.15,.63,"female"),noun("a tunic",.35,.78,"female")],
 "question":"What is the woman doing?",
 "answer":["She","is","shooting","an","arrow","with","a","bow."],
 "answerVoice":"female",
 "notes":"Close-ups: 1.0-1.5 s only her hand on the bow, 2.0 s only her shoulder, 4.5-5.0 s only her eye (woman box = what is visible). 2.5-4.0 s her shoulder runs under the man's chest; boxes split by a vertical line. The man hands over the arrow only in the last second."}
for i,d in D.items():
    json.dump(d,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)
