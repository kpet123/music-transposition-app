#creates horizontal projection and pickles it because can't get skikit learn to work with python 2.7
#Gamera section
#Base code taken from Gamera tutorial excercise 2.3, which highlighted staff lines in red 
import sys
import cPickle
from gamera.core import *
init_gamera()

verticalStaffs = load_image("cleanwithstaff.png")
#new image img, so don't have to copy
verticalStaffs = verticalStaffs.to_onebit()

#Get locations of staff lines(this is wrong, should be projection)
hor_runs = verticalStaffs.projection_rows()

with open("projection.pkl", "w") as f :
    cPickle.dump(hor_runs, f, cPickle.HIGHEST_PROTOCOL)

