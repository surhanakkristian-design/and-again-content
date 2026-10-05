import json,os
H=os.path.dirname(os.path.abspath(__file__));p=f'{H}/ua.json';t=json.load(open(p))
F=[
('102','phrases',0,'сидіти, розвалившись на пластиковому стільці','comma before the adverbial participle phrase'),
('102','answer',None,'Він сидить, розвалившись на пластиковому стільці.','comma before the adverbial participle phrase'),
('4858','phrases',0,'перекидати першу кісточку доміно','entry form must be imperfective like the other phrases'),
('15','phrases',0,'пити воду','imperfective entry form (as "їсти суп" in 24)'),
('15','phrases',1,'наливати воду','imperfective entry form'),
('23','phrases',1,'пити воду','imperfective entry form'),
('4538','phrases',2,'напівлежати на дивані','"відкидатися на дивані" is not idiomatic; recline = напівлежати'),
('401','phrases',0,'зашнуровувати свої ковзани','skates are laced, not tied ("зав\'язувати ковзани" is a calque)'),
('401','phrases',1,'тримати руки розведеними в сторони','"тримати руки в сторони" lacks the participle'),
('517','phrases',1,'виїжджати наперед','"виїжджати попереду" = drive out ahead (location), direction needs "наперед"'),
('24','phrases',0,'висувати шухляду','a drawer is pulled out (висувати), "відчиняти" is for doors'),
('6824','phrases',0,'витирати спітніле чоло','no possessive with body parts'),
('13','phrases',1,'витирати рот','no possessive with body parts'),
('795','phrases',1,'витирати волосся','no possessive with body parts'),
('795','answer',None,'Він витирає волосся рушником.','no possessive with body parts'),
('1','phrases',1,'торкатися голови','no possessive with body parts'),
('32','phrases',0,'торкатися бороди','no possessive with body parts'),
('32','answer',None,'Він торкається бороди.','no possessive with body parts'),
('4210','phrases',1,'ховати мордочку','no possessive with body parts'),
('33','answer',None,'Він від болю тримається за опухлу щоку.','no possessive with body parts'),
]
out=[]
for i,f,k,new,why in F:
    old=t[i][f] if k is None else t[i][f][k]
    assert old!=new,(i,f)
    if k is None: t[i][f]=new
    else: t[i][f][k]=new
    out.append(f"- {i}, {f}{'' if k is None else '['+str(k+1)+']'}: {old} -> {new} ({why})")
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(3+len(v['nouns'])+2 for v in t.values())
open(f'{H}/verify_ua.md','w').write(f"# b003 ua verification\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(out)})\n"+"\n".join(out)+"""

## Doubts left unchanged
- 4441 breath -> подих: visible breath is often "пара з рота"; kept, matches the English word.
- 18 seedling -> саджанець: "розсада"/"сіянець" possible for a small plant; kept.
- 733 phrases[3] "показувати біле коло" for a banner displaying a circle: literal, kept.
- 5325 answer uses "Подружжя" instead of "Вони" (avoids singular/plural clash with the question); kept.
- 4190 answer "зустрічає великого лева": could be "зустрічається з"; kept.
- 50 bag -> мішок (piping bag = кондитерський мішок); English says only "bag", kept.
- Possessive "свій" kept with belongings (ключі, квиток, покупки, стрілу), removed only with body parts.
""")
print(n,len(out))
