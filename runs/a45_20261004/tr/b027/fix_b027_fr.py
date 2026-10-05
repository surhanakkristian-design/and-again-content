import json
p='tr/b027/fr.json'
d=json.load(open(p))
fixes=[
('7201','phrases',0,"brandir une feuille fragile","lever une feuille fragile","brandir = wave triumphantly; he gently holds a dry leaf up and turns it"),
('7210','phrases',2,"fouiller dans une caisse","plonger la main dans une caisse","reach into = put a hand into, not rummage"),
('7235','phrases',0,"courir après un ballon échappé","courir après un ballon qui s'échappe","'ballon échappé' unidiomatic for runaway balloon"),
('7235','answer',None,"Elle court après un ballon échappé.","Elle court après un ballon qui s'échappe.","same fix as phrase, consistency"),
('7240','phrases',1,"porter une guirlande de soucis","porter une guirlande d'œillets d'Inde","Indian marigold (Tagetes) = œillet d'Inde; souci = Calendula"),
('7255','phrases',0,"balancer un fer de golf","faire un swing avec un fer de golf","balancer = rock/throw; golf swing = faire un swing"),
('7255','phrases',1,"mordre un club","mordre dans un club","bite on = mordre dans"),
('7255','answer',None,"Elle balance un fer de golf.","Elle fait un swing avec un fer de golf.","same fix as phrase"),
('7261','phrases',0,"dérouler un denim épais","dérouler du denim épais","denim is a mass noun here (cf. noun 'du denim')"),
('7267','phrases',2,"faire jaillir des étincelles","faire jaillir des étincelles vives","'bright' was left out"),
('7267','answer',None,"Elle relie les deux parties du pont.","Elle relie deux parties du pont.","English says 'two parts', not 'the two parts'"),
('7277','phrases',0,"écarter grand les bras","écarter largement les bras","'écarter grand' unidiomatic"),
('7277','answer',None,"Il écarte grand les bras.","Il écarte largement les bras.","same fix as phrase"),
('7280','nouns',0,"un gamin","un gars","gamin = kid; the lads are young adults, lad = gars"),
('7280','question',None,"D'où saute le gamin ?","D'où saute le gars ?","same word as noun"),
('7286','question',None,"Qui la maîtresse de conférences regarde-t-elle ?","Que regarde la maîtresse de conférences ?","English asks 'What', not 'Who'"),
('7290','phrases',0,"fondre à travers la bibliothèque","traverser la bibliothèque en piqué","'fondre à travers' is not French (fondre sur)"),
('7290','answer',None,"La chouette fond à travers la bibliothèque.","La chouette traverse la bibliothèque en piqué.","same fix as phrase"),
('7291','phrases',1,"célébrer les poings levés","exulter les poings levés","célébrer needs an object; intransitive celebrate = exulter"),
('7291','answer',None,"Il célèbre les poings levés.","Il exulte les poings levés.","same fix as phrase"),
('7295','phrases',0,"balancer un lourd marteau","abattre un lourd marteau","balancer un marteau = throw it away; he swings it down onto the link"),
]
out=[]
for vid,f,i,b,a,why in fixes:
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==b,(vid,f,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
    out.append(f"{vid} | {f}{'' if i is None else '['+str(i)+']'} | {b} -> {a} | {why}")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
open('tr/b027/fixlines_b027_fr.txt','w').write('\n'.join(out)+'\n')
print(len(out))
