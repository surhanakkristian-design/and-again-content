import json, os
H = os.path.dirname(os.path.abspath(__file__))
R = """
306|tener el pelo largo|tener la barba corta|brillar sobre las nubes|el sol;nubes;una mujer;un hombre|¿Sobre qué están volando?|Están volando sobre las nubes.
307|llevar un gorro rojo|caminar hacia el interior de la niebla|tener la lana blanca|niebla;una oveja;un gorro;hierba|¿Hacia dónde está caminando el hombre?|Está caminando hacia el interior de la niebla.
308|tener el pelo largo y rizado|estar de pie junto a la mesa|levantar la vista hacia ellos|queso;uvas;una mujer;un muro|¿Qué hay en la mesa?|La mesa está llena de comida.
309|marcar un gol|saltar a por el balón|entrar volando en la portería|un balón de fútbol;un hombre;el mar;arena|¿A qué están jugando?|Están jugando al fútbol en la arena.
310|tocar un árbol grande|llevar una chaqueta gris|brillar entre los árboles|el cielo;árboles;hierba;una mujer|¿Por dónde están caminando?|Están caminando por un bosque.
311|levantar un tenedor|abrir mucho los ojos|arder sobre la mesa|un tenedor;una vela;ensalada;pasta|¿Qué está haciendo la mujer?|Está comiendo pasta con un tenedor.
312|regatear con el balón|cometer una falta|tocar el silbato|el techo;una muñequera;una insignia|¿Qué está haciendo la árbitra?|Está tocando el silbato por una falta.
313|difuminar la base de maquillaje|girar la cabeza hacia un lado|reflejar a las dos mujeres|loros;trenzas;un espejo;base de maquillaje|¿Qué está haciendo la mujer de blanco?|Está difuminando la base de maquillaje con una esponja.
314|caminar por la hierba|saltar muy alto|sacudir el cuerpo|un zorro;un árbol;hierba|¿Qué está haciendo el zorro?|Está caminando por la hierba fría.
315|lanzar un tiro libre|formar una barrera defensiva|lanzarse a por el balón|un balón de fútbol;defensas;una colina;el campo|¿Qué está haciendo el jugador de rojo?|Está lanzando un tiro libre.
316|abrir el congelador|sostener los guisantes|sostener el helado|una cuchara;helado;un gorro;un congelador|¿Qué está sosteniendo la mujer?|Está sosteniendo una bolsa de guisantes.
317|cocinar patatas fritas|comer patatas fritas|llevar un gorro negro|patatas fritas;un gorro;bicicletas;luces|¿Qué está haciendo el cocinero?|Está cocinando patatas fritas.
318|parecer muy triste|compartir su helado|estar tirado en el suelo|una niña;el cielo;el mar;un helado|¿Qué está haciendo la niña de verde?|Está compartiendo su helado con su amiga.
319|estar sentado en una piedra|saltar a una hoja|nadar en el agua|una rana;una piedra;un pez|¿Qué está haciendo la rana?|Está sentada en una piedra.
320|limpiar el banco cubierto de escarcha|tocar una hoja helada|colgar entre dos postes|una telaraña;un banco;el sol|¿Qué está limpiando la mujer?|Está limpiando la escarcha del banco.
321|comer un melocotón|llevar una cesta|estar de pie detrás de la mesa|una piña;uvas;un melocotón;una cesta|¿Qué está comiendo la mujer?|Está comiendo un melocotón.
322|hacer una apuesta enorme|taparse los ojos con ansiedad|girar a gran velocidad|fichas;un pendiente;una barba|¿Qué está haciendo la mujer?|Está haciendo una apuesta enorme.
323|botar el balón|levantar a la mujer|volar por el aire|un balón;el cielo;una red;árboles|¿A qué están jugando los amigos?|Están jugando un partido de baloncesto.
326|oler una rosa de color rosa|llevar una caja de madera|caminar cerca del hombre|una rosa;una mujer;una casa;el cielo|¿Qué está oliendo la mujer?|Está oliendo una rosa de color rosa.
327|comer un tomate rojo|llevar un sombrero|volar cerca de las flores|el cielo;un sombrero;un hombre;una abeja|¿Qué está comiendo el hombre?|Está comiendo un tomate rojo.
328|pelar el ajo|estar sentado en la cocina|entrar en la cocina|una olla;un cuchillo;ajo|¿Qué está oliendo la mujer?|Está oliendo el ajo.
329|sostener una tetera blanca|abrir el gas|echar aceite en la sartén|una mujer;una olla;una tetera;fuego|¿Qué está sosteniendo el hombre?|Está sosteniendo una tetera blanca.
331|recoger una naranja|llevar una cesta|quitarse el sombrero|un paraguas;un caballero;una mujer;una cesta|¿Qué está llevando la anciana?|Está llevando una cesta de naranjas.
333|saltar por encima de una cuerda|llevar una camiseta amarilla|levantar las manos|una mujer;una pared;una niña|¿Qué está haciendo la niña de los vaqueros?|Está saltando por encima de una cuerda.
334|llevar una camisa blanca|tener la barba oscura|estar en un cuenco|un vaso;una jarra;limones;el cielo|¿Qué está haciendo la mujer?|Está bebiendo limonada de un vaso.
336|limpiar sus gafas|llevar una chaqueta azul|nadar en el agua|gafas;hojas;agua;un dedo|¿Qué está limpiando la mujer?|Está limpiando sus gafas.
338|señalar un continente|girar sobre su soporte|brillar sobre el escritorio|un globo terráqueo;una pantalla de lámpara;un pendiente;un jersey|¿Qué está haciendo la mujer?|Está señalando un continente en el globo terráqueo.
340|estar sentado en un banco|estar tumbado en el suelo|entrar volando en la portería|una portería;el cielo;piedras;una mujer|¿Adónde está volando el balón?|El balón está entrando volando en la portería.
341|trepar a un muro de piedra|morder una camisa blanca|estar de pie en el tejado|el cielo;una cabra;un tejado;un muro|¿Qué está mordiendo la cabra?|Está mordiendo una camisa blanca.
342|ponerse unas gafas de natación azules|señalar con un dedo|nadar bajo el agua|un gorro;gafas de natación;agua;un bañador|¿Qué se está poniendo la niña?|Se está poniendo unas gafas de natación azules.
344|levantar algo pesado|limpiar un lingote de oro|llevar una cadena de oro|gafas;una chaqueta;un lingote de oro;una cadena|¿Qué está limpiando la mujer?|Está limpiando un lingote de oro.
346|jugar al golf|sostener una bandera roja|rodar por la hierba|el cielo;una bandera;una pelota;un hoyo|¿Qué está haciendo la mujer?|Está jugando al golf.
348|sellar un documento oficial|gesticular con los brazos abiertos|mostrar tres barras de colores|un rotafolio;un sello de goma;un puntero|¿Qué está haciendo la mujer de morado?|Está sellando un documento oficial.
349|llevar una gorra|llevar una camiseta azul|estar tumbado sobre la madera|un abuelo;un niño;una mesa;árboles|¿Quién está jugando con el niño?|Su abuelo está jugando con él.
350|llevar una mochila|caminar hacia la puerta|estar sentado en un sillón|un nieto;una abuela;un sillón|¿A quién está abrazando la abuela?|Está abrazando a su nieto.
351|llevar una camiseta amarilla|llevar unos pantalones cortos azul oscuro|tener el pelo corto|hierba;un pájaro;una chica;un chico|¿Dónde están tumbados?|Están tumbados en la hierba.
352|tender la mano|levantar un dedo|tener rayas oscuras|flores;una mesa;una vela;una parrilla|¿Qué hay en la parrilla?|Hay queso y verduras en la parrilla.
355|hundir la cara|tener una grieta larga|contener arroz y guiso|un marco de fotos;cerámica;un sofá;un plato|¿Cómo está mostrando el hombre su culpa?|Está hundiendo la cara en las manos.
356|llevar una bolsa grande|mirar por todo el gimnasio|colgar de su hombro|el techo;pesas;una camiseta;una bolsa|¿Qué está llevando la mujer?|Está llevando una bolsa al interior del gimnasio.
357|cepillarse el pelo largo|dar palmas|estar tumbado junto a las flores|una cortina;una ventana;flores;un cepillo para el pelo|¿Quién está sosteniendo el cepillo para el pelo?|La mujer del pelo largo está sosteniendo el cepillo para el pelo.
359|correr en una rueda|comer unas semillas|estar lleno de semillas|un hámster;una rueda;un cuenco|¿Qué está haciendo el hámster?|Está comiendo semillas de un cuenco.
360|mirar por encima del asiento|tener la barba negra|estar sentado al lado del hombre|desinfectante de manos;un perro;un hombre;una mesa|¿Qué se están poniendo en las manos?|Se están poniendo desinfectante de manos en las manos.
361|envolver piruletas en papel|estar en un montón|tener una cara sonriente|piruletas;un ramo;una cinta|¿Qué están haciendo las manos?|Están envolviendo piruletas en papel.
362|bailar en la calle|comer un melocotón|acercarse a la mujer|un melocotón;un perro;un barco;zapatos|¿Qué aspecto tiene la mujer?|Parece muy feliz.
363|tomar apuntes|iluminar el escritorio|mostrar un documento|una lámpara de escritorio;un cárdigan;un portátil;notas adhesivas|¿Qué está haciendo el hombre?|Está investigando en su escritorio.
364|dibujar en papel|sostener un lápiz naranja|sonreír a la cámara|una cara;una camiseta;un lápiz;un dibujo|¿Qué está haciendo el hombre?|Está dibujando con un lápiz naranja.
366|quitarse una venda|agarrar una anilla de gimnasia|agitar el puño en señal de triunfo|una manga;un puño;una taza de café;llaves del coche|¿Qué está agarrando la mujer?|Está agarrando una anilla de gimnasia.
367|comer un polo|sostener un abanico|estar tumbado en el suelo|el cielo;una fuente;una camisa;un vestido|¿Qué está comiendo el hombre?|Está comiendo un polo naranja.
369|pasar junto a la moto|tener dos espejos|flotar en el cielo|un coche;una carretera;una moto;el cielo|¿Qué está haciendo el coche?|Está pasando junto a la moto.
370|ponerse un casco|sostener un monopatín|sostener un vaso|un casco;pantalones;un monopatín;el cielo|¿Qué se está poniendo la chica?|Se está poniendo un casco rojo.
371|frotar las hojas de albahaca|esparcir hierbas aromáticas sobre los espaguetis|levantar las cejas|hierbas aromáticas;una barba;espaguetis;un plato|¿Qué está haciendo la mujer?|Está esparciendo hierbas aromáticas sobre los espaguetis.
372|hacer malabares con un balón de fútbol|hacer el pino|girar por el aire|rascacielos;un balón de fútbol;una sombra|¿Qué está haciendo el hombre?|Está haciendo trucos con un balón de fútbol.
373|entrar en un estadio|llevar camisetas rojas|bajar las escaleras|el cielo;un estadio;un hombre;escaleras|¿Qué está haciendo el hombre rubio?|Está entrando en un estadio.
374|trotar por la carretera|mantener un ritmo constante|tener las piernas tatuadas|una farola;el cielo;un corredor;una carretera|¿Qué está haciendo el hombre?|Está trotando por la carretera.
375|abrocharse la correa del casco|correr a toda velocidad por la pista|agarrar el volante|el sol;una tribuna;un coche de carreras;asfalto|¿Qué está haciendo el coche de carreras?|Está corriendo a toda velocidad por la pista.
377|actuar para la cámara|tocar la batería|recostarse en un sofá|un foco;una artista;una batería;un sofá|¿Qué está haciendo la mujer?|Está actuando para la cámara.
379|saludar a la cámara con la mano|echarse el pelo hacia atrás|grabar un vlog|cortinas;figuritas;pecas;un portátil|¿Qué está haciendo la joven?|Está grabando un vlog en su dormitorio.
380|pasar por un torniquete|estar sobre una superficie de madera|proteger de la lluvia|una mochila;gafas;un teléfono inteligente;una ventana|¿Por dónde está pasando la mujer?|Está pasando por un torniquete del metro.
381|sostener una uva verde|parecer muy asustado|mostrar muchas fotos|pelo;una uva;fotos;un lavabo|¿Qué está sosteniendo el hombre?|El hombre asustado está sosteniendo una uva.
382|limpiar una ventana|sostener una herramienta amarilla|colgar a gran altura|un casco;el cielo;la ciudad|¿Qué está haciendo la mujer?|Está limpiando una ventana alta.
386|tener la barba negra|enseñarle sus barcos|estar tumbado en una caja|un hombre;una mujer;un gato;barcos|¿Qué le está enseñando el hombre?|Le está enseñando sus barcos pequeños.
387|descansar sobre la alfombra|despertar a su dueño|dormir bajo un edredón|una alfombra;un edredón;una almohada;una mesilla de noche|¿Qué está haciendo el perro?|El perro está intentando despertar a su dueño.
388|hacer sus deberes|llevar gafas redondas|escribir con un bolígrafo|pelo;gafas;un bolígrafo;deberes|¿Qué está haciendo la chica?|Está haciendo sus deberes.
389|poner miel en el pan|comer pan con miel|estar tumbado en un muro|una mujer;un hombre;pan;miel|¿Qué está comiendo el hombre?|Está comiendo pan con miel.
390|subirse la capucha|llevar una sudadera con capucha roja|nadar en el agua|agua;bicicletas;una sudadera con capucha;patos|¿Qué está haciendo el hombre?|Se está subiendo la capucha sobre la cabeza.
391|subirse al muro|levantar los brazos|navegar por el mar|una mujer;un barco;el mar;un muro|¿Qué está mirando la mujer?|Está mirando un barco.
392|montar un caballo|llevar a la mujer|subirse al caballo|el cielo;una mujer;un caballo;hierba|¿Qué está haciendo la mujer?|Está montando un caballo.
393|entregar una llave|agarrar la escalera de mano de madera|tender unas patatas fritas de bolsa|una escalera;un recepcionista;un mostrador;una llave|¿Qué está ofreciendo la mujer pelirroja?|Está ofreciendo una bolsa de patatas fritas.
394|secarse la cara|sostener una botella de agua|echarle aire|un tejado;una pared;un ventilador;una toalla|¿Qué está haciendo el hombre?|Se está secando la cara con una toalla.
396|sostener un regalo pequeño|correr hacia el hombre|caminar a cuatro patas|ventanas;un abrazo;un perro;el suelo|¿Qué están haciendo el hombre y la mujer?|Se están dando un abrazo.
397|mirar con unos prismáticos|llevar un gorro de punto|pastar entre los árboles|troncos de árboles;un ciervo;hojas caídas|¿Qué están haciendo el hombre y la mujer?|Están cazando un ciervo en el bosque.
398|enjuagarse la boca|enjabonarse las manos|secarse la cara a toquecitos|un espejo;un pijama;espuma;un lavabo|¿Qué está haciendo el niño?|Se está enjabonando las manos sobre el lavabo.
399|lamer el helado|llevar un sombrero grande|estar de pie sobre el muro|el cielo;un pájaro;un sombrero;helado|¿Qué está haciendo el hombre?|Está lamiendo su helado.
400|patinar alrededor de un cono|llevar un casco blanco|gritar detrás del cristal|aficionados;una portería;hielo|¿Qué están haciendo las chicas?|Están jugando al hockey sobre hielo.
404|mirar a la cámara|pelearse al fondo|reírse juntos|cortinas;pósteres;una tableta;un pupitre|¿Qué están haciendo los chicos que están detrás de él?|Se están peleando en el aula.
405|entrar el primero|llevar una olla caliente|tener el pelo muy corto|una lámpara;una ventana;un fuego;una mesa|¿Qué están haciendo las personas?|Están entrando desde la nieve.
407|abrir mucho los brazos|tener el pelo largo|volar sobre los árboles|pájaros;una isla;un hombre;agua|¿Qué están haciendo los pájaros?|Están volando sobre la isla.
408|ponerse una chaqueta|sonreír al hombre|estar de pie sobre la valla|una chaqueta;una mujer;un pájaro;el cielo|¿Qué lleva puesto el hombre?|Lleva puesta una chaqueta marrón.
410|abrir un tarro de mermelada|mirar a la mujer|estar de pie junto a la ventana|mermelada;mantequilla;una cesta;un gato|¿Qué está haciendo la mujer?|Está poniendo mermelada en el pan.
411|fruncir el ceño con los brazos cruzados|ganar la cinta roja|entregar el premio|una cinta;medias;zapatillas de ballet;un espejo|¿Qué aspecto tiene la bailarina de turquesa?|Parece tener celos de la otra bailarina.
412|desdoblar una camiseta de fútbol|entregar una camiseta de equipo|ponerse una camiseta de equipo|una camiseta de equipo;una camiseta;una coleta;botas de fútbol|¿Qué está haciendo la mujer del pelo rizado?|Está desdoblando una camiseta de fútbol.
413|cortar una fruta roja|coger el vaso|caminar por el suelo|zumo;un cuenco;un árbol;un pájaro|¿Qué está bebiendo el hombre?|Está bebiendo un vaso de zumo.
414|correr por la pista|saltar por encima del listón|caer en la colchoneta|el cielo;una colchoneta;árboles;una mujer|¿Qué está haciendo la mujer de delante?|Está saltando por encima del listón.
415|saltar por la arena|quedarse con su madre|llevar una cría|un canguro;el sol;hierba;el cielo|¿Qué está llevando el canguro grande?|Está llevando a su cría.
418|abrir una anilla haciendo palanca|aplaudir con una gran sonrisa|hacer girar un llavero|un llavero;un vendedor;un cubo;una manga|¿Qué está haciendo la mujer?|Está haciendo girar un llavero en el dedo.
422|dar patadas a un saco grande|colgar de unas cuerdas|levantar mucho una pierna|una mujer;un saco;nubes;el suelo|¿Qué está haciendo la mujer?|Está dando patadas a un saco grande.
423|lanzar un beso|besarle la mano|llevar un sombrero grande|un sombrero;un hombre;una cesta;una botella|¿Qué está haciendo el hombre?|Le está besando la mano.
424|cortar el pan|secarse las manos|comer un sándwich de tomate|un cuchillo;un perro;un tomate;una mujer|¿Qué está haciendo el hombre?|Está cortando pan con un cuchillo.
426|subir por una escalera de mano|coger una manzana roja|mantener firme la escalera de mano|una escalera de mano;una oveja;un árbol;manzanas|¿Qué está haciendo la mujer?|Está subiendo por una escalera de mano.
427|trepar por la hierba|abrir las alas|volar hacia el cielo|una mariquita;una flor;el cielo;hierba|¿Qué está haciendo la mariquita?|Está trepando por la hierba.
428|lanzar una piedra|llevar un jersey gris|llevar un jersey rojo|el cielo;una montaña;una barca;un lago|¿Qué está haciendo el hombre?|Está lanzando una piedra al lago.
430|llevar una bolsa marrón|estar sentado en una caja|tener la barba blanca|casas;una chica;una cesta;un barco|¿Qué está llevando la chica?|Está llevando una bolsa marrón.
431|estar tumbado en el sofá|estar junto a la pared|coger el mando|una ventana;una escoba;un hombre;una mesa|¿Qué está haciendo el hombre?|Está tumbado en el sofá.
435|cepillar un cinturón de cuero|ponerse una chaqueta|estar tumbado debajo de la mesa|una mujer;una chaqueta;un cinturón;una mesa|¿Qué lleva puesto el hombre?|Lleva puesta una chaqueta de cuero.
436|tener el pelo largo y gris|llevar una falda amarilla|tener flores rosas|el cielo;un árbol;el mar;una falda|¿Hacia dónde están señalando las personas?|Están señalando hacia la izquierda.
437|subir la pierna|subir corriendo las escaleras|alzarse sobre la colina|el cielo;escaleras;una zapatilla;una pierna|¿Qué está haciendo la mujer?|Está subiendo corriendo las escaleras.
438|morder un limón|tener la barba oscura|estar tumbado en el muro|un limón;un cuchillo;una mano|¿Qué está haciendo la mujer?|Está mordiendo un limón.
439|beber limonada fría|estar tumbado en el suelo|crecer en una maceta|limonada;flores;un perro;una mujer|¿Qué está haciendo la mujer?|Está bebiendo limonada fría.
440|levantar pesas pesadas|llevar un cinturón ancho|sonreír al final|un hombre;un cinturón;una ventana|¿Qué está haciendo el hombre?|Está levantando pesas pesadas.
442|forcejear con una caja|echar una mano|agacharse detrás de una caja|un gato;cajas de cartón;una barba;un suelo de madera|¿Qué están haciendo el hombre y la mujer?|Están apilando cajas de cartón juntos.
"""
out = {}
for line in R.strip().split('\n'):
    i, p1, p2, p3, n, q, a = line.split('|')
    out[i] = {"phrases": [p1, p2, p3], "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{H}/source.json'))
out = {k: out[k] for k in src}
json.dump(out, open(f'{H}/es.json', 'w'), ensure_ascii=False, indent=1)
