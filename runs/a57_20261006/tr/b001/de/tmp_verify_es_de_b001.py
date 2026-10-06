import json
p='tr/b001/de/es.json'; t=json.load(open(p)); s=json.load(open('tr/b001/source_de.json'))
fixes=[
('811','answer','Levantan el trofeo en el aire.','Levantan el trofeo al aire.','"al aire" is the idiomatic Spanish'),
('811','recall','levantan el trofeo en el aire','levantan el trofeo al aire','same as answer'),
('365','phrases','estar tumbado en la nevera','estar tumbado encima de la nevera','"auf dem Kühlschrank" = on top; "en la nevera" reads as inside'),
('365','recall','estar tumbado en la nevera','estar tumbado encima de la nevera','same'),
('518','phrases','estar posada en una rama','estar posado en una rama','agreement with "el búho" (masc.) used in the video'),
('518','recall','estar posada en una rama','estar posado en una rama','same'),
('38','phrases','despegar hacia el cielo','volar hacia el cielo','"fliegen" = fly, "despegar" added a meaning'),
('38','recall','despegar hacia el cielo','volar hacia el cielo','same'),
('785','phrases','mostrar trenes y horas','mostrar trenes y relojes','"Uhren" = clocks (timetable shows clock faces)'),
('785','recall','mostrar trenes y horas','mostrar trenes y relojes','same'),
('5282','phrases','cantar a una cuchara de madera','cantar con una cuchara de madera como micrófono','"cantar a" means singing to the spoon; idiomatic rendering of singing into it'),
('5282','recall','cantar a una cuchara de madera','cantar con una cuchara de madera como micrófono','same'),
('680','answer','Canta ante un micrófono.','Canta al micrófono.','"cantar al micrófono" is the natural phrase for singing into a mic'),
('680','recall','canta ante un micrófono','canta al micrófono','same'),
('4941','phrases','abrazar al gato contra sí','estrechar al gato contra el pecho','"abrazar ... contra sí" is unnatural'),
('4941','recall','abrazar al gato contra sí','estrechar al gato contra el pecho','same'),
('353','nouns','el invitado','la invitada','the guest in the clip is a woman (German Gast is always masc.)'),
('353','recall','el invitado','la invitada','same'),
('353','question','¿Qué trae el invitado?','¿Qué trae la invitada?','same'),
('353','answer','El invitado trae una flor.','La invitada trae una flor.','same'),
('5660','nouns','la manzana de edificios','el bloque de pisos','"Häuserblock" here is one tall apartment building'),
('5660','recall','la manzana de edificios','el bloque de pisos','same'),
('4788','question','¿Qué cara ponen las mujeres?','¿Qué aspecto tienen las mujeres?','closer to "Wie sehen ... aus?" and matches the answer'),
('4788','answer','Las mujeres parecen muy sorprendidas.','Las mujeres parecen muy impactadas.','"schockiert" is stronger than "sorprendidas"'),
('4788','recall','parecen muy sorprendidas','parecen muy impactadas','same'),
]
log=[]
for vid,f,a,b,why in fixes:
    x=t[vid]
    if isinstance(x[f],list):
        assert a in x[f],(vid,f,a); x[f]=[b if v==a else v for v in x[f]]
    else:
        assert x[f]==a,(vid,f,a); x[f]=b
    log.append(f'- {vid} {f}: "{a}" -> "{b}" ({why})')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2+len(v['recall'])+len(v['captions']) for v in t.values())
open('tr/b001/de/verify_es.md','w').write(f'# Verify es (Spanish, Spain) for de, batch b001\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes ({len(fixes)})\n'+'\n'.join(log)+'''

## Doubts left unchanged
- 571 "Sie kochen Kartoffeln" -> "Cocinan patatas": "Cuecen patatas" would be more precise for boiling; kept, both correct.
- 57 "Wo sitzen die drei?" -> "¿Dónde se sientan los tres?": the clip shows them going to sit at the back, so the action reading fits; "están sentados" also possible.
- 5609 "tener miedo de los ratones": "tener miedo a" is more common in Spain; "de" is also correct.
- 10 "¿Dónde cae el agua?": "¿Adónde/Sobre qué cae?" stricter, but "dónde" is natural usage.
- 277 "die Schuhe" -> "los zapatos": workout shoes would be "las zapatillas", kept the literal noun.
''')
print(n,len(fixes))
