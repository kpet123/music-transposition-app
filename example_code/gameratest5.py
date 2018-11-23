from gamera.core import *
init_gamera()
from gamera.toolkits.skeleton import *
img = Image(Point(0,0), Point(9,9))
img.draw_filled_rect(Point(3,3), Point(5,5), 1) 
print img.countvolume()

