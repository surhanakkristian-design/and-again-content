import json, os
H = os.path.dirname(os.path.abspath(__file__))
p = f'{H}/es.json'; t = json.load(open(p)); log = []
F = [
 ('307','phrases',1,'adentrarse en la niebla','"hacia el interior de la niebla" is a calque; "adentrarse en" is the natural verb for walking into fog'),
 ('307','answer',None,'Se está adentrando en la niebla.','same wording as the phrase; natural Spanish'),
 ('336','phrases',0,'limpiarse las gafas','Spanish uses the reflexive + article for one\'s own things, not the possessive'),
 ('336','answer',None,'Se está limpiando las gafas.','same as the phrase'),
 ('349','phrases',2,'estar sobre la madera','"tumbado" is not said of a fish; plain "estar sobre" (as for the lemons in 334)'),
 ('355','answer',None,'Está hundiendo la cara entre las manos.','the idiom is "la cara entre las manos"'),
 ('388','phrases',0,'hacer los deberes','fixed collocation takes the article, not the possessive'),
 ('388','answer',None,'Está haciendo los deberes.','same as the phrase'),
 ('390','answer',None,'Se está echando la capucha sobre la cabeza.','"subirse ... sobre la cabeza" is contradictory wording; "echarse la capucha sobre la cabeza" is natural'),
 ('392','phrases',0,'montar a caballo','standard expression for riding a horse'),
 ('392','answer',None,'Está montando a caballo.','same as the phrase'),
 ('405','phrases',0,'entrar primero','subject is a woman; "el primero" is wrong gender, "primero" is neutral'),
]
for i, f, k, new, why in F:
    old = t[i][f] if k is None else t[i][f][k]
    assert old != new, (i, f)
    if k is None: t[i][f] = new
    else: t[i][f][k] = new
    log.append(f'- {i}, {f}{"" if k is None else "[%d]" % k}: {old} -> {new} ({why})')
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
n = sum(3 + len(v['nouns']) + 2 for v in t.values())
doubts = [
 '- 319/328/350/360/386 etc., phrases "estar sentado/tumbado ..." with a feminine subject (la rana, la abuela, la mujer): kept in the masculine citation form of a vocabulary entry; the sentences agree correctly ("Está sentada").',
 '- 405, answer: "Están entrando desde la nieve." is a literal rendering of "coming inside from the snow"; kept because any smoother version adds or drops meaning.',
 '- 440: "levantar pesas pesadas" sounds repetitive but is the exact meaning (heavy weights); kept.',
 '- 412: jersey = "camiseta de equipo" is unusual but needed to keep it apart from T-shirt = "camiseta" in the same video; kept.',
 '- 399/408: bird "estar de pie sobre el muro / la valla" (a native would say "estar posado"); kept because the English says "stand".',
 '- 356: "mirar por todo el gimnasio" for "look around the gym" is acceptable; kept.',
]
open(f'{H}/verify_es.md', 'w').write(f'# verify b006 es\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes\n\n' + '\n'.join(log) + '\n\n## Doubts left unchanged\n\n' + '\n'.join(doubts) + '\n')
print(n, len(log))
