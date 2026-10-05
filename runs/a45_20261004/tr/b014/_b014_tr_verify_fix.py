import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tr.json')
d = json.load(open(p))
fixes = [
 ('4458','phrases',1,'yanık halde fırlamak','yanmış halde fırlamak','"yanmış halde" is the natural adverbial for burnt toast'),
 ('4460','answer',None,'Ateşte avuçlarını ısıtıyor.','Ateşin başında avuçlarını ısıtıyor.','"by the fire" = ateşin başında; "ateşte" reads as "in the fire"'),
 ('4468','phrases',1,'banknotları uzatmak','birkaç banknot uzatmak','"some banknotes" is indefinite, not "the banknotes"'),
 ('4468','answer',None,'Kocaman bir halı yığını taşıyor.','Yüksek bir halı yığını taşıyor.','"towering" = tall, not just huge'),
 ('4472','phrases',2,'uçuruma dik dik bakmak','uçuruma uzun uzun bakmak','"dik dik bakmak" means glaring at someone hostilely; wrong for staring at a cliff'),
 ('4487','phrases',0,'karı itmek','karı kenara itmek','"away" was left out'),
 ('4487','answer',None,'Karı patikadan itiyor.','Patikadaki karı kenara itiyor.','"pushing the snow off the path": original was unnatural'),
 ('4488','phrases',0,'damgayı sertçe vurmak','sertçe damga vurmak','"a stamp" is indefinite; collocation "damga vurmak"'),
 ('4488','answer',None,'Bir belgeye damgayı sertçe vuruyor.','Bir belgeye sertçe damga vuruyor.','same as phrase; definite accusative was wrong'),
 ('4498','phrases',1,'yeşille karalamak','yeşil renkle karalamak','"yeşille" alone is unnatural'),
 ('4502','phrases',0,'bir ampule dik dik bakmak','bir ampule gözünü dikip bakmak','"dik dik bakmak" = glare hostilely'),
 ('4525','question',None,'Turuncu giyen kadın ne yapıyor?','Turunculu kadın ne yapıyor?','"Turuncu giyen" is ungrammatical (needs object case); natural is "Turunculu"'),
 ('4529','answer',None,'Yukarıya, pencerelere bakıyor.','Başını kaldırıp pencerelere bakıyor.','comma construction unnatural; "looking up at"'),
 ('4589','question',None,'Mercan rengi giyen kadın ne yapıyor?','Mercan rengi kıyafetli kadın ne yapıyor?','"Mercan rengi giyen" ungrammatical'),
 ('4600','question',None,'Kadın neye dik dik bakıyor?','Kadın neye gözünü dikip bakıyor?','"dik dik" = hostile glare; she stares in amazement'),
 ('4600','answer',None,'Yelpaze gibi açılmış banknotlara dik dik bakıyor.','Yelpaze gibi açılmış banknotlara gözünü dikip bakıyor.','same as question'),
 ('4607','question',None,'Büyük tanklar neden yapılmış?','Büyük tanklar neyden yapılmış?','"neden" reads as "why"; "made of what" = neyden'),
]
log=[]
for i,f,k,b,a,why in fixes:
    cur = d[i][f][k] if k is not None else d[i][f]
    assert cur==b,(i,f,cur)
    if k is not None: d[i][f][k]=a
    else: d[i][f]=a
    log.append(f'- {i}, {f}{"["+str(k)+"]" if k is not None else ""}: {b} -> {a} ({why})')
json.dump(d, open(p,'w'), ensure_ascii=False, indent=1)
print(len(log)); open(os.path.join(os.path.dirname(p),'_b014_tr_fixlog.txt'),'w').write('\n'.join(log)+'\n')
