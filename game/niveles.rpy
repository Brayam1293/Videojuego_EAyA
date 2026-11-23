# 
# NIVEL 1
# UN NUEVO DÍA
#


label nivel_1:

    scene bg fondo_casa with fade

    "{cps=30}Las deciciones importantes deberian ser planeadas con tiempo y detenimiento."

    "{cps=30}Pero no todos tienen esa oportunidad."

    "{cps=30}Como es el caso de Valeria, una joven univercitaria a la que su vida dio un giro inesperado."

    "{cps=20}Por favor...{w=0.4} ayudala en lo que te sea posible..."

    pause 1.3

    # 
    # ESCENA 1 - MAÑANA APRESURADA
    # 

    show valeria_bebe normal at pos(0.5, -0.3), 
    with dissolve

    "{cps=30}Una nueva mañana comienza."

    v "{cps=30}Hoy tengo clases temprano."

    v "{cps=30}Debo prepararme antes de salir."

    v "{cps=30}Revisare que tenga todo en mi mochila."

    v "{cps=10}..."

    show valeria_bebe preocupada at pos(0.5, -0.3)

    v "{cps=30}Oh no{w=0.6}, olvide hacer la tarea para hoy!."

    v "{cps=30}Talvez si me apresuro pueda terminarla."

    show valeria_bebe llorando at pos(0.5, -0.3)

    b "{cps=30}snif, snif... !bua, buaa!"

    v "{cps=25}Ay no, ¿qué tienes bebé?..{p=0.3} ¿Qué paso?.."

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

            v "{cps=30}Ya casi es hora de irme."

        "Atender al bebé primero.":

            $ cuidado_bebe += 1

            v "{cps=30}Supongo que puedo hacer que deje de llorar primero."

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

            show valeria_bebe triste at pos(0.5, -0.3)

            b "{cps=30}{size=35}!Bua, bua!"

            v "{cps=30}Oh no, ya es tarde y no eh terminado nada aun."

            v "{cps=30}No hay de otra, tendre que irme asi."

            "{cps=30}El bebé ceso su llanto poco despues de esto."

            v "{cps=30}Menos mal...{w} Ya queda poco tiempo."

    #
    # ESCENA 1:2 - PREPARANDOSE PARA SALIR
    #

    menu:

        v "{cps=30}Muy bien{w}, ¿Qué deberia hacer antes de salir?"

        "Revisar mis cosas para la universidad.":

            $ objValeria = True
            $ estudios += 1

            show valeria_bebe normal at pos(0.5, -0.3)

            v "{cps=30}Deberia revisar que tenga todo para la univercidad."

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

            show valeria_bebe preocupada at pos(0.5, -0.3)

            v "{cps=30}¡No habia visto la hora!, ya es muy tarde."

            v "{cps=30}Debo darme prisa."

    if objAmbos == True:
        show valeria_bebe tarde :
            linear 2.5 xalign 2.5 yalign -3.0
        with dissolve
        
        "{cps=30}Valeria salio rapidamente de su casa camino a la escuela y logro calmarse un poco."
    
    else:
        v "{cps=30}Ahora sí, podemos irnos."

        show valeria_bebe normal:
            linear 3.0 xalign 2.5 yalign -3.0
        with dissolve
    pause 1.2

    #
    # ESCENA 2 - TRAYECTO A LA UNIVERCIDAD
    #

    scene bg fondo_trayecto
    with fade

    if objAmbos == True:
        show valeria_bebe tarde at move(-860, -0.3, 6.0, 200)
    else:
        show valeria_bebe normal at move(-860, -0.3, 6.0, 200)

    "{cps=30}Durante su trayecto Valera no paraba de escuchar murmullos a su alrededor y sentir que la miraban."

    show valeria_bebe incomoda

    pv "{cps=30}¿Porque siempre murmuran tanto?."

    pv "{cps=25}Tampoco dejan de mirarme hoy tambien.."

    pv "{cps=25}¿Porque no puedo ir tranquila a la universidad al menos una vez..?"

    show herneztino normal at move(2200, -0.3, 1.5, 1000)

    c "{cps=30}Hola."

    show valeria_bebe incomoda at move(200, -0.3, 0.2, 100)

    v "{cps=25}Ah!{w=0.3} emm{w=0.5}, hola{cps=20}...{w=0.3}"

    v "{cps=30}Disculpa pero, ¿nos conocemos o algo?"

    v "{cps=30}La verdad es que no lo recuerdo."

    c "{cps=30}A no, disculpa no me he prensentado."

    $ name_npc = "Herneztino" # NOMBRE PROPUESTO POR RAMON EDUARDO
    c "{cps=30}Me llamo Herneztino, estamos en la misma clase."

    show valeria_bebe normal

    v "{cps=30}A si perdona, mucho gusto yo soy Valeria."

    pv "{cps=30}No me suena de nada.."

    v "{cps=30}Y.. Puedo hacer algo por tí?"

    show herneztino amable:
        xpos 1000
        yalign -0.3

    c "{cps=30}No no, perdona, de hecho queria preguntarte eso mismo a ti, ¿hay algo con lo que necesites ayuda?"
    
    show herneztino normal

    show valeria_bebe incomoda

    v "{cps=30}¿Y eso porque?, no nos conocemos siquiera.."

    show herneztino amable

    c "{cps=30}Si lo se, es solo que siempre veo que pasas por aqui cargando con todo lo de tu bebé."

    c "{cps=30}Supuse que tal vez te vendria bien un poco de ayuda."

    show herneztino normal

    c "{cps=30}Asi que, ¿necesitas ayuda con algo?"

    pv "{cps=30}Todos parecen incomodos con que lleve a mi bebé a la universidad.{w=0.8} ¿Porque a el parece no importarle?"

    menu:

        pv "{cps=30}¿Qué deberia hacer?"

        "Rechazar su ayuda.":

            v "{cps=30}No gracias, puedo hacerlo por mi misma."

            show valeria_bebe triste

            v "{cps=30}Solo te quitaria tiempo."

            show herneztino amable

            c "{cps=30}No te preocupes por eso, quisiera ayudarte."

            show herneztino normal

            show valeria_bebe incomoda

            v "{cps=30}Gracias pero estoy bien asi.."

            pv "{cps=30}Debo ser capaz de hacerlo yo misma.."

            pv "{cps=30}Es mi bebé despues de todo.{p=0.3}No deberia de hacer que afecte la rutina de otros.."

            c "{cps=30}Okey, si tu lo dices esta bien."

            c "{cps=30}Supongo que nos vemos luego entonces."

        "Afirmar que no es necesario.":

            show valeria_bebe triste

            v "{cps=30}No es necesario, de verdad. No quisiera molestarte con mis cosas."

            show herneztino amable

            c "{cps=30}No te preocupes por eso. De todas formas, tambien voy a la universidad."

            show valeria_bebe incomoda

            show herneztino normal

            c "{cps=30}Ademas, no es necesario que lo lleves todo tu sola."

            c "{cps=30}Podria ayudarte a llevar la pañalera si quieres."

            pv "{cps=30}No quisiera molestarlo con esto.. seguramente tambien tenga sus propios asuntos."

            menu:

                pv "{cps=30}¿Debería aceptar su ayuda?.."

                "Insistir en negarte":

                    v "{cps=30}De verdad, estoy bien asi.."

                    show valeria_bebe normal

                    v "{cps=30}Pero muchas gracias."

                    show herneztino amable

                    c "{cps=30}Okey, si asi lo quieres esta bien."

                    c "{cps=30}Pero recuerda que mi oferta sigue en pie jeje."

                    show valeria_bebe incomoda

                    show herneztino normal at move(1000, -0.3, 3.0, 2200)

                    c "{cps=30}Bueno, nos vemos en la univercidad entonces."

                "Aceptar su ayuda":

                    $ aceptarAyuda = True
                    $ valeriaDuda = True

                    v "{cps=30}Pues, supongo que si estaria bien.. ya que insistes."

                    "{cps=30}Valeria accedio a darle la pañalera a Herneztino."

                    show valeria_bebe normal

                    v "{cps=30}Gracias.."

                    show herneztino normal

                    c "{cps=30}Con gusto."

                    c "{cps=30}Bueno vamos, no queremos llegar tarde jaja."

                    v "{cps=30}Si jaja, vamos."

                    jump Cap1_aceptarAyuda

        "Aceptar su ayuda.":

            $ aceptarAyuda = True

            pv "{cps=30}Está bien.."

            show valeria_bebe normal

            v "{cps=30}Emm, okey.."

            v "{cps=30}Está bien, muchas gracias por la ayuda."

            show herneztino amable

            c "{cps=30}Claro sin problema, te puedo ayudar con la pañalera."

            v "{cps=30}Si, gracias."

            jump Cap1_aceptarAyuda

    
    v "{cps=30}Si claro..{p=0.5}Nos vemos."

    show herneztino normal at move(1000, -0.3, 2.0, 2200)

    "{cps=30}El chico siguio su camino dejando atras a Valeria."

    show valeria_bebe incomoda at move(100, -0.3, 1.0, 400)

    v "{cps=30}Eso fue muy raro."

    show valeria_bebe normal

    v "{cps=30}Bueno bebé, ahora si vayamonos a la universidad."

    show valeria_bebe normal at move(400, -0.3, 4.0, 2200)

    "{cps=30}Valeria continuo su camino a la univercidad."

    scene bg fondo_universidad with dissolve

    show valeria_bebe tarde at move(-860, -0.6, 3.0, 400)

    v "{cps=30}Fuf.."

    v "{cps=30}Bien, creo que aun alcanzo a llegar a la clase."

    show valeria_bebe incomoda
    
    pv "{cps=30}Aunque sigo pensando en la oferta de ese chico..{w=0.4} Tal vez debi haber aceptado.."

    pv "{cps=30}No, no es momento para pensar en eso."

    pv "{cps=30}Debo demostrarles que puedo hacerlo.."

    show valeria_bebe normal

    v "{cps=30}Démonos prisa bebé, que apenas comienza el día."

    show valeria_bebe feliz

    v "{cps=30}Vamos con todo!"

    show valeria_bebe normal at move(400, -0.3, 2.5, 2200)

    pause 2.5

    if aceptarAyuda == True:
        label Cap1_aceptarAyuda:

        show valeria_bebe normal at move(100, -0.3, 3.0, 2200)

        show herneztino normal at move(1000, -0.3, 2.5, 2200)

        "{cps=30}Valeria decidio dejar que su compañero la apoyara a llevar algunas cosas."    

        $ estres -= 1
        "{cps=30}Valeria y Herneztino se fueron juntos a la universidad."

        # Cambio de escena a la universidad

        scene bg fondo_universidad with dissolve

        show herneztino feliz at move(-860, -0.3, 4.0, 950)

        show valeria_bebe feliz at move(-1200, -0.3, 4.0, 0)

        c "{cps=30}Jaja si, despues de que eso estuve forcejeando con mi perro para poder quitarselo."

        pv "{cps=30}Es bastante agradable, hacia tiempo que no me reia así."

        show herneztino normal

        show valeria_bebe normal

        v "{cps=30}Bueno, parece que ya llegamos, muchas gracias por todo."

        c "{cps=30}Gracias a ti, fue muy agradable charlar contigo."

        c "{cps=30}Bien, ya tengo que irme, mis clases estan por empezar."

        show herneztino normal at move(950, -0.3, 2.5, 2200)

        c "{cps=30}Nos vemos luego."

        show valeria_bebe feliz

        v "{cps=30}Si, nos vemos."

        show valeria_bebe normal

        pv "{cps=30}La verdad eso fue bastante mejor de lo que esperaba.."

        v "{cps=30}Bueno ya, debo apresurarme para ir a clase."

        show valeria_bebe feliz 

        v "{cps=30}Andando bebé!"

        show valeria_bebe normal at move(0, -0.3, 3, 2200)

    #
    # ESCENA 3 - EN LA UNIVERCIDAD
    #    
    
    "{cps=30}Cuando Valeria llego a la clase todos sus compañeros ya estaban alli."

    # Cambio de escena a el salon de clase

    show bg salon_clase with fade

    show valeria_bebe normal at move(-860, -0.3, 2.0, 10)

    pause 2.5

    v "{cps=30}Buen día maestro, disculpe la demora. ¿Puedo pasar?"

    show maestro normal at move(1700, -0.3, 1.0, 1600)

    ms "{cps=30}Claro adelante, tóme asiento."

    show valeria_bebe normal:
            linear 4.0 xalign 2.5 yalign -3.0

    show maestro normal at move(1600, -0.3, 2.5, 900)
    
    ms "{cps=30}Ya que estamos tan cerca de las evaluaciones"

    ms "{cps=30}El dia de hoy solo revisaremos los pendientes."
    
    ms "{cps=30}Solo para recordarles, revisare tanto las preguntas y el resumen juntos."

    ms "{cps=30}Tienen solo esta clase para poder entregarlas."

    scene bg salon_preocupada

    if tareaPendiente == True:
        
        pv "{cps=30}¡No puede ser! ¿son 2?"

        pv "{cps=30}¡No podre terminarlas a tiempo!"

        pv "{cps=15}..."

        scene bg salon_decidida

        pv "{cps=30}¡NO!"

        pv "{cps=30}Tengo hasta que acabe la clase, asi que debo intentarlo."

    else:

        scene bg salon_preocupada

        pv "{cps=30}¿Qué?, ¿habia otra?"

        pv "{cps=30}Esa aun no la he hecho."

        pv "{cps=30}Bueno, tengo esta clase para entregarla. Spongo que puedo terminarla antes que de eso."

    menu:
        "Esta por comenzar un minijuego de escritura. Prepara un teclado y ratón."

        "Empezar":
            call jugar_minijuego_aula

        "No jugar":
            "Esto conllevara a dar el juego por fallido."

    scene bg salon with fade
    
    if resumenTerminado == True and ayudaClase == True:

        $ resClase = 1

        show valeria_bebe feliz:
            xpos 100
            yalign -0.3

        show herneztino amable:
            xpos 1000
            yalign -0.3

        v "{cps=30}¡Bien, lo logramos! Muchisimas gracias."

        v "{cps=30}Creo que no lo habria logrado sin tu ayuda."

        c "{cps=30}No me agradezcas me alegra ayudar."

        c "{cps=30}Ademas este pequeño es un encanto."

        c "{cps=30}A que si bebé?"

        b "{cps=30}Mmha mmhm"

        show valeria_bebe normal:
            xpos 100
            yalign -0.3

        v "{cps=30}Jaja, bueno vayamos a revisar."

        jump resultadosClase

    elif resumenTerminado == False and ayudaClase == True:

        $ estres += 1
        $ resClase = 2

        show valeria_bebe triste:
            xpos 100
            yalign -0.3

        v "{cps=30}No puede ser.. {w=0.4}No logre terminarlo..."

        v "{cps=30}No se porque pense que si podria.."

        show herneztino normal:
            xpos 1000
            yalign -0.3

        c "{cps=30}Vamos no digas eso, solamente te falto un poco mas de tiempo."

        c "{cps=30}Ademas, aun puedes rescuperarte con el examen no?"

        show valeria_bebe preocupada:
            xpos 100
            yalign -0.3

        v "{cps=30}Si, bueno...{w=0.4} Tal vez."

        c "{cps=30}Todavia tienes una oportunidad más."

        show herneztino amable:
            xpos 1000
            yalign -0.3

        c "{cps=30}¡Arriva esos animos!"

        show valeria_bebe normal:
            xpos 100
            yalign -0.3

        v "{cps=30}Je je, si, supongo que tienes razón."

        jump resultadosClase

    elif resumenTerminado == True and ayudaClase == False:

        $ estudios += 2
        $ resClase = 3

        show valeria_bebe feliz:
            xpos 100
            yalign -0.3

        v "{cps=30}¡Wow!, de verdad no puedo creer que lo lograra."

        v "{cps=30}Fue mucho mas dificil de lo que esperaba."

        v "{cps=30}¿Desde cuando puedo escribir tan rapido?"

        show valeria_bebe normal:
            xpos 100
            yalign -0.3

        pv "{cps=30}Bien, si sigo asi, no hay duda de que lo lograre."

        jump resultadosClase

    elif resumenTerminado == False and ayudaClase == False:

        $ estres += 2
        $ resClase = 4

        show valeria_bebe triste:
            xpos 100
            yalign -0.3

        pv "{cps=30}No puede ser..."

        pv "{cps=30}No pude lograrlo.. No fui capaz.."

        pv "{cps=30}A este paso.. {w=0.4}Yo..."

        jump resultadosClase
    
    label resultadosClase:
        if resClase == 1: # Completado con ayuda

            scene bg salon_clase with dissolve

            show valeria_bebe normal at move(-200, -0.3, 0.6, 100) with dissolve
            
            show maestro normal at flip:
                xpos 1100
                yalign -0.3

            pause 0.6

            v "{cps=30}Maestro, aqui estan las activdades."

            ms "{cps=30}Muy bien, ahora mismo tienes buenas chances de pasar."

            ms "{cps=30}Me alegra ver que te llevas bien con tu compañero."

            show valeria_bebe feliz:
                xpos 100
                yalign -0.3

            v "{cps=30}Si, me ha ayudado mucho."

            show valeria_bebe normal:
                xpos 100
                yalign -0.3
            
            ms "{cps=30}Eso esta bien, me alegro por tí."

            ms "{cps=30}Bueno, con esto entregado bastará con que tengas una nota aprobatoiria en el examen."

            ms "{cps=30}Y deberias pasar con eso, asi que deberias relajarte un poco."

            show valeria_bebe feliz:
                xpos 100
                yalign -0.3

            v "{cps=30}Muchas gracias Maestro."

            "{cps=30}Valeria entregó las tareas a tiempo."

        elif resClase == 2: # No Completado con ayuda

            scene bg salon_clase with dissolve

            show valeria_bebe tarde at move(-200, -0.3, 0.6, 100) with dissolve

            show maestro normal at flip:
                xpos 1100
                yalign -0.3

            pause 0.6
             
            ms "{cps=30}Me temo que sin tener estas actividade te será complicado pasar."

            ms "{cps=30}Tendras que sacar una nota muy alta para poder compensar."

            v "{cps=30}Me esfrozaré."

            ms "{cps=30}Te vez cansada, creo que deberias descansar por hoy."
            
            show valeria_bebe triste:
                xpos 100
                yalign -0.3

            v "{cps=30}Estoy bien, necesito estudiar para poder pasar.."

            ms "{cps=30}Como gustes, recuerda que si necesitas ayuda, esta escuela ofrece servicios de psicopedagogia para el alumnado."

            ms "{cps=30}Tal vez la psicologa te pueda dar algun consejo."

            show valeria_bebe tarde:
                xpos 100
                yalign -0.3

            v "{cps=30}Lo pensaré.."

            "Valeria no logró entregar las tareas a tiempo."

        elif resClase == 3: # Completado sin ayuda

            scene bg salon_clase with dissolve
            
            show valeria_bebe normal at move(-200, -0.3, 0.6, 100) with dissolve
            
            show maestro normal at flip:
                xpos 1100
                yalign -0.3

            pause 0.6

            v "{cps=30}Maestro, aqui estan las activdades."

            ms "{cps=30}Muy bien, ahora mismo tienes buenas chances de pasar."

            v "{cps=30}Menos mal, estaba algo preocupada."
            
            ms "{cps=30}Bueno, con esto entregado bastará con que tengas una nota aprobatoiria en el examen."

            ms "{cps=30}Si quieres descansa el resto de la clase."

            ms "{cps=30}Se ve que has estado algo estresada."

            show valeria_bebe feliz:
                xpos 100
                yalign -0.3

            v "{cps=30}Si gracias eso haré, muchas gracias maestro."

            "{cps=30}Valeria entregó las tareas a tiempo."

        else: # No completado sin ayuda

            scene bg salon_clase with dissolve

            show valeria_bebe tarde at move(-200, -0.3, 0.6, 100) with dissolve
            
            show maestro normal at flip:
                xpos 1100
                yalign -0.3

            pause 0.6

            ms "{cps=30}Bueno Valeria, sin tener estas actividades te será complicado pasar."
             
            ms "{cps=30}Tendras que sacar una nota muy alta para poder compensar."

            v "{cps=30}Si.. lo se, me esfrozaré."

            ms "{cps=30}Creo que deberias descansar por hoy."

            show valeria_bebe triste:
                xpos 100
                yalign -0.3

            v "{cps=30}Estoy bien, necesito estudiar para poder pasar.."

            ms "{cps=30}Como gustes, recuerda que si necesitas ayuda, esta escuela ofrece servicios de psicopedagogia para el alumnado."

            ms "{cps=30}Tal vez la psicologa te pueda dar algun consejo."

            show valeria_bebe tarde:
                xpos 100
                yalign -0.3

            v "{cps=30}Lo pensaré.."

            "Valeria no logró entregar las tareas a tiempo."

    #
    # DESCANSO - EN EL PARQUE/BIBLIOTECA
    #

    scene bg salon with dissolve

    "La clase termino poco despues de saber los resultados."

    if resClase == 1 or resClase == 3:

        show valeria_bebe tarde at move(-100, -0.3, 2.0, 400) with dissolve

        pv "{cps=30}Menos mal si logre entregarlo."

        pv "{cps=30}No quisiera imaginarme como habria sido si no lo lograba."

        show valeria_bebe feliz:
                xpos 400
                yalign -0.3

        v "{cps=30}Bueno, creo que tengo algo de tiempo libre."

        menu:

            v "¿Deberia estudiar para los examenes o descansar un poco?"

            "Estudiar":

                $ estudiar += 1
                $ biblioteca = True

                show valeria_bebe normal:
                    xpos 400
                    yalign -0.3

                v "{cps=30}Si, creo que lo mejor sera que no me descuide ahora."

                v "{cps=30}Iré a la biblioteca a estudiar."

                show valeria_bebe normal at move(400, -0.3, 2.0, 2200)

                pause 1.0

                jump biblioteca

            "Descansar":

                show valeria_bebe normal:
                    xpos 400
                    yalign -0.3

                v "{cps=30}Bueno, creo que me podria permitir descansar un rato."

                show valeria_bebe normal at move(400, -0.3, 2.0, 2200) with dissolve

                pause 1.0

                scene bg fondo_parque with fade

                show valeria_bebe normal at move(-100, -0.3, 2.0, 400) with dissolve

                pause 1.0

                v "{cps=30}Creo que por aqui estaria bien, que te parece bebé."

                pv "{cps=30}Hace tiempo que no he podido pasar tiempo con mi bebé."

                pv "{cps=30}Deberia aprovechar."

                show valeria_bebe normal at move(400, -0.3, 2.0, 2200)

                pause 2.0

                "{cps=30}Valeria estuvo jugando con su bebé durante una buena parte del descanso."

                "{cps=30}Despues de un tiempo su bebé se quedo dormido."

                "{cps=30}Valeria ya estaba bastante cansada por todo lo del dia."

                "{cps=30}El sueño empezaba a afectarla."

                scene vision_valeria with dissolve

                pv "{cps=30}No deberia quedarme dormida aqui."

                pv "{cps=30}Ahora que se durmio deberia de aprovechar para estudiar un poco.."



    else:

        show valeria_bebe tarde at move(-100, -0.3, 2.0, 400) with dissolve

        pv "{cps=30}Debo poner mas empeño."

        pv "{cps=30}Debo lograrlo."

        pv "{cps=30}Estoy muy cerca, solo debo esforzarme más.."

        pv "{cps=30}Aunque.. ¿Deberia de ir con la psicologa como el maestro dijo?"

        show valeria_bebe triste:
            xpos 400
            yalign -0.3

        pv "{cps=30}No, que estoy pensando, estoy en riesgo de reprobar."

        pv "{cps=30}Tengo que centrarme."

        v "{cps=30}Iré a la biblioteca, alli podre estudiar sin interrupciones"

        show valeria_bebe tarde at move(400, -0.3, 3.0, 2200)

        pause 1.0

        "Valeria decidio ir a la biblioteca a estudiar."

        $ estudios += 1
        $ biblioteca = True

        jump biblioteca

    if biblioteca == True:

        label biblioteca:

            scene bg biblioteca with fade

            if resClase == 1 or resClase == 3:
                show valeria_bebe normal at move(1600, -0.3, 2.5, 1000), flip with dissolve
            else:
                show valeria_bebe tarde at move(1600, -0.3, 2.5, 1000), flip with dissolve

            "{cps=30}Para cuando Valeria llego a la biblioteca su bebé se habia quedado dormido."

            v "{cps=30}Bien, no hay timepo que perder."

            v "{cps=30}Hay que ponernos manos a la obra."

            if resClase == 1 or resClase == 3:
                show valeria_bebe normal at move(1000, -0.3, 2.0, 200)
            else:
                show valeria_bebe tarde at move(1000, -0.3, 2.0, 200)

            pause 1.0

            scene bg valeria_biblioteca estudiando with dissolve

            "{cps=30}Valeria estuvo estudiando por gran parte de su descanso."

            "{cps=30}Pero el cansancio de todo lo que habia hecho en el día empezo a cobrar factura."

            scene bg valeria_biblioteca cansada with dissolve

            pv "{cps=30}Siento los ojos pesados.."

            pv "{cps=30}No, debo seguir estudiando."

            pv "{cps=30}Esta es mi ultima oportunidad.."
    
    pv "{cps=30}Aun debo demostrarle que si podemos con esta vida..."

    pv "{cps=20}Si lo logro.."

    pv "{cps=20}Se que el volverá..."

    scene black with circleirisout
    
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

    scene bg biblioteca with fade

    "{cps=30}Valeria se quedo dormida en la universidad."

    "{cps=30}Una ola de recuerdos inundan la mente de Valeria."

    "{cps=30}Valeria no solia estar tan sola, ella tuvo una pareja."

    "{cps=30}Pareja la cual creia que la apoyaria en estos momentos tan importantes de su vida."

    "{cps=30}Hace ya casi 1 año de ello."

    #
    # ESCENA 1 - EN EL CAMPUS
    #

    scene bg raul_biblioteca dormido with dissolve

    vr "{cps=30}Jajaja, ¿en serio? ¿Otra vez te quedaste dormido estudiando?"

    scene bg raul_biblioteca avergonzado with dissolve

    en "{cps=30}Sabes que no es mi culpa que medicina tenga tantos temas por estudiar."

    vr "{cps=30}Eso dices siempre. Ya hasta parece que tu libro es más tu novia que yo."

    scene bg biblioteca with dissolve

    show valeria feliz:
        xpos -100
        yalign -0.3

    show raul feliz:
        xpos 900
        yalign -0.3

    en "{cps=30}Bueno, al menos mi libro no se burla de mi cuando estoy cansado."

    show valeria normal:
        xpos -100
        yalign -0.3

    vr "{cps=30}Jajaja, vamos no seas exagerado."

    show raul normal:
        xpos 900
        yalign -0.3

    en "{cps=30}Jaja, bueno ya en serio, ¿como te fue hoy en clases?"

    vr "{cps=30}Bien, el maestro dejó mas tarea para la proxima semana."

    show raul preocupado:
        xpos 900
        yalign -0.3

    en "{cps=30}¿Más? Parece que los maestros se ponen de acuerdo para no dejarnos descansar."

    vr "{cps=30}Hmm, lo dices como si no tuvieras tres examenes para esta semana."

    show raul triste:
        xpos 900
        yalign -0.3

    en "{cps=30}Uhg, ni me lo recuerdes.."

    show valeria feliz:
        xpos -100
        yalign -0.3

    vr "{cps=30}Jajaja, bueno, al menos estamos sufriendo juntos."

    show raul feliz:
        xpos 900
        yalign -0.3

    en "{cps=30}Jeje si, Eso es lo importante ¿no?"

    show valeria normal:
        xpos -100
        yalign -0.3

    vr "{cps=30}Supongo que si jeje."

    v "{cps=25}Como extraño estos pequeños momentos.."

    v "{cps=25}Como desearia poder volver..."

    show raul normal:
        xpos 900
        yalign -0.3

    en "{cps=30}Oye amor, por cierto, ¿ya pensaste en que es lo que quieres hacer una vez que salgamos de la univercidad?"

    vr "{cps=30}Mmm.. pues supongo que primero quisiera terminar la univercidad y conseguir un buen empleo."

    en "{cps=30}¿Y despues?"

    vr "{cps=30}Despues... no lo sé. Quizá independizarme, viajar un poco y supongo que conocer otros lugares."

    show raul feliz:
        xpos 900
        yalign -0.3

    en "{cps=30}¿Osea que no estoy incluido en esos planes? Ouch."

    show valeria feliz:
        xpos -100
        yalign -0.3

    vr "{cps=30}Jajaja, yo no dije eso!."

    en "{cps=30}Mas te vale jajaja."

    v "{cps=25}Tonto... Claro que estabas incluido en todos y cada uno de mis planes.."

    v "{cps=25}Queria que estubieras en todos..."

    show raul normal:
        xpos 900
        yalign -0.3

    en "{cps=30}Bueno ya, hablando enserio."

    show valeria normal:
        xpos -100
        yalign -0.3

    menu:

        en "{cps=30}¿Cómo imaginas tu futuro?"

        "Hablar sobre sus metas profecionales.":

            vr "{cps=30}Yo si hablaba enserio pero empezaste a bromear."

            show raul feliz:
                xpos 900
                yalign -0.3

            en "{cps=30}Jaja, disculpa."

            vr "{cps=30}Pues como dije, quisiera conseguir un buen empleo."

            vr "{cps=30}Quisiera demostrar de lo que soy capaz."

            vr "{cps=30}Hay gente que espera mucho de mi."

            vr "{cps=30}Y no pienso desepcionarlos."

            show raul normal:
                xpos 900
                yalign -0.3

            en "{cps=30}hmm, me parece admirable."

            en "{cps=30}Confio en que lo lograras."

            vr "{cps=30}jeje Graci.."

            show raul feliz:
                xpos 900
                yalign -0.3

            en "{cps=30}Ademas, asi podre decir que estoy con una exitosa mujer jaja."

            show valeria feliz:
                xpos -100
                yalign -0.3

            vr "{cps=30}Jajaja, gracias tonto rompiste el momento romantico."

            en "{cps=30}Jajajaja"

        "Hablar sobre vivir juntos.":

            vr "{cps=30}Pues, aparte de lo que ya dije."

            vr "{cps=30}Supongo que no estaria mal tal vez.."

            vr "{cps=30}No se... {w=0.4}Tener algun lugar para nosotros."

            vr "{cps=30}Bueno, claro que seria despues de terminar nuestra carrera y eso ¿no?"

            show valeria feliz:
                xpos -100
                yalign -0.3

            vr "{cps=30}Pero.. creo que seria lindo."

            show raul feliz:
                xpos 900
                yalign -0.3

            en "{cps=30}Jeje, si. {w=0.3}Me encanta la idea."

        "Bromear sobre su futuro juntos.":

            vr "{cps=30}Bueno, yo ya dije lo que quiero."

            show valeria feliz:
                xpos -100
                yalign -0.3

            vr "{cps=30}Asi que tendras que terminar tu carrera para poder cumplir con mis caprichos jaja."

            show raul feliz:
                xpos 900
                yalign -0.3

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

    scene bg fondo_parque with fade

    show valeria preocupada:
        xpos -100
        yalign -0.3
    with dissolve

    "{cps=30}2 Semanas despues."

    vr "{cps=30}¿Dónde se metio?"

    vr "{cps=30}Hace rato que deberia de estar aquí?"

    vr "{cps=30}Ah, ahi viene."

    show raul triste at move(1600, -0.3, 2.0, 900), flip with dissolve

    show valeria enojada:
        xpos -100
        yalign -0.3

    vr "{cps=30}Pense que ya no vendrias."

    en "{cps=30}Perdón, tuve que repasar algunos temas ya que pronto tendre los examenes."

    vr "{cps=30}Bien, entiendo. Pero llevamos bastante tiempo ya esperando para salir."

    en "{cps=30}Lo se, lo siento. Es que ultimamente tengo bastantes cosas por hacer."

    vr "{cps=30}Yo tambien las tengo y aun asi intento organizarme para poder venir."

    show raul triste at flip:
        xpos 900
        yalign -0.3

    en "{cps=30}Esta bien, no te enojes, no tienes porque ponerte así."

    show raul triste:
        xpos 900
        yalign -0.3

    show valeria triste at flip:
        xpos -100
        yalign -0.3

    vr "{cps=30}No estoy enojada es solo que... {w=0.4}solamente queria pasar un rato contigo.."

    show raul normal at flip:
        xpos 900
        yalign -0.3

    en "{cps=30}Bueno ya estoy aqui ¿no?, Vamos, no quiero que pasemos el dia discutiendo."

    en "{cps=30}No volvera a pasar, lo prometo."

    v "{cps=20}Mentiroso.."

    v "{cps=25}Esto paso mas de una sola vez.."

    menu:

        "¿Como responde Valeria?"

        "Decir que tambien deberia esforzarce por pasar tiempo juntos.":

            show valeria preocupada:
                xpos -100
                yalign -0.3

            vr "{cps=30}Sabes.. la verdad no me gusta como va todo esto."

            show raul preocupado:
                xpos 900
                yalign -0.3

            en "{cps=30}¿A que te refieres?"

            show valeria enojada:
                xpos -100
                yalign -0.3

            vr "{cps=30}¡A esto¡ dices que no volvera a pasar pero ya ha pasado varias veces antes."

            vr "{cps=30}No siento que te esfuerces tanto como yo lo hago por nuestra relacion."

            en "{cps=30}Claro que me esfuerzo es solo que.. he estado mas ocupado ultimamente."

            vr "{cps=30}Yo tambien, pero no por eso descuido lo nuestro."

            show valeria triste:
                xpos -100
                yalign -0.3

            vr "{cps=30}Creo que deberias esforzarte más por que pasaramos más tiempo juntos."

            show raul triste:
                xpos 900
                yalign -0.3

            en "{cps=30}Si esta bien.. hare lo posible para que asi sea."

        "Dejar pasar el comentario y continuar con su salida.":

            show valeria triste:
                xpos -100
                yalign -0.3

            vr "{cps=30}Hmm, está bien.. tienes razón.."

            vr "{cps=30}No deberiamos pasar nuestro tiempo juntos discutiendo por estas cosas..."
            
            show raul feliz:
                xpos 900
                yalign -0.3

            en "{cps=30}Exacto, lo mejor sera que disfrutemos de lo que podamos."

            show valeria triste at flip:
                xpos -100
                yalign -0.3

            vr "{cps=30}Si.. es cierto..."

        "Preguntar si realmente quiere pasar tiempo con ella.":

            show valeria preocupada:
                xpos -100
                yalign -0.3

            vr "{cps=30}Oye Raúl..."

            vr "{cps=30}¿De verdad quires estar conmigo?"

            show raul preocupado:
                xpos 900
                yalign -0.3

            en "{cps=30}¿Qué?, ¿porqué preguntas eso?"

            en "{cps=30}Por supuesto que que quiero estar contigo."

            show raul triste:
                xpos 900
                yalign -0.3

            en "{cps=30}Es solo que.. no he tenido mucho tiempo libre."

            show valeria triste:
                xpos -100
                yalign -0.3

            en "{cps=30}Y estoy teniendo problemas para organizarme."

    v "{cps=25}A veces me pregunto si es culpa mia.."

    v "{cps=25}¿Acaso yo pedía demaciado por querer estar con él?.."

    #
    # ESCENA 3 - PLANES DEL EX
    #

    scene bg cita_cafe with fade

    show valeria normal:
        xpos -200
        yalign -0.3

    show raul normal:
        xpos 1200
        yalign -0.3

    "Tras ese incidente en su cita su novio la invito a comer para compensarlo."

    en "{cps=30}Oye amor, ¿te he contado que estoy pensando en hacer mis practicas en otro hospital?"

    vr "{cps=30}¿En serio? ¿en cuál?"

    en "{cps=30}Todavia no estoy muy seguro, pero hay uno que me interesa bastante."

    show valeria feliz:
        xpos -200
        yalign -0.3

    vr "{cps=30}Eso es genial, seguro qué lo consigues."

    show raul feliz:
        xpos 1200
        yalign -0.3

    en "{cps=30}Jeje, no lo se. Tendria que esforzarme bastante."

    vr "{cps=30}Confio en que lo puedes lograr."

    en "{cps=30}Gracias. Aunque eso significaria que probablemente tendría menos tiempo libre.."

    show valeria normal:
        xpos -200
        yalign -0.3

    vr "{cps=30}Bueno, tampoco es como si tuvieras mucho ahora mismo."

    show raul normal:
        xpos 1200
        yalign -0.3

    en "{cps=30}Ouch."

    vr "{cps=30}Jajaja, perdona."

    en "{cps=30}Pero enserio.."
    
    menu:

        en "¿crees que podriamos seguir viendonos si tengo que dedicarle mas tiempo a mis practicas?"

        "Podremos encontrar tiempo para nosotros.":

            vr "{cps=30}Claro que si, seria complicado y tendriamos que organizarnos mejor."

            vr "{cps=30}Pero creo que si podriamos."

            vr "{cps=30}Eso si, tendriamos que organizarnos mejor con nuestras salidas."

            show valeria feliz:
                xpos -200
                yalign -0.3

            vr "{cps=30}Y cierto individuo deberá de darle un pequeño espacio aunque sea a su novia jaja."

            show raul feliz:
                xpos 1200
                yalign -0.3

            en "{cps=30}Jaja, si tienes razón, me alegra oir eso."

        "No me gustaria que descuides tus estudios por mi.":

            show valeria preocupada:
                xpos -200
                yalign -0.3

            vr "{cps=30}Pues.. supongo que si seria posible con una mejor organizacion.."

            vr "{cps=30}Pero me preocupa que llegases a descuidar tus estudios por mi.."

            vr "{cps=30}No quisiera importunarte..."

            show raul preocupado:
                xpos 1200
                yalign -0.3

            en "{cps=30}¿Qué? no no, claro que no."

            en "{cps=30}Tu jamas podrias importunarme."

            show raul normal:
                xpos 1200
                yalign -0.3

            show valeria normal:
                xpos -200
                yalign -0.3

            en "{cps=30}Tambien eres importante para mi."

        "Espero que no termines olvidandote de mi.":

            vr "{cps=30}Claro que sí, si ambos nos ponemos en ello seguro que podemos."

            vr "{cps=30}Es cierto que no nos veremos tanto pero creo que si podemos."

            show valeria feliz:
                xpos -200
                yalign -0.3

            vr "{cps=30}Solo espero que no termines olvidadote de mi eh! Jaja.."

            show raul feliz:
                xpos 1200
                yalign -0.3

            en "{cps=30}Jaja, claro que no."

            en "{cps=30}Haria todo lo posible por verte."

    v "{cps=25}El tambien tenia sus propios problemas.."

    v "{cps=25}Tal vez tenga razon.."

    v "{cps=25}Tal vez si era yo la del problema..."

    #
    # ESCENA 4 - PRIMEROS CAMBIOS
    #

    "{cps=30}Con el paso del tiempo sus responsabilidades no hicieron mas que aumentar."

    "{cps=30}Se veian cada vez menos."

    "{cps=30}Y sus charlas se volvian cada vez mas cortas."

    scene bg cuarto_valeria preocupada with fade

    vr "{cps=30}¿Habra terminado ya sus clases?"

    vr "{cps=30}Ultimamente no hemos podido vernos casi nada.."

    vr "{cps=30}Supongo que ambos estamos ocupados.."

    "Bzzz bzzz"

    vr "{cps=30}Creo que ya me contestó."

    scene bg cuarto_valeria celular

    $ mensajes_chat = []

    show screen celular_chat

    $ agregar_mensaje("Raúl", "Perdón, hoy tampoco podré salir. Tengo que estudiar para un examen")

    vr "{cps=30}¿Otra vez?, antes tampoco pudimos porque tenia tareas.."

    $ agregar_mensaje("Valeria", "Esta bien, no te preocupes")

    pause 1.0

    $ agregar_mensaje("Raúl", "Te prometo que cuando termine esta semana tendremos tiempo para nosotros")

    vr "{cps=30}Antes tambien me dijiste que podriamos esta semana.."

    $ agregar_mensaje("Valeria", "Está bien. Mucha suerte con tu examen. Te amo")

    pause 2.0

    $ agregar_mensaje("Raúl", "Yo a tí")

    pause 3.0

    hide screen celular_chat

    vr "{cps=30}No se si deberia darme esperanzas.."

    vr "{cps=30}Es probable que tampoco nos veamos la proxima semana."

    v "{cps=25}Y no me equivocaba.."

    v "{cps=25}No nos pudimos ver hasta mucho despues.."

    #
    # ESCENA 5 - MALESTARES EN CASA
    #

    scene bg cuarto_valeria with fade

    "{cps=30}Pasaron cerca de 2 semanas."

    "{cps=30}Valeria continuo con sus actividades, aunque Valeria habia comenzado a sentirse diferente."

    show valeria normal at move(-400, -0.3, 2.0, 200) with dissolve

    pause 2.0

    show valeria preocupada:
        xpos 200
        yalign -0.3

    vr "{cps=30}Que extraño.. ultimamente me he sentido bastante cansada."

    vr "{cps=30}Debe ser porque he estado muy ocupada."

    vr "{cps=30}Aunque... llevo varios dias sintiendome asi.."

    vr "{cps=30}No sera que..."

    "{cps=30}La posibilidad cruzo su mente. Pero no queria sacar conclusiones apresuradas."

    "{cps=30}Asi que se dispuso a hacer la prueba."

    v "{cps=25}Tenía razón.."

    scene bg prueba with dissolve

    vr "{cps=30}¿Estoy.. Embarazada?"

    v "{cps=25}Antes pensaba que eso me alegraria.."

    v "{cps=25}Pero con todo lo que habia estando pasando.."

    scene bg valeria_ansiedad with dissolve

    vr "{cps=30}No.. esto no puede estar pasando."

    vr "{cps=30}¿Qué pasara con mis estudios? ¿Y con nosotros...?"

    vr "{cps=30}Deberia decirle.. no quisiera estar sola ahora mismo.."

    vr "{cps=30}Pero.. ¿como lo tomará?"

    menu:

        vr "{cps=30}¿Qué deberia hacer?"

        "Buscarlo para hablar inmediatamente.":

            vr "{cps=30}Para ya de poner peros Valeria."

            scene bg valeria_decidida

            vr "{cps=30}Esto es algo importante, no es momento de dudar."

            vr "{cps=30}Debo ir a buscarlo."

            vr "{cps=30}Le dire que estoy embarazada."

        "Esperar el momento adecuado.":

            $ contarNoticia = 2

            vr "{cps=30}No.."

            vr "{cps=30}Es demaciado pronto.."

            scene bg valeria_preocupada

            vr "{cps=30}Tal vez este ocupado ahora.."

            vr "{cps=30}Si, lo mejor sera que espere a que llegue el moemnto."

            "{cps=30}Pasaron los días pero el 'momento' nunca llego."

            "{cps=30}Al final valeria decidio ir a decirle."

        "Pensar en lo que hará antes de contarselo.":

            $ contarNoticia = 3

            vr "{cps=30}No, tal vez.. deba tomarme un tiempo."

            vr "{cps=30}No se como podria reaccionar.."

            scene bg valeria_preocupada

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

    scene bg fondo_parque with fade

    show valeria preocupada:
        xpos -100
        yalign -0.3
    with dissolve
    
    "{cps=30}La hora habia llegado, era momento de contarle."

    if contarNoticia == 1:

        show raul normal at move(1600, -0.3, 1.5, 960)

        en "{cps=30}Valeria."

        en "{cps=30}Dijiste que queria deirme algo ¿no?"

        en "{cps=30}En tu mensaje sonaba a que era algo muy importante."

        en "{cps=30}¿Pasó algo?"

        show valeria triste:
            xpos -100
            yalign -0.3

        vr "{cps=30}Se podria decir que si.."

        v "{cps=25}Iba muy segura de lo que queria decirle.."

        v "{cps=25}Pero en ese momento.. me atrapó el miedo..."

        en "{cps=30}Dime. ¿Qué paso? ¿Te encuentras bien? Pareces bastante preocupada."

    elif contarNoticia == 2:

        vr "{cps=30}No se porque pense que lo mejor seria esperar."

        vr "{cps=30}Cuando podria ser un buen momento para contar algo com esto.."

        vr "{cps=30}.. Oh, parece que allí viene."

        show raul normal at move(1600, -0.3, 1.5, 960)

        en "{cps=30}Valeria. Disculpa la demora."

        en "{cps=30}Justo estaba terminando unos pendientes."

        en "{cps=30}Dime, ¿está todo bien?"

        en "{cps=30}Parecias preocupada en tu mensaje."

        show valeria triste:
            xpos -100
            yalign -0.3

    else:

        vr "{cps=30}Al final no pude pensar en nada más."

        vr "{cps=30}Pero no puedo retrasar mas esto."
        
        vr "{cps=30}Debo decirle y esperar lo mejor.."

        show raul normal at move(1600, -0.3, 1.5, 960)

        en "{cps=30}Hola Valeria."

        en "{cps=30}Perdona la demora."

        en "{cps=30}Estaba terminando unos pendientes."

        show valeria preocupada:
            xpos -100
            yalign -0.3

        vr "{cps=30}Si este.. está bien."

        en "{cps=30}¿Te encuetras bien?, pareces bastante preocupada."

        show valeria triste:
            xpos -100
            yalign -0.3

    vr "{cps=30}Bueno.. es que, no se como decirtelo.."

    en "{cps=30}Tranquila. Sea lo que sea se que podremos sobrellevarlo juntos."

    show valeria triste:
        xpos -100
        yalign -0.3

    vr "{cps=25}Estoy embarazada."

    show raul preocupado:
        xpos 960
        yalign -0.3

    en "{cps=30}¿Estas segura?"
    
    vr "{cps=30}Se que es algo dificil de creer. Yo tampoco se que hacer.."

    en "{cps=30}Pero.. ¿Cómo paso esto?"

    vr "{cps=30}No lo sé, simplemtente pasó."

    show valeria preocupada:
        xpos -100
        yalign -0.3

    vr "{cps=30}Ya no se que pensar.. estoy asustada.."

    en "{cps=30}Es que... no sé que decir."

    v "{cps=25}Lo que sea.."

    v "{cps=25}Cualquier cosa hubiera bastado.."

    v "{cps=25}Solo queria saber que no estaba sola..."

    menu:

        en "{cps=30}..."

        "Necesito saber que puedo contar contigo..":

            en "{cps=30}Si.. por supuesto que si."

            show raul normal:
                xpos 960
                yalign -0.3

            en "{cps=30}Es mi hijo despues de todo ¿no?.."

            v "{cps=20}No se porqué te creí.."

            show valeria triste:
                xpos -100
                yalign -0.3

            vr "{cps=30}Gracias.."

            vr "{cps=30}De verdad, necesitaba escuchar eso.."

        "Quisiera que pensemos juntos que haremos..":

            show raul normal:
                xpos 960
                yalign -0.3

            en "{cps=30}Ah, si.. es cierto."

            en "{cps=30}Tenemos mucho que planear ¿no?.."

            vr "{cps=30}Si.. asi es.."

            show valeria normal:
                xpos -100
                yalign -0.3

            vr "{cps=30}Tendriamos que ver todo el tema de su comida."

            vr "{cps=30}Jugetes.. y todo eso."

            show raul preocupado:
                xpos 960
                yalign -0.3

            en "{cps=30}Si.. pero ¿no crees que es algo pronto para todo eso?"

            en "{cps=30}Es que.. aun faltan muchos meses para que nazca ¿no?"

            show valeria triste:
                xpos -100
                yalign -0.3

            vr "{cps=30}A si.. {w=0.2}claro.. {w=0.2}supongo que tienes razon..."

        "Sé que no tenemos todas las respuestas..":

            show valeria triste:
                xpos -100
                yalign -0.3

            vr "{cps=30}Pero ahora mismo.. quisera que me escuches."

            vr "{cps=30}Se que no hemos pasado mucho tiempo juntos."

            vr "{cps=30}Y se que todo esto es muy repentino pero.."

            show valeria preocupada:
                xpos -100
                yalign -0.3

            vr "{cps=30}De verdad te necesito.."

            show raul normal:
                xpos 960
                yalign -0.3

            en "{cps=30}Si, lo se es solo que... me tomó por sorpresa.."

            en "{cps=30}No se que deberia hacer.."

            en "{cps=30}Pero se que no puedo dejarte sola.."

            show raul preocupado:
                xpos 960
                yalign -0.3

            en "{cps=30}Tendremos que hacerlo juntos."

    vr "{cps=30}Bueno.. tendre que hablar con mis padres."

    show raul preocupado:
        xpos 960
        yalign -0.3

    en "{cps=30}Si, es cierto.. ¿Crees que sea buena idea?"

    vr "{cps=30}No lo sé, pero necesito decírselo"

    show raul normal:
        xpos 960
        yalign -0.3

    en "{cps=30}Claro.. tienes razón."

    en "{cps=30}Bueno.. supongo que tendremos que pensar cómo hacerlo.."

    show valeria normal:
        xpos -100
        yalign -0.3

    vr "{cps=30}Si.. tendremos que pensarlo."

    v "{cps=25}Porque hacerme creer que me ayudarias.."

    v "{cps=25}¿Porque?.."

    v "{cps=25}Despues de ese dia, solo te volviste más distante.."

    v "{cps=25}No contestabas mis mesnajes y cuando te veia en la univercidad solo ponias excusas y te marchabas.."

    v "{cps=25}No tarde en entender que tendria que contarles a mis padres sola.."

    v "{cps=25}No tenia idea de lo que me esperaba..."

    scene bg fondo_marco with fade

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

    scene bg casa_exterior with fade

    "{cps=30}Pasaron unas cuantas semanas."

    "{cps=30}Valeria aun tenia dudas, pero estaba segura de algo."

    show valeria preocupada at move(1600, -0.3, 2.0, 1000), flip with dissolve

    vr "{cps=30}Mis padres deben ser saberlo."

    vr "{cps=30}Llegara un punto en donde se daran cuenta."
    
    scene bg puerta_casa with dissolve

    vr "{cps=30}No puedo vivir ocultandocelo."

    vr "{cps=30}Debo decirles ahora."

    scene bg puerta_madre with dissolve

    "{cps=30}Antes de que abriera la puerta fue recibida por su madre."

    m "{cps=30}Valeria! por fin llegaste, pensabamos que no llegarias a cenar con nosotros."

    scene bg fondo_casa_padres with dissolve

    show madre normal:
        xpos 1100
        yalign -0.33

    show valeria triste at move(-400, -0.3, 1.0, -200) with dissolve

    m "{cps=30}Dime, ¿cómo te fue en la escuela?"

    vr "{cps=30}Ah, hola mamá este, bien.. supongo que bien..."

    show madre preocupada zorder 2:
        xpos 1100
        yalign -0.33

    m "{cps=30}¿Qué sucede hija? ¿Te sientes bien?"

    m "{cps=30}Te véz un poco palida."

    vr "{cps=30}Bueno.. veras, mamá yo..."

    p "{cps=30}¿Ya llego Valeria?"

    show padre normal zorder 1 at move(1600, -0.1, 1.0, 800) with dissolve

    p "{cps=30}Oh, qué beno verte cariño normalmente no alcanzo a verte cuando vas a la universidad."

    show valeria preocupada:
        xpos -200
        yalign -0.3

    vr "{cps=30}em, si. Yo eh.."

    v "{cps=25}Aun recuerdo bien esa sensacion.."

    v "{cps=25}Sentir como las palabras se atoraban en mi garganta.."

    show padre preocupado:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Qué pasa hija? ¿Paso algo en la univercidad?"

    show valeria triste:
        xpos -200
        yalign -0.3

    vr "{cps=30}No exactametne.."

    m "{cps=30}Esta bien cariño tomate tu tiempo."

    vr "{cps=30}Es que... hay algo que tengo que contarles y no se como lo vayan a tomar.."

    p "{cps=30}Valeria, nos estas preocupando, ¿sucedio algo?"

    vr "{cps=30}Es que.. veran yo.."

    vr "{cps=30}Estoy embarazada.."

    show padre shock:
        xpos 800
        yalign -0.1

    show madre sorprendida:
        xpos 1100
        yalign -0.33

    "{cps=30}Por un momento, el silencio dominó en la casa."

    p "{cps=25}¿Qué fue lo que dijite?"

    show valeria preocupada:
        xpos -200
        yalign -0.3

    vr "{cps=30}Yo.. estoy embarazada, papá."

    p "{cps=25}Pero.. {cps=32}¿cómo? {w=0.3}¿Desde cuando?"

    show madre preocupada:
        xpos 1100
        yalign -0.33

    m "{cps=30}Cariño, espera. Déjala hablar."

    #
    # ESCENA 2 - LA DISCUCION
    #

    p "{cps=30}¿Tienes idea de lo que eso significa?"

    vr "{cps=30}Papá, yo.."

    show padre enojado1:
        xpos 800
        yalign -0.1

    p "{cps=30}¡Todavia estás estudiando! ¡Ni siquiera has terminado tu carrera!"

    m "{cps=30}Por favor, dejala explicarnos."

    p "{cps=30}¿Y que se supone que pasara ahora? ¿Qué harás con tus estudios? ¿Cómo piensas mantener a un bebé?"

    show valeria triste:
        xpos -200
        yalign -0.3

    vr "{cps=30}No lo sé.. Yo tambien tengo miedo, pero..."

    show padre enojado3:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Y el muchacho? ¿Él sabe lo que esta pasando?"

    vr "{cps=30}Si, ya hablé con él."

    p "{cps=30}¿Y qué dijo? ¿Se hará responsable?"

    show valeria preocupada:
        xpos -200
        yalign -0.3

    vr "{cps=30}Bueno.. él..."

    v "{cps=30}Una parte de mi ya sabia que no volvería.."

    v "{cps=30}Pero no podia decirles eso..."

    show valeria triste:
        xpos -200
        yalign -0.3

    vr "{cps=30}Dijo que.. que lo pensariamos juntos."

    show padre enojado1:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Eso es todo? ¿Y tú confias en que va a cumplirlo?"

    vr "{cps=30}Pues, yo.."

    show madre molesta:
        xpos 1100
        yalign -0.33

    m "{cps=30}No la presiones así. Ella tambien esta asustada."

    show padre enojado2:
        xpos 800
        yalign -0.1

    p "{cps=30}¡Precisamente por eso estoy preocupado! ¡No quiero que arruine su vida por una decisión que no pensó!"

    v "{cps=30}Para este punto mi madre ya estaba en su limite.."

    show madre enojada:
        xpos 1100
        yalign -0.33

    m "{cps=30}¡Ya basta!"

    show padre enojado1:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Qué?"

    show madre molesta:
        xpos 1100
        yalign -0.33

    m "{cps=30}¿Qué no te das cuenta de que esta intentando pedirnos ayuda?"

    m "{cps=30}No necesita que le grites ni que le recuerdes todo lo que puede salir mal. ¡Ella ya lo sabe!"

    show padre enojado1:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Y que quieres que haga? ¿Qué actue como si no estuviera pasando nada?"

    show madre enojada:
        xpos 1100
        yalign -0.33

    m "{cps=30}¡No! Quiero que la escuches antes de decidir que hacer."

    show valeria preocupada:
        xpos -200
        yalign -0.3

    vr "{cps=30}Mamá.."

    #
    # ESCENA 3 - EXPULCION
    #

    show padre enojado3:
        xpos 800
        yalign -0.1

    p "{cps=30}...No puedo creer que estemos pasando por esto."

    show madre molesta:
        xpos 1100
        yalign -0.33

    m "{cps=30}Es nuestra hija. Necesita que estemos con ella."

    show padre enojado1:
        xpos 800
        yalign -0.1

    p "{cps=30}¡No se como ayudarla si ni siquiera penso en las consecuencias!"

    show valeria triste:
        xpos -200
        yalign -0.3

    vr "{cps=30}Papá, por favor.. yo no quería que las cosas fueran así."

    show padre enojado2:
        xpos 800
        yalign -0.1

    p "{cps=30}¡Entonces debiste pensarlo antes!"

    show madre enojada:
        xpos 1100
        yalign -0.33

    m "{cps=30}¡No le hables así!"

    vr "{cps=30}Yo solamente.. quería contarles porque no sé que hacer."

    show madre molesta:
        xpos 1100
        yalign -0.33

    show padre enojado3:
        xpos 800
        yalign -0.1

    p "{cps=30}¿Entonces en que momento se les ocurrio que seria buena idea tener un bebé?"

    p "{cps=30}Si ya se creen sufucientemente adultos para tener un hijo, entonces tambien deberian serlo para hacerse cargo de sus deciciones."

    show valeria sorprendida:
        xpos -200
        yalign -0.3

    vr "{cps=30}¿Qué...?"

    show madre enojada:
        xpos 1100
        yalign -0.33

    m "{cps=30}¡Erasmo!"

    show padre enojado1:
        xpos 800
        yalign -0.1

    show madre molesta:
        xpos 1100
        yalign -0.33

    p "{cps=30}No puedo seguir fingiendo que nada ha pasado. Si decidiste tomar ese camino no tienes porque quedarte en esta casa."

    v "{cps=20}..."

    show madre enojada:
        xpos 1100
        yalign -0.33

    m "{cps=30}¡No puedes estar hablando en serio! ¡Es tu hija!"

    show padre espalda:
        xpos 800
        yalign -0.1

    p "{cps=30}Necesito que te vayas, Valeria."

    show valeria triste:
        xpos -200
        yalign -0.3

    vr "{cps=30}¿De verdad quieres que me vaya..?"

    vr "{cps=25}Soy tu hija, papá..."

    p "{cps=20}..."

    show madre preocupada:
        xpos 1100
        yalign -0.33

    m "{cps=30}Valeria espera. No tienes porque irte. Podemos hablarlo con más calma."

    show valeria triste at flip:
        xpos -200
        yalign -0.3

    vr "{cps=30}No.. está bien, mamá."

    vr "{cps=30}No quiero que sigan discutiendo por mi culpa."

    #
    # ESCENA 4 - CONSECUENCIAS
    #

    show valeria triste at flip, move(-200, -0.3, 1.0, -860)

    pause 0.5

    show madre preocupada at move(1100, -0.33, 1.5, 200)

    m "{cps=30}..."

    show madre molesta at flip:
        xpos 200
        yalign -0.33

    m "{cps=30}Nuestra hija vino aqui a pedirnos ayuda. y lo unico que se te ocurre es simplemente echarla?"

    m "{cps=30}¿Qué fue lo que pasó por tu cabeza?"

    p "{cps=25}..."

    m "{cps=30}Entiendo que estes preocupado por ella pero eres muy impulsivo."

    m "{cps=30}Siempre lo has sido."

    show madre molesta at flip:
        linear 2.5 xalign 2.5 yalign -4.0

    pause 2.0

    show padre triste at move(800, -0.1, 1.5, 400)

    p "{cps=30}¿Qué es lo que he hecho...?"

    p "{cps=30}Ella vino a nosotros por ayuda.."

    p "{cps=30}Y yo.."

    p "{cps=30}La eché de su propia casa..."

    p "{cps=30}No se que hacer.. No queria que las cosas terminaran asi."

    #
    # ESCENA 5 - DECISION SOBRE EL FUTURO
    #

    scene bg parque_nocturno with fade

    show valeria triste at move(-300, -0.3, 2.0, 200) with dissolve

    v "{cps=25}Despues de todo lo que paso en casa.."

    v "{cps=25}Sentia que estaba completamente sola en esto..."

    vr "{cps=30}Ya no sé que hacer.."

    vr "{cps=30}Pense que podría contar con ellos."

    vr "{cps=30}Mamá intentó ayudarme pero.."

    pause 1.0

    scene bg parque_nocturno triste with dissolve

    vr "{cps=30}¿Y ahora qué voy a hacer?"

    vr "{cps=30}No tengo mucho dinero, todavia estoy estudiando y ya no se que pasara con Raúl.."

    vr "{cps=30}¿Qué hare si no puedo darle lo que necesita a mi bebé?"

    vr "{cps=30}Y tampoco quiero renunciar a todo lo que he trabajado para conseguir.."

    menu:

        vr "{cps=30}¿Qué se supone que haga ahora?"

        "No abandonar sus estudios.":

            vr "{cps=30}No."

            scene bg parque_nocturno decidida

            vr "{cps=30}Dejar todo mi futuro y mis sueños de lado no es opcion."

            vr "{cps=30}Yo puedo. Solo tengo que organizarme ¿no?"

            vr "{cps=30}Claro, planeare mejor mis clases, mis responzabilidades, reducire mis tiempos de descanso"

            vr "{cps=30}Tal vez tenga que sacrificar algunas horas de sueño pero, supongo que no será tan malo ¿no?.."

            scene bg parque_nocturno decaida

            vr "{cps=30}Tendre que saltarme algunas comidas.."

            vr "{cps=30}No veré tanto a mis amigos.. {w=0.6}Ni a mis padres.."

            vr "{cps=30}Yo.. {w=0.6}{cps=25}Yo puedo..."

            v "{cps=25}Esa fue una de las desiciones mas dificiles que habia tomado.."

            v "{cps=25}A veces me pregunto si hice lo correcto.."

            v "{cps=25}Despues de todo.. una madre deberia ver primero por su hijo ¿no?."

            v "{cps=25}Sabiendo eso.."

            v "{cps=25}¿Siquiera puedo considerarme una buena madre...?"

            v "{cps=25}Y al final no sirvio. Reprobe igualmente en multiples ocaciones.."

            v "{cps=25}Esta.. es mi ultima oportunidad..."

        "Priorizar la estabilidad de su bebé.":

            $ eleccionPasado = 2

            vr "{cps=30}¿Qué estoy pensando..?"

            vr "{cps=30}¿De verdad estoy dudando en cual de los 2 priorizar?"

            vr "{cps=30}No puedo pensar solo en mi misma y en lo que quiero."

            scene bg parque_nocturno decidida

            vr "{cps=30}Este bebé debe ser mi prioridad ahora.."

            vr "{cps=30}Tendre que tomarme un tiempo para organizarlo todo."

            scene bg parque_nocturno decaida

            vr "{cps=30}Tal vez.. tenga que tomarme un tiempo de la univercidad..."

            v "{cps=25}Esa fue una de las desiciones mas dificiles que habia tomado.."

            v "{cps=25}Dejar de lado todo lo que habia trabajado por mi bebé.."

            v "{cps=30}Pero no me arrepiento."

            v "{cps=30}Jamas podria arrepentirme de elegir a mi bebé."

            v "{cps=30}Aunque.. Supongo que es por esa desicion que ésta, es mi última oportunidad.."

    vr "{cps=30}No pienses más en ello Valeria."

    scene bg parque_nocturno piernas with dissolve

    vr "{cps=30}No es momento de lloriqueos."

    vr "{cps=25}Ahora mismo yo..."

    a "{cps=30}¿Valeria?"

    vr "{cps=30}!!"

    #
    # ESCENA 6 - REFUGIO
    #

    scene bg parque_nocturno with fade

    show valeria preocupada:
        xpos 200
        yalign -0.3
    
    show veronica normal at move(1300, -0.3, 1.5, 900) with dissolve
    a "{cps=30}¿Qué haces aqui a esta hora? ¿No deberias estar en..?"

    show veronica preocupada:
        xpos 900
        yalign -0.3

    a "{cps=30}¿Te encuentras bien?, ¿sucedio algo?"

    vr "{cps=30}¿Qué? no, yo solo... {w=0.3}Estoy bien.."

    show veronica molesta:
        xpos 900
        yalign -0.3

    a "{cps=30}Valeria, te conozco desde hace mucho timepo. Sabes que no me pudes engañar tan facil."

    a "{cps=30}No tienes porque fingir conmigo. Asi que dime, ¿qué paso?"

    show valeria triste:
        xpos 200
        yalign -0.3

    vr "{cps=30}Es que, yo.. no quisiera preocuparte."

    a "{cps=30}Valeria. Ya me estas preocupando."

    vr "{cps=25}..."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}Vamos, ¿por qué no vienes conmigo? Podemos hablar mas tranquilas en mi casa, ¿sí?"

    show valeria preocupada:
        xpos 200
        yalign -0.3

    vr "{cps=30}No quisiera molestarte con esto.."

    show veronica molesta:
        xpos 900
        yalign -0.3

    a "{cps=30}¡No es ninguna molesita! Además, no pienso dejarte aquí sentada con esa cara."

    show valeria triste:
        xpos 200
        yalign -0.3

    vr "{cps=30}Okey.. está bien."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}Asi se habla. Vamos anda, que ya esta helando aqui fuera."

    v "{cps=30}Nunca pude ganar cuando se trata de ella."

    scene bg sala_vcasa with fade

    pause 0.5

    show veronica normal at flip:
        xpos -200
        yalign -0.3
    with dissolve

    show valeria triste at flip:
        xpos 900
        yalign -0.3
    with dissolve

    v "{cps=30}Me ofrecio bebida y un lugar calido para descansar.."

    v "{cps=30}Se sintió.. {w=0.4}Como volver a respirar tras estarme ahogando."

    v "{cps=30}Despues de un rato le conté todo lo que habia sucedido."

    show veronica molesta at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}¿En serio te dijeron que te fueras?"

    a "{cps=30}Pero... ¡es tu casa tambien! No pudeo creer que tu papá haya hecho algo asi."

    vr "{cps=30}El estaba muy enojado.. supongo que no sabía qué hacer.."

    show veronica molesta2 at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Eso no justifica que te haya echado."

    a "{cps=30}¿Y ahora donde piensas quedarte?"
    
    show veronica preocupada at flip:
        xpos -200
        yalign -0.3

    show valeria preocupada at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}No lo se..."

    vr "{cps=30}No tengo mucho dinero.. Y tamopoco quisiera causarles más problemas."

    show veronica molesta at flip:
        xpos 900
        yalign -0.3

    a "{cps=30}¿Y que hay de Raúl? ¿No puede ayudarte?"

    vr "{cps=30}Yo.. no estoy segura..."

    a "{cps=30}¿No estas segura? ¿A que te refieres con eso?"

    show valeria triste at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}Es que.. despues de contarle lo del embarazo comenzó a alejarse."

    vr "{cps=30}Ya no me contesta los mesnajes.. y ya ni siquiera voltea a verme en la universidad.."

    vr "{cps=30}Pensé que podríamos solucionarlo juntos, pero..."

    show valeria preocupada at flip:
        xpos 900
        yalign -0.3

    vr "{cps=25}Supongo que me equivoqué.."

    show veronica triste at flip:
        xpos -200
        yalign -0.3

    a "{cps=25}Valeria..."

    show valeria triste:
        xpos 900
        yalign -0.3

    vr "{cps=30}Perdón, no quiero hablar más de eso. Lo siento."

    a "{cps=30}No no, al contrario.."

    show veronica avergonzada at flip:
        xpos -200
        yalign -0.3

    a "{cps=25}Perdón, supongo que no debi entrometerme tanto.."

    show valeria burlona at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}Pff jajaja."

    show veronica normal at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}¿Y tu ahora de que te ries..?, ¿te golpeaste la cabeza o algo?"

    show valeria normal at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}Perdóna es que, es la primera vez que te escucho disculpatre."

    show veronica molesta at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}¿Y eso es gracioso?"

    v "{cps=30}Je, tenemos muchos años de conocernos."

    v "{cps=30}Pero con lo terca que eres nunca te habia escuchado disculparte por algo."

    show valeria burlona:
        xpos 900
        yalign -0.3

    vr "{cps=30}No, no, perdón, eso solo que no me lo esperaba, muchas gracias."

    vr "{cps=30}Me alegraste un poco el dia."

    a "{cps=30}Y me estoy arrepintiendo."

    vr "{cps=30}Jaja."

    #
    # ESCENA 7 - PROPUESTA INESPERADA
    #

    show veronica preocupada at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Oye, Valeria..."

    a "{cps=30}¿Por qué no te quedas aquí unos días?"

    show veronica normal at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Puedes quedarte en mi casa."

    show valeria preocupada at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}No, no podria hacer eso..."

    show veronica molesta at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}¿Por qué no? ¿No te gusta mi casa o que?"

    vr "{cps=30}No, no es eso es que.. Ya has hecho mucho por mi."

    show valeria triste at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}No quiero convertirme en una carga.."

    show veronica molesta2 at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}¿Una carga? ¿De verdad piensas que voy a verte sin un lugar donde quedarte y simplemente dejare que te las arregles sola?"

    a "{cps=30}Escucha. No tienes que decidir todo que harás con toda tu vida esta noche."

    show veronica molesta at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Puedes quedarte aqui mientras te organizas. No tienes que preocuparte por eso ahora."

    show valeria preocupada at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}Yo, no lo sé.. no se si deberia aceptar..."

    show veronica normal at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Valeria, somos amigas. ¿Por qué crees que estoy aqui?"

    vr "{cps=25}..."

    show veronica molesta at flip:
        xpos -200
        yalign -0.3

    a "{cps=30}Ademas no voy a dejar que pases la noche en un parque. Eso sí que no es negociable."

    show valeria triste at flip:
        xpos 900
        yalign -0.3

    show veronica normal at flip:
        xpos -200
        yalign -0.3

    vr "{cps=30}Je.. gracias."

    show valeria normal at flip:
        xpos 900
        yalign -0.3

    vr "{cps=30}De verdad. Muchas gracias..."

    a "{cps=30}No hay nada que agradecer Valeria. Ahora vamos a descansar."

    a "{cps=30}Mañana ya pensaremos con más calma qué hacer."
    
    v "{cps=30}Jaja, dijimos que solo serian unos dias pero han pasado meses y sigo viviendo contigo.."

    v "{cps=25}Despues de todo lo que habia pasado.. ella fue la unica que me extendio la mano para ayudarme.."

    v "{cps=25}Perdón Veronica, jamas podre pagarte todo lo que has hecho por mi.."

    scene black with fade

    "{cps=30}Los sueños de Valeria fueron interrumpidos por una voz que la llamaba."

    if biblioteca == True:

        scene bg valeria_biblioteca dormida with circleirisin

        a "{cps=30}¿Valeria?"

        a "{cps=30}¡Valeria!"

        scene bg valeria_biblioteca cansada

        a "{cps=30}Oye, despierta. ¿Qué haces durmiendo aqui?"

        v "{cps=30}¿Mmm...?"

        v "{cps=30}¿Eh..? ¿Donde..?"

        a "{cps=30}En la biblioteca de la univercidad, dormida sobre tu cuaderno. ¿Qué otra cosa podría ser?"

        v "{cps=30}Ah.. ¿Qué hora es?"

        scene bg biblioteca with dissolve

    else:
    
        scene bg vision_valeria veronica with circleirisin

        a "{cps=30}¿Valeria?"

        a "{cps=30}¡Valeria!"

        a "{cps=30}Oye, despierta. ¿Qué haces durmiendo aqui?"

        a "{cps=30}¿Acaso quieres resfriarte?"

        v "{cps=30}¿Mmm...?"

        v "{cps=30}¿Eh..? ¿Donde..?"

        a "{cps=30}En el patio de la univercidad, dormida en una banca. ¿Qué otra cosa podría ser?"

        v "{cps=30}Ah.. ¿Qué hora es?"

        scene bg fondo_parque with dissolve
    
    show valeria_bebe tarde at flip:
        xpos 900
        yalign -0.3
    with dissolve

    show veronica molesta at flip:
        xpos 0
        yalign -0.3
    with dissolve

    a "{cps=30}Las 8:43, ya es bastante tarde."

    show veronica preocupada at flip:
        xpos 0
        yalign -0.3

    a "{cps=30}¿Te encuentras bien? ¿No has estado durmiendo bien?"

    show valeria_bebe normal at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Si.. solamente estaba un poco cansada."

    show veronica molesta2 at flip:
        xpos 0
        yalign -0.3

    a "{cps=30}¿Un poco? estabas completamente dormida, te llame como 7 veces."

    v "{cps=30}¿En serio? jaja.. espera."

    show valeria_bebe preocupada at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}¿Dijiste 8:40?"

    show veronica molesta at flip:
        xpos 0
        yalign -0.3

    a "{cps=30}De hecho 8:43 pero.."

    show valeria_bebe tarde at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Hay no, ya es tarde, mi clase empesaba a las 8:30."

    v "{cps=30}Gracias por despertarme, pero ya debo irme."

    show valeria_bebe tarde at move(900, -0.3, 2.0, 2200)

    v "{cps=30}Nos vemos en casa. ¡Adios!"

    show veronica normal at flip, move(0, -0.3, 2.0, 400)

    a "{cps=30}Ah si claro, adios.."

    show veronica preocupada at flip:
        xpos 400
        yalign -0.3

    a "{cps=30}Hmm, eres todo un caso."

    show veronica molesta at flip:
        xpos 400
        yalign -0.3

    a "{cps=30}¿Qué hare contigo?"

    scene bg fondo_marco with fade

    call screen separador_nivel(
        "04",
        "Preparacion",
        "Los ultimos pasos"
    )

#
# CAPITULO 4
# EL PESO DE UNA ULTIMA OPORTUNIDAD
#

label nivel_4:

    #
    # ESCENA 1 - LLEGANDO TARDE A CLASE
    #

    scene bg salon_clase with fade

    show maestro normal at flip:
        xpos 1200
        yalign -0.3

    pv "{cps=30}No puede ser, otra vez llego tarde..."

    pv "{cps=30}Por favor, que el maestro todavía no haya empezado..."
    
    show valeria_bebe tarde at move(-400, -0.3, 1.0, 0) with dissolve

    v "{cps=30}Disculpe, maestro... ¿Puedo pasar?"
    
    show maestro normal:
        xpos 1200
        yalign -0.3

    ms "{cps=30}Valeria, buenos días."
    
    ms "{cps=30}Adelante, toma asiento. Precisamente estaba hablando sobre las evaluaciones finales."
    
    show valeria_bebe preocupada:
        xpos 0
        yalign -0.3

    v "{cps=30}¿Las evaluaciones...?"
    
    show maestro explicando:
        xpos 1200
        yalign -0.3

    ms "{cps=30}Como les comentaba a sus compañeros, los exámenes finales comenzarán dentro de unos días."
    
    ms "{cps=30}Esta será su última oportunidad para acreditar las materias que tengan pendientes."

    ms "{cps=30}Quienes ya hayan agotado sus oportunidades de recuperación y no aprueben ahora, no podrán solicitar otra evaluación de esta materia."

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3
    
    pv "{cps=30}Lo sé.. Ya no puedo seguir cometiendo errores."
    
    ms "{cps=30}Hoy terminaremos de repasar los temas más importantes, así que les recomiendo prestar atención."
    
    ms "{cps=30}Si tienen alguna duda, aprovechen para preguntarla."
    
    v "{cps=30}Sí, maestro..."

    #
    # RESULTADO DE LAS ACTIVIDADES DEL CAPITULO 1
    #

    if resClase in (1, 3):

        scene bg salon with fade

        show valeria_bebe normal:
            xpos 0
            yalign -0.3
        with dissolve

        show maestro normal at flip, move(1200, -0.3, 2.0, 1100) with dissolve
    
        ms "{cps=30}Valeria, por cierto, ya revisé las actividades que me entregaste."
    
        show valeria_bebe normal:
            xpos 0
            yalign -0.3

        v "{cps=30}¿En serio? ¿Y cómo me fue?"
    
        ms "{cps=30}Bastante bien. Con ellas has conseguido una buena parte de los puntos necesarios."
    
        show valeria_bebe feliz:
            xpos 0
            yalign -0.3

        v "{cps=30}¡Menos mal..!"
    
        show maestro explicando at flip:
            xpos 1100
            yalign -0.3

        ms "{cps=30}Eso sí, todavía necesitas aprobar el examen final."
    
        ms "{cps=30}No te confíes demasiado."
    
        show valeria_bebe normal:
            xpos 0
            yalign -0.3

        v "{cps=30}No lo haré, maestro. Muchas gracias."
    
        show maestro normal at flip:
            xpos -200
            yalign -0.3

        show maestro normal at move()
        
        pv "{cps=30}Bien... por lo menos tengo una preocupación menos."
    
        pv "{cps=30}Solo debo concentrarme en el examen..."

    else:

        show maestro normal at flip, move(1200, -0.3, 1.0, 1100) with dissolve

        ms "{cps=30}Por cierto Valeria, ¿puedo hablar contigo un momento?"

        v "{cps=30}Ah.. sí, claro."

        ms "{cps=30}Revisé tu situación académica. Me temo que todavía tienes varios puntos pendientes."

        show valeria_bebe triste:
            xpos 0
            yalign -0.3

        v "{cps=30}Sí.. lo sé."

        show maestro explicando at flip:
            xpos 1100
            yalign -0.3

        ms "{cps=30}Al no haber entregado todas las actividades, necesitarás una calificación considerablemente más alta en el examen."

        show valeria_bebe tarde:
            xpos 0
            yalign -0.3

        v "{cps=30}¿Cree que todavía pueda lograrlo?"

        show maestro normal at flip:
            xpos 1100
            yalign -0.3

        ms "{cps=30}No puedo asegurártelo. Pero matemáticamente todavía tienes oportunidad."

        ms "{cps=30}Eso sí, no puedes permitirte demasiados errores."

        v "{cps=30}Entiendo..."

        show valeria_bebe triste:
            xpos 0
            yalign -0.3

        pv "{cps=30}Una nota muy alta..."

        pv "{cps=30}¿De verdad podré conseguirla...?"

    #
    # ESCENA 2 - UNA OFERTA FAMILIAR
    #
    
    scene bg salon with fade

    show valeria_bebe normal:
        xpos 900
        yalign -0.3

    "{cps=30}Al terminar la clase, Herneztino se acerca a Valeria."

    show herneztino normal at move(-400, -0.3, 1.0, -100) with dissolve

    c "{cps=30}Oye, Valeria. ¿Tienes un momento?"

    show valeria_bebe normal at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Ah, hola, Herneztino."

    c "{cps=30}¿Cómo te va con los preparativos para los exámenes?"

    show valeria_bebe triste at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Pues... podría irme mejor."

    show herneztino amable:
        xpos -100
        yalign -0.3

    c "{cps=30}Jaja, supongo que estamos en las mismas."

    show herneztino normal:
        xpos -100
        yalign -0.3

    c "{cps=30}Oye, estuve pensando que podríamos estudiar juntos para el examen."

    c "{cps=30}Hay algunos temas que todavía no entiendo muy bien."

    c "{cps=30}Y pensé que podríamos ayudarnos a repasar."

    if aceptarAyuda == True:

        show herneztino amable:
            xpos -100
            yalign -0.3

        c "{cps=30}Además, después de lo de las actividades de la otra clase, creo que hacemos un buen equipo."

        v "{cps=30}Jeje, supongo que tienes razón."

        show valeria_bebe normal at flip:
            xpos 900
            yalign -0.3

        v "{cps=30}La verdad es que aquel día me ayudaste bastante."

        show herneztino normal:
            xpos -100
            yalign -0.3

        c "{cps=30}Pues podríamos repetirlo, ¿no?"

    else:

        c "{cps=30}Sé que la otra vez preferiste encargarte de las cosas por tu cuenta."

        show herneztino amable:
            xpos -100
            yalign -0.3

        c "{cps=30}Pero pensé que tal vez ahora te vendría bien alguien con quien repasar."

        v "{cps=30}Ah..."

        show valeria_bebe tarde at flip:
            xpos 900
            yalign -0.3

        pv "{cps=30}¿Por qué sigue preocupándose tanto por mí?"

        show herneztino normal:
            xpos -100
            yalign -0.3

        c "{cps=30}Claro, si prefieres estudiar sola, también lo entiendo."

    #
    # ELECCION 1 - COMO RESPONDER A HERNEZTINO
    #

    menu:
        "Aceptar estudiar juntos.":

            $ estudioConHerneztinoC4 = True
            $ estudios += 2
            $ estres -= 1

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Bueno... supongo que podría venir bien estudiar con alguien más."

            show herneztino amable:
                xpos -100
                yalign -0.3

            c "{cps=30}¡Genial!"

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Aunque te advierto que hay bastantes cosas que todavía no entiendo."

            show herneztino normal:
                xpos -100
                yalign -0.3

            c "{cps=30}Jaja, tranquila, yo tampoco soy ningún genio."

            c "{cps=30}Podemos ayudarnos entre los dos."

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Jeje, está bien. Muchas gracias."

            show herneztino amable:
                xpos -100
                yalign -0.3

            c "{cps=30}¡Perfecto! Entonces nos vemos mañana en la biblioteca."

            show valeria_bebe feliz at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Sí, nos vemos."
            
            show herneztino normal at flip, move(-100, -0.3, 1.0, -860)

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3

            pv "{cps=30}Quizá estudiar acompañada no sea tan mala idea..."

        "Estudiar por cuenta propia.":

            $ estudios += 1

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Gracias por ofrecerte, pero creo que esta vez prefiero estudiar por mi cuenta."

            show valeria_bebe triste at flip:
                xpos 900
                yalign -0.3
    
            v "{cps=30}Tengo varios pendientes y no sé si podría organizarme para reunirnos."
    
            c "{cps=30}Ah, entiendo."

            show herneztino amable:
                xpos -100
                yalign -0.3
    
            c "{cps=30}Bueno, si cambias de opinión, puedes avisarme."

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3
    
            v "{cps=30}Claro, muchas gracias."
    
            c "{cps=30}¡Mucha suerte!"

            show herneztino normal at flip, move(-100, -0.3, 1.0, -860)

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3
    
            pv "{cps=30}Espero haber tomado una buena decisión..."

        "Intercambiar apuntes.":
    
            $ apuntesHerneztinoC4 = True
            $ estudios += 1
            $ estres -= 1

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Me gustaría, pero la verdad es que no estoy segura de tener tiempo para reunirnos."
        
            c "{cps=30}Mmm... ¿Y si intercambiamos nuestros apuntes?"
        
            v "{cps=30}¿Nuestros apuntes?"

            show herneztino amable:
                xpos -100
                yalign -0.3
        
            c "{cps=30}Sí, así podemos revisar lo que nos falte sin tener que reunirnos."

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3
        
            v "{cps=30}Ah, eso podría funcionar."

            show herneztino normal:
                xpos -100
                yalign -0.3
        
            c "{cps=30}¡Perfecto! Te enviaré los míos cuando llegue a casa."
        
            show valeria_bebe feliz at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}Muchas gracias, Herneztino."

            show herneztino amable:
                xpos -100
                yalign -0.3
        
            c "{cps=30}No hay de qué."

    #
    # ESCENA 3 - REGRESAR A CASA
    #

    scene bg sala_vcasa with fade

    show veronica normal at flip:
        xpos 1100
        yalign -0.3
    with dissolve

    pause 0.5

    show valeria_bebe tarde at move(-400, -0.3, 1.0, 0) with dissolve

    show veronica normal:
        xpos 1100
        yalign -0.3

    a "{cps=30}!!"

    a "{cps=30}¡Valeria! que bueno que llegas."

    show veronica preocupada:
        xpos 1100
        yalign -0.3

    a "{cps=30}¿Y esa cara? ¿Otra vez fue un día pesado?"

    show valeria_bebe triste:
        xpos 0
        yalign -0.3

    v "{cps=30}Un poco..."

    show veronica molesta:
        xpos 1100
        yalign -0.3

    a "{cps=30}¿Un poco, dices?"

    show valeria_bebe normal:
        xpos 0
        yalign -0.3

    v "{cps=30}Jaja, está bien, bastante."

    show veronica normal:
        xpos 1100
        yalign -0.3

    a "{cps=30}Eso tiene más sentido."

    a "{cps=30}Oye, por cierto, ¿cómo te fue en clases?"

    v "{cps=30}Bueno... el maestro nos recordó que los exámenes finales ya están muy cerca."

    show veronica preocupada:
        xpos 1100
        yalign -0.3

    a "{cps=30}¿Los finales? ¿Ya?"

    v "{cps=30}Sí..."

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3

    v "{cps=30}Y si repruebo esta vez..."

    show veronica molesta:
        xpos 1100
        yalign -0.3

    a "{cps=30}¿Qué pasa?"

    show valeria_bebe triste:
        xpos 0
        yalign -0.3

    v "{cps=30}Ya no podré recuperar esa materia."

    v "{cps=30}He tenido tantas oportunidades..."

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3

    v "{cps=30}Y no he podido aprovecharlas como debería."

    show veronica preocupada:
        xpos 1100
        yalign -0.3

    a "{cps=30}Valeria..."

    v "{cps=30}A veces siento que no importa cuánto me esfuerce."

    v "{cps=30}Siempre hay algo que termina saliendo mal."

    show veronica normal:
        xpos 1100
        yalign -0.3

    a "{cps=30}Bueno, tampoco es como si hubieras estado perdiendo el tiempo."

    a "{cps=30}Tienes clases, tareas, un bebé y un montón de cosas que hacer."

    a "{cps=30}Es normal que estés cansada."

    show valeria_bebe triste:
        xpos 0
        yalign -0.3

    v "{cps=30}Pero hay otras personas que pueden hacerlo..."

    show veronica molesta2:
        xpos 1100
        yalign -0.3

    a "{cps=30}Y otras que no pueden. No tienes que compararte con todo el mundo."

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3

    v "{cps=30}Supongo..."

    show veronica preocupada:
        xpos 1100
        yalign -0.3

    a "{cps=30}Bueno, ¿qué tienes pensado hacer?"

    v "{cps=30}Eso es lo que todavía no sé..."

    #
    # RECUERDO DE LA DECISION DEL CAPITULO 3
    #

    if eleccionPasado == 1:

        pv "{cps=30}Cuando me enteré del embarazo, me prometí que no dejaría mis estudios."

        pv "{cps=30}Pensé que solo necesitaba esforzarme más..."

        show valeria_bebe triste:
            xpos 0
            yalign -0.3

        pv "{cps=30}Pero nunca imaginé que terminaría tan agotada."

        pv "{cps=30}Quizá debí haber hecho las cosas de otra manera..."

    elif eleccionPasado == 2:

        pv "{cps=30}Cuando me enteré del embarazo, decidí tomarme un tiempo de la universidad."

        pv "{cps=30}Creí que cuando regresara podría recuperar el ritmo..."

        pv "{cps=30}Pero había olvidado tantas cosas..."

        show valeria_bebe triste:
            xpos 0
            yalign -0.3

        pv "{cps=30}Ahora que he llegado hasta aquí, no quiero perder esta oportunidad."

    #
    # ESCENA 4 - LA NOCHE ANTES DE ESTUDIAR
    #

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3

    v "{cps=30}Tengo que repasar varios temas..."

    v "{cps=30}Pero también tengo cosas que preparar para mañana."

    show veronica molesta:
        xpos 1100
        yalign -0.3

    a "{cps=30}Oye, no has descansado desde que llegaste."

    show veronica normal:
        xpos 1100
        yalign -0.3

    a "{cps=30}¿Por qué no te sientas un rato?"

    show valeria_bebe triste:
        xpos 0
        yalign -0.3

    v "{cps=30}No puedo, todavía tengo mucho que hacer."

    show veronica molesta:
        xpos 1100
        yalign -0.3

    a "{cps=30}Valeria, puedes tomarte unos minutos."

    v "{cps=30}Lo sé, pero..."

    show valeria_bebe tarde:
        xpos 0
        yalign -0.3

    v "{cps=30}Tengo miedo de no alcanzar a estudiar todo."

    show veronica preocupada:
        xpos 1100
        yalign -0.3

    a "{cps=30}Mmm..."

    a "{cps=30}Bueno, entonces tendremos que organizarnos."

    #
    # ELECCION 2 - COMO APROVECHAR EL TIEMPO
    #

    menu:

        "Estudiar durante toda la noche.":

            $ estudios += 2
            $ estres += 2

            show valeria_bebe normal:
                xpos 0
                yalign -0.3

            v "{cps=30}Creo que lo mejor será aprovechar toda la noche para estudiar."

            show veronica molesta:
                xpos 1100
                yalign -0.3

            a "{cps=30}¿Toda la noche?"

            show valeria_bebe tarde:
                xpos 0
                yalign -0.3

            v "{cps=30}Sí... tengo demasiados temas pendientes."

            a "{cps=30}Valeria, mañana también tienes cosas que hacer."

            show valeria_bebe triste:
                xpos 0
                yalign -0.3

            v "{cps=30}Lo sé, pero no puedo reprobar."

            show veronica molesta2:
                xpos 1100
                yalign -0.3

            a "{cps=30}Y tampoco puedes presentarte al examen sin haber dormido."

            show valeria_bebe tarde:
                xpos 0
                yalign -0.3

            v "{cps=30}Solo será por esta vez..."

            show veronica molesta:
                xpos 1100
                yalign -0.3

            a "{cps=30}Eso dijiste la semana pasada."

            v "{cps=30}..."

            a "{cps=30}No voy a impedir que estudies, pero al menos haz descansos."

            show valeria_bebe triste:
                xpos 0
                yalign -0.3

            v "{cps=30}Sí... intentaré hacerlo."

            pv "{cps=30}No importa cuánto me canse..."

            pv "{cps=30}Debo conseguirlo."

            pause 0.6

            scene bg fondo_casa with fade

            show valeria_bebe normal:
                xpos 400
                yalign -0.3
            with dissolve

            "{cps=30}Al terminar de estudiar..."

            v "{cps=30}Bien... creo que ya terminé la mayoría."

            show valeria_bebe tarde:
                xpos 400
                yalign -0.3

            v "{cps=30}Aunque siento que mis ojos ya no pueden mantenerse abiertos..."

            pv "{cps=30}Mañana podré descansar..."

        "Organizar las actividades y pedir apoyo a Verónica.":

            $ estudios += 1
            $ cuidado_bebe += 1
            $ estres -= 1
            $ apoyoVeronicaC4 = True

            show valeria_bebe normal:
                xpos 0
                yalign -0.3

            v "{cps=30}Tal vez podría organizar los temas que me faltan..."

            v "{cps=30}Y... si no estás ocupada..."

            show veronica normal:
                xpos 1100
                yalign -0.3

            a "{cps=30}¿Sí?"

            v "{cps=30}¿Podrías ayudarme con el bebé durante un rato?"

            show veronica preocupada:
                xpos 1100
                yalign -0.3

            a "{cps=30}¿En serio me estás preguntando eso?"

            show valeria_bebe tarde:
                xpos 0
                yalign -0.3

            v "{cps=30}Bueno, no quiero molestarte..."

            show veronica normal:
                xpos 1100
                yalign -0.3

            a "{cps=30}Valeria, vivimos juntas. Claro que puedo ayudarte."

            a "{cps=30}Tengo algunas cosas que terminar, pero puedo cuidarlo mientras estudias."

            show valeria_bebe normal:
                xpos 0
                yalign -0.3

            v "{cps=30}¿De verdad?"

            a "{cps=30}Sí. Tú estudia y cuando termine con mis pendientes vemos qué falta."

            show valeria_bebe feliz:
                xpos 0
                yalign -0.3

            v "{cps=30}Gracias..."

            show veronica preocupada:
                xpos 1100
                yalign -0.3

            a "{cps=30}Pero con una condición."

            show valeria_bebe normal:
                xpos 0
                yalign -0.3

            v "{cps=30}¿Cuál?"

            show veronica normal:
                xpos 1100
                yalign -0.3

            a "{cps=30}Que no te quedes despierta hasta las tres de la mañana."

            show valeria_bebe feliz:
                xpos 0
                yalign -0.3

            v "{cps=30}Jaja, está bien."

            show veronica molesta:
                xpos 1100
                yalign -0.3

            a "{cps=30}No estoy bromeando."

            v "{cps=30}¡Lo sé, lo sé!"

            pause 0.6

            scene bg fondo_casa with fade

            show valeria_bebe normal:
                xpos 300
                yalign -0.3
            with dissolve

            show veronica normal:
                xpos 1100
                yalign -0.3
            with dissolve

            "{cps=30}Después de estudiar..."

            v "{cps=30}Bien... avancé bastante."

            show valeria_bebe feliz:
                xpos 300
                yalign -0.3

            v "{cps=30}Tal vez todavía me falten algunas cosas, pero creo que entiendo mejor los temas."

            a "{cps=30}¡Perfecto! Entonces a dormir."

            show valeria_bebe normal:
                xpos 300
                yalign -0.3

            v "{cps=30}Jaja, está bien."

        "Atender las necesidades del bebé y descansar.":

            $ cuidado_bebe += 2
            $ estres -= 2

            v "{cps=30}Creo que... hoy necesito descansar un poco."
    
            v "{cps=30}Últimamente he estado tan ocupada que apenas puedo pasar tiempo tranquila con mi bebé."
    
            v "{cps=30}Y sinceramente... estoy agotada."

            show veronica normal:
                xpos 1100
                yalign -0.3
            with dissolve
    
            a "{cps=30}Bueno, por fin dices algo sensato."

            show valeria_bebe feliz:
                xpos 0
                yalign -0.3
    
            v "{cps=30}Jaja, no seas así."
    
            a "{cps=30}Es broma."
    
            a "{cps=30}Anda, ve a descansar. Yo termino de ordenar esto."

            show valeria_bebe normal:
                xpos 0
                yalign -0.3
    
            v "{cps=30}Gracias, Verónica."

            scene bg fondo_casa with fade

            show valeria_bebe normal:
                xpos 400
                yalign -0.3
            with dissolve

            "{cps=30}Más tarde..."

            show valeria_bebe feliz:
                xpos 400
                yalign -0.3
    
            v "{cps=30}Ah... mucho mejor."
    
            v "{cps=30}Parece que tú también necesitabas descansar, ¿verdad, bebé?"
    
            b "{cps=30}Mmm..."

            show valeria_bebe normal:
                xpos 400
                yalign -0.3
    
            v "{cps=30}Jeje..."
    
            pv "{cps=30}Todavía tengo varios temas pendientes..."
    
            pv "{cps=30}Pero al menos ahora puedo pensar con más claridad."
    
            pv "{cps=30}Mañana tendré que aprovechar bien el tiempo."

    #
    # ESCENA 5 - UNA LLAMADA INESPERADA
    #

    scene bg sala_vcasa dia with fade

    show valeria_celular normal at flip:
        xpos 900
        yalign -0.3
    with dissolve

    v "{cps=30}¿Mmm? ¿Mi teléfono?"

    show valeria_celular duda at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}¿Mamá...?"
    
    pv "{cps=30}Hace tiempo que no hablamos tranquilamente..."
    
    pv "{cps=30}No sé si debería contestar..."

    #
    # ELECCION 3 - RESPONDER O POSPONER LA LLAMADA
    #

    menu:
    
        "Contestar la llamada.":
    
            $ habloConMamaC4 = True
            $ estres -= 1

            show valeria_celular preocupada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}¿Hola...?"

            m "{cps=30}¡Valeria! Cariño, qué bueno que contestaste."

            v "{cps=30}Hola, mamá."

            m "{cps=30}¿Cómo estás? ¿Y cómo está mi nietecito?"

            show valeria_celular preocupada2 at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Estamos bien... un poco cansados, pero bien."

            m "{cps=30}Me alegro mucho, hija."

            m "{cps=30}Oye, quería preguntarte cómo te está yendo en la universidad."

            show valeria_celular preocupada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Pues... podría estar mejor."

            m "{cps=30}¿Sucede algo?"

            show valeria_celular explicando at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Es que mis exámenes finales ya están muy cerca."

            v "{cps=30}Y... si no los apruebo, ya no podré recuperar una de las materias."

            m "{cps=30}Oh, hija..."

            show valeria_celular insegura at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Tengo miedo, mamá."

            show valeria_celular preocupada2 at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}He intentado tantas veces..."

            m "{cps=30}Lo sé, cariño."

            m "{cps=30}Pero quiero que sepas que, pase lo que pase, no tienes que enfrentarlo sola."

            show valeria_celular preocupada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Gracias, mamá..."

            m "{cps=30}Y Valeria..."

            show valeria_celular preocupada2 at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}¿Sí?"

            m "{cps=30}Quiero pedirte perdón por lo que pasó aquella noche."

            show valeria_celular preocupada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Mamá, tú no..."

            m "{cps=30}Déjame terminar, cariño."

            m "{cps=30}Debí haberme asegurado de que estuvieras bien. No debí permitir que te marcharas de aquella manera."

            show valeria_celular preocupada2 at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}..."

            m "{cps=30}Tu padre también está muy arrepentido."

            v "{cps=30}¿Papá...?"

            m "{cps=30}Sí. Ha querido hablar contigo desde hace tiempo."

            m "{cps=30}Pero no sabe cómo acercarse después de lo que sucedió."

            show valeria_celular preocupada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Yo tampoco sé si estoy preparada para hablar con él..."

            m "{cps=30}Lo entiendo."

            m "{cps=30}No tienes que hacerlo ahora."

            m "{cps=30}Solo quiero que sepas que te queremos."

            show valeria_celular aliviada at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Gracias, mamá."

            m "{cps=30}Te deseo mucha suerte con los exámenes, hija."

            v "{cps=30}Gracias... de verdad."

            show valeria_celular aliviada_celular at flip:
                xpos 900
                yalign -0.3

            pv "{cps=30}Hace mucho tiempo que no hablábamos así..."

            pv "{cps=30}Me alegra haber contestado."

        "Dejar la conversación para después.":

            pv "{cps=30}..."

            show valeria_celular negativo at flip:
                xpos 900
                yalign -0.3
    
            pv "{cps=30}Perdón, mamá..."
    
            pv "{cps=30}Ahora mismo no creo que pueda hablar sobre todo lo que pasó."
    
            pv "{cps=30}Tengo que concentrarme en los exámenes."
    
            pv "{cps=30}Cuando termine todo esto... intentaré llamarte."

    #
    # ESCENA 6 - EL ULTIMO REPASO
    #

    if estudioConHerneztinoC4 == True:

        scene bg biblioteca with fade

        show herneztino amable:
            xpos 100
            yalign -0.3
        with dissolve

        show valeria_bebe normal at flip, move(1600, -0.3, 1.5, 1000) with dissolve
    
        c "{cps=30}¡Valeria! Por aquí."
    
        v "{cps=30}Hola, disculpa si te hice esperar."
    
        show herneztino normal:
            xpos 100
            yalign -0.3

        c "{cps=30}No te preocupes, apenas llegué."
    
        c "{cps=30}Bueno, ¿por dónde empezamos?"
    
        v "{cps=30}Mmm... creo que me gustaría revisar los temas de la última unidad."
    
        show herneztino amable:
            xpos 100
            yalign -0.3

        c "{cps=30}¡Perfecto! Justo esos son los que más me cuestan."
    
        show valeria_bebe feliz at flip:
            xpos 1000
            yalign -0.3

        v "{cps=30}Jaja, entonces estamos igual."
    
        show herneztino normal:
            xpos 100
            yalign -0.3

        c "{cps=30}Oye, ¿y cómo te has sentido últimamente?"

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3
    
        v "{cps=30}¿Eh? ¿Por qué lo preguntas?"
    
        c "{cps=30}No sé... parecía que estabas algo preocupada estos días."

        show valeria_bebe tarde at flip:
            xpos 1000
            yalign -0.3
    
        v "{cps=30}Ah... son los exámenes."

        show herneztino mcabeza:
            xpos 100
            yalign -0.3
    
        c "{cps=30}Sí, supongo que todos estamos nerviosos."
    
        v "{cps=30}Es que... para mí es un poco diferente."

        show valeria_bebe triste at flip:
            xpos 1000
            yalign -0.3
    
        v "{cps=30}Si repruebo esta vez, ya no podré volver a presentar la materia."

        show herneztino preocupado:
            xpos 100
            yalign -0.3
    
        c "{cps=30}¿En serio...?"
    
        v "{cps=30}Sí..."
    
        c "{cps=30}Vaya... no sabía que tu situación fuera tan complicada."

        show valeria_bebe tarde at flip:
            xpos 1000
            yalign -0.3
    
        v "{cps=30}Je... tampoco es como si fuera algo de lo que me guste hablar."
    
        c "{cps=30}Entiendo."

        show herneztino normal:
            xpos 100
            yalign -0.3
    
        c "{cps=30}Bueno, no puedo prometerte que aprobarás."
    
        c "{cps=30}Pero sí puedo ayudarte a entender lo que nos falta."

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3
    
        v "{cps=30}Gracias, Herneztino."

        show herneztino amable:
            xpos 100
            yalign -0.3
    
        c "{cps=30}¡De nada! Ahora sí, vamos con todo."

        scene black with fade

        scene bg biblioteca with fade

        show valeria_bebe normal:
            xpos 400
            yalign -0.3
        with dissolve

    else:
    
        scene bg biblioteca with fade

        show valeria_bebe normal:
            xpos 400
            yalign -0.3
        with dissolve

        v "{cps=30}Bien... creo que ya tengo todo lo necesario."
    
        v "{cps=30}Voy a comenzar con los temas que todavía no domino."
    
        pv "{cps=30}Esta vez no puedo permitirme distraerme.."
    
        pv "{cps=30}Aunque tampoco me gustaria volver a terminar completamente agotada.."

        if estudios >= 3:

            scene bg valeria_biblioteca estudiando with dissolve
    
            v "{cps=30}A ver... este problema se resuelve utilizando lo que vimos en la segunda unidad."
    
            scene bg valeria_biblioteca alegre

            v "{cps=30}¡Ah, ya entendí!"
    
            v "{cps=30}Creo que por fin estoy empezando a comprenderlo."

            scene bg biblioteca with fade

            show valeria_bebe normal:
                xpos 400
                yalign -0.3
            with dissolve

        else:
    
            scene bg valeria_biblioteca estudiando with dissolve

            pause 0.6

            scene bg valeria_biblioteca preocupada

            v "{cps=30}¿Qué...?"
    
            v "{cps=30}No recuerdo haber visto esto..."
    
            v "{cps=30}¿Acaso estaba en alguna de las clases que falté?"
    
            pv "{cps=30}No puedo pasarme toda la tarde buscando cada respuesta..."
    
            pv "{cps=30}Tendré que concentrarme en lo más importante."

            scene bg biblioteca with fade

            show valeria_bebe tarde:
                xpos 400
                yalign -0.3
            with dissolve

    #
    # CIERRE DEL CAPITULO 4
    #

    v "{cps=30}Bueno... creo que ya no puedo hacer mucho más por hoy."
    
    v "{cps=30}He estudiado todo lo que he podido."

    show valeria_bebe triste at flip:
        xpos 400
        yalign -0.3
    
    v "{cps=30}Pero todavía tengo miedo..."
    
    pv "{cps=30}Todas esas noches en las que me quedé despierta..."
    
    pv "{cps=30}Todas las veces que pensé en abandonar..."
    
    pv "{cps=30}Y las personas que me han ayudado a llegar hasta aquí..."

    show valeria_bebe tarde:
        xpos 400
        yalign -0.3
    
    v "{cps=30}Mañana será el día..."
    
    v "{cps=30}Por favor..."
    
    v "{cps=30}Que todo este esfuerzo no haya sido en vano..."

    call screen separador_nivel(
        "05",
        "Una ultima oportunidad",
        "Solo una vez más Valeria"
    )

    jump nivel_5

#
# CAPITULO 5
# UNA ULTIMA OPORTUNIDAD
#

label nivel_5:

    #
    # ESCENA 1 - LA MANANA DEL EXAMEN
    #

    scene bg sala_vcasa despierta with fade

    v "{cps=30}Mmm..."
    
    v "{cps=30}¿Ya es de día...?"
    
    v "{cps=30}..."

    scene bg sala_vcasa celular
    
    v "{cps=30}¡Hoy son los exámenes!"

    scene bg sala_vcasa dia with dissolve

    show valeria_bebe tarde with dissolve:
        xpos 200
        yalign -0.3
    
    v "{cps=30}Está bien, Valeria. Tranquila."
    
    v "{cps=30}Solo tengo que prepararme y llegar a tiempo."
    
    v "{cps=30}¿Verdad, bebé?"
    
    b "{cps=30}Mmm... ah."

    show valeria_bebe normal:
        xpos 200
        yalign -0.3
    
    v "{cps=30}Jeje, buenos días para ti también."
    
    v "{cps=30}Muy bien. Revisemos que tengamos todo."

    #
    # OBJETOS SEGUN DECISION DEL CAPITULO 1
    #

    if objValeria == True:
    
        $ estres += 1
    
        v "{cps=30}Bien, tengo mis apuntes, lápiz, borrador..."

        show valeria_bebe preocupada:
            xpos 200
            yalign -0.3
    
        v "{cps=30}¿Y el chupón?"
    
        v "{cps=30}..."

        show valeria_bebe tarde:
            xpos 200
            yalign -0.3
    
        v "{cps=30}Ay, no..."
    
        v "{cps=30}¡Otra vez olvidé revisar bien la pañalera!"

        show valeria_bebe triste:
            xpos 200
            yalign -0.3
    
        b "{cps=30}Snif... snif..."
    
        v "{cps=30}No, no, bebé, espera un momento."
    
        v "{cps=30}Tal vez pueda encontrarlo antes de salir..."
        
        #
        # ELECCION - BUSCAR EL CHUPON
        #

        menu:

            "Buscar el chupón antes de salir.":

                v "{cps=30}Estoy segura de que tiene que estar por aquí..."

                v "{cps=30}A ver... ¿Dónde lo dejé?"

                if cuidado_bebe >= 2:

                    v "{cps=30}¡Ah, espera!"

                    show valeria_bebe tarde at flip, move(200, -0.3, 1.5, -860)

                    v "{cps=30}¡Creo que dejé uno de repuesto en la pañalera!"

                    pause 1.0

                    v "{cps=30}¡Aquí está!"

                    $ cuidado_bebe += 1
                    $ estres -= 1

                    show valeria_bebe feliz at move(-860, -0.3, 2.0, 200)

                    v "{cps=30}Jeje, menos mal que había guardado otro."

                    v "{cps=30}¿Ves, bebé? Ya está todo bien."

                    b "{cps=30}Mmm..."

                    show valeria_bebe normal:
                        xpos 200
                        yalign -0.3

                    v "{cps=30}Ahora sí, tenemos que irnos."

                    show valeria_bebe normal at move(200, -0.3, 2.0, -860)

                    scene bg fondo_universidad with fade

                    show valeria_bebe normal at move(-400, -0.3, 2.0, 700) with dissolve

                    v "{cps=30}Menos mal no llegue tan tarde"

                    v "{cps=30}Aun asi debo darme prisa. Andando."

                else:

                    v "{cps=30}¿Dónde está...?"

                    v "{cps=30}Estoy segura de que lo había visto por aquí..."

                    v "{cps=30}..."

                    show valeria_bebe tarde:
                        xpos 200
                        yalign -0.3

                    v "{cps=30}No puede ser, no lo encuentro..."

                    $ estres += 1

                    show valeria_bebe llorando:
                        xpos 200
                        yalign -0.3

                    b "{cps=30}¡Waaa!"

                    v "{cps=30}Ay, bebé, espera..."

                    v "{cps=30}No podemos seguir buscando, se nos está haciendo tarde."

                    v "{cps=30}Tendré que encontrar otra manera de tranquilizarte."

                    show valeria_bebe triste at move(200, -0.3, 1.5, -860)

                    scene bg fondo_universidad with fade

                    show valeria_bebe normal at move(-400, -0.3, 2.0, 700) with dissolve

                    v "{cps=30}Menos mal no llegue tan tarde"

                    v "{cps=30}Aun asi debo darme prisa. Andando."

            "Intentar tranquilizar al bebé sin el chupón.":

                v "{cps=30}No creo que tengamos tiempo para seguir buscando..."

                show valeria_bebe carga_llorando:
                    xpos 200
                    yalign -0.3

                v "{cps=30}Ven aquí, cariño."

                show valeria_bebe carga_calma:
                    xpos 200
                    yalign -0.3

                b "{cps=30}Snif... snif..."

                v "{cps=30}Shhh... tranquilo, aquí estoy."

                v "{cps=30}Ya sé, ya sé..."

                v "{cps=30}Mamá también está un poco nerviosa."

                v "{cps=30}Pero tenemos que calmarnos, ¿sí?"

                b "{cps=30}Mmm..."

                v "{cps=30}Eso es..."

                show valeria_bebe carga_alivio:
                    xpos 200
                    yalign -0.3

                v "{cps=30}Muy bien, mi amor."

                $ cuidado_bebe += 1
                $ estres -= 1

                v "{cps=30}Jeje, parece que ya estás más tranquilo."

                show valeria_bebe normal:
                    xpos 200
                    yalign -0.3

                v "{cps=30}Ahora tenemos que irnos antes de que sea demasiado tarde."

                show valeria_bebe normal at move(200, -0.3, 1.5, -860)

                scene bg fondo_universidad with fade

                show valeria_bebe normal at move(-400, -0.3, 2.0, 700) with dissolve

                v "{cps=30}Menos mal no llegue tan tarde"

                v "{cps=30}Aun asi debo darme prisa. Andando."

    elif objBebe == True:
    
        $ estres += 1
    
        v "{cps=30}A ver... pañales, toallitas, biberón..."
    
        v "{cps=30}Muy bien, parece que tenemos todo."
    
        v "{cps=30}Ahora solo necesito mi lápiz y..."
    
        v "{cps=30}..."

        show valeria_bebe preocupada:
            xpos 200
            yalign -0.3
    
        v "{cps=30}¿Dónde está mi lápiz?"
    
        v "{cps=30}No puede ser..."
    
        show valeria_bebe tarde:
            xpos 200
            yalign -0.3

        v "{cps=30}Justo hoy tenía que olvidar algo..."
    
        pv "{cps=30}Tengo que conseguir uno antes de que comience el examen..."
        
        #
        # ELECCION - CONSEGUIR UN LAPIZ
        #

        menu:

            "Buscar un lápiz de repuesto en casa.":

                show valeria_bebe triste:
                    xpos 200
                    yalign -0.3

                v "{cps=30}Tal vez todavía tenga alguno guardado..."

                show valeria_bebe triste :
                    linear 1.5 xalign 2.5 yalign -3.0

                v "{cps=30}A ver, creo que había dejado uno en el escritorio."

                v "{cps=30}..."

                v "{cps=30}¡Aquí está!"

                show valeria_bebe normal :
                    linear 1.5 xpos 200 yalign -0.3

                v "{cps=30}Aunque..."

                v "{cps=30}Está un poco gastado."

                v "{cps=30}Bueno, todavía puede servir."

                $ estres += 1

                show valeria_bebe tarde:
                    xpos 200
                    yalign -0.3

                v "{cps=30}¡Ay, no! ¡Ya perdí demasiado tiempo!"

                v "{cps=30}¡Tenemos que salir ahora!"

                show valeria_bebe tarde at flip, move(200, -0.3, 1.5, -860)

                scene bg fondo_universidad with fade

                show valeria_bebe normal at move(-400, -0.3, 2.0, 700) with dissolve

                v "{cps=30}Menos mal no llegue tan tarde"

                v "{cps=30}Aun asi debo darme prisa. Andando."

            "Conseguir un lápiz en la universidad.":

                v "{cps=30}No tengo tiempo para buscar otro."

                show valeria_bebe triste:
                    xpos 200
                    yalign -0.3

                v "{cps=30}Supongo que tendré que pedir uno prestado."

                v "{cps=30}Espero encontrar a alguien antes de que comience el examen..."

                show valeria_bebe normal at move(200, -0.3, 1.5, -860)

                #
                # AL LLEGAR A LA UNIVERSIDAD
                #

                scene bg fondo_universidad with dissolve

                show valeria_bebe normal at move(0, -0.3, 1.5, 900) with dissolve

                v "{cps=30}Bien... todavía tengo unos minutos."

                show valeria_bebe tarde:
                    xpos 900
                    yalign -0.3

                show herneztino normal at move(-400, -0.3, 1.0, 200) with dissolve

                v "{cps=30}¿A quién podría pedirle un lápiz?"

                show valeria_bebe tarde at flip:
                    xpos 900
                    yalign -0.3

                v "{cps=30}Ah, ¡Herneztino!"

                show valeria_bebe normal at flip, move(900, -0.3, 1.5, 700) with dissolve

                v "{cps=30}¡Herneztino! ¡Espera!"

                c "{cps=30}¿Eh? ¡Hola, Valeria!"

                c "{cps=30}¿Qué sucede? Pareces un poco apresurada."

                show valeria_bebe triste at flip:
                    xpos 700
                    yalign -0.3

                v "{cps=30}Es que... olvidé mi lápiz en casa."

                v "{cps=30}¿No tendrás uno que puedas prestarme?"

                if estudioConHerneztinoC4 == True:

                    c "{cps=30}¿Un lápiz?"

                    show herneztino amable:
                        xpos 200
                        yalign -0.3

                    c "{cps=30}Jaja, después de todo lo que estudiamos, ¿olvidaste traer uno?"

                    show valeria_bebe tarde at flip:
                        xpos 700
                        yalign -0.3

                    v "{cps=30}¡No te burles!"

                    c "{cps=30}Jajaja, perdón, perdón."

                    show herneztino normal:
                        xpos 200
                        yalign -0.3

                    c "{cps=30}Creo que tengo uno de repuesto."

                    v "{cps=30}¿En serio?"

                    show herneztino normal at move(200, -0.3, 1.0, 500) with dissolve

                    c "{cps=30}Sí, aquí tienes."

                    show valeria_bebe feliz at flip:
                        xpos 700
                        yalign -0.3

                    v "{cps=30}¡Muchas gracias!"

                    c "{cps=30}No hay problema."

                    show herneztino amable:
                        xpos 500
                        yalign -0.3

                    c "{cps=30}Después de estudiar tanto, sería una pena que no pudieras presentar el examen por un lápiz."

                    show valeria_bebe normal at flip:
                        xpos 700
                        yalign -0.3


                    v "{cps=30}Jeje, tienes razón."

                else:

                    c "{cps=30}Mmm... déjame revisar."

                    show valeria_bebe tarde at flip:
                        xpos 700
                        yalign -0.3

                    v "{cps=30}Por favor..."

                    show herneztino amable:
                        xpos 200
                        yalign -0.3

                    c "{cps=30}Ah, ¡aquí tengo uno!"

                    show herneztino normal at move(200, -0.3, 1.0, 500) with dissolve

                    c "{cps=30}Puedes quedártelo durante el examen."

                    show valeria_bebe feliz at flip:
                        xpos 700
                        yalign -0.3

                    v "{cps=30}¿De verdad? ¡Muchas gracias!"

                    show herneztino amable:
                        xpos 500
                        yalign -0.3

                    c "{cps=30}Jaja, no hay de qué."

                    c "{cps=30}Solo asegúrate de devolverlo después."

                    show valeria_bebe normal at flip:
                        xpos 700
                        yalign -0.3

                    v "{cps=30}¡Claro que sí!"

                $ estres -= 1

                pv "{cps=30}Menos mal que logré conseguir uno..."

                pv "{cps=30}Ahora solo necesito concentrarme en el examen."

                c "{cps=30}Bueno ya tengo que irme, mucha suerte."

                show herneztino normal at move(500, -0.3, 2.0, 1600) with dissolve

                v "{cps=30}Ah, si igualmente y gracias de nuevo."

                v "{cps=30}Bien, ya solo queda el examen."

    elif objAmbos == True:
    
        $ estres += 1
    
        v "{cps=30}Bien... parece que tengo todas nuestras cosas."
    
        v "{cps=30}Por lo menos hoy no olvidé nada."
    
        v "{cps=30}Aunque..."

        show valeria_bebe preocupada:
            xpos 200
            yalign -0.3
    
        v "{cps=30}¡Ya es tardísimo!"
    
        v "{cps=30}Ay no, no, no..."

        show valeria_bebe tarde:
            xpos 200
            yalign -0.3
    
        v "{cps=30}¡Tenemos que irnos ahora!"

        show valeria_bebe tarde at flip, move(200, -0.3, 1.5, -860)

        scene bg fondo_universidad with fade

        show valeria_bebe normal at move(-400, -0.3, 2.0, 700) with dissolve

        v "{cps=30}Menos mal no llegue tan tarde"

        v "{cps=30}Aun asi debo darme prisa. Andando."

    #
    # ESCENA 2 - ANTES DE ENTRAR
    #

    show valeria_bebe normal at move(700, -0.3, 2.0, 900)

    a "{cps=30}¡Valeria!"

    show veronica normal at flip, move(-400, -0.3, 1.5, 300) with dissolve

    show valeria_bebe normal at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}!!"

    a "{cps=30}Que bueno verte."

    a "{cps=30}Escuche que saliste algo tarde y me preocupé."

    show valeria_bebe tarde at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Ah si, perdona. Es que me quede dormida."

    show veronica molesta at flip:
        xpos 300
        yalign -0.3

    a "{cps=30}Pues claro, que mas podia ser ¿no?"

    show valeria_bebe normal at flip:
        xpos 900
        yalign -0.3

    v "{cps=30}Si jaja."

    show veronica normal at flip:
        xpos 300
        yalign -0.3

    a "{cps=30}Oye, Valeria."
    
    v "{cps=30}¿Mmm?"

    show veronica preocupada at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}¿Estás nerviosa?"

    show valeria_bebe triste at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}¿Tanto se me nota?"
    
    a "{cps=30}Bastante."
    
    a "{cps=30}¿Preparada?"

    show veronica triste at flip:
        xpos 300
        yalign -0.3
    
    v "{cps=30}Creo que sí..."

    show valeria_bebe tarde at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}Aunque siento que se me va a olvidar todo en cuanto vea las preguntas."

    show veronica normal at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}Jaja, eso nos pasa a todos."
    
    v "{cps=30}No es gracioso..."
    
    a "{cps=30}Bueno, bueno."

    show veronica triste at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}Escucha, no tiene caso que te pases estos últimos minutos imaginando todo lo que podría salir mal."

    show valeria_bebe triste at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}Lo sé..."

    show veronica normal at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}Además, puedo quedarme con el bebé mientras presentas el examen."

    show valeria_bebe tarde at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}¿Estás segura? ¿No tenías cosas que hacer?"
    
    a "{cps=30}Ya las organicé. Puedo cuidarlo durante ese rato."
    
    v "{cps=30}Verónica..."
    
    a "{cps=30}¿Qué?"

    show valeria_bebe normal at flip:
        xpos 900
        yalign -0.3
    
    v "{cps=30}Gracias."

    show veronica avergonzada at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}Jaja, anda, todavía no has presentado el examen."

    show veronica normal at flip:
        xpos 300
        yalign -0.3
    
    a "{cps=30}Ya tendrás tiempo de agradecerme cuando termines."

    #
    # ELECCION 4 - COMO MANEJAR LA PREOCUPACION
    #

    menu:
    
        "Aceptar el apoyo y concentrarse en el examen.":
    
            $ apoyoVeronicaExamen = True
            $ cuidado_bebe += 1
            $ estres -= 1
        
            v "{cps=30}Está bien... ¿podrías cuidarlo durante el examen?"
        
            a "{cps=30}Claro."
        
            v "{cps=30}No sé qué haría sin ti."

            show veronica molesta at flip:
                xpos 300
                yalign -0.3
        
            a "{cps=30}Probablemente llegar tarde a todos lados."

            show valeria_bebe feliz at flip:
                xpos 900
                yalign -0.3
        
            v "{cps=30}¡Verónica!"

            show veronica normal at flip:
                xpos 300
                yalign -0.3
        
            a "{cps=30}Jajaja, es broma."
        
            a "{cps=30}Ahora entra, que vas a terminar llegando tarde de verdad."

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3
        
            v "{cps=30}Jaja, está bien. Nos vemos al terminar."

        "Expresar sus preocupaciones antes de entrar.":
        
            $ apoyoVeronicaExamen = True
            $ cuidado_bebe += 1
            $ estres -= 2

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Verónica... ¿puedo decirte algo?"
            
            a "{cps=30}Claro."

            show valeria_bebe triste at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}Tengo miedo."
            
            a "{cps=30}Lo sé."
            
            v "{cps=30}No es solamente el examen..."

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}Siento que si fracaso esta vez, habré desperdiciado todo lo que he hecho."
            
            show veronica preocupada at flip:
                xpos 300
                yalign -0.3

            a "{cps=30}Valeria..."

            show valeria_bebe triste at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}No quiero volver a empezar..."

            show veronica molesta at flip:
                xpos 300
                yalign -0.3
            
            a "{cps=30}Escúchame."
            
            a "{cps=30}Sé cuánto significa esto para ti."

            show veronica molesta2 at flip:
                xpos 300
                yalign -0.3
            
            a "{cps=30}Pero un examen no va a decidir cuánto vales."
            
            v "{cps=30}..."

            show veronica molesta at flip:
                xpos 300
                yalign -0.3
            
            a "{cps=30}Y aunque no salga como esperas, tendrás que pensar qué hacer después."
            
            show veronica normal at flip:
                xpos 300
                yalign -0.3

            a "{cps=30}No significa que todo termine aquí."

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}Gracias..."
            
            a "{cps=30}Ahora ve y haz lo que puedas."

            show valeria_bebe normal at flip:
                xpos 900
                yalign -0.3
            
            v "{cps=30}Sí..."
            
            v "{cps=30}Lo intentaré."

        "Negar ayuda y concentrarse únicamente en aprobar.":
            
            $ estres += 1

            show valeria_bebe triste at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}No... no tengo tiempo para pensar en esas cosas."

            v "{cps=30}Tengo que aprobar."

            show veronica molesta at flip:
                xpos 300
                yalign -0.3

            a "{cps=30}Valeria..."

            show valeria_bebe tarde at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Si no lo hago, todo habrá sido para nada..."

            show veronica molesta2 at flip:
                xpos 300
                yalign -0.3

            a "{cps=30}No digas eso."

            show valeria_bebe triste at flip:
                xpos 900
                yalign -0.3

            v "{cps=30}Perdón..."

            v "{cps=30}Es solo que... necesito conseguirlo."

            show veronica molesta at flip:
                xpos 300
                yalign -0.3

            a "{cps=30}Lo sé. Pero recuerda respirar y leer bien las preguntas."

            v "{cps=30}Sí..."

            v "{cps=30}Lo haré."

    #
    # ESCENA 3 - EL EXAMEN FINAL
    #

    scene bg salon_clase with fade

    show herneztino normal with dissolve:
        xpos 900
        yalign -0.3

    if apoyoVeronicaExamen == True:

        show valeria normal at move(-400, -0.3, 1.5, 200) with dissolve
    
    else:

        show valeria_bebe normal at move(-400, -0.3, 1.5, 200) with dissolve

    c "{cps=30}¡Valeria! Hola."

    v "{cps=30}Hola..."

    show herneztino amable:
        xpos 900
        yalign -0.3

    c "{cps=30}¿Lista para sufrir?"

    if apoyoVeronicaExamen == True:

        show valeria sonrie:
            xpos 200
            yalign -0.3
    
    else:

        show valeria_bebe sonrie:
            xpos 200
            yalign -0.3

    v "{cps=30}Jaja... no me hagas reír."

    show herneztino normal:
        xpos 900
        yalign -0.3

    c "{cps=30}Bueno, dicen que la risa ayuda a aliviar los nervios."

    v "{cps=30}Pues creo que voy a necesitar reírme bastante."

    show herneztino amable:
        xpos 900
        yalign -0.3

    c "{cps=30}Jaja, suerte."

    if apoyoVeronicaExamen == True:

        show valeria normal:
            xpos 200
            yalign -0.3
    
    else:

        show valeria_bebe normal:
            xpos 200
            yalign -0.3

    v "{cps=30}Igualmente."

    show herneztino normal zorder 2:
        linear 2.5 xalign 1.5 yalign -3.0

    if apoyoVeronicaExamen == True:

        show valeria normal zorder 2:
            linear 2.5 xalign 1.0 yalign -3.0
    
    else:

        show valeria_bebe normal zorder 2:
            linear 2.5 xalign 1.0 yalign -3.0

    pause 0.6

    show maestro normal zorder 1 at move(1400, -0.3, 1.5, 1000) with dissolve 

    ms "{cps=30}Buenos días a todos."

    ms "{cps=30}Como saben, hoy realizaremos nuestra evaluación final."

    show maestro explicando:
        xpos 1000
        yalign -0.3

    ms "{cps=30}Tendrán el tiempo indicado para responder todas las preguntas."

    ms "{cps=30}Lean cuidadosamente cada una antes de contestar."

    show maestro normal:
        xpos 1000
        yalign -0.3

    ms "{cps=30}Y recuerden que esta evaluación representa su última oportunidad de recuperación para quienes ya agotaron las anteriores."

    pv "{cps=30}Mi última oportunidad..."

    ms "{cps=30}Bien. Pueden comenzar."

    #
    # PREPARACION SEGUN ESTUDIOS
    #

    if estudios >= 3:

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria feliz with fade
        
        else:

            scene bg examen_valeriab feliz with fade

        pv "{cps=30}Bien... conozco este tema."

        pv "{cps=30}Lo repasé hace poco."

        pv "{cps=30}Si me concentro, creo que puedo resolverlo."

    else:

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria preocupada
        
        else:

            scene bg examen_valeriab preocupada

        pv "{cps=30}No..."

        pv "{cps=30}No recuerdo bien este procedimiento..."

        pv "{cps=30}Sé que lo vimos en clase, pero..."

        pv "{cps=30}¿Cómo era...?"

    #
    # CONCENTRACION SEGUN ESTRES
    #

    if estres >= 3:

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria estres
        
        else:

            scene bg examen_valeriab estres

        pv "{cps=30}No puedo concentrarme..."

        pv "{cps=30}¿Por qué siento que no recuerdo nada?"

        pv "{cps=30}Vamos, Valeria..."

        pv "{cps=30}Piensa... por favor..."

        pv "{cps=30}No puedo fallar..."

    #
    # ORGANIZACION DEL CUIDADO DEL BEBE
    #

    if apoyoVeronicaExamen == True:

        if cuidado_bebe >= 2:

            scene bg examen_valeria concentrada

            pv "{cps=30}El bebé está con Verónica..."

            pv "{cps=30}Dejé preparadas todas sus cosas antes de salir."

            pv "{cps=30}Seguramente estará bien mientras termino el examen."

            pv "{cps=30}Ahora solo tengo que concentrarme."

        else:

            scene bg examen_valeria preocupada_bebe

            pv "{cps=30}Espero que Verónica no esté teniendo problemas con el bebé..."

            pv "{cps=30}Con tantas prisas, no estoy segura de haber preparado todo lo que necesitaba."

            pv "{cps=30}¿Y si se me olvidó algo importante...?"

            scene bg examen_valeria concentrada

            pv "{cps=30}No, no puedo distraerme pensando en eso."

            pv "{cps=30}Verónica sabe cuidarlo. Tengo que confiar en ella."

    else:

        if cuidado_bebe >= 2:

            scene bg examen_valeriab feliz_bebe

            pv "{cps=30}Parece que por fin te quedaste tranquilo, bebé..."

            pv "{cps=30}Menos mal que preparé todas tus cosas antes de salir."

            pv "{cps=30}Por favor, quédate así un poquito más..."

            b "{cps=30}Mmm..."

            pv "{cps=30}Jeje, eso es..."

            scene bg examen_valeriab feliz

            pv "{cps=30}Ahora mamá tiene que concentrarse en su examen."

            pv "{cps=30}Solo necesito aprovechar estos momentos de tranquilidad."

        else:

            b "{cps=30}Snif... snif..."

            scene bg examen_valeriab bebe_llorando

            pv "{cps=30}Ay, no... por favor, bebé..."

            pv "{cps=30}Sé que estás incómodo, pero mamá necesita terminar esto."

            b "{cps=30}¡Waaa!"

            pv "{cps=30}Shhh... tranquilo, tranquilo..."

            pv "{cps=30}No puedo concentrarme si sigue llorando..."

            scene bg examen_valeriab estres

            pv "{cps=30}Y todavía me faltan varias preguntas..."

            pv "{cps=30}¿Qué debería hacer...?"

            $ estres += 1

    #
    # MINIJUEGO DEL EXAMEN 
    #

    call jugar_minijuego_examen

    if aproboMateria == True:

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria feliz
        
        else:

            scene bg examen_valeriab feliz

        v "{cps=30}Listo..."

        v "{cps=30}Creo que respondí la mayoría."

        v "{cps=30}Aunque algunas preguntas me hicieron dudar bastante..."

        v "{cps=30}Por favor... que estén bien."

    else:

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria estres
        
        else:

            scene bg examen_valeriab estres

        v "{cps=30}No puede ser..."

        v "{cps=30}No alcancé a responder todo..."

        v "{cps=30}Y hubo varias preguntas que no supe cómo resolver..."

        if apoyoVeronicaExamen == True:

            scene bg examen_valeria preocupada
        
        else:

            scene bg examen_valeriab preocupada

        pv "{cps=30}Tal vez todavía consiga algunos puntos..."

        pv "{cps=30}Por favor..."

    #
    # ESCENA 4 - ESPERANDO LOS RESULTADOS
    #

    scene bg salon_clase with fade

    if apoyoVeronicaExamen == True:

        show valeria normal at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3

    show herneztino normal at move(-400, -0.3, 1.5, 0)

    c "{cps=30}¡Valeria!"

    v "{cps=30}Ah... Herneztino."

    c "{cps=30}¿Cómo te fue?"

    if apoyoVeronicaExamen == True:

        show valeria preocupada at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe tarde at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}No estoy muy segura..."

    show herneztino amable:
        xpos 0
        yalign -0.3

    c "{cps=30}Jaja, yo tampoco."

    show herneztino normal:
        xpos 0
        yalign -0.3

    c "{cps=30}Hubo unas preguntas bastante complicadas."

    if apoyoVeronicaExamen == True:

        show valeria normal at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}Sí... especialmente las del final."

    show herneztino amable:
        xpos 0
        yalign -0.3

    c "{cps=30}¡Exacto! Pensé que era el único."

    v "{cps=30}Jaja..."

    show herneztino normal:
        xpos 0
        yalign -0.3

    c "{cps=30}Bueno, supongo que solo nos queda esperar."

    if apoyoVeronicaExamen == True:

        show valeria preocupada at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe tarde at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}Sí..."

    c "{cps=30}Oye, independientemente de cómo salga todo..."

    show herneztino amable:
        xpos 0
        yalign -0.3

    c "{cps=30}Me alegró mucho haber podido conocerte este periodo."

    v "{cps=30}¿Eh?"

    c "{cps=30}Jaja, ¿por qué esa cara?"

    if apoyoVeronicaExamen == True:

        show valeria normal at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}No, es solo que... no esperaba que dijeras eso."

    show herneztino normal:
        xpos 0
        yalign -0.3

    c "{cps=30}Bueno, es la verdad."

    if apoyoVeronicaExamen == True:

        show valeria feliz2 at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe feliz at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}Je... gracias, Herneztino."

    if apoyoVeronicaExamen == True:

        show valeria normal at flip:
            xpos 1000
            yalign -0.3
    
    else:

        show valeria_bebe normal at flip:
            xpos 1000
            yalign -0.3

    v "{cps=30}Yo también me alegro de haberte conocido."

    scene bg salon_clase with fade

    "{cps=30}Unos días después, el maestro anuncia la publicación de los resultados."

    show maestro normal:
        xpos 900
        yalign -0.3
    with dissolve

    ms "{cps=30}Buenos días."

    ms "{cps=30}Ya se encuentran disponibles las calificaciones finales."

    show maestro explicando:
        xpos 900
        yalign -0.3

    ms "{cps=30}Les recuerdo que la calificación definitiva considera tanto las actividades entregadas como el examen."

    ms "{cps=30}Si alguien tiene dudas sobre cómo se calculó su resultado, puede acercarse para revisarlo."

    show maestro normal:
        xpos 900
        yalign -0.3

    pv "{cps=30}Ya están..."

    scene bg salon with fade

    show valeria_bebe normal at flip:
        xpos 500
        yalign -0.3

    pv "{cps=30}Después de todo este tiempo..."

    pv "{cps=30}Por fin voy a saber si lo conseguí..."

    v "{cps=30}Muy bien..."

    v "{cps=30}Voy a revisar..."

    show valeria_bebe normal at flip, move(500, -0.3, 2.0, -860)

    #
    # SELECCION DE FINAL
    # Asegurate de actualizar aproboMateria al terminar el minijuego.
    # Los umbrales de estres y cuidado_bebe son provisionales.
    #

    if aproboMateria == False:
        jump final_necesito_tiempo
    elif estres <= 2 and cuidado_bebe >= 2 and (apoyoVeronicaC4 or apoyoVeronicaExamen):
        jump final_no_estoy_sola
    else:
        jump final_seguir_adelante

#
# FINAL 1 - SEGUIR ADELANTE
#

label final_seguir_adelante:

    scene bg fondo_universidad calificaciones with fade

    show valeria_bebe tarde at flip, move(500, -0.3, 2.0, 100) with dissolve

    v "{cps=30}A ver.. Mi calificación es..."

    v "{cps=30}..."

    show valeria_bebe exito:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Aprobé!"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}No puedo creerlo..."

    v "{cps=30}Después de todo lo que pasó..."

    v "{cps=30}¡Lo conseguí!"

    pv "{cps=30}Todas esas noches en las que me quedé estudiando..."

    pv "{cps=30}Todas las veces que pensé que ya no podría continuar..."

    pv "{cps=30}Al final pude conseguirlo..."

    show veronica normal at move(1600, -0.3, 2.0, 900)

    a "{cps=30}¿Y bien? ¿Qué pasó?"

    show valeria_bebe tarde:
        xpos 100
        yalign -0.3

    v "{cps=30}Verónica..."

    show veronica preocupada:
        xpos 900
        yalign -0.3

    a "{cps=30}¿Qué? No me asustes."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Aprobé..."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}¿En serio?"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Sí! ¡Aprobé!"

    a "{cps=30}¡Jajaja! ¡Felicidades!"

    v "{cps=30}¡Gracias!"

    a "{cps=30}¿Ves? Tanto que te preocupabas."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje, sí..."

    show veronica molesta:
        xpos 900
        yalign -0.3

    a "{cps=30}Oye, ¿estás bien?"

    v "{cps=30}Sí, es solo que..."

    v "{cps=30}Ahora que todo terminó, siento que no tengo fuerzas para nada."

    show veronica triste:
        xpos 900
        yalign -0.3

    a "{cps=30}No me sorprende."

    a "{cps=30}Llevas semanas sin descansar como deberías."

    show valeria_bebe triste:
        xpos 100
        yalign -0.3

    v "{cps=30}Sí..."

    v "{cps=30}Creo que tienes razón."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}Bueno, ahora puedes tomarte un descanso, ¿no?"

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Sí..."

    v "{cps=30}Aunque todavía tengo muchas cosas pendientes."

    show veronica molesta2:
        xpos 900
        yalign -0.3

    a "{cps=30}¡Valeria!"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Jaja, está bien!"

    v "{cps=30}Descansaré."

    pv "{cps=30}Lo había conseguido..."

    pv "{cps=30}A pesar de todas las dificultades, todavía podía seguir estudiando."

    pv "{cps=30}¿Cuántas veces había terminado completamente agotada?"

    pv "{cps=30}¿Cuántas cosas había dejado de lado?"

    pv "{cps=30}No podía seguir haciendo lo mismo indefinidamente."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Verónica..."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}¿Sí?"

    v "{cps=30}Creo que... necesitaré cambiar algunas cosas."

    show veronica preocupada:
        xpos 900
        yalign -0.3

    a "{cps=30}¿Cómo cuáles?"

    v "{cps=30}No lo sé todavía."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Pero no quiero seguir viviendo con miedo de no poder hacerlo todo."

    show veronica normal:
        xpos 900
        yalign -0.3

    a "{cps=30}Bueno, eso ya es un comienzo."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje... supongo que sí."

    pv "{cps=30}Todavía me quedaba un largo camino por recorrer."

    pv "{cps=30}Seguramente habría más días difíciles."

    pv "{cps=30}Pero había logrado superar uno de mis mayores obstáculos."

    pv "{cps=30}Y esta vez quería aprender a seguir adelante sin dejarme a mí misma atrás."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Vamos, bebé."

    v "{cps=30}Todavía tenemos muchos sueños por cumplir."

    scene black with fade

    call screen pantalla_final("Seguir Adelante")
    
    return

#
# FINAL 2 - NECESITO TIEMPO
#
  
label final_necesito_tiempo:

    scene bg fondo_universidad calificaciones with fade

    show valeria_bebe tarde at flip, move(500, -0.3, 2.0, 100) with dissolve

    v "{cps=30}Bien..."

    v "{cps=30}Mi calificación es..."

    v "{cps=30}..."

    show valeria_bebe triste at flip:
        xpos 100
        yalign -0.3

    v "{cps=30}¿Qué...?"

    v "{cps=30}No puede ser..."

    pv "{cps=30}Reprobé.. Otra vez..."
    
    show valeria_bebe tarde:
        xpos 100
        yalign -0.3

    v "{cps=30}Pero... yo..."

    v "{cps=30}Estudié tanto..."

    show valeria_bebe triste:
        xpos 100
        yalign -0.3

    v "{cps=30}¿Por qué...?"

    show valeria_bebe tarde:
        xpos 100
        yalign -0.3

    v "{cps=30}No.. tengo que buscar al maestro."

    scene bg salon_clase with fade

    show maestro normal at flip:
        xpos 1000
        yalign -0.2

    show valeria_bebe tarde at move(-200, -0.3, 1.5, 200) with dissolve

    v "{cps=30}Maestro..."

    show maestro normal:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Valeria, buenos días."

    ms "{cps=30}¿Sucede algo?"

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Quería preguntarle sobre mi calificación..."

    ms "{cps=30}Claro, ¿qué necesitas saber?"

    v "{cps=30}Es que... no alcancé a aprobar."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}¿Está seguro de que no hubo algún error?"

    show maestro explicando:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Podemos revisar tu evaluación si gustas."

    v "{cps=30}Sí... por favor."

    show maestro notas:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Lo siento, Valeria."

    show maestro explicando:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Los puntos están correctamente contabilizados."

    v "{cps=30}Entonces..."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}¿No hay nada que pueda hacer?"

    show maestro normal:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Me temo que ya agotaste tus oportunidades de recuperación."

    ms "{cps=30}No puedo autorizarte otra evaluación de esta materia."

    v "{cps=30}..."

    ms "{cps=30}Sé que esto no era lo que esperabas."

    show maestro explicando:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Pero te recomiendo acercarte al departamento académico para conocer cuáles son tus opciones a partir de ahora."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}Entiendo..."

    v "{cps=30}Gracias, maestro..."

    show maestro normal:
        xpos 1000
        yalign -0.2

    ms "{cps=30}Lamento no poder darte una mejor respuesta."

    show valeria_bebe tarde at flip, move(200, -0.3, 1.5, -860)

    scene bg fondo_universidad with dissolve

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3
    with dissolve

    show veronica normal at move(1600, -0.3, 1.5, 1000)

    a "{cps=30}¡Valeria!"

    a "{cps=30}¿Cómo te fue?"

    v "{cps=30}..."

    show veronica preocupada:
        xpos 1000
        yalign -0.3

    a "{cps=30}¿Valeria?"

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}No aprobé..."

    show veronica triste:
        xpos 1000
        yalign -0.3

    a "{cps=30}Oh..."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}Lo intenté, Verónica."

    v "{cps=30}De verdad que lo intenté..."

    a "{cps=30}Lo sé..."

    v "{cps=30}Pero no fue suficiente..."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Ya no puedo recuperar esa materia."

    v "{cps=30}No sé qué voy a hacer..."

    a "{cps=30}..."

    v "{cps=30}Perdón..."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}¿Por qué te disculpas?"

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}Después de todo lo que has hecho por mí..."

    v "{cps=30}Quería demostrarte que podía conseguirlo..."

    a "{cps=30}Valeria..."

    show veronica molesta2:
        xpos 1000
        yalign -0.3

    a "{cps=30}No tienes que demostrarme nada."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Pero..."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Escúchame."

    a "{cps=30}Sé cuánto te esforzaste."

    show veronica molesta2:
        xpos 1000
        yalign -0.3

    a "{cps=30}Y sé que esto te duele muchísimo."

    show veronica triste:
        xpos 1000
        yalign -0.3

    a "{cps=30}No voy a decirte que no importa, porque sé que para ti sí importa."

    v "{cps=30}..."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Pero tampoco voy a dejar que pienses que todo lo que hiciste no sirvió para nada."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}¿Y qué se supone que haga ahora?"

    show veronica preocupada:
        xpos 1000
        yalign -0.3

    a "{cps=30}No lo sé."

    a "{cps=30}Tendrás que averiguar qué opciones te quedan."

    a "{cps=30}Quizá puedas continuar tus estudios de otra manera, o quizá necesites reorganizar tus planes."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Pero no tienes que resolverlo hoy."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}..."

    v "{cps=30}Tengo tanto miedo..."

    show veronica triste:
        xpos 1000
        yalign -0.3

    a "{cps=30}Lo sé."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    v "{cps=30}¿Y si nunca logro terminar mi carrera?"

    a "{cps=30}No puedo prometerte que todo saldrá exactamente como quieres."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Pero todavía tienes cosas que puedes intentar."

    v "{cps=30}..."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Supongo que tienes razón..."

    pv "{cps=30}Había fracasado en conseguir aquello por lo que tanto había luchado."

    pv "{cps=30}Y por primera vez tuve que aceptar que no siempre bastaba con esforzarse más."

    pv "{cps=30}A veces las cosas simplemente no salían como esperábamos."

    pv "{cps=30}Pero..."

    pv "{cps=30}Todavía tenía a mi bebé."

    pv "{cps=30}Tenía a Verónica."

    pv "{cps=30}Y aunque no sabía qué me esperaba después..."

    pv "{cps=30}Todavía tenía un futuro por delante."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Creo que..."

    v "{cps=30}Necesito algo de tiempo."

    show veronica normal:
        xpos 1000
        yalign -0.3

    a "{cps=30}Entonces tómalo."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Gracias, Verónica..."

    a "{cps=30}No hay nada que agradecer Valeria."

    pv "{cps=30}Mi camino había cambiado una vez más."

    show valeria_bebe tarde:
        xpos 200
        yalign -0.3

    pv "{cps=30}No sabía si algún día podría retomar mis estudios de la manera en que siempre había imaginado."

    pv "{cps=30}Pero ahora entendía que necesitar tiempo para encontrar otro camino no significaba que mi vida se hubiera terminado."

    show valeria_bebe triste:
        xpos 200
        yalign -0.3

    v "{cps=30}Vamos, bebé..."

    v "{cps=30}Tenemos muchas cosas que pensar."

    call screen pantalla_final("Necesito Tiempo")
    
    return

#
# FINAL 3 - NO ESTOY SOLA
#

label final_no_estoy_sola:

    scene bg fondo_universidad calificaciones with fade

    show valeria_bebe tarde at flip, move(500, -0.3, 2.0, 100) with dissolve

    v "{cps=30}Muy bien.."

    v "{cps=30}Vamos a ver.."

    v "{cps=30}..."

    show valeria_bebe exito at flip:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Aprobé!"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Lo conseguí!"

    v "{cps=30}¡De verdad lo conseguí!"

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    pv "{cps=30}No puedo creerlo..."

    pv "{cps=30}Después de todas esas veces que pensé que ya no podría seguir..."

    pv "{cps=30}Finalmente lo conseguí..."

    show veronica normal at move(1600, -0.3, 2.0, 1000) with dissolve

    a "{cps=30}¡Valeria! ¿Qué tal te fue?"

    v "{cps=30}¡Verónica!"

    show veronica preocupada:
        xpos 1000
        yalign -0.3

    a "{cps=30}¿Qué? ¿Por qué estás tan emocionada?"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Aprobé!"

    show veronica preocupada:
        xpos 1000
        yalign -0.3

    a "{cps=30}¡¿En serio?!"

    v "{cps=30}¡Sí!"

    show veronica feliz:
        xpos 1000
        yalign -0.3

    a "{cps=30}¡Jajaja, sabía que podías lograrlo!"

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje... gracias."

    a "{cps=30}Bueno, supongo que tendremos que celebrarlo."

    v "{cps=30}Jaja, ¿celebrarlo?"

    show veronica normal:
        xpos 1000
        yalign -0.3

    a "{cps=30}¡Por supuesto! No todos los días se supera algo así."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Tienes razón..."

    v "{cps=30}Aunque..."

    a "{cps=30}¿Mmm?"

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}No creo que hubiera podido hacerlo sin ustedes."

    show veronica preocupada:
        xpos 1000
        yalign -0.3

    a "{cps=30}¿Ustedes?"

    v "{cps=30}Sí..."

    v "{cps=30}Tú, Herneztino..."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Y todas las personas que me ayudaron cuando lo necesitaba."

    show valeria_bebe tarde:
        xpos 100
        yalign -0.3

    v "{cps=30}Durante mucho tiempo pensé que tenía que hacerlo todo por mi cuenta."

    show valeria_bebe triste:
        xpos 100
        yalign -0.3

    v "{cps=30}Que si necesitaba ayuda era porque no estaba esforzándome lo suficiente."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Valeria..."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Pero estaba equivocada."

    v "{cps=30}No podía estudiar, cuidar a mi bebé y hacer todas mis cosas sin detenerme a descansar."

    v "{cps=30}Y tampoco tenía que hacerlo."

    show veronica normal:
        xpos 1000
        yalign -0.3

    a "{cps=30}Bueno, me alegra que por fin te hayas dado cuenta."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje, sí..."

    show veronica molesta:
        xpos 1000
        yalign -0.3

    a "{cps=30}Aunque te tardaste bastante."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}¡Verónica!"

    show veronica normal:
        xpos 1000
        yalign -0.3

    a "{cps=30}Jajaja."

    a "{cps=30}Bueno, bueno. ¿Y ahora qué?"

    v "{cps=30}¿Ahora?"

    a "{cps=30}Sí. ¿Cuáles son tus siguientes planes?"

    v "{cps=30}Mmm..."

    show valeria_bebe sonrie:
        xpos 100
        yalign -0.3

    v "{cps=30}La verdad... todavía no estoy segura."

    v "{cps=30}Quiero continuar mis estudios."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Pero también quiero tener más tiempo para mi bebé."

    v "{cps=30}Y quizá... también para mí."

    show veronica feliz:
        xpos 1000
        yalign -0.3

    a "{cps=30}Eso suena bastante bien."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje, gracias."

    pv "{cps=30}Por primera vez en mucho tiempo..."

    pv "{cps=30}Sentía que podía mirar hacia el futuro sin tener tanto miedo."

    pv "{cps=30}Todavía habría días difíciles."

    pv "{cps=30}Seguramente volvería a cometer errores."

    pv "{cps=30}Pero ahora sabía algo que antes me costaba aceptar..."

    pv "{cps=30}No tenía que superar todos mis problemas yo sola."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}Bueno, ¿qué te parece si vamos a comer algo?"

    show veronica normal:
        xpos 1000
        yalign -0.3

    a "{cps=30}¡Eso sí que es una buena idea!"

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Jeje, entonces vamos."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    v "{cps=30}¿Qué dices, bebé? ¿Listo para irnos?"

    b "{cps=30}Ah... mm."

    show valeria_bebe feliz:
        xpos 100
        yalign -0.3

    v "{cps=30}Jajaja."

    pv "{cps=30}Cuando comenzó todo esto, pensé que tendría que renunciar a mis sueños."

    pv "{cps=30}Después creí que tendría que sacrificarlo todo para alcanzarlos."

    pv "{cps=30}Pero ahora..."

    show valeria_bebe normal:
        xpos 100
        yalign -0.3

    pv "{cps=30}Ahora sé que puedo construir un futuro para nosotros."

    pv "{cps=30}Un paso a la vez..."

    pv "{cps=30}Y sin olvidar a quienes están a mi lado."

    call screen pantalla_final("No Estoy Sola")
    
    return
