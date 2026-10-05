import json, os
H = os.path.dirname(os.path.abspath(__file__)); CODE = 'de'
DATA = r'''
569|die Eingangstür aufschließen;einen buschigen Schnurrbart haben;einen Pferdeschwanz tragen|eine Postmeisterin;Schlüssel;Pakete;ein Rollwagen|Was macht die Postmeisterin?|Sie schiebt einen Rollwagen voller Pakete.
572|im Garten graben;einen blauen Schal tragen;auf einem Zaun sitzen|ein Vogel;eine Frau;Kartoffeln;ein Eimer|Was macht die Frau?|Sie legt Kartoffeln in einen Eimer.
573|Orangensaft eingießen;eine große Flasche halten;ein Glas nehmen|ein Mann;eine Frau;eine Flasche;Gläser|Was macht der Mann?|Er gießt Orangensaft in Gläser.
574|den Mund weit öffnen;sich an die Brust fassen;kurze schwarze Haare haben|ein Baum;ein Pinsel;eine Dose;Puder|Was ist in der Dose?|In der Dose ist Puder.
575|die Hände in die Luft werfen;in ihrer Tasche kramen;eine Powerbank hochhalten|eine Powerbank;Tauben;Rosen;eine Bank|Woran schließen sie das Handy an?|Sie schließen es an eine Powerbank an.
576|an ihrem Schreibtisch beten;die Hände zusammenpressen;nach oben schauen und weinen|eine Frau;ein Laptop;Bücher;eine Lampe|Was macht die Frau?|Sie betet an ihrem Schreibtisch.
577|den Regen vorhersagen;in Gelächter ausbrechen;einen plötzlichen Schauer bringen|eine Gewitterwolke;ein Regenschirm;ein Schultertuch;Gras|Was macht die Frau?|Sie sucht unter einem gelben Regenschirm Schutz.
578|ein Motorrad herausschieben;den Benzintank polieren;ihr auf die Schulter klopfen|ein Bandana;ein Benzintank;ein Motor;Pflastersteine|Was macht die Mechanikerin?|Sie präsentiert stolz ihr Motorrad.
579|neuen Code tippen;zum Laptop hin deuten;der gezeichneten Strecke folgen|ein Roboter;ein Laptop;ein Pferdeschwanz;ein Bart|Was macht die Frau?|Sie programmiert einen kleinen Roboter.
580|einen Mantel hochhalten;einen Korb tragen;eine Brille tragen|ein Korb;ein Mantel;der Himmel;eine Brille|Was macht die große Frau?|Sie schützt ihre Freundin vor dem Regen.
581|eine Sonnenblume umklammern;ein Schild mit einem Baum tragen;in der Brise flattern|eine Sonnenblume;eine Palme;der Himmel;eine Menschenmenge|Was machen die Leute?|Sie protestieren mit bemalten Schildern.
582|auf einem Stuhl sitzen;die Arme verschränken;ihre Schulter berühren|ein Stuhl;eine Frau;ein Fenster;ein Tisch|Wie fühlt sich die Frau?|Sie ist stolz auf ihren neuen Stuhl.
584|einen Handstand vorführen;ihm das Gegenteil beweisen;vor Staunen nach Luft schnappen|nackte Füße;Leggings;eine Bank;eine Strickweste|Was macht die junge Frau?|Sie führt einen Handstand vor, um ihm das Gegenteil zu beweisen.
585|in der Öffentlichkeit Musik machen;auf einer Kiste sitzen;Wasser in die Höhe schießen|eine Straßenlaterne;Männer;ein Akkordeon;ein Koffer|Was macht die junge Frau?|Sie spielt in der Öffentlichkeit Akkordeon.
588|rote Stiefel tragen;schwarze Stiefel tragen;weit weg stehen|ein gelber Regenmantel;ein Vogel;rote Stiefel;eine Pfütze|Was machen die zwei Personen?|Sie springen in eine große Pfütze.
589|etwas Rotes halten;einen kurzen Bart haben;über das Gras rennen|ein Hund;Gras;ein Mann;ein Seil|Was machen der Mann und die Frau?|Sie ziehen an einem dicken Seil.
590|schnelle Schläge austeilen;Pratzen hochhalten;an einer Kette hängen|eine Backsteinmauer;ein Boxsack;Boxhandschuhe;Shorts|Was macht die Frau?|Sie schlägt auf die Pratzen.
591|kräftige Schläge austeilen;die Leiter festhalten;an der Decke schwingen|eine Kette;ein Boxsack;Boxhandschuhe;Shorts|Was macht der Mann?|Er schlägt auf den Boxsack ein.
592|einen dunklen Bart haben;ein weißes T-Shirt tragen;die Straße hinunterrollen|der Himmel;ein Lieferwagen;eine Straße|Was machen die zwei Männer?|Sie schieben einen weißen Lieferwagen.
593|kurze lockige Haare haben;lange dunkle Haare haben;auf dem Boden schlafen|ein Fenster;Schlafanzüge;ein Bett;ein Hund|Was tragen der Mann und die Frau?|Sie tragen Schlafanzüge.
594|die Latte überqueren;eine grüne Fahne schwenken;die Fäuste hochreißen|eine Querlatte;eine Fahne;ein Pferdeschwanz;eine Matte|Wie qualifiziert sich das Mädchen?|Es qualifiziert sich, indem es die Latte überquert.
595|grüne Blätter fressen;sich das Gesicht waschen;über das Gras springen|der Himmel;ein Kaninchen;Gras;Blätter|Was frisst das Kaninchen?|Es frisst grüne Blätter.
597|durch einen Schläger schauen;hinter dem Netz stehen;in die Kamera lächeln|Blumen;ein Ball;ein Netz;ein Schläger|Was hält die Frau?|Sie hält einen schwarzen Schläger.
598|die Arme weit ausbreiten;ein weißes Hemd tragen;auf vier Beinen laufen|ein Dach;ein Baum;ein Hund;ein Boot|Was macht das Mädchen?|Es tanzt im Regen.
599|mit einem bunten Ball dribbeln;den Mann in Schwarz angreifen;einen weißen Ball kontrollieren|ein Tor;ein Fußball;Rasen;ein Dach|Was machen die zwei Männer?|Sie kämpfen um den Ball.
600|auf zwei Beinen stehen;ein Pizzastück ziehen;große schwarze Räder haben|eine Ratte;Pizza;Stufen;ein Fenster|Was macht die Ratte?|Sie zieht ein Pizzastück.
601|sich mit einem Rasierer rasieren;auf seine Uhr zeigen;auf dem Waschbecken laufen|ein Rasierer;eine Lampe;ein Spiegel;ein T-Shirt|Was macht der Mann in Weiß?|Er rasiert sich mit einem Rasierer.
604|einen roten Apfel halten;Obst verkaufen;einen langen Kassenbon drucken|ein Kassenbon;Äpfel;Birnen;Flaschen|Was schaut sich der Mann an?|Er schaut sich einen langen Kassenbon an.
606|in einem Käfig sitzen;einen schwarzen Bart haben;lockige Haare haben|ein Rezept;ein Vogel;Pfannkuchen;ein Mann|Was essen der Mann und die Frau?|Sie essen Pfannkuchen.
607|auf dem Boden liegen;den Kühlschrank berühren;einen schwarzen Bart haben|ein Kühlschrank;ein Hund;ein Mann;eine Frau|Wo stehen der Mann und die Frau?|Sie stehen neben dem Kühlschrank.
608|das Lenkrad umklammern;vor Erleichterung lachen;auf der Windschutzscheibe ruhen|ein Lenkrad;ein Armaturenbrett;ein Scheibenwischer;ein Sweatshirt|Was umklammert die Fahrerin?|Sie umklammert das Lenkrad.
609|einen roten Rucksack tragen;seine Stiefel ausziehen;einen blauen Schal tragen|der Himmel;ein See;ein Felsen;ein Rucksack|Was machen der Mann und die Frau?|Sie ruhen sich auf dem Gras aus.
610|drei Bänder tragen;den großen Kürbis umarmen;groß und orange sein|ein Band;ein Kürbis;ein Hut;Fahnen|Was ist auf dem großen Kürbis?|Auf dem Kürbis ist ein blaues Band.
613|in den Ring steigen;blaue Handschuhe tragen;eine Wasserflasche halten|ein Ring;ein Mann;eine Wand|Was macht der Mann?|Er boxt im Ring.
615|über das Wasser fliegen;den Fluss hinuntertreiben;am Fluss wachsen|ein Fluss;ein Vogel;Blätter;Steine|Was treibt den Fluss hinunter?|Zwei Blätter treiben den Fluss hinunter.
616|rote Haare haben;einen grauen Pullover tragen;groß und rund sein|ein Felsen;der Himmel;ein Fluss|Worauf stehen sie?|Sie stehen auf einem großen Felsen.
618|ein Seil festbinden;hinter dem Karren stehen;ein großes Rad haben|ein Baum;ein Seil;ein Rad;Schlamm|Was macht der kräftige Mann?|Er zieht einen Karren mit einem Seil.
619|einen Korb hochziehen;in der Gasse warten;eine Mauer entlangschlendern|Kräuter;Orangen;ein Korb;ein Seil|Was macht die Frau?|Sie zieht einen Korb mit Orangen hoch.
621|neben der Reihe stehen;einen rosa Hut tragen;eine rote Spitze haben|der Himmel;ein Hut;Pflanzen;der Boden|Was machen die Leute?|Sie pflanzen kleine Pflanzen in einer Reihe.
622|an einem Gummiband ziehen;sein Gesicht berühren;auf der Straße laufen|ein Gummiband;eine Frau;ein Mann;eine Kiste|Was macht die Frau?|Sie zieht an einem Gummiband.
623|auf sein Handy schauen;ihm einen Kaffee bringen;die Füße hochlegen|ein Handy;eine Sonnenbrille;ein Stiefel;eine Gabel|Was macht der junge Mann?|Er schaut auf sein Handy.
626|aus einem Becher trinken;dem Rennen zuschauen;auf ihre Uhr schauen|ein Becher;eine Uhr;der Himmel;eine Läuferin|Was macht die Läuferin?|Sie trinkt aus einem Becher.
627|über den Teppich stolzieren;ihre Freundin filmen;ganz still sitzen|ein Teppich;Lichterketten;ein Kamin;eine Stehlampe|Was macht die Frau in Blau?|Sie stolziert über den Teppich.
628|einige Bücher einpacken;ein Buch halten;auf dem Boden weinen|Regale;eine Brille;Bücher;Kartons|Was macht die Frau?|Sie weint auf dem Boden.
629|die Tür schließen;eine Jacke aufhängen;eine gelbe Jacke tragen|eine Frau;ein Mann;Tassen;Holz|Was schließt die Frau?|Sie schließt die große Holztür.
630|an einem langen Seil ziehen;das große Steuerrad halten;beide Arme heben|eine Seglerin;ein Steuerrad;ein Seil;ein Segel|Was macht die Seglerin?|Sie zieht an einem langen Seil.
631|eine Gurke schneiden;den Salat mischen;eine kleine Tomate essen|eine Frau;ein Mann;Salat;ein Tisch|Was macht der Mann?|Er macht einen Salat.
632|Salz auf Tomaten geben;kurze dunkle Haare haben;draußen vor dem Fenster stehen|ein Vogel;Salz;Tomaten;Brot|Was macht die Frau?|Sie gibt Salz auf die Tomaten.
634|trockenen Sand rieseln lassen;mit einem Stock zeichnen;die Zeichnung bedecken|eine Frau;ein Mann;eine Welle;Sand|Was macht der Mann?|Er lässt Sand in seine Hand rieseln.
635|ihre Sandalen anziehen;grüne Shorts tragen;auf einer Bank stehen|der Himmel;ein Vogel;eine Bank;Sandalen|Was tragen sie an den Füßen?|Sie tragen Sandalen.
636|ein Sandwich machen;das Sandwich durchschneiden;hinter dem Korb stehen|Bäume;eine Ente;ein Korb;ein Sandwich|Was macht die Frau?|Sie macht ein Sandwich.
638|grüne Soße gießen;eine Kartoffel essen;auf dem Gras sitzen|ein Mann;eine Frau;ein Hund;Soße|Was macht der Mann?|Er gießt grüne Soße.
639|die Würstchen wenden;einen Hotdog essen;in einer Pfanne liegen|ein Hut;ein Zelt;ein Vogel;Würstchen|Was isst die Frau?|Sie isst einen Hotdog.
640|zwei Gewichte hochnehmen;seine großen Arme zeigen;auf die Waage zeigen|ein Mann;eine Frau;der Boden;eine Waage|Worauf steht der Mann?|Er steht auf einer Waage.
641|etwas Mehl schütten;einen langen Zopf tragen;auf der Waage hocken|Kupferpfannen;eine getigerte Katze;eine Rührschüssel;eine Küchenwaage|Wo hockt die Katze?|Sie hockt auf der Küchenwaage.
642|auf ihren Unterarm zeigen;einen buschigen Bart haben;sein vernarbtes Schienbein zeigen|ein Trenchcoat;eine Glühbirne;eine Narbe;Becher|Was zeigt der blonde Mann?|Er zeigt eine Narbe an seinem Schienbein.
644|sich den Mund zuhalten;eine weiße Tasche tragen;ein Handy hochhalten|eine Brille;Haare;eine Tasche;der Boden|Was macht die verängstigte Frau?|Sie hält sich den Mund zu.
645|einen Kreis zeichnen;einen schwarzen Stift halten;eine Uhr tragen|ein Terminplan;ein Mann;ein Notizbuch;Ordner|Was zeichnet der Mann?|Er zeichnet einen Kreis auf den Terminplan.
647|mit einer Schere Haare schneiden;in einen Spiegel schauen;auf einem Stuhl sitzen|eine Schere;ein Kamm;ein Handtuch;eine Brille|Was macht die Frau mit Brille?|Sie schneidet mit einer Schere Haare.
649|den jungen Mann ausschimpfen;einen Strohhut umklammern;die Arme verschränken|ein Kopftuch;eine Schürze;ein Tor;Kohlköpfe|Was macht die alte Frau?|Sie schimpft den jungen Mann aus.
650|über den Boden krabbeln;einen langen Zopf tragen;über den Karton spähen|eine Schraube;ein Karton;ein Golden Retriever;ein Daumen|Was sucht der Mann?|Er sucht eine fehlende Schraube.
651|eine Schraube festziehen;das Holzregal festhalten;auf dem Sofa hocken|ein Schraubenzieher;Bücher;eine Katze;eine Zimmerpflanze|Was macht die Frau?|Sie zieht eine Schraube mit einem Schraubenzieher fest.
652|gegen die Felsen schlagen;ein weißes Hemd tragen;kurze Haare haben|das Meer;eine Frau;ein Mann;Felsen|Was machen sie?|Sie springen ins Meer.
653|ein Kissen hochheben;auf die Schlüssel zeigen;an der Tür liegen|Schlüssel;eine Tür;eine Katze;ein Mann|Worauf zeigt der Mann?|Er zeigt auf die Schlüssel in der Tür.
654|ein Geheimnis flüstern;ihrer Freundin zuhören;über die Mauer schauen|der Himmel;eine Lampe;ein Berg;eine Brille|Was macht die Frau in Gelb?|Sie flüstert ihrer Freundin ein Geheimnis zu.
655|eine schwarze Linie malen;ins Zimmer rennen;in eine kleine Tröte blasen|ein Hut;eine Brille;Papier;ein Tisch|Was macht die Frau in Blau?|Sie malt eine schwarze Linie auf Papier.
656|die Schachuhr drücken;eine khakifarbene Jacke tragen;beide geballten Fäuste heben|Bogenfenster;ein Seil;eine Schachuhr;ein Schachbrett|Was macht die Schachspielerin?|Sie drückt nach ihrem Zug die Schachuhr.
657|das Essen servieren;etwas Wasser eingießen;sein Essen anschauen|eine Frau;ein Glas;eine Gabel;ein Tisch|Was macht die Frau?|Sie serviert dem Mann Essen.
660|ihrer Freundin die Haare einschäumen;sich über die Waschschüssel beugen;das Seifenwasser auffangen|Bananenblätter;ein Wasserhahn;eine Waschschüssel;ein Hocker|Was macht die Frau in Grün?|Sie schäumt ihrer Freundin die Haare ein.
661|sein großes Maul öffnen;ganz nah herankommen;in einer Gruppe schwimmen|Fische;ein Hai;Wasser|Was macht der Hai?|Der Hai öffnet sein großes Maul.
662|einen Stern zeichnen;kurze Haare haben;Gras fressen|ein Pferd;ein Anspitzer;ein Notizbuch;eine Schüssel|Was zeichnet die Frau?|Sie zeichnet einen Stern.
663|Rasierschaum auftragen;in den Spiegel schauen;seinen Freund beobachten|Lampen;ein Spiegel;Rasierschaum;ein Wasserhahn|Was macht der Mann in Blau?|Er trägt Rasierschaum auf sein Gesicht auf.
664|dem Mann das Gesicht rasieren;in einem Stuhl liegen;am Fenster sitzen|Flaschen;eine Katze;ein Mann;eine Schüssel|Was macht die Frau?|Sie rasiert dem Mann das Gesicht.
666|ein Hemd anziehen;den Mann beobachten;sein Hemd zuknöpfen|ein Vogel;eine Frau;ein Hemd|Was macht der Mann?|Er zieht ein blaues Hemd an.
667|sich an den Kopf fassen;auf dem Gehweg liegen;vor Schreck nach Luft schnappen|ein Fußgänger;ein Helm;ein Motorroller;der Gehweg|Was macht die Frau?|Sie fasst sich vor Schreck an den Kopf.
668|ihre Schuhe zubinden;Kaffeebecher halten;durchs Wasser laufen|eine Tür;eine Hose;Schuhe;der Boden|Was macht die Frau?|Sie bindet ihre braunen Schuhe zu.
669|einen Korb tragen;ihr das Brot geben;mit Münzen bezahlen|eine Lampe;eine Brille;Brot;ein Hut|Was macht die Frau?|Sie kauft Brot in einem Laden.
671|einen kurzen Bart haben;einen blauen Rucksack tragen;einen langen Hals haben|der Himmel;ein Lama;ein Mann;eine Frau|Was machen die zwei Personen?|Sie schreien in der Nähe eines Lamas.
672|ein Handtuch halten;ein blaues T-Shirt tragen;auf der Dusche stehen|ein Vogel;eine Dusche;ein Handtuch;ein Mann|Was macht die Frau?|Sie duscht am Strand.
674|sich die Nase putzen;ihr eine Tasse bringen;am Fenster wachsen|eine Pflanze;eine Tasse;eine Decke;ein Tisch|Was macht die Frau?|Die kranke Frau putzt sich die Nase.
675|sich über einen Eimer beugen;eine Brille tragen;leuchtend blau werden|ein Boot;ein Netz;ein Mann;Eimer|Was macht der blonde Mann?|Er streicht die Seite des Bootes.
678|die Seide hochhalten;schulterlange Haare haben;auf der Theke kauern|ein Ventilator;Seide;eine Katze;eine Theke|Was macht die Frau in Beige?|Sie drückt Seide an ihre Wange.
679|das Silber putzen;Ohrringe anlegen;über ihrem Kopf hängen|eine Lampe;Silber;eine Frau|Was macht die Frau?|Sie putzt Silber mit einem Tuch.
681|in die Kamera schauen;das Auto fahren;lang und gerade sein|ein Spiegel;eine Straße;ein Mann;eine Frau|Was machen sie?|Sie singen im Auto.
683|das Wasser aufdrehen;einen gelben Schwamm halten;einen sauberen Teller zeigen|ein Mann;eine Frau;ein Spülbecken;Teller|Was spülen sie im Spülbecken?|Sie spülen Teller im Spülbecken.
684|am Tisch sitzen;die Tür öffnen;die zwei Mädchen umarmen|eine Tür;ein Mädchen;ein Löffel;eine Gabel|Was machen die zwei Schwestern?|Die zwei Schwestern umarmen sich.
685|Hüte anprobieren;einen kleinen Spiegel halten;Hüte verkaufen|der Himmel;ein Hut;Haare;ein Kleid|Was macht das Mädchen?|Es probiert Hüte an.
687|Skateboard fahren;in die Luft springen;über der Stadt scheinen|die Sonne;Häuser;ein Junge;ein Skateboard|Was macht der Junge?|Er fährt Skateboard.
688|Gesichtscreme auftragen;sich den Arm reiben;ihre Wangen berühren|Haut;der Himmel;Pflanzen;ein T-Shirt|Was macht die Frau?|Sie trägt Creme auf ihre Haut auf.
689|ihren Rock halten;sich im Kreis drehen;weiße Schuhe tragen|ein Rock;ein T-Shirt;Vögel;Bäume|Was trägt die Frau?|Sie trägt einen gelben Rock.
691|ein graues Auto bewachen;einen Holzstock schwingen;draußen geparkt sein|ein Soldat;Stacheldraht;eine Betonmauer;ein Feldweg|Was macht der Soldat?|Er bewacht das Auto mit einem Stock.
692|die Arme hochstrecken;unter einer Decke schlafen;ein Buch lesen|eine Katze;eine Lampe;eine Decke;ein Kissen|Was macht der Mann?|Er schläft unter einer Decke.
693|sich die Augen reiben;am Fenster schlafen;auf ihrem Schoß liegen|ein Fenster;ein Sitz;ein Pullover;ein Notizbuch|Wie fühlt sich die Frau?|Sie fühlt sich sehr schläfrig.
695|sich auf ihre Hand stützen;einen grünen Schal tragen;über das Boot fliegen|die Sonne;Vögel;ein Boot;das Meer|Was machen die Leute?|Sie lächeln auf dem Boot.
696|über den Mann lachen;den Rauch wegwedeln;in den Himmel aufsteigen|Rauch;eine Frau;ein Mann;Blätter|Was macht der Mann?|Er wedelt den Rauch weg.
697|eine rote Jacke tragen;einen schwarzen Bart haben;eine Zigarette anzünden|eine Lampe;eine Zigarette;eine Jacke|Was macht der Mann in Rot?|Er raucht eine Zigarette.
698|einen Smoothie eingießen;mehr Obst hinzufügen;das Obst mixen|ein Smoothie;Bananen;Erdbeeren;eine Frau|Was macht die Frau in Orange?|Sie gießt einen Smoothie in ein Glas.
699|etwas Käse schmuggeln;die Schranke heben;mit Heu beladen sein|ein Wächter;Heu;eine Schranke;ein Karren|Was schmuggelt der Bauer?|Er schmuggelt Käse unter dem Heu.
700|sich sehr langsam bewegen;auf ein Blatt klettern;auf dem Weg liegen|eine Schnecke;ein Blatt;Gras|Was macht die Schnecke?|Sie klettert auf ein Blatt.
701|sich über den Sand bewegen;die Zunge herausstrecken;unter der Schlange liegen|eine Schlange;ein Felsen;Sand;der Himmel|Wo liegt die Schlange?|Sie liegt auf einem schwarzen Felsen.
'''
src = json.load(open(f'{H}/source.json')); rows = {}
for line in DATA.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
assert len(out) == len(rows) == len(src)
json.dump(out, open(f'{H}/{CODE}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
