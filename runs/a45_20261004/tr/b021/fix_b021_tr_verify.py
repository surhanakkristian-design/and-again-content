import json
p='tr.json'; t=json.load(open(p))
F=[
("5359","phrases",2,"kasket takmak","şapka takmak"),
("5359","nouns",2,"kasket","şapka"),
("5363","phrases",0,"sendeleyerek bitişe ilerlemek","sendeleyerek bitiş çizgisine doğru ilerlemek"),
("5364","phrases",1,"açık mavi bir kasket takmak","açık mavi bir şapka takmak"),
("5371","phrases",0,"direği dik hâle getirmek","direği iterek dik konuma getirmek"),
("5376","nouns",1,"kapı aralığı","kapı girişi"),
("5390","phrases",2,"mor bir kasket takmak","mor bir şapka takmak"),
("5390","nouns",2,"mor kasket","mor şapka"),
("5391","phrases",2,"telefonu yan tutmak","telefonu yatay tutmak"),
("5393","answer",None,"Gri bir battaniyenin altına sinmiş duruyor.","Gri bir battaniyenin altına siniyor."),
("5402","phrases",1,"biraz suyu kana kana içmek","kana kana biraz su içmek"),
("5405","phrases",0,"ilk sendeleyen adımlarını atmak","sendeleyerek ilk adımlarını atmak"),
("5405","question",None,"Çizgili bebek ne yapıyor?","Çizgili tulumlu bebek ne yapıyor?"),
("5405","answer",None,"Bebek ilk sendeleyen adımlarını atıyor.","Bebek sendeleyerek ilk adımlarını atıyor."),
("5408","nouns",0,"set","alet çantası"),
("5426","phrases",0,"kameraya göz atmak","başını kaldırıp kameraya göz atmak"),
("5426","nouns",0,"çalı çit","canlı çit"),
("5433","phrases",1,"hayranlıkla yukarı, ışıklara bakmak","başını kaldırıp ışıklara uzun uzun bakmak"),
("5433","phrases",2,"ön kapının önünde toplanmak","ön kapının yanında toplanmak"),
("5433","answer",None,"Hayranlıkla yukarı, ışıklara bakıyor.","Başını kaldırıp ışıklara uzun uzun bakıyor."),
("5444","answer",None,"Dev bir yapbozu iş birliği yaparak kuruyorlar.","İş birliği yaparak dev bir yapboz yapıyorlar."),
("5448","phrases",2,"bir meşale tutmak","bir meşaleyi havada tutmak"),
("5453","phrases",0,"biraz su dökmek","içine biraz su dökmek"),
("5462","question",None,"Hardal rengi giyen kadın ne yapıyor?","Hardal rengi bluzlu kadın ne yapıyor?"),
("5470","phrases",0,"ten rengi topuklu ayakkabılarla adımlamak","ten rengi topuklu ayakkabılarla uzun adımlarla yürümek"),
("5479","phrases",0,"kapının kenarından bakmak","kapının kenarından gizlice bakmak"),
("5480","phrases",1,"kasket takmak","şapka takmak"),
("5480","nouns",0,"kasket","şapka"),
]
for i,f,k,old,new in F:
    if k is None:
        assert t[i][f]==old,(i,f,t[i][f]); t[i][f]=new
    else:
        assert t[i][f][k]==old,(i,f,k,t[i][f][k]); t[i][f][k]=new
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
print(len(F),'fixes')
