import json,os
p=os.path.expanduser('~/Projects/and-again-content/runs/a45_20261004/tr/b013/sk.json')
d=json.load(open(p))
def S(i,f,idx,old,new):
    if idx is None:
        assert d[i][f]==old,(i,f,d[i][f]); d[i][f]=new
    else:
        assert d[i][f][idx]==old,(i,f,d[i][f][idx]); d[i][f][idx]=new
S('4276','answer',None,'Kráča s paličkou.','Chodí s paličkou.')
S('4299','phrases',1,'túliť nadýchanú mačku','držať nadýchanú mačku v náručí')
S('4316','phrases',1,'prekrížiť si ruky','založiť si ruky')
S('4426','phrases',1,'prekrížiť si ruky','založiť si ruky')
S('4317','question',None,'Čo jej muž nesie?','Čo jej muž prináša?')
S('4317','answer',None,'Nesie jej šálku kávy.','Prináša jej šálku kávy.')
S('4327','phrases',2,'žeraviť sa pod grilom','žeravieť pod grilom')
S('4333','question',None,'Kde sa kotúľa strieborný kufor?','Kade sa kotúľa strieborný kufor?')
S('4345','nouns',0,'balóny','balóniky')
S('4409','nouns',1,'balóny','balóniky')
S('4356','nouns',0,'papraďe','paprade')
S('4403','phrases',1,'navrstviť na seba vlnené vrstvy','naložiť na seba vlnené vrstvy')
S('4403','answer',None,'Navrstvuje na seba deky.','Nakladá na seba vrstvy diek.')
S('4403','phrases',2,'zababušiť sa pod deky','zababušiť sa do diek')
S('4409','phrases',0,'potácať sa dverami','prepotácať sa cez dvere')
S('4440','phrases',1,'prelomiť sa na polovicu','prelomiť sa napoly')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
