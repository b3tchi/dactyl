#libraries
from solid import scad_render_to_file
from solid import cube, cylinder
from solid.utils import up, down, left, right, forward, back

#for all possible items intellisense
from solid import *
from solid.utils import *

#global parameters
x = 18
y = 26
#3d designi

def block():
    body = up(2.75)(cube([y, x + 3,3.5],True))
    cover = up(0.5)(cube([y + 2 , x + 2 + 3, 1],True))
    return body + cover

#arduino board
def arduino():
    usbhole = up(2.5)(cube([2.5,7.5,9],True))
    board = up(3.75)(cube([2,x,7.5],True))
    smds = up(1.25)(cube([1.5,5,2.5],True))
    dupont = up(2.5)(cube([2.5,2.5,5],True))
    pinhole = cube([39,1,1],True)

    return (usbhole) \
    + up(1)(left(3.75)(smds)) \
    + up(1)(left(2)(board)) \
    + left(4.25)(up(3.5)(forward((x/2)-1.25)(dupont))) \
    + left(4.25)(up(3.5)(back((x/2)-1.25)(dupont))) \
    + left(5)(up(2.25)(forward((x/2)-1.25)(pinhole))) \
    + left(5)(up(2.25)(back((x/2)-1.25)(pinhole)))

#usb connector
def usbconn():
    usbhole2 = up(3.5)(cube([2.5,7.5,7],True))
    holewrap = up(9)(cube([7.5,11.5,7],True))
    return usbhole2 + holewrap


#button
def button():
    square = up(10.5)(cube([6,6,3],True))
    cylinderbutton = up(2.5)(cylinder(r=2,h=5,center=True))

    return down(5)(square) + cylinderbutton

    # d = cube(1) + right(5)(sphere(5)) - cylinder(r=2, h=6)

def final():
    return down(1)(block()) \
        - left(y / 2)( \
            right(21)(down(5.5)(usbconn())) \
            + right(4)(down(2)(button())) \
            + right(14)(arduino()) \
        )

#render
scad_render_to_file(final(), 'out_file.scad')
# scad_render_to_file(pinhole, 'out_file.scad')
# scad_render_to_file(usbconn, 'out_file.scad')
# scad_render_to_file(arduino(), 'out_file.scad')
# scad_render_to_file(dupont, 'out_file.scad')
# scad_render_to_file(smds, 'out_file.scad')
# scad_render_to_file(button, 'out_file.scad')
# scad_render_to_file(block, 'out_file.scad')
