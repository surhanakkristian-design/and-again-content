import json
p='tr.json'; t=json.load(open(p))
F=[("5100","question",None,"Sarılar giymiş adam ne yapıyor?","Sarılı adam ne yapıyor?","unnatural 'Sarılar giymiş'; same pattern as 'Kırmızılı/Beyazlı'"),
("5114","phrases",0,"teleskopla bakmak","teleskoptan dikkatle bakmak","'peer through' = look closely through; 'teleskoptan' for 'through'"),
("5124","phrases",0,"dümdüz ileri bakmak","dümdüz önüne bakmak","natural collocation for 'stare straight ahead'"),
("5125","phrases",1,"bir kaskı havaya kaldırmak","bir miğferi havaya kaldırmak","metal costume helmet = miğfer, not a modern kask"),
("5125","nouns",0,"kask","miğfer","same sense as phrase"),
("5125","answer",None,"Başının üzerinde bir kask tutuyor.","Başının üzerinde bir miğfer tutuyor.","same word for same thing"),
("5127","phrases",0,"kıyafetlerini bavula yerleştirmek","kıyafetlerini valize yerleştirmek","suitcase is 'valiz' everywhere else in the video"),
("5135","phrases",1,"dar bir boşluğa girmek","dar bir boşluğa sığmak","'squeeze into' lost; sığmak carries it"),
("5137","phrases",0,"iki eliyle el kol hareketi yapmak","iki eliyle jest yapmak","redundant 'eliyle el'"),
("5138","phrases",2,"valizle yardım etmek","valizi taşımaya yardım etmek","'valizle yardım etmek' is not idiomatic"),
("5150","phrases",1,"raflarda aramak","rafları aramak","transitive 'search the shelves'; locative without object is incomplete"),
("5154","phrases",1,"bitkilere dalgın dalgın bakmak","bitkilere uzun uzun bakmak","'dalgın dalgın' adds absent-mindedness; gaze = long look"),
("5179","phrases",0,"fırına uzanmak","fırına doğru uzanmak","'towards'; matches the answer"),
("5181","phrases",2,"zaferle kollarını kaldırmak","zafer edasıyla kollarını kaldırmak","'zaferle' is not idiomatic for 'in triumph'"),
("5203","phrases",0,"öne düşüp içeri girmek","önden içeri girmek","natural for 'lead the way inside'"),
]
log=[]
for i,f,k,b,a,why in F:
    cur=t[i][f][k] if k is not None else t[i][f]
    assert cur==b,(i,f,cur)
    if k is None: t[i][f]=a
    else: t[i][f][k]=a
    log.append(f"- {i}, {f}{'' if k is None else '['+str(k)+']'}: {b} -> {a} ({why})")
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
open('_log_b019_tr.txt','w').write("\n".join(log))
print(len(log))
