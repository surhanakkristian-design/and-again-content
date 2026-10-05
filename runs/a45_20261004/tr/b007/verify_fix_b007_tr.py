import json
p='tr/b007/tr.json'; raw=open(p).read(); t=json.loads(raw)
F=[
('467','phrases',2,'diğerlerinin üzerinde yükselmek','diğerlerinden çok daha uzun olmak','"üzerinde yükselmek" is a literal calque for a person; a tall man is "çok daha uzun"'),
('467','question',None,'Yaşlı usta neyi şekillendiriyor?','Yaşlı usta ne şekillendiriyor?','indefinite object in the answer ("uzun bir vazo") needs "ne", not accusative "neyi"'),
('491','question',None,'Adam neyi tadıyor?','Adam ne tadıyor?','indefinite object in the answer ("hardal") needs "ne", not "neyi"'),
('470','phrases',0,'uzun bir saç örgüsü olmak','uzun bir saç örgüsüne sahip olmak','as written it reads "to be a long braid" (compound suffix hides the possessive)'),
('473','phrases',0,'altın bir madalyayı ısırmak','altın bir madalya ısırmak','indefinite object directly before the verb takes no accusative'),
('473','answer',None,'Altın bir madalyayı ısırıyor.','Altın bir madalya ısırıyor.','same; same wording as the phrase'),
('486','phrases',0,'dağa doğru çıkmak','dağa çıkmak','"dağa doğru" = towards the mountain; the path goes up the mountain'),
('511','phrases',1,'koruyucu gözlük takmak','yüzücü gözlüğü takmak','the clip shows swim goggles, not safety glasses'),
('511','nouns',1,'koruyucu gözlük','yüzücü gözlüğü','same sense, same word as the phrase'),
('516','answer',None,'Lavabo taşıyor ve su yere akıyor.','Lavabo yere taşıyor.','added a second clause that is not in the English'),
('520','phrases',0,'kanoyla kürek çekmek','kanoda kürek çekmek','natural collocation is "kanoda kürek çekmek"'),
('520','answer',None,'Kanoyla kürek çekerek kayalıkların yanından geçiyor.','Kanoda kürek çekerek kayalıkların yanından geçiyor.','same wording as the phrase'),
('535','phrases',1,'bir tabaktan yemek','bir tabaktan yemek yemek','intransitive "eat" is "yemek yemek"; the bare form reads as the noun "food from a plate"'),
('545','phrases',2,'kot bir ceket giymek','bir kot ceket giymek','"kot ceket" is a fixed compound; "bir" goes before it'),
('555','phrases',1,'büyük bir yaprağı temizlemek','büyük bir yaprak temizlemek','indefinite object directly before the verb takes no accusative'),
('557','phrases',0,'bir tabağı temizlemek','bir tabak temizlemek','indefinite object directly before the verb takes no accusative'),
('561','phrases',1,'küçük bir parçayı kabul etmek','küçük bir parça kabul etmek','indefinite object directly before the verb takes no accusative'),
('566','phrases',0,'paslı bir varili boşaltmak','paslı bir varil boşaltmak','indefinite object directly before the verb takes no accusative'),
]
lines=[]
for i,f,k,a,b,w in F:
    cur=t[i][f] if k is None else t[i][f][k]
    assert cur==a,(i,f,cur)
    if k is None: t[i][f]=b
    else: t[i][f][k]=b
    lines.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({w})')
ind=2 if raw.startswith('{\n  ') else None
json.dump(t,open(p,'w'),ensure_ascii=False,indent=ind)
n=sum(3+len(v['nouns'])+2 for v in t.values())
open('tr/b007/verify_tr.md','w').write(f'''# b007 tr verification

Texts checked: {n} ({len(t)} videos)
Fixes: {len(F)}

## Fixes
'''+'\n'.join(lines)+'''

## Doubts left unchanged
- 453 nouns: peas = "bezelye" (singular collective; "bezelyeler" would be the literal plural but is unnatural for food on a plate).
- 488 phrases: "a black top" = "siyah bir atlet" (456 uses "üst" for "top"; "atlet" kept as it fits a bodybuilder's tank top, clip not viewable here).
- 532 phrases: "a grey shirt" = "gri bir tişört" (elsewhere shirt = "gömlek"; kept as a football shirt).
- 516: sink = "lavabo" (a kitchen sink is strictly "evye"; "lavabo" is common usage and consistent in the video).
- 553: "sahayı biçmek" (more idiomatic "sahanın çimlerini biçmek", but that adds a word; consistent in phrase and answer).
- 506 nouns: doorway = "kapı aralığı" (also "kapı girişi").
- 459: "bir klipsli altlığa" (compound "klipsli altlık" kept; "klipsli bir altlığa" also possible).
- 475, 476: "bir deniz kabuğunu dinlemek", "bir yaprağı büyütmek" keep the accusative (bare "bir yaprak büyütmek" would read "to grow a leaf").
''')
print(n,len(F))
