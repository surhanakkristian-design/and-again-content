import json, os
H = os.path.dirname(os.path.abspath(__file__))
R = """
4063|über den Wolken baumeln;den Mann loslassen;auf die Wolken zustürzen|Gurte;ein Gurtzeug;Stiefel;Wolken|Was macht der Mann?|Er stürzt auf die Wolken zu.
4064|ein riesiges Nest stützen;auf dem Mast balancieren;eine winzige Kamera tragen|ein Nest;Stromleitungen;ein Mast;ein Feld|Wohin fliegt der Sittich?|Er fliegt auf das Nest auf dem Mast zu.
4065|der Fahrer sein;seine Zunge zeigen;sich hinter einem Sitz verstecken|Bäume;ein Fahrer;eine Katze;ein Lenkrad|Wer sitzt auf dem Fahrersitz?|Ein weißer Hund sitzt auf dem Fahrersitz.
4066|einen winzigen Helm zurechtrücken;ein Geländemotorrad fahren;über einen Erdhügel segeln|ein Helm;ein Papagei;ein Geländemotorrad;Erde|Was macht der Papagei?|Er fährt ein winziges Geländemotorrad.
4067|in den See springen;die Tannen spiegeln;über dem Wasser aufragen|der Himmel;Tannen;kleine Wellen;ein Felsblock|Was spiegelt der See?|Der See spiegelt die Tannen.
4068|einen Tigerhai streicheln;einen dunklen Schatten werfen;neben einem Hai gleiten|eine Taucherin;ein Hai;ein Schatten;der Meeresboden|Was macht die Frau?|Sie streichelt einen Tigerhai.
4069|eine Angel halten;aus dem Meer auftauchen;die Meerjungfrau böse anstarren|der Himmel;eine Taube;eine Angel;Planken|Was hält der kleine Vogel?|Er hält eine dünne Angel.
4070|als Erste loslassen;einen Schutzhelm tragen;neben dem Rad baumeln|eine Tragfläche;ein Helm;ein Rad;die Küste|Was machen die beiden Personen?|Sie baumeln unter der Tragfläche.
4071|von einem Schiffswrack springen;neben einem Hai gleiten;im flachen Wasser rosten|ein Schiffswrack;Wolken;eine Frau;das Meer|Was macht die Frau?|Sie springt von einem rostigen Schiffswrack.
4072|zum Wasser schlendern;leuchtend türkis strahlen;sich über den Sand neigen|eine Lagune;ein Strand;Palmen;eine Klippe|Was liegt zwischen den Klippen?|Zwischen den Klippen liegt eine türkisfarbene Lagune.
4073|ein schlafendes Küken knuddeln;ihre drei Küken bewachen;einen hellen Flügel ausbreiten|ein Stock;ein Schnabel;Küken|Was macht die Henne?|Sie bedroht eine Taube mit einem Stock.
4074|einen roten Badeanzug tragen;auf das Wasser scheinen;am Himmel fliegen|die Sonne;ein Boot;Wasser;der Himmel|Was macht die Sonne?|Die Sonne geht hinter einem Hügel unter.
4075|im Meer treiben;die Arme ausgestreckt halten;einen schwarzen Badeanzug tragen|Haie;eine Frau;das Meer|Was macht die Frau?|Sie treibt im Meer.
4076|schwarze Shorts tragen;eine weiße Hose tragen;wegfliegen|der Himmel;ein Mann;eine Frau;eine Stadt|Was machen der Mann und die Frau?|Sie springen aus einem Hubschrauber.
4077|über dem Nest fliegen;wieder einschlafen;am Himmel scheinen|der Mond;der Himmel;ein Vogel;ein Nest|Was macht der weiße Vogel?|Er schläft im Nest.
4078|über das Bett krabbeln;die Arme weit ausbreiten;über dem Bett hängen|ein Wandbehang;Kissen;eine Frau;eine Bettdecke|Was macht die Frau?|Sie krabbelt auf die Reihe von Kissen zu.
4079|über die Wellen hüpfen;zwischen dunklen Felsen schäumen;am Ufer warten|ein Wald;Paddler;der Fluss;ein Kajak|Was macht der Fluss?|Der Fluss rauscht zwischen den Felsen hindurch.
4080|in einer Schublade wühlen;ein Haargummi abstreifen;in einem rosa Kapuzenpulli schmollen|Augenbrauen;Lippen;ein Handgelenk;ein Pullover|Wo sind die Haargummis?|Sie sind am Handgelenk der Mutter.
4081|auf der Kufe hocken;über den Bergen schweben;den Landeplatz markieren|die Sonne;ein Hubschrauber;ein Gipfel;ein Tal|Was macht der Hubschrauber?|Er schwebt über den verschneiten Gipfeln.
4082|kopfüber hängen;die Tragflächenstrebe umklammern;auf das Riff zufallen|eine Tragfläche;Wolken;eine Strebe;ein Riff|Was macht die Frau?|Sie hängt kopfüber.
4083|in der Mitte liegen;einen lila Schlafanzug tragen;einen Bart haben|eine Frau;ein Hund;ein Mann;eine Decke|Wo liegt der Hund?|Der Hund liegt in der Mitte.
4084|seinen Kopf berühren;gelbe Haare bekommen;auf dem Spiegel sitzen|ein Spiegel;ein Mann;eine Katze;ein Wasserhahn|Was berührt der Mann?|Er berührt seinen Kopf.
4085|ein Videospiel spielen;einen blauen Anzug tragen;den Mann hineinschieben|eine Tür;ein Mann;eine Frau;eine Treppe|Was spielt der Mann?|Er spielt ein Videospiel.
4086|in einen kahlen Kopf stechen;unter einer Decke schlafen;einen Schrei ausstoßen|der Mond;eine Mücke;ein Kissen;eine Decke|Was macht die Mücke?|Sie sticht in einen kahlen Kopf.
4087|auf einem Laptop tippen;auf dem Bett sitzen;ein Diagramm zeigen|eine Katze;ein Laptop;Papier;ein Schreibtisch|Worauf tippt die Katze?|Sie tippt auf einem Laptop.
4088|über die Kante fallen;in die Luft steigen;kleine weiße Wolken haben|der Himmel;ein Fluss;ein Wasserfall|Wohin fällt das Wasser?|Es fällt über eine breite Kante.
4089|die Kamera nehmen;mit weißer Sonnenbrille tanzen;leuchtend rot strahlen|ein Oktopus;eine Kamera;Sand|Was macht der Oktopus mit der Sonnenbrille?|Er tanzt unter den roten Quallen.
4090|am Turm vorbei aufsteigen;fest an Ort und Stelle bleiben;sich über den Boden ausbreiten|eine Rakete;ein Startturm;Rauch;Beton|Was macht die Rakete?|Sie steigt am Startturm vorbei auf.
4091|auf dem zugefrorenen See hocken;dampfenden Tee ausgießen;in alle Richtungen reißen|eine Mütze;eine Sonnenbrille;eine Thermoskanne;Dampf|Was passiert mit dem Eis?|Das Eis reißt in alle Richtungen.
4092|die Stufen hinunterfahren;über dem Meer scheinen;zum Meer führen|die Sonne;das Meer;Stufen;ein Fahrrad|Wohin fährt das Fahrrad?|Das Fahrrad fährt die Stufen hinunter.
4093|stetig größer werden;vor der Dunkelheit leuchten;seine Krater zeigen|der Mond;Krater;der Himmel|Was macht der Mond?|Der runde Mond leuchtet vor der Dunkelheit.
4094|etwas Wasser trinken;die Straße entlanggehen;einen braunen Kopf haben|ein Pferd;Säcke;eine Mauer|Was machen die beiden Pferde?|Die Pferde fressen ihr Futter.
4095|einem anderen Auto folgen;eine blaue Jacke tragen;eine Sonnenbrille tragen|der Himmel;eine Sonnenbrille;ein Tablet;ein Bildschirm|Was drehen die Leute?|Sie drehen einen Film.
4096|wegschwimmen;das Seil durchschneiden;schwarze Shorts tragen|ein Mann;eine Schildkröte;ein Netz;Sand|Was macht die Schildkröte?|Sie schwimmt vom Netz weg.
4097|in die Luft springen;vorne fahren;ein weißes Hemd tragen|der Himmel;ein Radfahrer;ein Hügel;ein Rad|Wie schnell fährt der Radfahrer?|Der Radfahrer fährt sehr schnell.
4098|das Kalb zur Seite schieben;den Kopf zur Seite neigen;lange gebogene Hörner haben|eine Glocke;ein Weg;ein Kalb;ein Handschuh|Was machen die Tiere?|Sie versperren dem Radfahrer den Weg.
4099|auf den Matratzen sitzen;ein rotes Hemd tragen;zwischen den Autos hindurchfahren|Gebäude;ein Hund;Matratzen;ein Motorrad|Wo sitzt der Hund?|Er sitzt auf den Matratzen.
4100|auf dem Bett liegen;ein großes Loch machen;am Fenster hängen|ein Loch;eine Sprungfeder;ein Mann;ein Vorhang|Was ist in der Decke?|In der Decke ist ein großes Loch.
4101|die Arme ausbreiten;seinen großen Schwanz zeigen;die Vorstellung ansehen|Licht;ein Vogel;ein Handy;Leute|Was zeigt der Vogel?|Der Vogel zeigt seinen großen Schwanz.
4102|auf einem Laptop tippen;an einer Schnur fliegen;am Himmel scheinen|die Sonne;ein Drachen;ein Tisch;Gras|Wie ist das Wetter?|Die Sonne scheint am Himmel.
4103|um einen Sichtschutz herumspähen;aus Pappe herausragen;die Wurst schnappen|ein Welpe;eine Wurst;ein Teppich;eine Tür|Was macht der Welpe?|Er späht geduldig zur Wurst.
4104|den grauen Vogel küssen;rot im Gesicht werden;groß und dunkel sein|ein grauer Vogel;ein weißer Vogel;Bäume|Was macht der weiße Vogel?|Er gibt dem grauen Vogel einen Kuss.
4105|ihr Haar berühren;am Auto warten;sich den Mund zuhalten|ein Auto;Blumen;ein Mann|Wer wartet am Auto?|Ihr Freund wartet am Auto.
4106|eine Gabel halten;seine Nudeln fressen;über den Hund lachen|ein Mann;ein Hund;Nudeln;ein Tisch|Was macht der Hund?|Der hungrige Hund frisst seine Nudeln.
4107|den Elefanten bedecken;mit der Hand winken;seine Zähne zeigen|ein Tiger;ein Mann;ein Handy|Was bedeckt den Elefanten?|Ein Tuch bedeckt den Elefanten.
4108|aus dem Auto winken;das Lenkrad halten;neben dem Auto stehen|ein Auto;ein Vogel;ein Haus|Was macht der weiße Vogel?|Er steht neben dem Auto.
4109|das Wasser aufschlecken;aufgeregt hochspringen;Wasser nach oben spritzen|eine Hecke;ein Springbrunnen;ein Rasen|Was macht der schwarze Hund?|Er trinkt aus dem Springbrunnen auf dem Rasen.
4110|auf dem Boden liegen;neben dem Clown sitzen;auf den Elefanten fallen|ein Clown;ein Tiger;ein Handy|Wo sitzt der Tiger?|Er sitzt neben dem Clown.
4111|einen Hammer halten;den Mann schubsen;eine Sonnenbrille tragen|ein Mann;ein Schaf;ein Hammer;der Himmel|Was macht das Schaf?|Das lästige Schaf schubst ihn.
4112|ein Loch machen;eine Flasche halten;den Staub auffangen|ein Fenster;eine Flasche;ein Handschuh;ein Mauerstein|Was macht die Bohrmaschine?|Sie macht ein Loch in einen Mauerstein.
4113|einen rosa Ring tragen;einen anderen Vogel anschreien;auf sie herabschauen|Schmuck;ein weißer Vogel;Gebäude;eine Straße|Was trägt der graue Vogel?|Er trägt einen rosa Ring.
4114|auf eine Schaufensterpuppe zeigen;barfuß herumlaufen;ein goldenes Kleid präsentieren|eine Schaufensterpuppe;Vorhänge;Shorts;Stöckelschuhe|Worauf zeigt die Frau?|Sie zeigt auf die Schaufensterpuppe im Einkaufszentrum.
4115|den Arm heben;sich umdrehen und lachen;einen weißen Rock tragen|Touristen;Sonnenbrillen;Hüte|Wer geht an den Hüten vorbei?|Zwei Touristen gehen an den Hüten vorbei.
4116|ins Auto steigen;auf einer Bank sitzen;klein und rot sein|ein Auto;eine Bank;ein Baum;Gras|Was fährt der Mann?|Er fährt ein kleines rotes Auto.
4117|unter das Sofa schauen;ein Handy halten;auf den Tisch zeigen|ein Handy;Schlüssel;eine Hand;ein Tisch|Worauf zeigt die Frau?|Sie zeigt auf den Tisch.
4118|über den Tennisplatz sprinten;zwischen zwei Pfosten hängen;über dem Tennisplatz aufragen|ein Tennisplatz;ein Netz;ein Gipfel;eine Wiese|Was macht der Spieler?|Der Spieler sprintet über den Tennisplatz.
4119|zu einem Haufen zusammenfallen;beide Arme ausstrecken;über dem Ufer aufragen|Kiefern;Treibholz;Kieselsteine;Seetang|Was passiert mit der Steinfigur?|Sie fällt zu einem Haufen zusammen.
4120|quer über der Schüssel liegen;die zerbrochenen Schalen auffangen;hinter dem Brett stehen|Nüsse;ein Brett;Schalen;eine Schüssel|Wo liegt das Brett?|Das Brett liegt quer über der Schüssel.
4121|durch den Steinbruch schwingen;in Flammen umkippen;die Explosion aufnehmen|Rauch;Silos;ein Steg;eine Kamera|Was nimmt die Kamera auf?|Sie nimmt eine Explosionsszene in einem Steinbruch auf.
4122|eine Pistole halten;mit einem Stift schreiben;in einem Topf wachsen|ein Fenster;eine Pflanze;eine Pistole;ein Schreibtisch|Was macht der maskierte Mann?|Er raubt den Mann am Schreibtisch aus.
4123|in Tränen ausbrechen;in einer Pfütze knien;sich unterhalb der Klippe versammeln|Tränen;ein Blatt Papier;eine Pfütze|Was macht das Mädchen?|Es kniet in einer Pfütze aus Tränen.
4124|die Straße entlangfahren;auf einer Decke schlafen;zwischen den Steinen brennen|der Himmel;ein Van;ein Feuer;ein Hund|Was fährt die Straße entlang?|Ein Van fährt die Straße entlang.
4126|scharfe Spitzen haben;das Wort „Gefahr“ zeigen;viele helle Fenster haben|der Himmel;Gebäude;Männer|Was sehen sich die beiden Männer an?|Sie sehen sich die hohen Gebäude an.
4127|die Straße entlangspringen;eine Karotte fressen;das weiche Fell berühren|Augen;eine Karotte;eine Hand|Was macht die Hand?|Sie berührt das weiche Fell.
4128|im Hof rennen;auf das Gras treten;die Zunge herausstrecken|ein Zaun;ein Welpe;ein Weg;Gras|Was macht der Welpe?|Er rennt im Hof.
4129|sich langsam öffnen;das Zuhause verlassen;die Stufen hinuntergehen|Bäume;ein Auto;ein Zaun;ein Welpe|Was macht der Welpe?|Er verlässt mit einem grünen Hut das Zuhause.
4130|dem Gorilla die Haare stutzen;den Daumen hochhalten;seine Flattop-Frisur tätscheln|Flaschen;ein Gorilla;eine Fliege;ein Friseurstuhl|Was macht die Katze?|Sie schneidet dem Gorilla eine Flattop-Frisur.
4131|dem Affen die Haare machen;einen weißen Kittel tragen;seine Zähne zeigen|eine Wand;ein Affe;eine Katze|Welche Farbe hat die Wand?|Die Wand ist dunkelgrün.
4132|das nasse Haar bürsten;dem Löwen den Kopf waschen;auf einem schwarzen Stuhl sitzen|ein Löwe;eine Katze;eine Bürste;ein Waschbecken|Was macht die Katze?|Die Katze bürstet dem Löwen das Haar.
4133|einen großen Hund umarmen;den Kopf des Hundes berühren;am Kühlschrank liegen|ein Kühlschrank;ein Mann;ein Napf;ein Hund|Was macht der Mann?|Er umarmt einen großen Hund.
4134|einen dicken Bauch haben;auf einem schwarzen Stuhl sitzen;sich das Maul zuhalten|eine Katze;ein Spiegel;ein Stuhl;Flaschen|Wo sitzt das dicke Tier?|Es sitzt auf einem schwarzen Stuhl.
4135|den Ball schießen;im Tor stehen;über das Gras rennen|eine Frau;ein Ball;ein Tor;Gras|Was macht die Frau?|Sie schießt einen Ball.
4136|auf dem Boden trainieren;schwere Gewichte heben;auf der Bank stehen|eine Bank;ein Vorhang;eine Hose;der Boden|Was macht der Mann?|Er trainiert mit den Hunden.
4137|ein gelbes Kleid tragen;ein Spielzeug aufheben;in ein gelbes Spielzeug beißen|ein Hund;ein Kleid;ein Bett;ein Stuhl|Was hält der Hund?|Der Hund hält ein gelbes Spielzeug.
4138|den Hund streicheln;ein Eis halten;über das Gras rennen|ein Hund;eine Kappe;ein Eis;eine Hose|Was macht der Mann?|Er streichelt den Hund.
4139|einen Pfad hinaufwandern;über dem Gras flattern;über dem Hang aufragen|ein Pfad;ein Rucksack;ein Gipfel;Gras|Wo wandert der Mann?|Er wandert einen schmalen Pfad hinauf.
4140|ins Wasser springen;den Hügel hinunterrennen;am Himmel scheinen|ein Berg;Leute;eine Brücke;ein Fluss|Wo sitzen die drei Leute?|Sie sitzen auf einer Brücke über einem Fluss.
4141|in rosa Shorts sonnenbaden;eine Klippe hinunterführen;in eine Schlucht stürzen|der Himmel;ein Wasserfall;eine Klippe;Turnschuhe|Was machen die sechs Männer?|Sie liegen flach auf dem Rücken.
4142|ins Wasser fallen;im Meer schwimmen;auf der Straße tanzen|Wolken;die Sonne;eine Straße|Was macht die Frau in Weiß?|Sie tanzt im Regen.
4144|aus einer Kiste herausschauen;im Kreis liegen;lang und grau sein|ein Teppich;eine Kiste;der Boden;ein Schlauch|Wo liegt der Schlauch?|Der Schlauch liegt auf dem Boden.
4145|nach dem Ball hechten;einen Fallrückzieher versuchen;mit erhobenen Fäusten jubeln|ein Volleyball;ein Segelboot;ein Spritzer|Was macht der blonde Mann?|Er hechtet nach dem Ball.
4146|zum Meer sprinten;in den Wellen zusammenbrechen;regungslos im Schaum liegen|der Himmel;Schaum;Turnschuhe;Sand|Was macht der Mann?|Der erschöpfte Mann liegt im Schaum.
4147|zum Auto eilen;ein großes Schild tragen;im Auto lachen|ein Schild;ein Mann;ein Auto|Was trägt der Mann?|Er trägt ein großes gelbes Schild.
4148|über die Motorhaube streichen;den Startknopf drücken;gemächlich durch das Parkhaus fahren|ein Lenkrad;ein Anzug;ein Sitz|Was drückt der Mann?|Er drückt den Startknopf.
4149|durch den Himmel purzeln;ein riesiges Auge öffnen;über den See fliehen|Kiefern;ein Biber;ein Riese|Worauf sitzt der Biber?|Er sitzt auf dem Kopf eines Riesen.
4150|die Straße entlangrasen;sich dem geparkten Auto nähern;den bewölkten Himmel spiegeln|der Himmel;ein Sportwagen;ein Mann;Kies|Was macht der Sportwagen?|Er rast eine Landstraße entlang.
4151|einen Stift halten;rosa werden;an der Wand hängen|ein blaues Auto;ein rosa Auto;ein Tisch|Was macht die Hand?|Sie zeichnet ein rosa Auto.
4152|sich auf den Kies senken;im Anhänger stehen;über dem Anhänger aufragen|ein Anhänger;ein Sportwagen;eine Rampe;Kies|Was parkt im Anhänger?|Im Anhänger parkt ein Fahrzeug.
4153|auf der Autobahn fahren;oben Schnee haben;über den Feldern hängen|Berge;eine Wolke;ein Auto;eine Autobahn|Was macht das blaue Auto?|Es fährt auf der Autobahn.
4154|einen Tennisball schlagen;einen Schläger halten;von einem Balkon aus zuschauen|ein Gebäude;Palmen;ein Schläger;eine Frau|Was macht die Frau?|Sie schlägt einen Tennisball.
4155|einen schmutzigen Teller abwaschen;in die Toilette schauen;einen sauberen Teller halten|ein Kätzchen;eine Pflanze;ein Teller;eine Toilette|Was macht das Kätzchen?|Es wäscht einen Teller in der Toilette ab.
4157|ein Pappschild hochhalten;die nasse Allee säumen;verstreut auf der Straße liegen|ein Bogen;ein Schal;ein Pappschild;Blätter|Was machen die Läufer?|Sie rennen an einer älteren Frau vorbei.
4158|sich an eine Stange klammern;den Otter angrinsen;sich wie ein Ballon aufblasen|ein Hai;Bambus;ein Otter;der Himmel|Was passiert mit dem Hai?|Der riesige Hai bläst sich wie ein Ballon auf.
4159|über das Gras fliegen;hinter den Bäumen stehen;durch das Feld führen|der Himmel;Berge;Bäume;Schuhe|Was macht die Person?|Die Person fliegt hoch über den Bäumen.
4160|schnell wegfahren;die Straße hinunter verschwinden;hinter dem Auto aufwirbeln|der Himmel;eine Straße;ein Auto;Sand|Was macht das Auto?|Das Auto verschwindet die Straße hinunter.
4161|sich langsam vorwärts bewegen;an einer Stelle bleiben;die Autos ansehen|ein Mann;ein Fenster;ein Scheinwerfer;der Boden|Was sieht sich der Mann an?|Er sieht sich die Vorderseite des Autos an.
4162|allein geparkt sein;über die Skyline ragen;in einem Schwarm kreisen|ein Platz;ein Turm;ein Schwarm;Säulen|Was parkt auf dem Platz?|Auf dem Platz parkt ein Sportwagen.
4163|in die Kamera sprechen;leuchtend gelb sein;im Dunkeln leuchten|ein Mann;ein Auto;eine Lampe|Was macht der Mann?|Er spricht in die Kamera.
4164|um eine Kurve fahren;rote Lichter haben;das grüne Auto beobachten|eine Bremse;ein Rad;eine Straße|Was macht das grüne Auto?|Es fährt um eine Kurve.
4165|in die Kamera lächeln;um eine Kurve kommen;hoch und grün sein|ein Auto;Bäume;eine Straße;Felsen|Was macht der Mann?|Er fährt mit hoher Geschwindigkeit.
"""
out = {}
for l in R.strip().split('\n'):
    i, p, n, q, a = l.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
json.dump(out, open(f'{H}/de.json', 'w'), ensure_ascii=False, indent=1)
