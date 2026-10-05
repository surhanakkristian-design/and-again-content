import json
p='ua.json'; d=json.load(open(p))
fixes=[
('7077','phrases',2,'заповнювати підстаканники','займати підстаканники','iced coffees sit in (occupy) the holders, not fill them'),
('7085','nouns',2,'драбина','стрем’янка','stepladder = стрем\'янка'),
('7087','phrases',2,"примоститися на кам'яній стіні","сидіти на кам'яній стіні",'perfective -> imperfective entry form, cat is perched'),
('7093','answer',None,'Вона стоїть у черзі статистів.','Вона стоїть у ряду статистів.','line behind a rope, not a queue'),
('7095','phrases',0,'їхати геть із шайбою','від’їжджати із шайбою','natural verb for skate off'),
('7095','answer',None,'Вона їде геть із шайбою.','Вона від’їжджає із шайбою.','same as phrase'),
('7108','phrases',2,'розчулитися до сліз','розчулюватися до сліз','imperfective entry form'),
('7139','nouns',0,'сітка','сіть','fishing net = сіть'),
('7142','phrases',2,'зображати стиглі лимони','зображувати стиглі лимони','standard form'),
('7144','phrases',0,'висипати кошик для фритюру','спорожняти кошик для фритюру','висипати takes the contents, not the basket'),
('7161','phrases',2,'обнюхувати надкушений торт','обнюхувати наполовину з’їдений торт','half-eaten, not bitten'),
('7166','phrases',2,'поправляти свої окуляри','поправляти свої захисні окуляри','same word as noun goggles'),
('7169','nouns',2,'медична аптечка','аптечка','pleonasm'),
('7172','phrases',2,'дивитися, склавши руки','дивитися, зчепивши руки','склавши руки = idly doing nothing; clasped hands = зчепивши руки'),
('7188','phrases',1,'тягнути руку вгору','витягувати руку вгору','stretch an arm = витягувати'),
('7191','answer',None,'Вона хапає каву з будки.','Вона хапає каву з будиночка.','будка = booth/kennel; hut = будиночок'),
('7194','phrases',2,'стояти на драбині','стояти на стрем’янці','stepladder = стрем\'янка, same as noun'),
('7194','nouns',2,'драбина','стрем’янка','stepladder = стрем\'янка'),
]
# apostrophe style: match file's existing apostrophe
txt=open(p).read(); apos="'" if "п'яниця" in txt else '’'
log=[]
for vid,f,i,b,a,why in fixes:
    a=a.replace('’',apos); b=b.replace('’',apos)
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==b,(vid,f,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
    log.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('verify_ua.md','w').write('# verify ua b026\n\nTexts checked: '+str(sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values()))+f' ({len(d)} videos)\n\nFixes ({len(log)}):\n'+'\n'.join(log)+'''

Doubts left unchanged:
- 7077 nouns[3] "холодні кави": plural of кава is colloquial; kept to preserve the English plural.
- 7094 nouns[0] "стюард" for a festival steward: used for event/stadium stewards, but also means flight attendant.
- 7105 phrases[2] "здувати пластівці в повітря": understandable; "здіймати" would be an alternative.
- 7118 "аплодувати з подіуму": conductor's podium, kept.
- 7163 "серветка" for tissue (паперова хусточка possible).
''')
print(len(log))
