'''
version of gameraStaffRemoval.py without gamera functions. 
input - png file of sheet music (sys.argv[0])
output - file with just staffs and file with music-staffs (filenames 
	     specified as sys.argv[1] and sys.argv[2], respectively

TODO: make it safe

'''

import sys
import im_functions #locally implemented version of gamera functions
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
import numpy as np

img = mpimg.imread(sys.argv[1]) #must be png
img = im_functions.format_doc(img)

proj_arr = im_functions.get_run_histogram(img, "vertical")
most_frequent_occurences = max(proj_arr) # number of occurences

#value corresponds to height of staff line, may also remove parts of slurs
value = np.where(proj_arr == most_frequent_occurences)[0]

img2 = np.copy(img) #isolate_run mutates original
verticalStaffs = im_functions.isolate_run(img2, value, 0, "vertical", thresh=1)

plt.imsave(sys.argv[2], verticalStaffs)

no_staff_raw = img - verticalStaffs

plt.imsave(sys.argv[3], no_staff_raw)




