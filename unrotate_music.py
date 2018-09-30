#unskews document via algorithm described in 
# section 3.1 of C. Dalitz, G.K. Michalakis, C. Pranzas: 'Optical Recognition of Psaltic Byzantine Chant Notation.' International Journal of Document Analysis and Recognition 11, pp. 143-158 (2008)
import sys
from gamera.core import *
init_gamera()
img = load_image("process_img.png")
img = img.to_onebit()
angle_arr = img.rotation_angle_projections()#return [angle, accuracy]
print "rotation calculation complete"
img.rotate(angle_arr[0])
img.save_PNG("corrected_image")



