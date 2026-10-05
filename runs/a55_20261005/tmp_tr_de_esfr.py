import json, os
HERE=os.path.dirname(os.path.abspath(__file__))
# per lang, per id: phrases, nouns, question, answer, recall-answer (no subject), captions list (in source order)
T={'es':{
'8055':(["einen Mann tragen","ein Seil halten","an einem Seil hängen"],["der Ballon","die Wolken","das Seil","der Mann"],"Was macht der Mann?","Er hängt an einem großen Ballon.","hängt an einem großen Ballon",["Ballon fahren","einen Ballon landen","der Korb des Ballons"]),
'236':(["im Meer schwimmen","sehr hoch springen","ins Wasser fallen"],["der Himmel","der Delfin","der Schwanz","das Wasser"],"Was macht der Delfin?","Er springt aus dem Wasser.","springt aus dem Wasser",["eine Gruppe Delfine","mit einem Delfin schwimmen","einen Delfin füttern"]),
'624':(["einem Hut hinterherrennen","mit dem Wind davonfliegen","einen Hut fangen"],["die Bäume","der Hut","das Mädchen","das Gras"],"Was macht das Mädchen?","Es rennt einem Hut hinterher.","rennt einem Hut hinterher",["rannte einem Hut hinterher","wird einem Hut hinterherrennen","rennen, um den Bus zu erwischen"]),
'7071':(["eine goldene Krone zur Schau tragen","durch den Schlamm fahren","den grauen Himmel spiegeln"],["die Krone","der König","das Quad","die Pfütze"],"Was macht der König?","Er fährt mit einem Quad durch eine Pfütze.","fährt mit einem Quad durch eine Pfütze",["ein junger König","der König und die Königin","sich vor dem König verbeugen"]),
'4265':(["ins Zimmer stürmen","auf dem Sofa herumlümmeln","einen wütenden Freund beruhigen"],["die Tür","die Flügel","der Papagei","das Sofa"],"Was macht der blaue Papagei?","Er beruhigt den wütenden Papagei mit einer Umarmung.","beruhigt den wütenden Papagei mit einer Umarmung",["wurde von einem Ritter beruhigt","einen bellenden Hund beruhigen","ein weinendes Baby beruhigen"]),
'461':(["eine Schaufensterpuppe anziehen","ein Halstuch um den Hals tragen","die Pose der Schaufensterpuppe nachahmen"],["das Halstuch","das Hemd","die Katze","die Schaufensterpuppe"],"Was macht der Junge?","Er ahmt die Pose der Schaufensterpuppe nach.","ahmt die Pose der Schaufensterpuppe nach",["eine Schaufensterpuppe auf der Schulter tragen","die Schaufensterpuppe","eine Schaufensterpuppe anziehen"]),
'62':(["eine schwere Tasche hochheben","voller Essen sein","eine Sonnenbrille tragen"],["das Hemd","das Brot","die Äpfel","die Tasche"],"Was macht der Mann?","Er füllt die Tasche mit Essen.","füllt die Tasche mit Essen",["eine Tasche fallen lassen","die Strandtasche","die Sporttasche"]),
'8039':(["einen Weg durch den Schnee bahnen","den geräumten Weg entlanglaufen","durch die Scheibe zeigen"],["der Schnee","die Schaufel","der Hund","der Weg"],"Was macht das Mädchen draußen?","Es bahnt einen Weg durch den Schnee.","bahnt einen Weg durch den Schnee",["den Durchgang versperren","der schmale Durchgang","einen Durchgang suchen"]),
'432':(["die Gruppe führen","im Dunkeln leuchten","eine Brille mit runder Fassung tragen"],["die Laterne","das Tal","die Jacke","der Rucksack"],"Was macht das Mädchen?","Es führt die Gruppe mit einer Laterne.","führt die Gruppe mit einer Laterne",["führte Ritter zu einer Burg","wird Roboter über den Mars führen","ein Pferd führen"]),
'8056':(["ein Buch lesen","den Mann ansehen","auf einer Bank sitzen"],["die Bäume","das Buch","die Bank","der Hund"],"Was macht der Mann?","Er liest auf einer Bank ein Buch.","liest auf einer Bank ein Buch",["die Hantelbank","eine Bank streichen","sich eine Bank teilen"]),
},'fr':{
'8055':(["einen Mann tragen","ein Seil halten","an einem Seil hängen"],["der Heißluftballon","die Wolken","das Seil","der Mann"],"Was macht der Mann?","Er hängt an einem großen Heißluftballon.","hängt an einem großen Heißluftballon",["Heißluftballon fahren","einen Heißluftballon landen","der Korb des Heißluftballons"]),
'236':(["im Meer schwimmen","in die Luft springen","ins Wasser zurückfallen"],["der Himmel","der Delfin","der Schwanz","das Wasser"],"Was macht der Delfin?","Er springt aus dem Wasser.","springt aus dem Wasser",["eine Gruppe Delfine","mit einem Delfin schwimmen","einen Delfin füttern"]),
'624':(["einem Hut hinterherrennen","mit dem Wind davonfliegen","einen Hut fangen"],["die Bäume","der Hut","das Mädchen","das Gras"],"Was macht das Mädchen?","Es rennt einem Hut hinterher.","rennt einem Hut hinterher",["ist einem Hut hinterhergerannt","wird einem Hut hinterherrennen","rennen, um den Bus zu erwischen"]),
'7071':(["eine goldene Krone zur Schau tragen","Schlamm verspritzen","den grauen Himmel spiegeln"],["die Krone","der König","das Quad","die Pfütze"],"Was macht der König?","Er fährt mit einem Quad durch eine Pfütze.","fährt mit einem Quad durch eine Pfütze",["ein junger König","der König und die Königin","sich vor dem König verbeugen"]),
'4265':(["ins Zimmer stürmen","sich auf dem Sofa räkeln","einen wütenden Freund beruhigen"],["die Tür","die Flügel","der Papagei","das Sofa"],"Was macht der blaue Papagei?","Er beruhigt den wütenden Papagei mit einer Umarmung.","beruhigt den wütenden Papagei mit einer Umarmung",["wurde von einem Ritter beruhigt","einen bellenden Hund beruhigen","ein weinendes Baby beruhigen"]),
'461':(["eine Schaufensterpuppe anziehen","in einen Schal gehüllt sein","die Pose der Schaufensterpuppe nachahmen"],["der Schal","das Hemd","die Katze","die Schaufensterpuppe"],"Was macht der junge Mann?","Er ahmt die Pose der Schaufensterpuppe nach.","ahmt die Pose der Schaufensterpuppe nach",["eine Schaufensterpuppe tragen","Schaufensterpuppe","eine Schaufensterpuppe anziehen"]),
'62':(["eine schwere Tasche hochheben","voller Essen sein","eine Sonnenbrille tragen"],["das Poloshirt","das Baguette","die Äpfel","die Tasche"],"Was macht der Mann?","Er füllt die Tasche mit Essen.","füllt die Tasche mit Essen",["eine Tasche fallen lassen","Strandtasche","Sporttasche"]),
'8039':(["einen Durchgang freischaufeln","den Durchgang entlanglaufen","hinter der Scheibe gestikulieren"],["der Schnee","die Schaufel","der Hund","der Durchgang"],"Was macht die Frau draußen?","Sie schaufelt einen Durchgang im Schnee frei.","schaufelt einen Durchgang im Schnee frei",["den Durchgang versperren","schmaler Durchgang","einen Durchgang suchen"]),
'432':(["die Gruppe führen","den Pfad beleuchten","eine Brille mit runder Fassung tragen"],["die Laterne","das Tal","die Jacke","der Rucksack"],"Was macht die junge Frau?","Sie führt die Gruppe mit einer Laterne.","führt die Gruppe mit einer Laterne",["führte Ritter zu einer Burg","wird Roboter auf dem Mars führen","ein Pferd führen"]),
'8056':(["ein Buch lesen","den Mann ansehen","auf einer Bank sitzen"],["die Bäume","das Buch","die Bank","der Hund"],"Was macht der Mann?","Er liest auf einer Bank ein Buch.","liest auf einer Bank ein Buch",["Hantelbank","eine Bank streichen","sich eine Bank teilen"]),
}}
for lang,tt in T.items():
    src=json.load(open(f'{HERE}/tr/source_{lang}.json')); out={}
    for vid,s in src.items():
        ph,no,q,a,ar,ca=tt[vid]
        assert len(ph)==3 and len(no)==len(s['nouns']) and len(ca)==len(s['captions'])
        m={}
        for x,y in zip([p['text'] for p in s['phrases']],ph): m[x]=y
        for x,y in zip(s['nouns'],no): m[x]=y
        for x,y in zip(s['captions'],ca): m[x]=y
        ra=s['answer'].rstrip('.')
        if lang=='es': ra=ra[0].lower()+ra[1:]
        else: ra=ra.split(' ',1)[1]
        m[ra]=ar
        rec=[m[r] for r in s['recall']]
        out[vid]={'phrases':ph,'nouns':no,'question':q,'answer':a,'captions':dict(zip(s['captions'],ca)),'recall':rec}
    os.makedirs(f'{HERE}/tr/{lang}',exist_ok=True)
    json.dump(out,open(f'{HERE}/tr/{lang}/de.json','w'),ensure_ascii=False,indent=1)
