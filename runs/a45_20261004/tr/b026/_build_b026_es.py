import json, os
H=os.path.dirname(os.path.abspath(__file__))
R='''7070|beber a sorbos su whisky;frotarse los ojos cansados;observarlo con preocupación|una camarera;vasos de chupito;cacahuetes;un borracho|¿Qué está haciendo el hombre?|Está bebiendo a sorbos su whisky.
7072|atrapar una caja que rueda;olfatear la sombrerera;observar desde la escalinata|una mansión;un conde;lebreles irlandeses;una sombrerera|¿Qué está haciendo el joven?|Está atrapando una sombrerera que rueda.
7073|sujetar una vidriera;arrodillarse sobre una manta acolchada;agarrar el andamio de arriba|una vidriera;una manta;cuerda;un nivel de burbuja|¿Qué está haciendo la mujer?|Está sujetando una vidriera.
7074|llevar una paella humeante;ajustarse el sombrero de paja;descansar debajo de la mesa|un sombrero de paja;paella;una hogaza;un perro|¿Qué está haciendo la mujer?|Está llevando una paella humeante.
7075|apuntar notas;tender una cebolla;cruzarse de brazos|una balanza colgante;una pizarra;un portapapeles;cebollas|¿Qué está haciendo la joven?|Está apuntando notas en un portapapeles.
7076|caminar por el borde;extender los brazos;doblarse de risa|una tienda de lona;flamencos;grava;un borde|¿Qué está haciendo la mujer?|Está caminando por el borde.
7077|señalar el salpicadero;levantar la mano en señal de protesta;llenar los portavasos|un retrovisor;un ambientador;un volante;cafés con hielo|¿Qué está haciendo la conductora?|Está señalando el salpicadero.
7079|examinar el vidrio ámbar;dejar el vidrio;colocar pequeños trozos de vidrio|un panel de vidriera;una lata de clavos;una bobina;un soldador|¿Qué está haciendo el hombre?|Está examinando un trozo de vidrio ámbar.
7080|llevar una planta grande;salir del ascensor;levantar su bolsa|una planta;un ascensor;un perro;escaleras|¿Qué está llevando la joven?|Está llevando una planta grande.
7081|correr junto a la camilla;ponerse los guantes;apretar una bolsa de reanimación|una camilla;una enfermera;un médico;una silla de ruedas|¿Qué está haciendo la enfermera?|Está corriendo junto a la camilla.
7082|apoyarse en la cancela;acariciar la cabeza de una oveja;observar el rebaño que pasa|un sombrero de paja;una cancela;ovejas;un perro|¿En qué se está apoyando la mujer?|Se está apoyando en una cancela de madera.
7083|ahogar un grito de incredulidad;sujetar una correa extensible;darse golpecitos en la frente|una bufanda;un bajante;tulipanes;corgis|¿Qué está haciendo el hombre?|Se está dando golpecitos en la frente.
7085|subir la persiana metálica;hacer cola bajo la lluvia;desprender vapor|una persiana metálica;una emprendedora;una escalera de mano;un taburete de bar|¿Qué está haciendo la mujer?|Está subiendo la persiana metálica.
7086|bajar la cuajada a la cuba;gotear suero;sostener una cuchara medidora|moldes de queso;un bloque de cuajada;una cuba de cobre;un paño de quesería|¿Qué está goteando de la cuajada?|De la cuajada está goteando suero.
7087|llevar un fajo de cartas;trotar detrás de los gansos;estar subido al muro de piedra|un quad;un gato;un collie;un ganso|¿Qué están haciendo los gansos?|Los gansos están escoltando a la mujer.
7089|empujar una esponja gigante;alzarse por encima de la mujer;grabar con su móvil|un toldo;una caja de madera;un barril;adoquines|¿Qué está haciendo la esponja con forma de elefante?|La esponja con forma de elefante se está expandiendo.
7090|abrir los brazos de par en par;estar descalza sobre una roca;protegerse los ojos|una cascada;un bañador;musgo;una roca|¿Qué está haciendo la mujer?|Está abriendo los brazos de par en par.
7091|liderar la carrera;ir detrás de la líder;extender el brazo|álamos;un casco;espectadores;balas de heno|¿Qué está haciendo la ciclista que va delante?|Está liderando la carrera.
7092|sostener un paño negro;sonreír ampliamente a la estatua;derretirse bajo el sol abrasador|una estatua de hielo;una gorra plana;un chaleco;un turista|¿Qué está haciendo el joven?|Está sonriendo ampliamente a la estatua que se derrite.
7093|bajar la mirada;cerrar los ojos;sostener un paraguas en alto|una lona;una extra;un paraguas;adoquines|¿Qué está haciendo la mujer de delante?|Está de pie en una fila de extras.
7094|liberar la bota de un tirón;caer en un charco de barro;llevar un chaleco reflectante|un auxiliar de seguridad;una tienda de campaña;un charco;un sombrero de pescador|¿Qué está haciendo la mujer?|Está sacando la bota del barro de un tirón.
7095|escaparse patinando con el disco;llevar una camiseta roja;sentarse entre los espectadores|un farol;un perro;un tambor;un montón de nieve|¿Qué está haciendo la jugadora de azul?|Se está escapando patinando con el disco.
7096|taparse la cara;estar al volante;sostener una hoja de papel|casas;una fuente;una hoja de papel;un coche|¿Qué está haciendo la mujer?|Se está tapando la cara.
7097|frotar la mejilla del busto;fruncir el ceño con duda;escribir en un portapapeles|una bata de laboratorio;un busto;un frasco;bastoncillos de algodón|¿Qué está haciendo la mujer de delante?|Está frotando el busto con un bastoncillo de algodón.
7099|tocar un piano de cola;precipitarse a un profundo desfiladero;llevar un poncho de lluvia azul|las cataratas;un arcoíris;una barandilla;un piano de cola|¿Qué está haciendo el joven?|Está tocando un piano de cola.
7100|improvisar una vela;contemplar la foca;asomar la cabeza|una vela;un iceberg;una foca;un kayak de mar|¿Qué está haciendo la mujer?|Está improvisando una vela.
7101|darle la comida;levantar la bolsa bien alto;reír de alegría|comida rápida;un casco;un perro;un scooter|¿Qué está sosteniendo la mujer?|Está sosteniendo una bolsa de comida rápida.
7102|chisporrotear en grasa caliente;gotear sobre el fogón;reposar sobre una tabla de cortar|grasa;una sartén de hierro fundido;cucharas de madera;una cuchilla de carnicero|¿Qué está goteando sobre el fogón?|Está goteando grasa derretida sobre el fogón.
7103|sostener un pastel;estar de pie sobre las patas traseras;llevar una camisa rosa|una lámpara;un pastel;una mesa;un perro|¿Qué está haciendo el perro grande?|Está de pie sobre las patas traseras.
7104|montar un caballo gris;hacer una pompa;llevar el caballo gris de las riendas|el cielo;árboles;una multitud;un caballo|¿Qué está haciendo el hombre de verde?|Está montando un caballo gris.
7105|levantar la barbilla;aplicar pan de oro;soplar escamas al aire|un vestido de gala;un perchero;un secador de pelo;una brocha de maquillaje|¿Qué está haciendo la modelo?|Está levantando la barbilla.
7106|agarrarse a la barandilla;abrir mucho la boca;tocarse el pecho|el cielo;el mar;un hombre;una cuerda|¿Qué está haciendo el hombre?|Se está agarrando a la barandilla.
7107|atrapar copos de nieve que caen;echar la cabeza hacia atrás;cerrar los ojos con fuerza|una ladera;rocas volcánicas;una fuente termal;un bañador|¿Qué está haciendo la mujer?|Está atrapando con las manos copos de nieve que caen.
7108|estar subida a hombros de alguien;aguantar el peso de su amiga;emocionarse hasta las lágrimas|edificios;un pañuelo;una chaqueta vaquera;un cartel de cartón|¿Qué está haciendo la mujer de arriba?|Está subida a hombros de su amiga.
7110|quitarse de encima a las mujeres;estar de rodillas en la cama;sentarse tranquilamente en el suelo|un cabecero;una lámpara de mesita;guirnaldas de luces;un perro|¿Qué está haciendo el hombre?|Se está quitando de encima a las mujeres con una almohada.
7111|lanzar un puñetazo;llevar pantalones cortos rojos;dar vueltas por el ring|una luchadora;un árbitro;gente;una lámpara|¿Qué está haciendo el árbitro?|Está dando vueltas por el ring.
7112|pintar una figura diminuta;dormitar en un taburete;dar una luz cálida|una figura;una lámpara de escritorio;una campana de cristal;un gato|¿Qué está haciendo el joven?|Está pintando una figura diminuta.
7113|rellenar un formulario;llevar una chaqueta amarilla;marcar la hora|un reloj;una chaqueta;un formulario;una máquina|¿Qué está haciendo la mujer de amarillo?|Está rellenando un formulario.
7114|levantar un marco metálico;brillar con los colores del arcoíris;medir la velocidad del viento|rascacielos;un depósito de agua;una película de jabón;una cubeta|¿Qué está haciendo la mujer de amarillo?|Está levantando un gran marco metálico.
7116|deslizarse por una barra de latón;salir del parque de bomberos;colgar en el campanario|un parque de bomberos;una campana;el cielo;nieve|¿Qué está haciendo el camión de bomberos?|Está saliendo del parque de bomberos.
7117|alejarse remando de la puerta;llevar un impermeable amarillo;asomarse a las ventanas|un bote de remos;agua de la inundación;un sofá;el cielo|¿Qué está haciendo la mujer de amarillo?|Se está alejando remando de la puerta.
7118|levantar el violonchelo por encima de la cabeza;hacer una profunda reverencia sobre el violonchelo;aplaudir desde el podio|un violonchelo;un director de orquesta;un estuche de violonchelo;un arco|¿Qué está haciendo el director de orquesta?|Está aplaudiendo desde el podio.
7120|estar de pie en el techo;estar tumbado en una tabla roja;sostener un paraguas|un autobús;un paraguas;herramientas;la carretera|¿Qué están haciendo los perros?|Los perros están arreglando un autobús viejo.
7121|emitir un potente haz de luz;romper contra las rocas;estar enrollada en el muelle|un faro;un acantilado;rocas;una cuerda|¿Qué está haciendo el faro?|El faro está destellando en la tormenta.
7122|correr por el agua;volar sobre el agua;cubrir el cielo|el cielo;caballos;agua;hierba|¿Qué están haciendo los caballos?|Están corriendo por el agua.
7123|abrir un salmón entero;alisar la carne;apoyarse en el mostrador|un cuchillo;un guante de goma;carne;una cabeza de pescado|¿Qué está haciendo la mujer?|Está alisando la carne de color naranja intenso.
7125|atrapar una moneda en el aire;apoyarse en el piano;saludar con la mano desde un portal|una moneda;un balcón;un piano;correas|¿Qué está haciendo la joven?|Está lanzando una moneda al aire.
7127|coger una bolsa de pan;estirarse hacia la ventana;mirar el pan|un balón;manzanas;una barca;un perro|¿Qué hay en la calle?|Hay una inundación en la calle.
7129|estar de pie junto al piano;colgar en el aire;planchar ropa|el cielo;un piano;un edificio|¿Dónde está el piano?|El piano está colgando en el aire.
7131|estar de pie en una piscina;sostener en alto una tarta grande;llevar un vestido blanco|una piscina;un flamenco;una tarta;una novia|¿Qué está haciendo el hombre de las gafas de sol?|Está de pie en una piscina.
7132|presumir de su grabación;cernerse sobre los campos;señalar la pantalla de la cámara|un tornado;una camioneta;grabación;un impermeable|¿Qué está enseñando la mujer de amarillo?|Está enseñando la grabación del tornado.
7134|atrapar el balón;correr con el balón;llevar una chaqueta azul|el cielo;un balón;un futbolista;hierba|¿Qué está haciendo el jugador de blanco?|Está atrapando el balón con las dos manos.
7135|agarrar una palanca roja;grabar con una tableta;estrellarse contra las sandías|una grúa;una bola de demolición;una tableta;sandías|¿Qué está haciendo el hombre de pelo rizado?|Está agarrando una palanca roja.
7136|abrirse paso por el río;cruzar vadeando de la mano;elevarse hacia el cielo|un glaciar;una tienda de campaña;excursionistas;un todoterreno|¿Qué están haciendo los excursionistas?|Están vadeando el río de la mano.
7137|vadear un río poco profundo;esperar en las pasaderas;mirar desde la otra orilla|ovejas;un poste de madera;pasaderas;una bota de goma|¿Qué está haciendo el todoterreno?|Está vadeando un río poco profundo.
7138|romper sobre los gruesos muros;estar en formación;balancearse en el mar agitado|un rayo de sol;humo;soldados;un fuerte|¿Qué está haciendo la ola enorme?|Está rompiendo sobre los gruesos muros.
7139|abrir los brazos de par en par;sostener en alto un pez;volar sobre el barco|una red;el cielo;un barco;peces|¿Qué está haciendo la mujer?|Está de pie en medio de un montón de peces.
7140|dirigirse a la multitud;gesticular desde su silla;cruzarse de brazos|una farola;una maqueta;un cojín;documentos|¿Qué está haciendo la joven?|Se está dirigiendo a la multitud en la plaza.
7141|probarse unas gafas;reírse de sus gafas;trabajar en un escritorio|monturas;una ventana;un armario;un mostrador|¿Qué está haciendo la mujer?|Se está riendo de sus gafas.
7142|ajustar un marco ornamentado;aplaudir encantado;representar limones maduros|una ingletadora;un marco;un frasco;un banco de trabajo|¿Qué está haciendo el anciano?|Está aplaudiendo encantado.
7143|sonreír de emoción;entrar deprisa en la habitación;empujar un minifrigorífico con ruedas|una estudiante de primer año;una caja de cartón;un colchón;un frigorífico|¿Qué está llevando la estudiante de primer año?|Está llevando una caja de cartón.
7144|vaciar una cesta de freír;servir las patatas fritas;alargar la mano hacia las patatas fritas|bombillas;una bandana;patatas fritas;una freidora|¿Qué está haciendo el cocinero?|Le está sirviendo las patatas fritas a un cliente.
7146|sujetar un cabo de amarre;deambular por el muelle;mecerse sobre las olas|un buque de carga;un ancla;un barco de pesca;un pastor alemán|¿Qué está sujetando el trabajador?|Está sujetando un cabo de amarre.
7147|agacharse junto a la hoguera;atrapar una sartén en el aire;pasear por la arena|una sartén;una tortita;un bol;una hoguera|¿Qué está atrapando el hombre?|Está atrapando una sartén en el aire.
7148|patinar sobre ruedas por el porche;abrir los brazos de par en par;estar tumbado en las tablas del suelo|un ventilador de techo;un helecho;un perro;una galería|¿Qué está haciendo la mujer?|Está patinando sobre ruedas por el porche.
7149|repostar un coche lleno de barro;quitarse el casco;estar cubierto de barro|una gasolinera;una tormenta de polvo;un coche de rally;una planta rodadora|¿Qué está haciendo el empleado?|Está repostando un coche de rally lleno de barro.
7150|repostar un generador;asomarse por una ventana;brillar sobre el generador|un bidón;gasolina;un farol;un generador|¿Qué está echando el hombre?|Está echando gasolina en un embudo.
7153|agacharse en el escenario;manejar la máquina de niebla;expulsar una niebla espesa|una estructura de iluminación;una batería;una máquina de niebla;una bombona|¿Qué está haciendo la mujer?|Está agachada junto a una máquina de niebla.
7155|trepar por el muro;sujetar las sandalias con los dientes;mirar desde el césped|el cielo;hiedra;un vestido de satén;invitados|¿Qué está haciendo la mujer de plateado?|Está trepando por un muro cubierto de hiedra.
7156|tragarse un perrito caliente;echar agua de una jarra;inflar los mofletes|banderines;una parrilla;un bol de cristal;perritos calientes|¿Qué está haciendo la mujer en pantalones cortos?|Está echando agua de una jarra.
7157|ponerse una chaqueta;deslizarse por una barra;tener manchas negras|un camión de bomberos;una chaqueta;un perro;una barra|¿Qué está haciendo la mujer?|Se está vistiendo en un parque de bomberos.
7158|cantar una canción a pleno pulmón;dejarse caer en el sofá;taparse los oídos|un gorro de fiesta;un micrófono;una botella de cerveza;una pandereta|¿Qué está haciendo la cantante?|Está cantando a pleno pulmón una canción de karaoke.
7159|sostener un paraguas;abrir con llave la puerta de entrada;levantar la vista hacia la mujer|un paraguas;un perro;bolsas de la compra;una puerta|¿Qué está haciendo la mujer?|Está abriendo con llave la puerta de entrada.
7160|mirar un mapa;señalar calle abajo;estar sentado en el suelo|un sombrero;una puerta;una maleta;un gato|¿Qué está haciendo la turista?|Está mirando un mapa.
7161|levantar un cachorro en alto;estirarse por encima de la mesa;olfatear la tarta a medio comer|guirnaldas de luces;una cesta de mimbre;una tarta;huellas de patas|¿Qué está haciendo la mujer descalza?|Está sacando un cachorro de la cesta.
7162|abrazar un montón de lana;blandir una escoba;ir al trote hacia los corrales|lana;una escoba;una oveja;tablas del suelo|¿Qué está haciendo la mujer?|Está abrazando un montón de lana.
7163|estornudar en un pañuelo;subirse la bufanda;leer un libro|guantes;un libro;pan;una bolsa|¿Qué está haciendo la mujer de blanco?|Está estornudando en un pañuelo.
7164|tirar de un trineo;ir en el trineo;pasear con correa|una casa;árboles;un trineo;un guante|¿De qué está tirando la mujer?|Está tirando de un trineo con perros.
7166|pisar la cima;mantener el equilibrio sobre la arista;ajustarse las gafas de nieve|gafas de nieve;nubes;un piolet;una cuerda|¿Dónde está de pie la escaladora?|Está de pie en la cima nevada.
7167|arrastrar un flamenco hinchable;abrir los brazos de par en par;abrazar al perro empapado|un flamenco hinchable;un golden retriever;un jersey de punto;arena mojada|¿Qué está haciendo el perro?|El perro está arrastrando un flamenco hinchable.
7168|sujetar la puerta abierta;subir al asiento del copiloto;llevar los faros encendidos|la aguja de una iglesia;un coche antiguo;una cinta;pétalos|¿Qué está haciendo el hombre?|Le está sujetando la puerta.
7169|arrodillarse en la piscina;inclinarse sobre la piscina;sostener una linterna pequeña|guirnaldas de luces;una pelota de parto;un botiquín;una piscina de partos|¿Qué está haciendo la mujer embarazada?|Está arrodillada en una piscina de partos.
7170|planear sobre el valle;caminar en fila india;estar en la ladera|un arcoíris;una cañada;un arroyo;ganado|¿Qué está haciendo el ganado?|Está caminando en fila india.
7172|pegar una pieza diminuta;saltar de alegría;mirar con las manos juntas|una iglesia;una casita de campo;un tubo de pegamento|¿Qué está haciendo la mujer de amarillo?|Está pegando una pieza diminuta en una casita de campo.
7173|sostener una pistola de silicona;decorar un barco viejo;llevar una concha|un bote de remos;una pistola de silicona;una caja;una gaviota|¿Qué está haciendo la mujer?|Está pegando conchas en un barco viejo.
7174|llevar una mochila grande;abrazarse;estar sentado en el suelo|un barco;un pasaporte;una mochila;el suelo|¿Qué está haciendo la pareja?|Se están abrazando.
7175|meter la mano en el arroyo;agarrar una raíz cubierta de musgo;olfatear el agua|un farol;un desplantador;un arroyo;hojas caídas|¿Qué le está enseñando al perro grande?|Le está enseñando al perro grande un bulto oscuro.
7176|quitarse el sombrero;llevar un collar;sostener una gallina|una cabra;un sombrero;una cesta;una ventana|¿Qué está haciendo la joven?|Se está quitando el sombrero.
7177|descender en rápel por un acantilado;agarrar la cuerda;echarse hacia atrás en el arnés|un casco;una cascada;un acantilado;una poza|¿Qué está haciendo la mujer?|Está descendiendo en rápel por un acantilado.
7178|agarrar los papeles que caen;sostener un portapapeles;estar sentada en la recepción|un portapapeles;una americana;una corbata|¿Qué está sosteniendo la mujer de las gafas?|Está sosteniendo un portapapeles.
7182|llevar la comida caliente;estar sentado en una barca;juntar las manos|el cielo;casas;una mesa;agua|¿Qué está llevando el joven?|Está llevando la cena a la mesa.
7183|señalar un escaparate;llevar bolsas de la compra;montar en bici|un paraguas;un poni;una bici;un escaparate|¿Qué está haciendo la mujer de amarillo?|Está yendo de compras con un poni.
7184|llevar una camiseta verde;sentarse detrás del hombre;salir volando|una iglesia;una bici;una paloma;un helado|¿Qué están haciendo el hombre y la mujer?|Están haciendo turismo en bici.
7185|saltar a través del detector;escribir en un portapapeles;agarrar sus botines|un detector de metales;botines;una chaqueta vaquera;una piña|¿Qué está haciendo la mujer en calcetines?|Está saltando a través del detector de metales.
7186|subirse a la cama;iluminar la cama;taparse con la manta|el cielo;una lámpara;una cama;una manta|¿Qué está haciendo la mujer?|Se está acostando en los árboles.
7187|quedarse dormido;dejar caer un libro;estar tumbado en una hamaca|árboles;un hombre;un libro;una cuerda|¿Qué está haciendo el hombre?|Se está quedando dormido en una hamaca.
7188|deslizarse bajo el hielo;estirar un brazo hacia arriba;llevar un traje de neopreno negro|un iceberg;rayos de sol;burbujas;una buceadora|¿Qué está haciendo la buceadora?|Se está deslizando bajo el hielo.
7191|coger un café;entregar una taza;dar saltos de emoción|un toldo;una cafetera;nubes;un perro|¿Qué está haciendo la parapentista?|Está cogiendo un café en la caseta.
7192|ponerse de pie de un salto;sostener en alto un diploma;dar un puñetazo al aire|un diploma;globos;un graduado;un podio|¿Qué está haciendo el graduado?|Está sosteniendo un diploma por encima de la cabeza.
7194|sostener un grabado de una polilla;alisar la página;estar de pie en una escalera de mano|ilustraciones;una ventana;una escalera de mano;pinceles|¿Qué está haciendo la mujer de delante?|Está fijando con chinchetas un grabado de una polilla.'''
out={}
for line in R.strip().split('\n'):
    i,p,n,q,a=line.split('|')
    out[i]={'phrases':p.split(';'),'nouns':n.split(';'),'question':q,'answer':a}
src=json.load(open(f'{H}/source.json'))
out={k:out[k] for k in src}
json.dump(out,open(f'{H}/es.json','w'),ensure_ascii=False,indent=1)
