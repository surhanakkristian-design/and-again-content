import json
p='cz.json'; d=json.load(open(p,encoding='utf-8'))
fixes=[
('7076','phrases',2,'prohýbat se smíchy','lámat se smíchy','"prohýbat se" = arch backwards; double over with laughter = lámat se smíchy'),
('7082','phrases',0,'opírat se o branku','opírat se o bránu','farm gate a flock passes through = brána; branka is a small garden gate'),
('7082','nouns',1,'branka','brána','same; consistency'),
('7082','answer',None,'Opírá se o dřevěnou branku.','Opírá se o dřevěnou bránu.','same; consistency'),
('7085','phrases',2,'vypouštět páru','vydávat páru','a pan gives off steam = vydává páru; vypouštět = release deliberately'),
('7086','phrases',1,'kapat syrovátkou','pouštět syrovátku','"kapat + instrumental" is not idiomatic; curd pouští syrovátku'),
('7092','phrases',1,'šklebit se na sochu','zubit se na sochu','šklebit se = sneer/grimace; grin = zubit se'),
('7092','answer',None,'Šklebí se na tající sochu.','Zubí se na tající sochu.','same; consistency'),
('7094','phrases',0,'vyrvat si holinu z bláta','vyškubnout si holinu z bláta','wrench free; natural verb with a perfective/imperfective pair matching the answer'),
('7094','answer',None,'Vytahuje si holinu z bláta.','Vyškubává si holinu z bláta.','"vytahuje" lost the force of "wrenching"; same verb as the phrase'),
('7099','phrases',1,'padat do hluboké soutěsky','řítit se do hluboké soutěsky','plunge = řítit se; padat too weak'),
('7101','phrases',1,'zvednout tašku vysoko','zvednout sáček vysoko','a paper bag of food = sáček, not taška'),
('7101','answer',None,'Drží tašku s fast foodem.','Drží sáček s fast foodem.','same; consistency'),
('7118','phrases',2,'tleskat od dirigentského pultu','tleskat z dirigentského stupínku','podium = stupínek; pult is the music stand'),
('7118','answer',None,'Tleská od dirigentského pultu.','Tleská z dirigentského stupínku.','same; consistency'),
('7123','phrases',0,'otevřít celého lososa','rozevřít celého lososa','a fish is opened up = rozevřít; otevřít is for doors/boxes'),
('7127','phrases',0,'vzít si tašku s chlebem','vzít si sáček s chlebem','paper bag of bread = sáček'),
('7131','question',None,'Co dělá muž se slunečními brýlemi?','Co dělá muž ve slunečních brýlích?','wearing glasses = ve brýlích; "se brýlemi" = carrying them'),
('7143','phrases',0,'usmívat se vzrušením','nadšeně se usmívat','"usmívat se vzrušením" is not idiomatic'),
('7146','phrases',0,'držet kotevní lano','držet vyvazovací lano','mooring rope = vyvazovací lano; kotevní = anchor rope'),
('7146','answer',None,'Drží kotevní lano.','Drží vyvazovací lano.','same; consistency'),
('7158','phrases',1,'sesunout se na pohovku','svalit se na pohovku','flop down = svalit se; sesunout se = slide down slowly'),
('7158','nouns',2,'láhev od piva','pivní láhev','"láhev od piva" implies an empty bottle; dictionary form pivní láhev'),
('7160','phrases',1,'ukazovat dolů ulicí','ukazovat do ulice','"ukazovat dolů ulicí" is a calque'),
('7170','phrases',0,'kroužit nad údolím','plachtit nad údolím','soar = plachtit; kroužit = circle'),
('7175','phrases',1,'sevřít mechový kořen','sevřít kořen porostlý mechem','mechový = made of moss; mossy = porostlý mechem'),
]
for i,f,k,old,new,why in fixes:
    if k is None:
        assert d[i][f]==old,(i,f,d[i][f]); d[i][f]=new
    else:
        assert d[i][f][k]==old,(i,f,d[i][f][k]); d[i][f][k]=new
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
src=json.load(open('source.json'))
n=sum(3+len(v['nouns'])+2 for v in src.values())
L=[f'# verify cz b026','',f'Texts checked: {n} ({len(src)} videos: phrases, nouns, question, answer)','','## Fixes']
L+= [f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {old} -> {new} ({why})' for i,f,k,old,new,why in fixes]
L+=['','## Doubts left unchanged',
'- 7134 footballer -> fotbalista: clip shows American football; kept the literal noun (míč, fotbalista acceptable for learners).',
'- 7104 grey horse -> šedý kůň: horse breeders say bělouš/šiml, kept the plain colour word for learners.',
'- 7191 phrase popadnout kávu vs answer "Bere si kávu z boudy": slightly different verbs, both correct, kept.',
'- 7136 "brodit se a držet se za ruce" vs answer "ruku v ruce": both natural, kept.',
'- 7097/7185 "psát na psací podložku" (acc) vs 7075 "na psací podložce" (loc): both standard, kept.',
'- 7166 goggles -> brýle (not lyžařské brýle): fine in context, kept.']
open('verify_cz.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
print(n,len(fixes))
