import json, os
H = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(f'{H}/cz.json')); s = json.load(open(f'{H}/source.json'))
F = [
 ('576','phrases',2,'podívat se nahoru a plakat','dívat se nahoru a plakat','two coordinated verbs need the same aspect'),
 ('579','phrases',2,'sledovat nakreslenou dráhu','jet po nakreslené dráze','"sledovat" reads as "to watch"; the robot drives along the track'),
 ('589','answer',None,'Táhnou tlusté lano.','Táhnou za tlusté lano.','tug-of-war: they pull on the rope, they do not drag it along'),
 ('592','phrases',2,'jet dolů po silnici','jet po silnici','"down the road" = along the road, not downhill'),
 ('616','phrases',2,'být velká a kulatá','být velký a kulatý','agreement with "balvan"'),
 ('616','nouns',0,'skála','balvan','a round boulder people push and climb is "balvan"; "skála" is a cliff'),
 ('616','answer',None,'Stojí na velké skále.','Stojí na velkém balvanu.','same word as the noun'),
 ('619','phrases',0,'táhnout košík nahoru','vytahovat košík','natural verb for hauling up on a rope'),
 ('619','answer',None,'Táhne košík pomerančů.','Vytahuje košík pomerančů.','"táhne" alone = drags; same verb as the phrase'),
 ('645','nouns',3,'šanony','složky','"folders" = složky; "šanony" are lever-arch binders'),
 ('667','phrases',2,'zalapat po dechu šokem','v šoku zalapat po dechu','instrumental "šokem" is unnatural; matches "v šoku" of the answer'),
 ('675','phrases',2,'zbarvit se do zářivě modré','zbarvit se zářivě modře','wrong form of the colour idiom'),
 ('701','nouns',1,'skála','kámen','a flat rock a snake coils on is "kámen"'),
 ('701','answer',None,'Leží na černé skále.','Leží na černém kameni.','same word as the noun'),
]
lines = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    lines.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({why})')
json.dump(t, open(f'{H}/cz.json', 'w'), ensure_ascii=False, indent=1)
n = sum(5 + len(v['nouns']) for v in s.values())
D = [
 '- 573 phrases[2]: "vzít sklenici" for "to pick up a glass" (elsewhere "zvednout"); natural, left.',
 '- 582 phrases[1]: "zkřížit si ruce" (649 has "založit si ruce" for "fold her arms"); both correct, left.',
 '- 595 phrases[1]: "mýt si obličej" for a rabbit; literal to the English "face", left.',
 '- 609 nouns: "skála" for "a rock"; cannot tell rock face from boulder without the picture, left.',
 '- 641 nouns: "mísa na míchání" for "a mixing bowl"; understandable, left.',
 '- 655 nouns: "klobouk" for "a hat" (the clip has party hats, "čepička" may fit better); left.',
 '- 678 nouns: "ventilátor" for "a fan"; in a fabric shop it could be a hand fan ("vějíř"); not decidable from the text, left.',
 '- 693 answer: "Cítí se velmi ospalá." kept close to the English "feels"; "Je velmi ospalá." would be equally natural.',
]
open(f'{H}/verify_cz.md', 'w').write(f'# b008 cz verification\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(F)})\n' + '\n'.join(lines) + '\n\n## Doubts left unchanged\n' + '\n'.join(D) + '\n')
print(n, len(F))
