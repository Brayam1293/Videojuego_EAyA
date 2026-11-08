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

            ms "{cps=30}Bueno Valeria, sin tener estas actividades."
             
            ms "{cps=30}Me temo que te será complicado pasar."

            ms "{cps=30}Tendras que sacar una nota muy alta para poder compensar."

            v "{cps=30}Si.. Lo se."

            v "{cps=30}Me esfrozaré."

            ms "{cps=30}Creo que deberias descansar por hoy."

            ms "{cps=30}Te vez cansada."

            v "{cps=30}Estoy bien, necesito estudiar para poder pasar.."

            ms "{cps=30}Como gustes, recuerda que si necesitas ayuda, esta escuela ofrece servicios de psicopedagogia para el alumnado."

            ms "{cps=30}Tal vez la psicologa te pueda dar algun consejo."

            v "{cps=15}..."

            v "{cps=30}Lo pensaré.."

            "Valeria no logró entregar las tareas a tiempo."

        else if resClase == 3: # Completado sin ayuda

            v "{cps=30}Maestro, aqui estan las activdades."

            ms "{cps=30}Muy bien, ahora mismo tienes buenas chances de pasar."

            v "{cps=30}Menos mal, estaba algo preocupada."
            
            ms "{cps=30}Si, puedo verlo."

            ms "{cps=30}Bueno, con esto entregado bastará con que tengas una nota aprobatoiria en el examen."

            ms "{cps=30}Y deberias pasar con eso, asi que deberias relajarte un poco."

            ms "{cps=30}Si quieres descansa el resto de la clase."

            ms "{cps=30}Se ve que has estado algo estresada."

            v "{cps=30}Si gracias, eso haré."

            v "{cps=30}Muchas gracias Maestro."

            "{cps=30}Valeria entregó las tareas a tiempo."

        else: # No completado sin ayuda

            ms "{cps=30}Bueno Valeria, sin tener estas actividades."
             
            ms "{cps=30}Me temo que te será complicado pasar."

            ms "{cps=30}Tendras que sacar una nota muy alta para poder compensar."

            v "{cps=30}Si.. Lo se."

            v "{cps=30}Me esfrozaré."

            ms "{cps=30}Creo que deberias descansar por hoy."

            ms "{cps=30}Te vez cansada."

            v "{cps=30}Estoy bien, necesito estudiar para poder pasar.."

            ms "{cps=30}Como gustes, recuerda que si necesitas ayuda, esta escuela ofrece servicios de psicopedagogia para el alumnado."

            ms "{cps=30}Tal vez la psicologa te pueda dar algun consejo."

            v "{cps=15}..."

            v "{cps=30}Lo pensaré.."

            "Valeria no logró entregar las tareas a tiempo."

    #
    # DESCANSO - EN EL PARQUE/BIBLIOTECA
    #

    "Tras saber los resultados el maestro les permitio salir antes a su descanso."

    if resClase = 1 || 3:

        pv "{cps=30}Menos mal si logre entregarlo."

        pv "{cps=30}No quisiera imaginarme como habria sido si no lo lograba."

        v "{cps=30}Bueno, creo que tengo algo de tiempo libre."

        menu:

            v "¿Deberia estudiar para los examenes o descansar un poco?"

            "Estudiar":

                $ estudiar += 1
                $ biblioteca = True

                v "{cps=30}Si, creo que lo mejor sera que no me descuide ahora."

                v "{cps=30}Iré a la biblioteca a estudiar."

                v "{cps=30}Andando bebé, aun tenemos cosas por hacer."

                jump biblioteca

            "Descansar":

                v "{cps=30}Bueno, creo que me podria permitir descansar un rato."

                v "{cps=30}Tal vez pueda pasar algo de tiempo con mi bebé en el parque."

                v "{cps=30}Tu que dices nene?"

                b "{cps=30}Apmm mhaa"

                v "{cps=30}Eso es, asi se dice, andando jaja."

                # Cambio de escena al parque.

                v "{cps=30}Creo que por aqui estaria bien, que te parece bebé."

                pv "{cps=30}Hace tiempo que no he podido pasar tiempo con mi bebé."

                pv "{cps=30}Deberia aprovechar."

                "{cps=30}Valeria estuvo jugando con su bebé durante una buena parte del descanso."

                "{cps=30}Despues de un tiempo su bebé se quedo dormido."

                "{cps=30}Valeria ya estaba bastante cansada por todo lo del dia."

                "{cps=30}El sueño empezaba a pegar."

                pv "{cps=30}No deberia quedarme dormida aqui."

                pv "{cps=30}Ahora que se durmio deberia de aprovechar para estudiar un poco.."



    else:

        pv "{cps=30}Debo poner mas empeño."

        pv "{cps=30}Debo lograrlo."

        pv "{cps=30}Estoy muy cerca, solo debo esforzarme más.."

        pv "{cps=30}Aunque.. ¿Deberia de ir con la psicologa como el maestro dijo?"

        pv "{cps=30}No, que estoy pensando, estoy en riesgo de reprobar."

        pv "{cps=30}Tengo que centrarme."

        v "{cps=30}Iré a la biblioteca, alli podre estudiar sin interrupciones"

        "Valeria decidio ir a la biblioteca a estudiar."

        $ estudios += 1
        $ biblioteca = True

        jump biblioteca

    if biblioteca == True:

        label biblioteca:

            "{cps=30}Para cuando Valeria llego a la biblioteca su bebé se habia quedado dormido."

            pv "{cps=30}Menos mal."

            v "{cps=30}Bien, no hay timepo que perder."

            v "{cps=30}Hay que ponernos manos a la obra."

            "{cps=30}Valeria estuvo estudiando por gran parte de su descanso."

            "{cps=30}Pero el cansancio de todo lo que habia hecho en el día empezo a cobrar factura."

            pv "{cps=30}Siento los ojos pesados.."

            pv "{cps=30}No, debo seguir estudiando."

            pv "{cps=30}Esta es mi ultima oportunidad.."
    
    pv "{cps=30}Aun debo demostrarle que si podemos con esta vida..."

    pv "{cps=20}Si lo logro.."

    pv "{cps=20}Se que el volverá..."

    # Animacion de cerrar ojos
    
    "{cps=30}Valeria cayo rendida ante el cansancio.."

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

    "{cps=30}Valeria se quedo dormida en la universidad."

    "{cps=30}Una ola de recuerdos inundan la mente de Valeria."

    "{cps=30}Valeria no solia estar tan sola."

    "{cps=30}Ella tuvo una pareja."

    "{cps=30}Pareja con la cual creyó que estaría toda la vida."

    "{cps=30}Pareja la cual creia que la apoyaria en estos momentos tan importantes de su vida."

    "{cps=30}Hace ya casi 1 año de ello."

    "{cps=30}Tal parece que todo lo que ha pasado hasta ahora hizo que volvieran esos recuerdos."

    # Mostrar a Valeria felz junto a su novio.

    #
    # ESCENA 1 - EN EL CAMPUS
    #

    vr "{cps=30}Jajaja, ¿en serio? ¿Otra vez te quedaste dormido estudiando?"

    en "{cps=30}Sabes que no es mi culpa que medicina tenga tantos temas por estudiar."

    vr "{cps=30}Eso dices siempre. Ya hasta parece que tu libro es más tu novia que yo."

    en "{cps=30}Bueno, al menos mi libro no se burla de mi cuando estoy cansado."

    vr "{cps=30}Jajaja, vamos no seas exagerado."

    en "{cps=30}Jaja, bueno ya en serio, ¿como te fue hoy en clases?"

    vr "{cps=30}Bien, el maestro dejó mas tarea para la proxima semana."

    en "{cps=30}¿Más? Parece que los maestros se ponen de acuerdo para no dejarnos descansar."

    vr "{cps=30}Hmm, lo dices como si no tuvieras tres examenes para esta semana."

    en "{cps=30}Uhg, ni me lo recuerdes.."

    vr "{cps=30}Jajaja, bueno, al menos estamos sufriendo juntos."

    en "{cps=30}Jeje si, Eso es lo importante ¿no?"

    vr "{cps=30}Supongo que si jeje."

    v "{cps=25}Como extraño estos pequeños momentos.."

    v "{cps=25}Como desearia poder volver..."

    en "{cps=30}Oye amor, por cierto, ¿ya pensaste en que es lo que quieres hacer una vez que salgamos de la univercidad?"

    vr "{cps=30}¿Mmh? ¿A que viene eso?"

    en "{cps=30}No lo se, ultimamente pienso mucho en el futuro?"

    v "{cps=25}Jeje, mentiroso, siempre estabas pensando en eso."

    vr "{cps=30}Mmm.. pues supongo que primero quisiera terminar la univercidad y conseguir un buen empleo."

    en "{cps=30}¿Y despues?"

    vr "{cps=30}Despues... no lo sé. Quizá independizarme, viajar un poco y supongo que conocer otros lugares."

    en "{cps=30}¿Osea que no estoy incluido en esos planes? Ouch."

    vr "{cps=30}Jajaja, yo no dije eso!."

    en "{cps=30}Mas te vale jajaja."

    v "{cps=25}Tonto... Claro que estabas incluido en todos y cada uno de mis planes.."

    v "{cps=25}Queria que estubieras en todos..."

    en "{cps=30}Bueno ya, hablando enserio."

    menu:

        en "{cps=30}¿Cómo imaginas tu futuro?"

        "Hablar sobre sus metas profecionales.":

            vr "{cps=30}Yo si hablaba enserio pero empezaste a bromear."

            en "{cps=30}Jaja, disculpa."

            vr "{cps=30}Pues como dije, quisiera conseguir un buen empleo."

            vr "{cps=30}Quisiera demostrar de lo que soy capaz."

            vr "{cps=30}Hay gente que espera mucho de mi."

            vr "{cps=30}Y no pienso desepcionarlos."

            en "{cps=30}hmm, me parece admirable."

            en "{cps=30}Confio en que lo lograras."

            vr "{cps=30}jeje Graci.."

            en "{cps=30}Ademas, asi podre decir que estoy con una exitosa mujer jaja."

            vr "{cps=30}Jajaja, gracias tonto rompiste el momento romantico."

            en "{cps=30}Jajajaja"

        "Hablar sobre vivir juntos.":

            vr "{cps=30}Pues, aparte de lo que ya dije."

            vr "{cps=30}Supongo que no estaria mal tal vez.."

            vr "{cps=30}No se... {w=0.4}Tener algun lugar para nosotros."

            vr "{cps=30}Solo nosotros dos, sabes."

            vr "{cps=30}Bueno, claro que seria despues de terminar nuestra carrera y eso ¿no?"

            vr "{cps=30}Pero.. creo que seria lindo."

            en "{cps=30}Jeje, si. {w=0.3}Me encanta la idea."

        "Bromear sobre su futuro juntos.":

            vr "{cps=30}Bueno, yo ya dije lo que quiero."

            vr "{cps=30}Asi que tendras que terminar tu carrera para poder cumplir con mis caprichos jaja."

            en "{cps=30}Jajaja, ¿yo? si hasta hace un momento ni me incluias jaja."

            vr "{cps=30}Jaja, Claro que estabas incluido tonto."

            vr "{cps=30}¿Quien crees que iba a financiar cada uno de mis viajes eh?"

            en "{cps=30}Jajaja, ¿seria tu monedero entonces?"

            vr "{cps=30}Jajaja por supuesto, puedes sentirte honrado si quieres."

            en "{cps=30}Jajajaja"

    v "{cps=25}Como extraño todo esto.."

    v "{cps=25}Ojala hubieramos podido cumplir con todo lo que planeamos juntos..."

    v "{cps=25}Tanta felicidad se sentia como un sueño.."

    v "{cps=25}Desearia que se hubiera mantenido asi siempre..."

    #
    # ESCENA 2 - CITA EN EL PARQUE
    # 

    # Cambio de escena al parque

    "{cps=30}2 Semanas despues."

    vr "{cps=30}¿Dónde se metio?"

    vr "{cps=30}Hace rato que deberia de estar aquí?"

    vr "{cps=30}Ah, ahi viene."

    # Llega el Exnovio

    vr "{cps=30}Pense que ya no vendrias."

    en "{cps=30}Perdón, tuve que repasar algunos temas ya que pronto tendre los examenes."

    vr "{cps=30}Bien, entiendo. Pero llevamos bastante tiempo ya esperando para salir."

    en "{cps=30}Lo se, lo siento. Es que ultimamente tengo bastantes cosas por hacer."

    vr "{cps=30}Yo tambien las tengo y aun asi intento organizarme para poder venir."

    en "{cps=30}Esta bien, no te enojes, no tienes porque ponerte así."

    vr "{cps=30}No estoy enojada es solo que... {w=0.4}solamente queria pasar un rato contigo.."

    en "{cps=30}Bueno ya estoy aqui ¿no?, Vamos, no quiero que pasemos el dia discutiendo."

    en "{cps=30}No volvera a pasar, lo prometo."

    v "{cps=20}Mentiroso.."

    v "{cps=25}Esto paso mas de una sola vez.."

    menu:

        "¿Como responde Valeria?"

        "Decir que tambien deberia esforzarce por pasar tiempo juntos.":

            vr "{cps=30}Sabes.. la verdad no me gusta como va todo esto."

            en "{cps=30}¿A que te refieres?"

            vr "{cps=30}¡A esto¡ dices que no volvera a pasar pero ya ha pasado varias veces antes."

            vr "{cps=30}No siento que te esfuerces tanto como yo lo hago por nuestra relacion."

            en "{cps=30}Claro que me esfuerzo es solo que.. he estado mas ocupado ultimamente."

            vr "{cps=30}Yo tambien, pero no por eso descuido lo nuestro."

            vr "{cps=30}Creo que deberias esforzarte mas por que pasaramos más tiempo juntos."

            en "{cps=30}Si esta bien.. hare lo posible para que asi sea."

        "Dejar pasar el comentario y continuar con su salida.":

            vr "{cps=30}Hmm, está bien.. tienes razón.."

            vr "{cps=30}No deberiamos pasar nuestro tiempo juntos discutiendo por estas cosas..."

            en "{cps=30}Exacto, lo mejor sera que disfrutemos de lo que podamos."

            vr "{cps=30}Si.. es cierto..."

        "Preguntar si realmente quiere pasar tiempo con ella.":

            vr "{cps=30}Oye Raúl..."

            vr "{cps=30}¿De verdad quires estar conmigo?"

            en "{cps=30}¿Qué?, ¿porqué preguntas eso?"

            en "{cps=30}Por supuesto que que quiero estar contigo."

            en "{cps=30}Es solo que.. no he tenido mucho tiempo libre."

            en "{cps=30}Y estoy teniendo problemas para organizarme."

    v "{cps=25}A veces me pregunto si es culpa mia.."

    v "{cps=25}¿Acaso yo pedía demaciado por querer estar con él?.."

    #
    # ESCENA 3 - PLANES DEL EX
    #

    "Tras ese incidente en su cita su novio la invito a comer para compensarlo."

    en "{cps=30}Oye amor, ¿te he contado que estoy pensando en hacer mis practicas en otro hospital?"

    vr "{cps=30}¿En serio? ¿en cuál?"

    en "{cps=30}Todavia noe stoy muy seguro, pero hay uno que me interesa bastante."

    vr "{cps=30}Eso es genial, seguro qué lo consigues."

    en "{cps=30}Jeje, no lo se. Tendria que esforzarme bastante."

    vr "{cps=30}Confio en que lo puedes lograr."

    en "{cps=30}Gracias. Aunque eso significaria que probablemente tendría menos tiempo libre.."

    vr "{cps=30}Bueno, tampoco es como si tuvieras mucho ahora mismo."

    en "{cps=30}Ouch."

    vr "{cps=30}Jajaja, perdona."

    en "{cps=30}Pero enserio.."
    
    menu:

        en "¿crees que podriamos seguir viendonos si tengo que dedicarle mas tiempo a mis practicas?"

        "Podremos encontrar tiempo para nosotros.":

            vr "{cps=30}Claro que si, seria complicado y tendriamos que organizarnos mejor."

            vr "{cps=30}Pero creo que si podriamos."

            vr "{cps=30}Eso si, tendriamos que organizarnos mejor con nuestras salidas."

            vr "{cps=30}Y cierto individuo deberá de darle un pequeño espacio aunque sea a su novia jaja."

            en "{cps=30}Jaja, si tienes razón, me alegra oir eso."

        "No me gustaria que descuides tus estudios por mi.":

            vr "{cps=30}Pues.. supongo que si seria posible con una mejor organizacion.."

            vr "{cps=30}Pero me preocupa que llegases a descuidar tus estudios por mi.."

            vr "{cps=30}No quisiera importunarte..."

            en "{cps=30}¿Qué? no no, claro que no."

            en "{cps=30}Tu jamas podrias importunarme."

            en "{cps=30}Tambien eres importante para mi."

            en "{cps=30}Asi que deberia darte mas de mi tiempo."

        "Espero que no termines olvidandote de mi.":

            vr "{cps=30}Claro que si, si ambos nos ponemos en ello seguro que podemos."

            vr "{cps=30}Es cierto que no nos veremos tanto pero creo que si podemos."

            vr "{cps=30}Solo espero que no termines olvidadote de mi eh! Jaja.."

            en "{cps=30}Jaja, claro que no."

            en "{cps=30}Haria todo lo posible por verte."

    v "{cps=25}El tambien tenia sus propios problemas.."

    v "{cps=25}Tal vez tenga razon.."

    v "{cps=25}Tal vez si sea yo la del problema..."

    #
    # ESCENA 4 - PRIMEROS CAMBIOS
    #

    "{cps=30}Con el paso del sus responsabilidades no hicieron mas que aumentar."

    "{cps=30}Se veian cada vez menos."

    "{cps=30}Y sus charlas se volvian cada vez mas cortas."

    # Mostrar a Valeria sentada en una vanca de la univercidad

    vr "{cps=30}¿Habra terminado ya sus clases?"

    vr "{cps=30}Ultimamente no hemos podido vernos casi nada.."

    vr "{cps=30}Supongo que ambos estamos ocupados.."

    "Bzzz bzzz"

    vr "{cps=30}Creo que ya me contestó."

    $ mensajes_chat = []

    show screen celular_chat

    $ agregar_mensaje("Raúl", "Perdón, hoy tampoco podré salir. Tengo que estudiar para un examen")

    vr "{cps=30}¿Otra vez?, antes tampoco pudimos porque tenia tareas.."

    $ agregar_mensaje("Valeria", "Esta bien, no te preocupes")

    $ agregar_mensaje("Valeria", "Entiendo")

    $ agregar_mensaje("Raúl", "Te prometo que cuando termine esta semana tendremos tiempo para nosotros")

    vr "{cps=30}Antes tambien me dijiste que podriamos esta semana.."

    $ agregar_mensaje("Valeria", "Está bien. Mucha suerte con tu examen")

    $ agregar_mensaje("Valeria", "Te amo")

    $ agregar_mensaje("Raúl", "Yo a tí")

    hide screen celular_chat

    vr "{cps=30}No se si deberia darme esperanzas.."

    vr "{cps=30}Es probable que tampoco nos veamos la proxima semana."

    v "{cps=25}Y no me equivocaba.."

    v "{cps=25}No nos pudimos ver hasta mucho despues.."

    #
    # ESCENA 5 - MALESTARES EN CASA
    #

    "{cps=30}Pasaron cerca de 2 semanas."

    "{cps=30}Valeria continuo con sus actividades, aunque Valeria habia comenzado a sentirse diferente."

    vr "{cps=30}Que extraño.. ultimamente me he sentido bastante cansada."

    vr "{cps=30}Debe ser porque he estado muy ocupada."

    vr "{cps=30}Aunque... llevo varios dias sintiendome asi.."

    vr "{cps=15}..."

    vr "{cps=30}No sera que..."

    "{cps=30}La posibilidad cruzo su mente. Pero no queria sacar conclusiones apresuradas."

    "{cps=30}Asi que se dispuso a hacer la prueba."

    v "{cps=25}Tenía razón.."

    vr "{cps=30}¿Estoy.. Embarazada?"

    v "{cps=25}Antes pensaba que eso me alegraria.."

    v "{cps=25}Pero con todo lo que habia estando pasando.."

    vr "{cps=30}No.. esto no puede estar pasando."

    vr "{cps=30}¿Qué voy a hacer ahora?"

    vr "{cps=30}¿Qué pasara con mis estudios? ¿Y con nosotros...?"

    vr "{cps=30}Deberia decirle.. no quisiera estar sola ahora mismo.."

    vr "{cps=30}Pero.. ¿como lo tomará?"

    menu:

        vr "{cps=30}¿Qué deberia hacer?"

        "Buscarlo para hablar inmediatamente.":

            vr "{cps=30}Para ya de poner peros Valeria."

            vr "{cps=30}Esto es algo importante, no es momento de dudar."

            vr "{cps=30}Debo ir a buscarlo."

            vr "{cps=30}Le dire que estoy embarazada."

        "Esperar el momento adecuado.":

            $ contarNoticia = 2

            vr "{cps=30}No.."

            vr "{cps=30}Es demaciado pronto.."

            vr "{cps=30}Tal vez este ocupado ahora.."

            vr "{cps=30}Si, lo mejor sera que espere a que llegue el moemnto."

            "{cps=30}Pasaron los días pero el 'momento' nunca llego."

            "{cps=30}Al final valeria decidio ir a decirle."

        "Pensar en lo que hará antes de contarselo.":

            $ contarNoticia = 3

            vr "{cps=30}No, tal vez.. deba tomarme un tiempo."

            vr "{cps=30}No se como podria reaccionar.."

            vr "{cps=30}¿Y si deicide dejarme?"

            vr "{cps=30}¿Qué pasa si le digo y decide no verme mas?"

            vr "{cps=30}No se que deberia hacer.."

            vr "{cps=30}Creo que me tomare unos dias para pensarlo.."

            "{cps=30}Pasaron unos dias pero no cambiaba de idea."

            "{cps=30}Al final valeria deciudio ir a decirle."

    v "{cps=25}A veces me pregunto si hice lo correcto.."

    v "{cps=25}¿Estuve mal por querer decirle?.."

    v "{cps=25}Me pregunto si las cosas hubieran sido distintas..."

    #
    # ESCENA 6 - UNA NOTICIA IMPORTANTE
    #

    "{cps=30}La hora habia llegado, era momento de contarle."

    if contarNoticia == 1:

        en "{cps=30}Valeria."

        en "{cps=30}Dijiste que queria deirme algo ¿no?"

        en "{cps=30}En tu mensaje sonaba a que era algo muy importante."

        en "{cps=30}¿Pasó algo?"

        vr "{cps=30}Pues..."

        vr "{cps=30}Se podria decir que si.."

        v "{cps=25}Iba muy segura de lo que queria decirle.."

        v "{cps=25}Pero en ese momento.. me atrapó el miedo..."

        en "{cps=30}Bueno, pues ya estoy aqui."

        en "{cps=30}Dime. ¿Qué paso? ¿Te encuentras bien? Pareces bastante preocupada."

    else if contar noticia == 2:

        vr "{cps=30}No se porque pense que lo mejor seria esperar."

        vr "{cps=30}Cuando podria ser un buen momento para contar algo com esto.."

        vr "{cps=30}.. Oh, parece que allí viene."

        en "{cps=30}Valeria. Disculpa la demora."

        en "{cps=30}Justo estaba terminando unos pendientes."

        en "{cps=30}Dime, ¿está todo bien?"

        en "{cps=30}Parecias preocupada en tu mensaje."

        vr "{cps=30}..."

    else:

        vr "{cps=30}Al final no pude pensar en nada más."

        vr "{cps=30}Pero no puedo retrasar mas esto."
        
        vr "{cps=30}Debo decirle y esperar lo mejor.."

        en "{cps=30}Hola Valeria."

        en "{cps=30}Perdona la demora."

        en "{cps=30}Estaba terminando unos pendientes."

        vr "{cps=30}Si este.. está bien."

        en "{cps=30}¿Te encuetras bien?, pareces bastante preocupada."

    vr "{cps=30}Bueno.. es que, no se como decirtelo.."

    en "{cps=30}Tranquila. Sea lo que sea se que podremos sobrellevarlo juntos."

    vr "{cps=20}..."

    vr "{cps=25}Estoy embarazada."

    en "{cps=25}..."

    vr "{cps=30}Se que es algo dificil de creer. Yo tampoco se que hacer.."

    en "{cps=30}¿Estas segura?"

    vr "{cps=30}Si..."

    en "{cps=30}Pero.. ¿Cómo paso esto?"

    vr "{cps=30}No lo sé, simplemtente pasó."

    vr "{cps=30}Ya no se que pensar.. estoy asustada.."

    en "{cps=30}Es que... no sé que decir."

    v "{cps=25}Lo que sea.."

    v "{cps=25}Cualquier cosa hubiera bastado.."

    v "{cps=25}Solo queria saber que no estaba sola..."

    menu:

        en "{cps=30}..."

        "Necesito saber que puedo contar contigo..":

            en "{cps=20}..."

            en "{cps=30}Si.. por supuesto que si."

            en "{cps=30}Es mi hijo despues de todo ¿no?.."

            v "{cps=20}No se porqué te creí.."

            vr "{cps=30}Gracias.."

            vr "{cps=30}De verdad, necesitaba escuchar eso.."

        "Quisiera que pensemos juntos que haremos..":

            en "{cps=30}Ah, si.. es cierto."

            en "{cps=30}Tenemos mucho que planear ¿no?.."

            vr "{cps=30}Si.. asi es.."

            vr "{cps=30}Tendriamos que ver todo el tema de su comida."

            vr "{cps=30}Jugetes.. y todo eso."

            en "{cps=30}Si.. pero ¿no crees que es algo pronto para todo eso?"

            en "{cps=30}Es que.. aun faltan muchos meses para que nazca ¿no?"

            en "{cps=30}Creo que.. podriamos espera un poco para pensar en ello."

            vr "{cps=30}A si.. {w=0.2}claro.. {w=0.2}supongo que tienes razon..."

        "Sé que no tenemos todas las respuestas..":

            vr "{cps=30}Pero ahora mismo.. quisera que me escuches."

            vr "{cps=30}Se que no hemos pasado mucho tiempo juntos."

            vr "{cps=30}Se bien que hemos estado muy ocupados ambos.."

            vr "{cps=30}Y se que todo esto es muy repentino pero.."

            vr "{cps=30}De verdad te necesito.."

            vr "{cps=30}No puedo hacer esto sin tí..."

            en "{cps=30}Si, lo se es solo que... me tomó por sorpresa.."

            en "{cps=30}No se que deberia hacer.."

            en "{cps=30}Pero se que no puedo dejarte sola.."

            en "{cps=30}Tendremos que hacerlo juntos."

            vr "{cps=30}Si.. tienes razón."


    vr "{cps=30}Bueno.. tendre que hablar con mis padres."

    en "{cps=30}Si, es cierto.. ¿Crees que sea buena idea?"

    vr "{cps=30}No lo sé, pero necesito decírselo"

    en "{cps=30}Claro.. tienes razón."

    en "{cps=30}Bueno.. supongo que tendremos que pensar cómo hacerlo.."

    vr "{cps=30}Si.. tendremos que pensarlo."

    v "{cps=25}Porque hacerme creer que me ayudarias.."

    v "{cps=25}¿Porque?.."

    v "{cps=25}Despues de ese dia, solo te volviste más distante.."

    v "{cps=25}No contestabas mis mesnajes y cuando te veia en la univercidad solo ponias excusas y te marchabas.."

    v "{cps=25}No tarde en entender que tendria que contarles a mis padres sola.."

    v "{cps=25}No tenia idea de lo que me esperaba..."

    call screen separador_nivel(
        "03",
        "Confrontacion",
        "Regresar a Casa"
    )

    jump nivel_3

label nivel_3:
    #
    # ESCENA 1 - REGRESAR A CASA
    #

    "{cps=30}Pasaron unas cuantas semanas."

    "{cps=30}Valeria aun tenia dudas, pero estaba segura de algo."

    vr "{cps=30}Mis padres deben ser saberlo."

    vr "{cps=30}No puedo vivir ocultandocelo."

    vr "{cps=30}"


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
