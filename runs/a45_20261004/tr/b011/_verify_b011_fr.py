import json, os
H = os.path.dirname(os.path.abspath(__file__))
p = f'{H}/fr.json'; t = json.load(open(p))
n = sum(3 + len(v['nouns']) + 2 for v in t.values())
fixes = [
 ('4066','phrases',2,"planer au-dessus d'une butte","s'envoler au-dessus d'une butte","planer = glide; the bike is launched off the mound (soar)"),
 ('4078','phrases',2,"être suspendu au-dessus du lit","être suspendue au-dessus du lit","agreement with la tenture murale (feminine), as the file does elsewhere"),
 ('4084','phrases',0,"toucher sa tête","se toucher la tête","own body part: reflexive + definite article"),
 ('4084','answer',None,"Il touche sa tête.","Il se touche la tête.","same, and same wording as the phrase"),
 ('4104','phrases',1,"devenir rouge au visage","avoir le visage qui rougit","'rouge au visage' is not idiomatic French"),
 ('4105','phrases',0,"toucher ses cheveux","se toucher les cheveux","own body part: reflexive + definite article (as 'se couvrir la bouche' in the same video)"),
 ('4119','question',None,"Qu'arrive-t-il à la figure de pierre ?","Qu'arrive-t-il au personnage de pierre ?","'figure' reads as 'face' in French; the clip shows a stone man"),
 ('4119','answer',None,"Elle s'effondre en tas.","Il s'effondre en tas.","pronoun follows le personnage"),
 ('4139','phrases',1,"voleter au-dessus de l'herbe","flotter au-dessus de l'herbe","voleter is for birds/insects; a sheet 'flotte'"),
 ('4145','phrases',2,"célébrer les poings levés","exulter les poings levés","célébrer needs an object in French (anglicism when intransitive)"),
 ('4151','phrases',0,"tenir un stylo","tenir un feutre","the clip shows a marker used for colouring, not a writing pen"),
]
lines = []
for i, f, k, a, b, why in fixes:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    lines.append(f'- {i} {f}{"" if k is None else "["+str(k+1)+"]"}: {a} -> {b} ({why})')
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
doubts = [
 "4072 phrases[1] 'flâner vers l'eau': flâner with a direction is slightly unusual, kept (closest to 'stroll').",
 "4084 phrases[2] 'voir pousser des cheveux jaunes': workaround for 'to grow yellow hair' (cat), kept; 'cheveux' for a cat follows the English 'hair'.",
 "4093 phrases[2] 'briller sur fond d'obscurité': a little literary, kept.",
 "4136 phrases[2] 'soulever des poids lourds': 'poids lourds' can also evoke lorries, kept (clear in a gym).",
 "4139 question 'Où l'homme marche-t-il ?' vs answer 'Il gravit un sentier étroit': two verbs for 'hike', kept (natural French).",
 "4144 phrases[1] 'regarder hors d'une boîte': correct but stiff; 'sortir la tête d'une boîte' would be more natural yet shifts the meaning.",
 "4161 nouns 'une fenêtre' for 'a window': could be 'une vitre' if it is a car window; context does not say.",
]
open(f'{H}/verify_fr.md', 'w').write(f'# b011 fr verification\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes ({len(fixes)})\n' + '\n'.join(lines) + '\n\n## Doubts left unchanged\n' + '\n'.join('- ' + d for d in doubts) + '\n')
print(n, len(fixes))
