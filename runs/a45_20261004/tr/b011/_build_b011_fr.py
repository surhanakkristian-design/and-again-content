import json, os
H = os.path.dirname(os.path.abspath(__file__))
R = """
4063|pendre au-dessus des nuages;lâcher l'homme;plonger vers les nuages|des sangles;un harnais;des bottes;des nuages|Que fait l'homme ?|Il plonge vers les nuages.
4064|soutenir un nid énorme;tenir en équilibre sur le poteau;porter une minuscule caméra|un nid;des lignes électriques;un poteau;un champ|Où vole la perruche ?|Elle vole vers le nid sur le poteau.
4065|être le conducteur;montrer sa langue;se cacher derrière un siège|des arbres;un conducteur;un chat;un volant|Qui est assis à la place du conducteur ?|Un chien blanc est assis à la place du conducteur.
4066|ajuster un minuscule casque;conduire une moto tout-terrain;planer au-dessus d'une butte|un casque;un perroquet;une moto tout-terrain;de la terre|Que fait le perroquet ?|Il conduit une minuscule moto tout-terrain.
4067|plonger dans le lac;refléter les sapins;dominer l'eau|le ciel;des sapins;des ondulations;un rocher|Que reflète le lac ?|Le lac reflète les sapins.
4068|caresser un requin-tigre;projeter une ombre sombre;glisser à côté d'un requin|une plongeuse;un requin;une ombre;le fond marin|Que fait la femme ?|Elle caresse un requin-tigre.
4069|tenir une canne à pêche;émerger de la mer;fusiller la sirène du regard|le ciel;un pigeon;une canne à pêche;des planches|Que tient le petit oiseau ?|Il tient une fine canne à pêche.
4070|lâcher prise la première;porter un casque de protection;pendre à côté de la roue|une aile;un casque;une roue;la côte|Que font les deux personnes ?|Elles pendent sous l'aile.
4071|sauter d'une épave;glisser à côté d'un requin;rouiller dans l'eau peu profonde|une épave;des nuages;une femme;la mer|Que fait la femme ?|Elle saute d'une épave rouillée.
4072|flâner vers l'eau;briller d'un turquoise éclatant;se pencher au-dessus du sable|un lagon;une plage;des palmiers;une falaise|Qu'est-ce qui s'étend entre les falaises ?|Un lagon turquoise s'étend entre les falaises.
4073|câliner un poussin endormi;garder ses trois poussins;déployer une aile pâle|un bâton;un bec;des poussins|Que fait la poule ?|Elle menace un pigeon avec un bâton.
4074|porter un maillot de bain rouge;briller sur l'eau;voler dans le ciel|le soleil;un bateau;de l'eau;le ciel|Que fait le soleil ?|Le soleil se couche derrière une colline.
4075|flotter dans la mer;tenir les bras écartés;porter un maillot de bain noir|des requins;une femme;la mer|Que fait la femme ?|Elle flotte dans la mer.
4076|porter un short noir;porter un pantalon blanc;s'envoler|le ciel;un homme;une femme;une ville|Que font l'homme et la femme ?|Ils sautent d'un hélicoptère.
4077|voler au-dessus du nid;se rendormir;briller dans le ciel|la lune;le ciel;un oiseau;un nid|Que fait l'oiseau blanc ?|Il dort dans le nid.
4078|traverser le lit à quatre pattes;écarter grand les bras;être suspendu au-dessus du lit|une tenture murale;des oreillers;une femme;une couette|Que fait la femme ?|Elle avance à quatre pattes vers la rangée d'oreillers.
4079|rebondir sur les vagues;écumer entre des rochers sombres;attendre sur la rive|une forêt;des pagayeurs;la rivière;un kayak|Que fait la rivière ?|La rivière dévale entre les rochers.
4080|fouiller dans un tiroir;enlever un élastique à cheveux;bouder dans un sweat à capuche rose|des sourcils;des lèvres;un poignet;un pull|Où sont les élastiques à cheveux ?|Ils sont au poignet de la mère.
4081|s'accroupir sur le patin;rester en vol stationnaire au-dessus des montagnes;marquer le point d'atterrissage|le soleil;un hélicoptère;un sommet;une vallée|Que fait l'hélicoptère ?|Il reste en vol stationnaire au-dessus des sommets enneigés.
4082|pendre la tête en bas;agripper le hauban de l'aile;tomber vers le récif|une aile;des nuages;un hauban;un récif|Que fait la femme ?|Elle pend la tête en bas.
4083|être couché au milieu;porter un pyjama violet;avoir une barbe|une femme;un chien;un homme;une couverture|Où le chien est-il couché ?|Le chien est couché au milieu.
4084|toucher sa tête;voir pousser des cheveux jaunes;être assis sur le miroir|un miroir;un homme;un chat;un robinet|Que touche l'homme ?|Il touche sa tête.
4085|jouer à un jeu vidéo;porter un costume bleu;pousser l'homme à l'intérieur|une porte;un homme;une femme;des escaliers|À quoi joue l'homme ?|Il joue à un jeu vidéo.
4086|piquer un crâne chauve;dormir sous une couverture;pousser un cri|la lune;un moustique;un oreiller;une couverture|Que fait le moustique ?|Il pique un crâne chauve.
4087|taper sur un ordinateur portable;être assis sur le lit;afficher un graphique|un chat;un ordinateur portable;du papier;un bureau|Sur quoi le chat tape-t-il ?|Il tape sur un ordinateur portable.
4088|tomber par-dessus le bord;s'élever dans les airs;avoir de petits nuages blancs|le ciel;une rivière;une cascade|Où tombe l'eau ?|Elle tombe par-dessus un large bord.
4089|prendre la caméra;danser avec des lunettes de soleil blanches;briller d'un rouge vif|une pieuvre;une caméra;du sable|Que fait la pieuvre aux lunettes de soleil ?|Elle danse sous les méduses rouges.
4090|s'élever le long de la tour;rester fermement en place;se répandre sur le sol|une fusée;une tour de lancement;de la fumée;du béton|Que fait la fusée ?|Elle s'élève le long de la tour de lancement.
4091|s'accroupir sur le lac gelé;verser du thé fumant;se fissurer dans toutes les directions|un bonnet;des lunettes de soleil;un thermos;de la vapeur|Qu'arrive-t-il à la glace ?|La glace se fissure dans toutes les directions.
4092|descendre les marches;briller au-dessus de la mer;mener à la mer|le soleil;la mer;des marches;un vélo|Où va le vélo ?|Le vélo descend les marches.
4093|grandir régulièrement;briller sur fond d'obscurité;révéler ses cratères|la lune;des cratères;le ciel|Que fait la lune ?|La lune ronde brille sur fond d'obscurité.
4094|boire de l'eau;marcher le long de la route;avoir la tête marron|un cheval;des sacs;un mur|Que font les deux chevaux ?|Les chevaux mangent leur nourriture.
4095|suivre une autre voiture;porter une veste bleue;porter des lunettes de soleil|le ciel;des lunettes de soleil;une tablette;un écran|Que tournent les gens ?|Ils tournent un film.
4096|s'éloigner à la nage;couper la corde;porter un short noir|un homme;une tortue;un filet;du sable|Que fait la tortue ?|Elle s'éloigne du filet à la nage.
4097|sauter en l'air;rouler devant;porter une chemise blanche|le ciel;un cycliste;une colline;une roue|À quelle vitesse va le cycliste ?|Le cycliste va très vite.
4098|écarter le veau;pencher la tête sur le côté;avoir de longues cornes recourbées|une cloche;un sentier;un veau;un gant|Que font les animaux ?|Ils barrent le passage au cycliste.
4099|être assis sur les matelas;porter une chemise rouge;rouler entre les voitures|des bâtiments;un chien;des matelas;une moto|Où le chien est-il assis ?|Il est assis sur les matelas.
4100|être allongé sur le lit;faire un grand trou;être accroché à la fenêtre|un trou;un ressort;un homme;un rideau|Qu'y a-t-il dans le plafond ?|Il y a un grand trou dans le plafond.
4101|ouvrir les bras;montrer sa grande queue;regarder le spectacle|de la lumière;un oiseau;un téléphone;des gens|Que montre l'oiseau ?|L'oiseau montre sa grande queue.
4102|taper sur un ordinateur portable;voler au bout d'une ficelle;briller dans le ciel|le soleil;un cerf-volant;une table;de l'herbe|Quel temps fait-il ?|Le soleil brille dans le ciel.
4103|épier de derrière un panneau;dépasser du carton;chiper la saucisse|un chiot;une saucisse;un tapis;une porte|Que fait le chiot ?|Il épie la saucisse avec patience.
4104|embrasser l'oiseau gris;devenir rouge au visage;être grand et sombre|un oiseau gris;un oiseau blanc;des arbres|Que fait l'oiseau blanc ?|Il donne un baiser à l'oiseau gris.
4105|toucher ses cheveux;attendre près de la voiture;se couvrir la bouche|une voiture;des fleurs;un homme|Qui attend près de la voiture ?|Son petit ami attend près de la voiture.
4106|tenir une fourchette;manger ses pâtes;rire du chien|un homme;un chien;des pâtes;une table|Que fait le chien ?|Le chien affamé mange ses pâtes.
4107|recouvrir l'éléphant;agiter la main;montrer ses dents|un tigre;un homme;un téléphone|Qu'est-ce qui recouvre l'éléphant ?|Un drap recouvre l'éléphant.
4108|faire signe depuis la voiture;tenir le volant;se tenir à côté de la voiture|une voiture;un oiseau;une maison|Que fait l'oiseau blanc ?|Il se tient à côté de la voiture.
4109|laper l'eau;bondir avec excitation;projeter de l'eau vers le haut|une haie;une fontaine;une pelouse|Que fait le chien noir ?|Il boit à la fontaine sur la pelouse.
4110|être allongé par terre;être assis à côté du clown;tomber sur l'éléphant|un clown;un tigre;un téléphone|Où le tigre est-il assis ?|Il est assis à côté du clown.
4111|tenir un marteau;pousser l'homme;porter des lunettes de soleil|un homme;un mouton;un marteau;le ciel|Que fait le mouton ?|Le mouton agaçant le pousse.
4112|faire un trou;tenir une bouteille;recueillir la poussière|une fenêtre;une bouteille;un gant;un bloc|Que fait la perceuse ?|Elle fait un trou dans un bloc.
4113|porter une bague rose;crier sur un autre oiseau;les regarder d'en haut|des bijoux;un oiseau blanc;des bâtiments;une rue|Que porte l'oiseau gris ?|Il porte une bague rose.
4114|montrer un mannequin du doigt;se promener pieds nus;présenter une robe dorée|un mannequin;des rideaux;un short;des talons hauts|Que montre la femme du doigt ?|Elle montre du doigt le mannequin dans le centre commercial.
4115|lever le bras;se retourner et rire;porter une jupe blanche|des touristes;des lunettes de soleil;des chapeaux|Qui passe devant les chapeaux ?|Deux touristes passent devant les chapeaux.
4116|monter dans la voiture;être assis sur un banc;être petite et rouge|une voiture;un banc;un arbre;de l'herbe|Que conduit l'homme ?|Il conduit une petite voiture rouge.
4117|regarder sous le canapé;tenir un téléphone;montrer la table du doigt|un téléphone;des clés;une main;une table|Que montre la femme du doigt ?|Elle montre la table du doigt.
4118|sprinter à travers le court;être tendu entre deux poteaux;dominer le court|un court;un filet;un sommet;une prairie|Que fait le joueur ?|Le joueur sprinte à travers le court.
4119|s'effondrer en tas;étendre les deux bras;dominer le rivage|des pins;du bois flotté;des galets;des algues|Qu'arrive-t-il à la figure de pierre ?|Elle s'effondre en tas.
4120|reposer en travers du bol;recueillir les coquilles cassées;se trouver derrière la planche|des noix;une planche;des coquilles;un bol|Où repose la planche ?|La planche repose en travers du bol.
4121|traverser la carrière en se balançant;basculer en flammes;filmer l'explosion|de la fumée;des silos;une passerelle;une caméra|Que filme la caméra ?|Elle filme une scène d'explosion dans une carrière.
4122|tenir un pistolet;écrire avec un stylo;pousser dans un pot|une fenêtre;une plante;un pistolet;un bureau|Que fait l'homme masqué ?|Il braque l'homme au bureau.
4123|fondre en larmes;être à genoux dans une flaque;se rassembler au pied de la falaise|des larmes;une feuille de papier;une flaque|Que fait la fille ?|Elle est à genoux dans une flaque de larmes.
4124|rouler sur la route;dormir sur une couverture;brûler entre les pierres|le ciel;un van;un feu;un chien|Qu'est-ce qui roule sur la route ?|Un van roule sur la route.
4126|avoir des pointes acérées;afficher le mot « danger »;avoir beaucoup de fenêtres éclairées|le ciel;des bâtiments;des hommes|Que regardent les deux hommes ?|Ils regardent les hauts bâtiments.
4127|sauter le long de la route;manger une carotte;toucher la fourrure douce|des yeux;une carotte;une main|Que fait la main ?|Elle touche la fourrure douce.
4128|courir dans la cour;s'avancer sur l'herbe;tirer la langue|une clôture;un chiot;une allée;de l'herbe|Que fait le chiot ?|Il court dans la cour.
4129|s'ouvrir lentement;quitter la maison;descendre les marches|des arbres;une voiture;une clôture;un chiot|Que fait le chiot ?|Il quitte la maison avec un chapeau vert.
4130|tailler les cheveux du gorille;lever le pouce;tapoter sa coupe en brosse plate|des bouteilles;un gorille;un nœud papillon;un fauteuil de barbier|Que fait le chat ?|Il fait au gorille une coupe en brosse plate.
4131|coiffer le singe;porter une blouse blanche;montrer ses dents|un mur;un singe;un chat|De quelle couleur est le mur ?|Le mur est vert foncé.
4132|brosser les cheveux mouillés;laver la tête du lion;être assis dans un fauteuil noir|un lion;un chat;une brosse;un lavabo|Que fait le chat ?|Le chat brosse les cheveux du lion.
4133|serrer un gros chien dans ses bras;toucher la tête du chien;être couché près du frigo|un frigo;un homme;une gamelle;un chien|Que fait l'homme ?|Il serre un gros chien dans ses bras.
4134|avoir un gros ventre;être assis sur une chaise noire;se couvrir la bouche|un chat;un miroir;une chaise;des bouteilles|Où le gros animal est-il assis ?|Il est assis sur une chaise noire.
4135|taper dans le ballon;se tenir dans le but;courir sur l'herbe|une femme;un ballon;un but;de l'herbe|Que fait la femme ?|Elle tape dans un ballon.
4136|faire de l'exercice au sol;soulever des poids lourds;se tenir sur le banc|un banc;un rideau;un pantalon;le sol|Que fait l'homme ?|Il fait de l'exercice avec les chiens.
4137|porter une robe jaune;ramasser un jouet;mordre un jouet jaune|un chien;une robe;un lit;une chaise|Que tient le chien ?|Le chien tient un jouet jaune.
4138|caresser le chien;tenir une glace;courir sur l'herbe|un chien;une casquette;une glace;un pantalon|Que fait l'homme ?|Il caresse le chien.
4139|gravir un sentier;voleter au-dessus de l'herbe;dominer le flanc de la colline|un sentier;un sac à dos;un sommet;de l'herbe|Où l'homme marche-t-il ?|Il gravit un sentier étroit.
4140|sauter dans l'eau;descendre la colline en courant;briller dans le ciel|une montagne;des gens;un pont;une rivière|Où les trois personnes sont-elles assises ?|Elles sont assises sur un pont au-dessus d'une rivière.
4141|bronzer en short rose;descendre le long d'une falaise;plonger dans une gorge|le ciel;une cascade;une falaise;des baskets|Que font les six hommes ?|Ils sont allongés à plat sur le dos.
4142|tomber dans l'eau;nager dans la mer;danser sur la route|des nuages;le soleil;une route|Que fait la femme en blanc ?|Elle danse sous la pluie.
4144|regarder hors d'une boîte;être posé en cercle;être long et gris|un tapis;une boîte;le sol;un tuyau|Où le tuyau est-il posé ?|Le tuyau est posé sur le sol.
4145|plonger vers le ballon;tenter un retourné acrobatique;célébrer les poings levés|un ballon de volley;un voilier;une éclaboussure|Que fait l'homme blond ?|Il plonge vers le ballon.
4146|sprinter vers la mer;s'effondrer dans les vagues;être allongé immobile dans l'écume|le ciel;de l'écume;des baskets;du sable|Que fait l'homme ?|L'homme épuisé est allongé dans l'écume.
4147|se hâter vers la voiture;porter une grande enseigne;rire dans la voiture|une enseigne;un homme;une voiture|Que porte l'homme ?|Il porte une grande enseigne jaune.
4148|caresser le capot;appuyer sur le bouton de démarrage;rouler tranquillement dans le parking|un volant;un costume;un siège|Sur quoi l'homme appuie-t-il ?|Il appuie sur le bouton de démarrage.
4149|dégringoler dans le ciel;ouvrir un œil énorme;fuir à travers le lac|des pins;un castor;un géant|Sur quoi le castor est-il assis ?|Il est assis sur la tête d'un géant.
4150|filer sur la route;s'approcher de la voiture garée;refléter le ciel nuageux|le ciel;une voiture de sport;un homme;du gravier|Que fait la voiture de sport ?|Elle file sur une route de campagne.
4151|tenir un stylo;devenir rose;être accrochée au mur|une voiture bleue;une voiture rose;une table|Que fait la main ?|Elle dessine une voiture rose.
4152|s'abaisser sur le gravier;se trouver dans la remorque;dominer la remorque|une remorque;une voiture de sport;une rampe;du gravier|Qu'est-ce qui est garé dans la remorque ?|Un véhicule est garé dans la remorque.
4153|rouler sur l'autoroute;avoir de la neige au sommet;planer au-dessus des champs|des montagnes;un nuage;une voiture;une autoroute|Que fait la voiture bleue ?|Elle roule sur l'autoroute.
4154|frapper une balle de tennis;tenir une raquette;regarder depuis un balcon|un bâtiment;des palmiers;une raquette;une femme|Que fait la femme ?|Elle frappe une balle de tennis.
4155|laver une assiette sale;regarder dans les toilettes;tenir une assiette propre|un chaton;une plante;une assiette;des toilettes|Que fait le chaton ?|Il lave une assiette dans les toilettes.
4157|brandir une pancarte en carton;border l'avenue mouillée;joncher la route|une arche;une écharpe;une pancarte en carton;des feuilles|Que font les coureurs ?|Ils passent en courant devant une femme âgée.
4158|s'accrocher à une perche;faire un grand sourire à la loutre;gonfler comme un ballon|un requin;du bambou;une loutre;le ciel|Qu'arrive-t-il au requin ?|Le requin géant gonfle comme un ballon.
4159|voler au-dessus de l'herbe;se dresser derrière les arbres;traverser le champ|le ciel;des montagnes;des arbres;des chaussures|Que fait la personne ?|La personne vole haut au-dessus des arbres.
4160|s'éloigner rapidement;disparaître au bout de la route;s'élever derrière la voiture|le ciel;une route;une voiture;du sable|Que fait la voiture ?|La voiture disparaît au bout de la route.
4161|avancer lentement;rester au même endroit;regarder les voitures|un homme;une fenêtre;un phare;le sol|Que regarde l'homme ?|Il regarde l'avant de la voiture.
4162|être garée seule;s'élever au-dessus de la ligne des toits;tournoyer en volée|une esplanade;une tour;une volée;des colonnes|Qu'est-ce qui est garé sur l'esplanade ?|Une voiture de sport est garée sur l'esplanade.
4163|parler à la caméra;être jaune vif;briller dans le noir|un homme;une voiture;une lampe|Que fait l'homme ?|Il parle à la caméra.
4164|prendre un virage;avoir des feux rouges;regarder la voiture verte|un frein;une roue;une route|Que fait la voiture verte ?|Elle prend un virage.
4165|sourire à la caméra;arriver au détour d'un virage;être grands et verts|une voiture;des arbres;une route;des rochers|Que fait l'homme ?|Il conduit à grande vitesse.
"""
out = {}
for l in R.strip().split('\n'):
    i, p, n, q, a = l.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
json.dump(out, open(f'{H}/fr.json', 'w'), ensure_ascii=False, indent=1)
