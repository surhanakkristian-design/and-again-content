import json, os
H = os.path.dirname(os.path.abspath(__file__)); CODE = 'fr'
DATA = r'''
569|déverrouiller la porte d'entrée;avoir une moustache fournie;porter une queue de cheval|une receveuse des postes;des clés;des colis;un chariot|Que fait la receveuse des postes ?|Elle pousse un chariot plein de colis.
572|creuser dans le jardin;porter une écharpe bleue;être posé sur une clôture|un oiseau;une femme;des pommes de terre;un seau|Que fait la femme ?|Elle met des pommes de terre dans un seau.
573|verser du jus d'orange;tenir une grande bouteille;prendre un verre|un homme;une femme;une bouteille;des verres|Que fait l'homme ?|Il verse du jus d'orange dans des verres.
574|ouvrir grand la bouche;se toucher la poitrine;avoir les cheveux courts et noirs|un arbre;un pinceau;un pot;de la poudre|Qu'y a-t-il dans le pot ?|Il y a de la poudre dans le pot.
575|lever les mains au ciel;fouiller dans son sac;lever une batterie externe|une batterie externe;des pigeons;des roses;un banc|Sur quoi branchent-ils le téléphone ?|Ils le branchent sur une batterie externe.
576|prier à son bureau;presser ses mains l'une contre l'autre;lever les yeux et pleurer|une femme;un ordinateur portable;des livres;une lampe|Que fait la femme ?|Elle prie à son bureau.
577|prédire la pluie;éclater de rire;apporter une averse soudaine|un nuage d'orage;un parapluie;un châle;de l'herbe|Que fait la femme ?|Elle s'abrite sous un parapluie jaune.
578|sortir une moto en la poussant;lustrer le réservoir d'essence;lui tapoter l'épaule|un bandana;un réservoir d'essence;un moteur;des pavés|Que fait la mécanicienne ?|Elle présente sa moto avec fierté.
579|taper un nouveau code;faire un geste vers l'ordinateur portable;suivre le parcours dessiné|un robot;un ordinateur portable;une queue de cheval;une barbe|Que fait la femme ?|Elle programme un petit robot.
580|tenir un manteau en l'air;porter un panier;porter des lunettes|un panier;un manteau;le ciel;des lunettes|Que fait la grande femme ?|Elle protège son amie de la pluie.
581|agripper un tournesol;porter une pancarte avec un arbre;flotter dans la brise|un tournesol;un palmier;le ciel;une foule|Que font les gens ?|Ils manifestent avec des pancartes peintes.
582|être assis sur une chaise;croiser les bras;lui toucher l'épaule|une chaise;une femme;une fenêtre;une table|Comment se sent la femme ?|Elle est fière de sa nouvelle chaise.
584|faire un équilibre sur les mains;lui prouver qu'il a tort;avoir le souffle coupé de stupéfaction|des pieds nus;des leggings;un banc;un gilet en tricot|Que fait la jeune femme ?|Elle fait un équilibre sur les mains pour lui prouver qu'il a tort.
585|jouer de la musique en public;être assis sur une caisse;projeter de l'eau vers le haut|un réverbère;des hommes;un accordéon;un étui|Que fait la jeune femme ?|Elle joue de l'accordéon en public.
588|porter des bottes rouges;porter des bottes noires;se tenir au loin|un imperméable jaune;un oiseau;des bottes rouges;une flaque|Que font les deux personnes ?|Elles sautent dans une grande flaque.
589|tenir quelque chose de rouge;avoir une barbe courte;courir à travers l'herbe|un chien;de l'herbe;un homme;une corde|Que font l'homme et la femme ?|Ils tirent sur une grosse corde.
590|donner des coups de poing rapides;tenir des pattes d'ours en l'air;être suspendu à une chaîne|un mur de briques;un sac de frappe;des gants de boxe;un short|Que fait la femme ?|Elle frappe les pattes d'ours.
591|donner des coups de poing puissants;maintenir l'échelle;se balancer au plafond|une chaîne;un sac de frappe;des gants de boxe;un short|Que fait l'homme ?|Il donne des coups de poing dans le sac de frappe.
592|avoir une barbe foncée;porter un tee-shirt blanc;descendre la route en roulant|le ciel;une camionnette;une route|Que font les deux hommes ?|Ils poussent une camionnette blanche.
593|avoir les cheveux courts et bouclés;avoir les cheveux longs et foncés;dormir par terre|une fenêtre;des pyjamas;un lit;un chien|Que portent l'homme et la femme ?|Ils portent des pyjamas.
594|franchir la barre;agiter un drapeau vert;brandir les poings|une barre transversale;un drapeau;une queue de cheval;un tapis|Comment la fille se qualifie-t-elle ?|Elle se qualifie en franchissant la barre.
595|manger des feuilles vertes;se laver le museau;sauter par-dessus l'herbe|le ciel;un lapin;de l'herbe;des feuilles|Que mange le lapin ?|Il mange des feuilles vertes.
597|regarder à travers une raquette;se tenir derrière le filet;sourire à la caméra|des fleurs;une balle;un filet;une raquette|Que tient la femme ?|Elle tient une raquette noire.
598|ouvrir grand les bras;porter une chemise blanche;marcher à quatre pattes|un toit;un arbre;un chien;un bateau|Que fait la fille ?|Elle danse sous la pluie.
599|dribbler avec un ballon coloré;tacler l'homme en noir;contrôler un ballon blanc|un but;un ballon de football;du gazon;un toit|Que font les deux hommes ?|Ils se disputent le ballon.
600|se tenir sur deux pattes;tirer une part de pizza;avoir de grandes roues noires|un rat;de la pizza;des escaliers;une fenêtre|Que fait le rat ?|Il tire une part de pizza.
601|se raser avec un rasoir;montrer sa montre du doigt;marcher sur le lavabo|un rasoir;une lampe;un miroir;un tee-shirt|Que fait l'homme en blanc ?|Il se rase avec un rasoir.
604|tenir une pomme rouge;vendre des fruits;imprimer un long ticket de caisse|un ticket de caisse;des pommes;des poires;des bouteilles|Que regarde l'homme ?|Il regarde un long ticket de caisse.
606|être posé dans une cage;avoir une barbe noire;avoir les cheveux bouclés|une recette;un oiseau;des pancakes;un homme|Que mangent l'homme et la femme ?|Ils mangent des pancakes.
607|être couché par terre;toucher le réfrigérateur;avoir une barbe noire|un réfrigérateur;un chien;un homme;une femme|Où se tiennent l'homme et la femme ?|Ils se tiennent à côté du réfrigérateur.
608|agripper le volant;rire de soulagement;reposer sur le pare-brise|un volant;un tableau de bord;un essuie-glace;un sweat-shirt|Qu'agrippe la conductrice ?|Elle agrippe le volant.
609|porter un sac à dos rouge;enlever ses bottes;porter une écharpe bleue|le ciel;un lac;un rocher;un sac à dos|Que font l'homme et la femme ?|Ils se reposent sur l'herbe.
610|porter trois rubans;serrer la grosse citrouille dans ses bras;être gros et orange|un ruban;une citrouille;un chapeau;des drapeaux|Qu'y a-t-il sur la grosse citrouille ?|Il y a un ruban bleu sur la citrouille.
613|monter sur le ring;porter des gants bleus;tenir une bouteille d'eau|un ring;un homme;un mur|Que fait l'homme ?|Il boxe sur le ring.
615|voler au-dessus de l'eau;descendre la rivière;pousser au bord de la rivière|une rivière;un oiseau;des feuilles;des pierres|Qu'est-ce qui descend la rivière ?|Deux feuilles descendent la rivière.
616|avoir les cheveux roux;porter un pull gris;être gros et rond|un rocher;le ciel;une rivière|Sur quoi se tiennent-ils ?|Ils se tiennent sur un gros rocher.
618|attacher une corde;se tenir derrière la charrette;avoir une grande roue|un arbre;une corde;une roue;de la boue|Que fait l'homme costaud ?|Il tire une charrette avec une corde.
619|hisser un panier;attendre dans la ruelle;se promener le long d'un mur|des herbes aromatiques;des oranges;un panier;une corde|Que fait la femme ?|Elle hisse un panier d'oranges.
621|se tenir à côté de la rangée;porter un chapeau rose;avoir le haut rouge|le ciel;un chapeau;des plantes;le sol|Que font les gens ?|Ils plantent de petites plantes en rangée.
622|tirer sur un élastique;se toucher le visage;marcher dans la rue|un élastique;une femme;un homme;une caisse|Que fait la femme ?|Elle tire sur un élastique.
623|regarder son téléphone;lui apporter un café;poser les pieds sur la table|un téléphone;des lunettes de soleil;une botte;une fourchette|Que fait le jeune homme ?|Il regarde son téléphone.
626|boire dans un gobelet;regarder la course;regarder sa montre|un gobelet;une montre;le ciel;une coureuse|Que fait la coureuse ?|Elle boit dans un gobelet.
627|se pavaner sur le tapis;filmer son amie;rester assis parfaitement immobile|un tapis;des guirlandes lumineuses;une cheminée;un lampadaire|Que fait la femme en bleu ?|Elle se pavane sur le tapis.
628|emballer des livres;tenir un livre;pleurer par terre|des étagères;des lunettes;des livres;des cartons|Que fait la femme ?|Elle pleure par terre.
629|fermer la porte;accrocher une veste;porter une veste jaune|une femme;un homme;des tasses;du bois|Que ferme la femme ?|Elle ferme la grande porte en bois.
630|tirer sur une longue corde;tenir la grande barre à roue;lever les deux bras|une navigatrice;une barre à roue;une corde;une voile|Que fait la navigatrice ?|Elle tire sur une longue corde.
631|couper un concombre;mélanger la salade;manger une petite tomate|une femme;un homme;de la salade;une table|Que prépare l'homme ?|Il prépare une salade.
632|mettre du sel sur des tomates;avoir les cheveux courts et foncés;se tenir dehors, devant la fenêtre|un oiseau;du sel;des tomates;du pain|Que fait la femme ?|Elle met du sel sur les tomates.
634|verser du sable sec;dessiner avec un bâton;recouvrir le dessin|une femme;un homme;une vague;du sable|Que fait l'homme ?|Il verse du sable dans sa main.
635|mettre ses sandales;porter un short vert;se tenir sur un banc|le ciel;un oiseau;un banc;des sandales|Que portent-ils aux pieds ?|Ils portent des sandales.
636|préparer un sandwich;couper le sandwich;se tenir derrière le panier|des arbres;un canard;un panier;un sandwich|Que prépare la femme ?|Elle prépare un sandwich.
638|verser de la sauce verte;manger une pomme de terre;être assis sur l'herbe|un homme;une femme;un chien;de la sauce|Que fait l'homme ?|Il verse de la sauce verte.
639|retourner les saucisses;manger un hot-dog;être posé dans une poêle|un chapeau;une tente;un oiseau;des saucisses|Que mange la femme ?|Elle mange un hot-dog.
640|soulever deux poids;montrer ses gros bras;montrer la balance du doigt|un homme;une femme;le sol;une balance|Sur quoi se tient l'homme ?|Il se tient sur une balance.
641|verser un peu de farine;porter une longue tresse;être perché sur la balance|des poêles en cuivre;un chat tigré;un bol à mélanger;une balance de cuisine|Où le chat est-il perché ?|Il est perché sur la balance de cuisine.
642|montrer son avant-bras du doigt;avoir une barbe fournie;montrer son tibia marqué d'une cicatrice|un trench-coat;une ampoule;une cicatrice;des mugs|Que montre l'homme blond ?|Il montre une cicatrice sur son tibia.
644|se couvrir la bouche;porter un sac blanc;tenir un téléphone en l'air|des lunettes;des cheveux;un sac;le sol|Que fait la femme effrayée ?|Elle se couvre la bouche.
645|dessiner un cercle;tenir un stylo noir;porter une montre|un planning;un homme;un carnet;des classeurs|Que dessine l'homme ?|Il dessine un cercle sur le planning.
647|couper des cheveux avec des ciseaux;se regarder dans un miroir;être assis sur une chaise|des ciseaux;un peigne;une serviette;des lunettes|Que fait la femme à lunettes ?|Elle coupe des cheveux avec des ciseaux.
649|gronder le jeune homme;agripper un chapeau de paille;croiser les bras|un foulard;un tablier;un portail;des choux|Que fait la vieille femme ?|Elle gronde le jeune homme.
650|ramper sur le sol;porter une longue tresse;jeter un œil par-dessus le carton|une vis;un carton;un golden retriever;un pouce|Que cherche l'homme ?|Il cherche une vis manquante.
651|serrer une vis;maintenir l'étagère en bois;être perché sur le canapé|un tournevis;des livres;un chat;une plante d'intérieur|Que fait la femme ?|Elle serre une vis avec un tournevis.
652|frapper les rochers;porter une chemise blanche;avoir les cheveux courts|la mer;une femme;un homme;des rochers|Que font-ils ?|Ils sautent dans la mer.
653|soulever un coussin;montrer les clés du doigt;être couché près de la porte|des clés;une porte;un chat;un homme|Que montre l'homme du doigt ?|Il montre du doigt les clés sur la porte.
654|chuchoter un secret;écouter son amie;regarder par-dessus le mur|le ciel;une lampe;une montagne;des lunettes|Que fait la femme en jaune ?|Elle chuchote un secret à son amie.
655|peindre une ligne noire;entrer dans la pièce en courant;souffler dans une petite trompette|un chapeau;des lunettes;du papier;une table|Que fait la femme en bleu ?|Elle peint une ligne noire sur du papier.
656|appuyer sur la pendule d'échecs;porter une veste kaki;lever les deux poings serrés|des fenêtres cintrées;une corde;une pendule d'échecs;un échiquier|Que fait la joueuse d'échecs ?|Elle appuie sur la pendule d'échecs après son coup.
657|servir le repas;verser un peu d'eau;regarder son repas|une femme;un verre;une fourchette;une table|Que fait la femme ?|Elle sert un repas à l'homme.
660|faire mousser les cheveux de son amie;se pencher au-dessus de la bassine;recueillir l'eau savonneuse|des feuilles de bananier;un robinet;une bassine;un tabouret|Que fait la femme en vert ?|Elle fait mousser les cheveux de son amie.
661|ouvrir sa grande gueule;s'approcher très près;nager en groupe|des poissons;un requin;de l'eau|Que fait le requin ?|Le requin ouvre sa grande gueule.
662|dessiner une étoile;avoir les cheveux courts;manger de l'herbe|un cheval;un taille-crayon;un carnet;un bol|Que dessine la femme ?|Elle dessine une étoile.
663|mettre de la mousse à raser;se regarder dans le miroir;regarder son ami|des lampes;un miroir;de la mousse à raser;un robinet|Que fait l'homme en bleu ?|Il met de la mousse à raser sur son visage.
664|raser le visage de l'homme;être allongé dans un fauteuil;être assis près de la fenêtre|des bouteilles;un chat;un homme;un bol|Que fait la femme ?|Elle rase le visage de l'homme.
666|mettre une chemise;regarder l'homme;boutonner sa chemise|un oiseau;une femme;une chemise|Que fait l'homme ?|Il met une chemise bleue.
667|se prendre la tête entre les mains;être couché sur le trottoir;avoir le souffle coupé sous le choc|un piéton;un casque;un scooter;le trottoir|Que fait la femme ?|Sous le choc, elle se prend la tête entre les mains.
668|lacer ses chaussures;tenir des gobelets de café;marcher dans l'eau|une porte;un pantalon;des chaussures;le sol|Que fait la femme ?|Elle lace ses chaussures marron.
669|porter un panier;lui donner le pain;payer avec des pièces|une lampe;des lunettes;du pain;un chapeau|Que fait la femme ?|Elle achète du pain dans un magasin.
671|avoir une barbe courte;porter un sac à dos bleu;avoir un long cou|le ciel;un lama;un homme;une femme|Que font les deux personnes ?|Elles crient près d'un lama.
672|tenir une serviette;porter un tee-shirt bleu;se tenir sur la douche|un oiseau;une douche;une serviette;un homme|Que fait la femme ?|Elle se douche sur la plage.
674|se moucher;lui apporter une tasse;pousser près de la fenêtre|une plante;une tasse;une couverture;une table|Que fait la femme ?|La femme malade se mouche.
675|se pencher au-dessus d'un seau;porter des lunettes;devenir bleu vif|un bateau;un filet;un homme;des seaux|Que fait l'homme blond ?|Il peint le côté du bateau.
678|tenir la soie en l'air;avoir les cheveux aux épaules;être accroupi sur le comptoir|un ventilateur;de la soie;un chat;un comptoir|Que fait la femme en beige ?|Elle presse de la soie contre sa joue.
679|nettoyer l'argent;mettre des boucles d'oreilles;être suspendu au-dessus de sa tête|une lampe;de l'argent;une femme|Que fait la femme ?|Elle nettoie de l'argent avec un chiffon.
681|regarder la caméra;conduire la voiture;être long et droit|un rétroviseur;une route;un homme;une femme|Que font-ils ?|Ils chantent dans la voiture.
683|faire couler l'eau;tenir une éponge jaune;montrer une assiette propre|un homme;une femme;un évier;des assiettes|Que lavent-ils dans l'évier ?|Ils lavent des assiettes dans l'évier.
684|être assis à table;ouvrir la porte;serrer les deux filles dans ses bras|une porte;une fille;une cuillère;une fourchette|Que font les deux sœurs ?|Les deux sœurs se serrent dans les bras.
685|essayer des chapeaux;tenir un petit miroir;vendre des chapeaux|le ciel;un chapeau;des cheveux;une robe|Que fait la fille ?|Elle essaie des chapeaux.
687|faire du skateboard;sauter en l'air;briller au-dessus de la ville|le soleil;des maisons;un garçon;un skateboard|Que fait le garçon ?|Il fait du skateboard.
688|mettre de la crème pour le visage;se frotter le bras;se toucher les joues|de la peau;le ciel;des plantes;un tee-shirt|Que fait la femme ?|Elle met de la crème sur sa peau.
689|tenir sa jupe;tourner sur soi-même;porter des chaussures blanches|une jupe;un tee-shirt;des oiseaux;des arbres|Que porte la femme ?|Elle porte une jupe jaune.
691|garder une voiture grise;balancer un bâton en bois;être garé dehors|un soldat;du fil barbelé;un mur en béton;un chemin de terre|Que fait le soldat ?|Il garde la voiture avec un bâton.
692|lever les bras;dormir sous une couverture;lire un livre|un chat;une lampe;une couverture;un oreiller|Que fait l'homme ?|Il dort sous une couverture.
693|se frotter les yeux;dormir près de la fenêtre;être posé sur ses genoux|une fenêtre;un siège;un pull;un carnet|Comment se sent la femme ?|Elle a très sommeil.
695|s'appuyer sur sa main;porter une écharpe verte;voler au-dessus du bateau|le soleil;des oiseaux;un bateau;la mer|Que font les gens ?|Ils sourient sur le bateau.
696|rire de l'homme;chasser la fumée de la main;monter dans le ciel|de la fumée;une femme;un homme;des feuilles|Que fait l'homme ?|Il chasse la fumée de la main.
697|porter une veste rouge;avoir une barbe noire;allumer une cigarette|une lampe;une cigarette;une veste|Que fait l'homme en rouge ?|Il fume une cigarette.
698|verser un smoothie;ajouter plus de fruits;mixer les fruits|un smoothie;des bananes;des fraises;une femme|Que fait la femme en orange ?|Elle verse un smoothie dans un verre.
699|passer du fromage en contrebande;lever la barrière;être chargé de foin|un garde;du foin;une barrière;une charrette|Que passe le fermier en contrebande ?|Il passe du fromage en contrebande sous le foin.
700|se déplacer très lentement;grimper sur une feuille;être posé sur le chemin|un escargot;une feuille;de l'herbe|Que fait l'escargot ?|Il grimpe sur une feuille.
701|se déplacer sur le sable;tirer la langue;se trouver sous le serpent|un serpent;un rocher;du sable;le ciel|Où le serpent est-il allongé ?|Il est allongé sur un rocher noir.
'''
src = json.load(open(f'{H}/source.json')); rows = {}
for line in DATA.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
assert len(out) == len(rows) == len(src)
json.dump(out, open(f'{H}/{CODE}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
