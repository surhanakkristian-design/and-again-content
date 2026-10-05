import json, os
H = os.path.dirname(os.path.abspath(__file__)); P = f'{H}/tr.json'
t = json.load(open(P, encoding='utf-8'))
F = [
 ('10','phrases',1,'parlak yeşil renkte parlamak','parlak yeşil renkte ışıldamak','"parlak ... parlamak" repeats the same root; ışıldamak = to shine/glow'),
 ('811','phrases',0,'kupaya koşmak','kupaya doğru koşmak','running towards a thing needs "-e doğru"; bare dative sounds unnatural'),
 ('7053','phrases',0,'kirli bir tabağı yıkamak','kirli bir tabak yıkamak','indefinite object ("a plate") next to the verb takes no accusative'),
 ('7053','phrases',1,'bir tabağı kurulamak','bir tabak kurulamak','indefinite object takes no accusative'),
 ('775','phrases',0,'bir satranç taşını oynatmak','bir satranç taşı oynatmak','indefinite object ("a chess piece") takes no accusative'),
 ('5129','phrases',0,'bir duvarı boyamak','bir duvar boyamak','indefinite object ("a wall") takes no accusative'),
 ('5282','question',None,'Daha yaşlı adam ne yapıyor?','Yaşlı adam ne yapıyor?','"daha yaşlı adam" without a comparison is unnatural; English "older" here is just the elderly man'),
 ('57','phrases',0,'yukarı ilk çıkmak','ilk olarak yukarı çıkmak','word order: "yukarı ilk çıkmak" is not natural Turkish'),
 ('353','phrases',2,'biraz su dökmek','biraz su koymak','"su dökmek" reads as spilling/pouring away; pouring a drink for someone is "su koymak"'),
 ('4760','phrases',2,'suyun kenarında sarılmak','suyun kenarında kucaklaşmak','"sarılmak" needs an object (birine); friends hugging each other = reciprocal "kucaklaşmak"'),
]
lines = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    lines.append(f'- {i}, {f}{"" if k is None else "["+str(k+1)+"]"}: {a} -> {b} ({why})')
json.dump(t, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n = sum(len(x['phrases']) + len(x['nouns']) + 2 for x in t.values())
doubts = [
 '- 449, answer: "Ağaçların altında dinliyorlar." — dinlemek without an object is slightly bare, but the English has no object either; left.',
 '- 163/247/785/721, "oğlan" for "a boy": colloquial but correct; "erkek çocuk" is the more formal alternative; left.',
 '- 5609, question: "neyden korkuyor" (common, unambiguous) instead of standard "neden" (which reads as "why"); left.',
 '- 852/5062, "restoranın içinden koşmak", "ofisin içinden yürümek": understood as "through"; "... koşarak/yürüyerek geçmek" would be fuller; left.',
 '- 5468, "selfie": TDK suggests "özçekim", everyday usage is "selfie"; left.',
 '- 706, "eldiven" for "a mitten": Turkish has no single everyday word (tek parmaklı eldiven); left.',
 '- 5382, "daha yaşlı bir kadınla konuşmak": literal comparative, acceptable here because it contrasts with the young man; left.',
 '- 5062, "tahtaya çizmek" / "Tahtaya kim çiziyor?": no object, as in English; "çizim yapmak" would be fuller; left.',
]
open(f'{H}/verify_tr.md', 'w', encoding='utf-8').write(
 f'# verify tr, batch b001\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes ({len(F)})\n' + '\n'.join(lines) + '\n\n## Doubts left unchanged\n' + '\n'.join(doubts) + '\n')
print(n, len(F))
