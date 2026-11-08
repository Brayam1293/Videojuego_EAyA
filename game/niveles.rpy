# 
# NIVEL 1
# UN NUEVO DÍA
#


label nivel_1:

    scene black with fade

    "{cps=30}Las deciciones importantes deberian ser planeadas con tiempo y detenimiento."

    "{cps=30}Pero no todos tienen esa oportunidad."

    "{cps=30}Como es el caso de Valeria, una joven univercitaria a la que su vida dio un giro inesperado."

    "{cps=20}Por favor...{w=0.7} ayudala en lo que te sea posible..."

    pause 1.3

    # 
    # ESCENA 1 - MAÑANA APRESURADA
    # 

    scene bg fondo_casa with dissolve

    show valeria_bebe normal at pos(0.5, -0.3)
    with dissolve

    "{cps=30}Una nueva mañana comienza."

    v "{cps=30}Hoy tengo clases temprano."

    v "{cps=30}Debo prepararme antes de salir."

    v "{cps=30}Revisare que tenga todo en mi mochila."

    v "{cps=10}..."

    show valeria_bebe preocupada at pos(0.5, -0.3)

    v "{cps=30}Oh no{w=0.6}, olvide hacer la tarea para hoy!."

    v "{cps=30}Talvez si me apresuro pueda terminarla."

    b "{cps=30}snif, snif..."

    show valeria_bebe llorando at pos(0.5, -0.3)

    b "{cps=30}!bua, buaa!"

    v "{cps=30}Ay no, ¿qué tienes bebé?..{p=0.6} ¿Qué paso?.."

    #
    # DECISION 1
    #

    menu:

        v "{cps=30}¿Qué se supone que deberia hacer ahora?..."

        "Centrarme en terminar mi tarea.":

            $ estudios += 1
            $ tareaPendiente = False
            $ estres += 1

            v "{cps=30}Perdoname bebé pero debo terminar esto, en un momento te atiendo ¿esta bien?"

            "{cps=30}Valeria termino su tarea a las prisas, pero su bebé no paró de llorar hasta un rato despues"

            show valeria_bebe triste at pos(0.5, -0.3)

            v "{cps=30}Menos mal, porfin se calmó."

            v "{cps=30}Ya casi es hora de irme."

        "Atender al bebé primero.":

            $ cuidado_bebe += 1

            v "{cps=30}Supongo que puedo hacer que deje de llorar primero."

            v "{cps=30}Despues de eso hago la tarea."

            "{cps=30}El bebé no paraba de llorar por mas que Valeria lo intentaba."

            "{cps=30}Cuando porfin se calmó, Valeria se dio cuenta de cuanto tiempo habia pasado."

            show valeria_bebe preocupada at pos(0.5, -0.3)

            v "{cps=30}Ay no, ya es tarde y no alcance a hacer la tarea que me faltaba."

            v "{cps=30}Debo darme prisa."

        "Hacer ambas cosas a la vez.":

            $ estres += 2

            v "{cps=30}No tengo mucho tiempo, tendre que hacer ambas cosas a la ves."

            v "{cps=30}Aver bebé, calmate porfavor.."

            "{cps=30}Por mas que intentaba el bebé no ceso su llanto."

            "{cps=30}Y por no tener su atencion en la tarea no pudo terminarla a tiempo."

            show valeria_bebe llorando at pos(0.5, -0.3)

            b "{cps=30}{size=35}!Bua, bua!"

            v "{cps=30}Oh no, ya es tarde y no eh terminado nada aun."

            v "{cps=30}No hay de otra, tendre que irme asi."

            v "{cps=30}Por favor ya calma bebé, estoy aqui contigo vez..."

            "{cps=30}El bebé ceso su llanto poco despues de esto."

            show valeria_bebe triste at pos(0.5, -0.3)

            v "{cps=30}Menos mal...{w} Ya queda poco tiempo."

    #
    # ESCENA 1:2 - PREPARANDOSE PARA SALIR
    #

    menu:

        v "{cps=30}Muy bien{w}, ¿Qué deberia hacer antes de salir?"

        "Preparar mis cosas para la universidad.":

            $ objValeria = True
            $ estudios += 1

            show valeria_bebe normal at pos(0.5, -0.3)

            v "{cps=30}Primero deberia preparar mis cosas para la univercidad."

            v "{cps=30}Quiero llegar preparada a clase."

            "{cps=30}Valeria se aseguro de tener todo listo para la universidad."

            v "Bien, ya tengo todo listo."

        "Organizar las cosas del bebé.":

            $ objBebe = True
            $ cuidado_bebe += 1

            show valeria_bebe normal at pos(0.5, -0.3)

            v "{cps=30}Antes de salir quiero asegurarme de que tengo todo lo del bebé."

            v "{cps=30}Después podré concentrarme en mis clases."

            "{cps=30}Valeria preparo todo lo que el bebé podria necesitar."

        "Preparar ambas cosas.":

            $ objAmbos = True

            show valeria_bebe normal at pos(0.5, -0.3)

            v "{cps=30}Creo que puedo prepararlo todo, no deberia de tardar mucho ¿no?"

            "{cps=30}Valeria alisto las cosas para la escuela y para el bebé."

            v "{cps=30}Bien creo que eso deberia ser todo."

            show valeria_bebe sorprendida at pos(0.5, -0.3)

            v "{cps=30}¡No habia visto la hora!, ya es muy tarde."

            v "{cps=30}Debo darme prisa."

    if objAmbos == True:
        show valeria_bebe preocupada:
            linear 2.0 xalign 2.5 yalign -3.0

        "{cps=30}Valeria salio rapidamente de su casa camino a la escuela y logro calmarse un poco."
    else:
        v "{cps=30}Ahora sí, podemos irnos."

        show valeria_bebe normal:
            linear 3.0 xalign 2.5 yalign -3.0

    pause 1.2

    #
    # ESCENA 2 - TRAYECTO A LA UNIVERCIDAD
    #

    scene bg fondo_trayecto
    with fade

    show valeria_bebe normal at move_derecha(-860, -0.3, 5.0, 800)

    "{cps=30}Durante su trayecto Valera no paraba de escuchar murmullos a su alrededor y sentir que la miraban."

    show valeria_bebe incomoda

    pv "{cps=30}¿Porque siempre murmuran tanto?."

    pv "{cps=25}Tampoco dejan de mirarme hoy tambien.."

    pv "{cps=25}¿Porque no puedo ir tranquila a la univercidad al menos una vez."

    b "{cps=30}Mmm, ma.. maa.."

    v "{cps=30}jeje, tienes razon bebé, no podemos quedarnos aqui, tenemos que llegar a clases."

    c "{cps=30}Hola."

    v "{cps=30}Ah emm{w=0.5}, hola{cps=25}...{w=0.3}"

    v "{cps=30}Disculpa pero, ¿nos conocemos o algo?"

    v "{cps=30}La verdad es que no lo recuerdo."

    c "{cps=30}A no, disculpa no me he prensentado."

    $ name_npc = "Herneztino" # NOMBRE PROPUESTO POR RAMON EDUARDO
    c "{cps=30}Me llamo Herneztino, estamos en la misma clase."

    v "{cps=30}A si perdona, mucho gusto yo soy Valeria."

    pv "{cps=30}No me suena de nada.."

    v "{cps=30}Y.. Puedo hacer algo por tí?"

    c "{cps=30}No no, perdona, de hecho queria preguntarte eso mismo a ti, ¿hay algo con lo que necesites ayuda?"

    v "{cps=30}¿Y eso porque?, no nos conocemos siquiera.."

    c "{cps=30}Si lo se, es solo que siempre veo que pasas por aqui cargando con todo lo de tu bebé."

    c "{cps=30}Supuse que tal vez te vendria bien un poco de ayuda."

    c "{cps=30}Asi que, ¿necesitas ayuda con algo?"

    pv "{cps=30}No entiendo, ¿porque me ayudaria asi sin más?.."

    pv "{cps=30}Todos parecen incomodos con que lleve a mi bebé a la universidad.{w=0.8} ¿Porque a el parece no importarle?"

    menu:

        pv "{cps=30}¿Qué deberia hacer?"

        "Rechazar su ayuda.":

            v "{cps=30}No gracias, puedo hacerlo por mi misma."

            v "{cps=30}Solo te quitaria tiempo."

            c "{cps=30}No te preocupes por eso."

            c "{cps=30}Quisiera ayudarte, ya que siempre veo que llevas las cosas de tu bebé"

            c "{cps=30}Ademas de las tuyas que necesitas en la univercidad."

            v "{cps=30}Gracias pero estoy bien asi.."

            pv "{cps=30}Debo ser capaz de hacerlo yo misma.."

            pv "{cps=30}Es mi bebé despues de todo.{p=0.3}No deberia de hacer que afecte la rutina de otros.."

            pv "{cps=30}Ademas no lo conosco de nada."

            c "{cps=30}Okey, si tu lo dices esta bien."

            c "{cps=30}Supongo que nos vemos luego entonces."

        "Afirmar que no es necesario.":

            v "{cps=30}No es necesario, de verdad. No quisiera molestarte con mis cosas."

            c "{cps=30}No te preocupes por eso. De todas formas, tambien voy a la universidad."

            pv "{cps=30}No lo entiendo.. ¿Deberia aceptar?... Apenas lo conozco. Pero parece que realmente intenta ayudar."

            c "{cps=30}Ademas, no es necesario que lo lleves todo tu sola."

            c "{cps=30}Podria ayudarte a llevar la pañalera si quieres."

            pv "{cps=30}No quisiera molestarlo con esto.. seguramente tambien tenga sus propios asuntos."

            pv "{cps=30}Pero es cierto que me cansa llevar siempre la pañalera cargando.."

            menu:

                pv "{cps=30}¿Debería aceptar su ayuda?.."

                "Insistir en negarte":

                    v "{cps=30}De verdad, estoy bien asi.."

                    v "{cps=30}Pero muchas gracias."

                    c "{cps=20}..."

                    c "{cps=30}Okey, si asi lo quieres esta bien."

                    c "{cps=30}Pero recuerda que mi oferta sigue en pie jeje."

                    c "{cps=30}Bueno, nos vemos en la univercidad entonces."

                "Aceptar su ayuda":

                    $ aceptarAyuda = True
                    $ valeriaDuda = True

                    v "{cps=30}Bueno..."

                    v "{cps=30}Pues, supongo que si estaria bien.. ya que insistes."

                    "{cps=30}Valeria accedio a darle la pañalera a Herneztino."

                    v "{cps=30}Gracias.."

                    c "{cps=30}Con gusto."

                    c "{cps=30}Bueno vamos, no queremos llegar tarde jaja."

                    v "{cps=30}Si jaja, vamos."

                    jump Cap1_aceptarAyuda

        "Aceptar su ayuda.":

            $ aceptarAyuda = True

            pv "{cps=25}..."

            pv "{cps=30}Está bien.."

            v "{cps=30}Emm, okey.."

            v "{cps=30}Está bien, muchas gracias por la ayuda."

            c "{cps=30}Claro sin problema, te puedo ayudar con la pañalera."

            v "{cps=30}Si, gracias."

            "{cps=30}Valeria decidio dejar que su compañero la apoyara a llevar algunas cosas."

            jump Cap1_aceptarAyuda

    
    v "{cps=30}Si claro..{p=0.5}Nos vemos."

    "{cps=30}El chico siguio su camino dejando atras a Valeria."

    v "{cps=30}Eso fue muy raro."

    b "{cps=30}Mma.. mammh"

    v "{cps=30}Si verdad, tu si me entiendes nene jaja."

    v "{cps=30}Bueno bebé, ahora si vayamonos a la universidad."

    "{cps=30}Valeria continuo con su camino."

    # Cambio de escena a la universidad

    v "{cps=30}Fuf.."

    v "{cps=30}Bien, creo que aun alcanzo a llegar a la clase."
    
    pv "{cps=30}Aunque sigo pensando en la oferta de ese chico..{w=0.4} Tal vez debi haber aceptado.."

    pv "{cps=30}No, no es momento para pensar en eso."

    pv "{cps=30}Ahora debo consentrarme en la escuela."

    pv "{cps=30}Debo demostrarles que puedo hacerlo.."

    v "{cps=30}Démonos prisa bebé, que apenas comienza el día."

    v "{cps=30}Vamos con todo!"

    if aceptarAyuda == True:
        label Cap1_aceptarAyuda:

        $ estres -= 1
        "{cps=30}Valeria y Herneztino se fueron juntos a la universidad."

        "{cps=30}Valeria y Hernestino se la pasaron hablando durante el trayecto."

        # Cambio de escena a la universidad

        c "{cps=30}Jaja si, despues de que eso estuve forcejeando con mi perro para poder quitarselo."

        v "{cps=30}Jajaja, me lo creo, tuve un perro hace tiempo y me la pasaba quitandole mis cosas."

        pv "{cps=30}Es bastante agradable, hacia tiempo que no me reia así."

        v "{cps=30}Bueno, parece que ya llegamos, muchas gracias por todo."

        c "{cps=30}Gracias a ti, fue muy agradable charlar contigo."

        c "{cps=30}Bien, ya tengo que irme, mis clases estan por empezar."

        c "{cps=30}Nos vemos luego."

        v "{cps=30}Si, nos vemos."

        pv "{cps=30}La verdad eso fue bastante mejor de lo que esperaba.."

        pv "{cps=30}Pero sige sin gustarme quitarle su tiempo a otros.."

        v "{cps=30}Bueno ya, debo apresurarme para ir a clase."

        v "{cps=30}Andando bebé!"

    #
    # ESCENA 3 - EN LA UNIVERCIDAD
    #    
    
    "{cps=30}Cuando Valeria llego a la clase todos sus compañeros ya estaban alli."

    # Cambio de escena a el salon de clase

    v "{cps=30}Buen día maestro, disculpe la demora. ¿Puedo pasar?"

    ms "{cps=30}Claro adelante, tóme asiento."

    # Valeria toma asiento

    ms "{cps=30}Buen día clase, ya que estamos tan cerca de las evaluacioes"

    ms "{cps=30}El dia de hoy solo revisaremos los pendientes."

    if tareaPendiente = True:

        pv "{cps=30}Oh no, no llegue a terminarla en la mañana!."

    else:

        pv "{cps=30}Menos mal que la termine antes de venir."

        pv "{cps=30}Me quite un peso de ensima."
    
    ms "{cps=30}Solo para recordarles, revisare tanto las preguntas y el resumen juntos."

    ms "{cps=30}Tienen solo esta clase para poder entregarlas."

    if tareaPendiente = True:
        
        pv "{cps=30}¡No puede ser! ¿son 2?"

        pv "{cps=30}¡No podre terminarlas a tiempo!"

        pv "{cps=15}..."

        pv "{cps=30}¡NO!"

        pv "{cps=30}No mientras siga pensando asi."

        pv "{cps=30}Tengo hasta que acabe la clase, asi que debo intentarlo."

    else:

        pv "{cps=30}¿Qué?, ¿habia otra?"

        pv "{cps=30}Esa aun no la he hecho."

        pv "{cps=30}Bueno, tengo esta clase para entregarla. Spongo que puedo terminarla antes que de eso."

        pv "{cps=30}Bien, hagamoslo Valeria, si se puede!."

    #
    # Minijuago (Si alcansa el tiempo)
    #

    if resumenTerminado == True && ayudaClase == True:

        $ estudios += 2
        $ resClase = 1

        v "{cps=30}¡Bien, lo logramos! Muchisimas gracias."

        v "{cps=30}Creo que no lo habria logrado sin tu ayuda."

        c "{cps=30}No me agradezcas me alegra ayudar."

        c "{cps=30}Ademas este pequeño es un encanto."

        c "{cps=30}A que si bebé?"

        b "{cps=30}Mmha mmhm"

        v "{cps=30}Jaja, si tienes razón."

        v "{cps=30}Bueno, vayamos a revisar."

        c "{cps=30}Si, vamos."

        jump resultadosClase

    else if resumenTerminado == False && ayudaClase == True:

        $ estres += 1
        $ resClase = 2

        v "{cps=30}No puede ser.. {w=0.4}No logre terminarlo..."

        v "{cps=30}No se porque pense que si podria.."

        c "{cps=30}..."

        c "{cps=30}Vamos no digas eso, solamente te falto un poco mas de tiempo."

        c "{cps=30}Ademas, aun puedes rescuperarte con el examen no?"

        v "{cps=30}Si, bueno...{w=0.4} Tal vez."

        c "{cps=30}Entonces no te angusties tanto."

        c "{cps=30}Todavia tienes una oportunidad más."

        c "{cps=30}¡Arriva esos animos!"

        v "{cps=30}Je je, si, supongo que tienes razón."

        ms "{cps=30}Disculpe, Valeria ¿verdad?"

        v "{cps=30}A este. Si, soy yo."

        ms "{cps=30}Okey, venga conmigo un momento porfavor."

        v "{cps=30}Si, claro.."

        jump resultadosClase

    else if resumenTerminado == True && ayudaClase == False:

        $ estudios += 2
        $ resClase = 3

        v "{cps=30}¡Wow!, de verdad no puedo creer que lo lograra."

        v "{cps=30}Fue mucho mas dificil de lo que esperaba."

        v "{cps=30}¿Desde cuando puedo escribir tan rapido?"

        v "{cps=30}No espera, concentrate Valeria, hay que ir a revisar con el maesto."

        pv "{cps=30}Bien, si sigo asi, no hay duda de que lo lograre."

        pv "{cps=30}Ya lo verán."

        jump resultadosClase

    else: resumenTermindo == False && ayudaClase == False:

        $ estres += 2
        $ resClase = 4

        pv "{cps=30}No puede ser..."

        pv "{cps=30}No pude lograrlo.. No fui capaz.."

        pv "{cps=30}A este paso.. {w=0.4}Yo..."

        ms "{cps=30}Disculpe. ¿Es usted Valeria?"

        v "{cps=30}A, si disculpe.. ¿necesita algo?"

        ms "{cps=30}¿Podria acompañarme? Necesito hablar de algo con usted."

        v "{cps=30}S-si, claro.. Ahora voy."

        jump resultadosClase
    
    label resultadosClase:
        if resClase == 1: # Completado con ayuda

            v "{cps=30}Maestro, aqui estan las activdades."

            ms "{cps=30}Muy bien, ahora mismo tienes buenas chances de pasar."

            ms "{cps=30}Me alegra ver que te llevas bien con tu compañero."

            v "{cps=30}Si, supongo que si. Me ha ayudado mucho."
            
            ms "{cps=30}Eso esta bien, me alegro por tí."

            ms "{cps=30}Bueno, con esto entregado bastará con que tengas una nota aprobatoiria en el examen."

            ms "{cps=30}Y deberias pasar con eso, asi que deberias relajarte un poco."

            ms "{cps=30}Se ve que has estado algo estresada."

            v "{cps=30}Si gracias, pero estoy bien por ahora."

            v "{cps=30}Muchas gracias Maestro."

            "{cps=30}Valeria entregó las tareas a tiempo."

        else if resClase == 2: # No Completado con ayuda

            ms 

        else if resClase == 3: # Completado sin ayuda

        else: # No completado sin ayuda



    # 
    # DECISIÓN 3
    # 

    menu:

        "¿Qué hará Valeria durante el descanso?"

        "Estudiar para el siguiente examen.":

            $ estudios += 1
            $ decisiones_nivel_1 += 1

            show valeria_bebe normal:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Tengo que aprovechar este momento para estudiar."

            v "Aunque sea difícil, quiero seguir avanzando."

        "Pasar tiempo con el bebé.":

            $ cuidado_bebe += 1

            show valeria_bebe feliz:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Quiero pasar un rato contigo."

            v "Estos momentos también son importantes."

        "Descansar un momento.":

            show valeria_bebe normal:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Necesito respirar un poco."

            v "También necesito cuidar de mí misma."


    # 
    # FINAL DEL NIVEL 1
    # 

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    v "Tal vez no sea fácil..."

    v "Pero quiero seguir adelante."

    v "Por mi bebé y por mí."

    narrador "Fin del Nivel 1."

    pause 1.0

    scene bg fondo_marco with fade

    pause 0.5

    call screen separador_nivel(
        "02",
        "Memorias del Pasado",
        "El peso de la responzabilidad"
    )

    jump nivel_2

label nivel_2:

    "Algunas antiguas memorias regresan a la mente Valeria."

    pause 1.0

    scene bg fondo_universidad

    show flashback_exnovio amor

    "Antes de convertirse en madre, Valeria otros planes para su vida."

    "Tenia aproximadamente veinte años y llevaba varios de ellos en una relacion."

    "Su novio estudiaba medicina."

    v "En ese momento pensaba que nuestro futuro seria estando juntos."

    v "Eramos jovenes y teniamos muchos sueños"

    scene black with dissolve

    "Pero todo comenzo a cambiar cuando Valeria descubrio que estaba embarazada."

    "Aquella noticia cambio sus planes y tambie su relacuion."

    v "Estoy embarazada..."

    v "Que se supone que haga ahora?..."

    "Valeria estaba asustada, pero sabia que debia enfrentar lo que estaba sucediendo."

    #
    # Decicion 4
    #

    menu:

        "¿Que decide hacer valeria ahora?"

        "Continuar con sus estudios y enfrentar la situacion.":

            $estudios += 1

            v "Debo seguir estudiando"

            v "No abandonare mis sueños asi sin más"

            "Valeria decidio que aunque tendra nuevos retos, queria continuar con su carrear."

        "Concentrarse primero en ser mamá.":

            $cuidado_bebe += 1

            v "Ahora necesito pensar en mi bebe."

            v "Quiero prepararme para todo lo que viene."

            "Valeria decidio concentrarse en su nueva responsabilidad."

    "Pero la noticia del embarazo tambien cambniara la relacion de Valeria con su familia."

    "Muy pronto tendra que regresar a casa de sus padres."

    "Fin del capitulo 2."

    call screen separador_nivel(
        "03",
        "Confrontacion",
        "Regresar a Casa"
    )

    jump nivel_3

label nivel_3:

    # ESCENA 1 - REGRESAR A CASA

    scene black with fade

    pause 0.3

    "{cps=25}Despues de descubrir su enbarazo Valeria decidio regresar a la casa de sus padres en busca de ayuda y consejo.{/cps}"

    "{cps=20}Esperaba encontrar comprención y apoyo durante uno de los momentos mas importantes de su vida.{/cps} {w}Pero..."

    scene bg fondo_casa_padres with dissolve

    show valeria deprimida:
        xalign 0.2
        yalign -0.3

    show padres normal:
        xalign 0.9
        yalign -0.3

    v "{cps=30}Mamá,{w=1.0} Papá...{w=1.5} Necesito hablar con ustedes{/cps}"

    v "{w=1.0}.{w=1.0}.{w=1.0}."

    v "{cps=30}Estoy embarazada."

    "{cps=30}La preocupacion de sus padres se veia en su mirada."

    "{cps=30}Su madre deseaba que Valeria pudiera construir un futuro diferente."
    
    "{cps=30}Aunque estaba preocupada queria apoyar a su hija."

    "{cps=20}Sin embargo..."

    show padres preocupados:
        xalign 0.9
        yalign -0.3

    p "{cps=50}{size=50}¡¿Que?!{/size}"

    show valeria preocupada:
        xalign 0.2
        yalign -0.3

    "{cps=30}El shock de la noticia hizo que su padre no pensara correctamente.."

    p "{cps=50}{size=40}¡¡¿En que estabas Pensando?!!"

    m "{cps=30}Cariño por favor, calmate."

    "{cps=30}Valeria intento explicarse. Pero sin exito."

    v "{cps=30}Porfavor, Papá.. Dejame explicart--"

    p "{cps=50}{size=40}¡¿Siquiera conocemos a ese chico?!"

    p "{cps=50}{size=40}¿Quien se supone que es?"

    m "{cps=30}Cariño por favor, deja que nos explique..."

    v "{cps=30}Papá por favor escuchame"

    p "{cps=50}{size=40}¡No hay nada que escuchar!"

    p "{cps=50}{size=40}¡Si se creen suficientemente grandes para tener un hijo entonces esta claro que no hay necesidad de que te quedes en esta casa!"

    v "{cps=20}Pero{/cps}{w=0.6} {cps=10}Papá.."

    m "{cps=40}¡Cariño por favor, sabes que esto no esta bien, piensa con claridad!"

    "{cps=30}Sin embargo...{p=1.3}Su padre no cambio de opinion."

    show valeria triste:
        xalign 0.2
        yalign -0.3

    v "{cps=30}¿De verdad quieres que me vaya?..."

    v "{cps=30}Soy tu hija..."

    show padres tristes:
        xalign 0.9
        yalign -0.3

    p "{cps=10}..."

    p "{cps=15}Ya me oíste..."

    "{cps=30}Su madre queria detenerla{w=0.7}, pero no logro cambiar la decicion de su esposo."

    pv "{cps=25}¿Qué se supone que haré ahora?..."

    pv "{cps=25}Tengo miedo..{w} {cps=35}Pero debo pensar en mi bebé y en mi futuro"

    # ESCENA 4 - DECICION DE VALERIA

    scene bg Black with dissolve

    p "{cps=15}¿Qué es lo que he hecho?{cps=10}..."

    p "{cps=15}Mi querida hija vino aqui por ayuda y solo la deje a su suerte..."

    p "¿Qué clase de padre soy?..."

    scene bg fondo_parque with dissolve

    "{cps=30}Lejos de la casa de sus padres{w}, Valeria intentó ordenar sus pensamientos."

    "{cps=30}Tenia muchas dificultades por delante, pero todavia podia decidir como enfrentarlas."

    menu:

        "¿Qué deberia hacer Valeria?"

        "Continuar luchando por sus estudios.":

            $estudios+=1

            v "{cps=30}No voy a abandonar mi carrera."

            v "{cps=30}Quiero demostrar que puedo ser una buen madre y continuar con mis estudios."

            "{cps=35}Valeria decidio seguir trabajando por el futuro que deseaba."

        "Concentrarse priemero en la seguridad de su bebé.":

            $cuidado_bebe+=1

            v "Mi bebé necesita que esté bien."

            v "Voy a buscar la manera de salir adelante, {w=0.5}paso a paso."

            "Valeria decidió priorizar la estabilidad de su nueva familia."

    # FINAL DEL NIVEL 3

    "Aquel dia, Valeria comprendio que su camino no seria sencillo."

    "Pero todavia tenia sueños por cumplir y un futuro por construir."

    "Fin del nivel 3."

    call screen separador_nivel(
        "04",
        "a",
        "a"
    )


    jump nivel_4

# NIVEL 4
# ENTRE ESTUDIOS Y MATERNIDAD

label nivel_4:

    # ESCENA 1 - UNA NUEVA MAÑANA EN CASA

    scene bg fondo_casa
    with fade

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Después de dejar la casa de sus padres, Valeria tuvo que aprender a organizar su nueva vida."

    narrador "Cada día era un reto: cuidar de su bebé, estudiar y encontrar tiempo para descansar."

    v "Tengo muchas cosas que hacer hoy."

    v "Debo estudiar para mi examen y preparar todo lo que necesita mi bebé."

    v "A veces siento que no me alcanza el tiempo, pero quiero continuar con mi carrera."

    # ESCENA 2 - PRIMERA DECISION

    menu:

        "¿Qué hará Valeria primero?"

        "Organizar sus apuntes y estudiar un poco.":

            $ estudios += 1

            v "Voy a aprovechar este momento para repasar mis apuntes."

            v "Cada pequeño avance me acerca a terminar mi carrera."

        "Preparar las cosas que necesita su bebé.":

            $ cuidado_bebe += 1

            v "Primero voy a revisar que tenga todo lo necesario."

            v "Quiero que esté bien antes de comenzar mis actividades."

    # ESCENA 3 - MOMENTO DIFICIL

    show valeria_bebe llorando:
        xalign 0.5
        yalign -0.3
    with dissolve

    v "Tranquilo, pequeño. Mamá está aquí."

    narrador "Mientras Valeria intentaba organizar sus pendientes, su bebé comenzó a llorar."

    narrador "Valeria sabía que también necesitaba atender sus propias necesidades y administrar bien su tiempo."

    # ESCENA 4 - SEGUNDA DECISION

    menu:

        "¿Cómo enfrenta Valeria la situación?"

        "Atender al bebé y después continuar estudiando.":

            $ cuidado_bebe += 1

            show valeria_bebe feliz:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Primero voy a asegurarme de que estés bien."

            v "Después buscaré otro momento para estudiar."

            narrador "Valeria comprendió que podía reorganizar sus actividades sin abandonar sus objetivos."

        "Tomarse un momento para organizar sus pendientes.":

            $ estudios += 1

            show valeria_bebe normal:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Necesito organizar mejor mi tiempo."

            v "Voy a dividir mis tareas para avanzar poco a poco."

            narrador "Valeria decidió buscar una forma más equilibrada de cumplir con sus responsabilidades."


    # ESCENA 5 - UNIVERSIDAD

    scene bg fondo_universidad
    with fade

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    v "Ya estamos en la universidad."

    narrador "Valeria llegó a clases con sus apuntes y todo lo necesario para cuidar de su bebé."

    v "Quiero aprender y terminar mi carrera."

    v "Sé que habrá días difíciles, pero no quiero rendirme."

    # ESCENA 6 - TERCERA DECISION

    menu:

        "¿Qué hará Valeria durante el descanso?"

        "Repasar para su próximo examen.":

            $ estudios += 1

            v "Voy a repasar los temas más importantes."

            v "Cada esfuerzo cuenta para alcanzar mi meta."

        "Pasar un momento tranquilo con su bebé.":

            $ cuidado_bebe += 1

            show valeria_bebe feliz:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Quiero disfrutar este momento contigo."

            v "Mi tiempo contigo también es importante."

    # ESCENA 7 - REFLEXION FINAL

    scene bg fondo_parque
    with fade

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Al terminar el día, Valeria pensó en todo lo que había vivido."

    v "No siempre puedo hacer todo en un solo día."

    v "Estoy aprendiendo a organizarme y a pedir ayuda cuando la necesito."

    v "Ser mamá es una parte importante de mi vida, pero mis sueños también lo son."

    v "Voy a seguir adelante, paso a paso."

    # FINAL DEL NIVEL 4

    scene black
    with fade

    narrador "Valeria comprendió que avanzar no significa hacerlo todo perfectamente."

    narrador "Lo importante era continuar construyendo el futuro que deseaba para ella y su bebé."

    narrador "Fin del Nivel 4."

    pause 1.0

    jump nivel_5

# NIVEL 5
# MI DECISION

label nivel_5:

    # ESCENA 1 - REFLEXION EN EL PARQUE

    scene bg fondo_parque
    with fade

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Han pasado varios días desde que Valeria comenzó a organizar su nueva vida."

    narrador "A pesar de las dificultades, ha seguido asistiendo a la universidad y cuidando de su bebé."

    v "He pasado por momentos muy difíciles."

    v "A veces tengo miedo de no poder con todas mis responsabilidades."

    v "Pero también sé que quiero construir un buen futuro para mi bebé y para mí."

    narrador "Valeria comprende que no tiene que resolver toda su vida en un solo día."

    narrador "Ahora debe decidir cómo quiere continuar su camino."

    # ESCENA 2 - DECISION FINAL

    menu:

        "¿Qué decisión tomará Valeria para su futuro?"

        "Seguir adelante con sus estudios.":

            $ estudios += 1

            jump final_seguir_adelante

        "Tomarse un tiempo para organizar su vida.":

            jump final_necesito_tiempo

        "Aceptar ayuda y continuar con sus sueños.":

            jump final_no_estoy_sola

# FINAL 1 - SEGUIR ADELANTE

label final_seguir_adelante:

    scene bg fondo_universidad
    with fade

    show valeria_bebe feliz:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Valeria decidió continuar con su carrera de Ingeniería."

    v "Sé que el camino no será fácil."

    v "Tendré que organizar mi tiempo y esforzarme cada día."

    v "Pero no quiero renunciar a mis sueños."

    narrador "Valeria comprendió que ser madre y estudiante implicaba grandes retos, pero estaba dispuesta a seguir aprendiendo."

    v "Quiero que mi bebé crezca sabiendo que nunca debemos dejar de luchar por lo que queremos."

    scene black
    with fade

    narrador "FINAL 1: SEGUIR ADELANTE"

    narrador "Valeria continúa sus estudios y trabaja por el futuro que desea para ambos."

    return

# FINAL 2 - NECESITO TIEMPO

label final_necesito_tiempo:

    scene bg fondo_casa
    with fade

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Valeria decidió tomarse un tiempo para organizar sus responsabilidades."

    v "Necesito aprender a cuidar de mí misma y de mi bebé."

    v "No quiero abandonar mi carrera, pero también debo reconocer cuándo necesito descansar."

    narrador "Valeria comprendió que avanzar a su propio ritmo también era una forma de seguir adelante."

    v "Mis sueños seguirán ahí. Voy a prepararme para retomarlos cuando esté lista."

    scene black
    with fade

    narrador "FINAL 2: NECESITO TIEMPO"

    narrador "Valeria decide priorizar su bienestar y el de su bebé, sin renunciar definitivamente a sus estudios."

    return

# FINAL 3 - NO ESTOY SOLA

label final_no_estoy_sola:

    scene bg  fondo_parque
    with fade

    show valeria_bebe feliz:
        xalign 0.5
        yalign -0.3
    with dissolve

    narrador "Valeria comprendió que no tenía que enfrentar todas las dificultades por sí sola."

    v "Durante mucho tiempo pensé que debía resolverlo todo sin ayuda."

    v "Ahora entiendo que pedir apoyo no me hace menos capaz."

    narrador "Valeria decidió buscar apoyo de personas de confianza y continuar trabajando por sus metas."

    v "Quiero terminar mi carrera y darle a mi bebé un futuro lleno de oportunidades."

    narrador "Con una nueva perspectiva, Valeria comenzó a mirar el futuro con esperanza."

    scene black
    with fade

    narrador "FINAL 3: NO ESTOY SOLA"

    narrador "Valeria acepta que recibir apoyo puede ayudarla a continuar sus estudios y cuidar de su bebé."

    return
