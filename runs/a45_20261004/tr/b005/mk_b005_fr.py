import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = r"""
188#se pencher par-dessus la table|porter une perruque poudrée|porter deux sceaux de cire#une perruque|une constitution|du marbre#Que lit le politicien ?#Il lit une page de la constitution.
189#mener le convoi|se garer entre deux véhicules|fermer la marche#un convoi|des arbres|de l'asphalte|le ciel#Que font les trois voitures ?#Elles roulent en convoi.
190#manger un gros cookie|tenir une cuillère|être allongé près de la fenêtre#une fenêtre|un chat|des cookies|une table#Que mange la femme ?#Elle mange un gros cookie.
191#renifler le bouchon|se visser dans le bouchon|porter une chemise à manches longues#un tire-bouchon|un bouchon|une bouteille|une marmite#Comment l'homme ouvre-t-il la bouteille ?#Il ouvre la bouteille avec un tire-bouchon.
192#s'ajuster dans le coin|porter des vêtements orange|porter des lunettes#le ciel|un coin|une femme|un homme#Où mettent-ils la planche ?#Ils la mettent dans le coin.
193#accepter un pot-de-vin|tamponner le document|mettre la main dans sa poche#un tampon|une moustache|un document|un tablier#Que fait l'homme ?#Le fonctionnaire corrompu accepte un pot-de-vin.
194#tenir du coton|chasser le coton en soufflant|porter un tee-shirt blanc#le soleil|un chapeau|du coton|un tee-shirt#Que tient la femme ?#Elle tient du coton.
195#tousser dans sa main|apporter du thé chaud|marcher sur la couverture#des plantes|une tasse|une couverture|un chat#Que fait la femme malade ?#Elle tousse dans sa main.
196#se tenir en équilibre sur une planche|agripper le câble d'acier|atteindre la plateforme en bois#un casque|un harnais|une planche|des arbres#Que fait la fille ?#Elle se tient en équilibre sur une planche étroite.
197#manger de l'herbe verte|boire le lait|verser le lait#une vache|une femme|une cloche|du lait#Que mange la vache ?#La vache mange de l'herbe verte.
198#serrer son mollet douloureux|s'agenouiller sur la piste|lever le pouce#une femme|un homme|des gratte-ciel|une piste de course#Que serre la femme ?#Elle serre son mollet douloureux.
199#conduire une voiture rouge|lever les deux bras|porter une chemise jaune#un homme|une voiture rouge|une voiture jaune#Que conduit l'homme ?#Il conduit une voiture rouge.
200#mélanger la crème|manger une gaufre|se couvrir les cheveux#de la crème|une gaufre|une assiette#Que fait l'homme ?#Il mélange de la crème dans un bol.
201#nager dans la rivière|sortir de l'eau|ouvrir grand la gueule#un crocodile|des arbres|une rivière#Que fait le crocodile ?#Il ouvre grand la gueule.
202#traverser la rue|regarder son téléphone|lever son pouce#un homme|une voiture|des bâtiments|une rue#Que fait l'homme ?#Il traverse la rue.
203#porter une robe d'été jaune|porter une chemise à fleurs|bondir au-dessus des vagues#un bateau de croisière|des dauphins|des îles|la mer#Que fait le bateau de croisière ?#Il navigue devant des îles tropicales.
204#marcher avec des béquilles|serrer un porte-bloc|lever un poing serré#une infirmière|une béquille|une botte orthopédique|une poignée de porte#Que fait le garçon ?#Il marche avec deux béquilles.
205#s'essuyer les yeux|serrer la femme dans ses bras|prendre un mouchoir#une femme|un homme|une couverture|des mouchoirs#Que fait la femme ?#Elle pleure et s'essuie les yeux.
206#couper un concombre|manger du concombre|regarder par-dessus la table#une fenêtre|un concombre|une chemise|un chien#Que fait l'homme ?#Il coupe un concombre.
207#porter une boucle d'oreille verte|porter des lunettes|porter une chemise bleue#un chat|une tasse|des fleurs|une théière#Que fait la femme ?#Elle boit du thé dans une tasse.
210#essayer un casque audio|remplir un sac en papier|tenir deux boîtes#une cliente|un sac|une carte|un casque audio#Que fait la cliente ?#Elle essaie un casque audio blanc.
211#inspecter une valise|joindre les mains|être couvert de piquants#un durian|une valise|une poubelle|un douanier#Que fait le douanier ?#Le douanier inspecte une valise.
212#étirer sa jambe|danser dans un studio|sourire à la caméra#une danseuse|un miroir|une enceinte|le sol#Que fait la danseuse ?#Elle danse dans un studio.
213#cuisiner sur la cuisinière|tenir la femme|porter une jupe longue#une femme|un homme|une radio|le sol#Que font l'homme et la femme ?#Ils dansent dans la cuisine.
214#marcher sur la glace|tirer son ami en arrière|se briser en morceaux#un panneau|un arbre|un garçon|de la glace#Que fait le garçon ?#Le garçon marche sur de la glace dangereuse.
215#craquer une allumette|porter un pull rayé|briller dans l'obscurité#une lanterne|une allumette|une fenêtre|une poêle en cuivre#Que fait la femme ?#Elle allume une lanterne dans l'obscurité.
217#viser la cible de fléchettes|grignoter des chips|atterrir près du mille#une fléchette|une cible de fléchettes|un mur en bois#Que fait la femme ?#Elle vise la cible de fléchettes avec une fléchette.
218#lever un parchemin|tirer la corde de la cloche|enlacer un petit garçon#une cloche|un parchemin|des colombes|un foulard#Que se passe-t-il sur le balcon ?#Une femme déclare quelque chose à la foule.
219#regarder la caméra|ouvrir la bouche|s'enfuir#un cerf|des arbres|des plantes#Que fait le cerf ?#Le cerf s'enfuit.
220#décongeler un poisson congelé|poser brutalement un poisson|tremper dans un bol#un filet|un robinet|un bol|un placard#Que fait l'homme ?#Il décongèle un poisson congelé.
221#fêter sa remise de diplôme|porter un sceau doré|voltiger dans les airs#un diplôme|un chapeau de diplômé|un pompon#Que fête la femme ?#Elle fête sa remise de diplôme.
222#bloquer la porte du bus|s'effondrer sur sa valise|afficher l'heure#une horloge|une valise|des enseignes au néon|un chauffeur#Que fait le chauffeur ?#Il bloque la porte du bus.
223#être allongé sur le canapé|livrer la nourriture|porter un haut orange#une lampe|une fenêtre|un chat|un canapé#Qui livre la nourriture ?#Un homme avec un casque livre la nourriture.
224#esquisser une chaise|montrer le croquis du doigt|renifler la chaise en carton#un croquis|un bocal|une plante d'intérieur#Que conçoivent-ils ?#Ils conçoivent une chaise.
226#jouer de l'accordéon|s'accroupir sur le sol|être posé ouvert et vide#un accordéon|des graffitis|un étui|un panneau d'affichage#De quoi joue le musicien ?#Il joue de l'accordéon.
227#tenir une loupe|avoir le souffle coupé d'émerveillement|se reposer sur le rebord de la fenêtre#un diamant|un coussin|un chat|une chaîne#Que fixe la femme rousse ?#Elle fixe un diamant étincelant.
228#porter une marmite chaude|allumer une bougie|être assis sur le mur#un chat|une marmite|une salade|du pain#Que font les gens ?#Ils dînent ensemble.
229#traverser la scène à grands pas|féliciter le diplômé|être attaché avec un ruban#un diplôme|un chapeau de diplômé|une toge|une écharpe#Que fait le diplômé ?#Il lève son diplôme au-dessus de sa tête.
231#fondre en larmes|lui tapoter l'épaule|vaciller sur la table#des guirlandes lumineuses|une bougie|des spaghettis|un cadeau#Que fait la femme ?#Elle fond en larmes à table.
232#se frotter les mains avec impatience|avoir l'air profondément déçu|contenir une portion minuscule#un bonnet|une barbe|un imperméable|un plateau#De quoi a l'air l'homme au premier plan ?#Il a l'air déçu avec son plateau vide.
233#se tenir l'épaule blessée|s'agenouiller à côté du grimpeur|être enroulée au sol#un casque|une épaule|une veste|de l'herbe#Que fait l'homme ?#Il se tient l'épaule blessée.
235#rapporter une balle rouge|frotter le ventre du chien|porter des pommes rouges#un pommier|une clôture|un chien|une pelouse#Que fait le chien ?#Le chien rapporte une balle rouge.
237#ouvrir grand la bouche|se rouler par terre|chercher de la nourriture#des oranges|une maison|un âne|des oiseaux#Que fait l'âne ?#L'âne se roule par terre.
238#voler une canette|porter un sac blanc|avoir des fleurs roses#le ciel|des fleurs|de l'herbe|des canettes#Que fait l'homme ?#Il vole une canette.
239#examiner une bague en or|adresser un large sourire au client|froncer les sourcils d'un air dubitatif#une bague|un foulard|une veste|des nuages#Qu'examine l'homme ?#Il examine une bague en or.
240#porter un tee-shirt turquoise|avoir une barbe épaisse|draper un torchon#un torchon|une table|une femme âgée#Comment se termine la partie de bras de fer ?#La partie se termine par un match nul.
241#être assis sur les marches|faire un dessin|porter un chapeau jaune#un dessin|un chapeau|des maisons|une chemise#Que montre l'homme à la femme ?#Il lui montre son dessin.
243#mettre un pull|l'aider à s'habiller|se regarder dans le miroir#un bonnet|un sac|une porte|un jean#Que fait l'homme ?#Il l'aide à s'habiller.
244#boire du jus d'orange|faire du jus d'orange|être posé sur un bâton#un perroquet|un homme|du jus|des oranges#Que fait l'homme ?#Il boit un verre de jus d'orange.
245#se laver les mains|remplir la bouteille|être assis sur les rochers#le ciel|des montagnes|une femme|un homme#Que font les deux personnes ?#Elles boivent de l'eau dans leurs bouteilles.
246#conduire la voiture|porter un chapeau gris|sourire à la conductrice#un rétroviseur|la mer|une femme|un homme#Que fait la femme ?#Elle conduit une voiture au bord de la mer.
248#mesurer les gouttes|avaler le médicament|dégager de la vapeur#un compte-gouttes|une cuillère en bois|un tablier#Que fait la femme ?#Elle mesure des gouttes avec un compte-gouttes.
250#mettre la tête sous l'eau|ouvrir ses ailes|ouvrir le bec#un canard|des arbres|de l'eau#Que fait le canard ?#Le canard nage sur l'eau.
251#faire des curls biceps|siroter son café|être assise en tailleur#un haltère|un palmier|un fauteuil|une fenêtre#Que fait l'homme ?#Il fait des curls biceps avec un haltère.
252#souffler sur une valise|lever un doigt|être perché tout en haut#de la poussière|un homme|une femme|une valise#Que fait l'homme ?#Il souffle sur une valise pour en enlever la poussière.
253#nettoyer au-dessus de la porte|porter une écharpe grise|marcher sur une étagère#un chat|des livres|une étagère|une lampe#Que fait l'homme ?#Il nettoie au-dessus de la porte.
254#arrêter le globe qui tourne|avoir les cheveux foncés et bouclés|dormir près de la fenêtre#le soleil|la mer|un chat|un globe#Que fait le chat ?#Le chat dort près de la fenêtre.
255#montrer le ciel du doigt|se lever à l'est|lever leurs tasses#le ciel|le soleil|des gens|des rochers#Que fait le soleil ?#Le soleil se lève au-dessus des nuages.
256#sentir la soupe chaude|avoir une barbe foncée|cuisiner dans la rue#une enseigne|une barbe|des bols|un jean#Que mangent l'homme et la femme ?#Ils mangent une soupe de nouilles chaude.
258#se tenir en équilibre sur des planches étroites|avoir une barbe rousse|recouvrir la pelouse#des pins|des rochers|un lac|des planches#Que fait la personne aux cheveux bleus ?#La personne se tient en équilibre sur des planches étroites.
259#se répandre dans le ciel|remplir la gare de marchandises|former une silhouette sombre#des nuages|une boule de feu|des wagons de marchandises|des cimes d'arbres#Qu'est-ce qui se répand dans le ciel nocturne ?#Une inquiétante lueur rouge se répand dans le ciel.
260#manger du pain|être assis près de la fenêtre|tomber dans la poêle#un homme|un chat|des tomates|un œuf#Que mange l'homme ?#Il mange du pain avec un œuf.
261#couper un fil|porter un tee-shirt rose|avoir une barbe#une porte|un homme|une fille|une électricienne#Que fait l'électricienne ?#Elle coupe un fil.
262#boire avec sa trompe|lever sa trompe|avoir des plumes blanches#un arbre|un éléphant|un oiseau|de l'eau#Que fait l'éléphant ?#Il boit de l'eau avec sa trompe.
263#émerger du lac|relever ses lunettes de natation|flotter près de la rive#des lunettes de natation|une barque|un reflet|des montagnes#Que fait la nageuse ?#Elle émerge du lac.
264#serrer un bouquet|s'appuyer sur la rambarde|pousser un chariot à bagages#un bouquet|un gilet|une rambarde|un jean#Que tient la femme ?#Elle serre un bouquet de fleurs jaunes.
265#recevoir une enveloppe|mettre une veste|lui toucher l'épaule#un employé|du papier|un clavier|une fenêtre#Que reçoit l'employé ?#Il reçoit une enveloppe.
266#monter les marches en courant|sauter sur place|se tenir les genoux#des marches|un lampadaire|un mur|le ciel#Que fait la femme en blanc ?#Elle monte les marches en courant.
267#construire un robot|ramasser un cube|taper dans ses mains#un ingénieur|un robot|un ordinateur portable|une boîte#Que fait l'ingénieur ?#Il construit un petit robot.
268#embrasser l'enveloppe|tenir une bougie|dormir derrière la lampe#une lampe|un chat|une bougie|une enveloppe#Qu'embrasse la femme en rouge ?#Elle embrasse l'enveloppe.
269#regarder fixement par la fenêtre|passer devant le bus en pédalant|reposer en travers de ses genoux#un cycliste|des cheveux bouclés|un haut sans manches|un guidon#Que fait la femme aux cheveux bouclés ?#Elle regarde fixement le cycliste avec envie.
270#sourire à la caméra|ressembler à une montagne|montrer un soleil rouge#une boîte|une main|une gomme|du papier#À quoi ressemble la gomme ?#La gomme ressemble à une petite montagne.
272#incliner la poêle vide|s'évaporer de la poêle|produire une flamme bleue#des lunettes de protection|de la vapeur|une poêle|un réchaud de camping#Qu'arrive-t-il à l'eau ?#Elle s'évapore de la poêle chaude.
273#passer derrière les collines|avoir les cheveux longs|porter un pull vert#le ciel|le soleil|des maisons|une femme#Que fait le soleil ?#Il se couche derrière les collines.
274#lever une écharpe|être assis sur les épaules de quelqu'un|briller depuis le toit#des lumières|un garçon|une écharpe#Que fait tout le monde ?#Tout le monde crie dans le stade.
275#pointer du doigt|lever les yeux et réfléchir|sourire à l'homme#des rideaux|un canapé|une table|un homme#Que font l'homme et la femme ?#Ils se disputent dans le salon.
276#paître à flanc de colline|plonger du haut d'une falaise|être posé sur un rocher#une cascade|un arc-en-ciel|un téléphone|un rocher#Que font les amis ?#Ils posent devant une cascade.
279#déployer toute sa force|serrer le poing|rouler à travers une flaque#des sacs|une roue|une flaque#Que fait l'homme ?#Il déploie toute sa force.
280#regarder la caméra|être assis sur un lit|s'approcher très près#un chaton|un lit|un téléphone#Que fait le chaton ?#Il regarde la caméra.
281#appliquer de l'eye-liner en aile|tenir un coton-tige|lever le pouce#des ampoules|un miroir|de l'eye-liner|un coton-tige#Que fait la femme brune ?#Elle applique de l'eye-liner en aile.
282#prendre du fard à paupières doré|porter un foulard|exhiber des paupières dorées#un foulard|du fard à paupières|un col|un bouton#Que prend le pinceau ?#Il prend du fard à paupières doré.
283#dérouler le tissu à motifs|couper avec de grands ciseaux|serrer le tissu plié dans ses bras#une boucle d'oreille|du tissu|une table|un mètre ruban#Que fait l'homme ?#Il coupe le tissu avec des ciseaux.
284#porter un bandeau pelucheux|montrer son amie du doigt|se reposer sur un coussin#un bandeau|un masque pour le visage|un chien|un bol#Que portent les femmes ?#Elles portent des masques verts pour le visage.
285#prendre une photo de famille|agiter les deux mains|monter les marches en courant#une fenêtre|une famille|des marches|de l'herbe#Que fait la famille ?#Elle prend une photo de famille.
287#montrer un village du doigt|se retourner pour la regarder|porter une veste rouge#le ciel|un village|de l'herbe#Que montre la femme du doigt ?#Elle montre du doigt un village au loin.
289#se tenir la poitrine|s'accrocher à un poteau|approcher par-derrière#des sommets|une rambarde|un reflet#Que fait la femme en bleu ?#Elle s'accroche à un poteau par peur.
290#toucher sa poitrine|fermer les yeux|porter une chemise grise#un drapeau|une femme|un verre#Que fait la femme ?#Elle touche sa poitrine.
292#lever haut un oreiller|porter un tee-shirt gris|avoir une barbe#une fenêtre|un oreiller|une plante|un lit#Que font-ils sur le lit ?#Ils font une bataille d'oreillers.
293#se protéger les yeux|s'accroupir derrière la caméra|être perché sur le rebord#un micro|un réflecteur|un pigeon|un trépied#Sur quoi la caméra est-elle montée ?#La caméra est montée sur un trépied.
294#tenir un long bâton|mettre du bois sur le feu|brûler entre les pierres#des arbres|un homme|un feu|des pierres#Que fait l'homme ?#Il met du bois sur le feu.
295#mélanger la pâte épaisse|tenir un manche noir|coller au sol#du ruban adhésif|un seau|une main|une chaussure#Que fait la main ?#La main mélange la pâte épaisse.
296#tenir un demi-citron|manger avec une fourchette|être posé au-dessus du feu#la mer|un bateau|un poisson|un feu#Que mange la femme ?#Elle mange du poisson avec une fourchette.
297#tenir une canne à pêche|tenir une épuisette|nager dans le lac#un poisson|une épuisette|une casquette|des arbres#Que font l'homme et la femme ?#Ils pêchent dans le lac.
298#essayer plusieurs tenues|lever le pouce|se reposer sur le comptoir#un rideau|une pile de vêtements|des sandales|un chien#Que fait la femme blonde ?#Elle essaie des tenues dans une cabine d'essayage.
299#dormir dans le lit|marcher sur le lit|se couvrir le visage#un oreiller|un chien|une couverture|une porte#Que fait le chien ?#Le chien la réveille.
300#tirer la corde|flotter au vent|lever les yeux vers le drapeau#un drapeau|le ciel|des montagnes|une fille#Que regarde la fille ?#Elle regarde le drapeau.
301#flotter sur le lac|lever le pouce|être posé sur l'homme#un oiseau|un homme|un lac#Que fait l'homme ?#Il flotte sur le lac.
302#être couché par terre|toucher son nez|porter une écharpe grise#de la farine|des œufs|un chien#Qu'y a-t-il sur le visage de l'homme ?#Il y a de la farine sur son visage.
303#tenir des fleurs|être assise près de la fenêtre|toucher une fleur rose#une fenêtre|des fleurs|une femme#Que tient la femme ?#Elle tient des fleurs.
305#se poser sur le pain|voler au-dessus de la table|agiter une serviette#une mouche|un pot|du thé|du pain#Que fait la mouche ?#Elle est posée sur le pain.
"""
out = {}
for l in D.strip().split('\n'):
    i, p, n, q, a = l.split('#')
    out[i] = {'phrases': p.split('|'), 'nouns': n.split('|'), 'question': q, 'answer': a}
json.dump(out, open(f'{H}/fr.json', 'w'), ensure_ascii=False, indent=1)
