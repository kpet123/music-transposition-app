#Base code taken from Gamera tutorial excercise 2.3, which highlighted staff lines in red 
import sys
from gamera.core import *
init_gamera()

img = load_image(sys.argv[1])
#new image img, so don't have to copy
img = img.to_onebit()
proj_arr = img.run_histogram("black", "vertical")

most_frequent_occurences = max(proj_arr) # number of occurences
print most_frequent_occurences

#value corresponds to height of staff line, may also remove parts of slurs
value = proj_arr.index(most_frequent_occurences)


verticalStaffs = img.image_copy()
#vertical Staffs will only have most frequent rune +- 1  
verticalStaffs.filter_short_runs(value-1, "black")
verticalStaffs.filter_tall_runs(value+1, "black")

img.subtract_images(verticalStaffs, in_place=True)

img.save_PNG(sys.argv[2])
#uncomment following section to get staffs for analysis
verticalStaffs.save_PNG("rawVerticalStaff.png")

#Get locations of staff lines
staff_arr = verticalStaffs.run_histogram("black", "horizontal")

#iterate thru array to find locations of staff lines, defined as more than 50%
i = verticalStaffs.ncols / 2




