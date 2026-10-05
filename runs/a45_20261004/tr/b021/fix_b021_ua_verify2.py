import json
p='ua.json'; d=json.load(open(p))
fixes=[
('5366','nouns',1,'металева бочка','бочка з-під пального'),
('5370','phrases',1,'відкушувати булочку з корицею','надкушувати булочку з корицею'),
('5370','answer',None,'Він відкушує булочку з корицею.','Він надкушує булочку з корицею.'),
('5401','phrases',1,'закривати очі','затуляти очі'),
]
for k,f,i,b,a in fixes:
    if i is None:
        assert d[k][f]==b,(k,f,d[k][f]); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i,d[k][f][i]); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
