import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/cz.json'
t = json.load(open(p)); n = sum(3 + len(v['nouns']) + 2 for v in t.values())
F = [('705','answer',None,'Kýchá si do paže.','Kýchá do paže.','"kýchat si" is not idiomatic here; plain verb'),
 ('746','phrases',0,'cákat vodu','cákat vodou','cákat takes the instrumental when no direction is given'),
 ('761','phrases',0,'zalapat po dechu šokem','šokovaně zalapat po dechu','bare instrumental "šokem" is a calque; adverb is natural'),
 ('761','phrases',2,'podpírat její chodidla','podpírat jí nohy','possessive dative is the natural Czech form; feet resting on a cushion are "nohy"'),
 ('768','phrases',0,'mít na sobě bílý klobouk','mít na hlavě bílý klobouk','a hat is worn "na hlavě"'),
 ('784','phrases',1,'usadit se do svého křesla','usadit se do svého lehátka','same thing same word: the chair is the deck chair = lehátko (noun, video 784)'),
 ('787','answer',None,'Zvedá obočí na svou kamarádku.','Zvedá obočí nad svou kamarádkou.','Czech idiom is "zvedat obočí nad někým", not "na někoho"')]
L = [f'# verify cz b009\n\nTexts checked: {n} ({len(t)} videos)\n\nFixes: {len(F)}\n']
for i, f, k, a, b, w in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    L.append(f'- {i}, {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({w})')
L += ['\nDoubts left unchanged', '- 724 "a splash" = šplouchnutí / "V bazénu je velké šplouchnutí.": dictionary-correct but names the event more than the visible burst of water; no clearly better single noun (sprška, šplíchanec are looser).',
 '- 812 "jistit lano zdola": climbers say "jistit (lezkyni) zdola"; kept because the English object is the rope.',
 '- 815 "jít po písku / Jde do moře" for a turtle: "lézt" would be more vivid; "jít" matches the English walk/go.',
 '- 839 "roztahovat jídelní stůl": "rozkládat" is the furniture term; both are used.',
 '- 770 "an orange shirt" = oranžové tričko (elsewhere shirt = košile): plausible for tennis wear, cannot confirm from the text.',
 '- 705/766/838 "svého nosu / své hrudi / svých vlasů": possessive is redundant in Czech but not wrong; kept to mirror the English.']
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
open(f'{H}/verify_cz.md', 'w').write('\n'.join(L) + '\n'); print(n, len(F))
