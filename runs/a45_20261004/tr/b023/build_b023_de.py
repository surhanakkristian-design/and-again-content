import json, os
D = os.path.dirname(os.path.abspath(__file__))
T = r"""
5607|auf trockenem Gras grasen;in Flammen aufgehen;im Wind flattern|eine Burg;ein Pferd;ein Banner;Schilde|Was macht das Pferd?|Das Pferd grast auf dem Schlachtfeld.
5608|die Knie beugen;die Arme weit ausbreiten;der Springerin ein Zeichen geben|ein Badeanzug;ein Sprungbrett;ein Trainer;eine Bahnleine|Was wird die Springerin gleich tun?|Sie wird gleich ins Becken springen.
5610|auf das Sofa springen;sich neben sie legen;den Hund streicheln|ein Kamin;ein Bild;ein Hund;ein Sofa|Was macht die Frau?|Sie streichelt den Hund.
5613|in die Kamera grinsen;über die Schulter zeigen;unter dem Gewicht ächzen|ein Felsbrocken;Bögen;ein Zopf;ein Zaun|Was trägt die Frau in Schwarz?|Sie trägt einen Felsbrocken auf der Schulter.
5614|eine gelbe Tasche tragen;grünen Saft trinken;ganz hinten gehen|eine Pflanze;Blumen;Fenster;eine Tasche|Was trägt die Frau in Gelb?|Sie trägt einen gelben Anzug.
5615|Nudeln in die Luft werfen;Nudeln in einer Pfanne kochen;Suppe in Becher gießen|Laternen;Leute;eine Pfanne;Becher|Was macht der Koch?|Er kocht Nudeln in einer Pfanne.
5617|Holz schneiden;einen Holzhammer halten;sein Werkzeug anlächeln|eine Säge;ein Hammer;Holz;eine Schürze|Was macht der bärtige Mann?|Er schneidet Holz.
5618|ihre Freundin herumwirbeln;ihren Freundinnen applaudieren;Eiskaffee eingießen|ein Olivenbaum;Dächer;ein Kissen;ein Krug|Was macht die Frau in Blau?|Sie hebt ihre Freundin vom Boden hoch.
5619|den Arm in die Höhe heben;ein weiteres Gericht hereinbringen;Essen in der Pfanne schwenken|Kupferpfannen;eine Hängelampe;Brathähnchen;ein karierter Boden|Was macht die Küchenchefin?|Sie hebt den Arm in die Höhe.
5620|sie hochheben;sein Gesicht berühren;einen roten Mantel tragen|ein Schaufenster;ein roter Mantel;ein Mann|Was trägt die Frau?|Sie trägt einen roten Mantel.
5621|auf Socken auf Zehenspitzen gehen;mit verschränkten Armen dasitzen;neben dem Sessel sitzen|gerahmte Drucke;eine Stehlampe;Schuhe;ein Teppich|Was macht die Frau?|Sie sitzt mit verschränkten Armen da.
5622|durch ein Teleskop schauen;die Arme verschränken;an seinem Arm ziehen|der Himmel;ein Teleskop;eine Lampe;Sand|Wodurch schaut die Frau?|Sie schaut durch ein Teleskop.
5623|einen Stapel Schallplatten umklammern;neben Holzkisten knien;in einem Pappkarton wühlen|Kopfhörer;eine Wandlampe;ein Pappkarton;Holzkisten|Was hält die Frau?|Sie umklammert einen Stapel Schallplatten.
5624|die Flügel ausbreiten;ein Teeglas halten;auf den stehenden Mann zeigen|ein Deckenventilator;eine Laterne;ein Papagei;Minztee|Wo sitzt der Papagei?|Er sitzt auf der Schulter des Mannes.
5625|aus einer Kokosnuss trinken;in einer Hängematte liegen;im Sand schlafen|eine Hängematte;ein Hund;ein Koffer;eine Strandbar|Was macht der Mann?|Er liegt in einer Hängematte.
5627|sich in einem Regal zusammenrollen;herzhaft gähnen;sich nach der Katze ausstrecken|eine Messinglampe;eine Katze;Mosaikfliesen|Wo liegt die Katze?|Sie liegt in einer Lücke zwischen den Gläsern.
5628|den Boden fegen;die Rollschuhe ausziehen;von der Decke hängen|eine Discokugel;eine Frau;ein Besen;Luftballons|Was macht der Mann?|Er fegt den Boden.
5630|eine Etagentorte balancieren;sich zu ihren Füßen kauern;unter Lichterketten tanzen|Weinranken;eine Etagentorte;Fensterläden;ein Korbsessel|Was trägt die Frau in Cremeweiß?|Sie trägt eine Etagentorte.
5631|aufeinander zeigen;sich umarmen;über der Terrasse hängen|Lichter;eine Tür;eine Lampe;ein Sofa|Was machen die beiden Frauen?|Sie zeigen aufeinander.
5632|sich in einer Hängematte räkeln;sich auf seiner Brust zusammenrollen;stirnrunzelnd auf ihn herabblicken|ein Zaun;eine Farbdose;ein Blumentopf;eine Hängematte|Wo räkelt sich der Mann?|Er räkelt sich in einer Hängematte aus Seil.
5633|ihm eine Jacke umlegen;zusammengesunken auf einer Bank sitzen;unter dem Dach leuchten|eine Laterne;eine Bank;ein Hund;ein Regenschirm|Was macht die Frau?|Sie legt ihm eine Jacke um.
5634|ein Spiegelselfie machen;in einer Schublade wühlen;auf der Bettdecke stehen|ein Kronleuchter;ein Hund;ein Handtuch;Kleidung|Was macht der Mann?|Er wühlt in einer Schublade.
5635|eine Zuckerscherbe aufsetzen;die Arme verschränken;von der bemalten Decke hängen|ein Kronleuchter;eine Torte;eine Tischdecke;ein Parkettboden|Was macht die Köchin?|Sie setzt eine Zuckerscherbe auf die Torte.
5637|auf den vorbeifahrenden Zug starren;sich über seine Cornflakes hermachen;auf der Fensterbank dösen|ein Zug;eine Katze;ein Stuhl;Dielen|Worauf starrt die Frau?|Sie starrt auf den vorbeifahrenden Zug.
5638|eine Spinne einfangen;ein rosa Slipdress tragen;ein Blatt Papier halten|eine Spinne;eine Topfpflanze;ein Regal;ein Kissen|Was macht die Frau in Rot?|Sie fängt eine Spinne mit einem Glas ein.
5640|die Faust in die Luft recken;die Arme weit ausbreiten;auf einem Felsvorsprung stehen|eine Bergziege;eine Wasserflasche;Wanderschuhe;Rucksäcke|Was macht der Mann?|Er breitet die Arme weit aus.
5641|trocken bleiben;klatschnass werden;einen umgestülpten Regenschirm halten|ein Balkon;eine Straßenlaterne;ein Taxi;eine Lederjacke|Was hält der Mann?|Er hält einen umgestülpten Regenschirm.
5643|die Frau anflehen;einen Karren schieben;eine große Tasche tragen|eine Schürze;Kisten;eine Tasche;ein Dach|Was macht der Mann vorne?|Er fleht die Frau an.
5644|einen kräftigen blauen Streifen malen;die Leiter festhalten;zu ihm hinaufschauen|der Himmel;eine Farbrolle;ein Streifen;eine Leiter|Was macht der Mann?|Er malt einen kräftigen blauen Streifen.
5645|mit den Armen wedeln;vor Freude jubeln;über den Boden rollen|Bücher;ein Schild;ein Rucksack;ein Wagen|Was macht die Frau mit den Locken?|Sie fährt auf einem Bücherwagen.
5646|sie von hinten umarmen;sich an ihn zurücklehnen;vom Strohdach hängen|eine Laterne;Palmen;ein Eisvogel;ein Kissen|Was macht der Mann?|Er umarmt sie von hinten.
5647|das Gesicht des Hundes in die Hände nehmen;etwas Brot hinhalten;sich von einer Leiter herunterbeugen|eine Schürze;ein Hund;eine Leiter;Schüsseln|Was macht die junge Frau?|Sie nimmt das Gesicht des Hundes in die Hände.
5648|unter der Decke klettern;ein schwarzes T-Shirt tragen;schwarze Leggings tragen|Fenster;Kästen;eine Schüssel;eine Frau|Was macht der Mann oben?|Er klettert unter der Decke.
5649|ein Skateboard hochhalten;in die Hände klatschen;sein Bein berühren|der Himmel;Palmen;eine Flasche|Was macht der Mann in Blau?|Er klatscht in die Hände.
5650|auf die Treppe zeigen;ein kurzärmeliges T-Shirt tragen;ein bauchfreies Top tragen|ein Handlauf;Geldscheine;ein Skateboard|Worauf zeigt der Mann?|Er zeigt auf die Treppe.
5651|einen Kamm halten;sehr überrascht aussehen;am Fenster schlafen|ein Regal;eine Katze;ein Kamm;Haare|Was macht die Katze?|Sie schläft am Fenster.
5653|einen Riesenkürbis schieben;einen kleinen Kürbis überragen;die Augen abschirmen|Zuschauer;eine Kreidetafel;ein Riesenkürbis;eine Palette|Was macht die Frau?|Sie schiebt einen Riesenkürbis auf eine Palette.
5654|auf dem Podest schmollen;eine Goldmedaille hochhalten;die Arme verschränken|ein Flutlicht;ein Blumenstrauß;eine Silbermedaille;ein Podest|Wie fühlt sich die Frau in Blau?|Sie ist verbittert über ihre Silbermedaille.
5655|eine gestreifte Socke tragen;in Gelächter ausbrechen;ein Handtuch herausziehen|eine Socke;ein Pferd;eine Waschmaschine;Turnschuhe|Was trägt das Pferd?|Das Pferd trägt eine gestreifte Socke.
5657|Weihwasser versprengen;die Handflächen aneinanderlegen;die Frau segnen|eine Kirche;ein Priester;Netze;ein Fischerboot|Was macht der Priester?|Er segnet die Frau auf dem Boot.
5658|sich an den Tresen lehnen;vor Freude die Faust in die Luft recken;den Teller nach vorne schieben|Wandfliesen;Kochtöpfe;ein Teller;eine Schürze|Was macht der Koch in Blau?|Er reckt vor Freude die Faust in die Luft.
5659|ihr Handy weglegen;sein Handy hochhalten;ein Croissant nehmen|eine Frau;ein Mann;ein Kaffee;ein Croissant|Was macht der Mann draußen?|Er hält sein Handy.
5662|die Hände in die Luft werfen;den Deckel des Mixers halten;sich Soße aus dem Gesicht wischen|Gewürzgläser;ein Mixer;Tomatensoße;ein Schneidebrett|Womit ist der Mann bedeckt?|Er ist mit Tomatensoße bedeckt.
5663|auf den Sack einschlagen;den Sack festhalten;an Ketten hängen|eine Wand;ein Fenster;ein Boxsack;eine Flasche|Was macht der Mann in Grau?|Er schlägt auf den Sack ein.
5664|die Arme heben;eine Spielfigur ziehen;neben der Lampe sitzen|ein Brettspiel;eine Katze;eine Lampe;eine Pflanze|Was machen die drei Freunde?|Sie spielen ein Brettspiel.
5665|über eine Planke gehen;ein Stahlseil halten;vom Felsvorsprung aus zuschauen|ein Klettergurt;Nebel;eine Klippe;eine Planke|Was macht die Kletterin?|Sie geht über eine schmale Planke.
5667|aufspringen;mit beiden Daumen nach unten zeigen;sich auf der Bühne nach vorne beugen|ein Scheinwerfer;ein Papierflieger;eine Kellnerin;ein Glas Bier|Was macht der Mann in Orange?|Er buht den Komiker auf der Bühne aus.
5668|auf einen Tisch zeigen;einen Stuhl herausziehen;einen Stift halten|eine Pflanze;Blumen;ein Tisch;ein Buch|Wohin zeigt die Frau?|Sie zeigt auf einen Tisch am Fenster.
5669|die Handflächen aneinanderlegen;nach dem Türgriff greifen;eine burgunderrote Bluse tragen|eine Laterne;eine Glastür;eine Karaffe;eine Tischdecke|Was macht der Mann in Schwarz?|Er legt die Handflächen aneinander.
5670|zwei Finger hochhalten;ein grünes Satintop tragen;einen Kontrabass halten|Lichterketten;ein Bogenfenster;ein Kontrabass;ein Leinenanzug|Was machen der Mann und die Frau?|Sie geben sich in einem geräumigen Saal die Hand.
5672|auf die Tafel zeigen;die Augen weit aufreißen;ein dunkelblaues T-Shirt tragen|ein Fenster;eine Pflanze;eine Kaffeetasse;ein Notizbuch|Was macht der junge Mann?|Er schläft an seinem Schreibtisch.
5674|nach einer Fliege schlagen;ein Sandwich umklammern;verärgert die Stirn runzeln|eine Sanddüne;ein Sandwich;eine Thermoskanne;Datteln|Was stört die Frau?|Eine Fliege stört sie.
5675|an einen Stuhl gefesselt sitzen;eine große rosa Schleife binden;das Band festziehen|ein Mast;eine Schleife;ein Klappstuhl|Was macht die Frau in Gelb?|Sie bindet ihm eine Schleife auf den Kopf.
5677|triumphierend beide Arme hochreißen;die Bahn hinunter zeigen;sich überrascht umdrehen|ein Neonschild;Pins;eine Rinne;eine Bowlingbahn|Was macht die Frau?|Sie reißt triumphierend beide Arme hoch.
5678|sich die Fußnägel lackieren;stirnrunzelnd auf seine Uhr schauen;auf dem Samtsofa liegen|eine Stehlampe;eine Katze;Nagellack;ein Couchtisch|Was macht der Mann?|Er schaut stirnrunzelnd auf seine Uhr.
5679|sanft seinen Arm berühren;eine leere Kiste umklammern;ihm ein Dokument zeigen|eine Straßenlaterne;der Himmel;ein Schuppen;eine Holzkiste|Was hält der Mann?|Er hält eine leere Holzkiste.
5680|in Gelächter ausbrechen;am Teetisch knien;über den Tisch watscheln|eine Laterne;Bambus;eine Ente;ein niedriger Tisch|Was macht die Frau?|Sie bricht in Gelächter aus.
5681|die Arme über den Kopf strecken;überrascht nach Luft schnappen;den Arm gerade ausstrecken|eine Discokugel;Scheinwerfer;eine Tanzfläche|Was macht die Frau mit den Locken?|Sie schnappt überrascht nach Luft.
5682|unter Wasser langsam ausatmen;an der Taucherin vorbeischwimmen;zur Oberfläche aufsteigen|Luftblasen;ein Fisch;ein Gewicht;der Meeresboden|Was macht die Frau?|Sie stößt einen Strom von Luftblasen aus.
5683|das Kinn aufstützen;sein Sakko ausziehen;keinen Sand mehr haben|eine Sanduhr;ein Marmortisch;ein weißes Hemd;eine grüne Bluse|Was macht der Mann?|Er zieht sein Sakko aus.
5685|sich vor der Menschenmenge verbeugen;die Arme weit öffnen;in die Hände klatschen|eine Menschenmenge;eine Fahne;ein Mann;eine Rose|Was macht der Mann?|Er verbeugt sich vor der Menschenmenge.
5686|einen Welpen im Arm halten;den Welpen unter dem Kinn kraulen;sich zum Welpen vorbeugen|Trauben;eine Laterne;ein Welpe;ein Wassernapf|Was macht der Mann?|Er krault den Welpen unter dem Kinn.
5687|frische Brote liefern;von ihrem Lastenrad absteigen;voller Brote sein|Lichterketten;eine Radfahrerin;Brote;eine Kiste|Was macht die Radfahrerin?|Sie liefert frische Brote.
5689|die Regler einstellen;ins Mikrofon sprechen;über der Tür leuchten|ein Funkmast;Kopfhörer;ein Mikrofon;ein Mischpult|Was macht der Mann?|Er spricht in ein Mikrofon.
5691|ein Spiegelselfie machen;mit den Flügeln schlagen;sich die Stirn reiben|ein Kronleuchter;ein Papagei;ein Rattanstuhl;ein Rock|Was macht der Papagei?|Er schlägt neben ihrem Gesicht mit den Flügeln.
5695|die sandige Piste überqueren;den Überrollbügel umklammern;bei den Dornbüschen innehalten|der Busch;ein Termitenhügel;eine Antilope;ein Überrollbügel|Was macht die Antilope?|Sie überquert die sandige Piste.
5696|die Blumen bezahlen;das Geld nehmen;unter dem Tisch schlafen|ein Fenster;ein Mann;ein Tisch;ein Hund|Was kauft das Mädchen in Jeans?|Es kauft Blumen.
5697|einen Strauß Dahlien an sich drücken;nach dem Geldschein greifen;warten, bis man an der Reihe ist|ein Glasdach;eine Hängewaage;ein Blumenstrauß;Einwickelpapier|Was macht die dunkelhaarige Frau?|Sie kauft einen Strauß Dahlien.
5698|nach dem Ball rufen;versuchen, seinen Wurf zu blocken;den Ball über den Kopf halten|ein Basketball;ein Korb;ein bauchfreies Top;ein Zaun|Was macht die Frau?|Sie ruft nach dem Ball.
5699|sie zu sich herwinken;auf ihn zuschlendern;am Ufer liegen|der Himmel;ein Laternenpfahl;ein Boot;Sand|Was macht der Mann?|Er winkt sie zu sich her.
5700|die Tür aufhalten;den Lenker umklammern;über die Veranda schlendern|eine Laterne;eine Tür;ein Fahrrad;ein Blumentopf|Was macht der Mann?|Er umklammert den Lenker.
5701|eine Schieferplatte hinhalten;aufgeregt rufen;auf dem steilen Dach knien|Gewitterwolken;das Meer;eine Schieferplatte;Dachziegel|Was macht die Frau?|Sie ruft vom Dach aus.
5702|die Augen schließen;seine Schulter berühren;langsam ausatmen|eine Lampe;ein Mann;eine Frau;ein Motorrad|Was macht der Mann?|Er schließt die Augen.
5703|sich über ihr Eis hermachen;ungläubig gestikulieren;sich unter eine Decke kuscheln|eine Hängelampe;eine Handtasche;eine Decke;ein Sofa|Was macht die Frau im Schlafanzug?|Sie macht sich über ihr Eis her.
5704|einen Stahlträger hochhalten;eine Halteschlaufe umklammern;sich aus der Hocke erheben|ein Stahlträger;ein Kranhaken;ein Umhang;Wolkenkratzer|Was macht die Superheldin?|Sie hebt einen riesigen Stahlträger hoch.
5705|ihren Autoschlüssel hochhalten;zwischen den Autos hindurchgehen;auf einem Auto sitzen|ein Licht;ein Auto;eine Katze;eine Frau|Was macht die Frau?|Sie geht zwischen den Autos hindurch.
5706|triumphierend den Arm hochreißen;die Augen verdrehen;unter dem Tisch liegen|eine Gepäckablage;Pappbecher;Karten;ein Spaniel|Was macht der Mann?|Er verdreht die Augen.
5707|eine Schildkröte im Arm halten;eine Erdbeere hinhalten;an einer Erdbeere knabbern|ein See;eine Schildkröte;ein Blumenbeet;eine Schüssel Erdbeeren|Was macht der Mann?|Er füttert die Schildkröte mit Erdbeeren.
5708|ihren Mantel weit öffnen;einen nassen Hund umklammern;hinter einem Einkaufswagen stehen|eine Straßenlaterne;ein Einkaufswagen;ein Hund;Asphalt|Was macht die junge Frau?|Sie drückt den nassen Hund an ihre Brust.
5711|den Kopf des Elefanten streicheln;gierig Milch aus einer Flasche trinken;den Rüssel nach oben einrollen|Akazien;ein Zaun;eine Milchflasche;eine Decke|Was macht der Mann?|Er füttert ein Elefantenbaby mit der Flasche.
5714|an einem Kiefernzapfen knabbern;von einem Grabstein springen;über bereiftes Gras huschen|Kiefern;ein Eichhörnchen;ein Grabstein;Gras|Was macht das Eichhörnchen?|Das Eichhörnchen knabbert an einem Kiefernzapfen.
5715|einen handgeschriebenen Brief zerschneiden;ein Metalllineal festhalten;Papiere durchsehen|ein Steinbogen;eine Schreibtischlampe;Briefumschläge;ein Brief|Was macht die Frau vorne?|Sie zerschneidet einen Brief mit einer Klinge.
5716|auf die vorbeiziehenden Pinguine zeigen;am Ufer entlangwatscheln;sich um eine Kiste versammeln|eine Mütze;ein Eisberg;Pinguine;ein Rucksack|Was macht die Frau?|Sie zählt die Pinguine am Ufer.
5717|sich immer wieder um sich selbst drehen;die Arme ausstrecken;über die Mauern fliegen|der Himmel;eine Frau;Sand;ein Kreis|Was macht die Frau?|Sie dreht sich in der Mitte um sich selbst.
5718|einen Holzklotz herausziehen;den Sockel festhalten;erschrocken beide Hände heben|eine Glühbirne;ein Turm;ein Buch;ein Becher|Was macht die Frau?|Sie hebt erschrocken beide Hände.
5719|ein Messingsiegel aufdrücken;die Urkunde hochhalten;entzückt lächeln|ein Kronleuchter;eine Topfpflanze;eine Strickjacke;eine Urkunde|Was macht die junge Frau?|Sie lächelt entzückt.
6814|einen Damm entlangfahren;ihren Hut festhalten;auf einer felsigen Insel stehen|eine Abtei;ein Strohhut;ein Regenmantel;ein Fahrrad|Was macht die Frau?|Sie fährt mit dem Fahrrad einen Damm entlang.
6815|eine halbe Zitrone auspressen;mit ihrem Handy filmen;die Menschenmenge überragen|ein Löwe;eine Schutzbrille;ein Teststreifen;eine Schüssel|Was macht die Frau mit der Schutzbrille?|Sie presst eine halbe Zitrone aus.
6816|die Augen abschirmen;Klavier spielen;eine Gießkanne kippen|eine Gießkanne;ein Ventilator;ein Klavier;ein Holzstuhl|Was macht die Schauspielerin?|Sie stellt auf der Bühne einen Sturm dar.
6817|in ein Megafon schreien;auf der Straße knien;einen brennenden Globus zeigen|ein Polizist;eine Aktivistin;eine Fahne;ein Lastwagen|Was macht die Aktivistin?|Sie schreit in ein Megafon.
6818|durch das Büro skaten;schwere Aktenordner tragen;einen grünen Pullover tragen|ein Verwaltungsangestellter;Aktenordner;ein alter Computer;Rollschuhe|Was macht der Verwaltungsangestellte?|Er skatet durch das Büro.
6819|auf einer Plattform stehen;eine blaue Mappe halten;im Wind flattern|eine Fahne;ein Schlepper;eine Admiralin;eine Plattform|Wo steht die Admiralin?|Sie steht auf einer Holzplattform.
6821|einen Blick in ihr Portemonnaie werfen;eine Meeresfrüchteplatte tragen;den Champagner einschenken|ein Kronleuchter;ein Hummer;eine Speisekarte;ein Portemonnaie|Was bringt der Kellner?|Er bringt eine riesige Meeresfrüchteplatte.
6823|schockiert nach oben starren;auf den Gehweg strömen;die enge Straße versperren|ein Fischerboot;ein Hund;eine Kiste;Seetang|Worauf starrt die Frau?|Sie starrt auf ein gestrandetes Boot.
6825|eine weiße Bettdecke ausschütteln;die Kissen zurechtlegen;auf einem Kissen liegen|ein Kirchturm;Geranien;eine Bettdecke;ein Teppich|Was macht die junge Frau?|Sie schüttelt eine Bettdecke über dem Balkon aus.
6826|sich auf einer Bank räkeln;über den Boden rollen;sich über die Mauer lehnen|Vorhänge;ein Windspiel;ein Strohhut;eine Katze|Was macht der Mann?|Er räkelt sich auf einem blauen Kissen.
6827|auf einem weißen Kissen schlafen;den Kopf heben;auf einer Zeitung stehen|eine Frau;ein Kissen;ein Wecker;ein Glas|Was macht die Frau?|Sie schläft auf einem weißen Kissen.
6828|die Arme weit ausbreiten;eine Reihe von Arbeitern anführen;ein Klemmbrett tragen|eine Alarmglocke;eine Warnleuchte;die Decke;ein Schutzhelm|Was macht die Frau?|Sie breitet die Arme weit aus.
6829|einen Reiseführer studieren;zu den Schildern hinaufschauen;eine Papiertüte überreichen|eine Laterne;ein Reiseführer;ein Koffer;ein Ladenschild|Was macht die blonde Frau?|Sie studiert einen Reiseführer.
6830|an Seilen hängen;sich langsam in der Luft drehen;untätig neben den Toren stehen|Aluminium;ein Wellblechdach;ein Gabelstapler;ein Schutzhelm|Was macht der Bootsrumpf?|Der Bootsrumpf hängt an Seilen.
"""
src = json.load(open(f'{D}/source.json'))
rows = {}
for line in T.strip().splitlines():
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{D}/de.json', 'w'), ensure_ascii=False, indent=1)
