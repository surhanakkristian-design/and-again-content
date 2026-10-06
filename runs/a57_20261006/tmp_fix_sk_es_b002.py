import json
p='tr/b002/es/sk.json'; d=json.load(open(p))
log=[]
def fix(i,field,old,new,why):
    v=d[i][field]
    if isinstance(v,list):
        n=0
        for k,x in enumerate(v):
            if x==old: v[k]=new; n+=1
        assert n, (i,field,old)
    else:
        assert v==old,(i,field,v); d[i][field]=new
    log.append(f"- {i} {field}: {old} -> {new} ({why})")
F=[
('596','phrases','byť oblečený v žltom','byť oblečená v žltom','target is the female runner, agreement'),
('596','recall','byť oblečený v žltom','byť oblečená v žltom','same fix in recall row'),
('596','phrases','byť oblečený vo fialovom','byť oblečená vo fialovom','target is the female runner, agreement'),
('596','recall','byť oblečený vo fialovom','byť oblečená vo fialovom','same fix in recall row'),
('36','phrases','vziať svojho miláčika do náručia','vziať svojho domáceho miláčika do náručia','mascota = pet; bare "miláčik" reads as darling'),
('36','recall','vziať svojho miláčika do náručia','vziať svojho domáceho miláčika do náručia','same fix in recall row'),
('36','nouns','sveter na gombíky','kardigán','natural noun for rebeca'),
('5358','nouns','sveter na gombíky','kardigán','natural noun for rebeca'),
('7858','answer','Balansuje v polovici cesty medzi dvoma útesmi.','Balansuje na polceste medzi dvoma útesmi.','natural idiom for a medio camino'),
('7858','recall','Balansuje v polovici cesty medzi dvoma útesmi','Balansuje na polceste medzi dvoma útesmi','same fix in recall row'),
('8032','phrases','chytiť priateľku za ruku','chytiť kamarátku za rameno','brazo = arm (za ruku = holding hands); priateľka can mean girlfriend'),
('8032','recall','chytiť priateľku za ruku','chytiť kamarátku za rameno','same fix in recall row'),
('7844','phrases','mať oblečenú košeľu s golierom','mať na sebe košeľu s golierom','natural wording, matches the sibling phrase'),
('7844','recall','mať oblečenú košeľu s golierom','mať na sebe košeľu s golierom','same fix in recall row'),
('8001','phrases','bicyklovať popri husi','bicyklovať sa popri husi','standard verb is reflexive bicyklovať sa'),
('8001','recall','bicyklovať popri husi','bicyklovať sa popri husi','same fix in recall row'),
('7154','phrases','bicyklovať za jednokolkou','bicyklovať sa za jednokolkou','standard verb is reflexive bicyklovať sa'),
('7154','recall','bicyklovať za jednokolkou','bicyklovať sa za jednokolkou','same fix in recall row'),
('7744','answer','Dopadá na hladinu.','Tvrdo dopadá na hladinu.','estrellarse = crash down, not a soft landing'),
('7744','recall','Dopadá na hladinu','Tvrdo dopadá na hladinu','same fix in recall row'),
('4222','phrases','prekrížiť si ruky','založiť si ruky','idiomatic for cruzarse de brazos'),
('4222','recall','prekrížiť si ruky','založiť si ruky','same fix in recall row'),
('4125','phrases','stiahnuť látku','potiahnuť za látku','tirar de = tug at'),
('4125','recall','stiahnuť látku','potiahnuť za látku','same fix in recall row'),
('4125','nouns','pódium','javisko','theatre stage = javisko'),
('4125','answer','Na pódiu dvíha chobot.','Na javisku dvíha chobot.','theatre stage = javisko, same word as noun'),
('4125','recall','Na pódiu dvíha chobot','Na javisku dvíha chobot','same fix in recall row'),
('7200','phrases','riadiť paraglajdový padák','ovládať paraglajdový padák','natural verb for steering a paraglider'),
('7200','recall','riadiť paraglajdový padák','ovládať paraglajdový padák','same fix in recall row'),
('5540','nouns','chvost','konský chvost','coleta = ponytail; bare chvost = tail'),
('7453','phrases','opekať rezance','restovať rezance','saltear = stir-fry'),
('7453','recall','opekať rezance','restovať rezance','same fix in recall row'),
]
for f in F: fix(*f)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tr/b002/es/tmp_fixlog_sk_es_b002.txt','w').write('\n'.join(log))
print(len(log))
