import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = 'fr'
DATA = """
306 | avoir les cheveux longs | avoir une barbe courte | briller au-dessus des nuages | le soleil ; des nuages ; une femme ; un homme | Au-dessus de quoi volent-ils ? | Ils volent au-dessus des nuages.
307 | porter un bonnet rouge | s'enfoncer dans le brouillard | avoir de la laine blanche | du brouillard ; un mouton ; un bonnet ; de l'herbe | Où va l'homme ? | Il s'enfonce dans le brouillard.
308 | avoir de longs cheveux bouclés | se tenir près de la table | lever les yeux vers eux | du fromage ; des raisins ; une femme ; un mur | Qu'y a-t-il sur la table ? | La table est pleine de nourriture.
309 | marquer un but | sauter vers le ballon | voler dans le but | un ballon de football ; un homme ; la mer ; du sable | À quoi jouent-ils ? | Ils jouent au football sur le sable.
310 | toucher un grand arbre | porter une veste grise | briller à travers les arbres | le ciel ; des arbres ; de l'herbe ; une femme | Où marchent-ils ? | Ils marchent dans une forêt.
311 | lever une fourchette | ouvrir de grands yeux | brûler sur la table | une fourchette ; une bougie ; de la salade ; des pâtes | Que fait la femme ? | Elle mange des pâtes avec une fourchette.
312 | dribbler avec le ballon | commettre une faute | donner un coup de sifflet | le plafond ; un bracelet ; un écusson | Que fait l'arbitre ? | Elle donne un coup de sifflet pour une faute.
313 | estomper le fond de teint | tourner la tête sur le côté | refléter les deux femmes | des perroquets ; des tresses ; un miroir ; du fond de teint | Que fait la femme en blanc ? | Elle estompe du fond de teint avec une éponge.
314 | marcher dans l'herbe | sauter très haut | se secouer | un renard ; un arbre ; de l'herbe | Que fait le renard ? | Il marche dans l'herbe froide.
315 | tirer un coup franc | former un mur défensif | plonger vers le ballon | un ballon de football ; des défenseurs ; une colline ; le terrain | Que fait le joueur en rouge ? | Il tire un coup franc.
316 | ouvrir le congélateur | tenir les petits pois | tenir la glace | une cuillère ; de la glace ; un bonnet ; un congélateur | Que tient la femme ? | Elle tient un sachet de petits pois.
317 | faire cuire des frites | manger des frites | porter un bonnet noir | des frites ; un bonnet ; des vélos ; des lumières | Que fait le cuisinier ? | Il fait cuire des frites.
318 | avoir l'air très triste | partager sa glace | être par terre | une fille ; le ciel ; la mer ; une glace | Que fait la fille en vert ? | Elle partage sa glace avec son amie.
319 | être assis sur une pierre | sauter sur une feuille | nager dans l'eau | une grenouille ; une pierre ; un poisson | Que fait la grenouille ? | Elle est assise sur une pierre.
320 | essuyer le banc givré | toucher une feuille gelée | être suspendu entre deux poteaux | une toile d'araignée ; un banc ; le soleil | Qu'essuie la femme ? | Elle essuie le givre du banc.
321 | manger une pêche | porter un panier | se tenir derrière la table | un ananas ; des raisins ; une pêche ; un panier | Que mange la femme ? | Elle mange une pêche.
322 | placer une énorme mise | se couvrir les yeux avec anxiété | tourner à grande vitesse | des jetons ; une boucle d'oreille ; une barbe | Que fait la femme ? | Elle place une énorme mise.
323 | faire rebondir le ballon | soulever la femme | voler dans les airs | un ballon ; le ciel ; un filet ; des arbres | À quoi jouent les amis ? | Ils jouent un match de basket.
326 | sentir une rose rose | porter une caisse en bois | marcher près de l'homme | une rose ; une femme ; une maison ; le ciel | Que sent la femme ? | Elle sent une rose rose.
327 | manger une tomate rouge | porter un chapeau | voler près des fleurs | le ciel ; un chapeau ; un homme ; une abeille | Que mange l'homme ? | Il mange une tomate rouge.
328 | éplucher l'ail | être assis dans la cuisine | entrer dans la cuisine | une casserole ; un couteau ; de l'ail | Que sent la femme ? | Elle sent l'ail.
329 | tenir une bouilloire blanche | allumer le gaz | verser de l'huile dans la poêle | une femme ; une casserole ; une bouilloire ; du feu | Que tient l'homme ? | Il tient une bouilloire blanche.
331 | ramasser une orange | porter un panier | enlever son chapeau | un parapluie ; un gentleman ; une femme ; un panier | Que porte la vieille femme ? | Elle porte un panier d'oranges.
333 | sauter par-dessus une corde | porter un tee-shirt jaune | lever les mains | une femme ; un mur ; une fille | Que fait la fille en jean ? | Elle saute par-dessus une corde.
334 | porter une chemise blanche | avoir une barbe foncée | être dans un bol | un verre ; un pichet ; des citrons ; le ciel | Que fait la femme ? | Elle boit de la limonade dans un verre.
336 | nettoyer ses lunettes | porter une veste bleue | nager dans l'eau | des lunettes ; des feuilles ; de l'eau ; un doigt | Que nettoie la femme ? | Elle nettoie ses lunettes.
338 | montrer du doigt un continent | tourner sur son socle | briller au-dessus du bureau | un globe ; un abat-jour ; une boucle d'oreille ; un pull | Que fait la femme ? | Elle montre du doigt un continent sur le globe.
340 | être assis sur un banc | être allongé par terre | voler dans le but | un but ; le ciel ; des pierres ; une femme | Où vole le ballon ? | Le ballon vole dans le but.
341 | escalader un mur de pierre | mordre une chemise blanche | se tenir sur le toit | le ciel ; une chèvre ; un toit ; un mur | Que mord la chèvre ? | Elle mord une chemise blanche.
342 | mettre des lunettes de natation bleues | pointer du doigt | nager sous l'eau | un bonnet de bain ; des lunettes de natation ; de l'eau ; un maillot de bain | Que met la fille ? | Elle met des lunettes de natation bleues.
344 | soulever quelque chose de lourd | nettoyer un lingot d'or | porter une chaîne en or | des lunettes ; une veste ; un lingot d'or ; une chaîne | Que nettoie la femme ? | Elle nettoie un lingot d'or.
346 | jouer au golf | tenir un drapeau rouge | rouler sur l'herbe | le ciel ; un drapeau ; une balle ; un trou | Que fait la femme ? | Elle joue au golf.
348 | tamponner un document officiel | gesticuler les bras ouverts | montrer trois barres colorées | un paperboard ; un tampon ; une baguette | Que fait la femme en violet ? | Elle tamponne un document officiel.
349 | porter une casquette | porter un tee-shirt bleu | être posé sur le bois | un grand-père ; un garçon ; une table ; des arbres | Qui joue avec le garçon ? | Son grand-père joue avec lui.
350 | porter un sac à dos | marcher vers la porte | être assis dans un fauteuil | un petit-fils ; une grand-mère ; un fauteuil | Qui la grand-mère serre-t-elle dans ses bras ? | Elle serre son petit-fils dans ses bras.
351 | porter un tee-shirt jaune | porter un short bleu foncé | avoir les cheveux courts | de l'herbe ; un oiseau ; une fille ; un garçon | Où sont-ils allongés ? | Ils sont allongés sur l'herbe.
352 | tendre la main | lever un doigt | avoir des rayures foncées | des fleurs ; une table ; une bougie ; un barbecue | Qu'y a-t-il sur le barbecue ? | Il y a du fromage et des légumes sur le barbecue.
355 | enfouir son visage | avoir une longue fissure | contenir du riz et du ragoût | un cadre photo ; de la poterie ; un canapé ; une assiette | Comment l'homme montre-t-il sa culpabilité ? | Il enfouit son visage dans ses mains.
356 | porter un grand sac | parcourir la salle de sport du regard | pendre à son épaule | le plafond ; des poids ; un tee-shirt ; un sac | Que porte la femme ? | Elle porte un sac dans la salle de sport.
357 | brosser ses longs cheveux | taper dans ses mains | être couché près des fleurs | un rideau ; une fenêtre ; des fleurs ; une brosse à cheveux | Qui tient la brosse à cheveux ? | La femme aux cheveux longs tient la brosse à cheveux.
359 | courir dans une roue | manger quelques graines | être plein de graines | un hamster ; une roue ; un bol | Que fait le hamster ? | Il mange des graines dans un bol.
360 | regarder par-dessus le siège | avoir une barbe noire | être assis à côté de l'homme | du gel hydroalcoolique ; un chien ; un homme ; une table | Que mettent-ils sur leurs mains ? | Ils mettent du gel hydroalcoolique sur leurs mains.
361 | emballer des sucettes dans du papier | être en tas | avoir un visage souriant | des sucettes ; un bouquet ; un ruban | Que font les mains ? | Elles emballent des sucettes dans du papier.
362 | danser dans la rue | manger une pêche | venir vers la femme | une pêche ; un chien ; un bateau ; des chaussures | De quoi la femme a-t-elle l'air ? | Elle a l'air très heureuse.
363 | prendre des notes | éclairer le bureau | afficher un document | une lampe de bureau ; un gilet ; un ordinateur portable ; des post-it | Que fait l'homme ? | Il fait des recherches à son bureau.
364 | dessiner sur du papier | tenir un crayon orange | sourire à la caméra | un visage ; un tee-shirt ; un crayon ; un dessin | Que fait l'homme ? | Il dessine avec un crayon orange.
366 | enlever un bandage | agripper un anneau de gymnastique | brandir le poing | une manche ; un poing ; une tasse à café ; des clés de voiture | Qu'agrippe la femme ? | Elle agrippe un anneau de gymnastique.
367 | manger une glace à l'eau | tenir un éventail | être couché par terre | le ciel ; une fontaine ; une chemise ; une robe | Que mange l'homme ? | Il mange une glace à l'eau orange.
369 | passer à côté de la moto | avoir deux rétroviseurs | être suspendu dans le ciel | une voiture ; une route ; une moto ; le ciel | Que fait la voiture ? | Elle passe à côté de la moto.
370 | mettre un casque | tenir un skateboard | tenir un gobelet | un casque ; un pantalon ; un skateboard ; le ciel | Que met la fille ? | Elle met un casque rouge.
371 | frotter les feuilles de basilic | parsemer des spaghettis d'herbes | hausser les sourcils | des herbes ; une barbe ; des spaghettis ; une assiette | Que fait la femme ? | Elle parsème les spaghettis d'herbes.
372 | jongler avec un ballon de football | faire l'équilibre sur les mains | tournoyer dans les airs | des gratte-ciel ; un ballon de football ; une ombre | Que fait l'homme ? | Il fait des figures avec un ballon de football.
373 | entrer dans un stade | porter des maillots rouges | descendre les escaliers | le ciel ; un stade ; un homme ; des escaliers | Que fait l'homme blond ? | Il entre dans un stade.
374 | faire du jogging le long de la route | garder un rythme régulier | avoir les jambes tatouées | un lampadaire ; le ciel ; un joggeur ; une route | Que fait l'homme ? | Il fait du jogging le long de la route.
375 | attacher la sangle de son casque | foncer sur la piste | agripper le volant | le soleil ; une tribune ; une voiture de course ; de l'asphalte | Que fait la voiture de course ? | Elle fonce sur la piste.
377 | se produire devant la caméra | jouer de la batterie | se prélasser sur un canapé | un projecteur ; une artiste ; une batterie ; un canapé | Que fait la femme ? | Elle se produit devant la caméra.
379 | faire signe à la caméra | ramener ses cheveux en arrière | enregistrer un vlog | des rideaux ; des figurines ; des taches de rousseur ; un ordinateur portable | Que fait la jeune femme ? | Elle enregistre un vlog dans sa chambre.
380 | franchir un tourniquet | être posé sur une surface en bois | protéger de la pluie | un sac à dos ; des lunettes ; un smartphone ; une fenêtre | Que franchit la femme ? | Elle franchit un tourniquet de métro.
381 | tenir un grain de raisin vert | avoir l'air très effrayé | montrer beaucoup de photos | des cheveux ; un grain de raisin ; des photos ; un lavabo | Que tient l'homme ? | L'homme effrayé tient un grain de raisin.
382 | nettoyer une fenêtre | tenir un outil jaune | être suspendu très haut | un casque ; le ciel ; la ville | Que fait la femme ? | Elle nettoie une fenêtre située en hauteur.
386 | avoir une barbe noire | lui montrer ses bateaux | être couché dans une boîte | un homme ; une femme ; un chat ; des bateaux | Que lui montre l'homme ? | Il lui montre ses petits bateaux.
387 | se reposer sur le tapis | réveiller son maître | dormir sous une couette | un tapis ; une couette ; un oreiller ; une table de chevet | Que fait le chien ? | Le chien essaie de réveiller son maître.
388 | faire ses devoirs | porter des lunettes rondes | écrire avec un stylo | des cheveux ; des lunettes ; un stylo ; des devoirs | Que fait la fille ? | Elle fait ses devoirs.
389 | mettre du miel sur du pain | manger du pain avec du miel | être couché sur un mur | une femme ; un homme ; du pain ; du miel | Que mange l'homme ? | Il mange du pain avec du miel.
390 | mettre sa capuche | porter un sweat à capuche rouge | nager dans l'eau | de l'eau ; des vélos ; un sweat à capuche ; des canards | Que fait l'homme ? | Il rabat sa capuche sur sa tête.
391 | grimper sur le mur | lever les bras | naviguer sur la mer | une femme ; un bateau ; la mer ; un mur | Que regarde la femme ? | Elle regarde un bateau.
392 | faire du cheval | porter la femme | monter sur le cheval | le ciel ; une femme ; un cheval ; de l'herbe | Que fait la femme ? | Elle fait du cheval.
393 | remettre une clé | agripper l'échelle en bois | tendre des chips | un escalier ; un réceptionniste ; un comptoir ; une clé | Que propose la femme rousse ? | Elle propose un paquet de chips.
394 | s'essuyer le visage | tenir une bouteille d'eau | souffler de l'air sur lui | un toit ; un mur ; un ventilateur ; une serviette | Que fait l'homme ? | Il s'essuie le visage avec une serviette.
396 | tenir un petit cadeau | courir vers l'homme | marcher à quatre pattes | des fenêtres ; un câlin ; un chien ; le sol | Que font l'homme et la femme ? | Ils se font un câlin.
397 | scruter à travers des jumelles | porter un bonnet en tricot | brouter parmi les arbres | des troncs d'arbres ; un cerf ; des feuilles mortes | Que font l'homme et la femme ? | Ils chassent un cerf dans la forêt.
398 | se rincer la bouche | se savonner les mains | se sécher le visage en tapotant | un miroir ; un pyjama ; de la mousse ; un lavabo | Que fait le garçon ? | Il se savonne les mains au-dessus du lavabo.
399 | lécher la glace | porter un grand chapeau | se tenir sur le mur | le ciel ; un oiseau ; un chapeau ; de la glace | Que fait l'homme ? | Il lèche sa glace.
400 | patiner autour d'un cône | porter un casque blanc | crier derrière la vitre | des supporters ; un but ; de la glace | Que font les filles ? | Elles jouent au hockey sur glace.
404 | regarder la caméra | se battre au fond | rire ensemble | des rideaux ; des affiches ; une tablette ; un bureau | Que font les garçons derrière lui ? | Ils se battent dans la salle de classe.
405 | entrer en premier | porter une marmite chaude | avoir les cheveux très courts | une lampe ; une fenêtre ; un feu ; une table | Que font les gens ? | Ils rentrent se mettre à l'abri de la neige.
407 | ouvrir grand les bras | avoir les cheveux longs | voler au-dessus des arbres | des oiseaux ; une île ; un homme ; de l'eau | Que font les oiseaux ? | Ils volent au-dessus de l'île.
408 | mettre une veste | sourire à l'homme | se tenir sur la clôture | une veste ; une femme ; un oiseau ; le ciel | Que porte l'homme ? | Il porte une veste marron.
410 | ouvrir un pot de confiture | regarder la femme | se tenir près de la fenêtre | de la confiture ; du beurre ; un panier ; un chat | Que fait la femme ? | Elle met de la confiture sur le pain.
411 | se renfrogner, les bras croisés | gagner le ruban rouge | remettre le prix | un ruban ; des collants ; des chaussons de danse ; un miroir | De quoi la danseuse en turquoise a-t-elle l'air ? | Elle a l'air jalouse de l'autre danseuse.
412 | déplier un maillot de football | remettre un maillot | enfiler un maillot | un maillot ; un tee-shirt ; une queue de cheval ; des chaussures de football | Que fait la femme aux cheveux bouclés ? | Elle déplie un maillot de football.
413 | couper un fruit rouge | prendre le verre | marcher sur le sol | du jus ; un bol ; un arbre ; un oiseau | Que boit l'homme ? | Il boit un verre de jus.
414 | courir sur la piste | sauter par-dessus la barre | tomber sur le tapis | le ciel ; un tapis ; des arbres ; une femme | Que fait la femme devant ? | Elle saute par-dessus la barre.
415 | bondir sur le sable | rester avec sa mère | porter un petit | un kangourou ; le soleil ; de l'herbe ; le ciel | Que porte le grand kangourou ? | Il porte son petit.
418 | forcer un anneau pour l'ouvrir | applaudir avec un grand sourire | faire tourner un porte-clés | un porte-clés ; un vendeur ; un seau ; une manche | Que fait la femme ? | Elle fait tourner un porte-clés sur son doigt.
422 | donner des coups de pied dans un grand sac | être suspendu à des cordes | lever une jambe bien haut | une femme ; un sac ; des nuages ; le sol | Que fait la femme ? | Elle donne des coups de pied dans un grand sac.
423 | souffler un baiser | lui embrasser la main | porter un grand chapeau | un chapeau ; un homme ; un panier ; une bouteille | Que fait l'homme ? | Il lui embrasse la main.
424 | couper le pain | se sécher les mains | manger un sandwich à la tomate | un couteau ; un chien ; une tomate ; une femme | Que fait l'homme ? | Il coupe du pain avec un couteau.
426 | monter à une échelle | cueillir une pomme rouge | tenir l'échelle immobile | une échelle ; un mouton ; un arbre ; des pommes | Que fait la femme ? | Elle monte à une échelle.
427 | grimper le long de l'herbe | ouvrir ses ailes | s'envoler dans le ciel | une coccinelle ; une fleur ; le ciel ; de l'herbe | Que fait la coccinelle ? | Elle grimpe le long de l'herbe.
428 | lancer une pierre | porter un pull gris | porter un pull rouge | le ciel ; une montagne ; un bateau ; un lac | Que fait l'homme ? | Il lance une pierre dans le lac.
430 | porter un sac marron | être assis sur une caisse | avoir une barbe blanche | des maisons ; une fille ; un panier ; un bateau | Que porte la fille ? | Elle porte un sac marron.
431 | être allongé sur le canapé | être posé contre le mur | prendre la télécommande | une fenêtre ; un balai ; un homme ; une table | Que fait l'homme ? | Il est allongé sur le canapé.
435 | brosser une ceinture en cuir | mettre une veste | être couché sous la table | une femme ; une veste ; une ceinture ; une table | Que porte l'homme ? | Il porte une veste en cuir.
436 | avoir de longs cheveux gris | porter une jupe jaune | avoir des fleurs roses | le ciel ; un arbre ; la mer ; une jupe | Dans quelle direction les gens pointent-ils ? | Ils pointent vers la gauche.
437 | poser sa jambe en hauteur | monter les escaliers en courant | se dresser sur la colline | le ciel ; des escaliers ; une chaussure ; une jambe | Que fait la femme ? | Elle monte les escaliers en courant.
438 | mordre dans un citron | avoir une barbe foncée | être couché sur le mur | un citron ; un couteau ; une main | Que fait la femme ? | Elle mord dans un citron.
439 | boire de la limonade fraîche | être couché sur le sol | pousser dans un pot | de la limonade ; des fleurs ; un chien ; une femme | Que fait la femme ? | Elle boit de la limonade fraîche.
440 | soulever des poids lourds | porter une large ceinture | sourire à la fin | un homme ; une ceinture ; une fenêtre | Que fait l'homme ? | Il soulève des poids lourds.
442 | peiner avec un carton | donner un coup de main | s'accroupir derrière un carton | un chat ; des cartons ; une barbe ; un parquet | Que font l'homme et la femme ? | Ils empilent des cartons ensemble.
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
