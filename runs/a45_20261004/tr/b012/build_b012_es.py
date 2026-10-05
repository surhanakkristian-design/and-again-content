import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
4166|caminar hasta el coche;abrir la puerta del coche;entrar en el coche rojo|un hombre;un coche;un árbol;un arbusto|¿Qué está haciendo el hombre?|Está subiendo al coche rojo.
4167|salir de la cueva;alzarse sobre la playa;brillar en la oscuridad|una salida;una pared de cueva;un caballo|¿Adónde se dirige el caballo?|Se dirige a la salida de la cueva.
4168|dormir boca arriba;caminar muy despacio;volar por el aire|la luna;un conejo;una mariposa;una tortuga|¿Qué está haciendo la tortuga?|Está caminando muy despacio.
4169|mirar al oso;estar sentado en una barca;nadar cerca de la barca|árboles;un río;una gorra;un oso|¿Qué está haciendo el hombre?|Está echando un vistazo al oso.
4170|salvar a un pollito pequeño;saltar al agua;llevar una flor blanca|una gallina;pollitos;una flor;hielo|¿Qué está haciendo la gallina?|Está salvando a un pollito pequeño.
4171|avanzar con sigilo entre los arbustos;recostar la cabeza;proteger a sus pollitos|un incendio forestal;una cascada;una gallina;pollitos|¿Qué está haciendo el lobo?|Está avanzando con sigilo entre los arbustos.
4172|caminar por el agua;estar tumbada sobre las piedras;arder en el campo|una colina;un nido;una gallina;un río|¿Qué está haciendo la gallina?|Está llevando un nido a través del río.
4173|enseñar los dientes;precipitarse hacia la niebla;aferrarse a la cuerda|un lobo;una gallina;tablones|¿Qué está haciendo el lobo?|Está persiguiendo a la gallina por el puente.
4174|extender bien las dos alas;acurrucarse en la hierba;brillar sobre las copas de los árboles|la luna;pinos;un zorro;pollitos|¿Qué está haciendo la gallina?|Está defendiendo a sus tres pollitos.
4175|pasar a hurtadillas junto a un ventisquero;enseñar los dientes afilados;hundirse hacia el horizonte|un ventisquero;lobos;un saco;huellas|¿Qué está haciendo la gallina?|La gallina está pasando a hurtadillas junto a los lobos.
4176|aferrar un tarro de cristal;abrazar al pollito;colgar en el cielo nocturno|una luciérnaga;un pico;un tarro|¿Qué está brillando dentro del tarro?|Una luciérnaga está brillando dentro del tarro.
4177|escalar una roca alta;abrir la boca;llevar una bolsa grande|una gallina;una boca;un nido;una roca|¿Qué están haciendo los pajaritos?|Están abriendo la boca.
4178|asomarse a la madriguera;estar de pie debajo de la gallina;brillar en la oscuridad|una gallina;una vela;maíz|¿Qué está haciendo la gallina?|Está compartiendo el maíz con los ratones.
4179|soplar las velas;colgar en la pared;tener tres velas|gafas de sol;una camisa;velas;una tarta|¿Qué está haciendo la mujer?|Está soplando las velas de su cumpleaños.
4180|agarrar una correa roja;acunar a un cachorro;arrastrarse por la acera|una mujer;un cachorro;una correa;un caimán|¿Qué está haciendo la mujer?|Está paseando a un caimán con correa.
4181|ir en un escúter rojo;sonreír a la cámara;estar sobre un plato blanco|una mujer;velas;una tarta;un plato|¿Qué está haciendo la mujer?|Va en un escúter rojo.
4182|pintar la hierba;estar tumbada en la hierba;volar sobre la mujer|una mujer;un hombre;un árbol;hierba|¿Qué está haciendo el hombre?|Está pintando la hierba.
4183|abrir la caja grande;abrir bien los brazos;taparse la boca|un regalo;una mujer;un hombre|¿Qué está recibiendo la anciana?|Está recibiendo un regalo grande.
4184|traer de vuelta la pelota;correr tras la pelota;lanzar la pelota|un perro;una pelota;un sofá;una alfombra|¿Qué está haciendo el perro?|Está llevando la pelota a la máquina.
4185|aplastar el ratón;asomar por debajo;llevar frambuesas encima|una taza;gofres;una cola;un mantel individual|¿Qué está haciendo la taza?|Está aplastando el ratón de juguete.
4186|correr tras la pelota;traer de vuelta la pelota;golpear una pelota de tenis|árboles;una red;un perro;una máquina|¿Qué está haciendo el perro?|Está devolviendo la pelota a la máquina.
4187|sostener un juguete azul;estar tumbado boca arriba;caerse el último|cortinas;loros;un sofá;una mano|¿Qué están haciendo los loros?|Se están haciendo los muertos en el sofá.
4188|descender una pendiente empinada;levantar nieve polvo;brillar sobre las cumbres|cumbres;el sol;una pendiente|¿Qué está haciendo el esquiador?|Está bajando esquiando por una pendiente empinada.
4189|comer de un cuenco;estar sentado en el suelo;quedarse en el cuenco|un perro;un cuenco;una pastilla;una puerta|¿Qué hay en el cuenco vacío?|Hay una pastilla blanca dentro.
4191|dar saltos;alzarse sobre el hombre;levantar los dos brazos|el cielo;un cohete;el sol;un edificio|¿Qué está haciendo el hombre?|Está saltando delante de un cohete.
4192|planear sobre las olas;extender bien las alas;pescar con las garras|un ala;un pico;un pez;el mar|¿Qué está haciendo el águila?|El águila está atrapando un pez del mar.
4193|entrar en un garaje subterráneo;levantarse sobre bisagras;relucir bajo luces naranjas|árboles;una trampilla;un coche deportivo;pavimento|¿Qué está haciendo el coche?|Está entrando en un garaje subterráneo.
4194|conducir un coche rosa;crecer detrás de la mujer;doblar las rodillas|el cielo;un árbol;un coche;hierba|¿Qué está haciendo la mujer?|Está dando una vuelta en un coche.
4195|romperse en pedazos;brillar en el cielo;rodar por la carretera|una rueda;una cesta;zapatos;la carretera|¿Qué le está pasando al escúter?|El escúter se está rompiendo en pedazos.
4196|mirar una vela;dormir en una cama;marcar la hora|un cubo;una vela;un hombre|¿Qué hay en el cubo?|Hay una vela en el cubo.
4197|despertarse tarde;volar por el aire;colgar junto a la ventana|un teléfono;una manta;una cortina;una almohada|¿Qué está haciendo el hombre?|Se está despertando tarde.
4198|caer muy hondo;estar oscuro por dentro;brillar al sol|un agujero;el mar;una mano;un zapato|¿Adónde está cayendo la persona?|La persona está cayendo muy hondo en un agujero.
4199|arrastrar los pies;desplomarse sobre el prado;observar el aterrizaje|un parapentista;salpicaduras;un reflejo;una orilla|¿Qué está haciendo el piloto?|Está arrastrando los pies por el agua.
4200|estar de pie bajo un árbol;lanzarse en picado hacia la bahía;volver dorado el mar|un arco;un acantilado;espuma;el cielo|¿Qué está haciendo el sol?|Está volviendo dorado el mar.
4201|mantener las motos en vertical;bordear la orilla;reflejar las nubes rosas|motos de cross;palmeras;un reflejo;nubes|¿Qué están haciendo los motoristas?|Están manteniendo las motos en vertical.
4202|estar tumbados boca arriba;sostener un utensilio de cocina;acercarse a los perros|una barriga;una oreja;una mano|¿Qué están haciendo los dos perros?|Están tumbados boca arriba.
4203|rescatar a un tiburón varado;nadar mar adentro;agarrar la cola de un tiburón|un tiburón;un bañador;arena;el mar|¿Qué está haciendo el hombre?|Está rescatando a un tiburón varado.
4205|llevar una flor blanca;caerse al suelo;cerrar los ojos|un hámster;una flor;el suelo|¿Qué está llevando el hámster?|Está llevando una flor blanca.
4207|entregar una pizza;hacer scroll en un móvil;estar recostado en un sofá|un lazo;una pantalla de lámpara;una caja de pizza;una alfombra|¿Qué está haciendo el hámster con gafas?|Está entregando una pizza.
4208|comer una hamburguesa;estar tumbado boca arriba;colgar de una estantería|una hamburguesa;un vaso;un sofá;una planta|¿Qué está comiendo el hámster?|Está comiendo muchos aperitivos.
4211|beber con una pajita;lavarse la cara;tocarse las mejillas|un lazo;una mejilla;una caja|¿Qué está haciendo el hámster?|Se está lavando la cara.
4212|llevar un bolso pequeño;llevar tacones altos;arreglarse la manga|una mujer;un hombre;un bolso;un sofá|¿Qué está llevando la mujer?|Está llevando un bolso pequeño.
4213|señalar a su amiga;tocarle el hombro a su amiga;llevar un collar verde|un collar;un vestido;un bolso;una pared|¿Qué llevan puesto las dos mujeres?|Llevan puestos vestidos largos.
4214|sostener un bolso pequeño;tener el pelo corto y negro;crecer en una maceta|una mujer;un hombre;un bolso;un árbol|¿Qué está sosteniendo la mujer?|Está sosteniendo un bolso pequeño.
4215|llevar un top naranja;llevar pantalones naranjas;llevar una falda larga|una camisa;un top;un bolso;un sofá|¿Qué está sosteniendo la mujer?|Está sosteniendo un bolso pequeño.
4216|llevar un vestido blanco;llevar una camisa negra;llevar tacones altos|un vestido;una camisa;pantalones;un sofá|¿Qué lleva puesto la mujer?|Lleva puesto un vestido blanco.
4217|estar sentado en un coche verde;seguir al perro;acercarse|el cielo;un coche de policía;un perro;una carretera|¿Qué está haciendo el coche de policía?|Está siguiendo al perro.
4218|conducir un tractor oxidado;echar humo negro;rodar por la carretera|humo;un viñedo;un tubo de escape;un tractor|¿Qué está haciendo el perro?|Está conduciendo un tractor oxidado.
4219|girar la cabeza con cuernos;agarrar la silla de montar de cuero;caer en cascada por las rocas|el cielo;una bestia;un fiordo;un guante|¿Qué está haciendo la bestia?|La bestia se está lanzando en picado desde un acantilado.
4220|limpiar el coche blanco;sostener una bolsa negra;circular por la carretera|colinas;un hombre;un coche;una rueda|¿Qué está haciendo el hombre?|Está limpiando el coche blanco.
4221|llevar un cuenco;subirse al sofá;comer del cuenco|un sofá;un lagarto;un cuenco;una manta|¿Dónde está sentado el lagarto?|Está sentado en el sofá.
4223|tragarse una guindilla picante;escupir fuego;llenar un cuenco poco profundo|un geco;guindillas;un cuenco|¿Qué está comiendo el geco?|Está comiendo una guindilla picante.
4224|ir al baño;abrirse y cerrarse;estar en el suelo|un lagarto;una puerta;una alfombra;una planta|¿Adónde va el lagarto?|El lagarto va al baño.
4225|comer de un plato;estar detrás de la caja;abrirse por arriba|un hámster;un plato;una caja|¿Qué está haciendo el hámster naranja?|El hámster naranja está comiendo de un plato.
4226|agacharse junto al río;aferrarse al dinosaurio;precipitarse por el acantilado|un dinosaurio;un cocodrilo;una cascada;espuma|¿Qué están cazando los cocodrilos?|Los cocodrilos están cazando un dinosaurio enorme.
4227|pedalear en una bicicleta amarilla;acariciar a un perro peludo;encaramarse a una mochila|una caja;una agente de policía;un coche de policía;una bicicleta|¿Qué está haciendo la agente de policía?|Está acariciando a un perro amistoso.
4228|abrir bien los brazos;subir a un helicóptero;caer en una sartén|una montaña;un lago;una mesa;la orilla|¿Dónde está comiendo el hombre?|Está comiendo huevos en la orilla.
4229|liberar a un mono congelado;estar sentado atrapado en el hielo;saltar de la barandilla|carámbanos;un mono;un martillo|¿Qué está haciendo la persona?|La persona está liberando a un mono congelado.
4230|sujetar el volante;llevar un gorro naranja;tener una puerta roja|un asiento;un gorro naranja;un volante;una puerta|¿Dónde está sentado el perro grande?|Está sentado en el asiento del conductor.
4231|subir las patas;llevar una gorra roja;tener una puerta roja|una ventanilla;perros;un asiento;una puerta|¿Qué están haciendo los perros?|Están mirando por la ventanilla.
4232|sostener una pelota grande;saltar muy alto;agarrarse la cabeza|un delfín;una pelota;árboles;el cielo|¿Qué está sosteniendo el hombre?|Está sosteniendo una pelota grande.
4233|cruzar el puente;caer por las rocas;estar hecho de piedra|un tren;un puente;agua;árboles|¿Qué está haciendo el tren?|Está cruzando un puente de piedra.
4234|levantar los brazos de golpe;vaciar todo el armario;formar un montón enorme|vestidos;un pijama;jerséis|¿Sobre qué está de pie el hombre?|Está de pie sobre un montón de ropa.
4235|lanzar un sedal;estar de pie descalzo sobre la hierba;contener sedal turquesa|una caña de pescar;un niño;un lago;hierba|¿Qué está haciendo el niño?|Está lanzando un sedal al lago.
4236|pasear por la acera;estar de pie con las manos en las caderas;tirar los guantes al suelo|una furgoneta;un televisor;un bolso;tacones altos|¿Quién llama la atención de los hombres?|La mujer de los tacones altos les llama la atención.
4237|ofrecer una zanahoria;asomarse por encima de la cuadra;estar repleta de zanahorias|un caballo;una zanahoria;vaqueros;una cuadra|¿Qué está haciendo el hombre?|Está dando de comer al caballo en el establo.
4238|asarse sobre un fuego;usar un inflador naranja;llevar una camisa gris|carne;una mesa;una alfombra|¿Qué se está asando sobre el fuego?|La carne se está asando sobre el fuego.
4239|planear entre buques de carga;saltar fuera del agua;dominar el puerto|el cielo;un faro;una gaviota;riendas|¿Qué está haciendo la gaviota?|Está planeando sobre el puerto.
4240|revolcarse boca arriba;alzarse sobre el cachorro;tocar el pecho de su compañero|una cortina;un cachorro;una alfombra;un smartphone|¿Qué está haciendo el cachorro?|El cachorro se está revolcando boca arriba.
4241|llevar unos auriculares verdes;flotar bajo el avión;tener marcas pintadas|unos auriculares;un micrófono;un cinturón de seguridad;una corbata|¿Qué está haciendo el hombre?|Está pilotando el avión.
4242|saltar por encima de la barrera;pasar por una puerta;permanecer cerrada|una barrera;una pared;un gato;el suelo|¿Qué está haciendo el gato gris?|Está pasando por una puerta pequeña.
4244|cargar hacia el coche;observar desde lejos;echar la cabeza hacia atrás|un árbol;una cabra;un toro;grava|¿Qué está haciendo el toro?|Está cargando hacia el coche.
4245|deslizarse sobre la barriga;derramarse por encima del muro;esprintar por agua poco profunda|una cascada;una palmera;musgo;el cielo|¿Qué está haciendo el hombre de turquesa?|Se está deslizando sobre la barriga.
4246|sostener un pájaro grande;tener el cuello azul;reírse mucho|un pájaro;una gorra;una camiseta;árboles|¿Qué está sosteniendo la mujer?|Está sosteniendo un pájaro grande y azul.
4247|saltar al agua;terminar en el pozo;estar de pie en fila|un pozo;niños;un camino;el cielo|¿Qué están haciendo los niños?|Están saltando al pozo.
4248|nadar entre olas grandes;estar de pie junto a la piscina;llevar un gorro blanco|un nadador;luces;personas;agua|¿Dónde está nadando el hombre?|Está nadando en una piscina cubierta.
4249|escupir fuego;agarrarse fuerte;caer en el lago|el sol;un lago;un lomo;manos|¿Qué está haciendo el dragón?|Está volando sobre un lago.
4250|manejar una carretilla elevadora;mirar fijamente a la cámara;hacer señas con la pata|un almacén;una carretilla elevadora;un casco;un chaleco|¿Qué está haciendo el golden retriever?|Está manejando una carretilla elevadora en un almacén.
4251|señalar unos estantes vacíos;sonreír de oreja a oreja al hombre;mirar fijamente con incredulidad|un estante;un moño;calcetines;jerséis|¿Qué está señalando la mujer?|Está señalando los estantes vacíos.
4252|beber a sorbos una bebida naranja;fregar con un cepillo;extenderse por el hormigón|una piscina;una alfombra;espuma;hormigón|¿Qué se está extendiendo por el hormigón?|Se está extendiendo espuma jabonosa por el hormigón.
4253|estar sentado en una moto;limpiar el casco;lavar la moto|un casco;una gorra;una moto|¿Qué le está pasando a la moto?|Un hombre está lavando la moto.
4254|posarse en el mostrador;fulminar a la paloma con la mirada;flotar por el aire|una paloma;un gorro de cocinero;un delantal;un mostrador|¿Dónde está la paloma?|La paloma está posada en el mostrador metálico.
4256|rascarle el pecho al canguro;despatarrarse en la hierba;recostarse contra la mano|un canguro;una manga;el cielo;hierba|¿Qué está haciendo la mano?|Le está rascando el pecho al canguro.
4257|abrazar fuerte a la tortuga;recibir un gran abrazo;observar desde el agua|un panda;una tortuga;un pez;agua|¿Qué está haciendo el panda?|Está abrazando fuerte a la tortuga.
4258|ponerse de pie atropelladamente;reflejar el cielo pálido;alzarse sobre el prado|acero;un cervatillo;un prado;un bosque|¿Qué está haciendo el cervatillo?|Está tumbado en un tobogán de acero.
4259|abrir la boca;llevar una bufanda naranja;poner cara de enfado|una cara;una bufanda;el cielo;lana|¿Qué está haciendo la oveja?|Está poniendo cara de enfado.
4260|sonreír de oreja a oreja ante una tableta;descansar junto a su dueño;acechar en el umbral|una figura;una lámpara;una tableta;una manta|¿Quién está de pie en el umbral?|Una figura oscura está de pie en el umbral.
4261|empujar una pelota roja;nadar detrás de su amigo;flotar en el agua|un perro;una pelota;árboles;agua|¿Qué están haciendo los perros?|Están nadando en un día soleado.
4262|extender las alas;revolotear sobre los oseznos;alzarse sobre sus oseznos|un cuervo;oseznos;nieve;una ladera|¿Qué está haciendo el cuervo?|Está revoloteando sobre los oseznos.
4263|caminar por la tienda;ser el primero en abrir los ojos;ponerse rojo|un pájaro verde;un pájaro azul;estantes;el suelo|¿Qué están haciendo los dos pájaros pequeños?|Están admirando al pájaro rosa.
4264|volar por el aire;llevar pantalones blancos;llevar anillos de oro|un balón de voleibol;una mujer;un coche;nubes|¿Qué está haciendo la mujer?|Está jugando al voleibol en la carretera.
4266|correr por la playa;sacar la lengua;revolcarse boca arriba|un perro;el cielo;arena;hierba|¿Qué está haciendo el perro?|Está corriendo por la playa.
4267|sacar la lengua;cerrar los ojos con fuerza;sujetar la barbilla del perro|tijeras;una lengua;un césped;una mesa|¿Qué está haciendo el perro?|Está jadeando con la lengua fuera.
4268|estar sentado con una pelota;estar tumbado en el sofá;mostrar un partido de fútbol|un televisor;flores;tazas;una mesa|¿Qué está viendo el perro?|Está viendo un partido de fútbol.
4269|verter agua;llevar guantes de jardín;mojarse|una mujer;una jarra;una taza;una planta|¿Qué está haciendo la mujer?|Está vertiendo agua sobre la tierra seca.
4270|agarrar el volante;reducir la velocidad del kart;cruzar la pista anadeando|una pancarta;un pato;un volante;un neumático|¿Qué está haciendo el piloto?|El piloto está reduciendo la velocidad por un pato.
4271|empezar una carrera;correr muy rápido;dar pasos grandes|un atleta;el cielo;hierba;una pista|¿Qué está haciendo el atleta?|Está corriendo muy rápido.
4272|ponerse unos pendientes de oro;llevar un sombrero grande;llevar dos bolsos|un sombrero;un pañuelo;un cinturón;pantalones|¿Qué lleva puesto la mujer?|Lleva puesto un sombrero grande.
4274|agarrar el volante;subirse las gafas;chocar contra un coche|daños;un faro;el cielo;una luz trasera|¿Qué están haciendo el hombre y la mujer?|Están inclinados sobre el coche dañado.
4275|señalar el coche;recoger un trozo;escribir con un bolígrafo|una furgoneta;una mujer;una rueda;el cielo|¿Qué está haciendo la mujer?|Se está quejando del coche.
"""
out = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/es.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
