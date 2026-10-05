import json
p='cz.json'; d=json.load(open(p))
fixes=[
("4618","phrases",0,"šklebit se za štítem","zubit se za štítem"),
("4622","nouns",2,"cestovní polštář na krk","polštář na krk"),
("4625","phrases",2,"bušit pěstí do vzduchu","máchnout pěstí do vzduchu"),
("4625","answer",None,"Po hlasování buší pěstí do vzduchu.","Po hlasování máchá pěstí do vzduchu."),
("4640","phrases",2,"zasunout šuplík","zasunout zásuvku"),
("4640","nouns",3,"šuplík","zásuvka"),
("4640","answer",None,"Nalévá prací prostředek do šuplíku.","Nalévá prací prostředek do zásuvky."),
("4641","phrases",1,"dávat jídlo do krabic","dávat jídlo do krabiček"),
("4641","answer",None,"Dává jídlo do krabic.","Dává jídlo do krabiček."),
("4643","phrases",0,"bušit pěstí do vzduchu","máchnout pěstí do vzduchu"),
("4653","phrases",2,"být dokořán otevřený","být otevřené dokořán"),
("4691","phrases",1,"usadit se ke svému stolu","usadit se u svého stolu"),
("4695","phrases",0,"vysypat šuplík","vysypat zásuvku"),
("4701","answer",None,"Padá do vody.","Hroutí se ve vodě."),
("4702","phrases",2,"řítit se dolů po cestě","řítit se po cestě"),
("4720","phrases",0,"dívat se stranou","dívat se do strany"),
("4743","phrases",0,"šklebit se do kamery","zubit se do kamery"),
]
for vid,f,i,b,a in fixes:
    if i is None:
        assert d[vid][f]==b,(vid,f,d[vid][f]); d[vid][f]=a
    else:
        assert d[vid][f][i]==b,(vid,f,d[vid][f][i]); d[vid][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(fixes))
