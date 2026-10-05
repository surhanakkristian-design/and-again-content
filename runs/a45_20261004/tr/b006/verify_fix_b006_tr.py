import json, os
H = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(f'{H}/tr.json')); s = json.load(open(f'{H}/source.json'))
n = sum(5 + len(v['nouns']) for v in s.values())
F = [
 ('333','phrases',0,'ipin üzerinden atlamak','bir ipin üzerinden atlamak','English "a rope" is indefinite; the bare genitive reads as "the rope"'),
 ('333','answer',None,'İpin üzerinden atlıyor.','Bir ipin üzerinden atlıyor.','same: "a rope", and same wording as the phrase'),
 ('348','phrases',1,'kollarını açarak el kol hareketi yapmak','kollarını açarak jest yapmak','"kollarını açarak el kol hareketi" doubles "kol" and is clumsy; "jest yapmak" is the natural wording'),
 ('348','phrases',2,'üç renkli sütun göstermek','üç tane renkli sütun göstermek','"üç renkli sütun" reads as "a three-coloured column"; "üç tane" fixes the sense "three coloured bars"'),
 ('349','phrases',0,'kasket takmak','bir kasket takmak','English "a cap": indefinite "bir" as in every other "wear a ..." phrase of the batch'),
 ('390','phrases',0,'kapüşonunu kaldırmak','kapüşonunu takmak','"kaldırmak" with a hood reads as lifting it off; putting the hood up is "kapüşonunu takmak"'),
]
L = [f'# verify tr b006', '', f'Texts checked: {n} (100 videos)', '', f'## Fixes ({len(F)})']
for i, f, k, a, b, w in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    L.append(f'- {i} {f}{"" if k is None else "[%d]" % k}: {a} -> {b} ({w})')
L += ['', '## Doubts left unchanged',
 '- 405 answer: "Karın içinden gelip içeri giriyorlar." for "coming inside from the snow" is grammatical; slightly wordy, no shorter wording is clearly better.',
 '- 437 phrases[0]: "bacağını yukarı koymak" (put her leg up) is literal; kept because "kaldırmak" would lose that she rests it on the parapet.',
 '- 322 phrases[1]: "gözlerini kapatmak" can mean close or cover the eyes; kept, adding "elleriyle" would add a word the English does not have.',
 '- 309/340 "kaleye uçmak" (fly into the goal): literal, understandable; "kaleye girmek" would drop "fly".',
 '- 396 noun "sarılma" (a hug): "kucaklaşma" also possible; kept because the answer uses "sarılıyorlar" (same word in one video).',
 '- 408/435 question "Adamın üzerinde ne var?" for "What is the man wearing?": natural Turkish for a state; phrase uses "giymek" for the action of putting on.',
 '- 366/418 noun "giysi kolu" (a sleeve): bare "kol" would read as "arm"; kept.']
json.dump(t, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
open(f'{H}/verify_tr.md', 'w').write('\n'.join(L) + '\n'); print(n, len(F))
