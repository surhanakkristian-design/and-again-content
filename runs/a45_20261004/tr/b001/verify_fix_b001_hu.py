import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hu.json')
d = json.load(open(P, encoding='utf-8'))
F = [
 ('209','phrases',1,'betenni egy mancsát','betenni a mancsát','"egy mancsát" is unnatural with the possessive; a native says "a mancsát"'),
 ('5468','nouns',0,'tábla','reklámtábla','bare "tábla" reads as blackboard; the clip shows illuminated advertising boards'),
 ('5215','answer',None,'A biciklijén megy egy úton.','Egy úton biciklizik.','unnatural wording; same verb as the phrases ("biciklizni")'),
 ('4603','answer',None,'A biciklijén megy az úton.','Az úton biciklizik.','unnatural wording; same verb as the phrase ("biciklizni")'),
 ('811','answer',None,'Együtt felemelik a trófeát.','Együtt emelik fel a trófeát.','word order: with focused "együtt" and an ongoing action the verbal prefix follows the verb'),
 ('4760','phrases',2,'a víz mellett ölelkezni','megölelni egymást a víz mellett','"ölelkezni" suggests a romantic embrace; these are friends hugging'),
 ('5673','phrases',0,'mindkét tortát tartani','mindkét süteményt tartani','"torta" is a whole cake; she holds two slices on plates'),
 ('5673','answer',None,'Mindkét tortát tartja.','Mindkét süteményt tartja.','same word as the phrase'),
 ('868','phrases',0,'egyre nagyobb lenni','egyre nagyobbra nőni','"nagyobb lenni" is not Hungarian for "get bigger"; a wave grows'),
 ('277','phrases',2,'két hüvelykujját felmutatni','mindkét hüvelykujját felmutatni','with a possessed paired body part Hungarian says "mindkét", not "két"'),
 ('358','nouns',3,'madárház','madárodú','"madárház" is an aviary; a small wooden nest box is "madárodú"'),
 ('741','phrases',0,'meghajolni a szélben','meghajlani a szélben','"meghajolni" is a person bowing; a tree bends = "meghajlani", as in the answer ("meghajlik")'),
]
for i, f, k, a, b, _ in F:
    cur = d[i][f] if k is None else d[i][f][k]
    assert cur == a, (i, f, cur)
    if k is None: d[i][f] = b
    else: d[i][f][k] = b
json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n = sum(len(v['phrases']) + len(v['nouns']) + 2 for v in d.values())
L = ['# verify b001 hu', '', f'Texts checked: {n} ({len(d)} videos)', '', f'## Fixes ({len(F)})']
for i, f, k, a, b, w in F:
    L.append(f'- {i}, {f if k is None else f"{f}[{k}]"}: "{a}" -> "{b}" ({w})')
L += ['', '## Doubts left unchanged',
 '- "to have ..." phrases (5468, 118, 449, 4055, 721, 368, 30, 100, 741, 690, 92): kept as "hosszú haja van", "nincs haja" etc.; Hungarian has no infinitive for possession, and the finite 3rd person is the dictionary convention.',
 '- 30, phrases[0] / answer: "lapozni az oldalakat" / "Egy tankönyv oldalait lapozza." kept; purists prefer "lapozni" without an object or "forgatni a lapokat", but the wording is common and keeps "oldal" the same as in "sok oldala van".',
 '- 617, answer: "Lila görkorcsolyával korcsolyázik." kept; the phrase has "görkorcsolyázni", repeating it in the answer would be clumsy.',
 '- 4827, question/answer: "a személy" is stiff but exact for "the person" (only a hand is seen).',
 '- 163, answer: "Evőpálcikákkal eszik." kept plural to match the noun "evőpálcikák"; the singular "evőpálcikával" is also usual.',
 '- 694, nouns: "kabát" (chef jacket) and "deszka" (cutting board) kept as plain equivalents; "szakácskabát" / "vágódeszka" would be more exact but add to the English.',
 '- 358, phrases[0] / Q / A: "egy szöget ütni", "Mit üt a kalapács?" kept literal ("beverni" would mean drive in, more than "hit").',
 '- 4015, phrases[0] / answer: "átugrani a víz fölött" kept; "átugrani a vizet" is the tighter form.',
 '- 288: "öltöny" used for the woman\'s oversized suit ("kosztüm" would be the women\'s suit), kept because both people wear the same kind.',
 '- 38, phrases[2]: "az égbe repülni" kept; "felrepülni az égbe" is a little more natural.',
]
open(os.path.join(os.path.dirname(P), 'verify_hu.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(n, len(F))
