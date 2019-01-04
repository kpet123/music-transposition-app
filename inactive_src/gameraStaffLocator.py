###erode then figure out locations
#OpenCV section
import cv2
import numpy as np

imageName = "rawVerticalStaff.png"
im = cv2.imread(imageName, 0)
ERODE_DIMENSIONS = (1,10)
kernel = np.ones(ERODE_DIMENSIONS, np.uint8)
ITERATIONS = 1
im = ~im
im = cv2.dilate(im, kernel, iterations = ITERATIONS)
cv2.imshow("Image", im)
cv2.waitKey(0)
cv2.imwrite("VerticalStaff.png", im)

#Gamera section
#Base code taken from Gamera tutorial excercise 2.3, which highlighted staff lines in red 
import sys
from gamera.core import *
init_gamera()

verticalStaffs = load_image("VerticalStaff.png")
#new image img, so don't have to copy
verticalStaffs = verticalStaffs.to_onebit()

#Get locations of staff lines(this is wrong, should be projection)
hor_runs = verticalStaffs.run_histogram("black", "horizontal")

#iterate thru array to find locations of staff lines, defined as more than 50%
staff_arr = []
i = verticalStaffs.ncols / 2
while i < len(hor_runs):
    print hor_runs[i]
    if hor_runs[i] > 0:                     #if empty move on
        print 'LINE HERE'
    i+=1
print staff_arr



