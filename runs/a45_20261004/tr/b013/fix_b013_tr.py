import json
p='tr.json'; t=json.load(open(p,encoding='utf-8'))
fixes=[
("4281","phrases",2,"ahşabın üzerine çıkmak","'tırmanmak' over-states a step across; 'climb onto' = üzerine çıkmak"),
("4287","answer",None,"Bir deste anahtar sallıyor.","indefinite object after 'bir deste' takes no accusative"),
("4295","phrases",2,"iki kolunu da açmak","'iki kolunu iki yana' repeats iki; 'both arms' = iki kolunu da"),
("4297","phrases",0,"hayretle yukarı bakmak","amazement = hayret; hayranlık is admiration"),
("4298","phrases",2,"çizgiye doğru yürümek","walk to a line needs 'doğru'"),
("4299","phrases",1,"tüylü kediyi kucağında tutmak","cradle = hold in the arms; kucaklamak = hug"),
("4309","nouns",2,"saç örgüsü","bare 'örgü' reads as knitting"),
("4313","phrases",1,"şaşkınlıkla kendini işaret etmek","'kendini göstermek' = show oneself; point at = işaret etmek"),
("4318","phrases",0,"başının üzerinde alkışlamak","'başının üstünde' is the idiom 'gladly'"),
("4333","phrases",2,"yana devrilmek","'yan devrilmek' ungrammatical; needs dative 'yana'"),
("4335","phrases",0,"elini ilk kaldırmak","'ilk kaldıran olmak' = to be the one who raises first; plain verb entry"),
("4341","question",None,"Genç adam neyden kaçıyor?","'neden' reads as 'why'; 'from what' = neyden"),
("4347","phrases",1,"dalgalarda sörf yapmak","'dalgaların arasından geçmek' loses the riding (she rides a board)"),
("4371","phrases",0,"kasa dairesine gözlerini dikmek","'dik dik bakmak' = glare hostilely; she stares in awe"),
("4371","question",None,"Kadın gözlerini neye dikmiş?","same verb as phrase 0 (stare = gözlerini dikmek)"),
("4371","answer",None,"Gözlerini bankanın kasa dairesine dikmiş.","same verb as phrase 0"),
("4386","phrases",1,"yatağını hazırlamak","she lays out a futon; 'yatağını toplamak' = tidy it away after sleep"),
("4387","phrases",1,"yatağını hazırlamak","she unfolds a futon; 'toplamak' = tidy away"),
("4387","answer",None,"Yatağını hazırlıyor.","same as phrase 1"),
("4393","phrases",0,"küçük bir torba açmak","paper bag of grain; 'poşet' = plastic bag"),
("4393","nouns",2,"torba","same word as phrase 0"),
("4403","phrases",1,"üstüne kat kat yün örtü almak","bare 'yün' = the material wool, not woollen layers"),
("4412","phrases",2,"kamyonete dayanmak","'sürtünmek' = rub against; press against = dayanmak"),
("4416","phrases",1,"bilet basmak","target is the printer; 'yazdırmak' = have something printed"),
("4427","phrases",1,"adama eğilerek selam vermek","'önünde eğilmek' = submit/bow down before; a formal bow = eğilerek selam vermek"),
("4427","answer",None,"Birbirlerine eğilerek selam veriyorlar.","same as phrase 1"),
]
log=[]
for vid,f,i,new,why in fixes:
    if i is None: old=t[vid][f]; t[vid][f]=new; fld=f
    else: old=t[vid][f][i]; t[vid][f][i]=new; fld=f"{f}[{i}]"
    log.append(f"- {vid} {fld}: {old} -> {new} ({why})")
json.dump(t,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in t.values())
doubts="""
Doubts left unchanged
- 4287 Q/4389 Q/4394 Q 'Yeşilli/Beyazlı/Mavili kadın' colloquial but natural for 'the woman in green'.
- 4318 nouns[3] 'kol' for sleeve: correct dictionary word, shares form with 'arm'.
- 4327 phrases[2] 'kızıl kızıl parlamak': adverb is the natural collocation for embers.
- 4349 'tahta' for the rescue board (not 'sörf tahtası'): kept, consistent across phrase, noun, Q, A.
- 4429 phrases[0] 'kaşıkla yemek' can read as noun phrase out of context; fine as vocabulary entry.
"""
open('verify_tr.md','w',encoding='utf-8').write(f"# b013 tr verify\n\nTexts checked: {n}\n\nFixes ({len(log)})\n"+"\n".join(log)+"\n"+doubts)
print(n,len(log))
