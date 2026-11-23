# -*- coding: utf-8 -*-
#
# MINIJUEGO DEL EXAMEN FINAL - ENTRE APUNTES Y AVENTURAS
# Archivo: game/minijuego_examen.rpy
# Diseñado para 1920x1080 (puedes adaptar tamaños y posiciones).
#
# Tres partes: opción múltiple (4), ordenar SQL (3), corregir SQL (3).
# La elección apoyoVeronicaExamen cambia el obstáculo:
#   True  = concentración + pensamientos que bloquean las respuestas.
#   False = calma del bebé + tensión del maestro.
#
# NO vuelvas a declarar estas variables si ya existen en tu historia:
#   apoyoVeronicaExamen, aproboMateria, estudios, estres,
#   cuidado_bebe, resClase.
#
# Ejecución desde el capítulo 5:
#     call jugar_minijuego_examen
#     # Se actualizan automáticamente calificacionExamen y aproboMateria.
#

default resultado_minijuego_examen = None
default calificacionExamen = 0

init python:
    class JuegoExamen(object):

        PASO = 0.1
        TIEMPO_LIMITE = 300.0

        # Mecánica del bebé, conservada del minijuego anterior.
        PERDIDA_CALMA = 3.0
        RECUPERACION_CALMA = 22.0
        SUBIDA_ESTRES_MAESTRO = 7.0

        # La concentración es un obstáculo más ligero.
        PERDIDA_CONCENTRACION = 0.22
        PENALIZACION_ERROR = 10.0
        UMBRAL_PENSAMIENTOS = 30.0
        RECUPERACION_RESPIRAR = 18.0
        TIEMPO_RESPIRAR = 8.0

        def __init__(self, ayuda_veronica, estudios, estres, cuidado_bebe):
            self.con_ayuda = bool(ayuda_veronica)
            self.estudios = estudios
            self.estres_historia = estres
            self.cuidado_bebe = cuidado_bebe

            self.tiempo_restante = self.TIEMPO_LIMITE
            self.indice = 0
            self.puntos = 0
            self.errores = 0
            self.errores_pregunta = 0
            self.resultado = None
            self.aviso = "Responde con cuidado: el tiempo no se detiene."

            self.calma = 100.0
            self.estres_maestro = 0.0
            self.atendiendo_bebe = False

            # 'estres' narrativo no es un porcentaje; se limita su efecto.
            self.concentracion = max(50.0, min(95.0, 92.0 - max(0, estres) * 4.0))
            self.pensamiento = None
            self.pensamiento_restante = 0.0
            self.siguiente_pensamiento = renpy.random.uniform(8.0, 14.0)
            self.pensamientos = [
                "{cps=30}No... no puedo distraerme. Esta es mi última oportunidad...",
                "{cps=30}¿Y si vuelvo a reprobar? No sé qué haría después...",
                "{cps=30}Vamos, Valeria... ¿Cómo era esa respuesta? Lo sabía hace un momento...",
                "{cps=30}Siento que el tiempo está pasando demasiado rápido...",
                "{cps=30}No puedo dejar de pensar en todo lo que podría salir mal..."
            ]

            # Prepararse en capítulos anteriores permite usar pistas.
            self.pistas = 2 if estudios >= 6 else (1 if estudios >= 3 else 0)
            self.pista_visible = False

            # Estado de los ejercicios de ordenar y corregir.
            self.orden_elegido = []
            self.token_elegido = None

            self.preguntas = [
                {
                    "tipo": "opcion", "titulo": "Consultas SQL",
                    "enunciado": "¿Qué comando obtiene información de una tabla?",
                    "opciones": ["INSERT", "SELECT", "DELETE", "UPDATE"],
                    "correcta": 1,
                    "pista": "Se usa para leer registros, sin modificar la tabla."
                },
                {
                    "tipo": "opcion", "titulo": "Filtros",
                    "enunciado": "¿Qué cláusula filtra los registros según una condición?",
                    "opciones": ["ORDER BY", "FROM", "WHERE", "VALUES"],
                    "correcta": 2,
                    "pista": "Suele aparecer después de FROM."
                },
                {
                    "tipo": "opcion", "titulo": "Claves",
                    "enunciado": "¿Qué clave identifica de manera única cada registro de una tabla?",
                    "opciones": ["PRIMARY KEY", "FOREIGN KEY", "DEFAULT", "INDEX"],
                    "correcta": 0,
                    "pista": "Es la clave principal de la tabla."
                },
                {
                    "tipo": "opcion", "titulo": "Relaciones",
                    "enunciado": "¿Qué operación combina filas de dos tablas que coinciden en una condición?",
                    "opciones": ["TRUNCATE", "GROUP BY", "DROP", "INNER JOIN"],
                    "correcta": 3,
                    "pista": "Su nombre contiene la palabra JOIN."
                },
                {
                    "tipo": "ordenar", "titulo": "Construye una consulta SELECT",
                    "enunciado": "Mostrar los nombres de estudiantes mayores de 18 años.",
                    "partes": [
                        {"id": 2, "texto": "WHERE edad > 18;"},
                        {"id": 0, "texto": "SELECT nombre"},
                        {"id": 1, "texto": "FROM estudiantes"}
                    ],
                    "respuesta": [0, 1, 2],
                    "pista": "Una consulta de lectura empieza por SELECT."
                },
                {
                    "tipo": "ordenar", "titulo": "Construye una inserción",
                    "enunciado": "Agregar una alumna llamada Ana a la tabla alumnos.",
                    "partes": [
                        {"id": 1, "texto": "(nombre)"},
                        {"id": 2, "texto": "VALUES ('Ana');"},
                        {"id": 0, "texto": "INSERT INTO alumnos"}
                    ],
                    "respuesta": [0, 1, 2],
                    "pista": "Para agregar un registro se comienza con INSERT INTO."
                },
                {
                    "tipo": "ordenar", "titulo": "Construye una actualización",
                    "enunciado": "Cambiar a 21 la edad del estudiante con id 3.",
                    "partes": [
                        {"id": 2, "texto": "WHERE id = 3;"},
                        {"id": 1, "texto": "SET edad = 21"},
                        {"id": 0, "texto": "UPDATE estudiantes"}
                    ],
                    "respuesta": [0, 1, 2],
                    "pista": "Se inicia con UPDATE."
                },
                {
                    "tipo": "corregir", "titulo": "Detecta un error",
                    "enunciado": "Señala el fragmento incorrecto y escoge cómo corregirlo.",
                    "tokens": ["SELEC", "nombre", "FROM", "alumnos;"],
                    "indice_error": 0,
                    "correcciones": ["DELETE", "SELECT", "SET"],
                    "correccion": 1,
                    "pista": "Revisa cómo está escrita la primera instrucción."
                },
                {
                    "tipo": "corregir", "titulo": "Detecta un error",
                    "enunciado": "Señala el fragmento incorrecto y escoge cómo corregirlo.",
                    "tokens": ["DELETE", "FROM", "alumnos", "WHER", "id = 5;"],
                    "indice_error": 3,
                    "correcciones": ["WHERE", "ORDER", "VALUES"],
                    "correccion": 0,
                    "pista": "El filtro debe escribirse WHERE."
                },
                {
                    "tipo": "corregir", "titulo": "Detecta un error",
                    "enunciado": "Señala el fragmento incorrecto y escoge cómo corregirlo.",
                    "tokens": ["INSERT INTO", "alumnos", "(nombre)", "VALUE", "('Ana');"],
                    "indice_error": 3,
                    "correcciones": ["WHERE", "VALUES", "SELECT"],
                    "correccion": 1,
                    "pista": "Después de indicar las columnas, se usa VALUES."
                }
            ]

        @property
        def pregunta(self):
            return self.preguntas[min(self.indice, len(self.preguntas) - 1)]

        @property
        def tiempo_formato(self):
            seg = int(self.tiempo_restante + 0.999)
            return "%02d:%02d" % (seg // 60, seg % 60)

        @property
        def seccion(self):
            if self.indice < 4:
                return "OPCIÓN MÚLTIPLE"
            if self.indice < 7:
                return "ORDENAR CONSULTAS SQL"
            return "CORREGIR CONSULTAS SQL"

        @property
        def bloqueado(self):
            return self.resultado is not None or self.pensamiento is not None or self.atendiendo_bebe

        @property
        def pensamiento_visible(self):
            # Revelar el pensamiento a 30 caracteres por segundo mediante
            # el reloj del minijuego evita que se reinicie al redibujar la UI.
            if self.pensamiento is None:
                return ""
            completo = self.pensamiento.replace("{cps=30}", "")
            pendientes = max(0.0, self.pensamiento_restante - 0.9)
            cantidad = max(0, min(len(completo), int(len(completo) - pendientes * 30.0)))
            return completo[:cantidad]

        @property
        def orden_mostrado(self):
            textos = []
            for fragmento_id in self.orden_elegido:
                for parte in self.pregunta["partes"]:
                    if parte["id"] == fragmento_id:
                        textos.append(parte["texto"])
                        break
            return "  ".join(textos) if textos else "(Selecciona los fragmentos en el orden correcto)"

        def _equivocacion(self, aviso):
            self.errores += 1
            self.errores_pregunta += 1
            self.aviso = aviso
            if self.con_ayuda:
                self.concentracion = max(0.0, self.concentracion - self.PENALIZACION_ERROR)
            renpy.restart_interaction()

        def _avanzar(self, correcto):
            if correcto:
                # Reintentar no borra el progreso, pero puede reducir puntos.
                ganancia = max(4, 10 - 2 * self.errores_pregunta)
                self.puntos += ganancia
                self.aviso = "¡Correcto! Sumaste %d puntos." % ganancia
                if self.con_ayuda:
                    self.concentracion = min(100.0, self.concentracion + 2.0)
            else:
                self.aviso = "Respuesta incorrecta. Continúa con la siguiente."
            self.indice += 1
            self.errores_pregunta = 0
            self.orden_elegido = []
            self.token_elegido = None
            self.pista_visible = False
            if self.indice >= len(self.preguntas):
                self.resultado = "completado"
            renpy.restart_interaction()

        def responder_opcion(self, indice_opcion):
            if self.bloqueado or self.pregunta["tipo"] != "opcion":
                return
            correcto = indice_opcion == self.pregunta["correcta"]
            if not correcto:
                self._equivocacion("Respuesta incorrecta.")
            self._avanzar(correcto)

        def seleccionar_fragmento(self, fragmento_id):
            if self.bloqueado or self.pregunta["tipo"] != "ordenar":
                return
            if fragmento_id not in self.orden_elegido:
                self.orden_elegido.append(fragmento_id)
            renpy.restart_interaction()

        def deshacer_fragmento(self):
            if self.bloqueado or self.pregunta["tipo"] != "ordenar":
                return
            if self.orden_elegido:
                self.orden_elegido.pop()
            renpy.restart_interaction()

        def comprobar_orden(self):
            if self.bloqueado or self.pregunta["tipo"] != "ordenar":
                return
            if len(self.orden_elegido) != len(self.pregunta["respuesta"]):
                self.aviso = "Primero debes seleccionar todos los fragmentos."
                renpy.restart_interaction()
                return
            if self.orden_elegido == self.pregunta["respuesta"]:
                self._avanzar(True)
            else:
                self._equivocacion("El orden es incorrecto. Pulsa DESHACER y corrígelo.")

        def elegir_token(self, indice_token):
            if self.bloqueado or self.pregunta["tipo"] != "corregir":
                return
            if indice_token == self.pregunta["indice_error"]:
                self.token_elegido = indice_token
                self.aviso = "¡Encontraste el error! Ahora elige su corrección."
                renpy.restart_interaction()
            else:
                self._equivocacion("Ese fragmento no contiene el error. Inténtalo de nuevo.")

        def corregir_token(self, indice_correccion):
            if self.bloqueado or self.pregunta["tipo"] != "corregir":
                return
            if self.token_elegido is None:
                return
            if indice_correccion == self.pregunta["correccion"]:
                self._avanzar(True)
            else:
                self._equivocacion("Esa corrección no es correcta. Prueba otra.")

        def mostrar_pista(self):
            if self.bloqueado or self.pistas <= 0 or self.pista_visible:
                return
            self.pistas -= 1
            self.pista_visible = True
            renpy.restart_interaction()

        def alternar_bebe(self):
            if self.con_ayuda or self.resultado is not None or self.pensamiento is not None:
                return
            self.atendiendo_bebe = not self.atendiendo_bebe
            self.aviso = "Estás atendiendo al bebé." if self.atendiendo_bebe else "Volviste al examen."
            renpy.restart_interaction()

        def respirar(self):
            if not self.con_ayuda or self.bloqueado:
                return
            self.concentracion = min(100.0, self.concentracion + self.RECUPERACION_RESPIRAR)
            self.tiempo_restante = max(0.0, self.tiempo_restante - self.TIEMPO_RESPIRAR)
            self.aviso = "Respiraste y recuperaste concentración, pero gastaste 8 segundos."
            if self.tiempo_restante <= 0.0:
                self.resultado = "tiempo"
            renpy.restart_interaction()

        def actualizar(self, segundos):
            if self.resultado is not None:
                return
            # El reloj sigue funcionando durante TODO el examen, incluso
            # mientras Valeria atiende al bebé o un pensamiento bloquea la UI.
            self.tiempo_restante = max(0.0, self.tiempo_restante - segundos)
            if self.tiempo_restante <= 0.0:
                self.resultado = "tiempo"
                self.pensamiento = None
                renpy.restart_interaction()
                return

            if not self.con_ayuda:
                if self.atendiendo_bebe:
                    self.calma = min(100.0, self.calma + self.RECUPERACION_CALMA * segundos)
                else:
                    self.calma = max(0.0, self.calma - self.PERDIDA_CALMA * segundos)
                if self.calma <= 0.0:
                    self.estres_maestro = min(100.0, self.estres_maestro + self.SUBIDA_ESTRES_MAESTRO * segundos)
                    if self.estres_maestro >= 100.0:
                        self.resultado = "maestro"
            else:
                self.concentracion = max(0.0, self.concentracion - self.PERDIDA_CONCENTRACION * segundos)
                if self.pensamiento is not None:
                    self.pensamiento_restante -= segundos
                    if self.pensamiento_restante <= 0.0:
                        self.pensamiento = None
                        self.pensamiento_restante = 0.0
                        self.siguiente_pensamiento = renpy.random.uniform(8.0, 14.0)
                elif self.concentracion < self.UMBRAL_PENSAMIENTOS:
                    self.siguiente_pensamiento -= segundos
                    if self.siguiente_pensamiento <= 0.0:
                        self.pensamiento = renpy.random.choice(self.pensamientos)
                        # Tiempo suficiente para mostrar la frase a 30 cps,
                        # más una pausa. No se puede saltar manualmente.
                        frase_limpia = self.pensamiento.replace("{cps=30}", "")
                        self.pensamiento_restante = max(2.5, len(frase_limpia) / 30.0 + 0.9)
                else:
                    # No acumular una interrupción inminente al recuperarse.
                    self.siguiente_pensamiento = max(self.siguiente_pensamiento, 5.0)
            renpy.restart_interaction()


screen minijuego_examen(juego):
    modal True
    zorder 100
    add Solid("#171D30")

    timer juego.PASO repeat True action Function(juego.actualizar, juego.PASO)
    if juego.resultado is not None:
        timer 0.01 action Return(juego.resultado)

    text "EXAMEN FINAL - BASES DE DATOS":
        xpos 130
        ypos 35
        size 42
        color "#FFFFFF"

    text "PREGUNTA %d / %d       NOTA: %d / 100" % (min(juego.indice + 1, 10), 10, juego.puntos):
        xpos 130
        ypos 91
        size 26
        color "#D3E0F3"

    # RELOJ
    frame:
        xpos 1440
        ypos 35
        xsize 350
        background "#28334A"
        padding (18, 12)
        vbox:
            spacing 4
            text "TIEMPO RESTANTE" size 23 color "#D5DFFF"
            text juego.tiempo_formato:
                size 45
                if juego.tiempo_restante <= 60.0:
                    color "#FF7979"  
                else: 
                    color "#FFFFFF"

    # BARRA: Solo se presenta la que corresponde a apoyoVeronicaExamen.
    frame:
        xpos 130
        ypos 158
        xsize 1660
        background "#28334A"
        padding (22, 16)
        vbox:
            spacing 10
            if juego.con_ayuda:
                text "CONCENTRACIÓN DE VALERIA  —  %d %%" % int(juego.concentracion):
                    size 26
                    color "#D1E8FF"
                bar:
                    value StaticValue(juego.concentracion, 100.0)
                    xsize 1585
                    ysize 20
                    left_bar Solid("#6EA5CB" if juego.concentracion >= 30 else "#DFA152")
                    right_bar Solid("#41495B")
                if juego.concentracion < juego.UMBRAL_PENSAMIENTOS:
                    text "Concentración baja: los pensamientos pueden interrumpir el examen.":
                        color "#FFD59B"
                        size 22
            else:
                text "CALMA DEL BEBÉ  —  %d %%      TENSIÓN DEL MAESTRO: %d %%" % (int(juego.calma), int(juego.estres_maestro)):
                    size 26
                    color "#F3CEB4"
                bar:
                    value StaticValue(juego.calma, 100.0)
                    xsize 1585
                    ysize 20
                    left_bar Solid("#B97A54")
                    right_bar Solid("#574942")
                if juego.calma <= 0.0:
                    text "¡El bebé llora! La tensión del maestro está subiendo.":
                        color "#FF7979"
                        size 22
                elif juego.atendiendo_bebe:
                    text "Estás calmando al bebé; mientras tanto no puedes responder.":
                        color "#F3CEB4"
                        size 22

    # PANEL PRINCIPAL DE PREGUNTAS
    frame:
        xpos 130
        ypos 310
        xsize 1660
        ysize 515
        background "#253047"
        padding (35, 27)
        vbox:
            spacing 19
            text juego.seccion:
                color "#8ECAFF"
                size 24
            text juego.pregunta["titulo"]:
                color "#FFFFFF"
                size 34
            text juego.pregunta["enunciado"]:
                color "#ECF0F8"
                size 29
                xmaximum 1560

            if juego.pregunta["tipo"] == "opcion":
                for i, opcion in enumerate(juego.pregunta["opciones"]):
                    textbutton "%s) %s" % ("ABCD"[i], opcion):
                        xsize 800
                        ysize 48
                        background "#344966"
                        hover_background "#49698F"
                        sensitive not juego.bloqueado
                        action Function(juego.responder_opcion, i)
                        text_size 26
                        text_color "#FFFFFF"

            elif juego.pregunta["tipo"] == "ordenar":
                text "Pulsa los fragmentos en el orden correcto:":
                    size 24
                    color "#BCD0EC"
                hbox:
                    spacing 16
                    for parte in juego.pregunta["partes"]:
                        textbutton parte["texto"]:
                            background "#344966"
                            hover_background "#49698F"
                            sensitive not juego.bloqueado and parte["id"] not in juego.orden_elegido
                            action Function(juego.seleccionar_fragmento, parte["id"])
                            text_size 22
                            text_color "#FFFFFF"
                frame:
                    xsize 1510
                    background "#111B30"
                    padding (15, 12)
                    text juego.orden_mostrado:
                        size 23
                        color "#E6F2FF"
                hbox:
                    spacing 25
                    textbutton "DESHACER ÚLTIMO":
                        sensitive not juego.bloqueado and len(juego.orden_elegido) > 0
                        action Function(juego.deshacer_fragmento)
                        text_size 24
                    textbutton "COMPROBAR ORDEN":
                        sensitive not juego.bloqueado and len(juego.orden_elegido) == len(juego.pregunta["respuesta"])
                        action Function(juego.comprobar_orden)
                        text_size 24

            elif juego.pregunta["tipo"] == "corregir":
                if juego.token_elegido is None:
                    text "Paso 1: señala la parte que contiene el error:":
                        size 24
                        color "#BCD0EC"
                    hbox:
                        spacing 14
                        for i, token in enumerate(juego.pregunta["tokens"]):
                            textbutton token:
                                background "#344966"
                                hover_background "#49698F"
                                sensitive not juego.bloqueado
                                action Function(juego.elegir_token, i)
                                text_size 25
                                text_color "#FFFFFF"
                else:
                    text "Paso 2: elige la corrección correcta:":
                        size 24
                        color "#BCD0EC"
                    hbox:
                        spacing 24
                        for i, correccion in enumerate(juego.pregunta["correcciones"]):
                            textbutton correccion:
                                background "#344966"
                                hover_background "#49698F"
                                sensitive not juego.bloqueado
                                action Function(juego.corregir_token, i)
                                text_size 27
                                text_color "#FFFFFF"

            if juego.pista_visible:
                text "PISTA: " + juego.pregunta["pista"]:
                    size 23
                    color "#B9F1B8"

    # CONTROLES DE AYUDA Y OBSTÁCULOS
    textbutton "PISTA (%d)" % juego.pistas:
        xpos 130
        ypos 855
        xsize 240
        ysize 60
        background "#245D4A"
        hover_background "#347B61"
        sensitive not juego.bloqueado and juego.pistas > 0 and not juego.pista_visible
        action Function(juego.mostrar_pista)
        text_size 25
        text_color "#FFFFFF"
        text_xalign 0.5

    if juego.con_ayuda:
        textbutton "RESPIRAR (+18 % / -8 s)":
            xpos 420
            ypos 855
            xsize 450
            ysize 60
            background "#22566B"
            hover_background "#337E99"
            sensitive not juego.bloqueado
            action Function(juego.respirar)
            text_size 25
            text_color "#FFFFFF"
            text_xalign 0.5
    else:
        textbutton ("DEJAR DE ATENDER" if juego.atendiendo_bebe else "ATENDER AL BEBÉ"):
            xpos 420
            ypos 855
            xsize 450
            ysize 60
            if juego.atendiendo_bebe:
                background "#775138"  
            else:
                background "#503B31"
            hover_background "#946848"
            action Function(juego.alternar_bebe)
            text_size 25
            text_color "#FFFFFF"
            text_xalign 0.5

    text juego.aviso:
        xpos 130
        ypos 950
        size 24
        color "#FFC98F"
        xmaximum 1640

    # INTERRUPCIÓN INVOLUNTARIA: tapa todas las respuestas y controles.
    # No tiene botón de continuar ni puede quitarse con un clic.
    # El reloj y la barra siguen corriendo; se cierra automáticamente
    # al terminar el pensamiento completo (30 caracteres por segundo).
    if juego.pensamiento is not None and juego.resultado is None:
        button:
            xpos 0
            ypos 0
            xsize 1920
            ysize 1080
            background "#0A0E18CC"
            hover_background "#0A0E18CC"
            action NullAction()

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1240
            ysize 270
            background "#26344E"
            padding (43, 28)
            vbox:
                spacing 18
                text "PENSAMIENTOS DE VALERIA":
                    color "#FFCC9A"
                    size 29
                text juego.pensamiento_visible:
                    color "#FFFFFF"
                    size 34
                    xmaximum 1140
                text "No puedes responder hasta que Valeria recupere el hilo de sus ideas...":
                    size 21
                    color "#B7C4DA"


#
# RESULTADO DEL MINIJUEGO
#
label jugar_minijuego_examen:
    $ juego_examen = JuegoExamen(apoyoVeronicaExamen, estudios, estres, cuidado_bebe)
    call screen minijuego_examen(juego_examen)
    $ resultado_minijuego_examen = _return
    $ calificacionExamen = juego_examen.puntos

    # Umbrales PROVISIONALES: puedes cambiarlos según el criterio escolar.
    # resClase 1/3: actividades entregadas; 2/4: actividades incompletas.
    $ nota_minima_examen = 70 if resClase in (1, 3) else 90
    $ aproboMateria = (calificacionExamen >= nota_minima_examen and resultado_minijuego_examen != "maestro")
    return
