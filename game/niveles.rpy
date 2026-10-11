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
        "01",
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

    pause 1.0

    