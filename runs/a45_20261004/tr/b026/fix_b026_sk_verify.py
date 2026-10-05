import json
p='sk.json'; t=json.load(open(p))
fixes=[
('7085','phrases',2,'vypúšťať paru','vydávať paru','a frying pan "gives off" steam; vypúšťať = release/let out deliberately'),
('7094','answer',None,'Vyťahuje si čižmu z blata.','Vytrháva si čižmu z blata.','"wrenching" = vytrhávať, matches phrase vytrhnúť'),
('7131','question',None,'Čo robí muž so slnečnými okuliarmi?','Čo robí muž v slnečných okuliaroch?','worn glasses: "v okuliaroch" is the natural form'),
('7132','phrases',0,'predvádzať svoj záznam','chváliť sa svojím záznamom','"show off" = chváliť sa; predvádzať = demonstrate'),
('7143','phrases',0,'usmievať sa od vzrušenia','nadšene sa usmievať','"usmievať sa od vzrušenia" is unidiomatic'),
('7163','phrases',1,'vytiahnuť si šál','povytiahnuť si šál','vytiahnuť si šál reads as "take out a scarf"; he pulls it up'),
('7168','phrases',1,'nastúpiť na sedadlo spolujazdca','sadnúť si na sedadlo spolujazdca','nastúpiť takes "do auta", not "na sedadlo"'),
('7192','nouns',1,'balóny','balóniky','party balloons = balóniky; balóny = big/hot-air balloons'),
]
for i,f,k,b,a,w in fixes:
    if k is None:
        assert t[i][f]==b,(i,f); t[i][f]=a
    else:
        assert t[i][f][k]==b,(i,f,k); t[i][f][k]=a
json.dump(t,open(p,'w'),ensure_ascii=False,indent=2)
with open('verify_sk.md','w') as o:
    o.write('# verify sk b026\n\nTexts checked: 100 videos, 1100 texts (300 phrases, %d nouns, 100 questions, 100 answers).\n\n## Fixes\n'%sum(len(v['nouns']) for v in t.values()))
    for i,f,k,b,a,w in fixes: o.write(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {b} -> {a} ({w})\n')
    o.write('''
## Doubts left unchanged
- 7076 phrases[2] "prehýbať sa od smiechu": acceptable; "zohýbať sa od smiechu" also possible.
- 7086 phrases[1] "kvapkať srvátkou" and nouns[1] "hrudka syreniny" (block): understandable, "kus syreniny" an alternative.
- 7092 nouns[1] "bekovka" for flat cap: regional/colloquial but understood.
- 7118 "dirigentský pult" for podium: common usage, strictly the stand.
- 7117/7173 "veslica" for rowing boat: also means racing shell; kept.
''')
