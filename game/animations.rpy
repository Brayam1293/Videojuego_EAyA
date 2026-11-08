#
# SALIR DE PANTALLA
#

transform move_derecha(start_x, height, speed, end=2200):
    xpos start_x
    yalign height
    linear speed xpos end

#
# POSICION
#

transform pos(x, y):
    xalign x
    yalign y