import json,os
H=os.path.dirname(os.path.abspath(__file__))
T="""7891|añadir una hojita;levantar la vista hacia la camarera;cortar el pescado|un hombre;una camarera;un plato;una mesa|¿Qué hay en el plato del hombre?|Hay un pequeño trozo de pescado.
7892|abrir camino;llevar unas gafas escarchadas;ir detrás de la mujer|gafas;nubes;crampones;nieve|¿Qué está haciendo la mujer?|Está subiendo por una cresta nevada.
7893|hacerse un selfi en el espejo;abrazarla por detrás;pasear por el suelo|una lámpara colgante;cajas de cartón;una bicicleta;un gato|¿Qué está haciendo la pareja?|Se están haciendo un selfi juntos en el espejo.
7894|beber de una taza;subir los escalones;montar en bicicleta|humo;un avión;una sábana;un perro|¿Dónde vive la mujer?|Vive en un avión viejo.
7896|estornudar en la mano;mirar desde arriba;abrir mucho la boca|una ventana;libros;papeles;una mesa|¿Qué está haciendo el hombre de blanco?|Está estornudando en la mano.
7897|cerrar los ojos;estar de pie en la hierba;bajar la cabeza|un granero;un caballo;una cancela;hierba|¿Qué está haciendo el hombre?|Está tocando la cara del caballo.
7898|inclinarse hacia atrás bajo la vara;arrodillarse junto al poste;dar un puñetazo al aire|el cielo;un tejado de paja;una vara de bambú;arena|¿Qué está haciendo el hombre de azul?|Se está inclinando hacia atrás bajo la vara de bambú.
7900|hacerse un selfi en el espejo;mirar con incredulidad;camuflarse con el papel pintado|papel pintado;un aplique;una palmera en maceta;una moqueta|¿Con qué combina su nuevo conjunto?|Su nuevo conjunto combina con el papel pintado de flamencos.
7901|agarrar con fuerza una funda de guitarra;tender un paño de cocina;agacharse en el suelo|una claraboya;una lámpara de aceite;una funda de guitarra;un cubo|¿Qué está haciendo la mujer?|Está agarrando con fuerza su funda de guitarra.
7902|lanzar una tortita al aire;escarbar en un bancal de hortalizas;llevar un delantal blanco|una lámpara colgante;una sartén;un golden retriever;un delantal|¿Qué está haciendo el hombre?|Está lanzando una tortita al aire.
7903|aparecer deslizándose;flotar a la deriva en aguas turbias;alzarse por encima de la barandilla|una pasarela;un cisne;una barca de remos;una farola|¿Qué está haciendo el cisne de delante?|Se está deslizando sobre el agua turquesa.
7904|grabar un vídeo selfi;llevar una camisa naranja desabrochada;colarse en la imagen|banderines;un globo aerostático;un sombrero de paja;hierba|¿Qué está haciendo la mujer de delante?|Está grabando un vídeo selfi.
7905|cruzarse de brazos;echarse a reír;llevar una camiseta blanca lisa|una luz de techo;la luna trasera;unos pantalones cortos vaqueros;una falda larga|¿Dónde está sentada la mujer de amarillo?|Está apretujada en el medio.
7906|hacer un ángel de nieve;cruzarse de brazos;tumbarse de espaldas en la nieve|un autobús de dos pisos;bicicletas;nieve;una chaqueta acolchada|¿Qué está haciendo la mujer de rojo?|Está haciendo un ángel de nieve.
7908|arrastrar una maleta;mirar en estado de shock;tocar un silbato|una lámpara de globo;un tren;ropa;una maleta|¿Qué le acaba de pasar a la mujer?|Acaba de perder el tren.
7909|quedarse en la puerta;agacharse con torpeza;llevar una bandeja de bebidas|un techo de cristal;un disfraz de dinosaurio;un cuarteto de cuerda;un vestido plateado|¿Qué lleva puesto el hombre de verde?|Lleva puesto un disfraz de dinosaurio hinchable.
7910|tocar el saxofón;bailar al ritmo de la música;dormir sobre el piano|una lámpara;un gato;un saxofón;un piano|¿Qué está haciendo el hombre?|Está tocando el saxofón.
7911|dar golpecitos a botellas con una cuchara;golpear las ollas con cucharas;cruzarse de brazos|tazas;un frigorífico;una olla;botellas|¿Qué está haciendo la mujer de rojo?|Está dando golpecitos a unas botellas con una cuchara.
7914|empapar a su vecino;usar un soplador de hojas;encaramarse a la valla|una chimenea;un soplador de hojas;una valla de madera;botas de agua|¿Qué está haciendo la mujer pelirroja?|Está empapando al vecino de al lado.
7915|sostener una caja de fideos;cocinar los fideos;marcar las doce|un reloj;el cielo;un edificio;gente|¿Qué está sosteniendo el hombre de delante?|Está sosteniendo una caja de fideos.
7917|agitarse con el fuerte viento;arremolinarse por el salar;extenderse sobre el suelo agrietado|una marquesina de autobús;un charco;montañas;nubes|¿Dónde está la marquesina de autobús?|La marquesina de autobús está en medio de la nada.
7919|pinchar el objeto brillante;llevarse las manos a la cabeza;agacharse junto a la esfera|un objeto;un palo;algas;el cielo|¿Qué hay tirado en la playa?|Hay un enorme objeto plateado tirado en la playa.
7920|enderezar un cuadro;fruncir el ceño por la concentración;tocarle el hombro al hombre|un nivel de burbuja;un globo terráqueo;un armario;una ventana|¿Qué está haciendo el hombre de rojo?|Está enderezando un cuadro.
7921|revolcarse en el barro;sacudirse el pelo mojado;sostener una toalla grande|una casa;un perro;una toalla;un cubo|¿Qué está haciendo el perro?|El perro se está revolcando en el barro.
7922|verter zumo a propósito;tender un paño de cocina;mirar hacia arriba con incredulidad|armarios;un hervidor;un paño de cocina;un charco|¿Qué está haciendo la mujer?|Está vertiendo zumo a propósito.
7923|hacer curl de bíceps con una mancuerna pesada;mirar fijamente un dónut de chocolate;deambular por el gimnasio|lámparas colgantes;una camiseta de tirantes;un dónut;una mancuerna|¿Qué está haciendo el hombre de delante?|Está mirando fijamente un dónut de chocolate.
7924|dar vueltas en la calle;balancear un bolso de cuero;llevar unos pantalones de chándal verdes|banderines;un bolso;un altavoz;adoquines|¿Qué está haciendo la mujer de azul?|Está bailando sin moverse del sitio.
7926|cruzar el sendero de un salto;derrapar hasta detenerse;dar un grito ahogado del susto|un casco;un ciervo;una bicicleta de montaña;hojas caídas|¿Qué está haciendo el ciervo?|Está cruzando el sendero de un salto.
7927|esperar en la puerta;llevar una caja;sostener una taza|una puerta;una mujer;un perro;una caja|¿Qué está haciendo el perro?|El perro está esperando en la puerta.
7928|hacer horas extra en su mesa;garabatear unas notas;frotarse la sien|un cartel de salida;una caja de comida para llevar;una taza;una chaqueta|¿Qué está haciendo la mujer?|Está haciendo horas extra en su mesa.
7930|restregar una furgoneta polvorienta;echar agua en un cubo;agacharse junto a la furgoneta|una esponja;una furgoneta camper;un muro de piedra;hormigón|¿Qué está haciendo la mujer?|Está restregando una furgoneta camper polvorienta.
7931|pasar en bici junto a un tractor;llevar un casco;conducir un tractor|el cielo;montañas;un tractor;una bici|¿Qué está haciendo la mujer?|Está pasando en bici junto a un tractor.
7935|vaciar un cuenco metálico;bajar la tapa transparente;formar una capa fina|un cuenco metálico;una tapa de plástico;un saco de tela;una planta de interior|¿Qué está haciendo el hombre?|Está volcando bolas rojas de un cuenco.
7936|contar pastillas diminutas;apoyarse en el mostrador;coger un frasco de medicina|una ventana nevada;una bufanda de rayas;un frasco de medicina;un mostrador de mármol|¿Qué está haciendo el gato?|El gato está contando pastillas con una espátula.
7937|tocar la cúpula metálica;girar una manivela de latón;dar un grito ahogado de sorpresa|una viga de acero;una pared de ladrillo;una cúpula metálica;unas zapatillas blancas|¿Qué está tocando la mujer?|Está tocando una cúpula metálica.
7938|juntar las manos;tender un plato;coger un cruasán|el cielo;árboles;un cruasán;una bolsa de papel|¿Qué está haciendo el hombre?|Le está dando un cruasán.
7939|columpiarse bajo un árbol;comer tarta de chocolate;jugar en la hierba|el cielo;un árbol;un perro;una manta|¿Qué está comiendo el hombre?|Está comiendo tarta de chocolate.
7940|mantener en equilibrio una pila de cajas;llevarse la mano a la frente;zamparse una pizza|un casco;una planta de interior;una mesa de centro;un golden retriever|¿Qué está haciendo el perro?|Se está zampando una pizza entera.
7941|mantener en equilibrio un cubo de metal;sujetar la silla;recorrer el pasillo a toda prisa|un cubo;una lámpara colgante;una silla de madera;un pomo|¿Qué está manteniendo en equilibrio la mujer de rojo?|Está manteniendo un cubo en equilibrio sobre la puerta.
7942|sostener una serpiente mascota;gritar de terror;encaramarse al reposabrazos|una serpiente;una planta colgante;un cojín;una alfombra|¿Qué está haciendo el hombre?|Está sosteniendo una serpiente mascota.
7943|sostener la tiza;frotarse las manos;sostener un palo largo|un punto;una luz;una mujer|¿Qué está sosteniendo la mujer?|Está sosteniendo un trozo de tiza.
7944|meter la mano en una bolsa;estar de pie entre los tubos;pasar en bici junto a la fuente|una farola;una chaqueta vaquera;una fuente;pelotas de tenis|¿Qué está haciendo el ciclista?|Está pasando en bici junto a la fuente.
7945|derramar la leche;limpiar el estropicio;saltar del mostrador|una lámpara de papel;un delantal;un trapo;leche derramada|¿Qué está haciendo el hombre de marrón?|Está limpiando el mostrador con un trapo.
7947|inclinarse sobre la balanza;llevar una cesta de mimbre;arrebatar la mantequilla|un mapache;una balanza de latón;mantequilla;una cesta de mimbre|¿Qué está llevando la mujer?|Está llevando una cesta de mimbre.
7949|abrazar con fuerza a un perro diminuto;posarse en la cabeza de un perro;sujetar la correa de un perro|flores;un bloque de pisos;un gatito;un rottweiler|¿Sobre qué está de pie el gatito?|Está de pie sobre la cabeza del rottweiler.
7950|inclinarse sobre la cúpula;celebrar con los brazos en alto;asomarse a la cúpula|el cielo;un castillo de arena;espuma|¿Qué está haciendo la mujer de amarillo?|Está celebrando con los brazos en alto.
7951|aplaudir con una sonrisa;marcar bíceps;levantar el pulgar|una lámpara de techo;un espejo;una camiseta de tirantes;una barra de pesas|¿Qué está haciendo el hombre de blanco?|Está marcando bíceps.
7952|gesticular con ambas manos;escuchar con atención;recostarse en un sofá|una lámpara de pie;una cortina;un cuaderno;un sofá de terciopelo|¿Dónde está tumbado el hombre?|Está tumbado en un sofá de terciopelo.
7953|tirar de una puerta cerrada con llave;dar vueltas con una falda roja;llevar un maletín negro|un maletín;banderines;una falda;el cielo|¿Qué está haciendo el hombre de negocios?|Está tirando de una puerta cerrada con llave.
7954|servir un trozo de tarta;sostener un plato blanco;reírse del perro|una lámpara;un gorro;un cuarto;el suelo|¿Qué está haciendo el perro?|Está poniendo un cuarto en el plato.
7955|lanzarse a por el balón;caer sobre el césped;llevarse las manos a la cabeza|un poste de portería;torres de pisos;una portera;césped|¿Qué está haciendo la portera?|Se está lanzando a por el balón.
7956|arrodillarse junto al coche;sostener en alto un cartel redondo;llevar un neumático viejo|el cielo;un cartel;una rueda;el suelo|¿Qué está haciendo la mujer?|Está cambiando una rueda del coche.
7957|levantar libros pesados;subir una escalera;estar de rodillas|libros;una escalera;una mesa;el suelo|¿Qué está haciendo la mujer?|Está levantando libros pesados.
7958|llevar una caja;abrir una puerta de cristal;estar de pie detrás de un escritorio|una caja;una lámpara;una papelera;un escritorio|¿Qué está llevando la mujer?|Está llevando una caja.
7960|llevar una camisa estampada;volcar un brik de zumo;aplaudir con entusiasmo|una jarra;limones;guirnaldas de luces;una botella|¿Qué está haciendo la mujer de pelo rizado?|Está aplaudiendo con entusiasmo.
7961|descorrer una cortina;olisquearle la cara;despejar una mesilla de noche|un beagle;una taza;tulipanes;un arco|¿Qué está haciendo el beagle?|Le está olisqueando la cara a la mujer de pelo rizado.
7963|mantener el equilibrio sobre un banco;trotar por el camino;taparse la cara|una farola;un caniche;mallas;un banco|¿Qué está haciendo el caniche?|El caniche está manteniendo el equilibrio sobre un banco.
7964|inclinar una pala de madera;caerse de la pala;sonreír a la cámara|una cesta de mimbre;una pala;un delantal;una bandeja de horno|¿Qué está sosteniendo el perro?|El perro está sosteniendo una pala de madera.
7965|despatarrarse en el sofá;saltar del sofá;dejar su taza|una pantalla de lámpara;estanterías;un sofá;una bolsa de tela|¿Qué está haciendo la mujer?|Está despatarrada en el sofá de terciopelo.
7967|agitar una linterna blanca;apoyarse en la pared;llevar una chaqueta azul|una pared;una cuerda;una bolsa;una roca|¿Qué está sosteniendo la mujer?|Está sosteniendo una linterna blanca.
7968|mirar hacia el techo;arrebatar la hoja de examen;garabatear en la hoja de examen|un reloj;paneles de madera;una hoja de examen;una mochila|¿Qué está haciendo el hombre?|Le está arrebatando la hoja de examen.
7969|hacerse un selfi;sostener un maletín por encima de la cabeza;apoyarse en una barra|asideros;un maletín;un gorro de lana;una chaqueta acolchada|¿Qué está haciendo el hombre de negocios?|Está sosteniendo su maletín por encima de la cabeza.
7970|sostener un cucurucho vacío;tocarle el hombro;comerse el helado|casetas de playa;una barandilla;una gaviota;un helado|¿Qué está comiendo la gaviota?|Se está comiendo el helado.
7971|marcar bíceps;ajustar la báscula;dar un puñetazo al aire|un ring de boxeo;una multitud;unos pantalones cortos de satén;una báscula|¿Qué está haciendo la boxeadora?|Está marcando bíceps sobre la báscula.
7972|señalar las vistas;reírse de alegría;llevar una pulsera de oro|el cielo;colinas;un puente de piedra;tejados|¿Qué está haciendo el joven?|Está admirando las vistas desde la torre.
7973|abrir la puerta de par en par;abrazar sus libros;agarrar las correas de la mochila|el cielo;un farol;libros;hojas de otoño|¿Qué está sosteniendo la joven?|Está abrazando un montón de libros.
7974|lanzarse sobre una tumbona;tumbarse boca abajo;llevar una nevera portátil|una torre de socorrista;una nevera portátil;una toalla de playa;una chancla|¿Qué está haciendo la mujer de naranja?|Se está lanzando sobre una tumbona.
7975|dar de comer al perro a escondidas;lamer el tenedor;aplaudir con entusiasmo|una lámpara de araña;un camarero;un candelabro;un perro|¿Qué está haciendo la mujer de azul?|Le está dando carne al perro.
7977|señalar por la ventana;sentarse en una silla;estar de pie junto a la silla|un pájaro;una lámpara;una silla;una ventana|¿Qué está haciendo la mujer?|Está señalando por la ventana.
7978|deslizarse junto al cristal;remar con las aletas;llevar un jersey azul corto|una tortuga marina;una columna;un helecho;un pasamanos|¿Qué está haciendo la tortuga marina?|Se está deslizando junto al cristal.
7979|apoyarse contra la lona;soltar risitas detrás del guante;levantar el casco por encima de la cabeza|una nube de tormenta;un pabellón;un charco;una cuerda de límite|¿Qué está haciendo la mujer de blanco?|Está soltando risitas detrás del guante.
7980|sujetarse el vestido;tocarse el pelo;servir una bebida|luces;el cielo;un árbol;una barra|¿Qué llevan puesto las dos mujeres?|Llevan puesto el mismo vestido verde.
7982|quitar la caja de un tirón;estirarse por encima de la mesa;encaramarse a la encimera|una caja de pizza;un gato;una servilleta;una lámpara colgante|¿Qué está sosteniendo la mujer?|Está apretando la caja de pizza contra el pecho.
7983|sonarse la nariz;incorporarse en la cama;traer una bandeja|una planta de interior;una bandeja;un golden retriever;zuecos|¿Qué está haciendo el perro?|El perro está trayendo una bandeja de sopa.
7984|llevar un bikini azul;señalar al otro lado de la piscina;secarse el pelo con una toalla|un socorrista;una entrada;un bikini;una piscina|¿Qué está haciendo la mujer de azul?|Está saltando a la piscina.
7985|bostezar en el sofá;estar de pie detrás del sofá;caminar por la estantería|una lámpara;un cuadro;libros;una taza|¿Qué están haciendo los tres jóvenes?|Están sentados en el sofá.
7986|tirar con fuerza de la correa;negarse a moverse;saltar por encima de la correa|un bulldog;una correa;un puente de piedra;una farola|¿Qué está haciendo la mujer de lila?|Está tirando con fuerza de la correa.
7987|cruzar la calle;esperar detrás de la tortuga;caminar muy despacio|una tortuga;un coche;una hoja;un árbol|¿Cómo está caminando la tortuga?|La tortuga está caminando muy despacio.
7988|caminar sobre una cuerda;extender los brazos;llevar unos pantalones cortos naranjas|un hombre;un río;un árbol;el cielo|¿Dónde está caminando el hombre?|Está caminando sobre una cuerda.
7989|llevar los zapatos en la mano;dormir en el sofá;estar tumbado en el suelo|un hombre;un perro;una ventana;zapatos|¿Cómo está caminando la mujer?|Está caminando sin hacer ruido.
7990|gritar de un lado a otro del campo;estar de pie sobre una caja;contemplar el campo|el cielo;una casa;una mujer;flores|¿Qué está haciendo la mujer?|Está de pie sobre una caja de madera.
7993|montar en monopatín;sentarse en el borde;estar tumbado junto a la radio|el cielo;un hombre;un perro;botellas|¿Qué está haciendo la mujer?|Está montando en monopatín.
7994|caminar por la calle;agitar su bufanda;sostener una taza|el cielo;una tienda;un abrigo blanco;nieve|¿Qué está haciendo el hombre?|Está caminando por la calle.
7995|hacer un caballito;levantar los brazos de golpe;mantener una bandeja en equilibrio por encima de la cabeza|un toldo;una moto;un camarero;adoquines|¿Qué está haciendo la motorista?|Está yendo en moto sobre la rueda trasera.
7998|mantener el equilibrio sobre una pierna;levantar los brazos por encima de la cabeza;juntar las palmas de las manos|el cielo;torres de pisos;un camión;una esterilla de yoga|¿Qué está haciendo la mujer?|Está manteniendo el equilibrio sobre una pierna.
8002|hacerse un selfi en el espejo;tirar de las asas de la bolsa;olisquear una bolsa de viaje|una lámpara de techo;una estantería;un perro salchicha;un cepillo de dientes|¿Qué está haciendo el perro salchicha?|Está olisqueando una bolsa de viaje.
8003|doblar una toalla de rayas;apoyarse en la barandilla;sentarse en el umbral|un faro;un gato;hierbas aromáticas;botas de goma|¿Qué está haciendo la mujer?|Está doblando una toalla de rayas.
8005|lanzar una bolsa de lona hacia abajo;llevar un saco de dormir;abrir una nevera portátil|una estrella de neón;una furgoneta camper;una almohada;una nevera portátil|¿Qué está haciendo el hombre?|Está arrodillado en el techo de la furgoneta camper.
8007|salir al campo trotando;salir del campo arrastrando los pies;llevar una equipación manchada de barro|un suplente;un peto de entrenamiento;árboles;el cielo|¿Qué está haciendo el jugador embarrado?|Está saliendo del campo arrastrando los pies.
8008|levantar las manos;agarrar con fuerza una baguette;lanzar agua al aire|una baguette;un sombrero de paja;una manta de pícnic;árboles|¿Qué está sosteniendo el hombre?|Está agarrando con fuerza una baguette.
8009|operar a un osito de peluche;tender un recipiente metálico;estar tumbado en la mesa de operaciones|una lámpara de quirófano;azulejos;un osito de peluche;una bandeja|¿Qué está haciendo la mujer?|Está operando a un osito de peluche.
8010|coser un plátano;aplaudir con las manos enguantadas;ajustar la lámpara de quirófano|una lámpara de quirófano;un plátano;una caja de pañuelos;una bandeja|¿Qué está haciendo el hombre de granate?|Está cosiendo un plátano.
8011|subir la montaña;sostener dos piolets;llevar una chaqueta roja|el cielo;una mujer;una roca;nieve|¿Qué está haciendo la mujer?|Está subiendo la montaña.
8012|mirar hacia el suelo;tomar a sorbos una taza de café;sentarse en los adoquines|un toldo;un mantel;un bulldog;adoquines|¿Qué está haciendo el hombre sentado?|Está tomando a sorbos una taza de café.
8013|hacerse un selfi;besarla en la mejilla;sostener en alto una chaqueta|el cielo;un árbol;una chaqueta;hierba|¿Qué está haciendo el hombre?|La está besando en la mejilla.
8014|posar junto al retrato;soltar risitas detrás de la mano;estar tumbado junto a la chimenea|una lámpara de araña;un retrato;una chimenea;un lebrel irlandés|¿Qué está haciendo la mujer?|Está soltando risitas detrás de la mano.
8015|posar para un selfi en el espejo;contener un bostezo;despatarrarse en la alfombra|una lámpara de noche;una colcha;un vestido de satén;tacones altos|¿Qué está haciendo la mujer de verde?|Está posando para un selfi en el espejo.
8016|acunar a un gatito naranja;tender una toalla;brillar sobre la puerta|un farol;un gatito;una toalla de baño;mallas|¿Qué está haciendo la mujer?|Está acunando a un gatito naranja.
8017|sostener una bebida rosa;nadar bajo el agua;sostener una pelota de playa|el cielo;una pelota;una bebida;una piscina|¿Qué está sosteniendo la mujer de azul?|Está sosteniendo una bebida rosa.
8018|levantar un ramo de novia;dar un puñetazo al aire;coger de la mano a la novia|un techo de cristal;una escalera de caracol;un ramo;una palmera|¿Qué está haciendo el novio?|Está dando un puñetazo al aire."""
src=json.load(open(f'{H}/source.json'));rows={}
for l in T.strip().split('\n'):
    i,p,n,q,a=l.split('|');rows[i]=dict(phrases=p.split(';'),nouns=n.split(';'),question=q,answer=a)
out={i:rows[i] for i in src}
json.dump(out,open(f'{H}/es.json','w'),ensure_ascii=False,indent=1)
