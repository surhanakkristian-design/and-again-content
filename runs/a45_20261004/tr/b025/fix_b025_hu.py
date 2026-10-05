import json
p='hu.json'; d=json.load(open(p))
fixes=[
('6959','nouns',3,'vízforraló','teáskanna','a camping kettle on a lake, not an electric kettle'),
('6968','nouns',0,'akácfa','akácia','African acacia is akácia; akácfa usually means the robinia'),
('6978','nouns',1,'kosárlabdapalánk','kosárlabdagyűrű','hoop = gyűrű, palánk is the backboard'),
('6987','phrases',0,'egy nehéz kalapáccsal lendíteni','lendíteni egy nehéz kalapácsot','lendít takes the hammer as object'),
('6987','answer',None,'Egy nehéz kalapáccsal lendít.','Egy nehéz kalapácsot lendít.','same as the phrase'),
('6994','phrases',0,'feldobni egy tekercs pamutot','ledobni egy tekercs pamutot','he tosses the roll down the stairs, feldob means upwards'),
('6994','answer',None,'Feldob egy tekercs pamutot.','Ledob egy tekercs pamutot.','same as the phrase'),
('6994','phrases',2,'egy ajtóból nézni','egy ajtónyílásból nézni','natural wording for watching from a doorway'),
('6995','phrases',2,'port verni fel','port felverni','verb prefix order in the infinitive'),
('6996','phrases',2,'fehér permetté válni','fehér permetté porladni','burst into spray, válni loses the burst'),
('7002','phrases',0,'átsiklani a tiszta vízen','siklani a tiszta vízben','glide through water = siklik a vízben; átsiklik means skim over'),
('7002','answer',None,'A pisztráng átsiklik a tiszta vízen.','A pisztráng a tiszta vízben siklik.','same as the phrase'),
('7003','nouns',0,'szikla','sziklafal','cliff = sziklafal, szikla is just a rock'),
('7007','answer',None,'Egy ekét vezet a földön át.','Egy ekét vezet a földben.','a földön át is a calque; the plough runs in the soil'),
('7015','phrases',2,'a pajta ajtajánál állni','az istálló ajtajánál állni','the metal shed is a cow shed (istálló), pajta is a barn'),
('7015','nouns',1,'pajta','istálló','same as the phrase'),
('7022','phrases',1,'megtartani a szekrényt','megtámasztani a ruhásszekrényt','steady = megtámasztani; same word as the noun ruhásszekrény'),
('7023','phrases',2,'négykézláb állni','négy lábon állni','négykézláb is for humans; a dog stands on four legs'),
('7026','nouns',3,'nézőtér','karzat','public gallery of a courtroom = karzat, nézőtér is theatre'),
('7030','phrases',2,'lecsapni az égen át','átsuhanni az égen','swoop across the sky; lecsap means dive down onto prey'),
('7054','phrases',2,'döbbenten levegő után kapkodni','döbbenten levegő után kapni','a single gasp; kapkodni means repeated panting'),
('7061','nouns',1,'hám','biztonsági heveder','hám is a horse harness; a worker\'s safety harness is biztonsági heveder'),
('7062','answer',None,'Megiszik egy nagy turmixot.','Egy nagy turmixot iszik.','ongoing action: imperfective present, not perfective'),
('7064','phrases',1,'szerelést kapni egy ellenféltől','elszenvedni egy ellenfél szerelését','szerelést kapni is unidiomatic'),
('7066','phrases',2,'a székek körül szimatolni','az ülések körül szimatolni','seats in a train carriage are ülések'),
]
log=[]
for vid,f,i,b,a,why in fixes:
    if i is None:
        assert d[vid][f]==b,(vid,f,d[vid][f]); d[vid][f]=a
    else:
        assert d[vid][f][i]==b,(vid,f,d[vid][f][i]); d[vid][f][i]=a
    log.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: "{b}" -> "{a}" ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('verify_hu.md','w').write(f"# b025 hu verify\n\nTexts checked: {n}\n\n## Fixes ({len(fixes)})\n"+"\n".join(log)+"""

## Doubts left unchanged
- 6993 phrases[1] "szundikálni az ablakpárkányon": the cat sleeps on a window seat; Hungarian has no common word for a window seat, ablakpárkány kept.
- 6960 phrases[2] "a keze mögött kuncogni": slightly literal, understandable; kept.
- 6976 phrases[2] "meleg takarót viselni": literal for 'wear a blanket'; kept to match the English verb.
- 7028 nouns[1] "lapostévé": colloquial compound, kept.
- 7058 phrases[2] "lőni egy fotót": colloquial for 'snap a photo', kept.
""")
print(n,len(fixes))
