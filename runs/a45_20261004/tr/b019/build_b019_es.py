import json, os
H = os.path.dirname(os.path.abspath(__file__))
S = "|"
rows = r"""
5099|llevar una camisa de rayas;llevar una cámara;añadir su foto|una mujer;una foto;un mapa|¿Qué está haciendo la mujer rubia?|Está añadiendo su foto al mapa.
5100|colocar una bandera verde;llevar un jersey rojo;pegar una foto en Asia|guirnaldas de luces;un mapa;una camiseta;una cámara|¿Qué está haciendo el hombre de amarillo?|Está pegando una foto en Asia.
5101|agarrarse a la barandilla;marearse;dejarse caer en un banco|pasajeros;el mar;un banco;una trenza|¿Qué está haciendo la mujer?|Se está tapando la boca con las manos.
5102|apretujarse para pasar junto a un hombre;dar un puñetazo al aire;llevar gafas de sol oscuras|un farol;un toldo;una mochila;un callejón|¿Qué está haciendo la mujer?|Se está apretujando para pasar junto a un hombre en el callejón.
5103|tocarse el cuello;atarse un pañuelo;doblar su largo cuello|un cuello;árboles;un pañuelo;una valla|¿Qué está haciendo la jirafa?|Está doblando su largo cuello.
5106|recorrer un canal en bicicleta;darle un mordisco a un gofre;girar sus aspas|el cielo;un molino de viento;un impermeable;tulipanes|¿Qué está comiendo la mujer?|Está comiendo un gofre de caramelo pegajoso.
5107|acunar a un recién nacido;contemplar a su bebé;dormir uno al lado del otro|pelo rizado;un recién nacido;un anillo de boda|¿Qué están haciendo el hombre y la mujer?|Están acunando a un bebé recién nacido.
5109|llevar una bandeja;llamar a la puerta;tomar una magdalena|una puerta;una planta;magdalenas;una mesa|¿Qué está llevando la mujer?|Está llevando una bandeja de magdalenas.
5113|señalar el cartel;levantar el pulgar;tocarle el hombro|un cartel;tomates;leche;un pescado|¿Qué está señalando la mujer?|Está señalando el cartel.
5114|mirar por un telescopio;apuntar notas;alzar el vuelo|el cielo;flamencos;un lago;juncos|¿Qué están haciendo los flamencos?|Están alzando el vuelo sobre el lago.
5115|estudiar un insecto;usar una lupa;dibujar en un cuaderno|una gorra;flores;una lupa;un tronco|¿Qué está haciendo la joven?|Está estudiando un pequeño insecto.
5116|abrir las cortinas;abrir las puertas del balcón;salir al balcón|el cielo;una cortina;un balcón;el suelo|¿Qué está abriendo el joven?|Está abriendo las puertas del balcón.
5118|abrir la ventana;sonreír a la cámara;estar de pie en el balcón|el cielo;luz del sol;tejados;un hombre|¿Dónde está de pie el hombre?|Está de pie en el balcón.
5119|sonreír a la cámara;agitar los brazos;abrirse lentamente|una entrada;un portón;gente;un vestido rojo|¿Qué está haciendo la mujer de rojo?|Está sonriendo a la cámara.
5120|inclinarse sobre el paciente;mostrar la frecuencia cardíaca;sostener una gasa|una lámpara quirúrgica;un cirujano;un paciente|¿Qué está haciendo el cirujano del centro?|Se está inclinando sobre el paciente.
5121|sacar una bandeja de magdalenas;sacar una fuente de horno;llevar panes recién horneados|panes;un horno;un panadero|¿Qué está sacando la mujer?|Está sacando una bandeja de magdalenas.
5122|escalar un muro;levantar pesas pesadas;cruzar la línea de meta|el cielo;árboles;un corredor;una pista|¿Qué está levantando el hombre?|Está levantando pesas pesadas.
5123|desbordarse de café;entrar corriendo en el baño;agarrarse la cabeza|una cortina de ducha;una sudadera con capucha;espuma;una bañera|¿Qué está haciendo el hombre?|Se está agarrando la cabeza con las dos manos.
5124|mirar al frente;aplaudir detrás de las vallas;llevar un chaleco amarillo|un balcón;espectadores;adoquines|¿Qué están haciendo los espectadores?|Están aplaudiendo detrás de las vallas.
5125|caerse de la silla;levantar un casco en alto;aplaudir|un casco;gente;un hombre;un colchón|¿Qué está sosteniendo la mujer?|Está sosteniendo un casco por encima de la cabeza.
5127|meter su ropa en la maleta;sentarse en la maleta;estar llena de ropa|pósteres;una puerta;ropa;una maleta|¿Qué está haciendo la mujer?|Está intentando cerrar la maleta.
5128|sujetarse la rodilla;apoyarse en la pared;sentarse en el suelo|una ventana;una planta;un armario;un sofá|¿Qué está haciendo el hombre?|Está sentado en el suelo.
5130|tocar el camión;mirar por la ventanilla;hacer volar una cometa roja|el cielo;una cometa;el sol;un hombre|¿Qué está haciendo el joven?|Está haciendo volar una cometa roja.
5132|derretirse en la sartén caliente;verter masa con un cucharón;levantar la sartén|un gorro;un cucharón;una sartén;masa|¿Qué está vertiendo el hombre?|Está vertiendo la masa de las tortitas en la sartén.
5133|grabarse riéndose;llevar una camiseta estampada;hacer un salto de tijera|un pino;una farola;un banco;césped|¿Qué está haciendo el hombre de blanco?|Se está riendo mirando a la cámara.
5134|dar de comer al bebé;leer un libro;comer de una cuchara|un hombre;una mujer;una torre;una alfombra|¿Qué está haciendo la madre?|Está dando de comer al bebé.
5135|asomarse por la ventanilla;meterse en un hueco estrecho;sostener en alto un periódico|un toldo;un periódico;una luz trasera;una tapa de alcantarilla|¿Qué está haciendo la mujer?|Está aparcando en un hueco estrecho.
5137|gesticular con ambas manos;estar de pie entre los miembros sentados;hablar desde el estrado|un balcón;escalones;un estrado|¿Qué está pasando en el estrado?|Un hombre está hablando desde el estrado.
5138|sentarse junto a la ventanilla;llevar un gorro naranja;ayudar con la maleta|un tren;un gorro;un billete;una maleta|¿Dónde está sentada la mujer?|Está sentada junto a la ventanilla.
5139|abrir su pasaporte;cerrar los ojos;sonreír a la cámara|luces;un pasaporte;una mochila;una mesa|¿Qué está sosteniendo el hombre?|Está sosteniendo un pasaporte.
5140|sellar un pasaporte;llevar una gorra de plato;presumir de su pasaporte|una gorra de plato;una cola;un sello de goma;un pasaporte|¿Qué está haciendo el agente?|Está sellando el pasaporte del viajero.
5141|abrir la boca;enseñar los músculos;darle una tarjeta|un cartel;un armario;un médico;una camilla|¿Qué está abriendo el joven?|Está abriendo la boca.
5142|alisar una bandera;cruzar el césped corriendo;saludar desde sus jardines|banderines;vecinos;un peto;una valla de estacas|¿Qué está haciendo la niña?|Está cruzando el césped corriendo.
5144|llorar en su hombro;llevar un traje beige;volar alto sobre el monumento|palomas;un monumento;colegialas;una cesta de mimbre|¿Qué están haciendo las palomas blancas?|Están volando alto sobre el monumento.
5145|pulsar un botón;mirar el reloj;tener puertas azules|un edificio;un tranvía;una chaqueta;vaqueros|¿Qué está haciendo el joven?|Está mirando el reloj.
5146|pelar una manzana roja;descansar en su regazo;colgar por debajo de sus rodillas|geranios;un delantal;un cuenco;una tira de cáscara|¿Qué está haciendo la mujer?|Está pelando una manzana en una sola tira larga.
5147|llevar una bolsa blanca;mirar la comida;llenar toda la calle|el cielo;una pantalla;gente|¿Qué está haciendo la gente?|Está cruzando una calle concurrida.
5148|irse volando;beber de una botella;cruzar la calle|el cielo;un semáforo;una calle|¿Qué están haciendo los pájaros?|Los pájaros se están yendo volando.
5150|tender una receta;buscar en las estanterías;brillar encima de la puerta|estanterías;un farmacéutico;una receta;un mostrador|¿Qué está haciendo el farmacéutico?|El farmacéutico está leyendo su receta.
5151|sostener en alto un cuadro;usar un martillo;mostrar una casa blanca|gafas;montañas;una casa;un marco|¿Qué está haciendo el anciano?|Está colgando un cuadro nuevo.
5152|dejar una almohada blanca;tirar almohadas sobre la cama;dejarse caer sobre las almohadas|una cortina;una pared;una mujer;almohadas|¿Qué está haciendo la mujer?|Está tirando almohadas sobre la cama.
5153|tener el pelo largo y oscuro;llevar pantalones cortos azules;llevar una camisa blanca|el cielo;árboles;un hombre;un bancal|¿Qué está haciendo el hombre?|Está poniendo plantas pequeñas en el bancal.
5154|plantar una plántula diminuta;contemplar las plantas;tener un pitorro largo|el techo;un helecho;un hombre;plantas de interior|¿Qué está haciendo el hombre?|Está regando una plántula diminuta.
5155|poner un plato grande;abrir los brazos;poner pasta en el plato|una ventana;flores;platos;un tenedor|¿Qué está haciendo la mujer de azul?|Está poniendo un plato grande en la mesa.
5156|regatear a un defensa;arrodillarse en el campo;abrazar al goleador|una portería;un futbolista;espectadores;una línea blanca|¿Qué está haciendo el goleador?|Está arrodillado en el campo.
5157|dar toques a un balón;salir corriendo a la calle;doblarse de la risa|una colina;un coche aparcado;un balón;adoquines|¿Qué están haciendo los hombres?|Están jugando al fútbol en una calle adoquinada.
5158|enchufar un cable;brillar sobre su cabeza;mirar asombrado|un monitor;un altavoz;una persiana;cables|¿Qué está haciendo el joven?|Está conectando cables a su ordenador.
5161|apoyarse en una barandilla;dispersarse por la plaza;probar una empanadilla frita|una catedral;palomas;una mochila;adoquines|¿Qué está comiendo el joven?|Está comiendo empanadillas fritas.
5162|abrir los brazos;volar hacia el cielo;comer con tenedor|montañas;árboles;un lago;un hombre|¿Qué está haciendo en la mesa?|Está comiendo con tenedor.
5164|alisar un cartel;sostener en alto pancartas de campaña;sonreír encantada|focos;una pantalla;un atril;un público|¿Qué está haciendo con la brocha?|Está alisando un cartel de campaña.
5165|pescar una botella;echar humo gris;llorar desesperada|una chimenea;una tubería;una mujer;plástico|¿Qué está flotando en el río?|Hay basura de plástico flotando en el río.
5167|tocar la pared de azulejos;estar espolvoreado de azúcar;saborear un trozo de pastel|una ventana;azulejos;una camisa;una mano|¿Qué está tocando el hombre?|Está tocando la pared de azulejos.
5168|hornear pastelitos;comer un pastelito;llevar una bandeja grande|una niña;gente;una mujer;una hornada|¿Qué está haciendo la niña?|Está comiendo un pastelito.
5169|echar una postal al correo;elegir unas postales;estar pintado de amarillo brillante|el cielo;gafas;una chaqueta de punto;un buzón|¿Qué está haciendo en el buzón?|Está echando una postal al correo.
5170|entregar un paquete;rebuscar en su bolsa;regar el jardín delantero|una gorra;un paquete;un muro de ladrillo;una bicicleta|¿Qué está haciendo el cartero?|Está entregando un paquete.
5171|añadir unas verduras;poner la tapa;remover la sopa|un delantal;sopa;una olla|¿Qué está añadiendo a la olla?|Está añadiendo unas verduras.
5172|golpear la masa;aporrear un tambor;machacar las especias|masa;un cuchillo;un filete;chiles secos|¿Qué está haciendo la mujer vestida de vaquero?|Está aporreando un tambor.
5173|llenar una botella;tocar el agua;caer de las rocas|una cascada;una mochila;un impermeable;rocas|¿Qué lleva puesto la mujer?|Lleva puesto un impermeable rojo.
5174|levantar la jarra en alto;aplaudir a la joven;tener una barba blanca recortada|una jarra;un vestido estampado;arroz;ensalada|¿Qué está haciendo la joven?|Está sirviendo zumo de naranja en un vaso.
5175|levantar la jarra por encima de la cabeza;dejar una jarra de cristal;llenarse de té|un bigote;una jarra de metal;un delantal;una jarra de cristal|¿Qué está haciendo el camarero?|Está sirviendo té en un vaso pequeño.
5176|llenarse de café;contener la masa de tortitas;estar apilados en una torre|una taza;café;una cafetera|¿Qué está cayendo en la taza?|Está cayendo café solo en la taza.
5177|servir té en una taza;tener trenzas pelirrojas;estar en fila|una tetera;una taza;una mujer;una mesa|¿Qué está sirviendo en la taza?|Está sirviendo té en la taza.
5178|abrir la puerta del horno;meter la bandeja;estar sobre la encimera|un pañuelo;un microondas;una rejilla del horno;galletas|¿Qué lleva en la cabeza?|Lleva un pañuelo azul marino.
5179|alargar la mano hacia el horno;llevar una bandeja de horno;brillar de color naranja por dentro|un armario;un horno;un pañuelo;masa|¿Hacia dónde está alargando la mano?|Está alargando la mano hacia el horno caliente.
5181|bajar de una limusina;firmar un documento oficial;levantar los brazos en señal de triunfo|una firma;una pluma estilográfica;una bandera;un escritorio|¿Qué está firmando la mujer?|Está firmando un documento oficial.
5182|dar las últimas pinceladas;secarse la frente;bajar de la escalera de mano|un mural;un peto;una escalera de mano;la acera|¿Qué está mirando la mujer?|Está mirando hacia arriba su mural.
5184|apoyar una rodilla en el suelo;tender un anillo de compromiso;romper a llorar|una torre;un acordeón;un estuche de anillo;un vestido|¿Qué está sosteniendo el hombre?|Está sosteniendo un anillo de compromiso.
5185|aferrar una bolsa de papel;protegerlo de la lluvia;rodearlo con el brazo|un paraguas;barras de pan;una bolsa de papel;un impermeable|¿Qué está sosteniendo el anciano?|Está aferrando una bolsa de barras de pan.
5187|tirar de una cuerda gruesa;apretar los dientes;estar vacío en el prado|el cielo;una camiseta;un carro;césped|¿Qué está haciendo el chico?|Está tirando de una cuerda gruesa.
5188|luchar con una caña de pescar;llevar un salabre;caer en el embarcadero|el cielo;un salabre;una bota de goma;un embarcadero|¿Qué ha pescado el hombre con barba?|Ha pescado una bota de goma verde.
5189|tender la mano;abrir un paraguas rojo;sonreír a la cámara|una gorra;un paraguas;un abrigo;una calle|¿Qué está sosteniendo el anciano?|Está sosteniendo un paraguas rojo.
5190|subirse la capucha;abrir los brazos de par en par;sonreír a la cámara|el cielo;un impermeable;el mar;botas|¿Qué está haciendo junto al mar?|Está abriendo los brazos de par en par.
5191|subir por el mástil;ondear al viento;levantar el puño|una bandera;el cielo;un abrigo;nieve|¿Qué está haciendo la gente?|Está izando una bandera en la nieve.
5192|ondear al viento;ir sin gorro;estar en el horizonte|una bandera;un mástil;una cabaña;el horizonte|¿Qué está haciendo la gente?|Está izando una bandera roja.
5193|rascarse el brazo que le pica;apretar un tubo de crema;descansar en su regazo|un sarpullido;un tubo;guantes de jardinería;arbustos|¿Qué está haciendo la mujer de pelo oscuro?|Está aplicando crema en el sarpullido.
5194|leer una novela;pasar una página;cerrar el libro|una novela;un sofá;una ventana;cortinas|¿Qué está haciendo la mujer?|Está leyendo una novela.
5195|sentarse en un banco;levantar un libro grande;estar detrás del banco|un banco;un pájaro;un gorro;árboles|¿Qué está haciendo el hombre?|Está sentado en un banco.
5196|agarrarse a una barra de metal;contener un bostezo;parpadear en la oscuridad|un moño;gafas;un banco;una paloma|¿Cómo lleva el pelo la mujer?|Lleva el pelo recogido en un moño.
5197|subirse a su escritorio;fulminar con la mirada a sus compañeros;arrancarse la corbata|una silla giratoria;archivadores de anillas;un teléfono de mesa;luces del techo|¿Qué está haciendo la mujer enfadada?|Está fulminando con la mirada a sus compañeros.
5199|seguir una receta escrita a mano;cortar tomates cherry;echar un chorrito de aceite de oliva|un pañuelo;un delantal;una ensaladera;un pimiento rojo|¿Qué está siguiendo la mujer?|Está siguiendo una receta escrita a mano.
5200|sentarse bajo una manta;saltar de una silla;hacer flexiones|una planta;una puerta;una silla;una taza|¿Qué están haciendo los jóvenes?|Están chocando los cinco.
5201|tocar el agua;alejarse;reflejar el cielo|el cielo;una mujer;una montaña;agua|¿Qué está tocando la mujer?|Está tocando el agua.
5202|abrir la nevera;sonreír a la cámara;poner comida en los estantes|una mujer;leche;zumo;una nevera|¿Qué está abriendo la mujer?|Está abriendo la nevera.
5203|ir delante al entrar;llevar una tarta tapada;sostener una tarta con fresas encima|un ramo;un perchero;una fuente;copas de champán|¿Qué están haciendo los familiares?|Están levantando las copas para brindar.
5204|arrancar el papel de la pared;usar un martillo;pintar la pared|una planta;un cinturón de herramientas;un rodillo de pintura;azulejos|¿Qué está sosteniendo la mujer?|Está sosteniendo un rodillo de pintura.
5205|prestar juramento;sostener un libro encuadernado en piel;extender los brazos|una cúpula;columnas;una banda;fotógrafos|¿Por qué está levantando la mano la mujer?|Está prestando juramento.
5206|clavar notas en el tablón;pasar las páginas;mirar el tablón|hilo;gafas;un ordenador;un libro|¿Qué tiene la mujer en la boca?|Tiene un bolígrafo en la boca.
5207|despatarrarse en un banco de madera;beber agua a tragos de una botella;apoyarse en los bastones de senderismo|cumbres;un prado;un banco;una botella de agua|¿Qué está sosteniendo el hombre con barba?|Está sosteniendo dos bastones de senderismo.
5208|mirar asombrado;caer sobre una mesa de plástico;levantar la tapa de un tajín|el perfil de la ciudad;una vela;un traje;un filete|¿Qué está haciendo el hombre?|Está mirando asombrado.
5209|desplomarse en un sofá;dar sorbos a una bebida helada;tumbarse boca arriba en la hierba|el sol;el mar;una hamaca;arena|¿Qué está haciendo la mujer al atardecer?|Está relajándose en una hamaca.
5210|extender las alas;aferrar un sándwich;adueñarse de la manta|un estanque;un banco;un ganso;sándwiches|¿Qué están haciendo los amigos?|Están retrocediendo ante el ganso.
5211|arrastrar una maleta hacia dentro;dejarse caer en la cama;colgar de la cerradura|una estantería;un sofá;una alfombra;una maleta|¿Qué está arrastrando la niña detrás de sí?|Está arrastrando una maleta cubierta de pegatinas.
5212|llevar una bolsa grande;sostener un cartel;sostener una gorra|un techo;un reloj;un tren;un cartel|¿Qué está llevando la joven?|Está llevando una bolsa grande.
5213|sostener en alto un cartel de cartón;saltar a los brazos de alguien;llevar una gorra de béisbol|un techo de cristal;una vía férrea;un ramo;un andén|¿Qué está haciendo el niño?|Está sosteniendo un cartel de cartón por encima de la cabeza.
5214|ir en patinete;sentarse en un camello;sonreír a la cámara|el sol;una mujer;camellos;un desierto|¿Qué está haciendo en el desierto?|Está sentada en un camello.
5216|tocar un muro desmoronado;estar detrás de un puesto de flores;extender los brazos de par en par|cables eléctricos;un farol;un muro desmoronado;una cámara de carrete|¿Qué está haciendo en la azotea?|Está extendiendo los brazos de par en par.
5217|tocar el tejado;llevar un chaleco amarillo;sonreír a la cámara|el cielo;una torre;un chaleco;un tejado|¿Qué lleva puesto el hombre?|Lleva puesto un chaleco amarillo.
5218|abrir una puerta;entrar en una sala grande;mirar hacia el techo|el techo;ventanas;una niña;el suelo|¿Qué está haciendo la niña?|Está mirando hacia el techo.
5219|remover la pasta;agitar la mano con entusiasmo;picar patatas fritas|el techo;una camiseta;una sudadera con capucha;patatas fritas|¿Qué está haciendo el hombre de pelo rizado?|Está removiendo la pasta con una cuchara de madera.
5222|trazar una ruta;pasar corriendo junto a una roca;subir los escalones de piedra|el cielo;una mochila;escalones;hierba|¿Qué está subiendo la excursionista?|Está subiendo un largo tramo de escalones de piedra.
"""
src = json.load(open(f'{H}/source.json'))
d = {}
for line in rows.strip().splitlines():
    i, p, n, q, a = line.split(S)
    d[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: d[i] for i in src}
json.dump(out, open(f'{H}/es.json', 'w'), ensure_ascii=False, indent=1)
