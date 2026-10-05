import json
p='hu.json'; d=json.load(open(p))
fixes=[
('4745','question',None,'Merre folyik a folyó?','Hol folyik a folyó?','the answer gives a location (under a bridge); "merre" asks for a direction'),
('4747','phrases',1,'a madarakra mosolyogni','rámosolyogni a madarakra','"smile at" is naturally rámosolyog'),
('4748','phrases',2,'derültnek és kéknek maradni','tisztának és kéknek maradni','"derült" describes weather, not the sky staying clear'),
('4749','phrases',2,'egy fonott kosárnak dőlni','nekidőlni egy fonott kosárnak','"lean on" is nekidől; bare dől + -nak is unnatural'),
('4757','answer',None,'Biciklivel gurul lefelé az úton.','Biciklivel halad az úton.','"down the road" = along the road, not downhill'),
('4759','phrases',0,'belehallgatni egy bagettbe','meghallgatni egy bagettet','"belehallgat" means to listen in/sample; the baker listens to the crust'),
('4761','phrases',2,'felhevíteni egy serpenyőt','felmelegíteni egy serpenyőt','natural verb for a stove heating a pan'),
('4762','phrases',0,'egy bőr aktatáskát szorongatni','egy bőraktatáskát szorongatni','material attribute is written as a compound'),
('4784','phrases',0,'elvenni egy nagy ajándékot','átvenni egy nagy ajándékot','"elvenni" = take away; receiving a present is átvenni'),
('4785','phrases',1,'rákacsintani a kamerára','belekacsintani a kamerába','idiomatic form for winking at a camera'),
('4793','phrases',0,'gesztikulálni a gyerekeknek','gesztikulálni a gyerekek felé','gesture to someone = valaki felé'),
('4793','phrases',1,'vergődni a fa stégen','vergődni a fastégen','material attribute written as a compound'),
('4793','phrases',2,'lobogni a park fölött','libegni a park fölött','"lobog" is for flags/flames; kites flutter = libeg'),
('4793','answer',None,'Egy fa madárodú van a munkapadon.','Egy fából készült madárodú van a munkapadon.','"fa madárodú" is misspelled (should be a compound) and ambiguous with "tree"'),
('4800','phrases',1,'kikukucskálni a vőlegény válla fölött','átkukucskálni a vőlegény válla fölött','peek over = átkukucskál; kikukucskál = peek out'),
('4804','phrases',2,'egy fa kocsit húzni','egy fakocsit húzni','material attribute written as a compound'),
('4815','phrases',1,'elfintorítani az arcát','összeráncolni az arcát','"elfintorítani az arcát" is not idiomatic for screwing up one\'s face'),
('4822','phrases',1,'a telefonjára mosolyogni','rámosolyogni a telefonjára','"smile at" = rámosolyog, same as 4747/4781/4820'),
('4829','phrases',0,'egy fém kaparót markolni','egy fémkaparót markolni','material attribute written as a compound'),
('4831','phrases',0,'meglendíteni egy alumínium ütőt','meglendíteni egy alumíniumütőt','material attribute written as a compound'),
('4831','answer',None,'Magasan a gyep fölé üti a labdát.','Magasra üti a labdát a gyep fölött.','"sending the ball high over the lawn": magasra üt is the natural form'),
('4832','phrases',2,'lábnyomok nyomát követni','lábnyomokat követni','"lábnyomok nyomát" is redundant (nyom twice)'),
('4853','phrases',2,'üveg mögött fogaskerekeket felfedni','felfedni az üveg mögötti fogaskerekeket','word order: infinitive phrase read unnaturally'),
('4853','nouns',2,'sárgaréz doboz','sárgarézdoboz','material attribute written as a compound'),
]
for vid,f,idx,b,a,_ in fixes:
    cur=d[vid][f] if idx is None else d[vid][f][idx]
    assert cur==b,(vid,f,cur)
    if idx is None: d[vid][f]=a
    else: d[vid][f][idx]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
s=json.load(open('source.json')); n=sum(3+len(v['nouns'])+2 for v in s.values())
L=[f'# verify hu b016','',f'Texts checked: {n} ({len(s)} videos)','',f'## Fixes ({len(fixes)})']
for vid,f,idx,b,a,w in fixes: L.append(f'- {vid} {f}{"" if idx is None else "["+str(idx)+"]"}: {b} -> {a} ({w})')
L+=['','## Doubts left unchanged',
'- 4779 phrases[1] "lovakkal díszítettnek lenni a tetején": clumsy, but "to have horses on top" has no neat Hungarian infinitive.',
'- 4744 nouns "lábak" for feet: lábfejek is more precise, lábak is the everyday word.',
'- 4795 nouns "gyapjú" for wool: knitting wool would be fonal; kept the literal label.',
'- 4778 "apró sárgaréz fogaskerekeket": strict orthography would give sárgaréz-fogaskerék; common usage kept.',
'- 4781 question "Mit csinál a férfi és a nő?": singular verb with coordinated subjects is acceptable; answer uses plural.',
'- 4753/4771 "... rendelkezni" for "to have": formal but the standard infinitive workaround.']
open('verify_hu.md','w').write('\n'.join(L)+'\n'); print(n,len(fixes))
