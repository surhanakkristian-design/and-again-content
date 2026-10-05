import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(c,target,t,box):
    n=0
    for tp in c['taps']:
        if tp['target']==target:
            for j,k in enumerate(tp['keys']):
                if abs(k['t']-t)<1e-6:
                    tp['keys'][j]={'t':k['t'],'x':box[0],'y':box[1],'w':box[2],'h':box[3]}; n+=1
    assert n, (target,t)
# 473
c=load(473)
W={1.0:(.78,.25,.22,.45),3.0:(.86,.35,.14,.65),4.0:(.85,.34,.15,.22),4.5:(.85,.36,.15,.20),5.0:(.85,.46,.15,.22),5.5:(.85,.47,.15,.22),
   6.0:(.85,.42,.15,.22),6.5:(.85,.45,.15,.22),7.0:(.85,.56,.15,.22),7.5:(.85,.48,.15,.24),8.0:(.85,.48,.15,.28),8.5:(.84,.46,.16,.26),9.5:(.82,.60,.18,.40)}
R={3.0:(0,.06,.86,.94),4.0:(0,0,.85,1),4.5:(.02,0,.83,1),5.0:(0,.02,.85,.98),5.5:(0,.03,.85,.97),6.0:(0,.05,.85,.95),6.5:(0,.08,.85,.92),
   7.0:(.02,.15,.83,.85),7.5:(.02,.17,.83,.83),8.0:(0,.17,.85,.83),9.5:(0,0,.82,1)}
for t,b in W.items(): setk(c,'the old woman',t,b)
for t,b in R.items(): setk(c,'the runner',t,b)
c['notes']+=' VERIFIER: the old woman is partly in the picture at the right edge at 3.0-8.5 and 9.5 s too (half a face / her clapping hands): boxes added there, runner box narrowed to the split line; her box at 1.0 s moved up to hold her head.'
save(473,c)
# 474
c=load(474)
setk(c,'the woman in front',9.0,(.39,.49,.18,.14)); setk(c,'the singing bowl',9.0,(.37,.63,.18,.14))
setk(c,'the man without a shirt',9.5,(.58,.45,.18,.14))
setk(c,'the woman in front',10.0,(.37,.47,.18,.14)); setk(c,'the man without a shirt',10.0,(.55,.46,.18,.14))
c['notes']+=' VERIFIER: the man without a shirt can still be told apart at 9.5 and 10.0 s (bare torso right behind the woman): boxes added; 9.0 s woman / bowl split moved to 0.63 so the bowl is inside its box.'
save(474,c)
# 475
c=load(475)
for n in c['nouns']:
    if n['word']=='a lid': n['word']='tiles'; n['x']=.72; n['y']=.90
c['notes']+=" VERIFIER: 'a lid' replaced by 'tiles' (floor, bottom right): the upturned cardboard lid looks like a shallow box, so 'a box' would also have been right at that pill."
save(475,c)
# 476
c=load(476)
S={1.5:(0,.28,.46,.72),2.0:(0,.30,.52,.70),2.5:(0,.30,.56,.70),5.0:(.38,.36,.62,.64),5.5:(.45,.34,.55,.66)}
M={1.5:(.27,0,.28,.28),2.0:(.30,0,.30,.30),2.5:(.33,0,.30,.30),5.0:(.12,0,.70,.36),5.5:(.05,0,.57,.34)}
t=8.0
while t<=15.0: M[t]=(0,.03,1,.97); t+=.5
for t,b in S.items(): setk(c,'the student',t,b)
for t,b in M.items(): setk(c,'the microscope',t,b)
c['notes']+=' VERIFIER: microscope switched on at 1.5-2.5 s (its base and knob are in the picture behind the finger; split at y 0.28-0.30, the upper finger falls outside the student box); 5.0-5.5 s split moved up so the fingers on the focus knob are in the student box; eyepiece-view box enlarged to the whole picture.'
save(476,c)
