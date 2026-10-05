import json
p='de.json'; d=json.load(open(p))
fixes=[
('5360','phrases',0,'durch die Schranke gehen','durch die Sperre gehen','ticket gate in a station is "Sperre"; "Schranke" is a boom barrier'),
('5365','phrases',1,'die Hände ergeben heben','die Hände heben und sich ergeben','"ergeben" as adverb is ungrammatical here; matches the answer'),
('5366','phrases',1,'beide Hände ergeben heben','beide Hände heben und sich ergeben','same as 5365'),
('5371','nouns',0,'eine Girlande','ein Blumenkranz','the garland is the ring of flowers worn on the head'),
('5404','question',None,'Was macht der Mann?','Was bereitet der Mann zu?','"Was macht der Mann?" reads as "what is he doing"; question asks what he is making'),
('5404','answer',None,'Er macht eine Menge Toast.','Er bereitet eine Menge Toast zu.','matches the corrected question'),
('5405','question',None,'Was macht das Baby im Ringelbody?','Was macht das Baby im gestreiften Body?','same word as the phrase "einen gestreiften Body tragen"'),
('5416','phrases',0,'staunend starren','erstaunt starren','"staunend starren" is a clumsy doubling'),
('5434','phrases',0,'einen Lichtschalter anknipsen','einen Lichtschalter umlegen','one switches on the light, not the switch; "umlegen" is the action on the switch'),
('5452','phrases',2,'Schnee darauf haben','mit Schnee bedeckt sein','"Schnee darauf haben" is unidiomatic'),
('5462','phrases',0,'sanft ihre Brust berühren','sich sanft an die Brust fassen','reflexive gesture, natural; the non-reflexive version sounds odd'),
('5469','phrases',0,'mit Wanderstöcken ausschreiten','mit Walkingstöcken ausschreiten','Nordic walking poles are "Walkingstöcke"'),
('5469','answer',None,'Sie hält zwei Wanderstöcke fest.','Sie hält zwei Walkingstöcke fest.','same word as the phrase'),
('5477','phrases',2,'auf einen Haufen zusammenbrechen','auf einen Haufen fallen','"zusammenbrechen" on a heap is unidiomatic for a playful tumble'),
]
log=[]
for vid,f,i,old,new,why in fixes:
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==old,(vid,f,cur)
    if i is None: d[vid][f]=new
    else: d[vid][f][i]=new
    log.append(f'- {vid} {f}{"["+str(i)+"]" if i is not None else ""}: {old} -> {new} ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('verify_de.md','w').write(f"# verify de b021\n\nTexts checked: {n} (100 videos)\n\nFixes ({len(log)}):\n"+"\n".join(log)+"""

Doubts left unchanged:
- 5355 nouns "ein Steinsims" for "a stone ledge" (a low stone platform); acceptable, "Steinvorsprung" also possible.
- 5439 phrase "vier Männer bedecken" for "to cover four men" (umbrella); literal but understandable.
- 5354 "a class" -> "eine Gruppe" (workout class); "Kurs" would make the question unnatural.
- 5432 answer "Er foppt den Kunden." for "tricking"; "foppen" is right but slightly old-fashioned.
- 5451 "eine Spritze" serves both "injection" (phrase) and "a syringe" (noun); standard German.
""")
print(n,len(log))
