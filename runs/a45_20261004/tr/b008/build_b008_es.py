import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
569|abrir con llave la puerta principal|tener un bigote poblado|llevar una coleta|una jefa de correos;llaves;paquetes;un carrito|¿Qué está haciendo la jefa de correos?|Está empujando un carrito lleno de paquetes.
572|cavar en el jardín|llevar una bufanda azul|estar posado en una valla|un pájaro;una mujer;patatas;un cubo|¿Qué está haciendo la mujer?|Está metiendo patatas en un cubo.
573|servir zumo de naranja|sostener una botella grande|coger un vaso|un hombre;una mujer;una botella;vasos|¿Qué está haciendo el hombre?|Está sirviendo zumo de naranja en vasos.
574|abrir mucho la boca|tocarse el pecho|tener el pelo corto y negro|un árbol;una brocha;un tarro;polvos|¿Qué hay en el tarro?|Hay polvos en el tarro.
575|levantar las manos|rebuscar en su bolso|levantar una batería externa|una batería externa;palomas;rosas;un banco|¿A qué están conectando el teléfono?|Lo están conectando a una batería externa.
576|rezar en su escritorio|juntar las manos|mirar hacia arriba y llorar|una mujer;un portátil;libros;una lámpara|¿Qué está haciendo la mujer?|Está rezando en su escritorio.
577|predecir la lluvia|echarse a reír|traer un chaparrón repentino|una nube de tormenta;un paraguas;un chal;hierba|¿Qué está haciendo la mujer?|Se está resguardando bajo un paraguas amarillo.
578|sacar una motocicleta empujándola|pulir el depósito de combustible|darle una palmada en el hombro|una bandana;un depósito de combustible;un motor;adoquines|¿Qué está haciendo la mecánica?|Está presentando su motocicleta con orgullo.
579|escribir código nuevo|hacer un gesto hacia el portátil|seguir la pista dibujada|un robot;un portátil;una coleta;una barba|¿Qué está haciendo la mujer?|Está programando un pequeño robot.
580|sostener en alto un abrigo|llevar una cesta|llevar gafas|una cesta;un abrigo;el cielo;gafas|¿Qué está haciendo la mujer alta?|Está protegiendo a su amiga de la lluvia.
581|aferrar un girasol|llevar una pancarta con un árbol|ondear con la brisa|un girasol;una palmera;el cielo;una multitud|¿Qué están haciendo las personas?|Están protestando con pancartas pintadas.
582|sentarse en una silla|cruzar los brazos|tocarle el hombro|una silla;una mujer;una ventana;una mesa|¿Cómo se siente la mujer?|Está orgullosa de su nueva silla.
584|hacer el pino|demostrarle que se equivoca|soltar un grito ahogado de asombro|pies descalzos;mallas;un banco;un chaleco de punto|¿Qué está haciendo la joven?|Está haciendo el pino para demostrarle que se equivoca.
585|tocar música en público|sentarse en una caja|lanzar agua hacia arriba|una farola;hombres;un acordeón;un estuche|¿Qué está haciendo la joven?|Está tocando el acordeón en público.
588|llevar botas rojas|llevar botas negras|estar lejos|un impermeable amarillo;un pájaro;botas rojas;un charco|¿Qué están haciendo las dos personas?|Están saltando a un gran charco.
589|sostener algo rojo|tener una barba corta|correr por la hierba|un perro;hierba;un hombre;una cuerda|¿Qué están haciendo el hombre y la mujer?|Están tirando de una cuerda gruesa.
590|lanzar puñetazos rápidos|sostener en alto las manoplas de boxeo|colgar de una cadena|una pared de ladrillo;un saco de boxeo;guantes de boxeo;pantalones cortos|¿Qué está haciendo la mujer?|Está golpeando las manoplas de boxeo.
591|lanzar puñetazos potentes|sujetar la escalera|balancearse colgado del techo|una cadena;un saco de boxeo;guantes de boxeo;pantalones cortos|¿Qué está haciendo el hombre?|Está lanzando puñetazos al saco de boxeo.
592|tener una barba oscura|llevar una camiseta blanca|rodar por la carretera|el cielo;una furgoneta;una carretera|¿Qué están haciendo los dos hombres?|Están empujando una furgoneta blanca.
593|tener el pelo corto y rizado|tener el pelo largo y oscuro|dormir en el suelo|una ventana;pijamas;una cama;un perro|¿Qué llevan puesto el hombre y la mujer?|Llevan puestos pijamas.
594|superar el listón|agitar una bandera verde|agitar los puños|un listón;una bandera;una coleta;una colchoneta|¿Cómo se clasifica la niña?|Se clasifica superando el listón.
595|comer hojas verdes|lavarse la cara|saltar por encima de la hierba|el cielo;un conejo;hierba;hojas|¿Qué está comiendo el conejo?|Está comiendo hojas verdes.
597|mirar a través de una raqueta|estar detrás de la red|sonreír a la cámara|flores;una pelota;una red;una raqueta|¿Qué está sosteniendo la mujer?|Está sosteniendo una raqueta negra.
598|abrir los brazos de par en par|llevar una camisa blanca|caminar a cuatro patas|un tejado;un árbol;un perro;un barco|¿Qué está haciendo la chica?|Está bailando bajo la lluvia.
599|regatear con un balón de colores|hacerle una entrada al hombre de negro|controlar un balón blanco|una portería;un balón de fútbol;césped;un tejado|¿Qué están haciendo los dos hombres?|Están disputándose el balón.
600|estar de pie sobre dos patas|tirar de una porción de pizza|tener grandes ruedas negras|una rata;pizza;escaleras;una ventana|¿Qué está haciendo la rata?|Está tirando de una porción de pizza.
601|afeitarse con una maquinilla de afeitar|señalar su reloj|caminar por el lavabo|una maquinilla de afeitar;una lámpara;un espejo;una camiseta|¿Qué está haciendo el hombre de blanco?|Se está afeitando con una maquinilla de afeitar.
604|sostener una manzana roja|vender fruta|imprimir un recibo largo|un recibo;manzanas;peras;botellas|¿Qué está mirando el hombre?|Está mirando un recibo largo.
606|estar en una jaula|tener una barba negra|tener el pelo rizado|una receta;un pájaro;tortitas;un hombre|¿Qué están comiendo el hombre y la mujer?|Están comiendo tortitas.
607|estar tumbado en el suelo|tocar el frigorífico|tener una barba negra|un frigorífico;un perro;un hombre;una mujer|¿Dónde están de pie el hombre y la mujer?|Están de pie junto al frigorífico.
608|agarrar con fuerza el volante|reír de alivio|reposar sobre el parabrisas|un volante;un salpicadero;un limpiaparabrisas;una sudadera|¿Qué está agarrando con fuerza la conductora?|Está agarrando con fuerza el volante.
609|llevar una mochila roja|quitarse las botas|llevar una bufanda azul|el cielo;un lago;una roca;una mochila|¿Qué están haciendo el hombre y la mujer?|Están descansando en la hierba.
610|llevar tres cintas|abrazar la calabaza grande|ser grande y naranja|una cinta;una calabaza;un sombrero;banderas|¿Qué hay en la calabaza grande?|Hay una cinta azul en la calabaza.
613|subir al ring|llevar guantes azules|sostener una botella de agua|un ring;un hombre;una pared|¿Qué está haciendo el hombre?|Está boxeando en el ring.
615|volar sobre el agua|desplazarse río abajo|crecer junto al río|un río;un pájaro;hojas;piedras|¿Qué se desplaza río abajo?|Dos hojas se desplazan río abajo.
616|tener el pelo rojo|llevar un jersey gris|ser grande y redonda|una roca;el cielo;un río|¿Sobre qué están de pie?|Están de pie sobre una gran roca.
618|atar una cuerda|estar detrás del carro|tener una rueda grande|un árbol;una cuerda;una rueda;barro|¿Qué está haciendo el hombre grande?|Está tirando de un carro con una cuerda.
619|izar una cesta|esperar en el callejón|pasear por un muro|hierbas aromáticas;naranjas;una cesta;una cuerda|¿Qué está haciendo la mujer?|Está izando una cesta de naranjas.
621|estar de pie junto a la hilera|llevar un sombrero rosa|tener la parte superior roja|el cielo;un sombrero;plantas;el suelo|¿Qué están haciendo las personas?|Están plantando plantas pequeñas en hilera.
622|tirar de una goma elástica|tocarse la cara|caminar por la calle|una goma elástica;una mujer;un hombre;una caja|¿Qué está haciendo la mujer?|Está tirando de una goma elástica.
623|mirar su teléfono|traerle un café|poner los pies en alto|un teléfono;gafas de sol;una bota;un tenedor|¿Qué está haciendo el joven?|Está mirando su teléfono.
626|beber de un vaso|ver la carrera|mirar su reloj|un vaso;un reloj;el cielo;una corredora|¿Qué está haciendo la corredora?|Está bebiendo de un vaso.
627|pavonearse por la alfombra|grabar a su amiga|permanecer sentado totalmente quieto|una alfombra;guirnaldas de luces;una chimenea;una lámpara de pie|¿Qué está haciendo la mujer de azul?|Se está pavoneando por la alfombra.
628|empaquetar algunos libros|sostener un libro|llorar en el suelo|estantes;gafas;libros;cajas|¿Qué está haciendo la mujer?|Está llorando en el suelo.
629|cerrar la puerta|colgar una chaqueta|llevar una chaqueta amarilla|una mujer;un hombre;tazas;leña|¿Qué está cerrando la mujer?|Está cerrando la gran puerta de madera.
630|tirar de una cuerda larga|sujetar el gran timón|levantar ambos brazos|una marinera;un timón;una cuerda;una vela|¿Qué está haciendo la marinera?|Está tirando de una cuerda larga.
631|cortar un pepino|mezclar la ensalada|comer un tomate pequeño|una mujer;un hombre;ensalada;una mesa|¿Qué está preparando el hombre?|Está preparando una ensalada.
632|echar sal a los tomates|tener el pelo corto y oscuro|estar fuera de la ventana|un pájaro;sal;tomates;pan|¿Qué está haciendo la mujer?|Está echando sal a los tomates.
634|verter arena seca|dibujar con un palo|cubrir el dibujo|una mujer;un hombre;una ola;arena|¿Qué está haciendo el hombre?|Está vertiendo arena en su mano.
635|ponerse las sandalias|llevar pantalones cortos verdes|estar de pie sobre un banco|el cielo;un pájaro;un banco;sandalias|¿Qué llevan en los pies?|Llevan sandalias.
636|preparar un sándwich|cortar el sándwich|estar detrás de la cesta|árboles;un pato;una cesta;un sándwich|¿Qué está preparando la mujer?|Está preparando un sándwich.
638|verter salsa verde|comer una patata|sentarse en la hierba|un hombre;una mujer;un perro;salsa|¿Qué está haciendo el hombre?|Está vertiendo salsa verde.
639|dar la vuelta a las salchichas|comer un perrito caliente|estar en una sartén|un gorro;una tienda de campaña;un pájaro;salchichas|¿Qué está comiendo la mujer?|Está comiendo un perrito caliente.
640|coger dos pesas|mostrar sus grandes brazos|señalar la báscula|un hombre;una mujer;el suelo;una báscula|¿Sobre qué está de pie el hombre?|Está de pie sobre una báscula.
641|verter un poco de harina|llevar una trenza larga|encaramarse a la báscula|sartenes de cobre;un gato atigrado;un cuenco para mezclar;una báscula de cocina|¿Dónde está encaramado el gato?|Está encaramado en la báscula de cocina.
642|señalar su antebrazo|tener una barba poblada|mostrar su espinilla con una cicatriz|una gabardina;una bombilla;una cicatriz;tazas|¿Qué está mostrando el hombre rubio?|Está mostrando una cicatriz en la espinilla.
644|taparse la boca|llevar una bolsa blanca|sostener en alto un teléfono|gafas;pelo;una bolsa;el suelo|¿Qué está haciendo la mujer asustada?|Se está tapando la boca.
645|dibujar un círculo|sostener un bolígrafo negro|llevar un reloj|un horario;un hombre;un cuaderno;carpetas|¿Qué está dibujando el hombre?|Está dibujando un círculo en el horario.
647|cortar el pelo con tijeras|mirarse en un espejo|sentarse en una silla|tijeras;un peine;una toalla;gafas|¿Qué está haciendo la mujer con gafas?|Está cortando el pelo con tijeras.
649|regañar al joven|aferrar un sombrero de paja|cruzarse de brazos|un pañuelo de cabeza;un delantal;una verja;coles|¿Qué está haciendo la anciana?|Está regañando al joven.
650|gatear por el suelo|llevar una trenza larga|asomarse por encima de la caja|un tornillo;una caja de cartón;un golden retriever;un pulgar|¿Qué está buscando el hombre?|Está buscando un tornillo que falta.
651|apretar un tornillo|sujetar el estante de madera|encaramarse al sofá|un destornillador;libros;un gato;una planta de interior|¿Qué está haciendo la mujer?|Está apretando un tornillo con un destornillador.
652|chocar contra las rocas|llevar una camisa blanca|tener el pelo corto|el mar;una mujer;un hombre;rocas|¿Qué están haciendo?|Están saltando al mar.
653|coger un cojín|señalar las llaves|estar tumbado junto a la puerta|llaves;una puerta;un gato;un hombre|¿Qué está señalando el hombre?|Está señalando las llaves que están en la puerta.
654|susurrar un secreto|escuchar a su amiga|mirar por encima del muro|el cielo;una lámpara;una montaña;gafas|¿Qué está haciendo la mujer de amarillo?|Le está susurrando un secreto a su amiga.
655|pintar una línea negra|entrar corriendo en la habitación|soplar una pequeña corneta|un gorro;gafas;papel;una mesa|¿Qué está haciendo la mujer de azul?|Está pintando una línea negra sobre papel.
656|pulsar el reloj de ajedrez|llevar una chaqueta caqui|levantar ambos puños cerrados|ventanas en arco;una cuerda;un reloj de ajedrez;un tablero de ajedrez|¿Qué está haciendo la jugadora de ajedrez?|Está pulsando el reloj de ajedrez después de su jugada.
657|servir la comida|verter un poco de agua|mirar su comida|una mujer;un vaso;un tenedor;una mesa|¿Qué está haciendo la mujer?|Le está sirviendo comida al hombre.
660|enjabonar el pelo de su amiga|inclinarse sobre la palangana|recoger el agua jabonosa|hojas de platanero;un grifo;una palangana;un taburete|¿Qué está haciendo la mujer de verde?|Está enjabonando el pelo de su amiga.
661|abrir su gran boca|acercarse mucho|nadar en grupo|peces;un tiburón;agua|¿Qué está haciendo el tiburón?|El tiburón está abriendo su gran boca.
662|dibujar una estrella|tener el pelo corto|comer hierba|un caballo;un sacapuntas;un cuaderno;un cuenco|¿Qué está dibujando la mujer?|Está dibujando una estrella.
663|ponerse espuma de afeitar|mirarse en el espejo|observar a su amigo|lámparas;un espejo;espuma de afeitar;un grifo|¿Qué está haciendo el hombre de azul?|Se está poniendo espuma de afeitar en la cara.
664|afeitarle la cara al hombre|estar tumbado en un sillón|sentarse junto a la ventana|botellas;un gato;un hombre;un cuenco|¿Qué está haciendo la mujer?|Le está afeitando la cara al hombre.
666|ponerse una camisa|observar al hombre|abotonarse la camisa|un pájaro;una mujer;una camisa|¿Qué está haciendo el hombre?|Se está poniendo una camisa azul.
667|agarrarse la cabeza|estar tirado en la acera|soltar un grito ahogado de la impresión|un peatón;un casco;un escúter;la acera|¿Qué está haciendo la mujer?|Se está agarrando la cabeza por la impresión.
668|atarse los zapatos|sostener vasos de café|caminar por el agua|una puerta;pantalones;zapatos;el suelo|¿Qué está haciendo la mujer?|Se está atando los zapatos marrones.
669|llevar una cesta|darle el pan|pagar con monedas|una lámpara;gafas;pan;un sombrero|¿Qué está haciendo la mujer?|Está comprando pan en una tienda.
671|tener una barba corta|llevar una mochila azul|tener el cuello largo|el cielo;una llama;un hombre;una mujer|¿Qué están haciendo las dos personas?|Están gritando cerca de una llama.
672|sostener una toalla|llevar una camiseta azul|estar de pie sobre la ducha|un pájaro;una ducha;una toalla;un hombre|¿Qué está haciendo la mujer?|Se está duchando en la playa.
674|sonarse la nariz|traerle una taza|crecer junto a la ventana|una planta;una taza;una manta;una mesa|¿Qué está haciendo la mujer?|La mujer enferma se está sonando la nariz.
675|inclinarse sobre un cubo|llevar gafas|volverse de un azul vivo|un barco;una red;un hombre;cubos|¿Qué está haciendo el hombre rubio?|Está pintando el costado del barco.
678|sostener en alto la seda|tener el pelo hasta los hombros|agazaparse en el mostrador|un ventilador;seda;un gato;un mostrador|¿Qué está haciendo la mujer de beige?|Se está apretando la seda contra la mejilla.
679|limpiar la plata|ponerse unos pendientes|colgar sobre su cabeza|una lámpara;plata;una mujer|¿Qué está haciendo la mujer?|Está limpiando plata con un paño.
681|mirar a la cámara|conducir el coche|ser larga y recta|un espejo;una carretera;un hombre;una mujer|¿Qué están haciendo?|Están cantando en el coche.
683|abrir el grifo|sostener una esponja amarilla|mostrar un plato limpio|un hombre;una mujer;un fregadero;platos|¿Qué están lavando en el fregadero?|Están lavando platos en el fregadero.
684|sentarse a la mesa|abrir la puerta|abrazar a las dos niñas|una puerta;una niña;una cuchara;un tenedor|¿Qué están haciendo las dos hermanas?|Las dos hermanas se están abrazando.
685|probarse sombreros|sostener un espejo pequeño|vender sombreros|el cielo;un sombrero;pelo;un vestido|¿Qué está haciendo la chica?|Se está probando sombreros.
687|montar en un monopatín|saltar en el aire|brillar sobre la ciudad|el sol;casas;un chico;un monopatín|¿Qué está haciendo el chico?|Está montando en un monopatín.
688|ponerse crema facial|frotarse el brazo|tocarse las mejillas|piel;el cielo;plantas;una camiseta|¿Qué está haciendo la mujer?|Se está poniendo crema en la piel.
689|sujetarse la falda|darse la vuelta|llevar zapatos blancos|una falda;una camiseta;pájaros;árboles|¿Qué lleva puesto la mujer?|Lleva puesta una falda amarilla.
691|vigilar un coche gris|blandir un palo de madera|estar aparcado fuera|un soldado;alambre de espino;un muro de hormigón;un camino de tierra|¿Qué está haciendo el soldado?|Está vigilando el coche con un palo.
692|levantar los brazos|dormir bajo una manta|leer un libro|un gato;una lámpara;una manta;una almohada|¿Qué está haciendo el hombre?|Está durmiendo bajo una manta.
693|frotarse los ojos|dormir junto a la ventana|reposar sobre su regazo|una ventana;un asiento;un jersey;un cuaderno|¿Cómo se siente la mujer?|Tiene mucho sueño.
695|apoyarse en su mano|llevar una bufanda verde|volar sobre el barco|el sol;pájaros;un barco;el mar|¿Qué están haciendo las personas?|Están sonriendo en el barco.
696|reírse del hombre|apartar el humo con la mano|elevarse hacia el cielo|humo;una mujer;un hombre;hojas|¿Qué está haciendo el hombre?|Está apartando el humo con la mano.
697|llevar una chaqueta roja|tener una barba negra|encender un cigarrillo|una lámpara;un cigarrillo;una chaqueta|¿Qué está haciendo el hombre de rojo?|Está fumando un cigarrillo.
698|servir un batido|añadir más fruta|mezclar la fruta|un batido;plátanos;fresas;una mujer|¿Qué está haciendo la mujer de naranja?|Está sirviendo un batido en un vaso.
699|pasar queso de contrabando|levantar la barrera|estar cargado de heno|un guardia;heno;una barrera;un carro|¿Qué está pasando de contrabando el granjero?|Está pasando queso de contrabando bajo el heno.
700|moverse muy despacio|subirse a una hoja|estar sobre el camino|un caracol;una hoja;hierba|¿Qué está haciendo el caracol?|Se está subiendo a una hoja.
701|desplazarse por la arena|sacar la lengua|estar debajo de la serpiente|una serpiente;una roca;arena;el cielo|¿Dónde está tumbada la serpiente?|Está tumbada sobre una roca negra.
"""
out = {}
for line in DATA.strip().split('\n'):
    f = line.split('|'); assert len(f) == 7, line
    out[f[0]] = {"phrases": f[1:4], "nouns": f[4].split(';'), "question": f[5], "answer": f[6]}
src = json.load(open(f'{HERE}/source.json'))
out = {k: out[k] for k in src}
json.dump(out, open(f'{HERE}/es.json', 'w'), ensure_ascii=False, indent=1)
