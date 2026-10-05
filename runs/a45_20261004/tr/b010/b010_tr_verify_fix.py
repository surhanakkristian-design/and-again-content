import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b010/tr.json'
d=json.load(open(p))
F=[
('843','question',None,'Sarılı kadın ne yapıyor?','Sarı giysili kadın ne yapıyor?','"sarılı" also reads as "wrapped/hugged"; unambiguous wording for "in yellow"'),
('848','nouns',2,'kiraz domatesler','kiraz domatesleri','noun compound needs the possessive suffix'),
('849','phrases',1,'sevinçle yumruğunu sallamak','yumruğunu havada sallamak','"sevinçle" (with joy) was added, not in the English'),
('873','answer',None,'Karı bir tava tutuyor.','Karısı bir tava tutuyor.','bare "karı" as a subject reads as the vulgar word for woman; possessed form is the natural "the wife"'),
('4003','answer',None,'Her kişi bir çift terlik giyiyor.','Her biri bir çift terlik giyiyor.','"her kişi" is unnatural; "her biri" is the idiomatic "each person"'),
('4013','answer',None,'Güvertenin üstündeki bir kirişin üzerinde duruyorlar.','Güvertenin üstündeki bir kirişin üzerinde duruyor.','inanimate plural subject (boots) takes a singular verb'),
('4014','phrases',2,'kaykayın yanında yuvarlanarak ilerlemek','kaykayın yanında tekerlekleri üzerinde ilerlemek','"yuvarlanmak" means tumbling over; a wheeled suitcase rolls on its wheels'),
('4014','answer',None,'Bavulunu kaykayının yanında yuvarlayarak götürüyor.','Bavulunu kaykayının yanında tekerlekleri üzerinde götürüyor.','same: "yuvarlayarak" = rolling it over and over'),
('4031','question',None,'Tenis topu nereye konuyor?','Tenis topu nereye düşüyor?','"konuyor" reads as passive "is placed" (or a bird perching); a thrown ball "düşer"'),
('4031','answer',None,'En üstteki topun üzerine konuyor.','En üstteki topun üzerine düşüyor.','same as the question'),
('4033','phrases',2,'bir çubuğun üzerine konmak','bir çubuğun üzerine düşmek','same sense of "land" for a ball; "konmak" is for birds / passive of koymak'),
('4037','phrases',0,'tavanın içinde durmak','tavada durmak','"tavanın" is also the genitive of "tavan" (ceiling); matches "tavada" in the question and answer'),
('4048','phrases',1,'bir vidayı vidalamak','bir vidayı sıkmak','tautology ("to screw a screw"); natural collocation'),
('4052','phrases',1,'telefona yürümek','telefona doğru yürümek','bare dative with "yürümek" is unnatural; "towards" needs "doğru"'),
('4060','phrases',0,'bir şelaleden aşağı dalmak','bir şelaleden aşağı düşmek','"dalmak" needs a medium to dive into; over a waterfall it is "aşağı düşmek"'),
('4060','answer',None,'Bir şelaleden aşağı dalıyor.','Bir şelaleden aşağı düşüyor.','same as the phrase'),
]
lines=[]
for i,f,k,b,a,w in F:
    cur=d[i][f] if k is None else d[i][f][k]
    assert cur==b,(i,f,cur)
    if k is None: d[i][f]=a
    else: d[i][f][k]=a
    lines.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {b} -> {a} ({w})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(3+len(v['nouns'])+2 for v in d.values())
doubts='''- 864 nouns[2] "a cap" = "kep" (worn cap); sk/cz read it as the bottle cap ("kapak"), de/fr as a worn cap. Left, the source is ambiguous.
- 886 / 4027 nouns "bir bardak çay", "bir bardak süt": "bir" kept, it is the measure word; without it the phrase is not Turkish.
- 849 nouns "a rubber stamp" = "damga"; "kaşe" would be the office word. Left.
- 873 nouns "karı" / "koca" left as dictionary forms.
- 4014 phrases[1] "ayağıyla yeri itmek": "ayağıyla" is added, but the phrase is not natural without it. Left.
- 4018 "biniyor" for "are riding": also means getting on; left as the usual wording.
- 880 "tarla boyunca koşmak" for "run across the field": acceptable, "çayırda" would suit sheep better. Left.
'''
open('/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b010/verify_tr.md','w').write(f'# b010 tr verification\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes ({len(F)})\n'+'\n'.join(lines)+'\n\n## Doubts left unchanged\n'+doubts)
print(n,len(F))
