import json
p='tr.json'; t=json.load(open(p))
fixes=[
('6837','question',None,'Sarılı kadın ne yapıyor?','Sarılar giymiş kadın ne yapıyor?','"sarılı" also reads as "wrapped"'),
('6853','nouns',0,'kep','kasket','the woman wears a flat cap; "kep" is a peaked/baseball cap'),
('6854','phrases',0,'kırmızı banda hayranlıkla bakmak','kırmızı şeride hayranlıkla bakmak','cloth strip on the arm; "bant" reads as tape'),
('6854','nouns',2,'bant','şerit','same thing as phrase 1'),
('6854','answer',None,'Kırmızı banda hayranlıkla bakıyor.','Kırmızı şeride hayranlıkla bakıyor.','same word as phrase/noun'),
('6854','phrases',1,'iskelenin yanında suda süzülmek','iskelenin yanında yüzmek','a boat floating is "yüzmek"; "süzülmek" = glide'),
('6874','phrases',2,'dizüstü bilgisayarın arkasına gizlenmek','dizüstü bilgisayarın arkasında gizlenmek','lurk = state, locative not dative'),
('6897','phrases',1,'bir çalı çitin üzerinden atlamak','bir çalı çitinin üzerinden atlamak','compound noun needs -(s)i'),
('6897','phrases',2,'kameraya bakmak','kameraya gözlerini dikmek','"stare" was weakened to plain "look"'),
('6900','phrases',0,'saçını düzgün bir topuz yapmak','saçını düzgün bir topuz yapmış olmak','"wear" is a state, not the action of making the bun'),
('6901','nouns',2,'örgü','saç örgüsü','"örgü" alone reads as knitting'),
('6931','nouns',1,'örgü','saç örgüsü','"örgü" alone reads as knitting'),
('6903','phrases',1,'küçük bir cam kavanozu tutmak','küçük bir cam kavanozu sıkıca tutmak','"grip" lost; batch uses "sıkıca" for grip'),
('6917','phrases',2,'liman duvarının üzerinden aşmak','liman duvarına çarpıp üzerinden aşmak','"crash" was missing'),
('6942','phrases',0,'açık savak kapağından coşkuyla akmak','açık savak kapağından gürül gürül akmak','"coşkuyla" = enthusiastically; gush = gürül gürül'),
('6942','answer',None,'Açık savak kapağından coşkuyla akıyor.','Açık savak kapağından gürül gürül akıyor.','same as phrase 1'),
('6944','nouns',2,'fincan','bardak','spilled coffee cup in an airport lounge is a paper cup'),
('6946','nouns',3,'boyun atkısı','boyun fuları','neckerchief = light scarf (fular), "atkı" is a winter scarf'),
]
for vid,f,i,old,new,why in fixes:
    if i is None: assert t[vid][f]==old,(vid,f,t[vid][f]); t[vid][f]=new
    else: assert t[vid][f][i]==old,(vid,f,i,t[vid][f][i]); t[vid][f][i]=new
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
lines=[f'# verify tr b024\n\nTexts checked: 900 (100 videos x 3 phrases + 300 nouns + 100 questions + 100 answers)\n\n## Fixes ({len(fixes)})\n']
for vid,f,i,old,new,why in fixes:
    lines.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: {old} -> {new} ({why})')
lines.append('''
## Doubts left unchanged
- 6862 noun "parallel bars" -> "paralel bar": singular is the usual Turkish apparatus name.
- 6837 "Bir yangını söndürüyor.": a native answer would drop "bir", kept to mirror the English "a fire".
- 6889 "ellerini başına götürmek" for "clutch his head": close idiomatic match.
- 6917 "limana girmek" for "sail into the harbour": sailing implied by the subject (yelkenli gemi).
- 6900 "saçını düzgün bir topuz yapmış olmak": state form, slightly long for an entry.''')
open('verify_tr.md','w').write('\n'.join(lines)+'\n')
