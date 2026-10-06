import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b001/'
t=json.load(open(P+'es/cz.json')); s=json.load(open(P+'source_es.json'))
fixes=[  # id, field, idx, before, after, why
('57','phrases',0,'nastoupit jako první','jít nahoru jako první','subir = climb the stairs, not board a vehicle'),
('57','recall',0,'nastoupit jako první','jít nahoru jako první','same as phrase'),
('785','phrases',1,'ukazovat vlaky a časy','ukazovat vlaky a hodiny','relojes = clocks (clock faces), not times'),
('785','recall',1,'ukazovat vlaky a časy','ukazovat vlaky a hodiny','same as phrase'),
('665','phrases',2,'chodit po poli','jít přes pole','por el campo = across the field; same wording as the answer'),
('665','recall',2,'chodit po poli','jít přes pole','same as phrase'),
('704','phrases',0,'hlasitě kýchnout','velmi silně kýchnout','muy fuerte = very strongly; "muy" was dropped'),
('704','recall',0,'hlasitě kýchnout','velmi silně kýchnout','same as phrase'),
('704','answer',None,'Hlasitě kýchá.','Velmi silně kýchá.','same word inside the video, "muy" kept'),
('704','recall',3,'Hlasitě kýchá','Velmi silně kýchá','same as answer'),
('5660','nouns',0,'jablko','blok','manzana here = city block (the building), not apple'),
('5660','recall',3,'jablko','blok','same as noun'),
('5129','nouns',1,'pouzdro','kryt','funda = the cover over the furniture, not a case'),
('5129','recall',3,'pouzdro','kryt','same as noun'),
('5108','answer',None,'Mávají z jednoho domu ve vesnici.','Mávají z domu ve vesnici.','"jednoho" is unnatural and not in the source'),
('5108','recall',3,'Mávají z jednoho domu ve vesnici','Mávají z domu ve vesnici','same as answer'),
]
for vid,f,i,b,a,w in fixes:
    cur=t[vid][f] if i is None else t[vid][f][i]
    assert cur==b,(vid,f,i,cur)
    if i is None: t[vid][f]=a
    else: t[vid][f][i]=a
json.dump(t,open(P+'es/cz.json','w'),ensure_ascii=False,indent=1)
n=sum(len(x['phrases'])+len(x['nouns'])+2+len(x['recall']) for x in s.values())
L=[f'# b001 es -> cz verification','',f'Texts checked: {n} (100 videos)','',f'Fixes ({len(fixes)}):']
L+=[f'- {v}, {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({w})' for v,f,i,b,a,w in fixes]
L+=['','Doubts left unchanged:',
'- 852 nouns/phrase "llevar un collar blanco" -> "nosit bílý náhrdelník": faithful to the source (target = the older lady).',
'- 4788 question "¿Cómo están las mujeres?" -> "Jak se ženy tváří?": natural with the answer "jsou velmi překvapené".',
'- 4658 "coche antiguo" -> "staré auto" (could be "historické auto"); kept, meaning clear.',
'- 868 "crecer cada vez más" -> "být čím dál větší": natural Czech, same meaning.',
'- 5282 answer "Zpívá píseň a hraje k tomu na kytaru" expands "con su guitarra" for naturalness.']
open(P+'es/verify_cz.md','w').write('\n'.join(L)+'\n'); print(n,len(fixes))
