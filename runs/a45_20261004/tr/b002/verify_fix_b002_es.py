import json, os
H = os.path.dirname(os.path.abspath(__file__)); P = f'{H}/es.json'
t = json.load(open(P))
V = 'intransitive "vitorear" is non-standard (the verb is transitive: vitorear a alguien)'
F = [
 ('68','answer',None,'Le está poniendo una venda en la mano.','redundant stressed "a ella" is unnatural; "le" already carries it'),
 ('347','answer',None,'Le está susurrando un cotilleo al oído.','redundant stressed "a él" is unnatural'),
 ('7124','phrases',1,'lanzar vítores desde el balcón',V),
 ('7932','phrases',2,'lanzar vítores con los brazos en alto',V),
 ('515','phrases',2,'lanzar vítores desde abajo',V),
 ('7563','phrases',2,'lanzar vítores junto a la verja',V),
 ('5272','answer',None,'Los excursionistas están lanzando vítores sobre el cañón.',V),
 ('7932','phrases',0,'colgarse del aro','a person hanging himself on the rim after a dunk: pronominal "colgarse"'),
 ('7932','answer',None,'Se está colgando del aro.','same verb as the phrase (colgarse)'),
 ('343','phrases',1,'estar en el fondo','"yacer" is literary / used of bodies, not of a ring on pool tiles'),
 ('637','phrases',1,'estar en un montón','"yacer" is unnatural for fruit in a crate'),
 ('8001','phrases',0,'extender las alas','own body part takes the article, not the possessive'),
 ('5358','phrases',2,'apoyarse en la mano','own body part takes the article, not the possessive'),
]
log = []
for i, f, k, new, why in F:
    old = t[i][f] if k is None else t[i][f][k]
    if k is None: t[i][f] = new
    else: t[i][f][k] = new
    log.append(f'- {i}, {f}{"" if k is None else "["+str(k+1)+"]"}: {old} -> {new} ({why})')
json.dump(t, open(P, 'w'), ensure_ascii=False, indent=1)
n = sum(3 + len(x['nouns']) + 2 for x in t.values())
doubts = [
 '- 7844 question/answer: "voltear tortitas" is standard but more Latin American; Spain would say "dar la vuelta a las tortitas". Left (rest of the file leans Peninsular: fregona, portátil, vaqueros).',
 '- 7813: "tamborilear sobre cubos" kept; it usually means drumming with the fingers, but reads acceptably for street drummers on buckets.',
 '- 7748 phrase 2: "bostezar sobre su café" is a literal rendering of "yawn over her coffee"; understandable, left.',
 '- 673: "dungarees" -> "un peto" (singular) kept: one garment in Spanish; 7748 uses the same word.',
 '- 673: "¿Qué le pasó al suéter?" kept in the simple past as in English (Peninsular speech would prefer "ha pasado").',
 '- 5594, 6820: possessive with body part plus adjective ("sus alas coriáceas", "su trompa corta") kept; acceptable with a modifier.',
 '- 5594 answer: "está posado" (state) for "is perching" kept; phrase has "posarse".',
 '- 7744, 7369: "remo" / "remar" for kayak and paddle board kept (technical term "pala").',
]
open(f'{H}/verify_es.md', 'w').write(f'# verify es, batch b002\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(log)})\n' + '\n'.join(log) + '\n\n## Doubts left unchanged\n' + '\n'.join(doubts) + '\n')
print(n, len(log))
