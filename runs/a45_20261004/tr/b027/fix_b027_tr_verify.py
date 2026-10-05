import json
p='tr.json'; d=json.load(open(p))
fixes=[
("7195","phrases",1,"başını kaldırıp uçuşan yapraklara bakmak","'yukarı bakmak' with a dative object is unnatural; gaze up = başını kaldırıp bakmak"),
("7195","nouns",2,"yeşillikler","English plural 'greens' must stay plural"),
("7201","nouns",3,"pirinç kap","çömlek is an earthenware pot, not a brass one"),
("7221","phrases",2,"rüzgârdan ters dönmek","'blown' (by the wind) was left out"),
("7222","question",None,"Sarı elbiseli kadın ne yapıyor?","'Sarılı kadın' reads as 'the wrapped woman'; she wears a yellow sundress"),
("7242","phrases",0,"başını kaldırıp kar tanelerine bakmak","'yukarı bakmak' with a dative object is unnatural"),
("7248","nouns",0,"komiser","a police inspector is 'komiser'; 'müfettiş' is an auditor/school inspector"),
("7249","phrases",0,"bir branda örtüsünü çekip almak","noun compound needs the -sı suffix"),
("7258","nouns",1,"balıkçı şapkası","noun compound needs the -sı suffix"),
("7266","phrases",0,"kahve dolu bardaklar taşımak","'bardaklarla kahve taşımak' is unnatural"),
("7270","answer",None,"Martıyı göz hapsinde tutuyor.","'göz kulak olmak' means to look after/protect; here she watches the seagull warily"),
]
log=[]
for vid,f,i,new,why in fixes:
    if i is None: old=d[vid][f]; d[vid][f]=new
    else: old=d[vid][f][i]; d[vid][f][i]=new
    log.append(f"- {vid}, {f}{'' if i is None else '['+str(i)+']'}: {old} -> {new} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('_b027_tr_fixlog.txt','w').write("\n".join(log))
