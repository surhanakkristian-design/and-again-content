import json, os
H = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(f'{H}/tr.json')); s = json.load(open(f'{H}/source.json'))
F = [
 ('572','answer',None,'Patatesleri bir kovaya koyuyor.','Bir kovaya patates koyuyor.','English object is indefinite ("potatoes"); the accusative made it "the potatoes"'),
 ('573','phrases',2,'bir bardağı eline almak','eline bir bardak almak','indefinite object stands bare directly before the verb'),
 ('575','phrases',2,'bir taşınabilir şarj cihazını havaya kaldırmak','taşınabilir bir şarj cihazını havaya kaldırmak','word order: adjective + bir + noun'),
 ('575','answer',None,'Onu bir taşınabilir şarj cihazına takıyorlar.','Onu taşınabilir bir şarj cihazına takıyorlar.','word order: adjective + bir + noun'),
 ('582','question',None,'Kadın nasıl hissediyor?','Kadın kendini nasıl hissediyor?','"hissetmek" is transitive, needs "kendini" (as the answer of 693 already has)'),
 ('584','phrases',2,'hayretle nefesini tutmak','hayretten nefesi kesilmek','"nefesini tutmak" = to hold one\'s breath on purpose; a gasp is "nefesi kesilmek"'),
 ('592','phrases',2,'yol boyunca yuvarlanıp gitmek','yol boyunca ilerlemek','"yuvarlanmak" for a van means tumbling over; it rolls along on its wheels'),
 ('604','phrases',2,'uzun bir fiş yazdırmak','uzun bir fiş basmak','"yazdırmak" is causative (to have something printed); the machine itself "basar"'),
 ('640','phrases',0,'iki ağırlığı eline almak','eline iki ağırlık almak','numeral + accusative reads as "the two weights"; indefinite object stands bare before the verb'),
 ('667','phrases',2,'şok içinde nefesini tutmak','şoktan nefesi kesilmek','same as 584: gasp is not "to hold one\'s breath"'),
 ('683','answer',None,'Evyede tabakları yıkıyorlar.','Evyede tabak yıkıyorlar.','answer to "ne yıkıyorlar?" with indefinite "plates": bare object, no accusative'),
 ('693','question',None,'Kadın nasıl hissediyor?','Kadın kendini nasıl hissediyor?','needs "kendini"; matches the answer "Kendini çok uykulu hissediyor."'),
 ('695','phrases',0,'eline yaslanmak','başını eline dayamak','"eline yaslanmak" is not said in Turkish; resting the chin/head on the hand is "başını eline dayamak"'),
]
lines = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    lines.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({why})')
json.dump(t, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
n = sum(5 + len(v['nouns']) for v in s.values())
D = [
 '- Accusative on "bir + noun" directly before the verb (600 "bir pizza dilimini çekmek", 622 "bir paket lastiğini çekmek", 630 "uzun bir halatı çekmek", 651 "bir vidayı sıkmak", 653 "bir yastığı kaldırmak", 599, 650 answer): grammatical as a specific indefinite, the bare form would be the more usual dictionary entry; left.',
 '- 572 phrases[0]: "bahçede toprak kazmak" adds "toprak"; Turkish "kazmak" sounds incomplete without an object, left.',
 '- 623 phrases[2]: "ayaklarını masaya uzatmak" adds "masaya" (from the clip) to render "put his feet up"; left.',
 '- 635 question/answer: "Ayaklarında ne var?" / "Ayaklarında sandalet var." (what is on their feet) instead of a literal "giymek"; natural Turkish for the state of wearing, left.',
 '- 569/618/699: "yük arabası" for both "a trolley" and "a cart"; a post-office trolley could be "el arabası".',
 '- 578 nouns[3]: "parke taşları" for cobblestones; "Arnavut kaldırımı" is the classic term but names the paving, not the stones.',
 '- 592: "minibüs" for "a van" (a cargo van is "panelvan"); common rendering, left.',
 '- 608 nouns[3]: "sweatshirt" kept in English spelling (TDK: "svetşört"); the English spelling is the usual one in Turkish.',
 '- 619 nouns[0]: "otlar" for "herbs" can also read as weeds/grass; no short unambiguous alternative.',
 '- 654 "Sarılı kadın": "sarılı" also means "wrapped"; standard colour pattern (mavili, yeşilli), left.',
 '- 678 phrases[2]: "çömelmek" for a crouching cat is human-like; nouns[0] "vantilatör" assumes an electric fan (hand fan = "yelpaze").',
 '- 699: "kaçak olarak geçirmek" for "to smuggle" is wordy; "peynir kaçırmak" is shorter but ambiguous. Left.',
 '- 644 phrases[0]: "ağzını kapatmak" can also mean "to close her mouth"; "eliyle" would be an addition.',
]
open(f'{H}/verify_tr.md', 'w').write(f'# verify b008 tr\n\nTexts checked: {n} (100 videos: 300 phrases, {n-500} nouns, 100 questions, 100 answers).\n\n## Fixes ({len(lines)})\n' + '\n'.join(lines) + '\n\n## Doubts left unchanged\n' + '\n'.join(D) + '\n')
print(n, len(lines))
