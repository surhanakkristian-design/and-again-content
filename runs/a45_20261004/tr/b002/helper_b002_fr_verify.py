import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/fr.json'
t = json.load(open(p)); n = sum(len(v['phrases']) + len(v['nouns']) + 2 for v in t.values())
F = [
 ('36','phrases',2,"soulever son animal dans ses bras","prendre son animal de compagnie dans ses bras","\"pet\" = animal de compagnie; \"prendre dans ses bras\" is the natural wording for scoop up"),
 ('406','phrases',0,"balancer un lourd marteau","manier un lourd marteau","\"balancer\" means to sway or throw away, wrong for swinging a hammer at work"),
 ('8036','phrases',0,"se serrer contre le mur","se plaquer contre le mur","idiomatic verb for pressing oneself against a wall"),
 ('7016','nouns',0,"un portail","une barrière","a metal farm gate on a field lane is \"une barrière\", \"portail\" is a house/garden entrance"),
 ('4222','phrases',0,"faire signe à la caméra","faire signe de la main à la caméra","\"faire signe à\" alone reads as beckoning; the gecko waves its hand"),
 ('4222','answer',None,"Il fait signe à la caméra.","Il fait signe de la main à la caméra.","same as the phrase, same wording inside the video"),
 ('7858','phrases',2,"faire signe depuis la falaise","faire signe de la main depuis la falaise","wave = hand gesture, not beckon"),
 ('4408','answer',None,"Il goûte un smoothie frais aux fruits.","Il goûte un smoothie aux fruits frais.","\"fresh fruit smoothie\": fresh qualifies the fruit"),
 ('5417','nouns',0,"des lignes aériennes","des câbles aériens","\"lignes aériennes\" reads as airlines; tram overhead wires"),
 ('5538','phrases',1,"se tenir à l'horizon","se dresser à l'horizon","\"se tenir\" is for people; buildings \"se dressent\""),
 ('6836','phrases',2,"lever le poing serré","lever un poing serré","English indefinite \"a clenched fist\"; with the adjective French takes \"un\""),
]
out = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    out.append(f"- {i} {f}{'' if k is None else '['+str(k+1)+']'}: {a} -> {b} ({why})")
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
D = """
Doubts left unchanged
- 8032 nouns[1] "une tour d'horloge" (a clock tower): the clip shows a church clock tower, "un clocher" would be the everyday word, kept because it mirrors the English label.
- 8032 answer "Il propose son chapeau à une femme" (offering): acceptable; "tend" would repeat the phrase verb, the English uses a different verb on purpose.
- 7997 nouns[4] "des feux de la rampe" (footlights): correct term, usually met with the definite article ("les feux de la rampe"); kept for the bare-plural rule.
- 5149 nouns[2] "des bouteilles" (bottles): in a pharmacy "des flacons" may fit better; the bottles are not described in the context.
- 7858 phrases[2] "s'abriter les yeux de la main" (to shade his eyes): "de la main" is added, but French needs it to give the sense.
- 4918 answer "Il monte les escaliers en portant des sacs en papier": verb order differs from the question ("Que porte ...") but the meaning is identical and natural.
- 278 answer "Il fait des squats" for "They": singular agrees with "le groupe" as the brief requires.
- 484 "un balai à franges" (a mop): correct; "une serpillière" is more colloquial.
- 7563 "une maisonnette" (a cottage), 5594 "ses ailes de cuir" (leathery wings), 798 "dans un survêtement turquoise": acceptable, kept.
"""
open(f'{H}/verify_fr.md', 'w').write(f"# b002 fr verification\n\nTexts checked: {n} ({len(t)} videos)\n\nFixes: {len(out)}\n" + '\n'.join(out) + '\n' + D)
print(n, len(out))
