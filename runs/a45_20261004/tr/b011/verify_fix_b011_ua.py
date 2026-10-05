import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/ua.json'; t = json.load(open(p))
F = [
 ('4072','phrases',0,'прогулюватися до води','неквапливо йти до води','"прогулюватися до" is not a natural collocation; stroll towards = walk unhurriedly to'),
 ('4073','phrases',0,'пригортати сонне курча','пригортати спляче курча','sleeping = спляче; сонне means sleepy'),
 ('4080','phrases',1,'зняти резинку для волосся','зняти гумку для волосся','"резинка" is a Russianism; standard word is гумка'),
 ('4080','question',None,'Де резинки для волосся?','Де гумки для волосся?','same: резинка -> гумка'),
 ('4084','question',None,'До чого торкається чоловік?','Чого торкається чоловік?','same government as phrase and answer (торкатися чого)'),
 ('4090','phrases',1,'міцно залишатися на місці','непорушно залишатися на місці','"міцно залишатися" is not a collocation; firmly in place = непорушно'),
 ('4094','phrases',0,'пити трохи води','випити трохи води','imperfective with "трохи води" is unnatural; a small quantity needs the perfective'),
 ('4097','phrases',0,'стрибати в повітря','підстрибувати в повітря','natural verb for jumping up into the air'),
 ('4119','phrases',0,'розсипатися на купу','розвалюватися на купу','wrong verb: things розсипаються into pieces, a figure розвалюється into a heap'),
 ('4119','answer',None,'Вона розсипається на купу.','Вона розвалюється на купу.','same verb as the phrase'),
 ('4129','answer',None,'Воно йде з дому в зеленому капелюшку.','Воно йде з дому в зеленому капелюсі.','hat, not a diminutive; nothing added'),
 ('4130','phrases',2,'поплескувати своє волосся з пласким верхом','поплескувати по своєму волоссю з пласким верхом','government: поплескувати по чому'),
 ('4134','phrases',1,'сидіти на чорному кріслі','сидіти в чорному кріслі','one sits у кріслі (as in 4132)'),
 ('4134','answer',None,'Вона сидить на чорному кріслі.','Вона сидить у чорному кріслі.','one sits у кріслі'),
 ('4145','phrases',1,'пробувати удар через себе','пробувати виконати удар через себе','attempt a kick needs the verb; "пробувати удар" reads as taste/test'),
]
out = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    out.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({why})')
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
n = sum(3 + len(v['nouns']) + 2 for v in t.values())
doubts = [
 '- 4064 answer: "Він летить" for папужка: dictionaries give папужка as masculine/common gender; left masculine.',
 '- 4071 "затонулий корабель" for a wreck that stands out of the shallows: usual word for shipwreck, left.',
 '- 4088 question "Де падає вода?" with answer "через широкий край": follows the English where/over pair, left.',
 '- 4104 phrases[2] "бути великим і темним": the bird is "пташка" (feminine) in this video; the big dark pigeon is not among the nouns, generic masculine left.',
 '- 4094 question "двоє коней": collective numeral with an animal noun is accepted usage ("два коні" also possible), left.',
 '- 4141 answer "лежать рівно на спині" for "lying flat on their backs": acceptable, left.',
 '- 4130 "з пласким верхом" for flat-top: descriptive rendering (the barber term is "майданчик"), left.',
]
open(f'{H}/verify_ua.md', 'w').write(f'# verify ua b011\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes ({len(F)})\n' + '\n'.join(out) + '\n\n## Doubts left unchanged\n' + '\n'.join(doubts) + '\n')
print(n, len(F))
