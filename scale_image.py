#scales image to standard size that will run quickly
#must include arugments in argv
from __future__ import division

TARGETCOLS = 1650
TARGETROWS = 1275
import cv2
import numpy as np
import sys


filename = sys.argv[1]
im = cv2.imread(filename, 0)
print len(im)
print len(im[0])
scaleX = TARGETCOLS/len(im)
scaleY = TARGETROWS/len(im[0])
print "scalex"
print scaleX
print "scaley"
print scaleY
scaled_im= cv2.resize(im, None, fx = scaleX, fy= scaleY,\
        interpolation= cv2.INTER_LINEAR)
print "enter name of output file"
output=sys.argv[2]
cv2.imwrite(output, scaled_im)

