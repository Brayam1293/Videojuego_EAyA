#
# MOVIMIENTO
#

transform move(start_x, height, speed, end=2200):
    xpos start_x
    yalign height
    linear speed xpos end

#
# POSICION
#

transform pos(x, y):
    xalign x
    yalign y

#
# VOLTEAR
#

transform flip:
    xzoom -1.0

#
# TRANSICIONES
#

define circleirisout = ImageDissolve(
    "images/circleiris.png",
    1.5,
    8
)

define circleirisin = ImageDissolve(
    "images/circleiris.png",
    1.5,
    8,
    reverse=True
)