import json
p='tr/b002/de/sk.json'; d=json.load(open(p))
fixes=[
('676','phrases',1,'riadiť gondolu','kormidlovať gondolu','steuern of a boat = kormidlovať; riadiť is for cars'),
('676','recall',1,'riadiť gondolu','kormidlovať gondolu','same as phrase'),
('7858','answer',None,'Balansuje v polovici cesty ponad roklinu.','Balansuje v polovici cesty nad roklinou.','static position: nad + instr., ponad implies motion'),
('7858','recall',3,'balansuje v polovici cesty ponad roklinu','balansuje v polovici cesty nad roklinou','same as answer'),
('7835','phrases',0,'rútiť sa cez skaly','rútiť sa po skalách','natural collocation for lava tumbling over rocks'),
('7835','recall',0,'rútiť sa cez skaly','rútiť sa po skalách','same as phrase'),
('7239','phrases',2,'tlačiť sa mužovi na hlavu','tlačiť na mužovu hlavu','brush presses against the head; reflexive reading was off'),
('7239','recall',2,'tlačiť sa mužovi na hlavu','tlačiť na mužovu hlavu','same as phrase'),
('5712','phrases',1,'pustiť voľný list papiera','nechať spadnúť voľný list papiera','fallen lassen without direction; pustiť alone reads as let go'),
('5712','recall',1,'pustiť voľný list papiera','nechať spadnúť voľný list papiera','same as phrase'),
('4209','nouns',2,'maska na tvár','pleťová maska','sheet face mask = pleťová maska'),
('7844','phrases',0,'nosiť top odhaľujúci brucho','nosiť krátky top','natural term for bauchfreies Top'),
('7844','recall',0,'nosiť top odhaľujúci brucho','nosiť krátky top','same as phrase'),
('4156','phrases',1,'vrhnúť sa za robotom','vrhnúť sa po robotovi','hechten nach = dive to grab, not chase'),
('4156','recall',1,'vrhnúť sa za robotom','vrhnúť sa po robotovi','same as phrase'),
('8036','phrases',0,'tlačiť sa o stenu','pritláčať sa k stene','tlačiť sa o stenu is unidiomatic'),
('8036','recall',0,'tlačiť sa o stenu','pritláčať sa k stene','same as phrase'),
('7016','nouns',2,'kanvice na mlieko','kanvy na mlieko','milk churns = kanvy; kanvica is a kettle/jug'),
('4125','nouns',3,'pódium','javisko','theatre stage = javisko'),
('4125','answer',None,'Na pódiu dvíha chobot.','Na javisku dvíha chobot.','same word as noun'),
('4125','recall',3,'na pódiu dvíha chobot','na javisku dvíha chobot','same word as noun'),
('4930','question',None,'Akú odmenu dostane dievča?','Akú odmenu dostáva dievča?','German present; perfective dostane is future'),
('4930','answer',None,'Dostane trblietavú zlatú hviezdičku.','Dostáva trblietavú zlatú hviezdičku.','German present; imperfective'),
('4930','recall',3,'dostane trblietavú zlatú hviezdičku','dostáva trblietavú zlatú hviezdičku','same as answer'),
('7200','phrases',0,'riadiť paraglajd','ovládať paraglajd','a paraglider is controlled (ovládať), riadiť is for vehicles'),
('7200','recall',0,'riadiť paraglajd','ovládať paraglajd','same as phrase'),
('376','phrases',1,'peniť sa cez skaly','peniť sa na skalách','natural collocation'),
('376','recall',1,'peniť sa cez skaly','peniť sa na skalách','same as phrase'),
]
log=[]
for vid,f,i,old,new,why in fixes:
    if i is None:
        assert d[vid][f]==old,(vid,f,d[vid][f]); d[vid][f]=new
    else:
        assert d[vid][f][i]==old,(vid,f,i,d[vid][f][i]); d[vid][f][i]=new
    log.append(f"- {vid} {f}{'' if i is None else '['+str(i)+']'}: {old} -> {new} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2+len(v['recall']) for v in d.values())
open('tmp_trv_sk_de_b002.log','w').write(f"{n}\n"+"\n".join(log)+"\n")
print(n,len(log))
