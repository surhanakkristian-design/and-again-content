import json
def V(ph,no,q,a,cap,rec): return {"phrases":ph,"nouns":no,"question":q,"answer":a,"captions":cap,"recall":rec}
def build(lang,data):
    src=json.load(open(f'tr/source_{lang}.json'))
    out={}
    for vid,s in src.items():
        ph,no,q,a,caps,ra=data[vid]
        cap=dict(zip(s['captions'],caps))
        m={}
        for t,f in zip([p['text'] for p in s['phrases']],ph): m[t]=f
        m.update(cap)
        rec=[m.get(r, ra.get(r)) for r in s['recall']]
        assert all(rec),(vid,s['recall'],rec)
        out[vid]=V(ph,no,q,a,cap,rec)
    json.dump(out,open(f'tr/{lang}/fr.json','w'),ensure_ascii=False,indent=1)
de={
"8055":(["transporter un homme","tenir une corde","être suspendu à une corde"],["la montgolfière","les nuages","la corde","l'homme"],"Que fait l'homme ?","Il est suspendu à une grande montgolfière.",["voler en montgolfière","faire atterrir une montgolfière","la nacelle de la montgolfière"],{"hängt an einem großen Heißluftballon":"est suspendu à une grande montgolfière"}),
"236":(["nager dans la mer","sauter en l'air","retomber dans l'eau"],["le ciel","le dauphin","la nageoire caudale","l'eau"],"Que fait le dauphin ?","Il saute hors de l'eau.",["un groupe de dauphins","nager avec un dauphin","nourrir un dauphin"],{"springt aus dem Wasser":"saute hors de l'eau"}),
"624":(["courir après un chapeau","voler au vent","attraper un chapeau"],["les arbres","le chapeau","la fille","l'herbe"],"Que fait la fille ?","Elle court après un chapeau.",["a couru après un chapeau","courra après un chapeau","courir jusqu'au bus"],{"rennt einem Hut hinterher":"court après un chapeau"}),
"7071":(["porter une couronne en or","rouler dans la boue","refléter le ciel gris"],["la couronne","le roi","le quad","la flaque"],"Que fait le roi ?","Il conduit le quad à travers une flaque.",["un jeune roi","roi et reine","s'incliner devant le roi"],{"das Quad":"le quad","steuert das Quad durch eine Pfütze":"conduit le quad à travers une flaque"}),
"4265":(["faire irruption dans la pièce","paresser sur le canapé","calmer un ami furieux"],["la porte","les ailes","le perroquet","le canapé"],"Que fait le perroquet bleu ?","Il calme le perroquet furieux avec un câlin.",["a été calmé par un chevalier","calmer un chien qui aboie","calmer un bébé qui pleure"],{"beruhigt den wütenden Papagei mit einer Umarmung":"calme le perroquet furieux avec un câlin"}),
"461":(["habiller un mannequin","porter une écharpe autour du cou","imiter la pose du mannequin"],["l'écharpe","la chemise","le chat","le mannequin"],"Que fait l'homme ?","Il imite la pose du mannequin.",["porter un mannequin","le mannequin dans la vitrine","habiller un mannequin"],{"ahmt die Pose der Schaufensterpuppe nach":"imite la pose du mannequin"}),
"62":(["soulever un sac lourd","être plein de nourriture","porter des lunettes de soleil"],["la chemise","le pain","les pommes","le sac"],"Que fait l'homme ?","Il met de la nourriture dans le sac.",["laisser tomber un sac","le sac de plage","le sac de sport"],{"packt Essen in die Tasche":"met de la nourriture dans le sac"}),
"8039":(["dégager un chemin étroit à la pelle","courir le long du chemin","gesticuler derrière la fenêtre"],["la neige","la pelle","le chien","le chemin"],"Que fait la femme dehors ?","Elle dégage un chemin dans la neige à la pelle.",["bloquer le passage","le passage étroit","chercher un passage"],{"schaufelt einen Weg durch den Schnee":"dégage un chemin dans la neige à la pelle"}),
"432":(["guider le groupe à travers la forêt","briller dans l'obscurité","porter des lunettes rondes"],["la lanterne","la vallée","la veste","le sac à dos"],"Que fait la femme ?","Elle guide le groupe avec une lanterne.",["a guidé des chevaliers jusqu'à un château","guidera des robots sur Mars","guider un cheval"],{"führt die Gruppe mit einer Laterne":"guide le groupe avec une lanterne"}),
"8056":(["lire un livre","lever les yeux vers l'homme","être assis sur un banc"],["les arbres","le livre","le banc","le chien"],"Que fait l'homme ?","Il lit un livre sur un banc.",["le banc de musculation","peindre un banc","partager un banc"],{"liest auf einer Bank ein Buch":"lit un livre sur un banc"}),
}
es={
"8055":(["transporter un homme","tenir une corde","être suspendu à une corde"],["la montgolfière","les nuages","la corde","l'homme"],"Que fait l'homme ?","Il est suspendu à une grande montgolfière.",["voler en montgolfière","faire atterrir une montgolfière","la nacelle de la montgolfière"],{"cuelga de un globo grande":"est suspendu à une grande montgolfière"}),
"236":(["nager dans la mer","sauter très haut","tomber dans l'eau"],["le ciel","le dauphin","la queue","l'eau"],"Que fait le dauphin ?","Il saute hors de l'eau.",["un groupe de dauphins","nager avec un dauphin","donner à manger à un dauphin"],{"salta fuera del agua":"saute hors de l'eau"}),
"624":(["courir après un chapeau","voler au vent","attraper un chapeau"],["les arbres","le chapeau","la fille","l'herbe"],"Que fait la fille ?","Elle court après un chapeau.",["a couru après un chapeau","courra après un chapeau","courir pour attraper le bus"],{"corre detrás de un sombrero":"court après un chapeau"}),
"7071":(["arborer une couronne en or","avancer dans la boue","refléter le ciel gris"],["la couronne","le roi","le quad","la flaque"],"Que fait le roi ?","Il traverse une flaque sur un quad.",["un jeune roi","le roi et la reine","faire une révérence au roi"],{"el quad":"le quad","atraviesa un charco montado en un quad":"traverse une flaque sur un quad"}),
"4265":(["faire irruption dans la pièce","être vautré sur le canapé","calmer un ami furieux"],["la porte","les ailes","le perroquet","le canapé"],"Que fait le perroquet bleu ?","Il calme le perroquet furieux avec un câlin.",["a été calmé par un chevalier","calmer un chien qui aboie","calmer un bébé qui pleure"],{"calma al loro furioso con un abrazo":"calme le perroquet furieux avec un câlin"}),
"461":(["habiller un mannequin","porter un foulard autour du cou","imiter la pose du mannequin"],["le foulard","la chemise","le chat","le mannequin"],"Que fait le garçon ?","Il imite la pose du mannequin.",["porter un mannequin sur l'épaule","le mannequin de vitrine","habiller un mannequin"],{"está imitando la pose del maniquí":"imite la pose du mannequin"}),
"62":(["soulever un sac lourd","être plein de nourriture","porter des lunettes de soleil"],["la chemise","le pain","les pommes","le sac"],"Que fait l'homme ?","Il remplit le sac de nourriture.",["laisser tomber un sac","le sac de plage","le sac de sport"],{"está llenando la bolsa de comida":"remplit le sac de nourriture"}),
"8039":(["ouvrir un chemin dans la neige","courir sur le chemin dégagé","faire des signes à travers la vitre"],["la neige","la pelle","le chien","le chemin"],"Que fait la fille qui est dehors ?","Elle ouvre un chemin dans la neige.",["barrer le passage","le passage étroit","chercher un passage"],{"está abriendo un camino en la nieve":"ouvre un chemin dans la neige"}),
"432":(["guider le groupe","briller dans l'obscurité","porter des lunettes à monture ronde"],["la lanterne","la vallée","la veste","le sac à dos"],"Que fait la fille ?","Elle guide le groupe avec une lanterne.",["guidait des chevaliers vers un château","guidera des robots sur Mars","guider un cheval"],{"está guiando al grupo con un farol":"guide le groupe avec une lanterne"}),
"8056":(["lire un livre","regarder l'homme","être assis sur un banc"],["les arbres","le livre","le banc","le chien"],"Que fait l'homme ?","Il lit un livre sur un banc.",["le banc de musculation","peindre un banc","partager un banc"],{"está leyendo un libro en un banco":"lit un livre sur un banc"}),
}
build('de',de); build('es',es)
