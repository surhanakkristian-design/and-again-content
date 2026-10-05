import json
p='cz.json'; d=json.load(open(p))
fixes=[('4987','phrases',2,'sesunout se na stůl','zhroutit se na stůl'),
('5008','phrases',1,'třídit staré klíče','probírat se starými klíči'),
('5042','nouns',1,'panelák','bytový dům'),
('5048','phrases',0,'šťourat se s klíčem','šťourat se klíčem'),
('5061','phrases',0,'vyjet nahoru po eskalátoru','vyjet nahoru eskalátorem'),
('5085','phrases',2,'zvednout telefon','zvednout telefon do výšky'),
('5086','phrases',2,'odrážet světla na stropě','odrážet stropní světla'),
('5087','phrases',2,'vyprat mop','vymáchat mop'),
('5094','phrases',1,'zářit do kamery','rozzářeně se usmívat do kamery')]
for k,f,i,a,b in fixes:
    assert d[k][f][i]==a,(k,d[k][f][i]); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values()))
