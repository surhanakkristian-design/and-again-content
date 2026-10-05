import json
p='fr.json'; d=json.load(open(p))
fixes=[
('7759','phrases',2,"écarter grand les bras","ouvrir grand les bras"),
('7819','phrases',0,"écarter grand les bras","ouvrir grand les bras"),
('7819','answer',None,"Elle écarte grand les bras.","Elle ouvre grand les bras."),
('7768','phrases',2,"s'étirer sur une marche","s'étendre sur une marche"),
('7772','phrases',1,"trotter sur le sable mouillé","courir à petites foulées sur le sable mouillé"),
('7772','nouns',0,"une tour de sauveteur","une tour de surveillance"),
('7789','nouns',3,"une cuve","un bac"),
('7789','answer',None,"Elle est assise dans une cuve d'eau glacée.","Elle est assise dans un bac d'eau glacée."),
('7805','phrases',2,"déployer grand ses ailes","déployer largement ses ailes"),
('7817','phrases',1,"froncer les sourcils de concentration","froncer les sourcils en se concentrant"),
('7817','phrases',2,"tenir une lampe en verre","tenir une lampe électronique en verre"),
('7824','phrases',0,"se pencher bas sur sa planche","s'accroupir sur sa planche"),
('7826','phrases',0,"porter un canard en jouet","porter un canard en plastique"),
('7826','phrases',1,"brandir un renard en jouet","brandir un renard en peluche"),
('7831','phrases',2,"être gênée derrière sa main","se cacher derrière sa main, gênée"),
('7840','nouns',0,"un flamant","un flamant rose"),
('7860','phrases',0,"frapper fort le pneu","frapper fort sur le pneu"),
('7860','answer',None,"Il frappe fort le pneu.","Il frappe fort sur le pneu."),
]
for i,f,k,a,b in fixes:
    if k is None:
        assert d[i][f]==a,(i,f); d[i][f]=b
    else:
        assert d[i][f][k]==a,(i,f,k); d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
