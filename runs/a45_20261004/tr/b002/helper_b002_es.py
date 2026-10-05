import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
620|oler una rosa de color rosa;cerrar los ojos;brillar en el cielo|una mujer;una rosa;una cesta;el sol|¿Qué está haciendo la mujer?|Está oliendo una rosa de color rosa.
5310|abrazar al niño;llevar una camiseta gris;pasar volando por delante del garaje|un niño;una pelota;un hombre|¿Qué está haciendo la mujer?|Está abrazando al niño.
41|sostener un martillo;tener el pelo negro;colgar en la pared|un cuadro;un martillo;una mujer;un hombre|¿Qué están haciendo el hombre y la mujer?|Están teniendo una discusión.
5499|llevar un vestido rojo;correr por la calle;regar las flores|una mujer;flores;una ventana;una pared|¿Qué está haciendo la mujer mayor?|Está regando las flores.
119|dar una luz cálida;sostener una taza;tener el pelaje gris|una bombilla;un gato;un cuenco;libros|¿Qué está sosteniendo la mujer?|Está sosteniendo una taza.
166|dibujar un círculo grande;sostener un palo largo;estar de pie en círculo|una mujer;el cielo;un círculo;el mar|¿Qué está dibujando la mujer?|Está dibujando un círculo en la arena.
596|ganar la carrera;llevar una camiseta amarilla;llevar una camiseta morada|corredores;hierba;una pista|¿Quién está ganando la carrera?|El corredor de amarillo está ganando la carrera.
484|limpiar el suelo;estar a punto de caerse;estar lleno de agua|una mujer;una fregona;un cubo;el suelo|¿Qué está haciendo la mujer?|Está limpiando el suelo con una fregona.
68|sonreír a la cámara;llevar gafas;rodear su mano|gafas;un pulgar;una venda;un banco|¿Qué está haciendo el hombre?|Le está poniendo una venda en la mano a ella.
5149|llevar una bolsa de papel;subir por una escalera alta;brillar con un verde intenso|una cruz;botellas;una bufanda;una caja|¿Qué está haciendo el hombre de blanco?|Está subiendo por una escalera alta.
457|cerrar los ojos;llevar un top verde;estar tumbado detrás de las mujeres|una luz;un espejo;un perro;maquillaje|¿Dónde está tumbado el perro?|El perro está tumbado detrás de las mujeres.
36|abrazar con mimo a su gato naranja;colgar en el aire;coger en brazos a su mascota|una maceta;un gato;un cojín;un cárdigan|¿Qué está haciendo la mujer?|Está abrazando con mimo al gato que adora.
676|fotografiar los lugares de interés;dirigir la góndola;alzarse sobre la plaza|un campanario;una cúpula;una cámara;una góndola|¿Qué están haciendo los dos turistas?|Están haciendo turismo en una góndola.
7962|sostener la caja de cartón;contener la pizza sobrante;colgar sobre la azotea|guirnaldas de luces;una chimenea;una caja de pizza;una alfombra|¿Qué contiene la caja de pizza?|Contiene el resto de la pizza.
7858|mantener el equilibrio sobre una slackline;hacerse sombra en los ojos;saludar con la mano desde el acantilado|el cielo;un acantilado;un río;un forro polar|¿Dónde está manteniendo el equilibrio la mujer de naranja?|Está manteniendo el equilibrio a mitad de camino sobre el desfiladero.
7124|bajar los escalones de piedra;vitorear desde el balcón;reposar sobre una bandeja|invitados;una tarta de boda;un esmoquin;una escalera|¿Qué está bajando el joven?|Está bajando un tramo de escalones de piedra.
6849|bajar los escalones de piedra;agarrar con fuerza una cesta de pan;agarrarse a una bicicleta|un automóvil;una cesta;ropa tendida;adoquines|¿Qué está haciendo el automóvil rojo?|El automóvil está bajando los escalones de piedra.
4206|bostezar en el escritorio;servir café recién hecho;brillar con un verde intenso|una tarjeta de identificación;un reloj;una silla de oficina;papeleo|¿Qué cuelga del cuello del hámster?|Una tarjeta de identificación cuelga de su cuello.
234|disolverse en el agua;remover con una cuchara;dejar caer un terrón de azúcar|una cuchara;un delantal;un vaso;un terrón de azúcar|¿Qué le está pasando al terrón de azúcar?|El terrón de azúcar se está disolviendo en el agua.
5273|recorrer la pasarela a grandes pasos;ajustarse las gafas de sol;lucir su chaqueta|un modelo;espectadores;una pasarela;el techo|¿Qué está haciendo el modelo?|Está recorriendo la pasarela a grandes pasos.
7835|derramarse por la ladera;brillar en la cima;cernerse sobre el horizonte|una colada de lava;un cráter;árboles;una nube|¿Qué está pasando en el volcán?|Una colada de lava se está derramando por la ladera.
8032|tender su sombrero;saltar hacia atrás del susto;agarrar el brazo de su amiga|una torre del reloj;una fuente;palomas;una falda|¿Qué está haciendo el hombre de bronce?|Le está ofreciendo su sombrero a una mujer.
278|elevarse por encima de las copas de los árboles;llevar una trenza larga;llevar unas mallas de color verde oscuro|el sol;una palmera;una trenza;un césped|¿Qué ejercicio está haciendo el grupo?|Están haciendo sentadillas en el césped.
93|hacer girar la fruta;lamerse el dedo;levantar el pulgar|una licuadora;una jarra;fresas;una cinta para la cabeza|¿Qué está preparando el hombre?|Está preparando un batido en una licuadora.
7239|tomar a sorbos una bebida espumosa;llevar una chaqueta impermeable;apretarse contra su cabeza|un cepillo;un perro;un vaso de papel;un parabrisas|¿Qué está haciendo el hombre?|Está tomando a sorbos una bebida espumosa.
5712|señalar las pruebas;dejar caer una hoja suelta;reposar sobre un soporte|un abogado;una bicicleta;barro;cajas de cartón|¿Qué está haciendo el abogado?|Está señalando la bicicleta embarrada.
406|blandir un martillo pesado;fijar una espiral de hierro;tener púas afiladas|un yunque;una barra de hierro;gafas protectoras;una ventana|¿Qué está haciendo el herrero?|Está martillando hierro caliente sobre un yunque.
378|posarse en una barandilla;planear sobre los tejados;proyectar largos rayos dorados|un pájaro;el cielo;tejados|¿Qué está haciendo el pájaro?|Está planeando sobre los tejados al amanecer.
6|frotarse la espalda dolorida;levantar el pulgar;amontonarse hasta muy arriba|una barba;un cárdigan;una maceta;un cojín|¿Qué está haciendo el hombre?|Está amontonando cojines sobre su regazo.
7946|vaciar el buzón;llevar una saca de correo;asomar la cabeza|árboles;un buzón;una furgoneta;una saca|¿Qué está haciendo el perro negro?|Está vaciando el buzón rojo.
7932|colgar del aro;llevar una equipación azul marino;vitorear con los brazos en alto|un balón de baloncesto;una red;una camiseta sin mangas|¿Qué está haciendo el hombre de blanco?|Está colgando del aro.
7996|destacar claramente;girar con la brisa;estar apoyada en la barandilla|árboles;un molino de viento;una bicicleta;tulipanes|¿Qué tulipán destaca en el campo?|El tulipán rojo destaca en el campo.
4209|escribir en un portátil;estar tumbado profundamente dormido;echar un vistazo a la cámara|un tulipán;un portátil;una mascarilla facial;un bolso|¿Qué está haciendo el hámster de la mascarilla?|Está durmiendo un poco con una mascarilla facial.
7844|girarse hacia los fogones;llevar una camisa con cuello;colgar encima de la ventana|sartenes de cobre;un bol para mezclar;tortitas;una encimera|¿Quién está volteando tortitas?|Dos generaciones de mujeres están volteando tortitas.
4156|estar de pie sobre su pecho;lanzarse tras el robot;extender ambas manos|un seto;una valla;un robot;un césped|¿Qué está haciendo el robot al principio?|Se está acercando a la cámara por el camino.
8036|apretarse contra la pared;llenar toda la habitación;colgar de una maceta|una claraboya;una pantalla de lámpara;un flamenco;tablas del suelo|¿Qué está haciendo el flamenco?|Está llenando todo el volumen de la habitación.
515|escalar un muro de escalada;colgar de una cuerda;vitorear desde abajo|una ventana;un muro de escalada;una escaladora;espectadores|¿Qué está haciendo la mujer?|Está escalando un muro de escalada.
673|cargar la lavadora;mirar fijamente con incredulidad;encoger en el lavado|pecas;un suéter;un peto;una lavadora|¿Qué le pasó al suéter?|El suéter encogió en la lavadora.
5458|beberse la bebida de un trago;burbujear y volverse naranja;tener una etiqueta de vitaminas|un armario;una pastilla de vitaminas;un frutero;un vaso|¿Qué está dejando caer ella en el vaso?|Está dejando caer una pastilla de vitaminas.
343|agarrar un aro de buceo;yacer en el fondo;caminar por aguas poco profundas|escalones;un aro de buceo;unas gafas de buceo;un bañador|¿Qué está agarrando la mujer bajo el agua?|Está agarrando un aro de buceo.
5594|posarse en una cresta;plegar sus alas coriáceas;bajar su cabeza con cuernos|picos;nubes;un dragón;pinos|¿Qué está haciendo el dragón?|El impresionante dragón está posado en una cresta.
94|derramar una lágrima;apretar los dientes;sonreír de oreja a oreja en señal de triunfo|gafas de sol;un pendiente de aro;batidos;llaves del coche|¿Qué está intentando evitar el hombre?|Está intentando evitar parpadear.
7981|morder una fresa;llevar las mangas remangadas;ofrecer una fresa|un toldo;una copa de helado;una jarra|¿Qué están haciendo los tres amigos?|Están compartiendo una copa de helado.
7145|retirarse detrás de la puerta;resoplarle al hombre;pasear junto a unas botellas de leche|una puerta principal;un albornoz;botellas de leche;adoquines|¿Qué está haciendo el hombre?|Se está retirando detrás de su puerta principal.
70|recortar una barba espesa;admirar su nuevo corte de pelo;reflejar su cara de alegría|un barbero;un cliente;un espejo de mano;botellas|¿Qué está haciendo el barbero?|Está recortando la barba espesa del cliente.
747|agarrarse la cabeza;alzarse sobre el escritorio;mostrar la hora|una taza;un portapapeles;papeleo;un reloj|¿Qué está haciendo la mujer?|Se está agarrando la cabeza en su escritorio.
7870|relamerse;colgar del tenedor;brillar en el árbol|un perro;espaguetis;una pulsera;un muro de piedra|¿Qué está haciendo el perro?|Está mirando fijamente los espaguetis que cuelgan.
7016|dar palmaditas en el lomo de una vaca;pasear a lo largo de la valla;caminar en fila india|un portón;un granero;lecheras;vacas|¿Qué está haciendo la mujer?|Le está dando palmaditas en el lomo a una vaca lechera.
8001|extender sus alas;pasar en bicicleta junto al ganso;saltar a la hierba|un ganso;una bicicleta;hiedra;un camino de grava|¿Qué está haciendo la mujer de pantalón corto?|Se está manteniendo alejada del ganso.
7744|estrellarse contra el agua;agarrar con fuerza un remo;soltar un grito ahogado del susto|una ballena;un cobertizo para botes;un remo;un chaleco salvavidas|¿Qué está haciendo la ballena?|Se está estrellando contra el agua.
6820|acariciar el lomo de la cría;trotar junto al adulto;levantar su trompa corta|un adulto;una acacia;colmillos;una cría|¿Qué está haciendo el elefante adulto?|Está acariciando el lomo de la cría.
4222|saludar con la mano a la cámara;cruzarse de brazos;inclinarse hacia el objetivo|ojos;una lengua;una barriga;una cola|¿Qué está haciendo el geco?|Está saludando con la mano a la cámara.
7845|levantar la cesta con suavidad;agarrar con fuerza la cesta de mimbre;correr a toda velocidad por la hierba|un globo aerostático;una cesta de mimbre;un perro;hierba|¿Qué está haciendo la mujer de azul?|Está viajando en una cesta de mimbre.
7563|conducir una moto;ir sentado en el sidecar;vitorear junto a la verja|una casita de campo;una verja;un saco de dormir;grava|¿Qué está haciendo el motorista?|Se está poniendo en marcha en una moto.
5053|sujetar una etiqueta de equipaje;colgar de una maleta;transportar el equipaje|gafas;un pañuelo para la cabeza;una etiqueta;una maleta|¿Qué está haciendo la mujer?|Está sujetando una etiqueta a su maleta.
8000|apoyarse en el mostrador;sonreír de oreja a oreja al perro;arrastrar una maleta pesada|una lámpara de araña;una columna;una maleta;un mostrador de recepción|¿Qué está haciendo el perro?|El perro se está apoyando en el mostrador de mármol.
98|soltar un grito ahogado de asombro;cerrar los ojos con fuerza;tener una cubierta burdeos|una hamaca;una cúpula;una trenza;flores|¿Qué está haciendo la mujer?|Está leyendo un libro en una hamaca.
5272|señalar a su compañero;tener una barba poblada;llevar un sombrero de ala ancha|un excursionista;una mochila;un cañón;una barandilla|¿Qué están haciendo los excursionistas?|Los excursionistas están vitoreando sobre el cañón.
4424|cruzar una franja pintada;sonreír de oreja a oreja a la cámara;meter la mano por una ventanilla|un pasaporte;una cabina;una barandilla;un gorro|¿Qué está haciendo el viajero?|Está cruzando la frontera a pie.
4408|beberse un batido de un trago;levantar el pulgar;estar repleta de fruta|una licuadora;espinacas;un batido;un bigote|¿Qué está haciendo el hombre?|Está probando un batido de fruta fresca.
5636|inclinarse sobre el mostrador;echarse a reír;sostener un cucurucho de barquillo|una lámpara de araña;una vitrina;un delantal;helado|¿Qué está haciendo la clienta?|Se está inclinando sobre el mostrador de helados.
8028|señalar la pila;taparse la cara;alzarse sobre el mostrador|un farolillo;una cinta para la cabeza;platos;palillos|¿Qué está haciendo el chef?|Está señalando la pila de platos.
637|abrirse como una flor;yacer en un montón;extenderse sobre colinas verdes|el cielo;un cuchillo;un pulgar;una granada|¿Qué le está pasando a la granada?|Se está abriendo como una flor.
7739|hacer rodar una rueda de queso;dar golpecitos con un martillo;subir por la escalera|un farol;una ventana;una escalera;un cubo|¿Qué está haciendo rodar el ratón?|Está haciendo rodar una pesada rueda de queso.
7813|tamborilear sobre cubos puestos boca abajo;llevar un jersey rosa;reflejar el cielo nublado|paraguas;una fuente;cubos;un charco|¿Qué está haciendo el dúo?|El dúo está tamborileando sobre cubos azules.
7997|protagonizar un espectáculo;estar arrodillado sobre una rodilla;bailar con tacones altos|cortinas;un foco;un vestido de gala;candilejas|¿Qué está haciendo la mujer de dorado?|Está protagonizando un espectáculo.
7748|pintar una escultura de dragón;bostezar sobre su café;dormitar sobre un cojín azul|un dragón;latas de pintura;una caja de pizza;una manta|¿Qué está haciendo la mujer del peto?|Está pintando una escultura de dragón.
7450|dar forma a un jarrón alto;meter la mano dentro del jarrón;trabajar al fondo|un horno de cerámica;una alfarera;un jarrón;una esponja|¿Qué está haciendo la alfarera de delante?|Está dando forma a un jarrón alto de arcilla.
7040|rodar por el tablero;agarrarse la cabeza;lanzar un dado|un dado;palomitas;un juego de mesa;collares|¿Qué está rodando por el tablero?|Un dado blanco está rodando por el tablero.
5517|aceptar una propuesta de matrimonio;arrodillarse sobre una manta;llevar una caña de pescar|un estuche de anillo;una cesta de pícnic;una manta;huellas|¿Qué está haciendo la mujer?|Está aceptando su propuesta de matrimonio.
4125|tirar de una sábana;estallar en pétalos;levantar la trompa|un foco;un elefante;un traje;un escenario|¿Qué está haciendo el elefante gris?|Está levantando la trompa en el escenario.
347|susurrar un cotilleo;soltar un grito ahogado tras las manos;llevar una camisa de rayas|un toldo;pelo rizado;una trenza;una mesa|¿Qué está haciendo la mujer de gafas?|Le está susurrando un cotilleo al oído a él.
7849|colgar sobre la azotea;alzarse en el horizonte;reposar sobre una tabla|guirnaldas de luces;una montaña;una pizza;una jarra|¿Qué están haciendo los amigos?|Están compartiendo una pizza en una azotea.
4920|regar los plantones;tener rayas de colores;alzarse sobre la multitud|el cielo;un cartel;un niño;un bancal elevado|¿Qué está haciendo la mujer rubia?|Está regando los plantones en el huerto comunitario.
4434|abrazar con mimo un oso de peluche;lamer un helado;quitarse la chaqueta|el cielo;una feria;un cucurucho de helado;un oso de peluche|¿Qué está haciendo ella en la feria?|Está abrazando con mimo un oso de peluche gigante.
7154|mantener el equilibrio sobre un monociclo;tomar a sorbos un café para llevar;pedalear detrás del monociclo|un autobús de dos pisos;un taxi;un maletín;un monociclo|¿Cómo se está desplazando el hombre de negocios?|Está montando en monociclo entre el tráfico.
5417|subir a un tranvía antiguo;recoger a una pasajera;mirar a su alrededor en la cochera|cables aéreos;raíles;una bolsa de tela;una trenza|¿Qué está haciendo ella al final?|Está mirando a su alrededor en la cochera de tranvías.
4918|subir corriendo las escaleras;tener dificultades con unas bolsas pesadas;levantar el pulgar|escaleras;una sudadera con capucha;vaqueros;una bolsa de papel|¿Qué está llevando el joven?|Está llevando bolsas de papel escaleras arriba.
7369|remar alrededor de una ballena;lanzar un chorro de vapor;levantar la cola|una tabla de paddle surf;una ballena;un barco;montañas|¿Qué está haciendo la mujer?|Se está moviendo alrededor de la gran ballena.
5502|apilar cajas de cartón;llevar un palé cargado;envolver cajas con film plástico|cajas de cartón;una transpaleta;un chaleco reflectante;estanterías|¿Qué está haciendo la mujer?|Está apilando cajas de cartón sobre un palé.
730|limpiar el mostrador de la cocina;extender un mantel;servir un capuchino|personal;clientes;un mantel;lámparas colgantes|¿Qué está haciendo la camarera?|Está extendiendo un mantel blanco.
230|levantar los puños triunfalmente;llevar un disfraz de pirata;estar sobre un trípode|una directora;una cámara de cine;una silla plegable;el sol|¿Qué está haciendo la directora?|Está levantando los puños en señal de triunfo.
7119|izar una red pesada;llevar ropa impermeable amarilla;rebosar de peces plateados|una gaviota;una red;una caja;una pescadora|¿Qué está haciendo la pescadora de naranja?|Está izando una red pesada.
4930|levantar la mano con entusiasmo;enseñar con orgullo su cuaderno;brillar en la página|una estrella dorada;un cuaderno de espiral;una pizarra blanca|¿Qué recompensa está recibiendo la niña?|Está recibiendo una estrella dorada.
5358|mirar a escondidas por un hueco;apilar libros pesados;apoyarse en su mano|estanterías de libros;gafas;un cárdigan;un libro de texto|¿Qué está haciendo la mujer escondida?|Está mirando a escondidas por un hueco entre los libros.
7|levantar su diploma;sonreír de oreja a oreja a la cámara;abrazar a otro graduado|un diploma;un estadio;un birrete;una banda|¿Qué está haciendo el hombre?|Está levantando su diploma en su graduación.
4360|mirar dentro de una bolsa;llevar varias bolsas de la compra;enseñar con orgullo su bolso|bolsas de papel;un bolso;una bolsa de viaje;una escalera mecánica|¿Qué está enseñando con orgullo la mujer?|Está enseñando con orgullo su bolso en una escalera mecánica.
5379|tomar las medidas de un cliente;marcar la tela con tiza;ponerse una chaqueta|un ventilador de techo;tela;una chaqueta;una cinta métrica|¿Qué está haciendo el sastre?|Está arreglando una chaqueta para un cliente.
798|cerrar la cremallera de una chaqueta;regar las plantas en maceta;tener un bigote espeso|ropa tendida;un escúter;un chándal;una regadera|¿Qué está haciendo la mujer joven?|Está bailando con un chándal turquesa.
7200|dirigir un parapente;elevar al piloto;ondear con la brisa|un parapente;una manga de viento;un golfo;un saliente rocoso|¿Qué está haciendo el piloto?|Está planeando sobre un golfo turquesa.
376|correr con fuerza por el desfiladero;hacer espuma sobre las rocas;alzarse a lo lejos|un bosque;un acantilado;rápidos|¿Qué está haciendo el río?|Está corriendo con fuerza por la naturaleza salvaje.
5538|remolcar un remolque cargado;erguirse en el horizonte;brillar en naranja y rosa|silos;una cosechadora;un tractor;trigo|¿Qué están haciendo las máquinas?|Están cosechando trigo al atardecer.
5117|hojear un libro de tapa dura;soltar un grito ahogado de asombro;estar abarrotadas de libros|gafas;estanterías de libros;una chaqueta vaquera;un libro de tapa dura|¿Qué está haciendo el joven?|Está hojeando un libro de tapa dura en una librería.
6836|izar un sofá;colgar de una cuerda;levantar un puño cerrado|un edificio de apartamentos;una barbacoa;un sofá;una furgoneta|¿Qué está haciendo la mujer joven?|Está izando un sofá hasta su balcón.
5540|escalar el muro de escalada;agacharse sobre la colchoneta;agarrar una presa grande|trenzas;una coleta;una colchoneta;una bolsa de magnesio|¿Qué está haciendo la mujer de las trenzas?|Está escalando un muro de escalada empinado.
5671|agitar el puño en el aire;pedalear cuesta arriba;correr junto a una ciclista|picos nevados;un casco;un muro de piedra;hojas caídas|¿Qué está haciendo el hombre?|Le está dando ánimos a la ciclista.
124|morder el pan;llevar un delantal de rayas;derretirse sobre el pan|mantequilla;un cuchillo;un delantal;sartenes|¿Qué está haciendo la niña?|Está untando mantequilla en el pan.
4364|soltar un grito ahogado al ver los cruasanes;llevar un delantal de flores;brillar por el calor|masa;harina;un delantal;una ventana|¿Qué están haciendo las dos mujeres?|Están dando forma a bolas de masa.
7453|saltear los fideos;tender un plato;arder debajo del wok|un wok;llamas;un cucharón;una bandana|¿Qué está haciendo la cocinera?|Está preparando fideos en un wok.
7883|arrodillarse en el camino;lamer la mejilla de la mujer;sujetar la correa del cachorro|un cachorro;una bicicleta;un banco;una farola|¿Qué está haciendo la mujer arrodillada?|Está abrazando al cachorro con alegría.
"""
out = {}
for line in DATA.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/es.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
