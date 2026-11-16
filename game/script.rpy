# 
# ENTRE APUNTES Y AVENTURAS
# ARCHIVO PRINCIPAL
# 

init python:
    import math

    def mascara_circular(t, st, at):
        ancho = 1920
        alto = 1080

        superficie = renpy.display.pgrender.surface(
            (ancho, alto), True
        )

        superficie.fill((255, 255, 255, 255))

        return renpy.display.render.Render(ancho, alto)

label start:

    scene black
    with fade

    narrador "Entre Apuntes y Aventuras"

    narrador "Una historia sobre una joven estudiante, una madre y sus sueños."

    pause 1.0

    jump nivel_1