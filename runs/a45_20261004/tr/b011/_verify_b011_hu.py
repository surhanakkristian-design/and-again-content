import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hu.json')
t = json.load(open(p, encoding='utf-8'))
F = [
 ('4065','phrases',0,'a sofőrnek lenni','sofőrnek lenni','predicate noun with "lenni" takes no article in an entry form'),
 ('4066','phrases',2,'átszállni egy bucka fölött','átrepülni egy bucka fölött','"átszállni" reads as changing trains; the bike flies over the mound'),
 ('4104','phrases',1,'elvörösödni az arcán','elvörösödni','"az arcán" is a calque and not said; the verb alone means the face turns red'),
 ('4121','phrases',1,'lángokban feldőlni','lángolva feldőlni','"lángokban" needs "állva"; natural adverbial is "lángolva"'),
 ('4126','phrases',2,'sok világos ablaka van','sok kivilágított ablaka van','night scene with lit windows; "világos ablak" does not mean a lit window'),
 ('4132','phrases',0,'megkefélni a vizes hajat','kikefélni a vizes hajat','hair is "kikefélni"; "megkefélni" is also a vulgar verb, avoided in a learner app'),
 ('4141','answer',None,'Laposan a hátukon fekszenek.','Hanyatt fekszenek.','"laposan a hátukon" is a word-for-word calque; "hanyatt fekszik" is the Hungarian for lying flat on the back'),
 ('4161','phrases',0,'lassan előrehaladni','lassan előrefelé haladni','"előrehaladni" means to make progress; the car physically moves forward'),
]
lines = []
for i, f, k, a, b, why in F:
    cur = t[i][f] if k is None else t[i][f][k]
    assert cur == a, (i, cur)
    if k is None: t[i][f] = b
    else: t[i][f][k] = b
    lines.append(f'- {i}, {f}{"" if k is None else f"[{k}]"}: "{a}" -> "{b}" ({why})')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n = sum(3 + len(v['nouns']) + 2 for v in t.values())
doubts = '''- "to have ..." phrases (4083, 4088, 4094, 4098, 4126, 4134, 4153, 4164): kept as finite "... van / vannak"; Hungarian has no natural infinitive for possession (same decision as in the earlier batches).
- 4070 phrases[0]: "elsőként elengedni a fogást" kept; "a kapaszkodót" would be an alternative, but "elengedni a fogást" is in use.
- 4072 question / answer: "fekszik" for a lagoon kept ("terül el" is the more idiomatic geographic verb), to stay close to "lies".
- 4093 phrases[0]: "folyamatosan egyre nagyobbra nőni" is slightly heavy ("egyre nagyobbra nőni" would do) but correct.
- 4112: "blokk" for a building block kept ("falazóblokk" is the trade word).
- 4119: "halomba omlani" kept ("halomra dőlni" is the fixed idiom, but it loses the literal collapse).
- 4126 phrases[1]: "a veszély szót hirdetni" for a sign that "says" a word; no shorter natural infinitive.
- 4157 noun: "boltív" for the start arch of a race kept ("rajtkapu" is the sports word, but the English label is only "an arch").
- 4153 phrases[2]: "a mezők fölött lógni" for a cloud kept ("lebegni" is commoner).
'''
open(os.path.join(os.path.dirname(p), 'verify_hu.md'), 'w', encoding='utf-8').write(
 f'# b011 hu verification\n\nTexts checked: {n} ({len(t)} videos)\n\n## Fixes ({len(F)})\n' + '\n'.join(lines) + '\n\n## Doubts left unchanged\n' + doubts)
print(n, len(F))
