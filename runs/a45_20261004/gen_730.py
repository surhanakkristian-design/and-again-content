import json
OFF='off'
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({'t':t,'off':True} if b is None else {'t':t,'x':b[0],'y':b[1],'w':b[2],'h':b[3]})
    return out
def T(n,step=0.5,start=0.0): return [round(start+i*step,1) for i in range(n)]
def write(mid, level, kw, dv, taps, times, still, nouns, q, a, av, notes):
    c={'mediaId':mid,'level':level,'keyWord':kw,'defaultVoice':dv,
       'taps':[{'phrase':p,'target':tg,'voice':v,'keys':keys(times,d)} for p,tg,v,d in taps],
       'stillS':still,'nouns':[{'word':w,'x':x,'y':y,'voice':v} for w,x,y,v in nouns],
       'question':q,'answer':a,'answerVoice':av,'notes':notes}
    json.dump(c,open(f'content/{mid}.json','w'),indent=1,ensure_ascii=False)

# 730
chef={0.0:(.33,.18,.44,.33),0.5:(.34,.2,.46,.33),1.0:(.42,.22,.46,.4),7.5:(.78,.15,.22,.75),8.0:(.2,.15,.8,.68),
      8.5:(.47,.17,.16,.6),9.0:(.48,.28,.13,.52),9.5:(.44,.31,.13,.47),10.0:(.44,.28,.13,.4)}
wss={4.0:(.05,.2,.95,.45),4.5:(.25,.08,.6,.55),5.0:(.35,.08,.63,.85),8.5:(.08,.2,.39,.55),9.0:(.36,.3,.12,.5),
     9.5:(.31,.35,.13,.43),10.0:(.32,.31,.12,.37)}
bar={5.5:(.5,.22,.5,.5),6.0:(.3,.08,.5,.58),6.5:(0,.15,.34,.5)}
write(730,'B','staff','female',[
 ('to wipe the kitchen counter','the chef','male',chef),
 ('to spread a tablecloth','the waitress','female',wss),
 ('to serve a cappuccino','the barman','male',bar)],T(21),10.0,
 [('staff',.40,.47,'female'),('guests',.85,.44,'female'),('a tablecloth',.80,.68,'female'),('pendant lamps',.28,.25,'female')],
 'What is the waitress doing?',['She','is','spreading','a','white','tablecloth.'],'female',
 'Fast clip with many cuts. Chef = grey-haired man in whites; at 0.0-1.0 he presses cloths on the steel pass (read as wiping). Barman boxed only in the bar shots 5.5-6.5: at the end two bearded waiters stand in the group and I cannot tell which of them is the barman, so he is off there. In the group shots 9.0-10.0 the chef and waitress boxes are narrow (people stand shoulder to shoulder).')

# 230
D={0.0:(.36,.12,.62,.88),0.5:(.36,.12,.62,.88),1.0:(.33,.2,.6,.8),3.0:(.31,.15,.62,.85),3.5:(.37,.15,.53,.85),4.0:(.18,.15,.57,.85),
   4.5:(.5,.24,.38,.66),5.0:(.5,.25,.33,.75),5.5:(.55,.25,.3,.75),6.0:(.62,.31,.36,.6),6.5:(.46,.47,.5,.42),7.0:(.5,.31,.47,.67),
   7.5:(.46,.27,.54,.7),8.0:(.47,.27,.5,.63),8.5:(.44,.27,.5,.63),9.0:(.58,.5,.42,.45),9.5:(.6,.28,.33,.65),10.0:(.56,.2,.28,.64),
   10.5:(.52,.18,.36,.75),11.0:(.36,.08,.57,.92)}
A={2.5:(.08,.28,.84,.62),4.5:(0,.25,.5,.65),5.0:(.12,.25,.38,.75),5.5:(.08,.25,.47,.75),6.0:(.12,.3,.5,.6),6.5:(.04,.33,.4,.5),
   7.0:(0,.32,.38,.63),7.5:(.05,.29,.35,.66),8.0:(.08,.27,.34,.58),8.5:(.05,.29,.37,.54),9.0:(.07,.47,.5,.45),9.5:(.03,.63,.22,.3),
   10.0:(0,.58,.2,.26),10.5:(0,.33,.15,.57)}
C={0.0:(0,.05,.36,.95),0.5:(0,.05,.36,.95),1.0:(0,.05,.33,.95),3.0:(0,.05,.31,.95),3.5:(0,.05,.37,.95),4.0:(0,.05,.18,.95),
   9.5:(.25,.22,.35,.75),10.0:(.2,.24,.36,.66),10.5:(.15,.23,.37,.75),11.0:(0,.17,.36,.83)}
write(230,'B','director','female',[
 ('to raise her fists triumphantly','the director','female',D),
 ('to wear a pirate costume','the actor','male',A),
 ('to stand on a tripod','the film camera','female',C)],T(23),10.0,
 [('a director',.68,.36,'female'),('a film camera',.30,.45,'female'),('a folding chair',.83,.62,'female'),('the sun',.12,.30,'female')],
 'What is the director doing?',['She','is','raising','her','fists','triumphantly.'],'female',
 'Animated clip. Director and film camera overlap in the picture (0.0-1.0, 3.0-4.0, 9.5-11.0): boxes split along a vertical line, so a raised hand or a reel is cut here and there. At 4.0 she leans on the camera, the camera box is only the left strip. 1.5-2.0 = clapperboard close-up, everything off. A cameraman in a grey cap is half hidden behind the camera and is no target. The actor phrase is a state (he spreads his arms at 2.5, but the director lifts her hands too).')

# 7119
t7=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W={0.2:(.27,.28,.26,.52),0.7:(.29,.27,.23,.52),1.2:(.27,.25,.24,.63),1.7:(.28,.2,.24,.66),2.2:(.25,.18,.25,.56),2.7:(.28,.16,.24,.6),
   3.2:(.27,.18,.24,.7),3.7:(.28,.18,.24,.72)}
M={0.2:(.05,.24,.22,.36),0.7:(.07,.23,.22,.36),1.2:(.04,.2,.23,.47),1.7:(.05,.16,.22,.48),2.2:(.03,.13,.2,.4),2.7:(.02,.13,.24,.38),
   3.2:(.02,.13,.22,.4),3.7:(0,.15,.26,.42)}
N={0.2:(.53,.3,.47,.34),0.7:(.52,.3,.48,.35),1.2:(.51,.28,.49,.46),1.7:(.52,.24,.48,.4),2.2:(.5,.22,.5,.34),2.7:(.52,.2,.48,.4),
   3.2:(.51,.22,.49,.5),3.7:(.52,.24,.48,.5)}
write(7119,'B','fisher','female',[
 ('to haul a heavy net','the woman','female',W),
 ('to wear yellow waterproofs','the man','male',M),
 ('to bulge with silver fish','the net','female',N)],t7,0.7,
 [('a seagull',.66,.22,'female'),('a net',.75,.48,'female'),('a crate',.14,.65,'female'),('a wave',.78,.34,'female')],
 'What is the fisher in orange doing?',['She','is','hauling','a','heavy','net.'],'female',
 'The woman holds the net against her body: woman and net boxes are split along a vertical line near x 0.52, so her right leg (under the net) falls outside her box. The man phrase is a state (both people laugh, so no action fits only him). Key word "fisher" is not a noun slot because both people are fishers; it is in the question instead.')

# 4930
G={0.0:(.02,.11,.96,.72),0.5:(.02,.1,.98,.74),1.0:(0,.1,1,.74),1.5:(.08,.18,.92,.82),2.0:(0,.08,1,.92),2.5:(0,.08,.8,.7),
   3.0:(0,.08,.88,.85),3.5:(0,.13,1,.8),4.0:(.08,.11,.88,.72),4.5:(0,0,1,.6),5.0:(0,0,1,.7),5.5:(0,0,1,.63),6.0:(0,0,1,.57),
   6.5:(0,0,1,.28),7.0:(0,0,1,.4),7.5:(.78,0,.22,.34),8.0:(0,0,1,.2),8.5:(.18,0,.77,.37),9.0:(.1,.03,.75,.55)}
S={6.5:(.42,.3,.36,.24),7.0:(.36,.4,.4,.23),7.5:(.42,.24,.36,.26),8.0:(.41,.37,.35,.2),8.5:(.47,.49,.32,.19),9.0:(.43,.59,.33,.16)}
write(4930,'B','reward','female',[
 ('to raise her hand eagerly','the girl','female',G),
 ('to jot down a list','the girl','female',G),
 ('to sparkle on the page','the gold star','female',S)],T(19),9.0,
 [('a gold star',.58,.66,'female'),('a notebook',.35,.86,'female'),('a whiteboard',.78,.10,'female')],
 "What is the girl's reward?",['Her','reward','is','a','gold','star.'],'female',
 'Only two targets: the pupils behind her do nothing that fits only one of them (two wear glasses), so two phrases are on the girl. In the close-ups 4.5-7.0 only her hands and sleeves are visible; the girl box is the upper part with the hands. At 6.5 an adult hand (off-camera person) presses the star on; it is no target and lies partly in the star box. 7.5-9.0 she holds the notebook up: girl box = face / fingers, kept clear of the star box. Whiteboard at the still (9.0) is the blurred board behind her, pill on its right panel. Key word "reward" is abstract, so it is in the question and answer, not a noun slot.')
