import json,os
p=os.path.join(os.path.dirname(__file__),'cz.json')
d=json.load(open(p,encoding='utf-8'))
F=[("4172","phrases",0,"jít přes vodu","jít vodou","'through the water' = vodou; 'přes vodu' means across/over it"),
("4184","answer",None,"Nese míček ke stroji.","Přináší míček ke stroji.","'bringing' = přinášet, same verb as the phrase 'přinést míček zpět'"),
("4187","phrases",2,"spadnout jako poslední","padnout jako poslední","'fall over' (flop down on the spot) = padnout; spadnout = fall off/down from something"),
("4198","phrases",1,"být uvnitř tmavý","být uvnitř tmavá","agreement: díra is feminine"),
("4199","phrases",1,"klesnout na louku","sesunout se na louku","'collapse' of the wing = sesunout se; klesnout only means sink/descend"),
("4213","phrases",2,"mít na sobě zelený náhrdelník","mít na krku zelený náhrdelník","natural wording: a necklace is worn 'na krku' (as 'na nohou', 'na hlavě' elsewhere in the file)"),
("4233","phrases",1,"padat po skalách","padat ze skal","'padat po skalách' is not Czech; water falls 'ze skal'"),
("4237","phrases",2,"být nacpaný mrkví","být nacpaná mrkví","agreement: the crate = bedna, feminine"),
("4237","answer",None,"Krmí koně ve stodole.","Krmí koně ve stáji.","sense: a barn with horse stalls is 'stáj' (matches 'stájový box'); stodola stores hay"),
("4242","phrases",2,"zůstat zavřený","zůstat zavřená","agreement: branka is feminine"),
("4259","phrases",1,"mít na sobě oranžovou šálu","mít na krku oranžovou šálu","natural wording: a scarf is worn 'na krku'"),
]
out=[]
for i,f,ix,a,b,w in F:
    if ix is None:
        assert d[i][f]==a,(i,d[i][f]); d[i][f]=b; n=f
    else:
        assert d[i][f][ix]==a,(i,d[i][f][ix]); d[i][f][ix]=b; n=f+'[%d]'%(ix+1)
    out.append(f"- {i} {n}: {a} -> {b} ({w})")
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
doubts="""- 4177 phrases[2]/nouns/answer: 'ústa' for the baby birds' mouths (Czech would say 'zobáky'); kept because the English says 'mouth' and the noun label is 'a mouth'.
- 4199 nouns: 'a paraglider' -> 'padákový kluzák' (the craft); if the label means the person it should be 'paraglidista'.
- 4191 phrases[1]: 'skákat nahoru a dolů' is literal; 'poskakovat' would be more idiomatic but drops 'up and down'.
- 4267 answer: 'Oddychuje s vyplazeným jazykem' for 'panting'; 'Funí' / 'Rychle dýchá' are alternatives.
- 4270 nouns: 'a banner' -> 'transparent'; if it is an advertising banner at the track, 'reklamní banner' fits better.
- 4185 answer: 'hračkovou myš' is correct but rare; 'plyšovou myš' would be more usual yet the toy is crocheted.
- 4259 phrases[1]: 'otevřít ústa' for a (cartoon) sheep; 'tlamu' is the animal word, kept 'ústa' for the humanised character.
"""
open(os.path.join(os.path.dirname(__file__),'verify_cz.md'),'w',encoding='utf-8').write(
f"# verify cz b012\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes ({len(out)})\n"+"\n".join(out)+"\n\n## Doubts left unchanged\n"+doubts)
print(n,len(out))
