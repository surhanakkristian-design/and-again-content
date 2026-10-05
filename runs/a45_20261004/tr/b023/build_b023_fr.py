import json, os
D = os.path.dirname(os.path.abspath(__file__))
T = r"""
5607|brouter de l'herbe sèche;partir en fumée;flotter au vent|un château;un cheval;une bannière;des boucliers|Que fait le cheval ?|Le cheval broute sur le champ de bataille.
5608|plier les genoux;écarter grand les bras;faire signe à la plongeuse|un maillot de bain;un plongeoir;un entraîneur;une ligne d'eau|Qu'est-ce que la plongeuse s'apprête à faire ?|Elle s'apprête à plonger dans la piscine.
5610|sauter sur le canapé;se coucher à côté d'elle;caresser le chien|une cheminée;un tableau;un chien;un canapé|Que fait la femme ?|Elle caresse le chien.
5613|sourire à pleines dents à la caméra;montrer quelque chose par-dessus son épaule;peiner sous le poids|un rocher;des arches;une tresse;une clôture|Que porte la femme en noir ?|Elle porte un rocher sur l'épaule.
5614|porter un sac jaune;boire du jus vert;marcher à l'arrière|une plante;des fleurs;des fenêtres;un sac|Que porte la femme en jaune ?|Elle porte un tailleur jaune.
5615|lancer des nouilles en l'air;cuire des nouilles dans une poêle;verser de la soupe dans des tasses|des lanternes;des gens;une poêle;des tasses|Que fait le cuisinier ?|Il fait cuire des nouilles dans une poêle.
5617|couper du bois;tenir un maillet en bois;sourire à son outil|une scie;un marteau;du bois;un tablier|Que fait l'homme barbu ?|Il coupe du bois.
5618|faire tournoyer son amie;applaudir ses amies;verser du café glacé|un olivier;des toits;un coussin;une carafe|Que fait la femme en bleu ?|Elle soulève son amie du sol.
5619|lever le bras bien haut;apporter un autre plat;faire sauter des aliments dans une poêle|des casseroles en cuivre;une suspension;du poulet rôti;un sol à damier|Que fait la cheffe ?|Elle lève le bras bien haut.
5620|la soulever;toucher son visage;porter un manteau rouge|une vitrine;un manteau rouge;un homme|Que porte la femme ?|Elle porte un manteau rouge.
5621|marcher sur la pointe des pieds en chaussettes;être assise les bras croisés;être assis à côté du fauteuil|des gravures encadrées;un lampadaire;des chaussures;un tapis|Que fait la femme ?|Elle est assise les bras croisés.
5622|regarder dans un télescope;croiser les bras;tirer sur son bras|le ciel;un télescope;une lampe;du sable|Dans quoi la femme regarde-t-elle ?|Elle regarde dans un télescope.
5623|serrer une pile de disques contre soi;s'agenouiller à côté de caisses en bois;fouiller dans un carton|un casque;une applique;un carton;des caisses en bois|Que tient la femme ?|Elle serre une pile de disques contre elle.
5624|déployer ses ailes;tenir un verre de thé;montrer du doigt l'homme debout|un ventilateur de plafond;une lanterne;un perroquet;du thé à la menthe|Où le perroquet est-il perché ?|Il est perché sur l'épaule de l'homme.
5625|boire dans une noix de coco;être allongé dans un hamac;dormir sur le sable|un hamac;un chien;une valise;un bar de plage|Que fait l'homme ?|Il est allongé dans un hamac.
5627|se rouler en boule sur une étagère;bâiller à s'en décrocher la mâchoire;tendre la main vers le chat|une lampe en laiton;un chat;des carreaux de mosaïque|Où le chat est-il couché ?|Il est couché dans un espace entre les bocaux.
5628|balayer le sol;enlever ses patins;pendre du plafond|une boule à facettes;une femme;un balai;des ballons|Que fait l'homme ?|Il balaie le sol.
5630|porter en équilibre une pièce montée;s'accroupir à ses pieds;danser sous des guirlandes lumineuses|des vignes;une pièce montée;des volets;un fauteuil en osier|Que porte la femme en crème ?|Elle porte une pièce montée.
5631|se montrer du doigt l'une l'autre;se serrer dans les bras;pendre au-dessus de la terrasse|des lumières;une porte;une lampe;un canapé|Que font les deux femmes ?|Elles se montrent du doigt l'une l'autre.
5632|se prélasser dans un hamac;se rouler en boule sur sa poitrine;le regarder d'en haut en fronçant les sourcils|une clôture;un pot de peinture;un pot de fleurs;un hamac|Où l'homme se prélasse-t-il ?|Il se prélasse dans un hamac en corde.
5633|lui poser une veste sur les épaules;être assis tout recroquevillé sur un banc;briller sous le toit|une lanterne;un banc;un chien;un parapluie|Que fait la femme ?|Elle lui pose une veste sur les épaules.
5634|prendre un selfie dans le miroir;fouiller dans un tiroir;se tenir sur la couette|un lustre;un chien;une serviette;des vêtements|Que fait l'homme ?|Il fouille dans un tiroir.
5635|poser un éclat de sucre;croiser les bras;pendre du plafond peint|un lustre;un gâteau;une nappe;un parquet|Que fait la cheffe ?|Elle pose un éclat de sucre sur le gâteau.
5637|fixer le train qui passe;attaquer ses céréales;somnoler sur le rebord de la fenêtre|un train;un chat;une chaise;un plancher|Que fixe la femme ?|Elle fixe le train qui passe.
5638|attraper une araignée;porter une nuisette rose;tenir une feuille de papier|une araignée;une plante en pot;une étagère;un coussin|Que fait la femme en rouge ?|Elle attrape une araignée avec un verre.
5640|lever le poing en l'air;écarter grand les bras;se tenir sur une corniche rocheuse|une chèvre de montagne;une gourde;des chaussures de randonnée;des sacs à dos|Que fait l'homme ?|Il écarte grand les bras.
5641|rester au sec;se faire tremper;tenir un parapluie retourné|un balcon;un réverbère;un taxi;une veste en cuir|Que tient l'homme ?|Il tient un parapluie retourné.
5643|supplier la femme;pousser un chariot;porter un grand sac|un tablier;des caisses;un sac;un toit|Que fait l'homme au premier plan ?|Il supplie la femme.
5644|peindre une large bande bleue;tenir l'échelle;lever les yeux vers lui|le ciel;un rouleau à peinture;une bande;une échelle|Que fait l'homme ?|Il peint une large bande bleue.
5645|agiter les bras;crier de joie;rouler sur le sol|des livres;un panneau;un sac à dos;un chariot|Que fait la femme aux cheveux bouclés ?|Elle roule sur un chariot à livres.
5646|l'enlacer par-derrière;s'appuyer contre lui;pendre du toit de chaume|une lanterne;des palmiers;un martin-pêcheur;un coussin|Que fait l'homme ?|Il l'enlace par-derrière.
5647|prendre la tête du chien entre ses mains;tendre un peu de pain;se pencher du haut d'une échelle|un tablier;un chien;une échelle;des bols|Que fait la jeune femme ?|Elle prend la tête du chien entre ses mains.
5648|grimper près du plafond;porter un t-shirt noir;porter un legging noir|des fenêtres;des caisses;un bol;une femme|Que fait l'homme tout en haut ?|Il grimpe près du plafond.
5649|brandir un skateboard;taper dans ses mains;toucher sa jambe|le ciel;des palmiers;une bouteille|Que fait l'homme en bleu ?|Il tape dans ses mains.
5650|montrer l'escalier du doigt;porter un t-shirt à manches courtes;porter un crop top|une rampe;des billets de banque;un skateboard|Que montre l'homme du doigt ?|Il montre l'escalier du doigt.
5651|tenir un peigne;avoir l'air très surpris;dormir près de la fenêtre|une étagère;un chat;un peigne;des cheveux|Que fait le chat ?|Il dort près de la fenêtre.
5653|pousser une citrouille géante;dominer une petite citrouille;se protéger les yeux du soleil|des spectateurs;un tableau noir;une citrouille géante;une palette|Que fait la femme ?|Elle pousse une citrouille géante sur une palette.
5654|bouder sur le podium;brandir une médaille d'or;croiser les bras|un projecteur;un bouquet;une médaille d'argent;un podium|Comment se sent la femme en bleu ?|Elle est amère à cause de sa médaille d'argent.
5655|porter une chaussette rayée;éclater de rire;sortir une serviette|une chaussette;un cheval;une machine à laver;des baskets|Que porte le cheval ?|Le cheval porte une chaussette rayée.
5657|asperger d'eau bénite;joindre les mains;bénir la femme|une église;un prêtre;des filets;un bateau de pêche|Que fait le prêtre ?|Il bénit la femme sur le bateau.
5658|s'appuyer contre le comptoir;lever le poing de joie;faire glisser l'assiette vers l'avant|du carrelage mural;des casseroles;une assiette;un tablier|Que fait le cuisinier en bleu ?|Il lève le poing de joie.
5659|poser son téléphone;brandir son téléphone;prendre un croissant|une femme;un homme;un café;un croissant|Que fait l'homme dehors ?|Il tient son téléphone.
5662|lever les bras au ciel;tenir le couvercle du mixeur;essuyer la sauce sur son visage|des pots à épices;un mixeur;de la sauce tomate;une planche à découper|De quoi l'homme est-il couvert ?|Il est couvert de sauce tomate.
5663|frapper le sac;tenir le sac immobile;pendre à des chaînes|un mur;une fenêtre;un sac de frappe;une bouteille|Que fait l'homme en gris ?|Il frappe le sac.
5664|lever les bras;déplacer un pion;être assis près de la lampe|un jeu de société;un chat;une lampe;une plante|Que font les trois amis ?|Ils jouent à un jeu de société.
5665|marcher sur une planche;tenir un câble en acier;regarder depuis la corniche|un harnais;de la brume;une falaise;une planche|Que fait la grimpeuse ?|Elle marche sur une planche étroite.
5667|se lever d'un bond;faire deux pouces vers le bas;se pencher en avant sur scène|un projecteur;un avion en papier;une serveuse;un verre de bière|Que fait l'homme en orange ?|Il hue l'humoriste sur scène.
5668|montrer une table du doigt;tirer une chaise;tenir un stylo|une plante;des fleurs;une table;un livre|Que montre la femme du doigt ?|Elle montre du doigt une table près de la fenêtre.
5669|joindre les mains;tendre la main vers la poignée de la porte;porter un chemisier bordeaux|une lanterne;une porte vitrée;une carafe;une nappe|Que fait l'homme en noir ?|Il joint les mains.
5670|lever deux doigts;porter un haut en satin vert;tenir une contrebasse|des guirlandes lumineuses;une fenêtre en arc;une contrebasse;un costume en lin|Que font l'homme et la femme ?|Ils se serrent la main dans une salle spacieuse.
5672|montrer le tableau du doigt;écarquiller les yeux;porter un t-shirt bleu foncé|une fenêtre;une plante;une tasse à café;un cahier|Que fait le jeune homme ?|Il dort sur son bureau.
5674|chasser une mouche d'un geste;serrer un sandwich;froncer les sourcils, agacée|une dune de sable;un sandwich;une gourde isotherme;des dattes|Qu'est-ce qui dérange la femme ?|Une mouche la dérange.
5675|être assis attaché à une chaise;nouer un gros nœud rose;serrer le ruban|un mât;un nœud;une chaise pliante|Que fait la femme en jaune ?|Elle lui noue un nœud sur la tête.
5677|lever les deux bras en signe de triomphe;montrer le bout de la piste;se retourner, surprise|une enseigne au néon;des quilles;une gouttière;une piste de bowling|Que fait la femme ?|Elle lève les deux bras en signe de triomphe.
5678|se vernir les ongles des pieds;regarder sa montre en fronçant les sourcils;être couché sur le canapé en velours|un lampadaire;un chat;du vernis à ongles;une table basse|Que fait l'homme ?|Il regarde sa montre en fronçant les sourcils.
5679|lui toucher doucement le bras;serrer une caisse vide;lui montrer un document|un réverbère;le ciel;une cabane;une caisse en bois|Que tient l'homme ?|Il tient une caisse en bois vide.
5680|éclater de rire;être agenouillé à la table à thé;traverser la table en se dandinant|une lanterne;du bambou;un canard;une table basse|Que fait la femme ?|Elle éclate de rire.
5681|tendre les bras au-dessus de la tête;avoir le souffle coupé par la surprise;tendre le bras bien droit|une boule à facettes;des projecteurs;une piste de danse|Que fait la femme aux cheveux bouclés ?|Elle a le souffle coupé par la surprise.
5682|expirer lentement sous l'eau;passer devant la plongeuse;monter vers la surface|des bulles;un poisson;un lest;le fond marin|Que fait la femme ?|Elle souffle un filet de bulles.
5683|appuyer le menton sur la main;retirer sa veste;être à court de sable|un sablier;une table en marbre;une chemise blanche;un chemisier vert|Que fait l'homme ?|Il retire sa veste.
5685|saluer la foule;ouvrir grand les bras;applaudir|une foule;un drapeau;un homme;une rose|Que fait l'homme ?|Il salue la foule.
5686|bercer un chiot dans ses bras;gratter le menton du chiot;se pencher vers le chiot|du raisin;une lanterne;un chiot;une gamelle d'eau|Que fait l'homme ?|Il gratte le menton du chiot.
5687|livrer des pains frais;descendre de son vélo cargo;être rempli de pains|des guirlandes lumineuses;une cycliste;des pains;une caisse|Que fait la cycliste ?|Elle livre des pains frais.
5689|régler les curseurs;parler dans le micro;briller au-dessus de la porte|une antenne radio;un casque;un micro;une table de mixage|Que fait l'homme ?|Il parle dans un micro.
5691|prendre un selfie dans le miroir;battre des ailes;se frotter le front|un lustre;un perroquet;une chaise en rotin;une jupe|Que fait le perroquet ?|Il bat des ailes à côté de son visage.
5695|traverser la piste sablonneuse;agripper l'arceau de sécurité;s'arrêter près des buissons épineux|la brousse;une termitière;une antilope;un arceau de sécurité|Que fait l'antilope ?|Elle traverse la piste sablonneuse.
5696|payer les fleurs;prendre l'argent;dormir sous la table|une fenêtre;un homme;une table;un chien|Qu'achète la fille en jean ?|Elle achète des fleurs.
5697|serrer un bouquet de dahlias contre soi;tendre la main vers le billet;attendre son tour|une verrière;une balance suspendue;un bouquet;du papier d'emballage|Que fait la femme aux cheveux bruns ?|Elle achète un bouquet de dahlias.
5698|réclamer le ballon;essayer de contrer son tir;tenir le ballon au-dessus de la tête|un ballon de basket;un panier;un crop top;une clôture|Que fait la femme ?|Elle réclame le ballon.
5699|lui faire signe de venir;s'avancer vers lui d'un pas tranquille;reposer sur le rivage|le ciel;un lampadaire;un bateau;du sable|Que fait l'homme ?|Il lui fait signe de venir.
5700|tenir la porte ouverte;agripper le guidon;traverser le porche en flânant|une lanterne;une porte;un vélo;un pot de fleurs|Que fait l'homme ?|Il agrippe le guidon.
5701|tendre une ardoise;crier avec enthousiasme;être agenouillée sur le toit pentu|des nuages d'orage;la mer;une ardoise;des tuiles|Que fait la femme ?|Elle crie depuis le toit.
5702|fermer les yeux;lui toucher l'épaule;expirer lentement|une lampe;un homme;une femme;une moto|Que fait l'homme ?|Il ferme les yeux.
5703|attaquer sa glace;faire des gestes d'incrédulité;se blottir sous une couverture|une suspension;un sac à main;une couverture;un canapé|Que fait la femme en pyjama ?|Elle attaque sa glace.
5704|soulever une poutre en acier;agripper une poignée suspendue;se relever d'une position accroupie|une poutre en acier;un crochet de grue;une cape;des gratte-ciel|Que fait la super-héroïne ?|Elle soulève une énorme poutre en acier.
5705|brandir sa clé de voiture;marcher entre les voitures;être assis sur une voiture|une lumière;une voiture;un chat;une femme|Que fait la femme ?|Elle marche entre les voitures.
5706|lever le bras en signe de triomphe;lever les yeux au ciel;être couché sous la table|un porte-bagages;des gobelets en carton;des cartes;un épagneul|Que fait l'homme ?|Il lève les yeux au ciel.
5707|bercer une tortue dans ses bras;tendre une fraise;grignoter une fraise|un lac;une tortue;un parterre de fleurs;un bol de fraises|Que fait l'homme ?|Il donne des fraises à la tortue.
5708|ouvrir grand son manteau;serrer un chien mouillé contre soi;se tenir derrière un caddie|un réverbère;un caddie;un chien;du bitume|Que fait la jeune femme ?|Elle serre le chien mouillé contre sa poitrine.
5711|caresser la tête de l'éléphant;engloutir du lait au biberon;enrouler sa trompe vers le haut|des acacias;une clôture;un biberon de lait;une couverture|Que fait l'homme ?|Il donne le biberon à un éléphanteau.
5714|grignoter une pomme de pin;sauter d'une pierre tombale;filer sur l'herbe givrée|des pins;un écureuil;une pierre tombale;de l'herbe|Que fait l'écureuil ?|L'écureuil grignote une pomme de pin.
5715|découper une lettre manuscrite;maintenir une règle en métal;parcourir des papiers|une arche en pierre;une lampe de bureau;des enveloppes;une lettre|Que fait la femme au premier plan ?|Elle découpe une lettre avec une lame.
5716|montrer du doigt les manchots qui passent;avancer en se dandinant le long du rivage;se rassembler autour d'une caisse|un bonnet;un iceberg;des manchots;un sac à dos|Que fait la femme ?|Elle compte les manchots sur le rivage.
5717|tourner sur elle-même encore et encore;tendre les bras;voler au-dessus des murs|le ciel;une femme;du sable;un cercle|Que fait la femme ?|Elle tourne sur elle-même au centre.
5718|retirer un bloc de bois;maintenir la base;lever les deux mains, alarmée|une ampoule;une tour;un livre;une tasse|Que fait la femme ?|Elle lève les deux mains, alarmée.
5719|apposer un sceau en laiton;brandir le certificat;sourire de bonheur|un lustre;une plante en pot;un gilet;un certificat|Que fait la jeune femme ?|Elle sourit de bonheur.
6814|rouler le long d'une chaussée submersible;tenir son chapeau;se dresser sur une île rocheuse|une abbaye;un chapeau de paille;un imperméable;un vélo|Que fait la femme ?|Elle roule à vélo le long d'une chaussée submersible.
6815|presser un demi-citron;filmer avec son téléphone;dominer la foule|un lion;des lunettes de protection;une bandelette de test;un bol|Que fait la femme aux lunettes de protection ?|Elle presse un demi-citron.
6816|se protéger les yeux du soleil;jouer d'un piano droit;incliner un arrosoir|un arrosoir;un ventilateur électrique;un piano droit;une chaise en bois|Que fait l'actrice ?|Elle mime une tempête sur scène.
6817|crier dans un mégaphone;s'agenouiller sur la route;représenter un globe en feu|un policier;une militante;un drapeau;un camion|Que fait la militante ?|Elle crie dans un mégaphone.
6818|traverser le bureau en patins à roulettes;porter de lourds classeurs;porter un pull vert|un employé administratif;des classeurs;un vieil ordinateur;des patins à roulettes|Que fait l'employé administratif ?|Il traverse le bureau en patins à roulettes.
6819|se tenir sur une estrade;tenir une chemise bleue;flotter au vent|un drapeau;un remorqueur;une amirale;une estrade|Où se tient l'amirale ?|Elle se tient sur une estrade en bois.
6821|jeter un œil dans son portefeuille;porter un plateau de fruits de mer;verser le champagne|un lustre;un homard;un menu;un portefeuille|Qu'apporte le serveur ?|Il apporte un énorme plateau de fruits de mer.
6823|lever les yeux, sous le choc;se déverser sur le trottoir;bloquer la rue étroite|un bateau de pêche;un chien;une caisse;des algues|Que fixe la femme ?|Elle fixe un bateau échoué.
6825|secouer une couette blanche;arranger les oreillers;reposer sur un oreiller|un clocher;des géraniums;une couette;un tapis|Que fait la jeune femme ?|Elle secoue une couette au-dessus du balcon.
6826|se prélasser sur un banc;rouler sur le sol;se pencher par-dessus le mur|des rideaux;un carillon éolien;un chapeau de paille;un chat|Que fait l'homme ?|Il se prélasse sur un coussin bleu.
6827|dormir sur un oreiller blanc;lever la tête;être posé sur un journal|une femme;un oreiller;un réveil;un verre|Que fait la femme ?|Elle dort sur un oreiller blanc.
6828|écarter grand les bras;mener une file d'ouvriers;porter un porte-bloc|une sonnerie d'alarme;un voyant d'alerte;le plafond;un casque de chantier|Que fait la femme ?|Elle écarte grand les bras.
6829|étudier un guide de voyage;lever les yeux vers les enseignes;tendre un sac en papier|une lanterne;un guide de voyage;une valise;une enseigne|Que fait la femme blonde ?|Elle étudie un guide de voyage.
6830|être suspendue à des cordes;tourner lentement dans les airs;rester inutilisé près des portes|de l'aluminium;un toit en tôle ondulée;un chariot élévateur;un casque de chantier|Que fait la coque du bateau ?|La coque est suspendue à des cordes.
"""
src = json.load(open(f'{D}/source.json'))
rows = {}
for line in T.strip().splitlines():
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{D}/fr.json', 'w'), ensure_ascii=False, indent=1)
