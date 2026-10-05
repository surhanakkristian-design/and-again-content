import json
p='cz.json'; d=json.load(open(p))
fixes=[('4753','phrases',0,'pevně si zkřížit ruce','pevně si založit ruce'),
('4758','phrases',2,'ležet v prázdném šuplíku','ležet v prázdné zásuvce'),
('4785','answer',None,'Ťukají si jimi.','Ťukají si sklenicemi.'),
('4796','phrases',2,'vyhodit chlapce nahoru','vyhoupnout chlapce do výšky'),
('4800','phrases',0,'upravovat si motýlka','upravovat si motýlek'),
('4800','answer',None,'Upravuje si motýlka.','Upravuje si motýlek.'),
('4802','phrases',1,'zkřížit si ruce','založit si ruce'),
('4814','phrases',0,'sbírat červené papriky','trhat červené papriky'),
('4814','answer',None,'Sbírá červené papriky.','Trhá červené papriky.'),
('4825','phrases',2,'nastříkat špinavou varnou desku','postříkat špinavou varnou desku'),
('4847','phrases',2,'utírat špinavou vodu','vytírat špinavou vodu')]
for k,f,i,a,b in fixes:
    if i is None: assert d[k][f]==a,(k,f); d[k][f]=b
    else: assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
