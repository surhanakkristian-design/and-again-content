import json
p='tr.json'; d=json.load(open(p))
fixes=[
("4618","phrases",2,"bir kılıcı zaferle havaya kaldırmak","bir kılıcı zafer edasıyla havaya kaldırmak"),
("4625","question",None,"Sarılı kadın ne yapıyor?","Sarı giyinmiş kadın ne yapıyor?"),
("4653","phrases",0,"paspasın üzerinde ayaklarını yere vurmak","paspasa ayaklarını vurmak"),
("4661","phrases",0,"savrulan yaprakları yakalamak","süzülen yaprakları yakalamak"),
("4661","answer",None,"Bir ağacın altında savrulan yaprakları yakalıyor.","Bir ağacın altında süzülen yaprakları yakalıyor."),
("4684","phrases",1,"sarı at kuyruğu saçı olmak","sarı bir at kuyruğu olmak"),
("4696","phrases",1,"sarkık bir duvara tırmanmak","öne eğimli bir duvara tırmanmak"),
("4729","question",None,"İki kadın kendini nasıl hissediyor?","İki kadın kendilerini nasıl hissediyor?"),
("4737","phrases",1,"sudan taşmak","suyla dolup taşmak"),
("4741","phrases",1,"bir kasa balığı kaldırmak","bir kasa balık kaldırmak"),
("4743","phrases",1,"büyük bir sevinçle alkışlamak","sevinçle alkışlamak"),
]
for k,f,i,b,a in fixes:
    if i is None:
        assert d[k][f]==b,(k,f); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(fixes))
