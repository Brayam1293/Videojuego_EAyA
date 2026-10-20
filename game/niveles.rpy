# 
# NIVEL 1
# UN NUEVO DÍA
#


label nivel_1:

    # 
    # ESCENA 1 - CASA
    # 

    scene bg fondo_casa

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    "Una nueva mañana comienza."

    v "Hoy tengo clases temprano."

    v "Debo prepararme antes de salir."

    v "Ser mamá y estudiar no siempre es fácil..."

    v "Pero quiero seguir adelante."


    # 
    # DECISIÓN 1
    # 

    menu:

        "¿Qué hago antes de salir?"

        "Preparar mis cosas para la universidad.":

            $ estudios += 1
            $ decisiones_nivel_1 += 1

            v "Primero debo preparar mis apuntes."

            v "Quiero llegar preparada a clase."

        "Revisar que el bebé esté bien.":

            $ cuidado_bebe += 1
            $ decisiones_nivel_1 += 1

            v "Antes de salir quiero asegurarme de que mi bebé esté bien."

            v "Después podré concentrarme en mis clases."


    # 
    # ESCENA 2 - EL BEBÉ LLORA
    # 

    show valeria_bebe llorando:
        xalign 0.5
        yalign -0.3
    with dissolve

    v "¿Qué pasa, pequeño?"

    v "Creo que necesitas algo."


    # 
    # DECISIÓN 2
    # 
    menu:

        "¿Qué hace Valeria?"

        "Calmar al bebé.":

            $ cuidado_bebe += 1
            $ decisiones_nivel_1 += 1

            v "Tranquilo, mamá está aquí."

            show valeria_bebe feliz:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Ya estás más tranquilo."

        "Prepararme rápidamente para salir.":

            $ estudios += 1
            $ decisiones_nivel_1 += 1

            v "Debo organizarme rápido."

            v "También tengo que llegar a tiempo a clases."

            show valeria_bebe normal:
                xalign 0.5
                yalign -0.3
            with dissolve


    # 
    # ESCENA 3 - PREPARÁNDOSE PARA SALIR
    # 

    show valeria_bebe normal:
        xalign 0.5
        yalign -0.3
    with dissolve

    v "Mis apuntes están listos."

    v "La pañalera también."

    v "Ahora sí, podemos irnos."

    show valeria_bebe normal:
        linear 2.0 xalign 2.5 yalign -3.0

    pause 1.2

    # 
    # ESCENA 4 - UNIVERSIDAD
    # 

    scene bg fondo_universidad
    with fade

    show valeria_bebe normal:
        xalign -0.3 yalign -0.3
        linear 1.2 xalign 0.5

    pause 1.2

    v "Ya llegamos."

    v "Ahora debo concentrarme en mis clases."

    v "Quiero terminar mi carrera."

    v "Quiero demostrarme que puedo hacerlo."


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
            $ decisiones_nivel_1 += 1

            show valeria_bebe feliz:
                xalign 0.5
                yalign -0.3
            with dissolve

            v "Quiero pasar un rato contigo."

            v "Estos momentos también son importantes."

        "Descansar un momento.":

            $ decisiones_nivel_1 += 1

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

    p "{cps=50}{size=50}!¿Que?!{/size}"

    "{cps=30}El shock de la noticia hizo que su padre no pensra correctamente.."

    p "{cps=50}{size=40}¿En que estabas Pensando?!!"

    m "{cps=30}Cariño por favor, calmate."

    "{cps=30}Valeria intento explicarse. Pero sin exito."

    v "{cps=30}Porfavor, Papá.. Dejame explicart--"



    "{cps=30}Sin embargo su padre no cambio de opinion."

    "Finalmente, le pidio a Valeria que se marchara de su casa."

    v "¿De verdad quieres que me vaya?{p} Soy tu hija..."

    "Su madre queria adetenerla, pero no logro cambiar la decicion de su esposo."

    v "¿Qué se supone que haré ahora?"

    v "Tengo miedo.{w} Pero debo pensar en mi bebé y en mi futuro"

    # ESCENA 4 - DECICION DE VALERIA

    scene bg fondo_parque with dissolve

    "Lejos de la casa de sus padres, Valeria intentó ordenar sus pensamientos."

    "Tenia muchas dificultades por delante, pero todavia podia decidir como enfrentarlas."

    menu:

        "¿Qué deberia hacer Valeria?"

        "Continuar luchando por sus estudios.":

            $estudios+=1

            v "No voy a abandonar mi carrera."

            v "Quiero demostrar que puedo ser una buen madre y continuar con mis estudios."

            "Valeria decidio seguir trabajando por el futuro que deseaba."

        "Concenntrarse priemero en la seguridad de su bebé.":

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
