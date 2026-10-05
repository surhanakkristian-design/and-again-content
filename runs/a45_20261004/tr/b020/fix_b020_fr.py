import json
p='fr.json'; d=json.load(open(p))
fixes=[
('5232','phrases',1,'tourner un winch','actionner un winch','"tourner un winch" is clumsy; the standard verb for working a winch is "actionner"'),
('5242','phrases',1,'être alignés en rangées','être alignés en rangées impeccables','"neat" was left out'),
('5243','phrases',2,'noter des choses','prendre des notes','"noter des choses" is vague and loses "notes"; "prendre des notes" is the natural entry'),
('5246','phrases',1,'noter des choses','prendre des notes','same as 5243'),
('5247','phrases',2,'rester assis sagement contre le mur','rester assis sagement près du mur','"by the wall" = près de, not "contre" (against)'),
('5255','phrases',0,'frapper avec le marteau','frapper du marteau','idiomatic form for banging a gavel'),
('5255','nouns',0,'des armoiries','un blason','English is singular "a coat of arms"; "armoiries" is plural-only, "un blason" keeps the singular with the indefinite article'),
('5256','nouns',0,'des armoiries','un blason','same as 5255'),
('5268','phrases',2,'se mettre à sourire largement','se fendre d\'un large sourire','idiomatic equivalent of "break into a grin"'),
('5271','phrases',0,'crier dans ses mains','crier, les mains en porte-voix','"crier dans ses mains" reads as shouting into the palms; cupped hands round the mouth = "les mains en porte-voix"'),
('5274','phrases',1,'se faire mousser les cheveux','faire mousser ses cheveux','"se faire mousser" also means "to show off"; non-reflexive form avoids the false sense'),
('5274','answer',None,'Il se fait mousser les cheveux trempés.','Il fait mousser ses cheveux trempés.','kept consistent with the phrase fix; avoids the "show off" reading'),
('5302','nouns',0,'des fleurs de cerisier','des fleurs','"de cerisier" added information not in the English "blossom"'),
('5307','nouns',2,'un parquet','des lames de parquet','English plural "floorboards" must stay plural'),
('5321','phrases',0,'tourner sur lui-même','tourner sur soi-même','infinitive entry form takes the generic "soi-même"'),
]
for i,f,ix,b,a,w in fixes:
    if ix is None: assert d[i][f]==b,(i,f); d[i][f]=a
    else: assert d[i][f][ix]==b,(i,f,ix); d[i][f][ix]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
s=json.load(open('source.json')); n=sum(3+len(v['nouns'])+2 for v in s.values())
L=[f'# verify fr b020','',f'Texts checked: {n} (100 videos)','','## Fixes']
for i,f,ix,b,a,w in fixes: L.append(f'- {i} {f}{"" if ix is None else "["+str(ix)+"]"}: {b} -> {a} ({w})')
L+=['','## Doubts left unchanged',
'- 5233/5268 phrases[1] "regarder derrière des barrières": reads naturally as "watch from behind barriers" in context, though "derrière" could also suggest looking behind them.',
'- 5326 "une entraîneuse": correct feminine of entraîneur for a female coach; the word has an old secondary sense (bar hostess) but the gym context makes it clear.',
'- 5311 nouns[3] "un pompon" for "a tassel": the precise term is "un gland", which is ambiguous (acorn) for learners; kept.',
'- 5261 phrases[1] "courir sur l\'herbe" for "jog": jogging nuance softened but natural.',
'- 5312 nouns[1] "une pince" for "tongs": French uses the singular for this tool (like "un jean").',
'- 5297 question "Où va la femme ?" for "Where is the woman walking?": natural, answer "Elle marche vers..." matches.']
open('verify_fr.md','w').write('\n'.join(L)+'\n'); print(n,len(fixes))
