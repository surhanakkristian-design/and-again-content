import json
p='tr/b020/hu.json'
d=json.load(open(p,encoding='utf-8'))
F=[
("5225","phrases",0,"inni egy pohárból","egy pohárból inni","natural entry word order (complement first), as in the rest of the file"),
("5225","nouns",3,"bója","terelőkúp","a traffic cone is terelőkúp; bója is primarily a buoy"),
("5231","phrases",2,"gőzt pöfékelni a kéményéből","gőzt eregetni a kéményéből","pöfékel is used for smoke/pipes, not steam"),
("5232","phrases",2,"öklével a levegőbe bokszolni","a levegőbe öklözni","idiomatic Hungarian for punch the air"),
("5233","answer",None,"Nézik a katonai parádét.","Nézik a katonai díszszemlét.","military parade = katonai díszszemle"),
("5237","phrases",0,"megérinteni az ősi falat","megérinteni a régi falat","English says old, not ancient"),
("5256","question",None,"Mit csinál a piros ruhás bíró?","Mit csinál a piros taláros bíró?","the judge wears a robe (talár), not a dress"),
("5260","phrases",0,"befalni egy epertortát","epertortát befalni","English has no article; egy epertorta implies a whole cake, he eats a slice"),
("5260","nouns",2,"szelet torta","tortaszelet","dictionary compound form"),
("5265","answer",None,"A távcsövével néz.","A távcsövén keresztül néz.","look through = keresztül néz; 'a távcsövével néz' is unidiomatic"),
("5267","phrases",0,"egy matracon feküdni","egy szőnyegen feküdni","a shooting mat is a szőnyeg, matrac is a mattress"),
("5274","nouns",3,"zuhanycső","zuhanytömlő","standard term for a shower hose"),
("5299","phrases",2,"rámosolyogni a tisztre","rámosolyogni a tisztviselőre","tiszt is a military officer; an airport checkpoint officer is a tisztviselő"),
("5316","nouns",3,"pácolt sonka","érlelt sonka","cured (air-dried) ham is érlelt sonka; pácolt = marinated/brined"),
("5322","phrases",2,"kiköpni egy falatot","kiköpni egy kortyot","he spits liquid (answer: folyadékot), a mouthful of liquid is korty"),
("5327","nouns",1,"karika fülbevaló","karikafülbevaló","compound written as one word"),
("5332","nouns",0,"kijárat tábla","kijáratjelző tábla","'kijárat tábla' is ungrammatical juxtaposition"),
("5344","phrases",0,"levágni egy laza cérnaszálat","levágni egy kilógó cérnaszálat","a loose thread on clothing is kilógó, laza = slack"),
("5344","phrases",2,"büszkén magasba tartva lenni","büszkén a magasba tartva lenni","'a magasba' needs the article"),
]
for vid,f,i,b,a,w in F:
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==b,(vid,f,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(F))
