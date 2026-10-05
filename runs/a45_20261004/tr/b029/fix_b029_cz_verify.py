import json
p='cz.json'; d=json.load(open(p))
fixes=[
('7759','phrases',0,'převrhnout sudy přes zábradlí','vyklopit sudy přes zábradlí','"převrhnout" = knock over; tipping barrels out to pour = vyklopit'),
('7759','answer',None,'Převracejí sudy přes zábradlí.','Vyklápějí sudy přes zábradlí.','same verb as phrase (vyklápět)'),
('7759','phrases',1,'zmoknout na kost','promoknout na kost','fixed idiom is "promoknout na kost"'),
('7765','phrases',0,'krájet své palačinky','krájet si palačinky','possessive "své" unnatural; dative "si" is the Czech form'),
('7772','phrases',1,'běžet po mokrém písku','klusat po mokrém písku','jog = klusat, not run'),
('7779','phrases',2,'svalit se na podlahu','skutálet se na podlahu','"svalit se" is for heavy bodies; a tumbling bowl = skutálet se'),
('7783','question',None,'Co dělá žena se slunečními brýlemi?','Co dělá žena ve slunečních brýlích?','"in sunglasses" (worn) = ve slunečních brýlích'),
('7787','phrases',2,'úžasem zalapat po dechu','zalapat úžasem po dechu','natural word order'),
('7788','phrases',0,'puknout na dvě poloviny','rozpuknout se na dvě poloviny','splitting into halves = rozpuknout se'),
('7797','phrases',2,'nakonec skončit vsedě','skončit vsedě','"nakonec skončit" redundant'),
('7817','phrases',1,'mračit se soustředěním','soustředěně se mračit','"mračit se soustředěním" unidiomatic'),
('7818','phrases',1,'vykopnout nohy','vyhodit nohy do vzduchu','"vykopnout" = kick out/away; legs kicking up = vyhodit nohy do vzduchu'),
('7818','answer',None,'Pláčou si navzájem v náručí.','Pláčou jedna druhé v náručí.','"si navzájem" ungrammatical here'),
('7828','phrases',1,'nést surf','nést surfové prkno','standard term for surfboard'),
('7829','phrases',2,'viset z lana','viset na laně','dangle from a rope = viset na laně'),
('7874','phrases',1,'chichotat se za rukou','chichotat se do dlaně','idiomatic for giggling behind one\'s hand'),
('7888','answer',None,'Naklání se přes model železnice.','Naklání se přes modelové kolejiště.','model railway layout = modelové kolejiště'),
]
log=[]
for vid,f,i,old,new,why in fixes:
    if i is None:
        assert d[vid][f]==old,(vid,f,d[vid][f]); d[vid][f]=new
    else:
        assert d[vid][f][i]==old,(vid,f,d[vid][f][i]); d[vid][f][i]=new
    log.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: {old} -> {new} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('fix_b029_cz_verify.log','w').write('\n'.join(log)+'\n')
print(len(log))
