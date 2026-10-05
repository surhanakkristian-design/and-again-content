import json
p="/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b022/tr.json"
d=json.load(open(p))
fixes=[("5483","question",None,"Sahil yolunda ne yapıyor?","Sahilde ne yapıyor?"),
("5488","answer",None,"Feribota veda etmek için el sallıyor.","Feribota el sallayarak veda ediyor."),
("5489","phrases",1,"gümüş bir elbise giymek","gümüş rengi bir elbise giymek"),
("5491","phrases",1,"çiçekten bir çelengi boyna geçirmek","boynuna bir çiçek çelengi geçirmek"),
("5512","phrases",0,"batonunu kaldırmak","bagetini kaldırmak"),
("5558","phrases",2,"hamur yoğurmak","hamuru yoğurmak"),
("5581","nouns",0,"kayalık","uçurum"),
("5597","phrases",0,"sessiz olun işareti yapmak","sus işareti yapmak"),
("5600","answer",None,"Kutudaki yiyecek bozuk.","Kutudaki yiyecek bozulmuş."),
("5606","phrases",1,"tümsekte arkasını dönmek","tümsekte arkasına dönmek")]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,"w"),ensure_ascii=False,indent=1)
print("ok")
