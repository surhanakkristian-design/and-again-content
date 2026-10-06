import json
p='tr/b002/fr/cz.json'
d=json.load(open(p))
F=[
('68','Obvazuje mu zápěstí','Obvazuje jí zápěstí','the injured player is a woman'),
('68','obvazuje mu zápěstí','obvazuje jí zápěstí','the injured player is a woman'),
('119','Nasazuje novou žárovku','Dává tam novou žárovku','"nasazovat žárovku" is not a natural collocation'),
('119','nasazuje novou žárovku','dává tam novou žárovku','same'),
('8032','natahovat klobouk','podávat klobouk','"natahovat klobouk" means to stretch the hat; tendre = hold out'),
('8032','Natahuje klobouk k mladé ženě','Podává klobouk mladé ženě','same'),
('8032','natahuje klobouk k mladé ženě','podává klobouk mladé ženě','same'),
('7124','po řadě kamenných schodů','po kamenných schodech','"řada schodů" unnatural for a flight of steps'),
('4206','zívat, až praská v čelisti','zívat na celé kolo','the natural Czech idiom'),
('4206','nechat natéct kávu','natočit kávu','natural wording for running a coffee'),
('4156','skočit pro robota','vrhnout se po robotovi','"skočit pro" = go and fetch; plonger pour rattraper = dive after'),
('673','srazit se praním','srazit se při praní','natural wording'),
('343','potápěčský kroužek','potápěcí kroužek','pool diving rings are "potápěcí kroužky"'),
('7016','postupovat husím pochodem','jít husím pochodem','natural collocation'),
('4125','zatáhnout za závoj','zatáhnout za plachtu','the clip shows a silk sheet covering the elephant, not a veil'),
('347','Šeptá jí do ucha drby','Šeptá mu do ucha drby','lui = the male friend (English: his ear)'),
('347','šeptá jí do ucha drby','šeptá mu do ucha drby','same'),
('4920','být pruhovaný všemi barvami','být pestrobarevně pruhovaný','unnatural wording'),
('7154','Jak se podnikatel pohybuje?','Jak se podnikatel dopravuje?','se déplacer = get around; "pohybovat se" = move (body)'),
('4918','vybíhat schody po čtyřech','vybíhat schody po dvou','Czech idiom for quatre à quatre'),
('7369','objet velrybu na pádle','pádlovat kolem velryby','"na pádle" is wrong; en pagayant = paddling'),
('5358','nakouknout mezi dvěma hromádkami','vykouknout mezi dvěma hromádkami','she is hidden and looks out: vykouknout (nakouknout + instrumental is ungrammatical)'),
('5358','Nakukuje mezi knihami','Vykukuje mezi knihami','same'),
('5358','nakukuje mezi knihami','vykukuje mezi knihami','same'),
('124','kousnout do svého chleba','kousnout si do chleba','natural wording, reflexive dative instead of possessive'),
]
log=[]
for vid,a,b,why in F:
    x=d[vid]; n=0
    for f in ['phrases','nouns','recall']:
        for i,t in enumerate(x[f]):
            if a in t: x[f][i]=t.replace(a,b); n+=1; log.append(f'{vid} | {f}[{i}] | {t} -> {x[f][i]} | {why}')
    for f in ['question','answer']:
        if a in x[f]: old=x[f]; x[f]=old.replace(a,b); n+=1; log.append(f'{vid} | {f} | {old} -> {x[f]} | {why}')
    assert n, (vid,a)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tmp_fixlog_cz_fr_b002.txt','w').write('\n'.join(log))
print(len(log))
