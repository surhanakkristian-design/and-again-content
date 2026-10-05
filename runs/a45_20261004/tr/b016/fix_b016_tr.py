import json
p='tr.json'; d=json.load(open(p))
fx=[("4750","phrases",1,"sepete uzanmak","elini sepete daldırmak"),
("4750","answer",None,"Yatağın üzerinde kıyafetleri katlıyor.","Yatağın üzerinde kıyafet katlıyor."),
("4757","answer",None,"Yolda aşağı doğru bisiklet sürüyor.","Yolda bisiklet sürüyor."),
("4758","phrases",1,"rafların üzerine yiyecek koymak","raflara yiyecek koymak"),
("4762","phrases",2,"uzaktaki duvarı kaplamak","karşı duvarı kaplamak"),
("4769","phrases",1,"mavi bir kasket takmak","mavi bir kep takmak"),
("4769","nouns",2,"kasket","kep"),
("4782","nouns",3,"oyun parkı","oyun alanı"),
("4793","phrases",2,"parkın üzerinde dalgalanmak","parkın üzerinde uçuşmak"),
("4796","nouns",0,"kasket","kep"),
("4801","phrases",2,"çok uzun boylu olmak","çok uzamak"),
("4830","phrases",0,"suda dönmek","suda geri dönmek"),
("4831","nouns",0,"kasket","kep")]
for k,f,i,a,b in fx:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(fx))
