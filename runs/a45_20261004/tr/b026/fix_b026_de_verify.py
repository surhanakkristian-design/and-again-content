import json
p='de.json'; d=json.load(open(p))
fixes=[
('7079','nouns',2,'eine Spule','eine Rolle','coil of lead strip is a roll, not an electrical coil/spool'),
('7094','phrases',0,'ihren Stiefel freireißen','ihren Stiefel losreißen','"freireißen" unidiomatic; "losreißen" is the natural verb'),
('7107','phrases',1,'den Kopf zurücklegen','den Kopf in den Nacken legen','"den Kopf zurücklegen" is not idiomatic for tilting the head back'),
('7110','nouns',2,'eine Lichterkette','Lichterketten','English plural must stay plural'),
('7116','phrases',1,'aus der Feuerwache fahren','aus der Feuerwache herausfahren','pull out = herausfahren'),
('7116','answer',None,'Es fährt aus der Feuerwache.','Es fährt aus der Feuerwache heraus.','pull out = herausfahren, matches phrase'),
('7120','nouns',2,'Werkzeug','Werkzeuge','English plural must stay plural'),
('7123','answer',None,'Sie streicht das leuchtend orange Fleisch glatt.','Sie streicht das leuchtend orangefarbene Fleisch glatt.','uninflected "orange" before noun is colloquial; inflected standard form'),
('7132','phrases',0,'ihre Aufnahmen zeigen','stolz ihre Aufnahmen zeigen','"show off" includes pride; plain "zeigen" lost that sense'),
('7139','answer',None,'Sie steht in einem Haufen Fische.','Sie steht inmitten vieler Fische.','"a lot of fish" is a quantity, not a heap; natural wording'),
('7161','nouns',0,'eine Lichterkette','Lichterketten','English plural must stay plural'),
('7169','nouns',0,'eine Lichterkette','Lichterketten','English plural must stay plural'),
('7191','answer',None,'Sie schnappt sich einen Kaffee von der Hütte.','Sie schnappt sich an der Hütte einen Kaffee.','"von der Hütte" reads as off the roof of the hut; "an der Hütte" is natural'),
('7192','answer',None,'Er hält ein Diplom über seinen Kopf.','Er hält ein Diplom über den Kopf.','body part takes definite article in German'),
('7194','phrases',0,'einen Mottendruck halten','einen Druck mit einer Motte halten','"Mottendruck" is not a German word'),
('7194','answer',None,'Sie pinnt einen Mottendruck fest.','Sie steckt einen Druck mit einer Motte fest.','"Mottendruck" not a word; "feststecken" is standard for pinning'),
]
log=[]
for k,f,i,b,a,why in fixes:
    if i is None:
        assert d[k][f]==b,(k,f,d[k][f]); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,d[k][f][i]); d[k][f][i]=a
    log.append(f'- {k} {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('verify_de.md','w').write(f"# verify de b026\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes ({len(fixes)})\n"+"\n".join(log)+"""

## Doubts left unchanged
- 7080 nouns: stairs -> "Treppenstufen" (alternative "eine Treppe" is more idiomatic but singular).
- 7166 nouns: goggles -> "eine Skibrille" (German pair noun is singular; kept, matches phrase).
- 7175 nouns: fallen leaves -> "Laub" (mass noun is the natural German equivalent).
- 7105 answer uses "Das Model" instead of a pronoun to avoid es/sie clash; kept.
- 7186 answer "Sie geht in den Bäumen ins Bett." slightly unusual but correct.
- 7170 phrase "hoch über dem Tal schweben": "hoch" renders "soar".
""")
print(n,len(fixes))
