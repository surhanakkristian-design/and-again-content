import json
p='tr/b030/fr.json'; d=json.load(open(p))
fixes=[
('7908','phrases',1,"fixer quelque chose sous le choc","regarder fixement, sous le choc"),
('7919','phrases',0,"tâter l'objet brillant","donner des petits coups dans l'objet brillant"),
('7920','phrases',1,"froncer les sourcils de concentration","froncer les sourcils, concentré"),
('7935','answer',None,"Il déverse des balles rouges d'un bol.","Il fait tomber des balles rouges d'un bol."),
('7961','phrases',0,"tirer un rideau","écarter un rideau"),
('7964','phrases',2,"sourire à la caméra","sourire de toutes ses dents à la caméra"),
('7974','nouns',0,"une tour de sauveteur","une tour de surveillance"),
('7978','phrases',1,"pagayer avec ses nageoires","battre des nageoires"),
('7982','phrases',0,"arracher la boîte","retirer vivement la boîte"),
('7998','phrases',0,"tenir en équilibre sur une jambe","se tenir en équilibre sur une jambe"),
('7998','answer',None,"Elle tient en équilibre sur une jambe.","Elle se tient en équilibre sur une jambe."),
('8005','phrases',0,"lancer un sac de voyage en bas","lancer un sac de voyage vers le bas"),
('8008','nouns',2,"une nappe de pique-nique","une couverture de pique-nique"),
('8016','phrases',0,"bercer un chaton roux dans ses bras","tenir un chaton roux au creux des bras"),
('8016','answer',None,"Elle berce un chaton roux dans ses bras.","Elle tient un chaton roux au creux de ses bras."),
]
for i,f,ix,a,b in fixes:
    if ix is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][ix]==a,(i,f); d[i][f][ix]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
