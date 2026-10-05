import json
p='tr.json'; d=json.load(open(p))
fixes=[
('7893','phrases',2,'yerde ağır ağır yürümek','yerde gezinmek','wander = aimless, not "slowly"'),
('7902','phrases',0,'bir pankeki havada çevirmek','bir pankeki havaya atıp çevirmek','same wording as answer'),
('7902','answer',None,'Pankeki havaya atıp çeviriyor.','Bir pankeki havaya atıp çeviriyor.','English "a pancake" is indefinite'),
('7905','question',None,'Sarılı kadın nerede oturuyor?','Sarı giyen kadın nerede oturuyor?','"sarılı" reads as "wrapped/hugged"'),
('7906','phrases',2,'karın içine sırtüstü uzanmak','karda sırtüstü uzanmak','natural phrasing'),
('7910','phrases',1,'müziğe göre dans etmek','müzik eşliğinde dans etmek','natural collocation'),
('7920','phrases',1,'dikkatle kaşlarını çatmak','dikkatini toplayıp kaşlarını çatmak','in concentration, not "carefully"'),
('7931','phrases',0,'bir traktörün yanından geçmek','bisikletle bir traktörün yanından geçmek','ride = on a bike, was lost'),
('7931','answer',None,'Bir traktörün yanından geçiyor.','Bisikletle bir traktörün yanından geçiyor.','ride = on a bike, was lost'),
('7940','answer',None,'Koca bir pizzayı hapır hupur yiyor.','Bütün bir pizzayı hapır hupur yiyor.','whole, not huge'),
('7941','nouns',3,'kapı tokmağı','kapı topuzu','tokmak = door knocker'),
('7942','phrases',2,'koltuğun kolçağına tünemek','kanepenin kolçağına tünemek','it is the sofa'),
('7950','question',None,'Sarılı kadın ne yapıyor?','Sarı giyen kadın ne yapıyor?','"sarılı" reads as "wrapped/hugged"'),
('7972','answer',None,'Kuleden manzarayı seyrediyor.','Kuleden manzarayı hayranlıkla seyrediyor.','admire, not just watch'),
('7974','nouns',3,'terlik','parmak arası terlik','flip-flop, not slipper'),
('7979','phrases',1,'eldiveninin arkasında kıkırdamak','eldivenini ağzına kapatıp kıkırdamak','literal calque; natural Turkish'),
('7979','answer',None,'Eldiveninin arkasında kıkırdıyor.','Eldivenini ağzına kapatıp kıkırdıyor.','same as phrase'),
('8014','phrases',1,'elinin arkasında kıkırdamak','elini ağzına kapatıp kıkırdamak','literal calque; natural Turkish'),
('8014','answer',None,'Elinin arkasında kıkırdıyor.','Elini ağzına kapatıp kıkırdıyor.','same as phrase'),
]
for vid,f,i,b,a,w in fixes:
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==b,(vid,f,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
with open('verify_tr.md','w') as o:
    o.write('# verify tr b030\n\nTexts checked: 1000 (100 videos)\n\nFixes: %d\n\n'%len(fixes))
    for vid,f,i,b,a,w in fixes:
        o.write('- %s %s%s: %s -> %s (%s)\n'%(vid,f,'' if i is None else '[%d]'%i,b,a,w))
    o.write('\nDoubts left unchanged:\n- 7954 "çeyrek" / "Tabağa bir çeyrek koyuyor." mirrors English "a quarter"; could also read as a coin.\n- 7949/7986 "tasma" used for lead (leash); common usage though strictly collar.\n- Colour nicknames "Mavili/Kırmızılı/Beyazlı" are colloquial but natural.\n')
