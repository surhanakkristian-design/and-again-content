import json
p='tr.json'; t=json.load(open(p))
F=[("5392","phrases",1,"kolunu onun etrafına dolamak","kolunu ona dolamak"),
("5418","question",None,"Kadın neyi tutuyor?","Kadın neye tutunuyor?")]
for i,f,k,old,new in F:
    if k is None: assert t[i][f]==old; t[i][f]=new
    else: assert t[i][f][k]==old; t[i][f][k]=new
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
