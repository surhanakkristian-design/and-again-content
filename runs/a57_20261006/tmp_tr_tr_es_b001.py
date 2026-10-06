import json
p='tr/b001/es/tr.json'; t=json.load(open(p)); s=json.load(open('tr/b001/source_es.json'))
F=[('5468','phrases',1,'uzun bir sakalı olmak','uzun sakallı olmak','natural Turkish possession form'),
('5468','recall',1,'uzun bir sakalı olmak','uzun sakallı olmak','same as phrase'),
('5215','phrases',0,'hızla pedal çevirmek','var gücüyle pedal çevirmek','"con fuerza" = hard, not fast'),
('5215','recall',0,'hızla pedal çevirmek','var gücüyle pedal çevirmek','same as phrase'),
('5456','phrases',0,'pasaportunu açmak','pasaportu açmak','source has no possessive (el pasaporte)'),
('5456','recall',0,'pasaportunu açmak','pasaportu açmak','same as phrase'),
('704','phrases',0,'çok sert hapşırmak','çok şiddetli hapşırmak','"sert" unidiomatic for sneezing'),
('704','recall',0,'çok sert hapşırmak','çok şiddetli hapşırmak','same'),
('704','answer',None,'Çok sert hapşırıyor.','Çok şiddetli hapşırıyor.','same'),
('704','recall',3,'Çok sert hapşırıyor','Çok şiddetli hapşırıyor','same'),
('4760','phrases',2,'suyun kenarında sarılmak','su kenarında birbirine sarılmak','reflexive abrazarse = hug each other; natural "su kenarında"'),
('4760','recall',2,'suyun kenarında sarılmak','su kenarında birbirine sarılmak','same'),
('5609','question',None,'Adam neden korkuyor?','Adam neyden korkuyor?','"neden" reads as "why"; "de qué" = of what'),
('665','phrases',2,'tarlada yürümek','kırda yürümek','campo here is grassy hillside, not a crop field'),
('665','recall',2,'tarlada yürümek','kırda yürümek','same'),
('665','answer',None,'Tarlada yürüyor.','Kırda yürüyor.','same'),
('665','recall',4,'Tarlada yürüyor','Kırda yürüyor','same'),
('7999','answer',None,'Köpek otel odasındaki yatakta uzanıyor.','Köpek otel yatağında uzanıyor.','"la cama del hotel" = the hotel bed; nothing added'),
('7999','recall',3,'otel odasındaki yatakta uzanıyor','otel yatağında uzanıyor','same'),
('57','phrases',0,'ilk olarak çıkmak','en önden çıkmak','natural wording, pairs with "en arkadan gitmek"'),
('57','recall',0,'ilk olarak çıkmak','en önden çıkmak','same'),
('339','phrases',0,'sokakta yürümek','sokaktan gitmek','same verb as question/answer (ir por la calle = sokaktan gitmek) inside one video'),
('339','recall',0,'sokakta yürümek','sokaktan gitmek','same'),
('680','phrases',2,'bir masada oturmak','bir masanın önünde oturmak','"frente a" = in front of'),
('680','recall',2,'bir masada oturmak','bir masanın önünde oturmak','same'),
('291','phrases',2,'sıraya dizilmek','sıra hâlinde durmak','state (estar en fila), not the act of lining up'),
('291','recall',2,'sıraya dizilmek','sıra hâlinde durmak','same'),
('5660','nouns',0,'elma','blok','"la manzana" here = city block (english "a block")'),
('5660','recall',3,'elma','blok','same'),
('225','answer',None,'Kadın çalışma masasında oturuyor.','Kadın çalışma masasının önünde oturuyor.','"frente al escritorio" = in front of the desk'),
('225','recall',3,'çalışma masasında oturuyor','çalışma masasının önünde oturuyor','same'),
('121','phrases',0,'bir krepi yakmak','bir pankeki yakmak','tortita = pancake, not crepe'),
('121','recall',0,'bir krepi yakmak','bir pankeki yakmak','same'),
('121','nouns',3,'krep','pankek','same'),
('121','answer',None,'Bir krepi yaktı.','Bir pankeki yaktı.','same'),
('121','recall',3,'Bir krepi yaktı','Bir pankeki yaktı','same'),
]
log=[]
for vid,f,i,a,b,why in F:
    if i is None:
        assert t[vid][f]==a,(vid,f,t[vid][f]); t[vid][f]=b
    else:
        assert t[vid][f][i]==a,(vid,f,i,t[vid][f][i]); t[vid][f][i]=b
    log.append(f"- {vid}, {f}{'' if i is None else '['+str(i)+']'}: {a} -> {b} ({why})")
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2+len(v['recall']) for v in s.values())
open('tr/b001/es/verify_tr.md','w').write(f"# verify tr (es, b001)\n\nTexts checked: {n} (100 videos; captions empty)\n\n## Fixes ({len(F)})\n"+"\n".join(log)+"""

## Doubts left unchanged
- "chico" rendered "çocuk" throughout (5456, 704, 247, 560 etc.); for a young man "genç" would be closer, kept for consistency with the batch.
- 852 "llevar un collar blanco" = "beyaz bir kolye takmak": source says necklace (english confirms), kept.
- 741 "se dobla por la tormenta" = "fırtınadan eğiliyor": colloquial causal ablative, acceptable.
- "gorra" = "şapka" (4058, 5506, 31): "kep" also possible; "şapka" is the everyday word.
""")
print(n,len(F))
