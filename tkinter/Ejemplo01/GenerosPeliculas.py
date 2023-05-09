class SubGeneros:
    
    def __init__(self,subgenero = "",text = ""):
        self.__subgenero = subgenero #Nombre
        self.__descripcion = text #Información

    def get_subgenero(self):
        return self.__subgenero 
    
    def get_descripcion(self):
        return self.__descripcion


class Generos:
    
    def __init__(self):
        self.__subgen = []#guardar los objetos subgénero
        self.__listsub = []#guardar los nombres

    def agregar_sub(self,subgeneros = SubGeneros()):
        
        self.__subgen.append(subgeneros)#Se agregan los objetos subgéneros
        self.__listsub.append(subgeneros.get_subgenero())#Se agrega solo el nombre del subgénero
        
    def get_list(self): #Obtener lista de los nombres de los subgéneros de cine
        return self.__listsub

    def get_inf(self,sub_gen): 
        for sub in self.__subgen:#Se revisan todos los subgeneros en la lista
            if sub.get_subgenero() == sub_gen:#si coinciden con el que buscamos 
                return sub.get_descripcion()#regresamos la inf



#Objetos de clasificación de genero de cine
estilo = Generos()
audiencia = Generos()
formato = Generos()
ambientacion = Generos()


###-------------------------------estilo-----------------------------------------------------------------------------
subest1 = SubGeneros("Acción", "Por lo general incluyen altas dosis de adrenalina y energía, con muchas acrobacias \
físicas y persecuciones, posiblemente con rescates, batallas, peleas, fugas, crisis destructivas \
(inundaciones, explosiones, catástrofes naturales, incendios, etc.), movimiento sin parar, ritmo \
espectacular, aventurero, a menudo con un personaje bueno que es el héroe o heroína de la película \
luchando contra los “chicos malos”.")
estilo.agregar_sub(subest1)

subest2 = SubGeneros("Aventura", "Suelen ser historias interesantes, con nuevas experiencias o lugares exóticos, a menudo muy \
similares a las películas de acción. Pueden incluir espadachines tradicionales, espectáculos históricos \
(similar al género de la película épica), búsquedas o expediciones de continentes perdidos, acción en la \
selva o el desierto, epopeyas, cazas del tesoro.")
estilo.agregar_sub(subest2)

subest3 = SubGeneros("Catástrofe", "Tienen como tema principal una catástrofe en curso o inminente para la raza humana; por ejemplo \
grandes incendios, terremotos, naufragios o una hipotética colisión de un asteroide contra la Tierra. \
Por lo general, traen consigo un amplio reparto de actores y múltiples líneas argumentales, y se centran \
en los intentos de los personajes de evitar, escapar o resistir las consecuencias de la catástrofe. Un \
personaje principal, varios menores y muchos extras suelen morir antes de la resolución de la historia.")
estilo.agregar_sub(subest3)


subest4 = SubGeneros("Ciencia Ficción","Utiliza representaciones especulativas basadas en la ciencia de fenómenos imaginarios como extraterrestres, \
planetas alienígenos y viajes en el tiempo, a menudo junto con elementos tecnológicos como naves \
espaciales futuristas, robots y otras tecnologías. El cine de ciencia ficción se ha utilizado en \
ocasiones para comentarios críticos de aspectos políticos o sociales, y la exploración de cuestiones \
filosóficas como la definición de ser humano.")
estilo.agregar_sub(subest4)

subest5 = SubGeneros("Comedia","Son alegres y deliberadamente diseñadas para divertir y provocar la risa con una línea sus líneas de diálogo \
y bromas, exagerando la situación, el lenguaje, la acción, las relaciones y los personajes. Su finalidad \
básica es entretener y causar risa entre los espectadores.")
estilo.agregar_sub(subest5)

subest6 = SubGeneros("Documentales","Indaga la realidad, plantea discursos sociales, representa historias particulares y colectivas, se \
constituye en archivo y memoria de las culturas pero tiene infinitas formas de hacerlo. Es la \
expresión de un aspecto de la realidad, mostrada en forma audiovisual. La organización y estructura \
de imágenes y sonidos (textos y entrevistas), según el punto de vista del autor, determina el tipo de \
documental.")
estilo.agregar_sub(subest6)

subest7 = SubGeneros("Drama","Se centran principalmente en el desarrollo de un conflicto entre los protagonistas, o del protagonista con \
su entorno o consigo mismo. Son serios, basan la trama en personajes realistas, escenarios, situaciones \
de la vida, y las historias que involucran el desarrollo del carácter y la interacción humana. Por lo \
general, no se centran en los efectos especiales, comedia, o acción,  las películas dramáticas son, \
probablemente, el género cinematográfico más grande, con muchos subconjuntos.")
estilo.agregar_sub(subest7)

subest8 = SubGeneros("Fantasía","Suelen incluir magia, mundos de fantasía exótica, o hechos, personajes o criaturas absolutamente irreales \
que de ningún modo pertenecen a la realidad conocida de nuestro mundo, en contraste con el cine de \
ciencia ficción o el cine de terror, que tienen o pueden tener una base realista o científica. Aunque \
en ocasiones también se utiliza el término 'fantástico' en su sentido más amplio para referirse a toda \
esta clase de cine en general.")
estilo.agregar_sub(subest8)

subest9 = SubGeneros("Musicales","Se caracteriza por películas que contienen interrupciones en su desarrollo, para dar un breve receso por \
medio de un fragmento musical cantado o acompañados de una coreografía. En los comienzos de este género, \
el fragmento musical tenía como objetivo impresionar, sin mantener mucha conexión con el desarrollo narrativo. \
Sin embargo, al alcanzar su madurez, se estilizó el género y los números concatenan la historia.")
estilo.agregar_sub(subest9)

subest10 = SubGeneros("Suspenso","Es básicamente una historia de intriga que se caracteriza por tener ritmo rápido, acción, héroes ingeniosos \
y villanos poderosos e influyentes. Posee un relato que tiene mayor consistencia y argumentación que otros \
géneros cinematográficos y su característica es que todos los elementos propios de un guion (personaje, \
antagonista, meta, conflicto, ritmo, etc.) están al servicio de una intriga, es decir al servicio de una acción \
que se ejecuta con astucia y ocultamente. También se las conoce como de 'Terror Inteligente'. Se utilizan técnicas \
como los cliffhangers ('ganchos' para que el público espere la próxima entrega: capítulo, episodios etc.). Así \
como la función del género de Terror es provocar un interés a través de emociones fuertes que ponen en estado \
de 'alerta' al público; el género suspenso quiere provocar un interés a través de la emoción, pero al mismo \
tiempo suma un interés de carácter mental; entonces una película de suspenso funciona en la medida de que \
emociona e interesa cognitivamente al espectador.")
estilo.agregar_sub(subest10)

subest11 = SubGeneros("Terror","Se caracteriza por su voluntad de provocar en el espectador sensaciones de pavor, miedo, disgusto, repugnancia, \
horror, incomodidad o preocupación. Sus argumentos frecuentemente desarrollan la súbita intrusión en un ámbito \
de normalidad de alguna fuerza, evento o personaje de naturaleza maligna, a menudo de origen criminal o \
sobrenatural. Toma elementos de fuentes de la literatura, supersticiones y leyendas tradicionales, así \
como de temores y pesadillas nacidos de contextos socioculturales mucho más actuales y precisos.")
estilo.agregar_sub(subest11)




###-------------------------------audiencia---------------------------------------------------------------------------
subaud1 = SubGeneros("Infantiles", "Son películas cuyo público meta en general son los niños. Poseen \
historias sencillas, finales felices y generalmente con alguna enseñanza implícita.")
audiencia.agregar_sub(subaud1)

subaud2 = SubGeneros("Juveniles", "Son películas cuyo público meta son adolescentes y adultos jóvenes principalmente. Los niños \
puede verlas pero la trama generalmente suele ser un poco complicada para los menores por lo que se \
recomienda la supervisión y orientación por parte de adultos")
audiencia.agregar_sub(subaud2)

subaud3 = SubGeneros("Adultos", "Son películas cuyo público meta son los adultos jóvenes y adultos en general, para mayores de \
edad o para ser vistas por jóvenes bajo la supervisión de adultos debido al contenido de violencia, \
de desnudos y/o actividades ilícitas.")
audiencia.agregar_sub(subaud3)

subaud4 = SubGeneros("Familiares", "Son películas que por su trama pueden ser vistas por toda la familia, con historias fáciles de entender, sin presencia de violencia \
y generalmente con finales felices")
audiencia.agregar_sub(subaud4)


###-------------------------------formato---------------------------------------------------------------------------
subfor1 = SubGeneros("Animación", "Películas compuestas de fotogramas dibujados a mano que, pasados rápidamente, producen ilusión \
de movimiento. También se incluyen aquí las películas generadas íntegramente mediante la informática.")
formato.agregar_sub(subfor1)

subfor2 = SubGeneros("Imágenes Reales", "En oposición a la animación, películas filmadas con actores reales, de “carne y hueso”.")
formato.agregar_sub(subfor2)

subfor3 = SubGeneros("Cine Mudo", "No posee sonido grabado y sincronizado, referido especialmente a diálogo hablado, consistiendo \
únicamente en imágenes.")
formato.agregar_sub(subfor3)


subfor4 = SubGeneros("Cine Sonoro", "Es aquel en el que la película incorpora sonido sincronizado, o sonido tecnológicamente \
aparejado con imagen.")
formato.agregar_sub(subfor4)

subfor5 = SubGeneros("Cine 2D", "Es el cine proyectado en dos dimensiones, ancho y altura, es la forma tradicional en la que \
vemos el cine, tanto en salas de exhibición como en televisión.")
formato.agregar_sub(subfor5)

subfor6 = SubGeneros("Cine 3D", "Es el cine proyectado en tres dimensiones, ancho, altura y fondo. Se ha popularizado mucho \
también la creación de películas animadas que utilizan 3D como tecnología.")
formato.agregar_sub(subfor6)

subfor7 = SubGeneros("Cine IMAX", "Es un sistema de proyección de cine creado por IMAX Corporation que tiene la \
capacidad de proyectar representaciones de mayor tamaño y definición que los sistemas convencionales de proyección. \
Aunque inicialmente se destinó casi exclusivamente para la proyección de documentales, en la actualidad también \
se emiten películas de cine convencional digitalmente transformadas a formato IMAX.")
formato.agregar_sub(subfor7)




###-------------------------------ambientacion----------------------------------------------------------------------
subamb1 = SubGeneros("Bélicas","Son películas que centran su historia en guerras. A mediados de esa década y ya en los 90 surge una \
nueva corriente, que deja un poco de lado el conflicto, que se convierte en el escenario y se centra en el soldado \
como persona, el cual tiene sentimientos y temores, además de numerosas dudas morales sobre la corrección de las \
acciones que se ve obligado a realizar. En este nuevo tipo de películas se observa la guerra y sus consecuencias \
con mucha mayor crueldad que en sus predecesoras, quién sabe si con la intención de aleccionar al espectador sobre \
la necesidad de que los conflictos armados queden únicamente en el cine y los libros de historia.")
ambientacion.agregar_sub(subamb1)

subamb2 = SubGeneros("Contemporáneas","Son películas temporalmente ambientadas en situaciones recientes o actuales de la sociedad.")
ambientacion.agregar_sub(subamb2)

subamb3 = SubGeneros("Crimen","Son películas que se centran en las vidas de los delincuentes. El enfoque estilístico a una \
película de la delincuencia varía de representaciones realistas de la vida real las figuras delictivas, \
a las obras descabelladas del mal de imaginarios archivillanos. Los actos criminales son casi siempre \
glorificados en estas películas.")
ambientacion.agregar_sub(subamb3)

subamb4 = SubGeneros("Deportivas","Son películas desarrolladas en entornos o acontecimientos relacionados con un deporte.")
ambientacion.agregar_sub(subamb4)

subamb5 = SubGeneros("Gangsters","Tiene como tema principal el crimen organizado. A diferencia de otros géneros \
cuyo tema central es el delito, en el cine de gángsters predomina el punto de vista del propio criminal, lo \
que hace que muchas de estas películas resulten moralmente ambiguas; en ocasiones, obras de este género han \
sido acusadas de glorificación de la violencia, por lo que han tenido frecuentes problemas con la censura.")
ambientacion.agregar_sub(subamb5)

subamb6 = SubGeneros("Históricas","Caracterizado por la ambientación en una época histórica determinada, \
tanto si los hechos y personajes representados son reales como si son imaginarios, pero verosímiles. Las \
películas históricas en algunas ocasiones son recreaciones cinematográficas de la biografía de algún \
personaje histórico relevante o adaptaciones de obras literarias. Una película de época puede utilizar \
la historia únicamente como un marco de ambientación para el desarrollo de cualquier argumento, por \
anecdótico o intrascendente que sea (cosa que puede ser precisamente lo que le proporcione su valor \
como recurso divulgativo o didáctico para la comprensión de esa época), o bien centrarse en la narración \
de un acontecimiento de gran importancia histórica (las únicas que en rigor son 'históricas',cosa que no \
garantiza ni su calidad ni su valor educativo).")
ambientacion.agregar_sub(subamb6)

subamb7 = SubGeneros("Policiacas","El argumento tiene generalmente una estructura sencilla, con introducción, \
desarrollo y desenlace. Usualmente al comienzo se ofrece al espectador los antecedentes de un grave crimen, \
acabando esta parte cuando efectivamente se comete dicho acto criminal y se arma el suspenso. El nudo de la \
historia pasa a ser la dura lucha de los estamentos policiales, normalmente a cargo de un duro y experimentado \
policía, contra quienes cometieron el delito. Finaliza tradicionalmente con la detención, o también muy \
frecuentemente con la muerte de quien violó la ley.")
ambientacion.agregar_sub(subamb7)

subamb8 = SubGeneros("Western","En principio una película se incluiría en este género simplemente por estar \
situada su acción en un contexto determinado: la exploración y el desarrollo del territorio occidental de los \
Estados Unidos durante el siglo XIX. Sin embargo con el tiempo las características de dicho contexto histórico \
se fueron extendiendo a los personajes de esas historias, condicionando su modo de vida y definiendo su \
idiosincrasia. Al estar las películas muchas veces ambientadas en territorios inexplorados o indómitos \
bajo la amenaza latente del ataque de los indios, o en ciudades sin ley en las que los bandidos campaban \
a sus anchas, el género se fue enfocando hacia la confrontación de los diversos personajes, adquiriendo \
un carácter cada vez más psicológico. Lo habitual es también que algunos de esos personajes representasen \
el bien sin ambages, aquella gente que viajaba esperanzada a esas tierras con la utopía de forjar un hogar \
y vivir en paz, y otros representasen por el contrario el lado malvado, aquellos que se aprovechaban de \
los indefensos para hacer su propia vida más fácil. Es por toda esta serie de temas fundamentales y rasgos \
comunes que no se considera necesario que una película esté ambientada en el oeste estadounidense para \
poder calificarla de western, aunque ello pueda ser siempre una apreciación algo sui generis.")
ambientacion.agregar_sub(subamb8)

subamb9 = SubGeneros("Religioso","on aquellas películas cuya temática y/u orientación está dirigida hacia \
dios, personajes bíblicos y otros conflictos que involucran la espiritualidad.")
ambientacion.agregar_sub(subamb9)

subamb10 = SubGeneros("Épicas","El término 'épico' se refiere a películas de larga duración, que a menudo \
centran su trama en tiempos de guerra o de conflictos y que suelen abarcar un amplio espacio de tiempo. Se \
suele hacer uso de un escenario histórico, aunque también se puede hacer uso de una ubicación de ficción. \
Normalmente, las películas épicas centran su trama en la consecución de una serie de metas o búsqueda, las \
cuales tienen que ser alcanzadas por un 'héroe' o por un grupo de personas.")
ambientacion.agregar_sub(subamb10)

subamb11 = SubGeneros("Futuristas","Caracterizado por la ambientación en una época futura, con hechos y \
personajes ficticios que pueden ser verosímiles o inverosímiles. Las películas futuristas están cargadas \
de elementos de inteligencia artificial, tecnología avanzada, formas de vida no conocidas, ambientación \
en lugares fuera del planeta o en una Tierra completamente distinta a la que conocemos. Frecuentemente \
las películas futuristas son clasificadas como ciencia ficción, sin embargo éstas deben estar ambientadas \
exclusivamente en el futuro, lo cuál no es una característica inherente de la ciencia ficción.")
ambientacion.agregar_sub(subamb11)
