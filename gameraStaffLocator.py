#OpenCV section






#Gamera section
#Base code taken from Gamera tutorial excercise 2.3, which highlighted staff lines in red 
import sys
from gamera.core import *
init_gamera()

verticalStaffs = load_image("rawVerticalStaff.png")
#new image img, so don't have to copy
verticalStaffs = verticalStaffs.to_onebit()

#Get locations of staff lines
hor_runs = verticalStaffs.run_histogram("black", "horizontal")

#iterate thru array to find locations of staff lines, defined as more than 50%
staff_arr = []
i = 0 #verticalStaffs.ncols / 2
while i < len(hor_runs):
    print hor_runs[i]
    if hor_runs[i] > 0:                     #if empty move on
        print 'LINE HERE'
    i+=1
print staff_arr



