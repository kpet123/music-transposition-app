##Exercise 2.1
from gamera.core import *
from gamera.toolkits.skeleton import *
init_gamera()

#cannibalizing code, use 

im1 = Image(Point(0,0), Point(19,19), RBG)
im1.save_PNG("out.png")
#imTEST = im1.flip1()
#Draw two crossing green diagonals into the image using only 
#methods get and set in a loop
img = Image(im1)
right = 1
left = img.ncols-2

for y in range(img.nrows):
    #diagonal starting top left
    if right< img.ncols:
        img.set([right-1,y], RGBPixel(0,255,0))
        img.set([right,y], RGBPixel(0,0,255))
    #diagonal starting top right
    if left > -1:
        img.set([left,y], RGBPixel(0,0,255))
        img.set([left+1,y], RGBPixel(0,0,255))

    right+=1
    left-=1
img.save_PNG("out1.png")

##Number two
img2 = Image(im1)
img2.draw_line(Point(0,0), Point(20,20), RGBPixel(0,0,255), 2)
img2.draw_line(Point(0,20), Point(20,0), RGBPixel(0,0,255), 2)
img2.save_PNG("out2.png")





