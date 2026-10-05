import json
p='ua.json'; t=json.load(open(p))
fixes=[('5607','phrases',1,'спалахнути вогнем','зайнятися полум\'ям'),
('5620','answer',None,'Вона в червоному пальті.','Вона в червоному пальто.'),
('5662','question',None,'Чим вкритий чоловік?','Чим укритий чоловік?'),
('5697','phrases',1,'тягнутися по банкноту','тягнутися до банкноти'),
('5672','nouns',2,'чашка кави','кавова чашка')]
for i,f,k,a,b in fixes:
    if k is None: assert t[i][f]==a; t[i][f]=b
    else: assert t[i][f][k]==a; t[i][f][k]=b
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(3+len(v['nouns'])+2 for v in t.values()); print(n)
