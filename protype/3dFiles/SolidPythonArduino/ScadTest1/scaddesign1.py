#libraries
from solid import *
from solid.utils import *

#3d designi
block = up(1.75)(cube([22,29,3.5],True))


#arduino board
usbhole = up(3.5)(cube([2.5,7.5,7],True))
board = up(3.75)(cube([2,23,7.5],True))
dupont = up(2.5)(cube([2.5,2.5,5],True))
pinhole = cube([29,1,1],True)

arduino = (usbhole) \
+ up(1)(left(2)(board)) \
+ left(4.25)(up(3.5)(forward((23/2)-1.25)(dupont))) \
+ left(4.25)(up(3.5)(back((23/2)-1.25)(dupont))) \
+ right(4)(up(2.25)(forward((23/2)-1.25)(pinhole))) \
+ right(4)(up(2.25)(back((23/2)-1.25)(pinhole)))

#button
square = up(10.5)(cube([6,6,3],True))
cylinderbutton = up(2.5)(cylinder(r=2,h=5,center=True))
button = down(5)(square) + cylinderbutton
# d = cube(1) + right(5)(sphere(5)) - cylinder(r=2, h=6)

d = block - left(4)(arduino) - down(2)(right(5)(button))

#render
scad_render_to_file(d, 'out_file.scad')
# scad_render_to_file(pinhole, 'out_file.scad')
# scad_render_to_file(arduino, 'out_file.scad')
# scad_render_to_file(dupont, 'out_file.scad')
# scad_render_to_file(button, 'out_file.scad')
# scad_render_to_file(block, 'out_file.scad')
