import json
p='sk.json'; d=json.load(open(p))
fixes=[
('4975','nouns',0,'klobúk','čiapka'),
('4987','answer',None,'Nesie podnos s kávami so sebou.','Nesie podnos s kávami na cestu.'),
('4998','question',None,'Čo je muž?','Čo muž práve je?'),
('5066','question',None,'Čo je mladý muž?','Čo mladý muž práve je?'),
('5042','phrases',2,'zvaliť sa na lavičku','klesnúť na lavičku'),
('5058','phrases',0,'urobiť smutnú tvár','zatváriť sa smutne'),
('5070','answer',None,'Leží naprieč obrovským matracom.','Leží krížom na obrovskom matraci.'),
('5085','phrases',2,'zdvihnúť telefón','zdvihnúť telefón do výšky'),
('5086','phrases',2,'odrážať svetlá na strope','odrážať stropné svetlá'),
('5087','phrases',2,'vyprať mop','vypláchnuť mop'),
('5089','question',None,'Čo robí mama?','Čo pripravuje mama?'),
('5089','answer',None,'Robí palacinky.','Pripravuje palacinky.'),
('5094','phrases',1,'žiariť do kamery','žiarivo sa usmievať do kamery'),
]
for i,f,k,a,b in fixes:
    if k is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][k]==a,(i,f,k); d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
