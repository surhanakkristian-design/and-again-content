import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = r"""
188#sich über den Tisch beugen|eine gepuderte Perücke tragen|zwei Wachssiegel tragen#eine Perücke|eine Verfassung|Marmor#Was liest der Politiker?#Er liest eine Seite der Verfassung.
189#den Konvoi anführen|zwischen zwei Fahrzeugen parken|das Schlusslicht bilden#ein Konvoi|Bäume|Asphalt|der Himmel#Was machen die drei Autos?#Sie fahren im Konvoi.
190#einen großen Keks essen|einen Löffel halten|am Fenster liegen#ein Fenster|eine Katze|Kekse|ein Tisch#Was isst die Frau?#Sie isst einen großen Keks.
191#am Korken riechen|sich in den Korken drehen|ein langärmliges Hemd tragen#ein Korkenzieher|ein Korken|eine Flasche|ein Kochtopf#Wie öffnet der Mann die Flasche?#Er öffnet die Flasche mit einem Korkenzieher.
192#in die Ecke passen|orangefarbene Kleidung tragen|eine Brille tragen#der Himmel|eine Ecke|eine Frau|ein Mann#Wohin legen sie das Brett?#Sie legen es in die Ecke.
193#ein Bestechungsgeld annehmen|das Dokument stempeln|in ihre Tasche greifen#ein Stempel|ein Schnurrbart|ein Dokument|eine Schürze#Was macht der Mann?#Der korrupte Beamte nimmt ein Bestechungsgeld an.
194#etwas Baumwolle halten|die Baumwolle wegpusten|ein weißes T-Shirt tragen#die Sonne|ein Hut|Baumwolle|ein T-Shirt#Was hält die Frau?#Sie hält etwas Baumwolle.
195#in ihre Hand husten|heißen Tee bringen|auf der Decke laufen#Pflanzen|eine Tasse|eine Decke|eine Katze#Was macht die kranke Frau?#Sie hustet in ihre Hand.
196#auf einem Brett balancieren|das Stahlseil umklammern|die Holzplattform erreichen#ein Helm|ein Klettergurt|ein Brett|Bäume#Was macht das Mädchen?#Es balanciert auf einem schmalen Brett.
197#grünes Gras fressen|die Milch trinken|die Milch gießen#eine Kuh|eine Frau|eine Glocke|Milch#Was frisst die Kuh?#Die Kuh frisst grünes Gras.
198#ihre schmerzende Wade umklammern|auf der Laufbahn knien|den Daumen nach oben zeigen#eine Frau|ein Mann|Wolkenkratzer|eine Laufbahn#Was umklammert die Frau?#Sie umklammert ihre schmerzende Wade.
199#ein rotes Auto fahren|beide Arme heben|ein gelbes Hemd tragen#ein Mann|ein rotes Auto|ein gelbes Auto#Was fährt der Mann?#Er fährt ein rotes Auto.
200#die Sahne rühren|eine Waffel essen|ihr Haar bedecken#Sahne|eine Waffel|ein Teller#Was macht der Mann?#Er rührt Sahne in einer Schüssel.
201#im Fluss schwimmen|das Wasser verlassen|sein Maul weit öffnen#ein Krokodil|Bäume|ein Fluss#Was macht das Krokodil?#Es öffnet sein Maul weit.
202#die Straße überqueren|auf sein Handy schauen|seinen Daumen hochhalten#ein Mann|ein Auto|Gebäude|eine Straße#Was macht der Mann?#Er überquert die Straße.
203#ein gelbes Sommerkleid tragen|ein geblümtes Hemd tragen|über die Wellen springen#ein Kreuzfahrtschiff|Delfine|Inseln|das Meer#Was macht das Kreuzfahrtschiff?#Es fährt an tropischen Inseln vorbei.
204#an Krücken gehen|ein Klemmbrett umklammern|eine geballte Faust heben#eine Krankenschwester|eine Krücke|ein orthopädischer Stiefel|eine Türklinke#Was macht der Junge?#Er geht an zwei Krücken.
205#ihre Augen trocknen|die Frau umarmen|ein Taschentuch nehmen#eine Frau|ein Mann|eine Decke|Taschentücher#Was macht die Frau?#Sie weint und trocknet ihre Augen.
206#eine Gurke schneiden|etwas Gurke essen|über den Tisch schauen#ein Fenster|eine Gurke|ein Hemd|ein Hund#Was macht der Mann?#Er schneidet eine Gurke.
207#einen grünen Ohrring tragen|eine Brille tragen|ein blaues Hemd tragen#eine Katze|eine Tasse|Blumen|eine Teekanne#Was macht die Frau?#Sie trinkt Tee aus einer Tasse.
210#Kopfhörer anprobieren|eine Papiertüte packen|zwei Schachteln halten#eine Kundin|eine Tüte|eine Karte|Kopfhörer#Was macht die Kundin?#Sie probiert weiße Kopfhörer an.
211#einen Koffer kontrollieren|ihre Hände falten|mit Stacheln bedeckt sein#eine Durian|ein Koffer|ein Abfalleimer|ein Zollbeamter#Was macht der Zollbeamte?#Der Zollbeamte kontrolliert einen Koffer.
212#ihr Bein dehnen|in einem Studio tanzen|in die Kamera lächeln#eine Tänzerin|ein Spiegel|ein Lautsprecher|der Boden#Was macht die Tänzerin?#Sie tanzt in einem Studio.
213#am Herd kochen|die Frau halten|einen langen Rock tragen#eine Frau|ein Mann|ein Radio|der Boden#Was machen der Mann und die Frau?#Sie tanzen in der Küche.
214#auf dem Eis gehen|ihren Freund zurückziehen|in Stücke brechen#ein Schild|ein Baum|ein Junge|Eis#Was macht der Junge?#Der Junge geht auf gefährlichem Eis.
215#ein Streichholz anzünden|einen gestreiften Pullover tragen|in der Dunkelheit leuchten#eine Laterne|ein Streichholz|ein Fenster|eine Kupferpfanne#Was macht die Frau?#Sie zündet in der Dunkelheit eine Laterne an.
217#auf die Dartscheibe zielen|Chips knabbern|nahe am Bullseye landen#ein Dartpfeil|eine Dartscheibe|eine Holzwand#Was macht die Frau?#Sie zielt mit einem Dartpfeil auf die Dartscheibe.
218#eine Schriftrolle hochhalten|am Glockenseil ziehen|einen kleinen Jungen umarmen#eine Glocke|eine Schriftrolle|Tauben|ein Kopftuch#Was passiert auf dem Balkon?#Eine Frau verkündet der Menge etwas.
219#in die Kamera schauen|sein Maul öffnen|weglaufen#ein Hirsch|Bäume|Pflanzen#Was macht der Hirsch?#Der Hirsch läuft weg.
220#einen gefrorenen Fisch auftauen|einen Fisch hinknallen|in einer Schüssel einweichen#ein Filet|ein Wasserhahn|eine Schüssel|ein Schrank#Was macht der Mann?#Er taut einen gefrorenen Fisch auf.
221#ihren Abschluss feiern|ein goldenes Siegel tragen|durch die Luft flattern#eine Abschlussurkunde|ein Absolventenhut|eine Quaste#Was feiert die Frau?#Sie feiert ihren Abschluss.
222#die Bustür versperren|auf ihrem Koffer zusammenbrechen|die Uhrzeit anzeigen#eine Uhr|ein Koffer|Neonschilder|ein Fahrer#Was macht der Fahrer?#Er versperrt die Bustür.
223#auf dem Sofa liegen|das Essen liefern|ein orangefarbenes Oberteil tragen#eine Lampe|ein Fenster|eine Katze|ein Sofa#Wer liefert das Essen?#Ein Mann mit Helm liefert das Essen.
224#einen Stuhl skizzieren|auf die Skizze zeigen|am Pappstuhl schnuppern#eine Skizze|ein Glasgefäß|eine Zimmerpflanze#Was entwerfen sie?#Sie entwerfen einen Stuhl.
226#Akkordeon spielen|auf dem Boden kauern|offen und leer daliegen#ein Akkordeon|Graffiti|ein Instrumentenkoffer|eine Pinnwand#Was spielt der Musiker?#Er spielt Akkordeon.
227#eine Lupe halten|vor Staunen nach Luft schnappen|auf der Fensterbank ruhen#ein Diamant|ein Kissen|eine Katze|eine Kette#Was starrt die rothaarige Frau an?#Sie starrt einen funkelnden Diamanten an.
228#einen heißen Topf tragen|eine Kerze anzünden|auf der Mauer sitzen#eine Katze|ein Topf|ein Salat|Brot#Was machen die Leute?#Sie essen zusammen zu Abend.
229#über die Bühne schreiten|dem Absolventen gratulieren|mit einem Band zugebunden sein#ein Diplom|ein Absolventenhut|ein Talar|eine Schärpe#Was macht der Absolvent?#Er hebt sein Diplom über den Kopf.
231#in Tränen ausbrechen|ihr auf die Schulter klopfen|auf dem Tisch flackern#Lichterketten|eine Kerze|Spaghetti|ein Geschenk#Was macht die Frau?#Sie bricht am Tisch in Tränen aus.
232#sich erwartungsvoll die Hände reiben|zutiefst enttäuscht aussehen|eine winzige Portion enthalten#eine Mütze|ein Bart|ein Regenmantel|ein Tablett#Wie sieht der Mann vorne aus?#Er sieht mit seinem leeren Tablett enttäuscht aus.
233#seine verletzte Schulter umklammern|neben dem Kletterer knien|aufgerollt daliegen#ein Helm|eine Schulter|eine Jacke|Gras#Was macht der Mann?#Er umklammert seine verletzte Schulter.
235#einen roten Ball apportieren|dem Hund den Bauch kraulen|rote Äpfel tragen#ein Apfelbaum|ein Zaun|ein Hund|ein Rasen#Was macht der Hund?#Der Hund apportiert einen roten Ball.
237#sein Maul weit öffnen|sich auf dem Boden wälzen|nach Futter suchen#Orangen|ein Haus|ein Esel|Vögel#Was macht der Esel?#Der Esel wälzt sich auf dem Boden.
238#eine Dose stehlen|eine weiße Tasche tragen|rosa Blumen haben#der Himmel|Blumen|Gras|Dosen#Was macht der Mann?#Er stiehlt eine Dose.
239#einen goldenen Ring begutachten|den Kunden angrinsen|zweifelnd die Stirn runzeln#ein Ring|ein Kopftuch|eine Jacke|Wolken#Was begutachtet der Mann?#Er begutachtet einen goldenen Ring.
240#ein türkisfarbenes T-Shirt tragen|einen dichten Bart haben|ein Geschirrtuch darüberlegen#ein Geschirrtuch|ein Tisch|eine ältere Frau#Wie endet das Duell im Armdrücken?#Das Duell endet unentschieden.
241#auf den Stufen sitzen|eine Zeichnung anfertigen|einen gelben Hut tragen#eine Zeichnung|ein Hut|Häuser|ein Hemd#Was zeigt der Mann der Frau?#Er zeigt ihr seine Zeichnung.
243#einen Pullover anziehen|ihr beim Anziehen helfen|in den Spiegel schauen#eine Mütze|eine Tasche|eine Tür|Jeans#Was macht der Mann?#Er hilft ihr beim Anziehen.
244#Orangensaft trinken|Orangensaft machen|auf einem Stock sitzen#ein Papagei|ein Mann|Saft|Orangen#Was macht der Mann?#Er trinkt ein Glas Orangensaft.
245#sich die Hände waschen|die Flasche füllen|auf den Felsen sitzen#der Himmel|Berge|eine Frau|ein Mann#Was machen die beiden Personen?#Sie trinken Wasser aus ihren Flaschen.
246#das Auto fahren|einen grauen Hut tragen|die Fahrerin anlächeln#ein Spiegel|das Meer|eine Frau|ein Mann#Was macht die Frau?#Sie fährt ein Auto am Meer.
248#die Tropfen abmessen|die Medizin schlucken|Dampf abgeben#eine Pipette|ein Holzlöffel|eine Schürze#Was macht die Frau?#Sie misst mit einer Pipette Tropfen ab.
250#ihren Kopf unter Wasser stecken|ihre Flügel öffnen|ihren Schnabel öffnen#eine Ente|Bäume|Wasser#Was macht die Ente?#Die Ente schwimmt auf dem Wasser.
251#Bizepscurls machen|an ihrem Kaffee nippen|im Schneidersitz sitzen#eine Hantel|eine Palme|ein Sessel|ein Fenster#Was macht der Mann?#Er macht Bizepscurls mit einer Hantel.
252#auf einen Koffer pusten|einen Finger hochhalten|hoch oben sitzen#Staub|ein Mann|eine Frau|ein Koffer#Was macht der Mann?#Er pustet Staub von einem Koffer.
253#über der Tür putzen|einen grauen Schal tragen|auf einem Regal laufen#eine Katze|Bücher|ein Regal|eine Lampe#Was macht der Mann?#Er putzt über der Tür.
254#den sich drehenden Globus anhalten|dunkles lockiges Haar haben|am Fenster schlafen#die Sonne|das Meer|eine Katze|ein Globus#Was macht die Katze?#Die Katze schläft am Fenster.
255#zum Himmel zeigen|im Osten aufgehen|ihre Tassen heben#der Himmel|die Sonne|Menschen|Felsen#Was macht die Sonne?#Die Sonne geht über den Wolken auf.
256#an der heißen Suppe riechen|einen dunklen Bart haben|auf der Straße kochen#ein Schild|ein Bart|Schüsseln|Jeans#Was essen der Mann und die Frau?#Sie essen heiße Nudelsuppe.
258#auf schmalen Brettern balancieren|einen rötlichen Bart haben|den Rasen bedecken#Kiefern|Felsbrocken|ein See|Bretter#Was macht die blauhaarige Person?#Die Person balanciert auf schmalen Brettern.
259#sich über den Himmel ausbreiten|den Güterbahnhof füllen|eine dunkle Silhouette bilden#Wolken|ein Feuerball|Güterwagen|Baumwipfel#Was breitet sich über den Nachthimmel aus?#Ein unheimliches rotes Leuchten breitet sich über den Himmel aus.
260#etwas Brot essen|am Fenster sitzen|in die Pfanne fallen#ein Mann|eine Katze|Tomaten|ein Ei#Was isst der Mann?#Er isst Brot mit einem Ei.
261#ein Kabel durchschneiden|ein rosa T-Shirt tragen|einen Bart haben#eine Tür|ein Mann|ein Mädchen|eine Elektrikerin#Was macht die Elektrikerin?#Sie schneidet ein Kabel durch.
262#mit seinem Rüssel trinken|seinen Rüssel heben|weiße Federn haben#ein Baum|ein Elefant|ein Vogel|Wasser#Was macht der Elefant?#Er trinkt Wasser mit seinem Rüssel.
263#aus dem See auftauchen|ihre Schwimmbrille anheben|nahe am Ufer treiben#eine Schwimmbrille|ein Ruderboot|eine Spiegelung|Berge#Was macht die Schwimmerin?#Sie taucht aus dem See auf.
264#einen Blumenstrauß umklammern|sich an das Geländer lehnen|einen Gepäckwagen schieben#ein Blumenstrauß|eine Strickjacke|ein Geländer|Jeans#Was hält die Frau?#Sie umklammert einen Blumenstrauß aus gelben Blumen.
265#einen Umschlag bekommen|eine Jacke anziehen|seine Schulter berühren#ein Angestellter|Papier|eine Tastatur|ein Fenster#Was bekommt der Angestellte?#Er bekommt einen Umschlag.
266#die Stufen hinauflaufen|auf und ab springen|seine Knie halten#Stufen|eine Straßenlaterne|eine Mauer|der Himmel#Was macht die Frau in Weiß?#Sie läuft die Stufen hinauf.
267#einen Roboter bauen|einen Würfel aufheben|in die Hände klatschen#ein Ingenieur|ein Roboter|ein Laptop|eine Schachtel#Was macht der Ingenieur?#Er baut einen kleinen Roboter.
268#den Umschlag küssen|eine Kerze halten|hinter der Lampe schlafen#eine Lampe|eine Katze|eine Kerze|ein Umschlag#Was küsst die Frau in Rot?#Sie küsst den Umschlag.
269#durch das Fenster blicken|am Bus vorbeiradeln|quer auf ihrem Schoß liegen#ein Radfahrer|lockiges Haar|ein ärmelloses Oberteil|ein Lenker#Was macht die Frau mit dem lockigen Haar?#Sie blickt neidisch auf den Radfahrer.
270#in die Kamera lächeln|wie ein Berg aussehen|eine rote Sonne zeigen#eine Schachtel|eine Hand|ein Radiergummi|Papier#Wie sieht der Radiergummi aus?#Der Radiergummi sieht aus wie ein kleiner Berg.
272#die leere Pfanne neigen|aus der Pfanne verdampfen|eine blaue Flamme erzeugen#eine Schutzbrille|Dampf|eine Pfanne|ein Campingkocher#Was passiert mit dem Wasser?#Es verdampft aus der heißen Pfanne.
273#hinter den Hügeln verschwinden|lange Haare haben|einen grünen Pullover tragen#der Himmel|die Sonne|Häuser|eine Frau#Was macht die Sonne?#Sie geht hinter den Hügeln unter.
274#einen Schal hochhalten|auf jemandes Schultern sitzen|vom Dach strahlen#Lichter|ein Junge|ein Schal#Was machen alle?#Alle schreien im Stadion.
275#mit dem Finger zeigen|nach oben schauen und nachdenken|den Mann anlächeln#Vorhänge|ein Sofa|ein Tisch|ein Mann#Was machen der Mann und die Frau?#Sie streiten im Wohnzimmer.
276#an einem Hang grasen|über eine Klippe stürzen|auf einem Felsbrocken liegen#ein Wasserfall|ein Regenbogen|ein Handy|ein Felsbrocken#Was machen die Freunde?#Sie posieren vor einem Wasserfall.
279#seine ganze Kraft aufbieten|seine Faust ballen|durch eine Pfütze rollen#Säcke|ein Rad|eine Pfütze#Was macht der Mann?#Er bietet seine ganze Kraft auf.
280#in die Kamera schauen|auf einem Bett sitzen|ganz nah herankommen#ein Kätzchen|ein Bett|ein Handy#Was macht das Kätzchen?#Es schaut in die Kamera.
281#geschwungenen Eyeliner auftragen|ein Wattestäbchen halten|den Daumen nach oben zeigen#Glühbirnen|ein Spiegel|Eyeliner|ein Wattestäbchen#Was macht die dunkelhaarige Frau?#Sie trägt geschwungenen Eyeliner auf.
282#goldenen Lidschatten aufnehmen|ein Kopftuch tragen|goldene Augenlider zur Schau stellen#ein Kopftuch|Lidschatten|ein Kragen|ein Knopf#Was nimmt der Pinsel auf?#Er nimmt goldenen Lidschatten auf.
283#den gemusterten Stoff ausrollen|mit einer großen Schere schneiden|den gefalteten Stoff an sich drücken#ein Ohrring|Stoff|ein Tisch|ein Maßband#Was macht der Mann?#Er schneidet den Stoff mit einer Schere.
284#ein flauschiges Haarband tragen|auf ihre Freundin zeigen|auf einem Kissen ruhen#ein Haarband|eine Gesichtsmaske|ein Hund|eine Schüssel#Was tragen die Frauen?#Sie tragen grüne Gesichtsmasken.
285#ein Familienfoto machen|mit beiden Händen winken|die Stufen hinauflaufen#ein Fenster|eine Familie|Stufen|Gras#Was macht die Familie?#Sie macht ein Familienfoto.
287#auf ein Dorf zeigen|zu ihr zurückschauen|eine rote Jacke tragen#der Himmel|ein Dorf|Gras#Worauf zeigt die Frau?#Sie zeigt auf ein weit entferntes Dorf.
289#sich an die Brust fassen|sich an einen Pfosten klammern|sich von hinten nähern#Gipfel|ein Geländer|eine Spiegelung#Was macht die Frau in Blau?#Sie klammert sich vor Angst an einen Pfosten.
290#ihre Brust berühren|ihre Augen schließen|ein graues Hemd tragen#eine Flagge|eine Frau|ein Glas#Was macht die Frau?#Sie berührt ihre Brust.
292#ein Kissen hoch in die Luft heben|ein graues T-Shirt tragen|einen Bart haben#ein Fenster|ein Kissen|eine Pflanze|ein Bett#Was machen sie auf dem Bett?#Sie machen eine Kissenschlacht.
293#ihre Augen abschirmen|hinter der Kamera hocken|auf dem Sims sitzen#ein Mikrofon|ein Reflektor|eine Taube|ein Stativ#Worauf ist die Kamera montiert?#Die Kamera ist auf einem Stativ montiert.
294#einen langen Stock halten|Holz aufs Feuer legen|zwischen den Steinen brennen#Bäume|ein Mann|ein Feuer|Steine#Was macht der Mann?#Er legt Holz aufs Feuer.
295#die dicke Paste mischen|einen schwarzen Griff halten|am Boden kleben#Klebeband|ein Eimer|eine Hand|ein Schuh#Was macht die Hand?#Die Hand mischt die dicke Paste.
296#eine halbe Zitrone halten|mit einer Gabel essen|über dem Feuer liegen#das Meer|ein Boot|ein Fisch|ein Feuer#Was isst die Frau?#Sie isst Fisch mit einer Gabel.
297#eine Angel halten|einen Kescher halten|im See schwimmen#ein Fisch|ein Kescher|eine Kappe|Bäume#Was machen der Mann und die Frau?#Sie angeln im See.
298#mehrere Outfits anprobieren|den Daumen nach oben zeigen|auf der Theke ruhen#ein Vorhang|ein Kleiderstapel|Sandalen|ein Hund#Was macht die blonde Frau?#Sie probiert in einer Umkleidekabine Outfits an.
299#im Bett schlafen|auf dem Bett laufen|ihr Gesicht bedecken#ein Kissen|ein Hund|eine Decke|eine Tür#Was macht der Hund?#Der Hund weckt sie auf.
300#am Seil ziehen|im Wind wehen|zur Flagge hinaufschauen#eine Flagge|der Himmel|Berge|ein Mädchen#Was schaut das Mädchen an?#Es schaut die Flagge an.
301#auf dem See treiben|den Daumen nach oben zeigen|auf dem Mann sitzen#ein Vogel|ein Mann|ein See#Was macht der Mann?#Er treibt auf dem See.
302#auf dem Boden liegen|ihre Nase berühren|einen grauen Schal tragen#Mehl|Eier|ein Hund#Was ist auf dem Gesicht des Mannes?#Auf seinem Gesicht ist Mehl.
303#ein paar Blumen halten|am Fenster sitzen|eine rosa Blume berühren#ein Fenster|Blumen|eine Frau#Was hält die Frau?#Sie hält ein paar Blumen.
305#auf dem Brot landen|über den Tisch fliegen|mit einer Serviette wedeln#eine Fliege|ein Marmeladenglas|Tee|Brot#Was macht die Fliege?#Sie sitzt auf dem Brot.
"""
out = {}
for l in D.strip().split('\n'):
    i, p, n, q, a = l.split('#')
    out[i] = {'phrases': p.split('|'), 'nouns': n.split('|'), 'question': q, 'answer': a}
json.dump(out, open(f'{H}/de.json', 'w'), ensure_ascii=False, indent=1)
