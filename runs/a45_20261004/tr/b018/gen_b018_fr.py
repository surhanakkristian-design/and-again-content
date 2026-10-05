from build_b018_de_fr_lib import build
T = """
4973
P se pencher sur les épices ; surveiller son étal ; dominer les jardins
N un monument ; le ciel ; des cyprès ; un bassin
Q Que fait le jeune voyageur ?
A Il pose devant un monument.
4974
P verser le thé de haut ; distribuer des tasses de thé ; l'encourager
N un vendeur ; une foule ; une guirlande ; des gobelets en acier
Q Que fait le vendeur ?
A Il verse le thé de haut.
4975
P boire du jus d'orange ; sourire à la caméra ; verser du jus d'orange
N un chapeau ; un gobelet ; un manteau ; une machine
Q Que boit la femme en bleu ?
A Elle boit du jus d'orange.
4977
P marcher à travers les champs ; se balancer sur une grande balançoire ; avoir une longue queue
N le ciel ; des palmiers ; une main ; un chemin
Q À côté de quoi l'homme est-il assis ?
A Il est assis à côté d'un singe.
4978
P casser un œuf ; voler dans les airs ; brûler sous la poêle
N un cuisinier ; un œuf ; du riz ; une assiette
Q Que fait le cuisinier ?
A Il fait cuire du riz dans une poêle.
4979
P lui donner un stylo ; prendre un stylo ; lui tendre des papiers
N un homme ; une fenêtre ; un clavier ; un téléphone
Q Que font les employés de bureau ?
A Ils se mouchent.
4980
P sentir son café ; sentir les fleurs ; écarter grand les bras
N le ciel ; des collines ; des gens
Q Que font les amis ?
A Ils prennent une grande inspiration.
4981
P sourire par-dessus son épaule ; percer la peau ; brandir le poing
N un débardeur ; une fenêtre ; une infirmière ; une poubelle
Q Que fait le jeune homme ?
A Il se fait vacciner dans le haut du bras.
4982
P frapper le ballon ; se tenir la cheville ; s'asseoir sur un banc
N un but ; un bandeau ; de l'herbe ; une cheville
Q Que tient l'homme en blanc ?
A Il se tient la cheville.
4983
P regarder un passeport ; contrôler une valise ; être allongé sous une camionnette
N une camionnette ; un agent ; une lampe torche ; une chaussure
Q Sous quoi l'agent est-il allongé ?
A Il est allongé sous une camionnette.
4984
P porter des genouillères ; serrer un skateboard ; faire du skate en costume
N le ciel ; des palmiers ; une mallette ; une promenade
Q Que porte l'homme d'affaires ?
A Il porte une mallette noire.
4985
P utiliser une perceuse sans fil ; se tenir sur un escabeau ; tendre le bras vers le plafond
N le plafond ; des écrans ; un cordon ; un chemisier
Q Que font les deux ouvriers ?
A Ils fixent l'écran au mur.
4986
P tenir une perceuse ; toucher le plafond ; sourire à la caméra
N le plafond ; des écrans ; un homme ; une femme
Q De quelle couleur sont les écrans ?
A Les écrans sont bleu vif.
4987
P présenter ses idées ; porter un plateau de cafés ; s'affaler sur la table
N des post-it ; des gobelets à emporter ; des tresses ; un ordinateur portable
Q Que porte l'homme ?
A Il porte un plateau de cafés à emporter.
4988
P porter un grand drapeau ; mener l'attaque ; regarder les combattants
N le ciel ; des drapeaux ; de l'herbe ; des tentes
Q Que porte l'homme en armure ?
A Il porte un grand drapeau.
4989
P courir devant les autres ; filmer avec un téléphone ; se dresser au pied de la colline
N des drapeaux ; une colline ; une tente ; une corde
Q Où courent les hommes ?
A Ils descendent la colline en courant.
4990
P repasser une chemise ; plier une chemise ; mettre des vêtements sur une pile
N une machine à laver ; des vêtements ; un fer à repasser ; une planche à repasser
Q Que fait l'homme ?
A Il repasse une chemise.
4991
P faire la grimace ; glisser sur une chemise froissée ; montrer une chemise bien lisse
N un rideau ; une plante d'intérieur ; un tas de vêtements ; une couette
Q Que repasse l'homme ?
A Il repasse une chemise bleue froissée.
4992
P porter beaucoup de vêtements ; ouvrir un placard ; montrer une chemise bleue
N une fenêtre ; une femme ; un fer à repasser ; une chemise
Q Que porte la femme ?
A Elle porte beaucoup de vêtements.
4993
P pagayer dans un bateau rouge ; monter sur un rocher ; se tenir à côté d'un arbre
N le ciel ; un arbre ; un bateau ; un lac
Q Où se tient la femme ?
A Elle se tient à côté d'un arbre.
4994
P faire des pâtes fraîches ; utiliser une cuillère en bois ; porter une grande assiette
N une femme ; de l'ail ; des pâtes ; une table
Q Que porte la femme ?
A Elle porte une grande assiette de pâtes.
4997
P pencher d'un côté ; se pencher hors d'une gondole ; serrer un cornet géant
N du linge ; un pont ; un canal ; une gondole
Q Que tient l'homme ?
A Il tient un cornet de glace géant.
4998
P former un long tunnel ; aspirer bruyamment ses nouilles ramen ; être suspendues au-dessus de l'étal
N des lanternes ; une veste ; des baguettes ; un bol
Q Que mange l'homme ?
A Il mange des ramen avec des baguettes.
5000
P couper de fines tranches ; poser du poisson sur du riz ; applaudir le chef
N un homme ; des sushis ; une assiette
Q Que coupe l'homme ?
A Il coupe de fines tranches de poisson.
5001
P s'asseoir près de la fenêtre ; monter une colline à pied ; porter un sac à dos
N le ciel ; des montagnes ; un village ; un sac à dos
Q Que fait la femme ?
A Elle regarde le paysage.
5002
P plonger le premier ; porter un maillot de bain rouge ; porter un bikini bleu
N le ciel ; des pins ; des nageurs ; une jetée
Q Que font les gens ?
A Ils sautent de la jetée au crépuscule.
5005
P regarder avec des jumelles ; montrer le bateau du doigt ; avancer sur l'eau
N le ciel ; une colline ; une baie ; un bateau
Q Que montre la femme du doigt ?
A Elle montre du doigt le bateau orange.
5006
P remplir la bouilloire ; verser de l'eau dans des tasses ; faire bouillir de l'eau
N une fenêtre ; une bouilloire ; des tasses ; une table
Q Que fait la femme ?
A Elle verse de l'eau dans des tasses.
5008
P ouvrir une boîte aux lettres en laiton ; trier de vieilles clés ; s'ouvrir en grand
N le ciel ; du lierre ; un cordon ; des pots de fleurs
Q Que fait la femme ?
A Elle ouvre une boîte aux lettres en laiton.
5009
P descendre un toboggan ; taper dans un ballon ; voler dans les airs
N le ciel ; un enfant ; un ballon ; de l'herbe
Q Dans quoi le garçon tape-t-il ?
A Il tape dans un ballon.
5010
P marcher sur un tapis rouge ; s'asseoir sur un trône ; tenir une couronne en or
N un drapeau ; une couronne ; un roi ; un tapis
Q Où le roi est-il assis ?
A Il est assis sur un trône.
5011
P porter un chapeau rouge ; embrasser une vieille dame ; embrasser une jeune femme
N un bâtiment ; une voiture ; une main ; une veste
Q Que fait le vieil homme ?
A Il embrasse une vieille dame.
5013
P remuer une casserole ; faire des cookies ; porter un pull noir
N une femme ; des cookies ; une bouilloire
Q Que fait la femme ?
A Elle sort des cookies du four.
5014
P goûter la soupe ; tenir un plat brûlant ; ouvrir grand les bras
N des casseroles ; la ville ; un homme ; une cuisinière
Q Que tient la femme ?
A Elle tient un plat brûlant.
5015
P avoir une longue tresse ; porter un tablier couleur rouille ; porter un foulard à motifs
N de la pâte ; un foulard ; un tablier ; des poteries
Q Que font les deux femmes ?
A Elles pétrissent la pâte ensemble.
5016
P plier les genoux ; porter des lunettes rondes ; tenir un petit marteau
N des lunettes ; un placard ; une médecin ; un genou
Q Que tient la médecin ?
A Elle tient un petit marteau.
5017
P couper un oignon rouge ; sourire à la caméra ; porter un tablier
N un homme ; un torchon ; des légumes ; un couteau
Q Que fait l'homme ?
A Il coupe des légumes avec un couteau.
5019
P faire griller du bœuf sur un gril ; tenir une feuille de laitue ; porter des lunettes
N un homme ; de la laitue ; du bœuf ; un gril
Q Que fait la serveuse ?
A Elle fait griller du bœuf sur un gril.
5020
P monter sur une échelle ; changer une ampoule ; lever le pouce
N une ampoule ; une femme ; une échelle ; un homme
Q Que fait la femme ?
A Elle change une ampoule.
5021
P verser du thé ; sourire à la caméra ; s'essuyer les mains
N un chapeau ; une dame ; une théière ; des gâteaux
Q Que fait la dame ?
A Elle verse du thé dans une tasse.
5022
P être assis à un bureau ; tenir une grande lampe ; porter une robe longue
N une lampe ; une femme ; un canapé ; des livres
Q Que fait l'homme ?
A Il est assis à un bureau.
5023
P lever les deux bras ; se tenir sur un poteau ; survoler l'homme
N un avion ; un oiseau ; de l'herbe ; le ciel
Q Qu'est-ce qui survole l'homme ?
A Un gros avion le survole.
5024
P faire signe à la caméra ; joindre les mains ; porter beaucoup de livres
N des dictionnaires ; un drapeau ; une tasse
Q Que porte la femme aux cheveux bouclés ?
A Elle porte beaucoup de dictionnaires.
5025
P regarder son téléphone ; se tenir devant le tableau blanc ; être allongé par terre
N un professeur ; un tableau blanc ; un ordinateur portable ; le sol
Q Que fait le professeur ?
A Il se tient devant le tableau blanc.
5026
P essuyer ses larmes ; rejeter la tête en arrière ; fixer les yeux écarquillés
N un tableau blanc ; un ordinateur portable ; un sweat à capuche ; un smartphone
Q Que fait l'étudiant aux cheveux bleus ?
A Il pleure de rire.
5028
P porter des livres lourds ; tenir un marteau en bois ; être ouvert sur la pile
N des livres ; des lunettes ; un juge ; un marteau
Q Que porte le jeune homme ?
A Il porte des livres lourds.
5030
P porter une haute bannière ; défiler avec leurs tambours ; courir devant les tambours
N un costume ; une perche ; des guirlandes de fanions ; des balcons
Q Que fait la femme en plumes ?
A Elle porte une bannière dans la rue.
5032
P lire une carte ; avoir de la neige au sommet ; lever le poing
N des montagnes ; une casquette ; une veste ; une carte
Q Que fait la femme en rouge ?
A Elle lit une carte.
5033
P danser dans la rue ; ouvrir grand les bras ; être suspendus au-dessus de la rue
N des drapeaux ; une femme ; un tambour ; la rue
Q Que fait la femme ?
A Elle danse dans la rue.
5034
P s'accroupir sous l'évier ; fuir sur la table ; goutter dans un seau
N une brique de lait ; un peignoir ; une flaque ; une table
Q Qu'est-ce qui goutte dans le seau ?
A De l'eau goutte du tuyau.
5035
P jongler avec trois balles ; ramasser une balle ; s'asseoir dans l'herbe
N des arbres ; un t-shirt ; un pantalon ; de l'herbe
Q Que fait la fille blonde ?
A Elle jongle avec trois balles.
5036
P apprendre à jongler ; taper dans ses mains ; porter une veste bleue
N le ciel ; des immeubles ; un homme ; une femme
Q Que fait l'homme ?
A Il apprend à jongler.
5037
P tirer une valise ; ouvrir une porte ; sourire à un client
N un bâtiment ; une femme ; une valise ; un trottoir
Q Où est la femme en manteau ?
A Elle est sur le trottoir.
5038
P étirer ses ischio-jambiers ; monter l'escalier en courant ; garder un rythme régulier
N une tour de guet ; une casquette ; une chaussure de course ; une rambarde
Q Que fait la coureuse ?
A Elle court à un rythme régulier.
5039
P ouvrir la porte d'une cage ; avoir une barbe blanche touffue ; tournoyer au-dessus de la ville
N une volée d'oiseaux ; le soleil ; une foule ; une cage
Q Que tient le vieil homme ?
A Il tient une cage vide.
5040
P tenir une lampe en laiton ; hisser une caisse en bois ; être chargé de meubles
N un fauteuil ; une caisse ; un vélo cargo ; une veste
Q Que soulèvent les deux femmes ?
A Elles soulèvent un fauteuil en velours.
5042
P tenir la porte ; porter un crop top bleu marine ; se laisser tomber sur un banc
N des arbres ; un immeuble ; un banc ; le trottoir
Q Que fait la femme aux cheveux bouclés ?
A Elle se laisse tomber sur un banc.
5044
P écouter de la musique ; tenir une tasse de café ; écouter à la porte
N une lampe ; un verre ; une tasse ; une table
Q Que fait l'homme au casque ?
A Il écoute de la musique.
5045
P se toucher l'oreille ; mettre un casque ; avoir deux grandes enceintes
N une affiche ; un magasin ; une radio
Q Que porte le jeune homme ?
A Il porte un grand casque.
5047
P tenir la télécommande ; apporter le pop-corn ; apporter une couverture
N une horloge ; une lampe ; du pop-corn ; une couverture
Q Que mangent-ils ?
A Ils mangent du pop-corn.
5048
P tripoter la clé ; tenir une pastèque mûre ; pendre aux poignées
N un foulard ; une charnière ; un cadenas ; un trousseau de clés
Q Que fait la vieille femme ?
A Elle tripote un énorme cadenas.
5049
P attacher son vélo ; tourner la clé ; briller près de la porte
N un homme ; des arbres ; un cadenas ; un portail
Q Que fait l'homme ?
A Il attache son vélo.
5050
P avoir le souffle coupé d'horreur ; enfouir son visage ; décrocher une banderole
N un diagramme en barres ; des ballons ; une cravate ; des confettis
Q Que fait l'homme aux cheveux gris ?
A Il enfouit son visage dans ses mains.
5051
P vider son sac à dos ; chercher sous le lit superposé ; fouiller dans ses vêtements
N un lit superposé ; une fenêtre ; un sac à dos ; un tas de vêtements
Q Que fait la jeune femme ?
A Elle fouille dans ses vêtements.
5054
P mettre un sac lourd sur son épaule ; pousser un chariot chargé ; charger des valises dans une camionnette
N le ciel ; des valises ; une glacière ; un chariot à bagages
Q Que soulève l'homme ?
A Il soulève des valises pour les mettre dans le coffre.
5056
P secouer un drap ; regonfler les oreillers ; plier des serviettes en forme de cygnes
N une femme de chambre ; un chariot de ménage ; un balcon ; une fleur
Q Que plie la femme de chambre ?
A Elle plie les serviettes en forme de cygnes.
5058
P faire une tête triste ; distribuer les lettres ; sortir les lettres
N un facteur ; une voiture ; une boîte aux lettres ; de l'herbe
Q Que fait le facteur ?
A Il met des lettres dans la boîte aux lettres.
5059
P ouvrir la boîte aux lettres ; apporter les lettres ; courir jusqu'à la boîte aux lettres
N une lettre ; un colis ; une boîte aux lettres ; un sweat à capuche
Q Que tient l'homme ?
A Il tient beaucoup de lettres.
5060
P tendre la main vers un jouet à empiler ; faire de la trottinette ; faire des tractions à une barre
N un musée ; une aire de jeux ; un homme âgé ; un banc
Q Que fait l'homme en bleu ?
A Il porte un petit enfant sur ses épaules.
5061
P monter par un escalator ; écarter grand les bras ; glisser dans l'eau
N un aquarium ; un tunnel ; une rambarde ; une patinoire
Q Que regarde le jeune homme ?
A Il lève les yeux vers les requins.
5063
P mener la fanfare ; jouer de la musique ; avoir les cheveux gris
N un drapeau ; des arbres ; une colonne ; un homme
Q Que fait la fanfare ?
A La fanfare défile dans la rue.
5064
P souffler dans leurs trompettes ; agiter des drapeaux nationaux ; battre leurs tambours
N des drapeaux ; un tambour ; une avenue ; une trompette
Q Que font les musiciens ?
A Ils défilent sur une longue avenue.
5065
P goûter une olive verte ; flâner dans l'allée ; pendre à des chaînes en métal
N un plafond ; une allée ; des épices ; un filet
Q Où marche le jeune homme ?
A Il flâne dans une longue allée.
5066
P manger une olive ; porter un tablier bleu ; tenir une grande cuillère
N le ciel ; une mosquée ; des oranges ; un sac
Q Que mange le jeune homme ?
A Il mange une olive verte.
5068
P porter un long voile ; embrasser la mariée ; soulever son voile
N des roses ; la mer ; une mariée ; du sable
Q Que font les mariés ?
A Ils s'embrassent sur la plage.
5070
P se percher sur le bord ; faire une grimace de douleur ; s'étaler en travers du matelas
N des fenêtres ; une tête de lit ; une femme ; un matelas
Q Où la femme est-elle allongée ?
A Elle est allongée en travers d'un immense matelas.
5071
P sourire à la caméra ; serrer les écrous de roue ; fermer le capot
N un mécanicien ; un capot ; des étagères
Q Que fait le mécanicien ?
A Il fait l'entretien de la voiture.
5073
P prendre son médicament ; tirer la langue ; boire un peu d'eau
N un médicament ; une cuillère ; un verre ; un couvercle
Q Que fait la femme ?
A Elle prend son médicament.
5074
P porter un grand carton ; serrer beaucoup de mains ; se tenir derrière elle
N une veste ; un carton ; une chaise ; un ordinateur
Q Que porte la femme en orange ?
A Elle porte un grand carton.
5075
P lécher un cornet qui coule ; avoir les mains collantes ; être plein de glaçons
N une glace ; des lunettes de soleil ; un parasol ; des pavés
Q Comment sont les mains de l'homme ?
A Ses mains sont collantes.
5076
P entrer dans la salle de sport ; afficher une coche verte ; déplacer une pièce d'échecs
N des livres ; une femme ; un échiquier ; une table
Q Que fait la vieille femme ?
A Elle déplace une pièce d'échecs.
5077
P se rappeler les réponses ; prendre des notes ; lever le poing en signe de victoire
N un pilier ; des lunettes ; un casque ; des fiches
Q Que fait l'étudiant ?
A Il essaie de se rappeler les réponses.
5078
P découper le rôti de porc ; presser un citron vert ; avoir une barbe touffue
N du porc ; un tablier ; un citron vert ; des tacos
Q Que fait le cuisinier ?
A Il découpe des tranches de rôti de porc.
5079
P mordre dans un taco ; monter les marches en pierre ; être suspendues en travers de la rue
N le ciel ; une pyramide ; un sac en paille ; des marches
Q Que fait la femme ?
A Elle mord dans un taco juteux.
5080
P se regarder dans le miroir ; prendre une photo ; se retourner vite
N un téléphone ; une plante ; une robe jaune ; un panier
Q Que porte la femme ?
A Elle porte une robe jaune.
5081
P porter un sweat à capuche bleu ; montrer le miroir du doigt ; porter une robe violette
N un miroir ; des cheveux ; une robe violette ; un tapis
Q Que fait la femme en violet ?
A Elle se regarde dans le miroir.
5082
P se toucher les cheveux ; se regarder dans le miroir ; porter un collier jaune
N un miroir ; une coiffure ; un collier ; un haut orange
Q Que fait la femme ?
A Elle se regarde dans le miroir.
5083
P battre des œufs dans un bol ; verser les œufs battus ; se lécher la pâte sur le doigt
N une cuillère en bois ; des baies ; un saladier ; de la farine
Q Que font les deux femmes ?
A Elles mélangent la pâte ensemble.
5084
P marcher vers la caméra ; porter une longue robe verte ; regarder par-dessus son épaule
N des boucles d'oreilles ; une robe ; des téléphones ; le sol
Q Que porte la femme ?
A Elle porte une longue robe verte.
5085
P montrer le panneau du doigt ; avoir une barbe ; brandir son téléphone
N une statue ; des arbres ; un panneau ; un téléphone
Q Que montre la femme du doigt ?
A Elle montre le panneau du doigt.
5086
P passer la serpillière sur le sol ciré ; tenir une réunion d'affaires ; refléter les lumières du plafond
N des lumières du plafond ; des fenêtres ; des gants en caoutchouc ; une serpillière
Q Que fait l'agente d'entretien ?
A Elle passe la serpillière sur le sol brillant du bureau.
5087
P traverser la cuisine ; nettoyer le sol sale ; laver la serpillière
N un placard ; un seau ; une serpillière ; des empreintes de pas
Q Que fait l'homme ?
A Il nettoie le sol sale.
5089
P faire cuire une crêpe ; s'envoler dans les airs ; avoir mal au genou
N une mère ; un réfrigérateur ; une crêpe
Q Que prépare la mère ?
A Elle prépare des crêpes.
5091
P sourire à la caméra ; avoir un phare rond ; porter un casque rouge
N un homme ; une moto ; la mer ; le ciel
Q Sur quoi l'homme roule-t-il ?
A Il roule à moto.
5092
P porter un grand carton ; sourire à la caméra ; arroser les plantes
N un camion ; un aide ; un canapé ; une échelle
Q Que porte la femme ?
A Elle porte un grand carton.
5093
P pousser une tondeuse à gazon ; projeter de l'herbe coupée ; arroser la pelouse tondue
N une tondeuse à gazon ; une haie ; un arroseur ; de l'herbe haute
Q Que fait l'homme ?
A Il tond la pelouse envahie par les herbes.
5094
P grimacer sous l'effort ; sourire à la caméra ; contracter les deux biceps
N une montre ; un débardeur noir ; un banc de musculation
Q Que fait le culturiste ?
A Il contracte les deux biceps.
5095
P dessiner les vieilles pièces de monnaie ; lever les yeux avec émerveillement ; pendre du toit en verre
N un toit en verre ; un squelette ; une chemise en velours côtelé ; un carnet
Q Que fixe l'homme du regard ?
A Il fixe du regard un énorme squelette.
5097
P jouer de la guitare ; lever la main ; tenir un bébé
N le ciel ; une guitare ; un bébé ; un étui à guitare
Q Que fait le guitariste ?
A Il joue de la musique dans la rue.
5098
P se filmer ; porter une longue écharpe ; couvrir le ciel
N un drapeau ; des lumières ; des gens
Q Que regarde l'homme roux ?
A Il regarde le drapeau national.
"""
build(T, 'fr')
