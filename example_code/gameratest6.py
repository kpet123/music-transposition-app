##Excerise 3.1 tester file
from gamera.core import *
from gamera.toolkits.skeleton import *
init_gamera()


im1 = Image(Point(0,0), Point(19,19), ONEBIT)
im1.save_PNG("out.png")

imTEST = im1.flip1()
imTEST.save_PNG("flipped.png")
