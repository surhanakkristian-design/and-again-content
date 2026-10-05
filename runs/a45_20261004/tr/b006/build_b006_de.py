import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = 'de'
DATA = """
306 | lange Haare haben | einen kurzen Bart haben | über den Wolken scheinen | die Sonne ; Wolken ; eine Frau ; ein Mann | Worüber fliegen sie? | Sie fliegen über die Wolken.
307 | eine rote Mütze tragen | in den Nebel gehen | weiße Wolle haben | Nebel ; ein Schaf ; eine Mütze ; Gras | Wohin geht der Mann? | Er geht in den Nebel.
308 | lange lockige Haare haben | neben dem Tisch stehen | zu ihnen hinaufschauen | Käse ; Trauben ; eine Frau ; eine Mauer | Was ist auf dem Tisch? | Der Tisch ist voller Essen.
309 | ein Tor schießen | nach dem Ball springen | ins Tor fliegen | ein Fußball ; ein Mann ; das Meer ; Sand | Was spielen sie? | Sie spielen Fußball im Sand.
310 | einen großen Baum berühren | eine graue Jacke tragen | durch die Bäume scheinen | der Himmel ; Bäume ; Gras ; eine Frau | Wo gehen sie spazieren? | Sie gehen in einem Wald spazieren.
311 | eine Gabel hochhalten | die Augen weit öffnen | auf dem Tisch brennen | eine Gabel ; eine Kerze ; Salat ; Nudeln | Was macht die Frau? | Sie isst Nudeln mit einer Gabel.
312 | mit dem Ball dribbeln | ein Foul begehen | in die Pfeife blasen | die Decke ; ein Armband ; ein Abzeichen | Was macht die Schiedsrichterin? | Sie bläst wegen eines Fouls in die Pfeife.
313 | die Foundation verblenden | den Kopf zur Seite drehen | beide Frauen spiegeln | Papageien ; Zöpfe ; ein Spiegel ; Foundation | Was macht die Frau in Weiß? | Sie verblendet Foundation mit einem Schwamm.
314 | im Gras laufen | sehr hoch springen | sich schütteln | ein Fuchs ; ein Baum ; Gras | Was macht der Fuchs? | Er läuft im kalten Gras.
315 | einen Freistoß schießen | eine Abwehrmauer bilden | nach dem Ball hechten | ein Fußball ; Verteidiger ; ein Hügel ; das Spielfeld | Was macht der Spieler in Rot? | Er schießt einen Freistoß.
316 | das Gefrierfach öffnen | die Erbsen halten | das Eis halten | ein Löffel ; Eis ; eine Mütze ; ein Gefrierfach | Was hält die Frau? | Sie hält eine Tüte Erbsen.
317 | Pommes frites zubereiten | Pommes frites essen | eine schwarze Mütze tragen | Pommes frites ; eine Mütze ; Fahrräder ; Lichter | Was macht der Koch? | Er bereitet Pommes frites zu.
318 | sehr traurig aussehen | sein Eis teilen | auf dem Boden liegen | ein Mädchen ; der Himmel ; das Meer ; ein Eis | Was macht das Mädchen in Grün? | Es teilt sein Eis mit seiner Freundin.
319 | auf einem Stein sitzen | auf ein Blatt springen | im Wasser schwimmen | ein Frosch ; ein Stein ; ein Fisch | Was macht der Frosch? | Er sitzt auf einem Stein.
320 | die mit Raureif bedeckte Bank abwischen | ein gefrorenes Blatt berühren | zwischen zwei Pfosten hängen | ein Spinnennetz ; eine Bank ; die Sonne | Was wischt die Frau ab? | Sie wischt den Raureif von der Bank.
321 | einen Pfirsich essen | einen Korb tragen | hinter dem Tisch stehen | eine Ananas ; Trauben ; ein Pfirsich ; ein Korb | Was isst die Frau? | Sie isst einen Pfirsich.
322 | einen riesigen Einsatz machen | sich ängstlich die Augen zuhalten | sich mit hoher Geschwindigkeit drehen | Jetons ; ein Ohrring ; ein Bart | Was macht die Frau? | Sie macht einen riesigen Einsatz.
323 | den Ball prellen | die Frau hochheben | durch die Luft fliegen | ein Ball ; der Himmel ; ein Netz ; Bäume | Was spielen die Freunde? | Sie spielen eine Partie Basketball.
326 | an einer rosa Rose riechen | eine Holzkiste tragen | in der Nähe des Mannes laufen | eine Rose ; eine Frau ; ein Haus ; der Himmel | Woran riecht die Frau? | Sie riecht an einer rosa Rose.
327 | eine rote Tomate essen | einen Hut tragen | in der Nähe der Blumen fliegen | der Himmel ; ein Hut ; ein Mann ; eine Biene | Was isst der Mann? | Er isst eine rote Tomate.
328 | den Knoblauch schälen | in der Küche sitzen | in die Küche gehen | ein Topf ; ein Messer ; Knoblauch | Woran riecht die Frau? | Sie riecht am Knoblauch.
329 | einen weißen Wasserkessel halten | das Gas aufdrehen | Öl in die Pfanne gießen | eine Frau ; ein Topf ; ein Wasserkessel ; Feuer | Was hält der Mann? | Er hält einen weißen Wasserkessel.
331 | eine Orange aufheben | einen Korb tragen | seinen Hut abnehmen | ein Regenschirm ; ein Gentleman ; eine Frau ; ein Korb | Was trägt die alte Frau? | Sie trägt einen Korb mit Orangen.
333 | über ein Seil springen | ein gelbes T-Shirt tragen | die Hände heben | eine Frau ; eine Mauer ; ein Mädchen | Was macht das Mädchen in Jeans? | Es springt über ein Seil.
334 | ein weißes Hemd tragen | einen dunklen Bart haben | in einer Schüssel liegen | ein Glas ; ein Krug ; Zitronen ; der Himmel | Was macht die Frau? | Sie trinkt Limonade aus einem Glas.
336 | ihre Brille putzen | eine blaue Jacke tragen | im Wasser schwimmen | eine Brille ; Blätter ; Wasser ; ein Finger | Was putzt die Frau? | Sie putzt ihre Brille.
338 | auf einen Kontinent zeigen | sich auf seinem Ständer drehen | über dem Schreibtisch leuchten | ein Globus ; ein Lampenschirm ; ein Ohrring ; ein Pullover | Was macht die Frau? | Sie zeigt auf einen Kontinent auf dem Globus.
340 | auf einer Bank sitzen | auf dem Boden liegen | ins Tor fliegen | ein Tor ; der Himmel ; Steine ; eine Frau | Wohin fliegt der Ball? | Der Ball fliegt ins Tor.
341 | auf eine Steinmauer klettern | in ein weißes Hemd beißen | auf dem Dach stehen | der Himmel ; eine Ziege ; ein Dach ; eine Mauer | Wo beißt die Ziege hinein? | Sie beißt in ein weißes Hemd.
342 | eine blaue Schwimmbrille aufsetzen | mit dem Finger zeigen | unter Wasser schwimmen | eine Badekappe ; eine Schwimmbrille ; Wasser ; ein Badeanzug | Was setzt das Mädchen auf? | Es setzt eine blaue Schwimmbrille auf.
344 | etwas Schweres heben | einen Goldbarren putzen | eine Goldkette tragen | eine Brille ; eine Jacke ; ein Goldbarren ; eine Kette | Was putzt die Frau? | Sie putzt einen Goldbarren.
346 | Golf spielen | eine rote Fahne halten | über das Gras rollen | der Himmel ; eine Fahne ; ein Ball ; ein Loch | Was macht die Frau? | Sie spielt Golf.
348 | ein offizielles Dokument stempeln | mit offenen Armen gestikulieren | drei farbige Balken zeigen | ein Flipchart ; ein Stempel ; ein Zeigestock | Was macht die Frau in Lila? | Sie stempelt ein offizielles Dokument.
349 | eine Kappe tragen | ein blaues T-Shirt tragen | auf dem Holz liegen | ein Großvater ; ein Junge ; ein Tisch ; Bäume | Wer spielt mit dem Jungen? | Sein Großvater spielt mit ihm.
350 | einen Rucksack tragen | zur Tür gehen | in einem Sessel sitzen | ein Enkel ; eine Großmutter ; ein Sessel | Wen umarmt die Großmutter? | Sie umarmt ihren Enkel.
351 | ein gelbes T-Shirt tragen | dunkelblaue Shorts tragen | kurze Haare haben | Gras ; ein Vogel ; ein Mädchen ; ein Junge | Wo liegen sie? | Sie liegen im Gras.
352 | seine Hand ausstrecken | einen Finger hochhalten | dunkle Streifen haben | Blumen ; ein Tisch ; eine Kerze ; ein Grill | Was liegt auf dem Grill? | Käse und Gemüse liegen auf dem Grill.
355 | sein Gesicht vergraben | einen langen Riss haben | Reis und Eintopf enthalten | ein Bilderrahmen ; Töpferwaren ; eine Couch ; ein Teller | Wie zeigt der Mann seine Schuldgefühle? | Er vergräbt sein Gesicht in den Händen.
356 | eine große Tasche tragen | sich im Fitnessstudio umsehen | an ihrer Schulter hängen | die Decke ; Gewichte ; ein T-Shirt ; eine Tasche | Was trägt die Frau? | Sie trägt eine Tasche ins Fitnessstudio.
357 | ihre langen Haare bürsten | in die Hände klatschen | bei den Blumen liegen | ein Vorhang ; ein Fenster ; Blumen ; eine Haarbürste | Wer hält die Haarbürste? | Die Frau mit den langen Haaren hält die Haarbürste.
359 | in einem Laufrad laufen | ein paar Körner fressen | voller Körner sein | ein Hamster ; ein Laufrad ; eine Schale | Was macht der Hamster? | Er frisst Körner aus einer Schale.
360 | über den Sitz schauen | einen schwarzen Bart haben | neben dem Mann sitzen | Handdesinfektionsmittel ; ein Hund ; ein Mann ; ein Tisch | Was geben sie sich auf die Hände? | Sie geben sich Handdesinfektionsmittel auf die Hände.
361 | Lutscher in Papier einwickeln | auf einem Haufen liegen | ein Smiley-Gesicht haben | Lutscher ; ein Strauß ; ein Band | Was machen die Hände? | Sie wickeln Lutscher in Papier ein.
362 | auf der Straße tanzen | einen Pfirsich essen | zu der Frau kommen | ein Pfirsich ; ein Hund ; ein Boot ; Schuhe | Wie sieht die Frau aus? | Sie sieht sehr glücklich aus.
363 | sich Notizen machen | den Schreibtisch beleuchten | ein Dokument anzeigen | eine Schreibtischlampe ; eine Strickjacke ; ein Laptop ; Klebezettel | Was macht der Mann? | Er recherchiert an seinem Schreibtisch.
364 | auf Papier zeichnen | einen orangefarbenen Stift halten | in die Kamera lächeln | ein Gesicht ; ein T-Shirt ; ein Stift ; eine Zeichnung | Was macht der Mann? | Er zeichnet mit einem orangefarbenen Stift.
366 | einen Verband abnehmen | einen Turnring umklammern | die Faust in die Luft recken | ein Ärmel ; eine Faust ; eine Kaffeetasse ; Autoschlüssel | Was umklammert die Frau? | Sie umklammert einen Turnring.
367 | ein Eis am Stiel essen | einen Fächer halten | auf dem Boden liegen | der Himmel ; ein Brunnen ; ein Hemd ; ein Kleid | Was isst der Mann? | Er isst ein orangefarbenes Eis am Stiel.
369 | am Motorrad vorbeifahren | zwei Spiegel haben | am Himmel hängen | ein Auto ; eine Straße ; ein Motorrad ; der Himmel | Was macht das Auto? | Es fährt am Motorrad vorbei.
370 | einen Helm aufsetzen | ein Skateboard halten | einen Becher halten | ein Helm ; eine Hose ; ein Skateboard ; der Himmel | Was setzt das Mädchen auf? | Es setzt einen roten Helm auf.
371 | die Basilikumblätter reiben | Kräuter über Spaghetti streuen | die Augenbrauen hochziehen | Kräuter ; ein Bart ; Spaghetti ; ein Teller | Was macht die Frau? | Sie streut Kräuter über die Spaghetti.
372 | mit einem Fußball jonglieren | einen Handstand machen | durch die Luft wirbeln | Wolkenkratzer ; ein Fußball ; ein Schatten | Was macht der Mann? | Er macht Tricks mit einem Fußball.
373 | in ein Stadion gehen | rote Trikots tragen | die Treppe hinuntergehen | der Himmel ; ein Stadion ; ein Mann ; eine Treppe | Was macht der blonde Mann? | Er geht in ein Stadion.
374 | die Straße entlang joggen | ein gleichmäßiges Tempo halten | tätowierte Beine haben | eine Straßenlaterne ; der Himmel ; ein Jogger ; eine Straße | Was macht der Mann? | Er joggt die Straße entlang.
375 | seinen Helmriemen schließen | über die Strecke rasen | das Lenkrad umklammern | die Sonne ; eine Tribüne ; ein Rennwagen ; Asphalt | Was macht der Rennwagen? | Er rast über die Strecke.
377 | vor der Kamera auftreten | Schlagzeug spielen | sich auf einer Couch räkeln | ein Scheinwerfer ; eine Künstlerin ; ein Schlagzeug ; eine Couch | Was macht die Frau? | Sie tritt vor der Kamera auf.
379 | in die Kamera winken | sich die Haare zurückstreichen | einen Vlog aufnehmen | Vorhänge ; Figuren ; Sommersprossen ; ein Laptop | Was macht die junge Frau? | Sie nimmt in ihrem Schlafzimmer einen Vlog auf.
380 | durch ein Drehkreuz gehen | auf einer Holzfläche stehen | den Regen abhalten | ein Rucksack ; eine Brille ; ein Smartphone ; ein Fenster | Wo geht die Frau hindurch? | Sie geht durch ein U-Bahn-Drehkreuz.
381 | eine grüne Weintraube halten | sehr erschrocken aussehen | viele Fotos zeigen | Haare ; eine Weintraube ; Fotos ; ein Waschbecken | Was hält der Mann? | Der erschrockene Mann hält eine Weintraube.
382 | ein Fenster putzen | ein gelbes Werkzeug halten | sehr hoch hängen | ein Helm ; der Himmel ; die Stadt | Was macht die Frau? | Sie putzt ein hoch gelegenes Fenster.
386 | einen schwarzen Bart haben | ihr seine Boote zeigen | in einer Kiste liegen | ein Mann ; eine Frau ; eine Katze ; Boote | Was zeigt der Mann ihr? | Er zeigt ihr seine kleinen Boote.
387 | auf dem Teppich ruhen | seinen Besitzer wecken | unter einer Bettdecke schlafen | ein Teppich ; eine Bettdecke ; ein Kissen ; ein Nachttisch | Was macht der Hund? | Der Hund versucht, seinen Besitzer zu wecken.
388 | seine Hausaufgaben machen | eine runde Brille tragen | mit einem Stift schreiben | Haare ; eine Brille ; ein Stift ; Hausaufgaben | Was macht das Mädchen? | Es macht seine Hausaufgaben.
389 | Honig auf Brot geben | Brot mit Honig essen | auf einer Mauer liegen | eine Frau ; ein Mann ; Brot ; Honig | Was isst der Mann? | Er isst Brot mit Honig.
390 | seine Kapuze hochziehen | einen roten Kapuzenpullover tragen | im Wasser schwimmen | Wasser ; Fahrräder ; ein Kapuzenpullover ; Enten | Was macht der Mann? | Er zieht sich die Kapuze über den Kopf.
391 | auf die Mauer klettern | die Arme heben | auf dem Meer fahren | eine Frau ; ein Boot ; das Meer ; eine Mauer | Was schaut die Frau an? | Sie schaut ein Boot an.
392 | auf einem Pferd reiten | die Frau tragen | auf das Pferd steigen | der Himmel ; eine Frau ; ein Pferd ; Gras | Was macht die Frau? | Sie reitet auf einem Pferd.
393 | einen Schlüssel übergeben | die Holzleiter umklammern | ein paar Chips hinhalten | eine Treppe ; ein Rezeptionist ; ein Tresen ; ein Schlüssel | Was bietet die rothaarige Frau an? | Sie bietet eine Tüte Chips an.
394 | sich das Gesicht abwischen | eine Wasserflasche halten | Luft auf ihn blasen | ein Dach ; eine Wand ; ein Ventilator ; ein Handtuch | Was macht der Mann? | Er wischt sich das Gesicht mit einem Handtuch ab.
396 | ein kleines Geschenk halten | zu dem Mann rennen | auf vier Beinen laufen | Fenster ; eine Umarmung ; ein Hund ; der Boden | Was machen der Mann und die Frau? | Sie umarmen sich.
397 | durch ein Fernglas spähen | eine Strickmütze tragen | zwischen den Bäumen grasen | Baumstämme ; ein Hirsch ; herabgefallene Blätter | Was machen der Mann und die Frau? | Sie jagen im Wald einen Hirsch.
398 | sich den Mund ausspülen | sich die Hände einseifen | sich das Gesicht trocken tupfen | ein Spiegel ; ein Schlafanzug ; Schaum ; ein Waschbecken | Was macht der Junge? | Er seift sich über dem Waschbecken die Hände ein.
399 | am Eis lecken | einen großen Hut tragen | auf der Mauer stehen | der Himmel ; ein Vogel ; ein Hut ; Eis | Was macht der Mann? | Er leckt an seinem Eis.
400 | auf Schlittschuhen um einen Kegel fahren | einen weißen Helm tragen | hinter der Scheibe schreien | Fans ; ein Tor ; Eis | Was machen die Mädchen? | Sie spielen Eishockey.
404 | in die Kamera schauen | hinten raufen | zusammen lachen | Vorhänge ; Poster ; ein Tablet ; ein Schultisch | Was machen die Jungen hinter ihm? | Sie raufen im Klassenzimmer.
405 | als Erste hereinkommen | einen heißen Topf tragen | sehr kurze Haare haben | eine Lampe ; ein Fenster ; ein Feuer ; ein Tisch | Was machen die Leute? | Sie kommen aus dem Schnee herein.
407 | die Arme weit ausbreiten | lange Haare haben | über die Bäume fliegen | Vögel ; eine Insel ; ein Mann ; Wasser | Was machen die Vögel? | Sie fliegen über die Insel.
408 | eine Jacke anziehen | den Mann anlächeln | auf dem Zaun stehen | eine Jacke ; eine Frau ; ein Vogel ; der Himmel | Was trägt der Mann? | Er trägt eine braune Jacke.
410 | ein Marmeladenglas öffnen | der Frau zusehen | am Fenster stehen | Marmelade ; Butter ; ein Korb ; eine Katze | Was macht die Frau? | Sie streicht Marmelade auf das Brot.
411 | mit verschränkten Armen finster dreinblicken | die rote Schleife gewinnen | den Preis verleihen | eine Schleife ; eine Strumpfhose ; Ballettschuhe ; ein Spiegel | Wie sieht die Tänzerin in Türkis aus? | Sie sieht neidisch auf die andere Tänzerin aus.
412 | ein Fußballtrikot auseinanderfalten | ein Trikot überreichen | ein Trikot überziehen | ein Trikot ; ein T-Shirt ; ein Pferdeschwanz ; Fußballschuhe | Was macht die Frau mit den lockigen Haaren? | Sie faltet ein Fußballtrikot auseinander.
413 | eine rote Frucht aufschneiden | das Glas nehmen | auf dem Boden laufen | Saft ; eine Schüssel ; ein Baum ; ein Vogel | Was trinkt der Mann? | Er trinkt ein Glas Saft.
414 | auf der Bahn rennen | über die Latte springen | auf die Matte fallen | der Himmel ; eine Matte ; Bäume ; eine Frau | Was macht die Frau vorne? | Sie springt über die Latte.
415 | über den Sand springen | bei seiner Mutter bleiben | ein Junges tragen | ein Känguru ; die Sonne ; Gras ; der Himmel | Was trägt das große Känguru? | Es trägt sein Junges.
418 | einen Ring aufbiegen | grinsend applaudieren | einen Schlüsselbund herumwirbeln | ein Schlüsselbund ; ein Verkäufer ; ein Eimer ; ein Ärmel | Was macht die Frau? | Sie wirbelt einen Schlüsselbund an ihrem Finger herum.
422 | gegen einen großen Sack treten | an Seilen hängen | ein Bein hoch heben | eine Frau ; ein Sack ; Wolken ; der Boden | Was macht die Frau? | Sie tritt gegen einen großen Sack.
423 | eine Kusshand zuwerfen | ihre Hand küssen | einen großen Hut tragen | ein Hut ; ein Mann ; ein Korb ; eine Flasche | Was macht der Mann? | Er küsst ihre Hand.
424 | das Brot schneiden | sich die Hände abtrocknen | ein Tomatensandwich essen | ein Messer ; ein Hund ; eine Tomate ; eine Frau | Was macht der Mann? | Er schneidet Brot mit einem Messer.
426 | auf eine Leiter steigen | einen roten Apfel pflücken | die Leiter ruhig halten | eine Leiter ; ein Schaf ; ein Baum ; Äpfel | Was macht die Frau? | Sie steigt auf eine Leiter.
427 | am Gras hochklettern | seine Flügel öffnen | in den Himmel fliegen | ein Marienkäfer ; eine Blume ; der Himmel ; Gras | Was macht der Marienkäfer? | Er klettert am Gras hoch.
428 | einen Stein werfen | einen grauen Pullover tragen | einen roten Pullover tragen | der Himmel ; ein Berg ; ein Boot ; ein See | Was macht der Mann? | Er wirft einen Stein in den See.
430 | eine braune Tasche tragen | auf einer Kiste sitzen | einen weißen Bart haben | Häuser ; ein Mädchen ; ein Korb ; ein Boot | Was trägt das Mädchen? | Es trägt eine braune Tasche.
431 | auf dem Sofa liegen | an der Wand stehen | die Fernbedienung nehmen | ein Fenster ; ein Besen ; ein Mann ; ein Tisch | Was macht der Mann? | Er liegt auf dem Sofa.
435 | einen Ledergürtel bürsten | eine Jacke anziehen | unter dem Tisch liegen | eine Frau ; eine Jacke ; ein Gürtel ; ein Tisch | Was trägt der Mann? | Er trägt eine Lederjacke.
436 | lange graue Haare haben | einen gelben Rock tragen | rosa Blüten haben | der Himmel ; ein Baum ; das Meer ; ein Rock | Wohin zeigen die Leute? | Sie zeigen nach links.
437 | ihr Bein hochlegen | die Treppe hinaufrennen | auf dem Hügel stehen | der Himmel ; eine Treppe ; ein Schuh ; ein Bein | Was macht die Frau? | Sie rennt die Treppe hinauf.
438 | in eine Zitrone beißen | einen dunklen Bart haben | auf der Mauer liegen | eine Zitrone ; ein Messer ; eine Hand | Was macht die Frau? | Sie beißt in eine Zitrone.
439 | kalte Limonade trinken | auf dem Boden liegen | in einem Topf wachsen | Limonade ; Blumen ; ein Hund ; eine Frau | Was macht die Frau? | Sie trinkt kalte Limonade.
440 | schwere Gewichte heben | einen breiten Gürtel tragen | am Ende lächeln | ein Mann ; ein Gürtel ; ein Fenster | Was macht der Mann? | Er hebt schwere Gewichte.
442 | sich mit einem Karton abmühen | mit anpacken | hinter einem Karton hocken | eine Katze ; Pappkartons ; ein Bart ; ein Holzboden | Was machen der Mann und die Frau? | Sie stapeln zusammen Pappkartons.
"""
src = json.load(open(f'{HERE}/source.json'))
rows = {}
for line in DATA.strip().split('\n'):
    f = [x.strip() for x in line.split(' | ')]
    assert len(f) == 7, line
    rows[f[0]] = {'phrases': f[1:4], 'nouns': [n.strip() for n in f[4].split(' ; ')], 'question': f[5], 'answer': f[6]}
out = {}
for i, s in src.items():
    r = rows[i]
    assert len(r['nouns']) == len(s['nouns']), i
    out[i] = r
assert len(rows) == len(src)
json.dump(out, open(f'{HERE}/{CODE}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
