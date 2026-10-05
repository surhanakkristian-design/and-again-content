import json
p='sk.json'; d=json.load(open(p))
fixes=[
('7891','phrases',0,'pridať malý lístok','pridať malý lístoček','"lístok" in a restaurant reads as ticket/menu; garnish leaf needs lístoček'),
('7892','phrases',1,'mať na sebe zamrznuté okuliare','mať na sebe ojínené okuliare','frost-covered goggles = ojínené; zamrznuté suggests frozen solid'),
('7896','phrases',2,'otvoriť doširoka ústa','doširoka otvoriť ústa','natural word order: adverb before the verb'),
('7902','phrases',1,'prekopať záhon so zeleninou','rozhrabať záhon so zeleninou','a dog digging up a bed = rozhrabať; prekopať is deliberate gardening'),
('7903','nouns',2,'loďka na veslovanie','veslová loďka','standard term for a rowing boat'),
('7914','answer',None,'Zmáča suseda odvedľa.','Oblieva suseda odvedľa.','zmáčať is perfective; ongoing action needs an imperfective verb'),
('7915','phrases',2,'ukazovať dvanástu hodinu','ukazovať dvanásť hodín','a clock shows "dvanásť hodín"; dvanásta hodina is unnatural'),
('7942','phrases',2,'sedieť na operadle','sedieť na opierke','armrest = opierka; operadlo is the backrest'),
('7963','phrases',1,'behať po cestičke','bežať po cestičke','one directed run along the path = bežať; behať is iterative/aimless'),
('7970','phrases',2,'jesť zmrzlinu','žrať zmrzlinu','animal eating = žrať; also removes the Q ambiguity'),
('7970','question',None,'Čo je čajka?','Čo žerie čajka?','"Čo je čajka?" reads as "What is a seagull?"'),
('7970','answer',None,'Je zmrzlinu.','Žerie zmrzlinu.','same verb as phrase and question'),
('7995','question',None,'Čo robí jazdkyňa?','Čo robí motorkárka?','jazdkyňa = horse rider; motorbike rider = motorkárka'),
('8012','phrases',1,'usrkávať šálku kávy','usrkávať zo šálky kávy','one sips from a cup, not the cup itself'),
]
out=[]
for k,f,i,b,a,why in fixes:
    cur=d[k][f][i] if i is not None else d[k][f]
    assert cur==b,(k,f,cur)
    if i is None: d[k][f]=a
    else: d[k][f][i]=a
    out.append(f'- {k}, {f}{"["+str(i)+"]" if i is not None else ""}: {b} -> {a} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
doubts='''
Doubts left unchanged
- 7897 answer: "Dotýka sa tváre koňa" keeps the English "face"; hlava/papuľa would be more idiomatic for a horse but changes the word.
- 7939 question: "Čo je muž?" is correct (jesť) but could be misread as "What is the man?"; kept, the answer disambiguates.
- 7910 phrase: "tancovať na hudbu" is colloquial; "tancovať do hudby" also possible.
- 7993: "skejtbord" spelling kept (codified variant beside skateboard).
- 7941 answer: "Vyvažuje vedro na dverách" kept, matches the phrase verb.
'''
open('verify_sk.md','w').write(f'# b030 sk verify\n\nTexts checked: {n} ({len(d)} videos)\n\nFixes ({len(out)})\n'+'\n'.join(out)+'\n'+doubts)
print(n,len(out))
