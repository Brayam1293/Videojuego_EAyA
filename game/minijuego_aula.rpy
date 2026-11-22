# Minijuego de clase: escritura, bebé, Herneztino y estrés del maestro.
# Coloca este archivo en la carpeta game/ de tu proyecto Ren'Py.
# Prototipo para proyectos de escritorio (1920x1080).

# El resultado permite distinguir victoria, tiempo agotado o estrés del maestro.
# Nota: resumenTerminado y ayudaClase YA están declaradas en tu proyecto.
# No vuelvas a declararlas en este archivo.
default resultado_minijuego_aula = None

init python:
    class JuegoAula(object):
        # Ajusta estos valores para cambiar la dificultad.
        PASO = 0.1
        TIEMPO_LIMITE = 300.0  # 5 minutos; 420.0 equivale a 7 minutos.
        PERDIDA_CALMA = 3.0       # Puntos por segundo sin ayuda.
        PERDIDA_CON_AYUDA = 1.0   # Puntos por segundo mientras ayuda Herneztino.
        RECUPERACION_CALMA = 22.0 # Puntos por segundo al atender al bebé.
        SUBIDA_ESTRES = 7.0       # Puntos por segundo si el bebé llora.
        DURACION_AYUDA = 18.0     # Segundos de ayuda; se puede usar una vez.

        def __init__(self):
            # Resumen de MySQL: 14 oraciones, de dificultad progresiva.
            # Se respetan las mayúsculas, los acentos y la puntuación.
            self.lineas = [
                'MySQL es un sistema de gestión de bases de datos.',
                'Una base de datos reúne información organizada.',
                'Los datos se guardan en tablas con filas y columnas.',
                'Cada fila representa un registro de información.',
                'Cada columna almacena un dato del registro.',
                'Una clave primaria identifica cada registro.',
                'Una clave foránea permite relacionar tablas.',
                'SQL es el lenguaje para trabajar con los datos.',
                'SELECT permite consultar registros de una tabla.',
                'WHERE sirve para filtrar los resultados.',
                'INSERT agrega nuevos registros a la tabla.',
                'UPDATE modifica los registros existentes.',
                'DELETE elimina los registros indicados.',
                'Los respaldos ayudan a proteger los datos.'
            ]
            self.indice = 0
            self.tiempo_restante = self.TIEMPO_LIMITE
            self.texto = ""
            self.calma = 100.0
            self.estres = 0.0
            self.modo = "ninguno"  # ninguno / escribir / bebe
            self.ayuda_restante = 0.0
            self.ayuda_utilizada = False
            self.errores = 0
            self.aviso = "Selecciona ESCRIBIR para empezar."
            self.resultado = None  # None / victoria / tiempo / maestro

        @property
        def tiempo_formato(self):
            # Redondear hacia arriba evita mostrar 00:00 antes de acabar.
            segundos = int(self.tiempo_restante + 0.999)
            return "%02d:%02d" % (segundos // 60, segundos % 60)

        @property
        def linea_actual(self):
            if self.indice < len(self.lineas):
                return self.lineas[self.indice]
            return ""

        def abrir_escritura(self):
            if self.resultado is not None:
                return
            self.modo = "escribir"
            self.aviso = "Escribe exactamente la oración y presiona Enter."
            renpy.restart_interaction()

        def atender_bebe(self):
            if self.resultado is not None:
                return
            self.modo = "bebe"
            self.aviso = "Estás atendiendo al bebé."
            renpy.restart_interaction()

        def dejar_bebe(self):
            if self.resultado is None and self.modo == "bebe":
                self.modo = "ninguno"
                self.aviso = "Dejaste de atender al bebé."
                renpy.restart_interaction()

        def pedir_ayuda(self):
            if self.resultado is not None or self.ayuda_utilizada:
                return
            self.modo = "ninguno"
            self.ayuda_utilizada = True
            self.ayuda_restante = self.DURACION_AYUDA
            self.aviso = "¡Herneztino entretendrá al bebé un momento!"
            renpy.restart_interaction()

        def escribir(self, nuevo_texto):
            if self.resultado is not None or self.modo != "escribir":
                return

            # No comprobar ni borrar caracteres mientras el jugador escribe.
            # Puede usar Retroceso y corregir errores sin perder lo avanzado.
            # La validación se realiza solo cuando presiona Enter.
            self.texto = nuevo_texto

        def confirmar_linea(self):
            if self.resultado is not None or self.modo != "escribir":
                return

            if self.texto == self.linea_actual:
                self.indice += 1
                self.texto = ""
                if self.indice == len(self.lineas):
                    self.resultado = "victoria"
                else:
                    self.aviso = "¡Correcto! Ahora escribe la siguiente oración."
            else:
                self.texto = ""
                self.errores += 1
                self.aviso = "La oración no coincide. Se reinició para intentarlo otra vez."
            renpy.restart_interaction()

        def actualizar(self, segundos):
            if self.resultado is not None:
                return

            # El tiempo no se detiene por escribir, cuidar al bebé o pedir ayuda.
            self.tiempo_restante = max(0.0, self.tiempo_restante - segundos)
            if self.tiempo_restante <= 0.0:
                self.resultado = "tiempo"
                renpy.restart_interaction()
                return

            if self.ayuda_restante > 0.0:
                self.ayuda_restante = max(0.0, self.ayuda_restante - segundos)

            if self.modo == "bebe":
                self.calma = min(100.0, self.calma + self.RECUPERACION_CALMA * segundos)
            else:
                rapidez = self.PERDIDA_CON_AYUDA if self.ayuda_restante > 0 else self.PERDIDA_CALMA
                self.calma = max(0.0, self.calma - rapidez * segundos)

            # El estrés no disminuye automáticamente, pero deja de aumentar
            # en cuanto el bebé recupera un poco de calma.
            if self.calma <= 0.0:
                self.estres = min(100.0, self.estres + self.SUBIDA_ESTRES * segundos)
                if self.estres >= 100.0:
                    self.resultado = "maestro"

            renpy.restart_interaction()


    class EntradaAula(InputValue):
        # Mantiene sincronizado el campo de texto con el estado del minijuego.
        default = True

        def __init__(self, juego):
            self.juego = juego

        def get_text(self):
            return self.juego.texto

        def set_text(self, texto):
            self.juego.escribir(texto)

        def enter(self):
            self.juego.confirmar_linea()
            raise renpy.IgnoreEvent()


screen minijuego_aula(juego):
    modal True
    zorder 100

    # Fondo temporal; puede reemplazarse por el salón de clases.
    add Solid("#171D30")

    # Captura clics en espacios vacíos: deja de atender al bebé.
    button:
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        background None
        hover_background None
        action Function(juego.dejar_bebe)

    timer 0.1 repeat True modal True action Function(juego.actualizar, juego.PASO)

    # Finaliza el call screen al ganar, quedarse sin tiempo o agotar al maestro.
    if juego.resultado is not None:
        timer 0.01 action Return(juego.resultado)

    text "MINIJUEGO: EXPLICACIÓN EN CLASE":
        xalign 0.5
        ypos 28
        size 42
        color "#FFFFFF"

    # AZUL: estrés del maestro.
    frame:
        xpos 100
        ypos 110
        xsize 600
        background "#263250"
        padding (25, 18)
        vbox:
            spacing 10
            text "ESTRÉS DEL MAESTRO  —  %d %%" % int(juego.estres):
                color "#D1D9FF"
                size 28
            bar:
                value StaticValue(juego.estres, 100.0)
                xsize 540
                ysize 24
                left_bar Solid("#4752DB")
                right_bar Solid("#41495B")

    # RELOJ: límite de cinco minutos (configurable arriba).
    frame:
        xpos 1370
        ypos 110
        xsize 450
        background "#263250"
        padding (25, 16)
        vbox:
            spacing 8
            text "TIEMPO RESTANTE":
                color "#D1D9FF"
                size 26
            text juego.tiempo_formato:
                if juego.tiempo_restante <= 60.0:
                    color "#FF7777"
                else: 
                    color "#FFFFFF"
                size 44
            bar:
                value StaticValue(juego.tiempo_restante, juego.TIEMPO_LIMITE)
                xsize 390
                ysize 18
                left_bar Solid("#E6A356")
                right_bar Solid("#41495B")

    # Panel de escritura (ROJO).
    frame:
        xpos 285
        ypos 375
        xsize 1350
        ysize 345
        background "#253047"
        padding (35, 24)
        vbox:
            spacing 18
            hbox:
                spacing 35
                textbutton "ESCRIBIR / VOLVER AL DICTADO":
                    action Function(juego.abrir_escritura)
                    text_size 27
                    text_color "#FF7575"
                text "Oración %d de %d" % (min(juego.indice + 1, len(juego.lineas)), len(juego.lineas)):
                    color "#FFFFFF"
                    size 26
            if juego.resultado is None:
                text juego.linea_actual:
                    color "#FFFFFF"
                    size 33
                    xmaximum 1250

                if juego.modo == "escribir":
                    frame:
                        background "#12192B"
                        xsize 1200
                        ysize 58
                        padding (14, 7)
                        input:
                            value EntradaAula(juego)
                            length 140
                            copypaste False
                            size 29
                            color "#CDE6FF"
                else:
                    text "Haz clic en ESCRIBIR para activar el teclado.":
                        color "#B7C4D6"
                        size 27
            text juego.aviso:
                color "#FFC98F"
                size 24

    # VERDE: Herneztino.
    textbutton "PEDIR AYUDA A HERNEZTINO":
        xpos 380
        ypos 800
        xsize 440
        ysize 90
        background "#196440"
        hover_background "#26885A"
        sensitive not juego.ayuda_utilizada
        action Function(juego.pedir_ayuda)
        text_size 27
        text_color "#FFFFFF"
        text_xalign 0.5
        text_yalign 0.5

    if juego.ayuda_restante > 0.0:
        text "Ayuda: %d s" % int(juego.ayuda_restante + 0.99):
            xpos 390
            ypos 900
            color "#BAFBD1"
            size 25
    elif juego.ayuda_utilizada:
        text "Ayuda agotada":
            xpos 390
            ypos 900
            color "#B6BDC6"
            size 25

    # Botón para atender al BEBÉ (sustituible por un imagebutton de su sprite).
    textbutton "ATENDER AL BEBÉ":
        xpos 880
        ypos 800
        xsize 350
        ysize 90
        if juego.modo == "bebe":
            background "#775138"
        else:
            background "#503B31"
        hover_background "#946848"
        action Function(juego.atender_bebe)
        text_size 28
        text_color "#FFFFFF"
        text_xalign 0.5
        text_yalign 0.5

    # CAFÉ: calma del bebé.
    frame:
        xpos 1260
        ypos 775
        xsize 550
        background "#38302F"
        padding (23, 20)
        vbox:
            spacing 13
            text "CALMA DEL BEBÉ  —  %d %%" % int(juego.calma):
                color "#F3CEB4"
                size 27
            bar:
                value StaticValue(juego.calma, 100.0)
                xsize 490
                ysize 26
                left_bar Solid("#B97A54")
                right_bar Solid("#574942")
            if juego.calma <= 0.0:
                text "¡EL BEBÉ ESTÁ LLORANDO!":
                    color "#FF7979"
                    size 25
            elif juego.modo == "bebe":
                text "Recuperando la calma...":
                    color "#EFC5A7"
                    size 24
            else:
                text "La calma está disminuyendo.":
                    color "#EFC5A7"
                    size 24

    text "Errores: %d" % juego.errores:
        xpos 100
        ypos 1010
        color "#C7CEDB"
        size 25


# Llama a este label desde el capítulo que corresponda:
#     call jugar_minijuego_aula
#     if resultado_minijuego_aula == "victoria": ...
#     elif resultado_minijuego_aula == "tiempo": ...
#     elif resultado_minijuego_aula == "maestro": ...
#
# Las siguientes variables ya deben existir en tu proyecto:
#     default resumenTerminado = False
#     default ayudaClase = False
label jugar_minijuego_aula:
    $ juego_aula = JuegoAula()
    call screen minijuego_aula(juego_aula)
    $ resultado_minijuego_aula = _return
    $ resumenTerminado = (resultado_minijuego_aula == "victoria")
    $ ayudaClase = juego_aula.ayuda_utilizada
    return
