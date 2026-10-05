import json
F='tr.json'; d=json.load(open(F))
fixes=[
('5613','nouns',2,'örgü','saç örgüsü','"örgü" alone reads as knitting; braid of hair'),
('5614','question',None,'Sarılı kadın ne giyiyor?','Sarı giyen kadın ne giyiyor?','"sarılı" also means wrapped/hugged; ambiguous'),
('5615','phrases',2,'bardaklara çorba dökmek','bardaklara çorba koymak','"dökmek" suggests spilling; serving soup = koymak'),
('5618','phrases',2,'buzlu kahve dökmek','buzlu kahve doldurmak','pouring a drink = doldurmak; dökmek suggests spilling'),
('5625','phrases',0,'hindistan cevizinden içmek','hindistancevizinden içmek','TDK spelling: hindistancevizi (one word)'),
('5630','phrases',1,'ayaklarının dibine çömelmek','ayaklarının dibinde çömelmek','"at her feet" is location: locative -de'),
('5635','phrases',2,'boyalı tavandan sarkmak','resimli tavandan sarkmak','painted (frescoed) ceiling = resimli; boyalı = merely painted a colour'),
('5638','phrases',1,'pembe bir askılı saten elbise giymek','pembe askılı saten bir elbise giymek','word order: "bir" stands before the head noun after adjectives'),
('5643','phrases',1,'bir el arabası itmek','bir yük arabası itmek','clip shows a trolley stacked with crates; el arabası = wheelbarrow'),
('5645','phrases',2,'zeminde kayarak ilerlemek','yerde tekerlekleriyle ilerlemek','the trolley rolls on wheels; kaymak = slide'),
('5648','phrases',0,'tavana yakın tırmanmak','tavana yakın bir yerde tırmanmak','ungrammatical adverbial; matches the answer'),
('5649','phrases',0,'kaykayı havaya kaldırmak','bir kaykayı havaya kaldırmak','English "a skateboard": indefinite entry form'),
('5651','phrases',0,'tarak tutmak','bir tarak tutmak','English "a comb": entry form like "bir içecek tutmak"'),
('5658','phrases',2,'tabağı öne itmek','tabağı öne doğru kaydırmak','slide = kaydırmak, not itmek (push)'),
('5662','phrases',1,'blenderin kapağını tutmak','blenderın kapağını tutmak','vowel harmony: blender is pronounced "blendır" -> -ın'),
('5665','nouns',0,'emniyet kemeri','tırmanış kemeri','emniyet kemeri = car seatbelt; climbing harness = tırmanış kemeri'),
('5668','phrases',2,'kalem tutmak','bir kalem tutmak','English "a pen": indefinite entry form'),
('5670','phrases',2,'kontrbas tutmak','bir kontrbas tutmak','English "a double bass": indefinite entry form'),
('5674','phrases',0,'sineği kovalamak','bir sineği eliyle kovmak','swat at = wave the hand at to drive off; kovalamak = chase; "a fly" indefinite'),
('5717','phrases',0,'durmadan dönmek','fırıl fırıl dönmek','"round and round" idiom is fırıl fırıl dönmek'),
('6814','phrases',0,'geçit yolu boyunca gitmek','geçit yolu boyunca bisiklet sürmek','"ride" lost the bicycle; matches the answer'),
('6821','phrases',0,'cüzdanına göz atmak','cüzdanının içine göz atmak','peek INTO the wallet'),
]
log=[]
for vid,field,i,before,after,why in fixes:
    if i is None:
        assert d[vid][field]==before,(vid,d[vid][field]); d[vid][field]=after
    else:
        assert d[vid][field][i]==before,(vid,d[vid][field][i]); d[vid][field][i]=after
    log.append(f'- {vid} {field}{"" if i is None else "["+str(i)+"]"}: {before} -> {after} ({why})')
json.dump(d,open(F,'w'),ensure_ascii=False,indent=1)
open('fix_b023_tr_verify.log','w').write('\n'.join(log)+'\n')
print(len(fixes))
