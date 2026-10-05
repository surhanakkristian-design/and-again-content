import json,collections
p='tr/b025/fr.json'
f=json.load(open(p),object_pairs_hook=collections.OrderedDict)
fixes=[
 ('6957','question',None,"Que font les deux ouvriers ?","Que prennent les deux ouvriers ?","English asks what they are having; 'Que font' changes the question"),
 ('6957','answer',None,"Ils font une pause café.","Ils prennent une pause café.","matches the corrected question (prendre une pause)"),
 ('6963','nouns',3,"un porte-tubes à essai","un portoir à tubes à essai","standard lab term for a test tube rack"),
 ('6998','phrases',0,"mener un veau sombre","mener un veau foncé","an animal's coat colour is 'foncé', 'sombre' reads as gloomy"),
 ('6998','answer',None,"Elle mène un veau sombre à travers les vagues.","Elle mène un veau foncé à travers les vagues.","same word as the phrase"),
 ('7003','nouns',3,"un bâtiment de bains","un établissement de bains","'bâtiment de bains' is not idiomatic for a bathhouse"),
 ('7019','nouns',1,"des danishs","des feuilletés danois","'danishs' is not French; usual term is feuilletés danois"),
 ('7019','answer',None,"Il tient en équilibre un plateau de danishs.","Il tient en équilibre un plateau de feuilletés danois.","same word as the noun"),
 ('7046','phrases',0,"sauter pour une tête","sauter pour faire une tête","'sauter pour une tête' is clipped; a header is 'faire une tête'"),
 ('7061','phrases',1,"reculer du mur","s'écarter du mur","'reculer du mur' is not idiomatic for stepping back from a wall"),
 ('7066','phrases',0,"acclamer dans son sommeil","pousser des cris de joie dans son sommeil","'acclamer' needs an object; intransitive cheer = pousser des cris de joie (as in 6994/6999)"),
]
for k,fld,i,b,a,why in fixes:
    if i is None:
        assert f[k][fld]==b,(k,fld,f[k][fld]); f[k][fld]=a
    else:
        assert f[k][fld][i]==b,(k,fld,f[k][fld][i]); f[k][fld][i]=a
json.dump(f,open(p,'w'),ensure_ascii=False,indent=1)
lines=[f"- {k} {fld}{'' if i is None else '['+str(i)+']'}: {b} -> {a} ({why})" for k,fld,i,b,a,why in fixes]
open('tr/b025/_fix_lines_b025_fr.txt','w').write('\n'.join(lines))
