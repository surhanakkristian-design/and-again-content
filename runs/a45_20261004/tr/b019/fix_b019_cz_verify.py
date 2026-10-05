import json
f='cz.json'; d=json.load(open(f))
fx=[('5106','phrases',2,'otáčet lopatkami','otáčet křídly','windmill sails are "křídla" in Czech; "lopatky" are turbine/propeller blades'),
('5115','nouns',3,'kmen stromu','kláda','a fallen log is "kláda"; "kmen stromu" is a standing tree trunk'),
('5120','phrases',0,'naklonit se nad pacienta','naklonit se nad pacientem','position over someone takes the instrumental: "nad pacientem"'),
('5120','answer',None,'Naklání se nad pacienta.','Naklání se nad pacientem.','same: instrumental after "nad" for position'),
('5140','answer',None,'Razítkuje pas cestujícího.','Razítkuje pas cestující.','the traveller is the woman in the beanie: feminine genitive "cestující"'),
('5157','phrases',2,'prohýbat se smíchy','svíjet se smíchy','"prohýbat se" means to arch/sag; the idiom for doubling up with laughter is "svíjet se smíchy"'),
('5161','phrases',1,'rozprchnout se po náměstí','rozletět se po náměstí','pigeons fly apart: "rozletět se"; "rozprchnout se" is for running'),
('5208','phrases',2,'zvednout poklici tajinu','zvednout poklici tažínu','Czech spelling of tagine is "tažín"'),
]
log=[]
for k,fld,i,b,a,why in fx:
    if i is None:
        assert d[k][fld]==b,(k,d[k][fld]); d[k][fld]=a
    else:
        assert d[k][fld][i]==b,(k,d[k][fld][i]); d[k][fld][i]=a
    log.append(f'- {k}, {fld}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({why})')
json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('verify_cz.md','w').write(f'# b019 cz verification\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes ({len(fx)})\n'+'\n'.join(log)+'''

## Doubts left unchanged
- 5099 "nosit fotoaparát" for "to carry a camera": habitual aspect, acceptable as an entry form.
- 5103 / answer "Sklání svůj dlouhý krk.": "svůj" is slightly redundant but correct, kept to mirror "its".
- 5137 "řečnit z řečnického pultu": repetitive but correct, kept for consistency with the noun "řečnický pult".
- 5167 "koláč" for a custard tart (pastel de nata): close enough for a learner gloss.
- 5172 "bubnovat na buben": tautological but correct and natural.
''')
print(n)
