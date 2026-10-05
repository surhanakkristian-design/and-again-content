import json
p='cz.json'; d=json.load(open(p))
fixes=[
('6977','phrases',1,'naklánět se nad pracovní stůl','sklánět se nad pracovním stolem'),
('6984','nouns',1,'krabička s jídlem s sebou','krabička na jídlo s sebou'),
('6990','phrases',2,'držet se za hlavy','držet se za hlavu'),
('7012','question',None,'Co dělá muž se slunečními brýlemi?','Co dělá muž ve slunečních brýlích?'),
('7015','phrases',2,'stát u dveří přístřešku','stát u dveří stáje'),
('7015','nouns',1,'přístřešek','stáj'),
('7025','phrases',0,'klouzat se bahnem','klouzat bahnem'),
('7025','answer',None,'Klouže se bahnitou louží.','Klouže bahnitou louží.'),
('7030','phrases',2,'prolétnout po obloze','prolétnout oblohou'),
('7052','nouns',2,'mrkev','mrkve'),
('7068','nouns',3,'rohlíky','housky'),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(fixes))
